# Securing Key Vault Access

## Reference

Key Vaults are full of sensitive data, so securing access to them is paramount. You can use Azure AD to restrict access, which limits what users can do in the Portal and through the az command line interface. You also need to secure the Key Vault internally to ensure that only the components which need to read the data actually have access to the vault. In this lab we'll see how to restrict Key Vault access using virtual networks and Azure managed identities, implementing defense in depth with both network-level and identity-based security. The best practices documentation covers everything from access control to backup strategies and audit logging. Managed identities provide a secure way for Azure resources to authenticate to other Azure services without storing credentials. The command line interface gives you complete control through the az vm identity and az keyvault network-rule commands, which we'll be using throughout these exercises.

## Create RG, KeyVault and Secret

Let's start by creating a Key Vault in a new Resource Group.

**Create the Resource Group**: We're creating a resource group named "labs-keyvault-access" in the East US region with the standard course tags. This will contain all the resources we create in this lab.

**Create the Key Vault**: We're creating a Key Vault using the keyvault create command. Remember that the Key Vault name must be globally unique across all of Azure, so choose something like your initials plus a descriptive term plus some numbers.

**Create a Secret**: Let's add a secret to verify everything is working. We're creating a secret named "secret01" with the value "azure-labs" using the keyvault secret set command.

**Verify Access**: We're confirming we can read it back again from our own machine using keyvault secret show with the query parameter to extract just the value. Perfect - we can see our secret value because we created the account and have all permissions automatically.

**Check Access Policies**: Open the Key Vault in the Portal and navigate to the Access policies tab. You'll see your account listed with all permissions granted. This is important - access policies control what authenticated principals can do with the vault's contents. You need two things to access a Key Vault: network connectivity and authorization via access policies or RBAC.

**Understanding Principals**: Can you give someone outside your organization access to your Key Vault, for example by adding their external email address? Try adding a new access policy and entering an external email - you'll see no results found. The list of principals you can use is limited to your own Azure Active Directory account, and external identities are in different AD accounts. If you wanted to give external access, you'd need to add them as an external ID in your Azure Active Directory first.

Azure talks about principals when you're applying security. That's a general term which could refer to a user with a Microsoft Account, a group of users, a system identity used by an Azure resource, or a managed identity for a resource which is managed by Azure. You need to consider all these options because you don't want any unauthorized access to your secrets.

Before a principal can authenticate, they need network access to the Key Vault, which you can also restrict using network rules.

---

## Restrict Access to VNet

We'll create a Virtual Network and run a VM in the network. We'll set up Key Vault so it can only be used by the VM, demonstrating network-level security.

**Create the Virtual Network**: We're starting with a VNet using the address prefix 10.10.0.0/16. This creates the virtual network container for our resources using the network vnet create command.

**Create the Subnet**: We're adding a subnet with the address prefix 10.10.1.0/24 where we'll deploy our VM. The subnet is a subdivision of the VNet's address space using the network vnet subnet create command.

**Try to Add Network Rule**: Let's attempt to use the keyvault network-rule add command to give access to the Key Vault from any services running in the subnet. If you try this now, you'll see an error about service endpoints.

**Understanding Service Endpoints**: Other services aren't allowed to route traffic to subnets unless you explicitly allow them with a service endpoint. Service endpoints are special routing rules that keep traffic on the Azure backbone network rather than going through the public internet, improving both security and performance. This sets the subnet so Key Vault resources are allowed into the subnet.

**Add Service Endpoint**: We're updating the subnet with the service-endpoints parameter set to Microsoft.KeyVault. Any Azure resources which need access to a subnet have to have a service endpoint set up, but this only needs to be done once for each service type that's going to use the subnet.

**Add Network Rule**: Now we can add the network rule using keyvault network-rule add with the VNet name, subnet name, and Key Vault name. This succeeds because the service endpoint is now configured.

