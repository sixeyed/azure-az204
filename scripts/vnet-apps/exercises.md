# Securing Apps with Key Vault and Virtual Networks - Exercises

## Exercise 1: Create Resource Group, VNet and Subnet

Let's begin by creating our foundational resources. We'll start with a resource group to contain all our resources, and then create a Virtual Network with a subnet.

We're running az group create with the name "labs-vnet-apps", adding the "courselabs=azure" tag to help us track resources that belong to this course.

This creates our resource group. The tag helps us identify and manage resources associated with this lab later.

Now let's create a Virtual Network with an address space. We're running az network vnet create with the resource group "labs-vnet-apps", network name "vnet1", and address prefix "10.30.0.0/16". This gives us a private IP range for our virtual network.

And within that VNet, we'll create a subnet using az network vnet subnet create with the resource group, VNet name "vnet1", subnet name "subnet1", and address prefix "10.30.1.0/24". This subnet will be our secure communications bridge.

There's nothing particularly new here if you've worked with VNets before. The interesting thing is that we're not actually going to deploy any VMs or traditional compute resources into this VNet. Instead, we'll use it as a secure bridge for communication between PaaS services. This is a common pattern in Azure when working with platform services that don't run inside VNets natively.

## Exercise 2: Create Storage Account and KeyVault

Our application needs Blob Storage to persist data, so let's create a storage account. Remember to use a unique name that's globally unique across all of Azure.

We're running az storage account create with the resource group "labs-vnet-apps", SKU set to Standard_ZRS for zone-redundant storage which provides good durability, and a unique name you'll need to provide.

We're using Zone-Redundant Storage here which replicates data across multiple availability zones for durability. The application code will create the blob container it needs automatically, so we don't need to manually create that.

Now let's get the connection string for this storage account. We're running az storage account show-connection-string with tab-separated value output, the resource group "labs-vnet-apps", and storage account name.

This connection string gives complete access to everything in the Storage Account - read, write, delete, everything. It's extremely sensitive - anyone with this key can access all your data. This is exactly the kind of secret we need to protect with Key Vault.

Let's create an Azure Key Vault to store it securely. We're running az keyvault create with the resource group "labs-vnet-apps" and a unique name for your Key Vault.

Again, use a globally unique name for your Key Vault - something like "mykv" followed by your initials and a date often works well.

Now we'll store the connection string as a secret in Key Vault. We're using az keyvault secret set with the secret name "ConnectionStrings--AssetsDb". Notice the double dashes - this is a naming convention that the .NET configuration system understands for hierarchical configuration keys. The vault name is your Key Vault, and the value is the connection string we retrieved earlier.

Let's verify we can read this secret from our current machine using az keyvault secret show with the secret name "ConnectionStrings--AssetsDb" and vault name.

You should see the secret value returned in the output. Right now, this Key Vault is accessible from anywhere on the internet if you have the right permissions. There's no need for this secret to be accessible outside of Azure's internal network, so let's lock it down.

## Exercise 3: Restrict Access to Key Vault

To restrict Key Vault to only be accessible from our subnet, we first need to enable service endpoints on the subnet. Service endpoints allow Azure PaaS services to communicate privately over the Azure backbone network instead of going through the public internet.

We're running az network vnet subnet update with the resource group "labs-vnet-apps", VNet name "vnet1", subnet name "subnet1", and service-endpoints parameter set to enable both "Microsoft.KeyVault" and "Microsoft.Storage". We're enabling endpoints for both services because we'll secure both the Key Vault and Storage Account.

Now let's add our subnet to the Key Vault's network rules. We're using az keyvault network-rule add with the VNet name "vnet1", subnet "subnet1", resource group "labs-vnet-apps", and Key Vault name.

And set the default action to deny all other traffic using az keyvault update with default-action set to "Deny", the resource group, and Key Vault name.

Let's view our network rules using az keyvault network-rule list with the resource group "labs-vnet-apps" and Key Vault name.

Now try to read the secret again using the CLI or opening the Azure Portal. It may take a few minutes for the rules to propagate through Azure's infrastructure, but soon you should find that access is denied. Your local machine isn't on the allowed subnet, so you can't access the Key Vault anymore. This is exactly what we want - the secret is now protected from external access.

## Exercise 4: Deploy and Configure the Web Application

Our application is a .NET 6 web site, which is perfect for Azure App Service. An important thing to understand about App Services: they don't run inside Virtual Networks by default. They're platform services designed to be publicly accessible web applications. However, we can still secure them through VNet integration for outbound calls.

