# Azure Key Vault - Exercises Narration Script

## Exercise: Explore Key Vault in the Portal

Let's start by exploring Key Vault in the Azure Portal to understand its capabilities and configuration options.

Open the Azure Portal and use the search bar at the top to find "Key vaults". Click on "Create" to start the creation wizard.

### Review the Configuration Options

Take a moment to review the configuration options available on the Basics tab. You need to specify a resource group, region, and a globally unique name for your Key Vault. The name becomes part of the DNS, forming a URL like https colon slash slash your-name dot vault dot azure dot net. This is the endpoint your applications will use to connect.

Notice the Pricing tier options. There are Standard and Premium tiers. Premium tier offers HSM-backed keys for hardware-level encryption, which provides an additional layer of security with hardware security modules. For most applications, Standard tier is sufficient and cost-effective. Premium is typically used when you have compliance requirements that mandate HSM-backed keys.

Look at the Recovery options. Soft-delete is enabled by default with a 90-day retention period. This is a safeguard against accidental deletion - if you delete a secret, key, or certificate, it's not immediately gone. It enters a deleted state for 90 days, during which you can recover it. This has saved many people from disaster.

Purge protection adds an extra layer by preventing permanent deletion during the retention period. Even if you want to permanently delete something, you can't until the retention period expires. This protects against malicious or accidental purging.

For Access configuration, you can choose between Access Policies, which is the classic approach, and Azure RBAC, which is the newer role-based access control model. For new vaults, Azure RBAC is recommended as it provides better integration with Azure's overall security model. We'll explore both approaches in the exercises.

Don't complete the creation in the Portal yet - we'll use the Azure CLI instead for more precise control and better automation capabilities.

## Exercise: Create a Key Vault with the CLI

Let's use the Azure CLI to create our Key Vault. This gives us better automation capabilities and is how you'd typically create resources in a production environment.

### Step 1: Create a Resource Group

First, create a new resource group for this lab using the group create command with parameters for the name, location, and tags. We're creating a resource group named "labs-keyvault" in the East US region. The tag helps us track lab resources and makes cleanup easier later.

### Step 2: Create the Key Vault

Now create a Key Vault using the keyvault create command. Remember that the name must be globally unique across all of Azure. A good pattern is to use your initials and a random number, like "jd-kv-2024-001". We're specifying the location, resource group, and vault name.

What's happening during creation? Azure is provisioning the Key Vault service in the specified region, setting up the vault's DNS name, configuring default access policies - you as the creator get full access automatically - enabling soft-delete by default, and setting up the underlying storage. This takes about a minute or two to complete.

While it's being created, let's review what types of data you can store. Secrets are any sensitive data up to 25 kilobytes - passwords, connection strings, API keys, or any other sensitive text. Keys are cryptographic keys for encryption, signing, and verification operations - Azure can perform crypto operations without exposing the key itself. Certificates are X.509 certificates that Key Vault can automatically renew with supported certificate authorities, making certificate lifecycle management much easier.

## Exercise: Manage Secrets in the Portal

Now that our Key Vault is created, let's explore secret management through the Portal.

### Step 1: Navigate to Your Key Vault

In the Azure Portal, navigate to your newly created Key Vault. You can use the search bar or find it in your resource group.

### Step 2: Create a Secret

Let's create a secret that could represent a database password. In the left menu, click on "Secrets" under the Objects section. Click the Generate slash Import button at the top.

For upload options, leave "Manual" selected. Name the secret "sql-password". For the value, enter a sample password. Notice the optional settings available - Content type lets you add metadata like "password" or "connection-string" to document what the secret contains. Activation date means the secret won't be accessible before this date - useful for scheduling credential rotations. Expiration date makes the secret invalid after this date, enforcing rotation policies. And the Enabled toggle lets you disable a secret without deleting it, useful when investigating potential compromises.

Click "Create" to save the secret.

### Step 3: View the Secret

After creation, click on your secret name to see its details. You'll see the current version listed - remember, Key Vault automatically versions everything. Click on the current version. Notice that the value is hidden by default - you must click "Show Secret Value" to reveal it. This is a security feature - you must explicitly choose to view sensitive data, reducing the risk of shoulder surfing or accidental exposure.

### Step 4: Update the Secret

Let's see how versioning works. Go back to the Secrets list and click on your secret. Click the New Version button at the top. Enter a new value for the password and click "Create".

Now when you click on your secret, you'll see two versions listed. The newest version automatically becomes the current version - any application requesting this secret by name without specifying a version will get this new value. The old version is preserved and still accessible if needed using its version ID.

This versioning is crucial for several reasons. Secret rotation without downtime - you update the secret, applications pick up the new value on their next request. Rollback capability if a new secret causes issues - you can easily revert. And you have a complete audit trail of changes.

## Exercise: Manage Secrets with the CLI

