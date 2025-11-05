# Azure Blob Storage - Quickfire Questions

## Question 1
What is Azure Blob Storage designed for?


- A) Only text files
- B) Relational data
- C) Storing massive amounts of unstructured object data (text, binary, images, videos)
- D) Virtual machines

**Answer: C**
Blob Storage is optimized for storing unstructured data like documents, images, videos, backups, and logs.
---
## Question 2
What are the three types of blobs?


- A) Public, Private, Shared
- B) Block blobs, Append blobs, Page blobs
- C) Hot, Cool, Archive
- D) Small, Medium, Large

**Answer: B**
Block blobs (most common), Append blobs (logs), Page blobs (VHD files, random read/write).
---
## Question 3
What is a blob container?


- A) A database table
- B) A logical grouping of blobs, similar to a directory/folder
- C) A storage account
- D) A virtual machine

**Answer: B**
Containers organize blobs within a storage account, providing a namespace and access control boundary.
---
## Question 4
What is the maximum size of a block blob?


- A) 100 MB
- B) ~190 TB (4.75 TB × 50,000 blocks)
- C) Unlimited
- D) 1 GB

**Answer: B**
Block blobs support approximately 190 TB (each block up to 4000 MiB, up to 50,000 blocks).
---
## Question 5
What blob access tier provides the lowest storage cost?


- A) Hot
- B) Archive
- C) Cold
- D) Cool

**Answer: B**
Archive tier offers lowest storage cost but highest access cost and latency (hours to rehydrate).
---
## Question 6
What is blob lifecycle management?


- A) Backup scheduling
- B) Manual deletion
- C) Rule-based policies to automatically transition blobs between tiers or delete them
- D) Versioning

**Answer: C**
Lifecycle policies automatically move blobs to cooler tiers or delete them based on age or last access time.
---
## Question 7
What is blob versioning?


- A) Container versioning
- B) Account versioning
- C) API versioning
- D) Automatic maintenance of previous versions when a blob is modified or deleted

**Answer: D**
Versioning automatically creates a new version each time a blob is overwritten, enabling recovery of previous states.
---
## Question 8
What is soft delete for blobs?


- A) Retains deleted blobs/versions for a specified retention period, allowing recovery
- B) Permanent deletion
- C) Encryption
- D) Compression

**Answer: A**
Soft delete protects data from accidental deletion by retaining deleted blobs for a configurable period (up to 365 days).
---
## Question 9
What is the difference between a Service SAS and an Account SAS?


- A) Service SAS is for a specific resource; Account SAS can access multiple services
- B) No difference
- C) Account SAS is more secure
- D) Service SAS is deprecated

**Answer: A**
Service SAS grants access to specific resources (container, blob). Account SAS can access multiple storage services.
---
## Question 10
What is blob immutability?


- A) Blobs cannot be created
- B) Blobs cannot be read
- C) Automatic encryption
- D) WORM (Write Once, Read Many) policy preventing modification or deletion for a period

**Answer: D**
Immutability policies (time-based or legal hold) prevent blob modification/deletion, meeting compliance requirements.