# Securing Apps with Key Vault and Virtual Networks

## Reference

The ideal application in Azure uses managed identities for all authentication and restricted virtual networks for all communication. This eliminates credentials to manage and store, and ensures no services are exposed beyond where they should be accessible. However, not all services in Azure support VNet connections, and not all components in your app will have integrated authentication. In this lab we'll deploy an app which uses Blob Storage, storing the connection details in a KeyVault which is restricted to a VNet. The documentation covers storage account firewall and virtual networks configuration, VNet integration for App Service apps, and how to combine these features for secure application architectures.

## Create RG, VNet and Subnet

**Create Foundation Resources**: Let's start with the core resources - the resource group and VNet. We're running az group create with the name "labs-vnet-apps" and adding our "courselabs=azure" tag for tracking. Then we're creating a virtual network with az network vnet create using the resource group "labs-vnet-apps", VNet name "vnet1", and address prefix "10.30.0.0/16". Finally, we're creating a subnet with az network vnet subnet create using the VNet name "vnet1", subnet name "subnet1", and address prefix "10.30.1.0/24".

**Understanding the Pattern**: Nothing new here if you've worked with VNets before. The interesting thing is that we're not actually going to deploy anything into the VNet traditionally. Instead, we'll use it as a bridge to secure communication between services. This is a common pattern when working with PaaS services that don't run inside VNets natively but need secure connectivity.

---

## Create Storage Account and KeyVault

**Create Storage Account**: The app uses Blob Storage, so we'll need to create an account and grab the connection string. We're running az storage account create with the resource group "labs-vnet-apps", SKU Standard_ZRS for zone-redundant storage, and a unique name that you'll provide. This application has code to create the blob container, so we don't need to do that in advance. Remember that storage account names must be globally unique across all of Azure.

**Get Connection String**: Now let's print the connection string using az storage account show-connection-string with tab-separated value output, resource group "labs-vnet-apps", and storage account name. That key gives complete access to everything in the Storage Account - read, write, delete, everything. It's extremely sensitive, so we need to keep it safe.

**Create Key Vault**: We'll create a KeyVault and store the connection string in a secret. We're running az keyvault create with the resource group "labs-vnet-apps" and a unique name for your Key Vault. Again, use a globally unique name - something like your initials followed by "kv" and today's date works well.

**Store the Secret**: Now we're storing the secret using az keyvault secret set with the secret name "ConnectionStrings--AssetsDb". Notice the double dashes - this is a naming convention that the .NET configuration system understands for hierarchical configuration keys. The vault name is your Key Vault, and the value is the connection string we retrieved earlier.

**Verify Access**: Let's check you can read the secret from your machine using az keyvault secret show with the secret name "ConnectionStrings--AssetsDb" and vault name. You should see the secret value returned. Right now, this KeyVault is accessible from anywhere on the internet if you have the right permissions. There's no need for this secret to be accessible outside of Azure, so we should lock it down.

---

## Restrict Access

**Enable Service Endpoints**: We'll use the subnet for communication to KeyVault and Storage, so we need to set service endpoints to allow that. We're running az network vnet subnet update with the resource group "labs-vnet-apps", VNet name "vnet1", subnet name "subnet1", and service-endpoints parameter enabling both "Microsoft.KeyVault" and "Microsoft.Storage". Service endpoints allow Azure PaaS services to communicate privately over the Azure backbone network.

**Add Network Rule to Key Vault**: Now let's restrict the KeyVault so it's only accessible from the vnet. We're running az keyvault network-rule add with the VNet name "vnet1", subnet "subnet1", resource group "labs-vnet-apps", and Key Vault name. This adds our subnet to the allowed list.

**Set Default Deny**: We're setting the default action to deny all other traffic using az keyvault update with default-action set to "Deny", resource group "labs-vnet-apps", and Key Vault name. This ensures that only explicitly allowed networks can access the vault.

**View Network Rules**: Let's list the network rules using az keyvault network-rule list with the resource group "labs-vnet-apps" and Key Vault name to see what we've configured.

**Test Restriction**: Check if you can read the secret with the CLI or the Portal again. It may take a few minutes for the rules to take effect, but now the secret should be blocked outside of the VNet. Your local machine isn't on the allowed subnet, so access is denied - this is exactly what we want for security.

---

