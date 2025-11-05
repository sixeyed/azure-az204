# Azure Key Vault - Exercises Narration Script

## Exercise: Explore Key Vault in the Portal

Let's start by exploring Key Vault in the Azure Portal to understand its capabilities and configuration options.

Open the Azure Portal and use the search bar at the top to find "Key vaults". Click on "Create" to start the creation wizard.

### Review the Configuration Options

Take a moment to review the configuration options available:

**Basics tab:**
- You need to specify a resource group, region, and a globally unique name for your Key Vault
- The name becomes part of the DNS: `https://<your-name>.vault.azure.net`

**Pricing tier:**
- Notice the Standard and Premium options
- Premium tier offers HSM-backed keys for hardware-level encryption
- For most applications, Standard tier is sufficient

**Recovery options:**
- Soft-delete is enabled by default with a 90-day retention period
- This is a safeguard against accidental deletion
- Purge protection adds an extra layer by preventing permanent deletion during the retention period

**Access configuration:**
- You can choose between Access Policies (classic) and Azure RBAC
- For new vaults, Azure RBAC is recommended
- We'll explore both approaches in the exercises

Don't complete the creation in the Portal yet - we'll use the Azure CLI instead for more precise control.

## Exercise: Create a Key Vault with the CLI

Let's use the Azure CLI to create our Key Vault. This gives us better automation capabilities and is how you'd typically create resources in a production environment.

### Step 1: Create a Resource Group

First, create a new resource group for this lab:

```bash
az group create -n labs-keyvault --tags courselabs=azure -l eastus
```

This creates a resource group named "labs-keyvault" in the East US region. The tag helps us track lab resources.

### Step 2: Create the Key Vault

Now create a Key Vault. Remember that the name must be globally unique across all of Azure:

```bash
az keyvault create -l eastus -g labs-keyvault -n <keyvault-name>
```

Replace `<keyvault-name>` with your unique name. A good pattern is to use your initials and a random number, like "jd-kv-2024-001".

**What's happening during creation:**
- Azure is provisioning the Key Vault service in the specified region
- Setting up the vault's DNS name
- Configuring default access policies (you as the creator get full access)
- Enabling soft-delete by default
- This takes about a minute or two to complete

While it's being created, let's review what types of data you can store:
- **Secrets** - Any sensitive data up to 25 KB
- **Keys** - Cryptographic keys for encryption, signing, and verification
- **Certificates** - X.509 certificates that Key Vault can automatically renew

## Exercise: Manage Secrets in the Portal

Now that our Key Vault is created, let's explore secret management through the Portal.

### Step 1: Navigate to Your Key Vault

In the Azure Portal, navigate to your newly created Key Vault. You can use the search bar or find it in your resource group.

### Step 2: Create a Secret

Let's create a secret that could represent a database password:

1. In the left menu, click on "Secrets" under the Objects section
2. Click "+ Generate/Import" at the top
3. For upload options, leave "Manual" selected
4. Name the secret: `sql-password`
5. For the value, enter a sample password like: `<sample-password>`
6. Notice the optional settings:
   - Content type: You can add metadata like "password" or "connection-string"
   - Activation date: The secret won't be accessible before this date
   - Expiration date: The secret becomes invalid after this date
   - Enabled: You can disable a secret without deleting it

7. Click "Create"

### Step 3: View the Secret

After creation:
- Click on your secret name to see its details
- You'll see the current version listed
- Click on the current version
- Notice that the value is hidden by default - click "Show Secret Value" to reveal it
- This is a security feature - you must explicitly choose to view sensitive data

### Step 4: Update the Secret

Let's see how versioning works:

1. Go back to the Secrets list and click on your secret
2. Click "+ New Version" at the top
3. Enter a new value: `<new-sample-password>`
4. Click "Create"

Now when you click on your secret, you'll see two versions listed. The newest version automatically becomes the current version. The old version is preserved and still accessible if needed.

This versioning is crucial for:
- Secret rotation without downtime
- Rollback capability if a new secret causes issues
- Audit trail of changes

## Exercise: Manage Secrets with the CLI

The Portal is great for exploration, but the CLI is essential for automation. Let's work with secrets using the Azure CLI.

### Step 1: Get Secret by ID

Each secret has a unique identifier that includes the version. In the Portal, copy the Secret Identifier from your latest secret version (it looks like: `https://<keyvault-name>.vault.azure.net/secrets/sql-password/<version-id>`).

Now retrieve it using the CLI:

```bash
az keyvault secret show --id <secret-id>
```

This returns a JSON object with all the secret's metadata:
- The secret value
- Version information
- Creation and update timestamps
- Enabled status
- Tags and content type

### Step 2: Extract Just the Value

In automation scripts, you often need just the value. Use the query parameter:

```bash
az keyvault secret show -o tsv --query "value" --id <secret-id>
```

This outputs only the secret value in plain text, perfect for storing in environment variables or passing to other commands.

