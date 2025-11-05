# AKS with Key Vault Integration - Exercises Introduction

We've covered how the Container Storage Interface (CSI) enables Key Vault to serve as a storage provider, keeping secrets secure in Azure rather than in the Kubernetes cluster. Now let's implement this integration.

## What You'll Do

You'll start by **creating an AKS cluster with the azure-keyvault-secrets-provider add-on enabled**. This add-on installs the CSI driver components that know how to communicate with Azure Key Vault and mount secrets as volumes in your containers.

Then you'll **create a Key Vault and add some secrets** to it. These could be connection strings, API keys, or any sensitive configuration your application needs. Next, you'll **retrieve the AKS managed identity client ID** - this is the identity that will authenticate to Key Vault on behalf of your applications.

The critical security step is **granting the managed identity access to Key Vault** using access policies. You'll give it GET and LIST permissions for secrets, enabling it to retrieve the values but not modify or delete them. This follows the principle of least privilege.

Next comes the Kubernetes magic: you'll **create a SecretProviderClass** - a custom resource that maps specific Key Vault secrets to volume mounts with custom filenames. This object tells the CSI driver which secrets to fetch from which Key Vault, and how to present them in the filesystem. You can even rename secrets so "DATABASE-CONNECTION-STRING" in Key Vault becomes "connectionstring.txt" in your container.

When you **deploy the application**, the CSI driver automatically fetches the secrets from Key Vault and mounts them as files at `/app/secrets`. The application simply reads these files - it has no idea it's accessing Key Vault. The secrets are only materialized in memory, never written to disk, and are only available to containers that mount the volume.

The **lab challenge** explores secret rotation behavior - what happens when you update a secret in Key Vault? How long does it take for the application to see the new value?

Let's implement secure, centralized secret management for AKS!