Let's deploy the application. First, change to the application directory, then we're running az webapp up with the resource group "labs-vnet-apps", app plan name "app-plan-02", OS type Linux, runtime "dotnetcore:6.0", SKU B1 for the basic tier, and a unique app name.

This command packages up the application source code and deploys it to a new or existing App Service plan. Use a unique name for your app since it becomes part of the URL.

Now we need to configure the application with settings that tell it to use Blob Storage and to fetch secrets from Key Vault. We're running az webapp config appsettings set with the resource group "labs-vnet-apps", and multiple settings: Database__Api set to "BlobStorage" to use blob storage instead of in-memory, KeyVault__Enabled set to "true" to enable Key Vault integration, KeyVault__Name set to your Key Vault name, and the app name.

If you browse to the app now at its URL, you'll see an error page instead of the application working. Let's investigate why by checking the logs.

## Exercise 5: Troubleshooting Authentication Issues

Open the Advanced Tools for your web app in the Azure Portal - this is called Kudu. It's a diagnostic and management interface for App Service. From there, open the Log stream and wait patiently for logs to appear. The app will keep restarting because it's encountering an error during startup.

Eventually, you'll see an error message about a Forbidden response from Key Vault. The error tells us that the application's identity doesn't have permission to list secrets on the Key Vault. This makes sense - we haven't given the app any identity or permissions yet.

App Service supports managed identities, which means it can authenticate with other Azure services without storing any credentials in your code or configuration. Let's enable this feature.

We're running az webapp identity assign with the resource group "labs-vnet-apps" and app name.

The output includes a principalId - this is the unique identifier of the managed identity that was created for your app. Copy this value because we need it for the next step.

Now we'll grant that identity permission to read secrets from Key Vault using az keyvault set-policy with the secret-permissions parameter set to "get" and "list", the object-id parameter set to the principalId we just got, and the Key Vault name.

Try the app again in your browser. It will still fail, but with a different error this time, which means we're making progress.

## Exercise 6: Troubleshooting Network Access Issues

Back in the log stream, you'll see a new error message. This time it says "Client address is not authorized and caller is not a trusted service" with a "ForbiddenByFirewall" error code.

Now the App Service is using an authorized managed identity, so authentication works. But the network call is being blocked because the outbound request from the App Service is not coming from our trusted subnet.

We have a couple of options here. We could get the outbound IP addresses of the webapp and add them to the Key Vault firewall. But IP addresses can change when the App Service scales or restarts, which would break our application.

The better solution is VNet integration. When we integrate the Web App with our VNet, its outbound calls to Azure services will go through the subnet, which has access to Key Vault thanks to the service endpoint.

We're running az webapp vnet-integration add with the VNet "vnet1", subnet "subnet1", resource group "labs-vnet-apps", and app name.

Let's check the configuration using az webapp show with the resource group "labs-vnet-apps" and app name to see the VNet integration settings.

Wait a few moments for the changes to take effect and for the app to restart. Then try the app again in your browser.

This time it should work! The app can now successfully authenticate with Key Vault using its managed identity, make the call through the VNet subnet which has access to Key Vault via the service endpoint, retrieve the connection string for Blob Storage, connect to Blob Storage and read or write data, and serve the application properly.

The full security flow is working: managed identity for authentication without secrets, VNet integration for network-level access control, service endpoints for private connectivity, and Key Vault for secure secret storage.

## Exercise 7: Lab Challenge - Secure the Storage Account

There's still a security gap in our architecture that needs to be addressed. The Storage Account is still open to the public internet. Just like Key Vault, Storage Accounts can't be deployed inside a VNet directly, but they can be restricted using network rules to only allow access through specific subnets.

Your challenge is to configure the Storage Account so that only services using our subnet have access, just like we did with Key Vault. This involves several steps working together.

Here are some hints to get you started: Storage Accounts have similar network rule capabilities to Key Vault in their firewall and virtual networks settings. You'll need to add a network rule that allows access from the subnet using the storage account network-rule commands. Don't forget to set the default action appropriately to deny other traffic. The app will need to be able to access the storage account through the VNet integration we've already set up.

If you complete this successfully, you'll have a fully secured application architecture where all communication happens through controlled network paths, all authentication uses managed identities with no secrets exposed, resources are only accessible through the VNet, and there's no public access to your backend services.

This is the gold standard for secure Azure application architecture - defense in depth with multiple layers of security working together!
