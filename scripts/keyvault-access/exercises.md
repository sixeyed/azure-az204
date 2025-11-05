# Securing Key Vault Access - Exercise Walkthrough

## Exercise 1: Create Key Vault and Secret

Let's start by creating a new Resource Group for this lab. We'll use the East US region and add our standard course labs tag.

```
az group create -n labs-keyvault-access --tags courselabs=azure -l eastus
```

Now we'll create the Key Vault. Remember, Key Vault names must be globally unique, so you'll need to choose your own unique name. I'll use a placeholder "my-secure-vault" in the examples.

```
az keyvault create -l eastus -g labs-keyvault-access -n my-secure-vault
```

The Key Vault is created. Now let's add a secret to it. We'll create a secret called "secret01" with the value "azure-labs".

```
az keyvault secret set --name secret01 --value azure-labs --vault-name my-secure-vault
```

Let's verify we can read it back. We'll use the query parameter to extract just the value.

```
az keyvault secret show --name secret01 -o tsv --query "value" --vault-name my-secure-vault
```

Perfect - we can see our secret value. Right now, you have full access because you created the Key Vault. Let's look at the access policies in the Azure Portal.

Open your Key Vault and navigate to the Access policies tab. You'll see your account listed with all permissions granted. This is important - access policies control what authenticated principals can do with the vault's contents.

Notice that you can't easily grant access to users outside your Azure Active Directory. Azure security is tied to your organization's identity provider. This is by design - it ensures only authorized identities from your organization can be granted access.

## Exercise 2: Restrict Access to Virtual Network

Now we'll see how network-level restrictions work. We'll create a virtual network and configure the Key Vault so it can only be accessed from that network.

First, let's create a virtual network with the address space 10.10.0.0/16.

```
az network vnet create -g labs-keyvault-access -n vnet1 --address-prefix "10.10.0.0/16"
```

Now we'll add a subnet with the address prefix 10.10.1.0/24.

```
az network vnet subnet create -g labs-keyvault-access --vnet-name vnet1 -n subnet1 --address-prefix "10.10.1.0/24"
```

Now let's try to add a network rule to allow Key Vault access from this subnet. If we try this command right now:

```
az keyvault network-rule add -g labs-keyvault-access --vnet-name vnet1 --subnet subnet1 --name my-secure-vault
```

This will fail with an error about service endpoints. Before Azure services like Key Vault can communicate with resources in a subnet, the subnet needs a service endpoint configured.

Let's add the Key Vault service endpoint to our subnet:

```
az network vnet subnet update -g labs-keyvault-access --vnet-name vnet1 -n subnet1 --service-endpoints 'Microsoft.KeyVault'
```

Service endpoints are configured once per service type, per subnet. Now let's add the network rule again:

```
az keyvault network-rule add -g labs-keyvault-access --vnet-name vnet1 --subnet subnet1 -n my-secure-vault
```

This succeeds. Let's verify the service endpoint in the Portal. Open your virtual network, go to the Subnets tab, and select subnet1. You'll see Microsoft.KeyVault listed in the Service Endpoints section.

Now here's an important point. Let's try to access our secret from our local machine again:

```
az keyvault secret show --name secret01 -o tsv --query "value" --vault-name my-secure-vault
```

It still works! Why is that? Open the Key Vault in the Portal and go to the Networking section. You'll see the default setting is "Allow public access from all networks". Adding a network rule doesn't automatically deny other access.

Let's change that. We'll update the Key Vault's default action to Deny:

```
az keyvault update --default-action Deny -g labs-keyvault-access -n my-secure-vault
```

Now try to read the secret again:

```
az keyvault secret show --name secret01 -o tsv --query "value" --vault-name my-secure-vault
```

This time it fails with a forbidden error. Your Key Vault is now locked down - only resources in the subnet can reach it over the network.

## Exercise 3: Create VM with Managed Identity

Now we'll prove that resources in the subnet can still access the Key Vault. We'll create a virtual machine in the subnet and configure it to read secrets.

We'll create an Ubuntu server and use a custom data script to install the necessary tools. This setup script installs Python and the Azure SDK libraries we need.

```
az vm create -g labs-keyvault-access -n vm01 --image UbuntuLTS --vnet-name vnet1 --subnet subnet1 --custom-data @labs/keyvault-access/scripts/setup.sh
```

This will take a few minutes. When it completes, you'll see the VM's public IP address in the output. Let's connect to the VM via SSH. I'll use a placeholder IP address:

```
ssh azureuser@20.30.40.50
```

Once connected, let's download a Python script that will attempt to read our secret:

```
curl -o read-secret.py https://raw.githubusercontent.com/courselabs/azure/main/labs/keyvault-access/scripts/read-secret.py
```

Now let's try to run it:

```
python3 read-secret.py
```

This fails with an authentication error. This is important - the VM is inside the subnet, so it can reach the Key Vault over the network. But it still needs to authenticate as an authorized principal to actually read secrets.

Let's fix this by adding a managed identity. Open a new terminal window on your local machine and run:

```
az vm identity assign -n vm01 -g labs-keyvault-access
```

This command creates a system-assigned managed identity for the VM. The output includes a systemAssignedIdentity field with the identity's object ID. Copy this value - we'll need it.

Now let's grant this identity permission to read secrets from our Key Vault. Replace the placeholder with your actual object ID:

```
az keyvault set-policy --secret-permissions get --object-id 12345678-1234-1234-1234-123456789abc --name my-secure-vault
```

Now go back to your VM SSH session and run the Python script again:

```
python3 read-secret.py
```

Success! This time it prints the secret value. Let's review what happened.

The VM now has a managed identity that Azure manages automatically. When the Python script runs, it uses Azure's metadata service to get a token for the managed identity. That token is then used to authenticate with Key Vault. There's no password or credential stored anywhere - Azure handles the entire authentication flow securely.

If you check the Access policies in the Portal, you'll see the managed identity listed with get permissions on secrets.

## Lab Challenge: Soft Delete and Recovery

Now it's your turn to explore. Key Vault has a soft-delete feature enabled by default. Try deleting the secret01 secret, then attempt to recreate it with a new value. What happens? What do you need to do to make it work? And finally, can you verify from the VM that your Python script reads the new value?

Take some time to work through this challenge. The hints and solution files are available if you need help.

## Cleanup

When you're done, clean up all the resources by deleting the resource group:

```
az group delete -y --no-wait -n labs-keyvault-access
```

This removes the resource group, the Key Vault, the virtual network, and the VM - everything we created in this lab.
