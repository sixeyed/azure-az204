# Securing AKS Apps with Key Vault and Virtual Networks - Exercises

## Exercise 1: Create Resource Group, Virtual Network and Subnet

Let's start by creating our foundational networking infrastructure.

First, we'll create a resource group for all our resources:

```
az group create -n labs-aks-apps --tags courselabs=azure
```

This creates a resource group named "labs-aks-apps" with a tag to help us track our lab resources.

Next, we'll create a virtual network with a specific address space:

```
az network vnet create -g labs-aks-apps -n appnet --address-prefix "10.30.0.0/16" -l eastus
```

We're using the 10.30.0.0/16 address space, which gives us plenty of room for multiple subnets. The network is created in the East US region.

Now we need a subnet specifically for our AKS cluster:

```
az network vnet subnet create -g labs-aks-apps --vnet-name appnet -n aks --address-prefix "10.30.1.0/24"
```

This subnet uses 10.30.1.0/24, which provides 256 IP addresses. Remember, when using Azure CNI with AKS, each Pod gets an IP from this subnet, so you need to plan your address space accordingly.

## Exercise 2: Create the AKS Cluster

Before creating the AKS cluster, we need to get the resource ID of our subnet. This ID will be used to tell AKS which subnet to use for the cluster:

```
az network vnet subnet show -g labs-aks-apps --vnet-name appnet -n aks --query id -o tsv
```

This returns something like: /subscriptions/YOUR-SUBSCRIPTION-ID/resourceGroups/labs-aks-apps/providers/Microsoft.Network/virtualNetworks/appnet/subnets/aks

Now we can create our AKS cluster. This command has several important flags:

```
az aks create -g labs-aks-apps -n aks06 --node-count 2 --enable-addons azure-keyvault-secrets-provider --enable-managed-identity --network-plugin azure --vnet-subnet-id 'YOUR-SUBNET-ID' -l eastus
```

Let me break down what each parameter does:

- name aks06: Our cluster name
- node-count 2: We want two worker nodes
- enable-addons azure-keyvault-secrets-provider: This installs the KeyVault CSI driver
- enable-managed-identity: Creates a managed identity for the cluster
- network-plugin azure: This is the key setting that enables Azure CNI networking
- vnet-subnet-id: Points to our subnet so Pods get IPs from there

This creation process takes several minutes because Azure needs to propagate Active Directory role assignments for the network. Feel free to open a second terminal to continue with the next steps while this completes.

## Exercise 3: Create Storage Account and Container

Our application uses Blob Storage, so we need to create a storage account:

```
az storage account create -g labs-aks-apps --sku Standard_ZRS -l eastus -n YOUR-STORAGE-ACCOUNT-NAME
```

Remember that storage account names must be globally unique, lowercase, and contain only letters and numbers.

Now create a blob container named assetsdb:

```
az storage container create -n assetsdb -g labs-aks-apps --account-name YOUR-STORAGE-ACCOUNT-NAME
```

Next, we need the connection string. The application will use this to connect to blob storage:

```
az storage account show-connection-string -o tsv -g labs-aks-apps --name YOUR-STORAGE-ACCOUNT-NAME
```

*[SHOW ON SCREEN: The connection string output from this command]*

Copy the connection string from the output. Now we need to edit the file at labs/aks-apps/secrets/asset-manager-connectionstrings.json and replace the placeholder with your connection string.

## Exercise 4: Create Key Vault and Store the Secret

This connection string contains sensitive credentials, so we'll store it in Azure Key Vault:

```
az keyvault create -g labs-aks-apps -l eastus -n YOUR-KEYVAULT-NAME
```

Again, Key Vault names must be globally unique.

Now let's store our connection string file as a secret:

```
az keyvault secret set --name asset-manager-connectionstrings --file labs/aks-apps/secrets/asset-manager-connectionstrings.json --vault-name YOUR-KEYVAULT-NAME
```

The file contents become the secret value. Let's verify we can read it:

```
az keyvault secret show --name asset-manager-connectionstrings --vault-name YOUR-KEYVAULT-NAME
```

