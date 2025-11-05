# AKS with KeyVault Secret Storage - Exercises Walkthrough

## Exercise 1: Create the AKS Cluster

Let's start by creating our resources for this lab. First, we're creating a new resource group to keep everything organized.

**Create the Resource Group**: We're creating a resource group named "labs-aks-keyvault" in the East US region with a tag to identify it as part of our course labs. This will contain our AKS cluster and Key Vault.

**Understanding Key Vault Security**: Here's something important to understand: Key Vault access is restricted by design. We need a security principal that the AKS nodes can use when connecting to Azure Key Vault. You can't just access Key Vault anonymously or with basic credentials - everything goes through Azure Active Directory.

**Create the AKS Cluster**: Let's create our AKS cluster with the necessary flags. We're creating a cluster named "aks-cluster" with two nodes, enabling managed identity, and most importantly, enabling the Key Vault secrets provider add-on. This command does several things: it creates the cluster infrastructure, provisions two nodes for redundancy, enables the azure-keyvault-secrets-provider add-on which installs the CSI driver, and sets up a managed identity for the cluster to use when authenticating to Azure services.

This will take several minutes to complete. While it's running, let's talk about what's happening behind the scenes.

**Understanding the Architecture**: When we enable the Key Vault secrets provider add-on, Azure installs additional components into the cluster. These components run as pods in a special Kubernetes namespace called "kube-system" - this is where Kubernetes system components live, separate from application workloads. The CSI driver pods handle the mounting of Key Vault secrets into your application pods, acting as a bridge between Kubernetes and Azure Key Vault.

**Connect to the Cluster**: Once the cluster is created, let's connect to it using az aks get-credentials. This command downloads the credentials and configures kubectl to connect to our new cluster. The overwrite-existing flag means it will replace any existing credentials for a cluster with the same name.

**Verify the CSI Driver**: Now let's check for the CSI driver pods using kubectl get pods in the kube-system namespace with a label filter for the secrets-store-csi-driver app. You should see two pods with names starting with "aks-secrets-store-csi-driver" - one for each node in our cluster. These pods handle the mounting of Key Vault secrets into your application pods.

**Troubleshooting Note**: If you ever need to troubleshoot issues with Key Vault integration, these are the pods whose logs you'll want to check. They contain detailed information about secret retrieval, authentication, and mounting operations.

## Exercise 2: Create and Configure Key Vault

Now let's create our Key Vault. For this lab, the default options are fine.

**Create the Key Vault**: We're creating a Key Vault in our resource group. Remember to use a unique name for your Key Vault - something like "kv-lab-demo" followed by your initials or a random number. Key Vault names are globally unique across Azure.

**Authorizing AKS to Access Key Vault**: Here's a critical step: we need to authorize the AKS managed identity to access our Key Vault. This follows the principle of least privilege - we grant only the permissions needed, nothing more.

**Get the Identity Client ID**: Let's first get the client ID of the identity that AKS is using. We're running az aks show with a query parameter to extract the addonProfiles.azureKeyvaultSecretsProvider.identity.clientId value. This returns a GUID that uniquely identifies the managed identity. Copy this value because we'll need it in the next command.

**Create the Access Policy**: Now we're creating an access policy that allows this identity to read secrets using az keyvault set-policy. We're granting the "get" permission on secrets to our AKS identity. Notice that we're not linking the entire AKS cluster to a specific Key Vault. Instead, we're authorizing an identity to access the vault. This means the same AKS cluster could potentially read from multiple Key Vaults, as long as the identity has appropriate permissions on each one. This is a flexible approach that supports complex scenarios.

## Exercise 3: Create and Model KeyVault Secrets

Let's create a secret in Key Vault. We'll upload a JSON file containing configuration values.

**Understanding Secret Storage**: First, let's look at what we're uploading. The file contains configuration data in JSON format - perhaps database connection strings, API keys, or other sensitive settings. Notice that Key Vault secrets don't have to be simple strings - they can contain structured data like JSON documents. Key Vault will store it as a multi-line string, up to a maximum of 25 kilobytes.

