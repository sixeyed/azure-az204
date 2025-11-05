# Securing Key Vault Access - Exercise Walkthrough

## Exercise 1: Create Key Vault and Secret

Let's start by creating a new Resource Group for this lab. We'll use the East US region and add our standard course labs tag using the group create command.

Now we'll create the Key Vault. Remember, Key Vault names must be globally unique across all of Azure, so you'll need to choose your own unique name. Think of something like your initials plus a descriptive term plus some numbers.

We're using the keyvault create command with parameters for location, resource group, and the vault name. The Key Vault is created. Now let's add a secret to it. We'll create a secret called "secret01" with the value "azure-labs" using the keyvault secret set command with the name, value, and vault-name parameters.

Let's verify we can read it back. We'll use the keyvault secret show command with the query parameter to extract just the value, and table output format for clean display.

Perfect - we can see our secret value. Right now, you have full access because you created the Key Vault. Let's look at the access policies in the Azure Portal.

Open your Key Vault and navigate to the Access policies tab. You'll see your account listed with all permissions granted. This is important - access policies control what authenticated principals can do with the vault's contents. You need two things to access a Key Vault: network connectivity and authorization via access policies or RBAC.

Notice that you can't easily grant access to users outside your Azure Active Directory. Azure security is tied to your organization's identity provider. This is by design - it ensures only authorized identities from your organization can be granted access. No sharing passwords, no external accounts - everything goes through Azure AD authentication.

## Exercise 2: Restrict Access to Virtual Network

Now we'll see how network-level restrictions work. We'll create a virtual network and configure the Key Vault so it can only be accessed from that network.

First, let's create a virtual network with the address space 10.10.0.0 slash 16. We're using the network vnet create command with parameters for the resource group, name, and address prefix.

Now we'll add a subnet with the address prefix 10.10.1.0 slash 24 using the network vnet subnet create command.

Now let's try to add a network rule to allow Key Vault access from this subnet. If we try the keyvault network-rule add command right now, pointing to our virtual network and subnet, this will fail with an error about service endpoints.

Before Azure services like Key Vault can communicate with resources in a subnet, the subnet needs a service endpoint configured. Service endpoints are special routing rules that keep traffic on the Azure backbone network rather than going through the public internet. This improves security and performance.

Let's add the Key Vault service endpoint to our subnet using the network vnet subnet update command with the service-endpoints parameter set to Microsoft dot KeyVault.

Service endpoints are configured once per service type, per subnet. Now let's add the network rule again using the keyvault network-rule add command.

This succeeds. Let's verify the service endpoint in the Portal. Open your virtual network, go to the Subnets tab, and select subnet1. You'll see Microsoft dot KeyVault listed in the Service Endpoints section.

Now here's an important point. Let's try to access our secret from our local machine again using the keyvault secret show command.

It still works! Why is that? Open the Key Vault in the Portal and go to the Networking section. You'll see the default setting is "Allow public access from all networks". Adding a network rule doesn't automatically deny other access - it just adds an exception to the list. You need to explicitly change the default action to deny public access.

Let's change that. We'll update the Key Vault's default action to Deny using the keyvault update command with the default-action parameter.

Now try to read the secret again with the same show command.

This time it fails with a forbidden error. Your Key Vault is now locked down - only resources in the subnet can reach it over the network. You're being blocked at the network layer, before authentication even happens.

## Exercise 3: Create VM with Managed Identity

Now we'll prove that resources in the subnet can still access the Key Vault. We'll create a virtual machine in the subnet and configure it to read secrets.

We'll create an Ubuntu server and use a custom data script to install the necessary tools. This setup script installs Python and the Azure SDK libraries we need. The custom-data parameter accepts a file path with an @ symbol prefix.

We're using the vm create command with parameters for resource group, name, image, virtual network, subnet, and custom-data. This will take a few minutes. When it completes, you'll see the VM's public IP address in the output. Let's connect to the VM via SSH using that IP address.

Once connected, let's download a Python script that will attempt to read our secret. We're using curl to download it from the course GitHub repository.

Now let's try to run it using python3.

This fails with an authentication error. This is important - the VM is inside the subnet, so it can reach the Key Vault over the network. The network-level check passes. But it still needs to authenticate as an authorized principal to actually read secrets. Network access and authorization are two separate layers of security.

Let's fix this by adding a managed identity. Open a new terminal window on your local machine and run the vm identity assign command with the VM name and resource group.

This command creates a system-assigned managed identity for the VM. The output includes a systemAssignedIdentity field with the identity's object ID. Copy this value - we'll need it to set up permissions.

Now let's grant this identity permission to read secrets from our Key Vault. We're using the keyvault set-policy command with parameters for secret-permissions set to "get", the object-id of our managed identity, and the vault name.

Now go back to your VM SSH session and run the Python script again.

Success! This time it prints the secret value. Let's review what happened.

The VM now has a managed identity that Azure manages automatically. When the Python script runs, it uses Azure's instance metadata service to get a token for the managed identity. That token is then used to authenticate with Key Vault. There's no password or credential stored anywhere - Azure handles the entire authentication flow securely behind the scenes.

If you check the Access policies in the Portal, you'll see the managed identity listed with get permissions on secrets. This is how you securely connect applications to Key Vault without embedding credentials in your code.

## Lab Challenge: Soft Delete and Recovery

Now it's your turn to explore. Key Vault has a soft-delete feature enabled by default. Try deleting the secret01 secret, then attempt to recreate it with a new value. What happens? What do you need to do to make it work? And finally, can you verify from the VM that your Python script reads the new value?

Take some time to work through this challenge. The hints and solution files are available if you need help. This challenge explores an important Key Vault feature that prevents accidental data loss.

## Cleanup

When you're done, clean up all the resources by deleting the resource group using the group delete command with the yes and no-wait flags.

This removes the resource group, the Key Vault, the virtual network, and the VM - everything we created in this lab. The no-wait flag means the command returns immediately while the deletion happens in the background.
