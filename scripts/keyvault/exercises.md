# Azure Key Vault

## Reference

Key Vault is a specialized storage service designed specifically for small pieces of sensitive data. You use it for user credentials, API keys, certificates, and any other application configuration that shouldn't be visible in plain text. The service provides encryption at rest, fine-grained permission controls for who can read values, and the ability to block access to the entire Key Vault so it's only available when you need to read the data. The documentation covers everything from basic secret management to advanced features like hardware security modules and automated certificate renewal. The command line interface gives you complete control through the az keyvault commands, which we'll be using throughout these exercises.

## Explore Key Vault in the Portal

Let's start by getting familiar with Key Vault options in the Portal.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Key Vault" to create a new resource. Before creating anything, let's explore the available options to understand what Key Vault offers.

**Pricing Tiers**: You'll see two pricing tiers available. The Standard tier is sufficient for most applications and includes all the core functionality for storing and managing secrets, keys, and certificates. The Premium tier offers hardware security module backed keys, which provides hardware-level encryption for scenarios with stringent compliance requirements or when you need the highest level of cryptographic security.

**Recovery Options**: Soft-delete is enabled by default with a retention period that acts as a safeguard against accidental deletion. When you delete a secret, key, or certificate, it's not immediately gone - it enters a deleted state during the retention period, and you can recover it. Purge protection adds an extra layer by preventing permanent deletion during the retention period, protecting against both accidental and malicious purging.

**Access Configuration**: You can choose between Access Policies, which is the classic approach with fine-grained permissions for individual operations, and Azure RBAC, which is the newer role-based access control model that provides better integration with Azure's overall security model. For new vaults, Azure RBAC is generally recommended.

After exploring the Portal, we'll switch to the command line to create our Key Vault with the Azure CLI - this approach is much more suitable for automation and repeatability.

---

## Create a Key Vault with the CLI

**Create a Resource Group**: Every Azure resource needs a home, so we're starting by creating a resource group for this lab. We're calling it "labs-keyvault" and placing it in the East US region. The tags parameter helps you track resources created for this course - this is a best practice for organizing and managing resources, especially when you have multiple projects or labs running.

**Find the Create Command**: Let's explore what options are available for creating a Key Vault by running az keyvault create with the help flag. The CLI offers many configuration options including network rules, retention policies, and encryption settings. Some of these can be configured later in the management pages, but it's good to know they exist upfront.

**Create Your Key Vault**: We're creating a Key Vault for this lab using the keyvault create command. You need to specify the resource group, location, and most importantly, a globally unique name. Remember to choose a unique name - something like "kv" followed by your initials and a random number works well.

**Naming Rules**: The Key Vault name becomes part of your DNS endpoint with the vault.azure.net suffix, which is why it must be globally unique across all of Azure. If you see an error, check that your name contains only lowercase letters, numbers, and hyphens, is between 3 and 24 characters, starts with a letter, and doesn't end with a hyphen.

**What's Happening During Creation**: Azure is provisioning the Key Vault service in your specified region, setting up the vault's DNS name, configuring default access policies where you as the creator get full access automatically, enabling soft-delete by default, and setting up the underlying encrypted storage. This takes about a minute or two to complete.

**Types of Data You Can Store**: While the Key Vault is being created, it's worth understanding what types of data you can store. Secrets are any sensitive data up to 25 kilobytes like passwords, connection strings, or API keys. Keys are cryptographic keys for encryption, signing, and verification operations where Azure can perform crypto operations without exposing the key itself. Certificates are X.509 certificates that Key Vault can automatically renew with supported certificate authorities, making certificate lifecycle management much easier.

---

## Manage Secrets in the Portal

Browse to your new Key Vault in the Portal to explore secret management.

**Create a Secret**: We're creating a secret with the key "sql-password" which could represent database credentials. In the Secrets section, click the Generate/Import button. The workflow is straightforward - you provide a name and value, and optionally add metadata like content type to document what the secret contains, activation dates to control when the secret becomes accessible, expiration dates to enforce rotation policies, and an enabled toggle to disable secrets without deleting them.

**Viewing Secrets**: After creating the secret, when you click on it, you'll see the current version listed. Key Vault automatically versions everything, which is crucial for managing changes. Click on the version to see its details. Notice that the value is hidden by default - you must explicitly click "Show Secret Value" to reveal it. This is a security feature reducing the risk of shoulder surfing or accidental exposure.

**Updating Secrets**: When you need to update a secret, use the New Version button. Key Vault creates a new version with your new value, and this new version automatically becomes the current version. The old version is preserved and still accessible if needed using its version ID. This versioning is crucial for several reasons - it enables secret rotation without downtime where applications automatically pick up new values on their next request, provides rollback capability if a new secret causes issues, and maintains a complete audit trail of changes.

---

## Manage Secrets in the CLI

Secrets have a unique identifier which contains the Key Vault name, secret name, and version. It's shown in the Portal - copy the identifier of the latest version of your secret to the clipboard, which will look something like https://your-kv-name.vault.azure.net/secrets/sql-password/some-version-guid.

**Show Secret by ID**: You can show the secret data using just the ID with the keyvault secret show command and the id parameter. The response includes all the secret fields including the value, version information, timestamps, enabled status, and metadata.

**Extract Just the Value**: The response includes all the secret's metadata, but you might want to retrieve just the secret value for automation. You can add output and query parameters to display just the value in plain text. The query syntax "value" combined with tsv output format gives you just the secret value, perfect for storing in environment variables or passing to other commands.

**Get Latest Version by Name**: If you don't know the full ID, you can get the latest version using the secret name parameter instead. Use the keyvault secret show command with the name and vault-name parameters. This always retrieves the current version, which is how your applications should reference secrets - by name without version, so rotation happens transparently.

**Update a Secret**: You can update the value using the secret set command, which works for both creating new secrets and updating existing ones. We're using secret set with the name, value, and vault-name parameters. This creates a new version and makes it the current version automatically.

**List All Versions**: Print all the versions using the keyvault secret list-versions command. This shows all versions with their IDs and timestamps, but notice it doesn't show the actual values - you need to query each version individually to see its value. It also doesn't explicitly show which is the current version, though the most recent one by timestamp is current.

---

## Lab

Secrets are just one type of data which you can store in Key Vault. You can also generate and store encryption keys and TLS certificates.

**The Scenario**: Use the CLI to create a self-signed certificate where the subject common name CN is azure.courselabs.co and which is valid for 6 months. Download the public and private keys for your new certificate.

**Your Task**: You'll need to find the certificate commands and understand how to create a certificate policy. Certificate creation requires a policy that defines the certificate properties including the issuer, key type and size, subject name, and validity period.

**Hints**: Start by exploring the keyvault certificate commands with the help flag. You'll need to create a policy file that specifies issuer parameters with name set to "Self" for self-signed certificates, key properties including exportable set to true so you can download the keys, keySize of 2048 bits, and keyType as RSA. The X.509 certificate properties need the subject as CN equals azure.courselabs.co and validityInMonths set to 6. After creation, use the certificate download command to get the certificate in PEM format which includes the full certificate chain.

**Understanding Certificates in Key Vault**: When you create a certificate in Key Vault, it automatically creates three objects - a certificate object that combines key and metadata, a key object for the private key, and a secret object containing the full certificate with private key in PKCS12 format. This means you can access the certificate through multiple interfaces depending on your needs.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up resource groups.

The resource group and all contents will be permanently deleted after the soft-delete retention period expires. Remember that soft-delete means the Key Vault and its contents are recoverable for the retention period if you need to restore them.
