# Azure Storage Accounts - Quickfire Questions

## Question 1
What is an Azure Storage Account?


- A) A resource that provides a unique namespace for storing Azure Storage data (blobs, files, queues, tables)
- B) A billing account
- C) A virtual machine
- D) A database service

**Answer: A**
Storage Accounts provide a unique namespace and contain blob containers, file shares, queues, and tables.
---
## Question 2
What are the types of Azure Storage services?


- A) Blob (object storage), Files (SMB shares), Queue (messaging), Table (NoSQL)
- B) Only file shares
- C) Only blobs
- D) Only databases

**Answer: A**
Azure Storage provides Blob storage, Azure Files, Queue storage, and Table storage under one account.
---
## Question 3
What are the storage account redundancy options?


- A) Only local backups
- B) LRS, ZRS, GRS, GZRS, RA-GRS, RA-GZRS
- C) Manual replication only
- D) Only single copy

**Answer: B**
Options: Locally Redundant (LRS), Zone-Redundant (ZRS), Geo-Redundant (GRS/RA-GRS), Geo-Zone-Redundant (GZRS/RA-GZRS).
---
## Question 4
What does LRS (Locally Redundant Storage) provide?


- A) Three synchronous copies within a single datacenter
- B) Replication across regions
- C) One copy only
- D) Replication across availability zones

**Answer: A**
LRS maintains 3 synchronous replicas in a single physical location within one region, protecting against hardware failures.
---
## Question 5
What is the difference between GRS and RA-GRS?


- A) RA-GRS provides read access to the secondary region; GRS does not
- B) GRS is cheaper
- C) GRS is faster
- D) No difference

**Answer: A**
GRS replicates to secondary region (read-only during failover). RA-GRS allows read access to secondary region anytime.
---
## Question 6
What are the storage account performance tiers?


- A) Basic and Advanced
- B) Standard (HDD) and Premium (SSD)
- C) Fast and Slow
- D) Free and Paid

**Answer: B**
Standard uses HDD for cost-effective storage. Premium uses SSD for low-latency, high-throughput scenarios.
---
## Question 7
What access tiers are available for blob storage?


- A) Only one tier
- B) Fast and Slow
- C) Hot, Cool, Cold, Archive
- D) Public and Private

**Answer: C**
Hot (frequent access), Cool (infrequent, 30+ days), Cold (rare, 90+ days), Archive (rarely accessed, 180+ days).
---
## Question 8
What is the purpose of a Storage Account access key?


- A) Full access credential for programmatic access to storage services
- B) Read-only access
- C) Network access control
- D) Encryption key

**Answer: A**
Access keys provide full administrative access to the storage account and all its data. Each account has 2 keys.
---
## Question 9
What is a Shared Access Signature (SAS)?


- A) An encryption method
- B) A URI granting limited, time-bound access to storage resources
- C) A password
- D) A network protocol

**Answer: B**
SAS tokens grant delegated access with specific permissions, time bounds, and IP restrictions without sharing account keys.
---
## Question 10
What protocol does Azure Files use?


- A) FTP
- B) HTTP only
- C) SMB 3.0 (and NFS 4.1 for premium)
- D) SFTP only

**Answer: C**
Azure Files supports SMB 3.0 protocol (mountable on Windows, Linux, macOS) and NFS 4.1 for Premium tier.