# Securing AKS Apps with Key Vault and Virtual Networks - Exercises

## Exercise 1: Create Resource Group, Virtual Network and Subnet

Let's start by creating our foundational networking infrastructure.

**Create the Resource Group**: We're creating a resource group for all our resources, naming it "labs-aks-apps" and adding the courselabs=azure tag to help us track our lab resources. This resource group will contain everything we need for this lab - the virtual network, AKS cluster, Key Vault, and storage account.

**Create the Virtual Network**: Next, we're creating a virtual network with a specific address space of 10.30.0.0/16. This gives us plenty of room for multiple subnets - the /16 prefix means we have over 65,000 IP addresses to work with. We're deploying it to the East US region and naming it "appnet" for application network.

**Create the AKS Subnet**: Now we need a subnet specifically for our AKS cluster. We're creating it within the appnet virtual network, naming it "aks", and using the 10.30.1.0/24 address space. This subnet provides 256 IP addresses, which is important because when using Azure CNI with AKS, each Pod gets its own IP address from this subnet. You need to plan your address space carefully based on how many Pods you expect to run - if you run out of IPs in the subnet, you can't scale your cluster any further.

## Exercise 2: Create the AKS Cluster

**Get the Subnet Resource ID**: Before creating the AKS cluster, we need to get the resource ID of our subnet. This ID will be used to tell AKS which subnet to use for the cluster. We're using az network vnet subnet show with a query parameter to extract just the ID field. This returns a long string that looks like /subscriptions/YOUR-SUBSCRIPTION-ID/resourceGroups/labs-aks-apps/providers/Microsoft.Network/virtualNetworks/appnet/subnets/aks. Copy this value - we'll need it in the next command.

**Create the AKS Cluster**: Now we can create our AKS cluster with several important configuration flags. We're naming it "aks06", requesting two worker nodes for high availability, enabling the azure-keyvault-secrets-provider add-on which installs the KeyVault CSI driver, enabling managed identity for the cluster to authenticate with Azure services, using the azure network plugin which is the key setting that enables Azure CNI networking, and specifying the vnet-subnet-id so Pods get IP addresses from our subnet.

Let me break down what's happening here. The node-count of 2 gives us redundancy - if one node fails, workloads can continue on the other. The azure-keyvault-secrets-provider add-on installs additional components that allow Pods to mount secrets from Azure Key Vault as volumes. The managed-identity creates an Azure AD identity that the cluster uses to interact with other Azure services securely. The network-plugin azure is crucial - it means each Pod gets a real IP address from your virtual network, unlike the default kubenet which uses private overlay networking. And the vnet-subnet-id points to our subnet so Azure knows where to allocate those Pod IPs.

This creation process takes several minutes because Azure needs to provision the infrastructure and propagate Active Directory role assignments for the network. The cluster needs permission to manage network resources, and setting up these permissions takes time. Feel free to open a second terminal to continue with the next steps while this completes.

## Exercise 3: Create Storage Account and Container

**Create the Storage Account**: Our application uses Blob Storage, so we need to create a storage account. We're using the Standard ZRS SKU for zone-redundant storage, deploying to the labs-aks-apps resource group in East US. Remember that storage account names must be globally unique, lowercase, and contain only letters and numbers - something like "saaksapps" followed by your initials or a random number works well.

**Create the Blob Container**: Now we're creating a blob container named "assetsdb" within the storage account. This is where the application will store its data. Blob containers are like folders in a storage account - they organize your blobs logically.

**Get the Connection String**: Next, we need the connection string so the application can connect to blob storage. We're using az storage account show-connection-string with the output format set to tsv for plain text. This returns a connection string that contains the account name, account key, and endpoint information all in one string. Copy this value carefully - it's sensitive information that grants full access to your storage account.

**Edit the Configuration File**: Now we need to edit the file at labs/aks-apps/secrets/asset-manager-connectionstrings.json and replace the placeholder with your actual connection string. This file contains the application configuration in JSON format, and it will become our Key Vault secret.

## Exercise 4: Create Key Vault and Store the Secret

**Create the Key Vault**: This connection string contains sensitive credentials, so we'll store it in Azure Key Vault rather than in Kubernetes directly. We're creating a Key Vault in our resource group in East US. Again, Key Vault names must be globally unique - something like "kv-aks-apps" followed by your initials works well.

**Store the Secret**: Now we're storing our connection string file as a secret using az keyvault secret set. The secret name is "asset-manager-connectionstrings", and we're using the file parameter to upload the entire JSON file as the secret value. The file contents become the secret value, preserving the JSON structure.

**Verify the Secret**: Let's verify we can read it using az keyvault secret show. This command retrieves the secret and displays its value, confirming it's stored correctly.

**Security Consideration**: Right now, this Key Vault is accessible from the Internet. Anyone with proper authentication can read these secrets from anywhere in the world. That's not ideal for a production scenario - we want to restrict access to only our AKS cluster.

## Exercise 5: Restrict Key Vault Access with Network Rules

**Enable Service Endpoints**: First, we need to enable service endpoints on our AKS subnet for both Key Vault and Storage using az network vnet subnet update. We're adding Microsoft.KeyVault and Microsoft.Storage to the service-endpoints list. Service endpoints enable the subnet to communicate efficiently with these Azure services while allowing those services to identify traffic from the subnet. It's a special routing configuration that keeps traffic on the Azure backbone network rather than going out to the internet.

