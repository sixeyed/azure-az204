# AKS with KeyVault Secret Storage - Exercises Walkthrough

## Exercise 1: Create the AKS Cluster

Let's start by creating our resources for this lab. First, we'll create a new resource group to keep everything organized.

```
az group create -n labs-aks-keyvault --tags courselabs=azure -l eastus
```

This creates our resource group in the East US region with a tag to identify it as part of our course labs.

Now, here's something important to understand: Key Vault access is restricted by design. We need a security principal that the AKS nodes can use when connecting to Azure Key Vault.

Let's create our AKS cluster with the necessary flags. We'll create a cluster with two nodes, enable managed identity, and most importantly, enable the Key Vault secrets provider add-on.

```
az aks create -g labs-aks-keyvault -n aks-cluster --node-count 2 --enable-addons azure-keyvault-secrets-provider --enable-managed-identity -l eastus
```

This command does several things:
- Creates a cluster named "aks-cluster"
- Provisions two nodes
- Enables the azure-keyvault-secrets-provider add-on, which installs the CSI driver
- Sets up a managed identity for the cluster to use

This will take several minutes to complete. While it's running, let's talk about what's happening behind the scenes.

### Understanding the Architecture

When we enable the Key Vault secrets provider add-on, Azure installs additional components into the cluster. These components run as pods in a special Kubernetes namespace called "kube-system" - this is where Kubernetes system components live, separate from application workloads.

Once the cluster is created, let's connect to it and verify the CSI driver is running.

```
az aks get-credentials -g labs-aks-keyvault -n aks-cluster --overwrite-existing
```

This command downloads the credentials and configures kubectl to connect to our new cluster. Now let's check for the CSI driver pods:

```
kubectl get pods --namespace kube-system -l app=secrets-store-csi-driver
```

You should see two pods with names starting with "aks-secrets-store-csi-driver" - one for each node in our cluster. These pods handle the mounting of Key Vault secrets into your application pods.

If you ever need to troubleshoot issues with Key Vault integration, these are the pods whose logs you'll want to check.

## Exercise 2: Create and Configure Key Vault

Now let's create our Key Vault. For this lab, the default options are fine:

```
az keyvault create -g labs-aks-keyvault -n kv-lab-demo
```

Remember to use a unique name for your Key Vault, as these names are globally unique across Azure.

### Authorizing AKS to Access Key Vault

Here's a critical step: we need to authorize the AKS managed identity to access our Key Vault. Let's first get the client ID of the identity that AKS is using:

```
az aks show -g labs-aks-keyvault -n aks-cluster --query addonProfiles.azureKeyvaultSecretsProvider.identity.clientId -o tsv
```

This returns the identity ID. Copy this value because we'll need it in the next command. Now let's create an access policy that allows this identity to read secrets:

```
az keyvault set-policy --secret-permissions get --spn 'your-identity-id' -n kv-lab-demo
```

This grants the "get" permission on secrets to our AKS identity. Notice that we're not linking the entire AKS cluster to a specific Key Vault. Instead, we're authorizing an identity to access the vault. This means the same AKS cluster could potentially read from multiple Key Vaults, as long as the identity has appropriate permissions.

## Exercise 3: Create and Model KeyVault Secrets

Let's create a secret in Key Vault. We'll upload a JSON file containing configuration values.

First, let's look at what we're uploading. The file contains configuration data in JSON format - perhaps database connection strings, API keys, or other sensitive settings.

```
az keyvault secret set --name configurable-secrets --file labs/aks-keyvault/secrets/configurable-secret.json --vault-name kv-lab-demo
```

Notice that Key Vault secrets don't have to be simple strings. This secret contains an entire JSON document. Key Vault will store it as a multi-line string, up to a maximum of 25 kilobytes.

### Defining the SecretProviderClass

Now comes the interesting part: we need to tell Kubernetes how to map Key Vault secrets to volume mounts. This is done with a custom resource called a SecretProviderClass.

Let's look at the keyVault.yaml file. This resource specifies:
- The Key Vault name
- Your Azure tenant ID
- The identity client ID
- And most importantly, an array of objects defining which secrets to mount

For each secret, we specify:
- objectName: the name of the secret in Key Vault - in our case, "configurable-secrets"
- objectType: the type of Key Vault object - "secret"
- objectAlias: the filename that will appear in the volume mount - "secret.json"

This is a fine-grained approach. You explicitly declare which Key Vault objects should be made available in your pods.

Before deploying, we need to customize this file. Let's get our tenant ID:

```
az account list -o table
```

Now update the YAML file with your tenant ID, identity ID, and Key Vault name. Then deploy it:

```
kubectl apply -f labs/aks-keyvault/specs/secretProviderClasses/keyVault.yaml
```

This creates the SecretProviderClass in your cluster. It's now ready to mount volumes from your Key Vault secret.

## Exercise 4: Deploy an Application

Now let's deploy an application that uses our Key Vault secret. We're using the configurable app - the same one from previous labs.

Looking at the deployment YAML, notice the volume configuration. It specifies:
- A CSI volume type
- The secrets-store.csi.k8s.io driver
- A reference to our SecretProviderClass

And in the container spec, we mount this volume to /app/secrets.

Let's deploy it:

```
kubectl apply -f labs/aks-keyvault/specs/configurable
```

This creates both the Deployment and a LoadBalancer Service. Let's watch the pod come up:

```
kubectl get po -l app=configurable --watch
```

Wait for the pod to reach the Running state. What's happening here is:
1. Kubernetes schedules the pod
2. The CSI driver sees the volume mount request
3. It contacts Azure Key Vault using the managed identity
4. It retrieves the secret value
5. It mounts it into the pod's filesystem

Let's verify the secret was mounted correctly:

```
kubectl exec deploy/configurable -- cat /app/secrets/secret.json
```

You should see the JSON content from your Key Vault secret. The secret has been successfully mounted as a file in your container's filesystem.

Now let's browse to the application. Get the LoadBalancer IP:

```
kubectl get svc configurable
```

Open that IP in your browser. You should see the application displaying the configuration values from the Key Vault secret. The application is reading the file at /app/secrets/secret.json and displaying its contents.

## Lab Challenge

Here's a challenge for you: In Kubernetes, when you update a ConfigMap or Secret that's mounted as a volume, the changes eventually propagate to running pods. It can take a few minutes due to caching, and there's no guarantee the application will pick up the changes without a restart.

What happens with the CSI secrets store? Update the secret in Key Vault and see if the change flows through to your running pod. Does the file content update? How long does it take? Does the application pick up the change?

This is an important consideration for production deployments. Understanding the behavior helps you plan your secret rotation strategy.

## Cleanup

When you're done, clean up all resources:

```
az group delete -y --no-wait -n labs-aks-keyvault
```

And switch your kubectl context back to your local environment:

```
kubectl config use-context docker-desktop
```

Great job working through this lab. You've learned how to integrate Azure Key Vault with AKS for secure, centralized secret management.