Right now, this Key Vault is accessible from the Internet. Anyone with proper authentication can read these secrets from anywhere. That's not ideal for a production scenario.

## Exercise 5: Restrict Key Vault Access with Network Rules

First, we need to enable service endpoints on our AKS subnet for both Key Vault and Storage:

```
az network vnet subnet update -g labs-aks-apps --vnet-name appnet --name aks --service-endpoints Microsoft.KeyVault Microsoft.Storage
```

Service endpoints enable the subnet to communicate efficiently with these Azure services while allowing those services to identify traffic from the subnet.

Now let's add a network rule to allow our AKS subnet:

```
az keyvault network-rule add --vnet-name appnet --subnet aks -g labs-aks-apps --name YOUR-KEYVAULT-NAME
```

Next, we change the default action to deny all other traffic:

```
az keyvault update --default-action 'Deny' -g labs-aks-apps -n YOUR-KEYVAULT-NAME
```

Let's verify our network rules:

```
az keyvault network-rule list -g labs-aks-apps --name YOUR-KEYVAULT-NAME
```

You should see your VNet and subnet listed in the allowed rules.

## Exercise 6: Grant AKS Managed Identity Access

The KeyVault Secrets Provider add-on created a managed identity for AKS. We need to grant this identity permission to read secrets.

First, get the identity's client ID:

```
az aks show -g labs-aks-apps -n aks06 --query addonProfiles.azureKeyvaultSecretsProvider.identity.clientId -o tsv
```

This returns a GUID that identifies the managed identity.

Now create a Key Vault access policy for this identity:

```
az keyvault set-policy --secret-permissions get --spn 'YOUR-IDENTITY-ID' -n YOUR-KEYVAULT-NAME
```

This grants the identity permission to get secrets, which is all our application needs.

Now try reading the secret again from your local machine or the Azure Portal. After a few minutes, you should find that access is denied because you're not connecting from the AKS subnet. The only way to access this secret now is through the AKS managed identity from within the cluster.

## Exercise 7: Deploy the Application to AKS

Let's review the Kubernetes manifests we'll deploy. There are three files:

The service.yaml defines a LoadBalancer Service to expose our app on a public IP.

The deployment.yaml contains the Pod specification. Notice the volume mount that loads the Key Vault secret.

The secretProviderClass.yaml is the most interesting. This tells the CSI driver which Key Vault to use, which secret to fetch, and which identity to authenticate with.

You need to edit secretProviderClass.yaml and fill in three placeholders:
- Your Key Vault name
- Your AKS identity client ID
- Your Azure tenant ID

Once that's done, connect to your AKS cluster:

```
az aks get-credentials -g labs-aks-apps -n aks06 --overwrite-existing
```

This configures kubectl to connect to your cluster.

Deploy all three manifests:

```
kubectl apply -f labs/aks-apps/specs/asset-manager
```

Watch the Pod start up:

```
kubectl get po --watch
```

You should see the Pod go through ContainerCreating and then Running. The CSI driver mounts the Key Vault secret during the ContainerCreating phase.

Get the external IP address:

```
kubectl get svc asset-manager-lb
```

It may show as "pending" for a minute while Azure provisions a load balancer. Once you see a public IP, browse to that address.

The application should load successfully. In the background, it's reading the connection string from the mounted Key Vault secret, connecting to Blob Storage, and creating some sample data. You should see asset information displayed on the page.

## Lab Challenge

The application is working, but we have one more security gap. The Storage Account is still accessible from the Internet. Anyone who obtains the connection string can access the data.

Your challenge is to configure the Storage Account firewall to only allow access from the AKS subnet, just like we did with Key Vault.

Think about:
- What service endpoint do we need? (We already configured this earlier)
- What network rules do we need to add?
- What should the default action be?

The commands will be similar to what we used for Key Vault, but applied to the storage account instead.

Try it on your own, and test that the application still works after you make the change.

## Cleanup

When you're finished, delete the resource group to remove all resources:

```
az group delete -y --no-wait -n labs-aks-apps
```

The --no-wait flag means this runs in the background so you don't have to wait for completion.
