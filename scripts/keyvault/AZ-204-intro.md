# Azure Key Vault - AZ-204 Exam Introduction

Great work with Key Vault! This is one of the most heavily tested security topics on the AZ-204 exam.

## What We'll Cover

**Securing application configuration data** is the primary use case. Store connection strings, API keys, passwords, and certificates in Key Vault instead of config files or environment variables. The exam heavily tests knowing when to use Key Vault versus other configuration methods.

**Azure SDK with DefaultAzureCredential** is the modern approach for accessing Key Vault. `DefaultAzureCredential` tries multiple authentication methods in order (environment variables, managed identity, Visual Studio, Azure CLI, interactive browser). This enables passwordless authentication with zero code changes between dev and production. The exam tests understanding of credential chains and troubleshooting authentication.

**Managed Identities** eliminate passwords entirely. System-assigned (created with the resource, deleted with it, 1-to-1 relationship) versus user-assigned (standalone resource, shared across multiple services, survives resource deletion). The exam heavily tests when to use each type and how to configure them.

**Secret versioning and rotation strategies** are important. Reference secrets by name (not version) to automatically get the latest value when rotated. Set expiration dates to force rotation. Use multiple versions during rotation (keep old version briefly for gradual rollout). The exam tests designing rotation workflows.

**Access policies vs RBAC** for permission management needs to be understood. Access policies are the traditional model (permissions per vault, granular control per operation like Get/List/Set). RBAC is the modern model (standard Azure roles, consistent across services, easier to manage at scale). Key Vault supports both. The exam tests choosing between them.

**App Service integration with Key Vault references** uses special syntax `@Microsoft.KeyVault(SecretUri=...)` in application settings. App Service automatically retrieves the secret value at startup. Changes to Key Vault require restarting the app. The exam tests this integration pattern.

**Backup and recovery with soft delete** prevents accidental deletion. Deleted secrets enter soft-delete state (recoverable for retention period, default 90 days). Purge protection prevents even admins from permanently deleting during retention. The exam tests understanding of recovery workflows.

We'll cover **the distinction between secrets/keys/certificates**, **network security**, **audit logging**, **pricing tiers**, **CLI commands**, and **common scenarios** about secret rotation, troubleshooting access, and implementing zero-trust security.

Master Key Vault for the AZ-204!
