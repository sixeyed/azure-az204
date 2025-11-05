# Azure Blob Storage - AZ-204 Exam Introduction

Excellent work on the hands-on exercises! Now let's shift to what you need to know about Azure Blob Storage for the AZ-204 certification exam.

## Exam Weight

Blob Storage is a major topic, accounting for a significant portion of the "Develop for Azure Storage" domain, which makes up 15-20% of the total AZ-204 exam. Expect multiple questions on blob types, SAS tokens, lifecycle policies, and access tiers.

## What We'll Cover

We'll start with **blob types** - the three kinds Azure supports. Block blobs for text and binary data (most common), append blobs optimized for append operations like logs, and page blobs for random read/write operations used by virtual hard disks. The exam tests when to use each type.

**Access tiers** is heavily tested. Hot tier for frequently accessed data (fast but expensive storage), Cool tier for infrequent access with 30-day minimum storage (cheaper storage, higher access costs), and Archive tier for rare access with 180-day minimum (cheapest storage, but accessing data takes hours). Know the cost tradeoffs and minimum duration requirements - the exam loves questions about choosing the right tier for specific scenarios.

**SAS tokens and security** appears on nearly every exam. You need to understand how to generate SAS tokens with specific permissions (read, write, delete, list), set appropriate expiration times, and grant access to specific blobs, containers, or entire storage accounts. Know the difference between simple SAS tokens (can't be revoked) and policy-based SAS tokens (revocable by deleting the stored access policy). The exam tests which approach to use for different security requirements.

**Stored access policies** provide centralized access control. We'll cover how to create policies with `az storage container policy create`, reference them when generating SAS tokens, and revoke access by deleting policies. This is your answer to "how do I revoke a SAS token before it expires?"

We'll dive into **lifecycle management policies** - automated rules that transition blobs to cooler tiers or delete them based on age. These are crucial for cost optimization and appear frequently in exam scenarios. Know how to create policies that move 30-day-old blobs to Cool tier and delete blobs older than 180 days.

**CLI commands** you must memorize include creating storage accounts and containers, uploading with patterns and filters, generating SAS tokens, managing stored access policies, and setting blob access tiers. The exam tests command syntax and parameter names.

**Blob versioning and soft delete** are important features for data protection. Versioning keeps previous versions of blobs automatically, while soft delete allows recovery of deleted blobs within a retention period. Know when to recommend each feature.

**Static website hosting** from Blob Storage is another exam topic. You can host entire static websites (HTML, CSS, JavaScript) directly from a special $web container. Know the configuration steps and when this is appropriate versus using App Service.

**Metadata and properties** frequently appear in questions. Understand the difference between system properties (read-only like Content-Type and ETag) and user-defined metadata (custom key-value pairs you can set).

Finally, we'll cover **common exam scenarios**: when to use which blob type, how to implement lifecycle policies, securing blob access with SAS tokens, optimizing costs with access tiers, and implementing data retention and recovery strategies.

Ready to master Blob Storage for the AZ-204? Let's explore the exam-focused content!