### Step 3: Get Latest Version by Name

You don't always need to specify the version ID. To get the latest version, use the secret name:

```bash
az keyvault secret show --name sql-password --vault-name <keyvault-name>
```

This always retrieves the current version. This is how your applications should reference secrets - by name without version, so rotation happens transparently.

### Step 4: Update a Secret

To update a secret (which creates a new version):

```bash
az keyvault secret set --name sql-password --value <new-password-value> --vault-name <keyvault-name>
```

The `secret set` command works for both creating new secrets and updating existing ones.

### Step 5: List All Versions

See the complete version history:

```bash
az keyvault secret list-versions --name sql-password --vault-name <keyvault-name>
```

This shows all versions with their IDs and timestamps, but notice it doesn't show the actual values - you need to query each version individually to see its value. This is a security feature.

### Step 6: Working with Content Types

Content types help document what type of data a secret contains:

```bash
az keyvault secret set \
  --vault-name <keyvault-name> \
  --name "api-key" \
  --value "<api-key-value>" \
  --content-type "api-key"
```

This metadata is useful when you have many secrets and need to understand their purpose at a glance.

## Exercise: Advanced Secret Operations

Let's explore some advanced features.

### Set Expiration Date

Secrets can have expiration dates to enforce rotation policies:

```bash
az keyvault secret set \
  --vault-name <keyvault-name> \
  --name "temporary-token" \
  --value "<token-value>" \
  --expires "2025-12-31T23:59:59Z"
```

After the expiration date, attempts to retrieve the secret will fail. This ensures secrets can't be used indefinitely.

### Disable a Secret

You can temporarily disable a secret without deleting it:

```bash
az keyvault secret set-attributes \
  --vault-name <keyvault-name> \
  --name "api-key" \
  --enabled false
```

This is useful when you suspect a secret may be compromised and want to immediately stop its use while investigating.

### Add Tags

Tags help with organization and searching:

```bash
az keyvault secret set \
  --vault-name <keyvault-name> \
  --name "prod-db-password" \
  --value "<db-password>" \
  --tags environment=production tier=database
```

## Lab: Working with Certificates

For the lab exercise, you'll create and manage a TLS certificate. Certificates combine cryptographic keys with identity information, perfect for HTTPS, code signing, or authentication.

### Goal

Create a self-signed certificate with these requirements:
- Subject common name (CN): `azure.courselabs.co`
- Validity period: 6 months
- Download both the public and private keys

### Hints

1. **Find the certificate commands:**
   ```bash
   az keyvault certificate --help
   ```

2. **Certificate creation requires a policy** that defines the certificate properties. You can create a policy file or use inline JSON.

3. **Policy elements to consider:**
   - Issuer: "Self" for self-signed
   - Key type: RSA
   - Key size: 2048 bits
   - Subject: CN=azure.courselabs.co
   - Validity: 6 months (validityInMonths: 6)

4. **After creation, you can download** the certificate using the `certificate download` command with different encoding formats (PEM or DER).

### Solution Approach

Create a policy file first:

```bash
cat > cert-policy.json << 'EOF'
{
  "issuerParameters": {"name": "Self"},
  "keyProperties": {
    "exportable": true,
    "keySize": 2048,
    "keyType": "RSA"
  },
  "x509CertificateProperties": {
    "subject": "CN=azure.courselabs.co",
    "validityInMonths": 6
  }
}
EOF
```

Create the certificate:

```bash
az keyvault certificate create \
  --vault-name <keyvault-name> \
  --name "course-cert" \
  --policy @cert-policy.json
```

Download the certificate in PEM format (includes the full certificate chain):

```bash
az keyvault certificate download \
  --vault-name <keyvault-name> \
  --name "course-cert" \
  --file course-cert.pem \
  --encoding PEM
```

Download in DER format (binary format):

```bash
az keyvault certificate download \
  --vault-name <keyvault-name> \
  --name "course-cert" \
  --file course-cert.cer \
  --encoding DER
```

### What You've Learned

In this lab, you've learned to:
- Create and configure a Key Vault
- Store and retrieve secrets through both Portal and CLI
- Work with secret versioning
- Set expiration dates and other secret attributes
- Create and download certificates

## Key Takeaways

1. **Key Vault is purpose-built for secrets** - It's not a general storage service but a specialized security service
2. **Versioning is automatic** - Every update creates a new version, giving you a complete audit trail
3. **Reference by name, not version** - This enables transparent secret rotation
4. **Portal for exploration, CLI for automation** - Both have their place in your workflow
5. **Certificates are more than keys** - They combine keys with identity metadata and Key Vault can manage their entire lifecycle

## Cleanup

When you're finished with the lab, remove all resources:

```bash
az group delete -y --no-wait -n labs-keyvault
```

The `--no-wait` flag lets the deletion happen in the background. The resource group and all its contents (including the Key Vault and all secrets) will be permanently deleted after the retention period expires.