The Portal is great for exploration, but the CLI is essential for automation. Let's work with secrets using the Azure CLI.

### Step 1: Get Secret by ID

Each secret has a unique identifier that includes the version. In the Portal, copy the Secret Identifier from your latest secret version - it looks like https colon slash slash your-vault dot vault dot azure dot net slash secrets slash sql-password slash some-version-guid.

Now retrieve it using the keyvault secret show command with the id parameter.

This returns a JSON object with all the secret's metadata. The secret value, version information, creation and update timestamps, enabled status, tags and content type - everything about the secret.

### Step 2: Extract Just the Value

In automation scripts, you often need just the value. Use the query parameter to extract it. The query syntax "value" combined with table output format gives you just the secret value in plain text, perfect for storing in environment variables or passing to other commands.

### Step 3: Get Latest Version by Name

You don't always need to specify the version ID. To get the latest version, use the secret name parameter instead of the full ID. This always retrieves the current version. This is how your applications should reference secrets - by name without version, so rotation happens transparently.

### Step 4: Update a Secret

To update a secret, which creates a new version, use the keyvault secret set command with the name, value, and vault-name parameters. The secret set command works for both creating new secrets and updating existing ones, making your scripts simpler.

### Step 5: List All Versions

See the complete version history using the keyvault secret list-versions command. This shows all versions with their IDs and timestamps, but notice it doesn't show the actual values - you need to query each version individually to see its value. This is a security feature preventing bulk exposure of sensitive data.

### Step 6: Working with Content Types

Content types help document what type of data a secret contains. When setting a secret, use the content-type parameter. This metadata is useful when you have many secrets and need to understand their purpose at a glance. You might have hundreds of secrets in a vault, and content types help you organize and understand them.

## Exercise: Advanced Secret Operations

Let's explore some advanced features that are important for production environments.

### Set Expiration Date

Secrets can have expiration dates to enforce rotation policies. Use the expires parameter with an ISO 8601 formatted date. After the expiration date, attempts to retrieve the secret will fail with an error. This ensures secrets can't be used indefinitely, forcing regular rotation and improving security posture.

### Disable a Secret

You can temporarily disable a secret without deleting it using the keyvault secret set-attributes command with the enabled parameter set to false. This is useful when you suspect a secret may be compromised and want to immediately stop its use while investigating. Better to temporarily disable and investigate than to discover later that a compromised secret was used for malicious purposes.

### Add Tags

Tags help with organization and searching. Use the tags parameter when setting a secret. For example, you might tag secrets with environment equals production and tier equals database. This helps you manage secrets at scale, finding all production secrets or all database-related secrets with simple queries.

## Lab: Working with Certificates

For the lab exercise, you'll create and manage a TLS certificate. Certificates combine cryptographic keys with identity information, perfect for HTTPS, code signing, or authentication scenarios.

### Goal

Create a self-signed certificate with these requirements: Subject common name CN equals azure dot courselabs dot co, validity period of 6 months, and download both the public and private keys.

### Hints

Find the certificate commands using the keyvault certificate help command. Certificate creation requires a policy that defines the certificate properties. You can create a policy file or use inline JSON. Policy elements to consider include the Issuer set to "Self" for self-signed certificates, key type as RSA, key size of 2048 bits, subject as CN equals your domain, and validity in months set to 6.

After creation, you can download the certificate using the certificate download command with different encoding formats - PEM or DER.

### Solution Approach

Create a policy file first with the required settings in JSON format. The policy specifies the issuer parameters, key properties with exportable set to true, and X.509 certificate properties with the subject and validity.

Create the certificate using the keyvault certificate create command with the vault name, certificate name, and policy parameters.

Download the certificate in PEM format, which includes the full certificate chain, using the certificate download command with encoding set to PEM.

You can also download in DER format, which is a binary format, by specifying DER encoding.

### What You've Learned

In this lab, you've learned to create and configure a Key Vault, store and retrieve secrets through both Portal and CLI, work with secret versioning, set expiration dates and other secret attributes, and create and download certificates. These are fundamental skills for securing applications in Azure.

## Key Takeaways

Key Vault is purpose-built for secrets - it's not a general storage service but a specialized security service focused on protecting sensitive data. Versioning is automatic - every update creates a new version, giving you a complete audit trail without any extra work. Reference by name, not version - this enables transparent secret rotation where applications automatically get updated secrets. Portal for exploration, CLI for automation - both have their place in your workflow. Certificates are more than keys - they combine keys with identity metadata and Key Vault can manage their entire lifecycle including automatic renewal.

## Cleanup

When you're finished with the lab, remove all resources using the group delete command with the yes and no-wait flags. This deletes the resource group and all its contents, including the Key Vault and all secrets. The no-wait flag lets the deletion happen in the background. The resource group and all contents will be permanently deleted after the retention period expires due to soft-delete.
