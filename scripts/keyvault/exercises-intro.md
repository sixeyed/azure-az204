We've covered Key Vault as Azure's specialized security service for storing secrets, keys, and certificates with encryption, access control, and audit logging. Now let's work with Key Vault hands-on to see how it protects sensitive application data.

When you explore Key Vault in the Portal, you'll search for Key Vault resources and examine the creation options including the Standard tier with software encryption and Premium tier with HSM-backed keys for higher security requirements. You'll see that both pricing tiers include automatic versioning for secrets and recovery features like soft delete that prevent accidental data loss. The access policy options let you set granular permissions for who can read and write secrets, keys, and certificates.

Creating a Key Vault with the CLI gives you the programmatic approach needed for automation. You'll use the az keyvault create command specifying your resource group, region, and a globally unique name. While the Key Vault provisions, you can review the documentation to understand that Key Vault supports three types of data - secrets for connection strings and passwords, keys for encryption operations, and certificates for TLS and authentication.

Managing secrets in the Portal walks you through creating a secret called sql-password demonstrating the workflow for storing credentials. You'll see how the Portal asks for a key-value pair and provides options for activation and expiration dates. When you create the secret you'll discover the versioning system where each update creates a new version that becomes current while old versions remain accessible. Viewing the secret requires clicking through to see the actual value, showing how Key Vault protects sensitive data even in the Portal interface.

Managing secrets in the CLI shows you the automation approach using az keyvault secret commands. You'll show secrets using their full identifier including version number, or just the name to get the latest version. You'll use query parameters to extract just the value in plain text for scripting scenarios. Then you'll practice updating secrets with secret set which creates new versions, and listing all versions to see the version history that Key Vault maintains automatically.

The lab challenge has you working with certificates which are another data type in Key Vault. You'll create a self-signed certificate with a specific subject common name and validity period, then download the certificate in different formats. This demonstrates Key Vault's certificate lifecycle management capabilities beyond just storing secrets.

The key learning is that Portal works great for exploration and one-off tasks, but CLI is essential for automation and production workflows. Everything you do in Portal has a CLI equivalent for scripting into your deployment pipelines.

Let's secure sensitive data with Key Vault!