## Create Web App using VNet, KeyVault and Blob Storage

**Understanding App Service**: Our app is a .NET 6 web site, so it's a good fit for PaaS. An important thing to understand - App Services don't run inside VNets. They're intended to be public facing platform services. We can still secure them, but it needs some more configuration through VNet integration.

**Deploy the Application**: Let's start by deploying the app as a Web App. We're changing to the src/asset-manager directory, then running az webapp up with the resource group "labs-vnet-apps", app plan name "app-plan-02", OS type Linux, runtime "dotnetcore:6.0", SKU B1 for basic tier, and a unique app name. This command packages and deploys the application.

**Configure Application Settings**: Now we're setting some app configuration settings. These tell the app to use Blob Storage for data, and to fetch the connection string from Key Vault. We're running az webapp config appsettings set with the resource group "labs-vnet-apps", multiple settings including Database__Api set to "BlobStorage", KeyVault__Enabled set to "true", KeyVault__Name set to your Key Vault name, and the app name.

**Check for Errors**: Browse to the app - it will show an error page. Let's investigate by opening the logs.

**View Application Logs**: Open Advanced tools for the web app in the Portal and launch the Kudu session. This is Azure App Service's diagnostic and management interface. Open the Log stream link and be patient - logs take time to appear. The app will keep restarting because the failure causes it to exit. Eventually you'll see a useful error log indicating the app doesn't have permission to access Key Vault secrets.

**The Problem**: The error shows that the application's identity doesn't have secrets list permission on Key Vault. This makes sense - we haven't given the app any identity or permissions yet. The app isn't using an identity which KeyVault trusts.

**Assign Managed Identity**: App Service can use managed identity, so it can authenticate with KeyVault without needing any connection strings or other credentials. We're running az webapp identity assign with the resource group "labs-vnet-apps" and app name. The output contains the principalId of the identity that was created.

**Grant Key Vault Access**: Now we're giving the identity access to read secrets using az keyvault set-policy with the secret-permissions parameter set to "get list", object-id set to the principalId from the previous command, and Key Vault name. This grants the managed identity permission to retrieve secrets.

**Test Again**: Try the app again in your browser. It will still fail, but with a different error this time.

**New Error**: Open the logs for the app again using the same Kudu process. After waiting for the logs, you'll see a new error indicating "Client address is not authorized and caller is not a trusted service" with a "ForbiddenByFirewall" error code. Now the App Service is using an authorized identity but the call is not coming from a trusted location, because the KeyVault is restricted to the subnet.

**VNet Integration Solution**: One option we have here is to get the outbound IP addresses of the webapp and add them to the KeyVault firewall. But IP addresses change when apps scale or restart, so it's better to add VNet integration to the web app. Then when the App Service makes internal Azure calls, it will be via the subnet which has Key Vault access.

**Add VNet Integration**: We're running az webapp vnet-integration add with the VNet "vnet1", subnet "subnet1", resource group "labs-vnet-apps", and app name. This connects the app's outbound traffic to the VNet.

**Verify Configuration**: Let's check the app using az webapp show with the resource group "labs-vnet-apps" and app name to see the VNet integration settings.

**Test Success**: Now when the changes filter through, the app can connect to Key Vault where it reads the connection string for the Storage Account and then it downloads the data from the blob container. The full security chain is working - managed identity for authentication, VNet integration for network access, service endpoints for private connectivity, and Key Vault for secret storage.

---

## Lab

**The Challenge**: But the Storage Account is still open to the Internet. Storage Accounts can't be deployed inside a VNet like traditional resources because they're intended to have public connections, but they can be restricted using network rules just like Key Vault.

**Your Task**: Fix the Storage Account so only services using the subnet have access. You'll need to use similar commands to what we used for Key Vault, but for storage accounts. The app should continue working because it accesses storage through the VNet integration we've already configured.

**What to Consider**: Think about the storage account network-rule commands, setting appropriate default actions, and ensuring the app can still access the storage through the integrated VNet. When complete, you'll have a fully secured architecture with no public access to backend services.

---

## Cleanup

**Delete Resources**: You can delete the resource group with az group delete using the -y flag to skip confirmation and resource group name "labs-vnet-apps". This removes all the resources - Web App, App Service Plan, Storage Account, Key Vault, VNet, and everything else we created.