**Verify Service Endpoint**: Open your VNet in the Portal, select the subnet in the Subnets tab, and you'll see Key Vault listed in the Service Endpoints. This confirms the configuration.

**Test Access**: Try and print the secret value from your local machine again using keyvault secret show. Your machine is not in the VNet, but you'll notice you can still print the secret. Why is that?

**Check Default Action**: Open the Key Vault in the Portal and browse to Networking. You'll see the default value "Allow public access from all networks" is selected. Adding a network rule doesn't change this default - it just adds an exception to the allow list. You need to explicitly deny public access.

**Update Default Action**: We're updating the Key Vault so access is denied unless there's a network rule to allow it using keyvault update with the default-action parameter set to Deny.

**Test Denied Access**: Now try to print the secret again. This will fail with a forbidden error. Your Key Vault is locked down now, so only resources in the subnet can use it. You're being blocked at the network layer, before authentication even happens.

---

## Create a VM with access to the KeyVault

Now we'll create a VM in the subnet to prove we can still access the secrets. This is a simple Ubuntu Server VM demonstrating that network access and identity-based access are two separate security layers.

**Understanding the Scripts**: We're using two scripts for this exercise. The setup.sh script installs Python and the libraries we need to use Key Vault, and the read-secret.py script is the Python program we'll run on the machine to test access to the Key Vault.

**Create the VM**: We're creating the VM with the setup script using vm create with parameters for resource group, name, image set to UbuntuLTS, the VNet name, subnet name, and custom-data pointing to the setup script. This takes a few minutes to complete.

**Connect to the VM**: When the VM is ready, we're connecting via SSH using the VM's public IP address that was shown in the creation output.

**Download the Python Script**: Inside the VM, we're downloading the Python script using curl from the course GitHub repository.

**Try to Read Secret**: Let's run it with python3. This will fail with an authentication error. This is the crucial point - the VM is inside the subnet which has access to the Key Vault at the network level, but to consume a secret you still need to use an authenticated Azure principal. Network access and authorization are two separate layers.

**Add Managed Identity**: In a new terminal on your local machine, we're adding a system-generated managed identity to the VM using vm identity assign. The output from this command contains the managed identity ID in the systemAssignedIdentity field. This ID is what we need to grant permissions.

**Grant Key Vault Access**: We're giving the identity access to read secrets using keyvault set-policy with secret-permissions set to "get", the object-id set to the systemAssignedIdentity from the previous command, and the vault name.

**Verify Access Works**: Now repeat the Python script in your VM shell session with python3. You'll see the secret value successfully displayed. The VM authenticates with Managed Identity, so there's no credential to supply for accessing Key Vault - Azure handles the entire authentication flow securely behind the scenes.

**Understanding Managed Identities**: Managed identities are only used within Azure services to authenticate with other Azure services. When the Python script runs, it uses Azure's instance metadata service to get a token for the managed identity. That token is then used to authenticate with Key Vault. There's no password or credential stored anywhere. Check the access policies for your Key Vault in the Portal and you'll see the managed identity listed with get permissions on secrets.

---

## Lab

Key Vault has a soft-delete policy by default - if you delete a secret by accident, then you can restore it.

**The Scenario**: Try that with the secret01 secret. Delete it and then try to recreate it with a new value. What happens? What do you need to do to make that work?

**Your Task**: Can you figure out how to successfully recreate the secret so that in the VM your Python script prints the new value of the secret?

**Hints**: When you delete a secret with soft-delete enabled, it's not immediately gone - it enters a deleted state. You can't create a new secret with the same name until you either recover or purge the deleted secret. Explore the keyvault secret commands to find options for listing deleted secrets, recovering them, or purging them permanently. Remember that soft-delete is about preventing accidental data loss, so Azure makes you acknowledge the deletion before you can reuse the name.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up resource groups.

This removes the resource group, the Key Vault with its soft-deleted secrets, the virtual network with its service endpoint configuration, and the VM with its managed identity - everything we created in this lab.
