# Azure Blob Storage - Lab Exercises Walkthrough

## Introduction to the Lab

Welcome to the Azure Blob Storage hands-on lab. In this session, we'll work through practical exercises that cover the more advanced features of Blob Storage, including SAS tokens, stored access policies, and storage access tiers. Before we begin, make sure you have the Azure CLI installed and you're logged in to your Azure subscription. Let's get started!

## Part 1: Managing Blob Storage with the Azure CLI

### Creating the Resource Group and Storage Account

First, let's create a resource group to organize all our lab resources. We're using az group create with -n set to "labs-storage-blob", placing it in West Europe with -l westeurope, and adding a tag called "courselabs" with the value "azure" using --tags. This helps us identify and manage resources that belong to this course - you can easily find and clean up all course resources by filtering on this tag.

Next, we need to create a storage account. Remember, storage account names must be globally unique across all of Azure and can only contain lowercase letters and numbers - no hyphens, underscores, capital letters, or special characters. Choose a name that's unique to you - something like "sacourseyourname123" works well. We're using az storage account create with -g for the resource group we just created, -l westeurope for the location, --sku Standard_LRS for locally redundant storage, and -n with your unique storage account name. Standard_LRS is the most cost-effective option for our lab exercises, providing three synchronous copies of your data within a single datacenter.

### Creating a Blob Container

Now that we have a storage account, let's create a container. In Blob Storage, containers are like folders - they organize your blobs into logical groups and serve as the boundary for access policies and security settings. We're using az storage container create with -n labs for the container name, -g for the resource group, and --account-name with your storage account name. Great! We now have a container named "labs" where we can upload files.

## Part 2: Uploading Files in Bulk

### Understanding the Upload Batch Command

The Azure CLI has a powerful feature called upload-batch that lets you upload multiple files at once, preserving directory structure. Let's explore this with a dry run first to see what would happen without actually uploading anything.

A dry run shows you what would happen without actually performing the operation - this is a great way to verify your command before executing it and avoiding mistakes. We're using az storage blob upload-batch with -d labs for the destination container, -s ./labs for the source directory on your local machine, --dryrun to simulate without uploading, -o table for readable table output, and --account-name with your storage account.

Looking at the table output, the command would upload every file from the labs directory, preserving the entire folder structure. Each row shows the blob URL where the file would be stored and the file type based on its extension. This gives you a preview of exactly what will be uploaded and where it will go in the container.

### Filtering Files with Patterns

But what if we only want to upload certain types of files? Let's say we only want to upload markdown files. We can use the pattern parameter to filter by file extension or name pattern.

First, let's do another dry run to see which files would be uploaded when we filter for markdown files. We're adding --pattern '*.md' to match only files ending in .md. Perfect! Now we see only the markdown files in the output - all the other file types are filtered out. This pattern matching is very useful when you have mixed content but only want to upload specific file types.

Let's do the actual upload by removing the --dryrun flag. We're using the same command but without the dry run parameter, so it will actually upload the markdown files.

Looking at the output, each successful upload shows the blob URL where the file now lives, along with generated eTags and last modified timestamps. These eTags are important for HTTP caching and concurrency control - they're essentially version identifiers that change whenever the blob changes.

### Listing and Inspecting Blobs

Let's verify that our files were uploaded correctly. We can list the blobs in a specific directory using the directory list command. We're using az storage blob directory list with -c labs for the container name, -d 'storage-blob' to list files within this virtual directory path, -o table for readable output, and --account-name with your storage account name.

You'll notice a warning that this command is deprecated - the Azure CLI evolves over time, and commands occasionally get replaced with better alternatives. Always check for deprecated commands when you upgrade your CLI to the latest version.

Now let's get detailed information about a specific blob. The storage blob show command retrieves metadata and properties for a blob. We're using az storage blob show with --container-name labs, --name 'storage-blob/README.md' specifying the full blob path, -o table for formatting, and --account-name. The output shows properties like content type, etag, last modified time, size, and more.

Important note: blob names are case-sensitive! If you try "readme.md" instead of "README.md", you'll get a "BlobNotFound" error. Azure Storage treats these as completely different files, just like Linux filesystems.

## Part 3: Understanding Blob URLs and Public Access

### Blob URL Structure

Every blob in Azure Storage has a public URL following a predictable pattern: https://your-storage-account-name.blob.core.windows.net/container-name/blob-name. This URL structure is consistent and makes it easy to construct URLs programmatically.

Let's try downloading the README file using curl and this URL pattern. We're using curl with -o download.md to save the output to a local file, followed by the full blob URL constructed from your storage account name.

Now let's look at what we downloaded using cat download.md. Notice that we got an XML error message instead of the file content! The error says something like "ResourceNotFound" or "PublicAccessNotPermitted". This is because the container is not enabled for public blob access. By default, blobs are private and require authentication to access. This is a security feature - you don't want your data publicly accessible unless you explicitly choose to make it so.

## Part 4: Shared Access Signatures (SAS Tokens)

### Generating a Simple SAS Token

So how do we give someone access to a blob without making the entire container public? This is where Shared Access Signatures, or SAS tokens, come in. A SAS token is like a temporary key that grants limited access to specific resources.

Let's generate a SAS token using the Azure Portal. Navigate to the storage account, click on Containers, find the labs container, browse to storage-blob folder, locate README.md, click the ellipsis button (three dots), and select "Generate SAS". In the SAS configuration panel, we'll set permissions to read-only so the token can only download, not modify or delete the blob. We'll set the expiry time to 1 hour from now, giving temporary access that automatically expires. Then click Generate SAS token and URL.

