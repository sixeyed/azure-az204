# Blob Storage

## Reference

Blob storage serves as your own personal cloud storage solution, but it's also a powerful storage backend for applications. When you have scenarios where users can upload files, storing them in blob storage is better than using a relational database. You can even store JSON files in blobs as a cost-effective way to manage reference data in your applications. The documentation covers everything from basic blob operations to advanced features like SAS tokens and storage tiers. The command line interface provides complete control through az storage blob and az storage container commands.

## Managing Blob Storage with the CLI

We explored blob storage using the Portal in the Storage Account lab. Now we'll see the CLI tooling for blobs, which gives us more power and automation capabilities.

**Create the Infrastructure**: We're creating a Resource Group called "labs-storage-blob" and a Storage Account with standard locally redundant storage. Remember that storage account names can only contain lowercase letters and numbers - no special characters, no hyphens, no uppercase letters. Choose a unique name that follows these rules.

**Create a Container**: We're creating a blob container where we can upload some files. We're using az storage container create with the name "labs", specifying our resource group and storage account name. This container will hold all the files we upload during this lab.

**Understanding Batch Upload**: The CLI has a powerful upload-batch command which you can use to upload files to blob storage in bulk. It has a useful dryrun flag which tells you what it would do without actually doing it - this is a great way to verify your command before executing it. We're running az storage blob upload-batch with the destination container "labs", source directory set to the local labs folder, the dryrun flag enabled, and output formatted as a table for readability.

**Inspect Dry Run Results**: The output tells you the target URL and file type for each blob it would upload. This shows you exactly what will happen when you run the command for real. Looking at the output, you can see that the batch upload preserves the file paths from your local directory structure, maintaining the folder hierarchy in blob storage.

**Filter Files with Patterns**: Let's say we only want to upload markdown files. We can use the pattern parameter to filter which files get uploaded. We're adding the pattern parameter set to asterisk dot md to match only files ending in dot md. Running another dry run first shows us only the markdown files would be uploaded - all other file types are filtered out.

**Upload Markdown Files**: Now let's do the actual upload by removing the dryrun flag. We're using the same command but without dry run, so it actually uploads the markdown files to our container. The output shows each blob URL, generated eTag, and Last Modified dates - these eTags are used for HTTP caching and concurrency control, changing whenever the blob content changes.

**List Directory Contents**: Let's check the exercises files are there with a directory list. We're using az storage blob directory list to print out the files in the storage-blob directory within the labs container. Notice the warning that this is a deprecated command - the CLI evolves over time, and commands occasionally get replaced with better alternatives. Always check for deprecated commands when you upgrade to a new version.

**Show Blob Details**: We're using the storage blob show command to print information about the readme file in the storage-blob folder. Remember that blob file names are case-sensitive - if you try "readme.md" instead of "README.md", you'll get a BlobNotFound error. Azure Storage treats these as completely different files, just like Linux filesystems. The output shows file metadata and properties, but not the actual content.

## Shared Access Tokens & Policies

All blobs have a public URL which you can use if you want to download the content. The URL follows a standard pattern combining your storage account name, the blob core windows net domain, the container name, and the blob name.

**Try Public Download**: Let's try to download the README doc using curl with the public blob URL. We're saving the output to a local file and then examining its contents. The output is an XML error string - the container is not enabled for public blobs. Even though the URL is public, the content isn't accessible without authentication.

**Generate SAS Token in Portal**: You can give someone access to the blob without making it public by creating a Shared Access Signature. We're opening the storage-blob/README.md blob in the Portal, clicking the ellipsis button, and selecting Generate SAS. We're creating a SAS key for read-only access to the blob, which is valid for one hour. This gives temporary, limited access without exposing your storage account keys.

**Understanding SAS URLs**: The blob SAS URL you see in the Portal includes query parameters appended to the standard blob URL. These parameters include things like the signature, start time, expiry time, permissions, service version, and resource type. The URL is quite long because it contains all the security information needed to validate the access.

**Download with SAS**: Let's use curl to download the file using the SAS URL. Make sure to wrap the URL in quotes because it contains ampersands and other special characters that would confuse the shell. This time when we examine the file contents, we see the actual README content. The SAS token authenticated our request successfully.

**SAS Security Features**: You can safely share this SAS token because it has built-in security features. It has limited permissions - in this case read-only, so recipients can't modify or delete the blob. It has a limited timeframe - after one hour, it expires automatically and becomes useless. And it only grants access to this specific blob, not other blobs in the container or storage account.

**SAS Limitations**: However, there's one limitation with simple SAS tokens like this - they cannot be revoked before expiration. Once issued, the token remains valid until it expires naturally. If you accidentally share it with the wrong person or need to revoke access immediately, you can't without regenerating your storage account keys, which would invalidate all SAS tokens. For better control, we need stored access policies.

**Create Stored Access Policy**: Let's create a read-only access policy for our container that we can modify or delete to control access. We're using az storage container policy create with the policy name "labs-reader", container name "labs", permissions set to "r" for read-only, and our storage account name. The policy is now stored in the container metadata and can be referenced by SAS tokens.

**Generate Policy-Based SAS**: Now we're generating a SAS token that references this stored policy. The expiry date format needs to be in ISO 8601 format - year-month-day T hour-minute Z. We're using az storage blob generate-sas with the blob name, container name, policy name to reference our stored policy, full-uri flag to get the complete URL not just the token, and an expiry date. The generated SAS URL includes a reference to the stored access policy in the parameters.

**Verify Policy-Based Access**: Let's verify this token works by downloading the file. We're using curl to download with our SAS URL, and the file downloads successfully because the token is valid and the policy allows read access. So far this seems the same as before, but watch what happens next.

**Revoke Access**: Now here's the powerful part - we're deleting the stored access policy using az storage container policy delete. The policy is removed from the container metadata. Let's try downloading the file again using the exact same SAS token we just used successfully. This time we get an XML authentication failure message instead of file content. Even though the SAS token hasn't expired - we set expiration far in the future - it's no longer valid because the policy it depends on has been deleted. This is the key advantage of stored access policies - you can revoke access at any time by deleting or modifying the policy, even if the SAS tokens are still within their expiry window.

## Lab

Blob storage doesn't usually need high performance, and Azure has access tiers to let you get the best mix of performance and storage cost. Hot access is faster but expensive, Cool is cheaper but slower, and Archive is cheapest but requires rehydration before access.

**Your Challenge**: Change the readme for this lab to the archive tier and try to download it. What do you need to do to gain access to archived blobs? This demonstrates the tradeoff between cost and accessibility - Archive tier offers the lowest storage costs but data isn't immediately available.

**Hint**: Check the Azure documentation on blob rehydration and tier changes. You'll need to understand how to move blobs between tiers and what the implications are for access.

## Cleanup

When you're finished with the lab, remember to clean up your resources.

**Delete the Resource Group**: We're using az group delete with -y to confirm without prompting and --no-wait to return immediately without waiting for completion. This removes the entire resource group and all its contents including the storage account, containers, and all blobs. The deletion happens asynchronously in the background.
