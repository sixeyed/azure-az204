# Azure Blob Storage - Lab Exercises Walkthrough
## Step-by-Step Narration Script

*Duration: Full lab walkthrough*

---

## Introduction to the Lab

Welcome to the Azure Blob Storage hands-on lab. In this session, we'll work through practical exercises that cover the more advanced features of Blob Storage, including SAS tokens, stored access policies, and storage access tiers.

Before we begin, make sure you have the Azure CLI installed and you're logged in to your Azure subscription. Let's get started!

---

## Part 1: Managing Blob Storage with the Azure CLI

### Creating the Resource Group and Storage Account

First, let's create a resource group to organize all our lab resources. We'll call it `labs-storage-blob` and place it in West Europe.

*[SHOW ON SCREEN: Command being typed]*

```bash
az group create -n labs-storage-blob --tags courselabs=azure -l westeurope
```

Notice we're adding a tag called "courselabs" with the value "azure" - this helps us identify and manage resources that belong to this course.

Next, we need to create a storage account. Remember, storage account names must be globally unique and can only contain lowercase letters and numbers. Choose a name that's unique to you - I'll use a placeholder in the commands.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage account create -g labs-storage-blob -l westeurope --sku Standard_LRS -n <sa-name>
```

We're using the Standard_LRS SKU, which stands for "locally redundant storage" - this is the most cost-effective option for our lab exercises.

### Creating a Blob Container

Now that we have a storage account, let's create a container. In Blob Storage, containers are like folders - they organize your blobs into logical groups.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage container create -n labs -g labs-storage-blob --account-name <sa-name>
```

Great! We now have a container named "labs" where we can upload files.

---

## Part 2: Uploading Files in Bulk

### Understanding the Upload Batch Command

The Azure CLI has a powerful feature called `upload-batch` that lets you upload multiple files at once. Let's explore this with a dry run first.

A dry run shows you what would happen without actually performing the operation - this is a great way to verify your command before executing it.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob upload-batch -d labs -s ./labs --dryrun -o table --account-name <sa-name>
```

*[SHOW ON SCREEN: Table output showing files that would be uploaded]*

As you can see from the output, the command would upload every file from the labs directory, preserving the entire folder structure. Each blob URL and file type is displayed in the table.

### Filtering Files with Patterns

But what if we only want to upload certain types of files? Let's say we only want to upload markdown files. We can use the `pattern` parameter to filter.

First, let's do another dry run to see which files would be uploaded:

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob upload-batch -d labs -s ./labs --dryrun -o table --pattern '*.md' --account-name <sa-name>
```

Perfect! Now we see only the markdown files. Let's do the actual upload by removing the `--dryrun` flag.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob upload-batch -d labs -s ./labs --pattern '*.md' --account-name <sa-name>
```

*[SHOW ON SCREEN: Upload progress and completion]*

Excellent! The output shows each blob URL, along with generated eTags and last modified dates. These eTags are important for HTTP caching and concurrency control.

### Listing and Inspecting Blobs

Let's verify that our files were uploaded correctly. We can list the blobs in a specific directory using the directory list command.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob directory list -c labs -d 'storage-blob' -o table --account-name <sa-name>
```

*[SHOW ON SCREEN: Table output showing files]*

You'll notice a warning that this command is deprecated - the Azure CLI evolves over time, so always check for deprecated commands when you upgrade.

