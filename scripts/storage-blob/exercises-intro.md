# Azure Blob Storage - Exercises Introduction

We've covered what Blob Storage is and why it's the right solution for file storage in cloud applications. Now let's get hands-on with the Azure CLI and see these concepts in action.

## What's Ahead

You'll start by **creating a storage account and blob container** using the Azure CLI. You'll learn why storage account names must be globally unique and can only contain lowercase letters and numbers - no hyphens or special characters allowed, which is different from most Azure resources.

Next, you'll explore the powerful **upload-batch command** for uploading multiple files at once while preserving directory structure. You'll use the `--dryrun` flag first to preview what would happen without actually uploading - a great practice to avoid mistakes. Then you'll use the `--pattern` parameter to filter and upload only markdown files, seeing how selective uploads work. You'll inspect the uploaded blobs with `az storage blob show` and learn that blob names are case-sensitive - "README.md" and "readme.md" are completely different files!

Then comes an important lesson about **public access and security**. You'll attempt to download a blob using curl and its public URL, but you'll get an authentication error because containers aren't publicly accessible by default. This is a security feature - your data is private unless you explicitly choose otherwise.

This leads to **Shared Access Signatures (SAS tokens)**. You'll generate a SAS token in the Portal with read-only permissions and a 1-hour expiry, then successfully download the blob using the SAS URL. You'll learn the security benefits: limited permissions, limited timeframe, and access to specific blobs only. But there's a limitation - simple SAS tokens cannot be revoked before expiration.

That's where **stored access policies** come in. You'll create a read-only policy using `az storage container policy create`, generate a policy-based SAS token, and verify it works. Then comes the magic: you'll delete the policy and watch as the previously working SAS token immediately fails - even though it hasn't expired. This demonstrates revocable access control!

Finally, you'll explore **storage access tiers** by changing a blob to Archive tier and discovering that archived blobs aren't immediately accessible - they need rehydration first, which can take hours. This teaches the tradeoff between storage cost and access speed.

Let's dive into Blob Storage hands-on!