**Add Network Rule**: Now we're adding a network rule to allow our AKS subnet to access the Key Vault using az keyvault network-rule add. This creates a rule that says "allow access from this specific virtual network subnet". The Key Vault can now identify traffic coming from our AKS subnet and allow it through.

**Change Default Action**: Next, we're changing the default action to deny all other traffic using az keyvault update with default-action set to 'Deny'. This is the crucial step - it flips the security model from "allow all, block specific" to "block all, allow specific". Now only traffic from our explicitly allowed subnet can access the Key Vault.

**Verify Network Rules**: Let's verify our network rules using az keyvault network-rule list. You should see your VNet and subnet listed in the allowed rules, confirming that the firewall is configured correctly.

## Exercise 6: Grant AKS Managed Identity Access

**Understanding the Architecture**: The KeyVault Secrets Provider add-on created a managed identity for AKS to use when accessing Key Vault. We need to grant this identity permission to read secrets. This follows Azure's principle of least privilege - give only the permissions needed, nothing more.

**Get the Identity Client ID**: First, we're getting the identity's client ID using az aks show with a query parameter to extract the addonProfiles.azureKeyvaultSecretsProvider.identity.clientId value. This returns a GUID that uniquely identifies the managed identity. Copy this value.

**Create Access Policy**: Now we're creating a Key Vault access policy for this identity using az keyvault set-policy. We're granting only the "get" permission on secrets, which is all our application needs - it can read secrets but not create, update, or delete them. The spn parameter stands for "service principal name" and accepts the identity's client ID.

**Test the Restriction**: Now try reading the secret again from your local machine or the Azure Portal. After the network rules propagate (this can take a few minutes), you should find that access is denied. You're seeing an error because you're not connecting from the AKS subnet - you're connecting from the internet. The only way to access this secret now is through the AKS managed identity from within the cluster. This is exactly what we want for production security.

## Exercise 7: Deploy the Application to AKS

**Review the Manifests**: Let's review the Kubernetes manifests we'll deploy. There are three files in the directory. The service.yaml defines a LoadBalancer Service to expose our app on a public IP - this creates an Azure Load Balancer automatically. The deployment.yaml contains the Pod specification with volume mounts that load the Key Vault secret into the container's filesystem. The secretProviderClass.yaml is the most interesting - this tells the CSI driver which Key Vault to use, which secret to fetch, and which identity to authenticate with.

**Edit the Secret Provider Class**: You need to edit secretProviderClass.yaml and fill in three placeholders. Replace the keyvault-name placeholder with your Key Vault name, the identity-client-id placeholder with your AKS identity client ID that we retrieved earlier, and the tenant-id placeholder with your Azure tenant ID. You can get your tenant ID from the az account list command output.

**Connect to AKS**: Once that's done, we're connecting to your AKS cluster using az aks get-credentials. This configures kubectl to connect to your cluster by downloading the connection credentials and setting up the kubectl context.

**Deploy the Application**: We're deploying all three manifests using kubectl apply with the directory path. Kubectl processes all YAML files in the directory and creates the resources in the cluster.

**Watch the Pod Start**: We're watching the Pod start up using kubectl get po with the watch flag. You should see the Pod go through several phases - Pending, then ContainerCreating, and finally Running. The CSI driver mounts the Key Vault secret during the ContainerCreating phase - this is when it authenticates to Key Vault, fetches the secret value, and mounts it as a file in the container.

**Get the External IP**: We're getting the external IP address using kubectl get svc for the asset-manager-lb service. It may show as "pending" for a minute while Azure provisions a load balancer and assigns a public IP. This is Azure creating real infrastructure for you. Once you see a public IP address, that's your application's internet-accessible address.

**Test the Application**: We're browsing to that IP address, and the application should load successfully. In the background, it's reading the connection string from the mounted Key Vault secret at /app/secrets, connecting to Blob Storage using that connection string, and creating some sample data in the blob container. You should see asset information displayed on the page, confirming that the entire chain is working - Key Vault secret mounted into the Pod, application reading the secret, connecting to Blob Storage, and serving the data.

## Lab Challenge

The application is working, but we have one more security gap. The Storage Account is still accessible from the Internet. Anyone who obtains the connection string - through a code leak, log file, or other exposure - can access the data directly, bypassing our application and its security.

Your challenge is to configure the Storage Account firewall to only allow access from the AKS subnet, just like we did with Key Vault.

Think about: What service endpoint do we need? We already configured Microsoft.Storage on the subnet earlier, so that's done. What network rules do we need to add to the storage account? The commands will be similar to what we used for Key Vault, but applied to the storage account instead. What should the default action be? You want to deny all traffic except from your AKS subnet.

Try it on your own, and test that the application still works after you make the change. If the app continues to work, you've successfully locked down both the Key Vault and the Storage Account to only allow access from your AKS cluster.

## Cleanup

When you're finished, we're deleting the resource group to remove all resources using az group delete with the yes flag to skip confirmation and the no-wait flag to return immediately. The deletion runs in the background, cleaning up the AKS cluster, Key Vault, storage account, virtual network, and all associated resources.

This cleanup is important - AKS clusters can be expensive to run, especially with multiple nodes, so you want to delete them promptly when you're done learning.
