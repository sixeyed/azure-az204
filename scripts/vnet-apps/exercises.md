# Securing Apps with Key Vault and Virtual Networks - Exercises

## Exercise 1: Create Resource Group, VNet and Subnet

Let's begin by creating our foundational resources. We'll start with a resource group to contain all our resources, and then create a Virtual Network with a subnet.

```bash
az group create -n labs-vnet-apps --tags courselabs=azure
```

This creates our resource group. The tag helps us track resources that belong to this course.

Now let's create a Virtual Network with an address space of 10.30.0.0/16:

```bash
az network vnet create -g labs-vnet-apps -n vnet1 --address-prefix "10.30.0.0/16"
```

And within that VNet, we'll create a subnet with the address prefix 10.30.1.0/24:

```bash
az network vnet subnet create -g labs-vnet-apps --vnet-name vnet1 -n subnet1 --address-prefix "10.30.1.0/24"
```

There's nothing particularly new here if you've worked with VNets before. The interesting thing is that we're not actually going to deploy any resources into this VNet. Instead, we'll use it as a secure bridge for communication between services. This is a common pattern in Azure when working with PaaS services that don't run inside VNets.

## Exercise 2: Create Storage Account and KeyVault

Our application needs Blob Storage to persist data. Let's create a storage account. Remember to use a unique name:

```bash
az storage account create -g labs-vnet-apps --sku Standard_ZRS -n <sa-name>
```

We're using Zone-Redundant Storage here for durability. The application code will create the blob container it needs, so we don't need to do that manually.

Now let's get the connection string for this storage account:

```bash
az storage account show-connection-string -o tsv -g labs-vnet-apps --name <sa-name>
```

This connection string gives complete access to everything in the Storage Account. It's extremely sensitive - anyone with this key can read, write, and delete all your data. This is exactly the kind of secret we need to protect.

Let's create an Azure Key Vault to store it securely:

```bash
az keyvault create -g labs-vnet-apps -n <kv-name>
```

Again, use a globally unique name for your Key Vault. Now we'll store the connection string as a secret. Notice the secret name uses double dashes - this is a naming convention that the .NET configuration system understands:

```bash
az keyvault secret set --name 'ConnectionStrings--AssetsDb' --vault-name <kv-name> --value "<connection-string>"
```

Let's verify we can read this secret from our machine:

```bash
az keyvault secret show --name 'ConnectionStrings--AssetsDb' --vault-name <kv-name>
```

You should see the secret value returned. Right now, this Key Vault is accessible from anywhere on the internet if you have the right permissions. There's no need for this secret to be accessible outside of Azure, so let's lock it down.

## Exercise 3: Restrict Access to Key Vault

To restrict Key Vault to only be accessible from our subnet, we first need to enable service endpoints on the subnet. Service endpoints allow Azure services to communicate privately over the Azure backbone network:

```bash
az network vnet subnet update -g labs-vnet-apps --vnet-name vnet1 --name subnet1 --service-endpoints Microsoft.KeyVault Microsoft.Storage
```

We're enabling endpoints for both Key Vault and Storage because we'll secure both services.

Now let's add our subnet to the Key Vault's network rules:

```bash
az keyvault network-rule add --vnet-name vnet1 --subnet subnet1 -g labs-vnet-apps --name <kv-name>
```

And set the default action to deny all other traffic:

```bash
az keyvault update --default-action 'Deny' -g labs-vnet-apps -n <kv-name>
```

Let's view our network rules:

```bash
az keyvault network-rule list -g labs-vnet-apps --name <kv-name>
```

Now try to read the secret again using the CLI or the Azure Portal. It may take a few minutes for the rules to propagate, but soon you should find that access is denied. Your local machine isn't on the allowed subnet, so you can't access the Key Vault anymore. This is exactly what we want - the secret is now protected.

## Exercise 4: Deploy and Configure the Web Application

Our application is a .NET 6 web site, which is perfect for Azure App Service. An important thing to understand about App Services: they don't run inside Virtual Networks. They're platform services designed to be publicly accessible. However, we can still secure them through VNet integration.

Let's deploy the application:

```bash
cd src/asset-manager

az webapp up -g labs-vnet-apps --plan app-plan-02 --os-type Linux --runtime dotnetcore:6.0 --sku B1 -n <app-name>
```

This command packages up the application and deploys it to a new or existing App Service plan. Use a unique name for your app.

Now we need to configure the application. We'll set some app settings that tell it to use Blob Storage and to fetch the connection string from Key Vault:

```bash
az webapp config appsettings set -g labs-vnet-apps --settings Database__Api=BlobStorage KeyVault__Enabled=true KeyVault__Name=<kv-name> -n <app-name>
```

If you browse to the app now, you'll see an error page. Let's investigate why.

## Exercise 5: Troubleshooting Authentication Issues

Open the Advanced Tools for your web app in the Azure Portal - this launches the Kudu service. From there, open the Log stream and wait patiently. The app will keep restarting because it's encountering an error.

Eventually, you'll see an error message about a Forbidden response from Key Vault. The error tells us that the application's identity doesn't have permission to list secrets on the Key Vault. This makes sense - we haven't given the app any identity yet.

App Service supports managed identities, which means it can authenticate with other Azure services without storing any credentials. Let's enable this:

```bash
az webapp identity assign -g labs-vnet-apps -n <app-name>
```

The output includes a principalId - this is the ID of the managed identity. Copy this value, and then grant that identity permission to read secrets from Key Vault:

```bash
az keyvault set-policy --secret-permissions get list --object-id "<principalId>" -n <kv-name>
```

Try the app again. It will still fail, but with a different error.

## Exercise 6: Troubleshooting Network Access Issues

Back in the log stream, you'll see a new error. This time it says "Client address is not authorized and caller is not a trusted service" with a "ForbiddenByFirewall" error code.

Now the App Service is using an authorized identity, so authentication works. But the network call is being blocked because it's not coming from our trusted subnet.

We have a couple of options here. We could get the outbound IP addresses of the webapp and add them to the Key Vault firewall. But IP addresses can change, which would break our application.

The better solution is VNet integration. When we integrate the Web App with our VNet, its outbound calls to Azure services will go through the subnet, which has access to Key Vault:

```bash
az webapp vnet-integration add --vnet vnet1 --subnet subnet1 -g labs-vnet-apps -n <app-name>
```

Let's check the configuration:

```bash
az webapp show -g labs-vnet-apps -n <app-name>
```

Wait a few moments for the changes to take effect, then try the app again. This time it should work! The app can now:
1. Use its managed identity to authenticate with Key Vault
2. Make the call through the VNet subnet which has access to Key Vault
3. Retrieve the connection string for Blob Storage
4. Connect to Blob Storage and read/write data

## Exercise 7: Lab Challenge - Secure the Storage Account

There's still a security gap in our architecture. The Storage Account is still open to the internet. Just like Key Vault, Storage Accounts can't be deployed inside a VNet, but they can be restricted using network rules.

Your challenge is to configure the Storage Account so that only services using our subnet have access, just like we did with Key Vault.

Here are some hints to get you started:
- Storage Accounts have similar network rule capabilities to Key Vault
- You'll need to add a network rule that allows the subnet
- Don't forget to set the default action appropriately
- The app will need to be able to access the storage account through the VNet integration

If you complete this successfully, you'll have a fully secured application where all communication happens through controlled network paths and all authentication uses managed identities - no secrets exposed, no public access to resources.

This is the gold standard for secure Azure applications!
