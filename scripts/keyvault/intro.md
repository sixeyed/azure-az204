# Azure Key Vault - Introduction Narration Script

## Opening

Welcome to Azure Key Vault. In this lab, we'll explore one of Azure's most important security services for protecting sensitive application data.

Key Vault is a specialized storage service designed specifically for storing small pieces of sensitive data. This includes user credentials, API keys, certificates, and any other application configuration that should never be visible in plain text.

## Why Use Key Vault?

Think about all the secrets your applications need: database passwords, API keys, connection strings, certificates. Where do you store them? In configuration files? In environment variables? These approaches have significant security risks.

Key Vault solves this problem by providing:

- **Encryption at rest** - All data stored in Key Vault is encrypted
- **Access control** - You can set fine-grained permissions for who can read which values
- **Network isolation** - You can block access to the entire Key Vault except when needed
- **Audit logging** - Track every access to your secrets
- **Versioning** - Maintain history of secret values for rotation and rollback

## What Can You Store in Key Vault?

Key Vault supports three types of data:

1. **Secrets** - Small pieces of sensitive data like passwords, connection strings, and API keys. Maximum size is 25 KB.

2. **Keys** - Cryptographic keys used for encryption and decryption operations. These can be software-protected or hardware-protected using HSMs.

3. **Certificates** - X.509 certificates that combine keys with identity metadata. Key Vault can even manage the entire certificate lifecycle.

## Key Vault Pricing Tiers

When you create a Key Vault, you can choose between two pricing tiers:

- **Standard tier** - Secrets and keys are protected by software encryption
- **Premium tier** - Adds support for HSM-backed keys, which means hardware-based encryption for the highest security standards

## Recovery and Protection Features

Key Vault includes important safeguards to prevent accidental data loss:

- **Soft delete** - Automatically enabled on new vaults. When you delete a secret, it's retained for a recovery period (default 90 days) before permanent deletion.

- **Purge protection** - When enabled, prevents anyone from permanently deleting secrets during the retention period. This is critical for production environments.

## Access Control

Key Vault offers two permission models:

1. **Access Policies** - The traditional model where you assign specific permissions at the Key Vault level. You can grant permissions like "get secrets", "list secrets", "set secrets", etc.

2. **Azure RBAC** - The modern approach that uses Azure's role-based access control system. This is now the recommended model for new Key Vaults as it provides consistent access management across all Azure resources.

## Key Vault URI Structure

Every secret, key, and certificate in Key Vault has a unique URI that includes:

- The Key Vault DNS name: `https://<keyvault-name>.vault.azure.net`
- The object type: `/secrets/`, `/keys/`, or `/certificates/`
- The object name
- Optionally, a version identifier

Example: `https://<keyvault-name>.vault.azure.net/secrets/database-password/<version-id>`

When you reference a secret without specifying a version, you always get the latest version. This is important for secret rotation - your application code never needs to change.

## Best Practices Overview

As we go through the exercises, keep these best practices in mind:

1. **Never hardcode secrets** in your application code or configuration files
2. **Use separate Key Vaults** for different environments (dev, test, production)
3. **Enable soft delete and purge protection** for production Key Vaults
4. **Use Managed Identities** when your applications run in Azure - this eliminates the need to store credentials for accessing Key Vault itself
5. **Set expiration dates** on secrets and implement rotation policies
6. **Monitor and audit** Key Vault access with Azure Monitor and Log Analytics

## What's Next

In the hands-on exercises, we'll:

1. Create a Key Vault using both the Azure Portal and Azure CLI
2. Store and retrieve secrets
3. Work with secret versioning
4. Create and manage certificates
5. Implement proper access controls

Let's begin by exploring Key Vault in the Azure Portal, then we'll move to the CLI for more advanced operations.