Now we have a blob SAS URL. Notice how it includes query parameters appended to the blob URL - the SAS token itself is embedded in the URL as query string parameters. The URL structure looks like: https://your-storage-account-name.blob.core.windows.net/labs/storage-blob/README.md?sp=r&st=...&se=...&sv=...&sr=b&sig=... where each parameter has specific meaning.

Let's try downloading the file again, this time using the SAS URL. Make sure to put the entire URL in single quotes because it contains special characters like ampersands that would confuse the shell. Run curl -o download2.md followed by your full SAS URL in quotes, then cat download2.md to view the contents. Success! This time we see the actual file content because the SAS token authenticated our request. The token proved we have permission to access this specific blob.

### Important Security Considerations

You can safely share this SAS token because it has several built-in security features. It has limited permissions - in this case, read-only, so recipients can't modify or delete the blob. It has a limited timeframe - after one hour, it expires automatically and becomes completely useless. And it only grants access to this specific blob, not other blobs in the container or storage account.

However, there's one limitation with simple SAS tokens like this: they cannot be revoked before expiration. Once issued, the token remains valid until it expires naturally. If you accidentally share it with the wrong person or need to revoke access immediately, you can't - you have to wait for expiration or regenerate your storage account keys which would invalidate all SAS tokens. For better control, we need stored access policies.

## Part 5: Stored Access Policies

### Creating a Stored Access Policy

Stored access policies provide better control over SAS tokens by allowing revocation at any time. Let's create a read-only access policy for our container that we can modify or delete to control access.

We're using az storage container policy create with -n labs-reader as the policy name, --container-name labs for which container this applies to, --permissions r for read-only access, and --account-name with your storage account. Now we have a policy named "labs-reader" with read permissions stored in the container metadata. This policy can be referenced by SAS tokens, creating a layer of indirection.

### Generating a Policy-Based SAS Token

The format for the expiry date needs to be in ISO 8601 format: YYYY-MM-DDTHH:MMZ. Let's generate a token that expires at a specific time far in the future. We're using az storage blob generate-sas with -n 'storage-blob/README.md' for the blob name, --container-name labs, --policy-name labs-reader to reference our stored policy, --full-uri to get the complete URL not just the token, --expiry '2025-12-31T23:59Z' for an expiration date, and --account-name.

Looking at the generated SAS URL, it includes a reference to the stored access policy in the parameters. This is the key difference from the simple SAS we created earlier.

Let's verify this token works by downloading the file. Run curl -o download3.md with your SAS URL in quotes, then cat download3.md. Perfect! The file downloads successfully because the token is valid and the policy allows read access. So far this seems the same as before, but watch what happens next.

### Revoking Access by Deleting the Policy

Now here's the powerful part - watch what happens when we delete the stored access policy. We're using az storage container policy delete with -n labs-reader for the policy name, --container-name labs, and --account-name. The policy is now deleted from the container metadata.

Let's try downloading the file again using the exact same SAS token we just used successfully. Run curl -o download4.md with the same SAS URL, then cat download4.md to see what we got. Notice we get an XML authentication failure message instead of the file content! Even though the SAS token hasn't expired - we set expiration for 2025 - it's no longer valid because the policy it depends on has been deleted.

This is the key advantage of stored access policies - you can revoke access at any time by deleting or modifying the policy, even if the SAS tokens are still within their expiry window. This gives you much better control over access management, especially important when dealing with sensitive data or third-party integrations.

## Part 6: Storage Access Tiers

### Understanding Access Tiers

Blob Storage offers different access tiers to balance performance and cost based on how frequently you access your data. The Hot tier provides fast access with higher storage cost but lower access cost - use this for frequently accessed data. The Cool tier offers slower access with lower storage cost but higher access cost, with a 30-day minimum storage duration - good for backups and archives accessed occasionally. The Archive tier is offline storage with the lowest storage cost but highest rehydration cost and a 180-day minimum - perfect for long-term archives that are rarely accessed.

### The Lab Challenge

For the lab exercise, you'll need to change the README file to the Archive tier and then try to download it. You'll discover that archived blobs aren't immediately accessible - they're stored offline and need to be rehydrated first before you can access them.

The question is: What do you need to do to gain access to archived blobs? Here's a hint: Check the Azure documentation on blob rehydration. You'll need to change the access tier back to Hot or Cool before you can download the file, and this rehydration process can take several hours depending on the priority you specify. There are two rehydration priorities - Standard which takes up to 15 hours, and High which takes under one hour but costs more.

Let's change the tier to Archive to see what happens. We're using az storage blob set-tier with --account-name, --container-name labs, --name 'storage-blob/README.md' for the specific blob, and --tier Archive to move it to archive storage. Try to access it now by downloading with your SAS URL, and you'll see an error about the blob being archived. You'll see why the Archive tier is truly for long-term, rarely accessed data - the tradeoff for extremely low storage costs is that data isn't immediately available.

## Conclusion

In this lab, we've covered essential Blob Storage concepts and operations. We created storage accounts and containers with the Azure CLI, understanding the hierarchy and organization. We uploaded files in bulk with filtering patterns, seeing how to efficiently manage multiple files at once. We learned about blob URLs and public access controls, understanding Azure's security-first approach. We generated and used SAS tokens for secure, temporary access without exposing storage account keys. We created stored access policies for revocable access control, giving us fine-grained security management. And we explored storage access tiers, learning how to optimize costs based on access patterns.

These are all critical skills for the AZ-204 exam and for working with Azure Blob Storage in production environments. You now understand both the basic operations and the advanced security and cost management features.

When you're ready, don't forget to clean up your resources using az group delete -y -n labs-storage-blob --no-wait to remove the resource group and everything within it. Great work! In the next session, we'll dive deeper into exam-specific topics like metadata management, lifecycle policies for automatic tier transitions, and static website hosting with Blob Storage.