Now let's get detailed information about a specific blob. The `storage blob show` command retrieves metadata and properties.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob show --container-name labs --name 'storage-blob/README.md' -o table --account-name <sa-name>
```

*[SHOW ON SCREEN: Blob properties displayed]*

Important note: blob names are case-sensitive! If you try "readme.md" instead of "README.md", you'll get a "BlobNotFound" error.

---

## Part 3: Understanding Blob URLs and Public Access

### Blob URL Structure

Every blob in Azure Storage has a public URL following this pattern:

*[SHOW ON SCREEN: URL pattern]*

```
https://<sa-name>.blob.core.windows.net/<container>/<blob-name>
```

Let's try downloading the README file using curl and this URL pattern.

*[SHOW ON SCREEN: Command being typed]*

```bash
curl -o download.md https://<sa-name>.blob.core.windows.net/labs/storage-blob/README.md
```

*[SHOW ON SCREEN: Command executing]*

Now let's look at what we downloaded:

```bash
cat download.md
```

*[SHOW ON SCREEN: XML error message displayed]*

Notice that we got an XML error message instead of the file content! This is because the container is not enabled for public blob access. By default, blobs are private and require authentication.

---

## Part 4: Shared Access Signatures (SAS Tokens)

### Generating a Simple SAS Token

So how do we give someone access to a blob without making it public? This is where Shared Access Signatures, or SAS tokens, come in.

Let's generate a SAS token using the Azure Portal. I'll navigate to the storage account, find the blob, click the ellipsis, and select "Generate SAS".

*[SHOW ON SCREEN: Portal navigation - Storage Account → Containers → labs → storage-blob/README.md → ellipsis → Generate SAS]*

In the SAS configuration panel, I'll:
- Set permissions to read-only
- Set the expiry time to 1 hour from now
- Click Generate SAS token and URL

*[SHOW ON SCREEN: SAS generation panel]*

Now we have a blob SAS URL. Notice how it includes query parameters - the SAS token itself is embedded in the URL.

*[SHOW ON SCREEN: Example URL structure without real token]*

```
https://<sa-name>.blob.core.windows.net/labs/storage-blob/README.md?<sas-token>
```

Let's try downloading the file again, this time using the SAS URL:

*[SHOW ON SCREEN: Command being typed]*

```bash
curl -o download2.md '<blob-url-with-sas-token>'
cat download2.md
```

*[SHOW ON SCREEN: File content displayed successfully]*

Success! This time we see the actual file content because the SAS token authenticated our request.

### Important Security Considerations

You can safely share this SAS token because:
1. It has limited permissions - in this case, read-only
2. It has a limited timeframe - after one hour, it expires automatically
3. It only grants access to this specific blob

However, there's one limitation: a simple SAS token like this cannot be revoked. Once issued, it remains valid until it expires. For better control, we need stored access policies.

---

## Part 5: Stored Access Policies

### Creating a Stored Access Policy

Stored access policies provide better control over SAS tokens by allowing revocation. Let's create a read-only access policy for our container.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage container policy create -n labs-reader --container-name labs --permissions r --account-name <sa-name>
```

Now we have a policy named "labs-reader" with read permissions. Let's generate a SAS token that's backed by this policy.

### Generating a Policy-Based SAS Token

The format for the expiry date needs to be YYYY-MM-DDTHH:MMZ. Let's generate a token that expires at a specific time.

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage blob generate-sas -n 'storage-blob/README.md' --container-name labs --policy-name labs-reader --full-uri --expiry '2025-12-31T23:59Z' --account-name <sa-name>
```

*[SHOW ON SCREEN: Generated SAS URL]*

Let's verify this token works by downloading the file:

*[SHOW ON SCREEN: Command being typed]*

```bash
curl -o download3.md "<blob-url-with-sas-token>"
cat download3.md
```

*[SHOW ON SCREEN: File content displayed]*

Perfect! The file downloads successfully because the token is valid and the policy allows read access.

### Revoking Access by Deleting the Policy

Now here's the powerful part - watch what happens when we delete the stored access policy:

*[SHOW ON SCREEN: Command being typed]*

```bash
az storage container policy delete -n labs-reader --container-name labs --account-name <sa-name>
```

The policy is now deleted. Let's try downloading the file again using the exact same SAS token:

*[SHOW ON SCREEN: Command being typed]*

```bash
curl -o download4.md "<blob-url-with-sas-token>"
cat download4.md
```

*[SHOW ON SCREEN: XML authentication failure message]*

Notice the XML authentication failure! Even though the SAS token hasn't expired, it's no longer valid because the policy it depends on has been deleted.

This is the key advantage of stored access policies - you can revoke access at any time by deleting or modifying the policy, even if the SAS tokens are still within their expiry window.

---

## Part 6: Storage Access Tiers

### Understanding Access Tiers

Blob Storage offers different access tiers to balance performance and cost:
- **Hot** tier: Fast access, higher storage cost, lower access cost
- **Cool** tier: Slower access, lower storage cost, higher access cost, 30-day minimum
- **Archive** tier: Offline storage, lowest storage cost, highest rehydration cost

### The Lab Challenge

For the lab exercise, you'll need to change the README file to the Archive tier and then try to download it. You'll discover that archived blobs aren't immediately accessible - they need to be rehydrated first.

The question is: What do you need to do to gain access to archived blobs?

I'll give you a hint: Check the Azure documentation on blob rehydration. You'll need to change the access tier back to Hot or Cool before you can download the file, and this process can take several hours.

*[SHOW ON SCREEN: Command to change tier]*

```bash
az storage blob set-tier --account-name <sa-name> --container-name labs --name 'storage-blob/README.md' --tier Archive
```

Try to access it now, and you'll see why the Archive tier is truly for long-term, rarely accessed data.

---

## Conclusion

In this lab, we've covered:
- Creating storage accounts and containers with the Azure CLI
- Uploading files in bulk with filtering patterns
- Understanding blob URLs and public access
- Generating and using SAS tokens for secure access
- Creating stored access policies for revocable access control
- Working with storage access tiers

These are all critical skills for the AZ-204 exam and for working with Azure Blob Storage in production environments.

When you're ready, don't forget to clean up your resources:

```bash
az group delete -y -n labs-storage-blob --no-wait
```

Great work! In the next session, we'll dive deeper into exam-specific topics like metadata management, lifecycle policies, and static website hosting.