**Upload the Secret**: We're creating a secret named "configurable-secrets" by uploading the JSON file using az keyvault secret set. The file parameter tells the command to read the file contents and use that as the secret value.

**Defining the SecretProviderClass**: Now comes the interesting part: we need to tell Kubernetes how to map Key Vault secrets to volume mounts. This is done with a custom resource called a SecretProviderClass.

**Understanding the Configuration**: Let's look at the keyVault.yaml file. This resource specifies the Key Vault name, your Azure tenant ID, the identity client ID, and most importantly, an array of objects defining which secrets to mount. For each secret, we specify the objectName which is the name of the secret in Key Vault - in our case "configurable-secrets", the objectType which is "secret", and the objectAlias which is the filename that will appear in the volume mount - "secret.json".

This is a fine-grained approach - you explicitly declare which Key Vault objects should be made available in your pods. You're not mounting the entire Key Vault, just the secrets you need.

**Get Your Tenant ID**: Before deploying, we need to get your tenant ID using az account list. The tenant ID identifies your Azure Active Directory instance.

**Customize and Deploy**: Now we're updating the YAML file with your tenant ID, identity ID, and Key Vault name, then deploying it using kubectl apply. This creates the SecretProviderClass in your cluster. It's now ready to mount volumes from your Key Vault secret.

## Exercise 4: Deploy an Application

Now let's deploy an application that uses our Key Vault secret. We're using the configurable app - the same one from previous labs.

**Understanding the Deployment**: Looking at the deployment YAML, notice the volume configuration. It specifies a CSI volume type, the secrets-store.csi.k8s.io driver, and a reference to our SecretProviderClass. In the container spec, we mount this volume to /app/secrets. This is the magic that connects Kubernetes volumes to Azure Key Vault.

**Deploy the Application**: Let's deploy it using kubectl apply. This creates both the Deployment and a LoadBalancer Service.

**Watch the Pod Start**: We're watching the pod come up using kubectl get po with the watch flag and a label filter. Wait for the pod to reach the Running state. What's happening here is: Kubernetes schedules the pod, the CSI driver sees the volume mount request, it contacts Azure Key Vault using the managed identity, it retrieves the secret value, and it mounts it into the pod's filesystem as a file.

**Verify the Secret Mount**: Let's verify the secret was mounted correctly using kubectl exec to run a command inside the pod. We're using cat to read /app/secrets/secret.json. You should see the JSON content from your Key Vault secret displayed. The secret has been successfully mounted as a file in your container's filesystem.

**Test the Application**: Now let's browse to the application. We're getting the LoadBalancer IP using kubectl get svc. Open that IP in your browser and you should see the application displaying the configuration values from the Key Vault secret. The application is reading the file at /app/secrets/secret.json and displaying its contents, confirming the entire integration is working.

## Lab Challenge

Here's a challenge for you: In Kubernetes, when you update a ConfigMap or Secret that's mounted as a volume, the changes eventually propagate to running pods. It can take a few minutes due to kubelet caching, and there's no guarantee the application will pick up the changes without a restart.

**The Question**: What happens with the CSI secrets store? Update the secret in Key Vault using az keyvault secret set with new values and see if the change flows through to your running pod. Does the file content update? How long does it take? Does the application pick up the change automatically, or do you need to restart the pod?

This is an important consideration for production deployments. Understanding the behavior helps you plan your secret rotation strategy. Some applications can reload configuration without restarting, while others need to be restarted to pick up new values.

## Cleanup

When you're done, we're cleaning up all resources by deleting the resource group using az group delete with the yes flag to skip confirmation and the no-wait flag to return immediately.

We're also switching your kubectl context back to your local environment using kubectl config use-context docker-desktop. This ensures future kubectl commands target your local Docker Desktop cluster, not the deleted AKS cluster.

Great job working through this lab. You've learned how to integrate Azure Key Vault with AKS for secure, centralized secret management - a critical pattern for production Kubernetes applications.
