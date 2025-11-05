# Azure Blob Storage - Quickfire Questions

## Question 1
What is Azure Blob Storage designed for?

- A) Relational data
- B) Storing massive amounts of unstructured object data (text, binary, images, videos)
- C) Only text files
- D) Virtual machines

**Answer: B**
Blob Storage is optimized for storing unstructured data like documents, images, videos, backups, and logs.

---

## Question 2
What are the three types of blobs?

- A) Small, Medium, Large
- B) Block blobs, Append blobs, Page blobs
- C) Public, Private, Shared
- D) Hot, Cool, Archive

**Answer: B**
Block blobs (most common), Append blobs (logs), Page blobs (VHD files, random read/write).

---

## Question 3
What is a blob container?

- A) A virtual machine
- B) A logical grouping of blobs, similar to a directory/folder
- C) A storage account
- D) A database table

**Answer: B**
Containers organize blobs within a storage account, providing a namespace and access control boundary.

---

## Question 4
What is the maximum size of a block blob?

- A) 100 MB
- B) 1 GB
- C) ~190 TB (4.75 TB × 50,000 blocks)
- D) Unlimited

**Answer: C**
Block blobs support approximately 190 TB (each block up to 4000 MiB, up to 50,000 blocks).

---

## Question 5
What blob access tier provides the lowest storage cost?

- A) Hot
- B) Cool
- C) Cold
- D) Archive

**Answer: D**
Archive tier offers lowest storage cost but highest access cost and latency (hours to rehydrate).

---

## Question 6
What is blob lifecycle management?

- A) Manual deletion
- B) Rule-based policies to automatically transition blobs between tiers or delete them
- C) Backup scheduling
- D) Versioning

**Answer: B**
Lifecycle policies automatically move blobs to cooler tiers or delete them based on age or last access time.

---

## Question 7
What is blob versioning?

- A) API versioning
- B) Automatic maintenance of previous versions when a blob is modified or deleted
- C) Container versioning
- D) Account versioning

**Answer: B**
Versioning automatically creates a new version each time a blob is overwritten, enabling recovery of previous states.

---

## Question 8
What is soft delete for blobs?

- A) Permanent deletion
- B) Retains deleted blobs/versions for a specified retention period, allowing recovery
- C) Compression
- D) Encryption

**Answer: B**
Soft delete protects data from accidental deletion by retaining deleted blobs for a configurable period (up to 365 days).

---

## Question 9
What is the difference between a Service SAS and an Account SAS?

- A) No difference
- B) Service SAS is for a specific resource; Account SAS can access multiple services
- C) Account SAS is more secure
- D) Service SAS is deprecated

**Answer: B**
Service SAS grants access to specific resources (container, blob). Account SAS can access multiple storage services.

---

## Question 10
What is blob immutability?

- A) Blobs cannot be created
- B) WORM (Write Once, Read Many) policy preventing modification or deletion for a period
- C) Blobs cannot be read
- D) Automatic encryption

**Answer: B**
Immutability policies (time-based or legal hold) prevent blob modification/deletion, meeting compliance requirements.
