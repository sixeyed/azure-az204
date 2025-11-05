# Azure Storage Accounts - Quickfire Questions

## Question 1
What is an Azure Storage Account?

- A) A billing account
- B) A resource that provides a unique namespace for storing Azure Storage data (blobs, files, queues, tables)
- C) A database service
- D) A virtual machine

**Answer: B**
Storage Accounts provide a unique namespace and contain blob containers, file shares, queues, and tables.

---

## Question 2
What are the types of Azure Storage services?

- A) Only blobs
- B) Blob (object storage), Files (SMB shares), Queue (messaging), Table (NoSQL)
- C) Only databases
- D) Only file shares

**Answer: B**
Azure Storage provides Blob storage, Azure Files, Queue storage, and Table storage under one account.

---

## Question 3
What are the storage account redundancy options?

- A) Only single copy
- B) LRS, ZRS, GRS, GZRS, RA-GRS, RA-GZRS
- C) Only local backups
- D) Manual replication only

**Answer: B**
Options: Locally Redundant (LRS), Zone-Redundant (ZRS), Geo-Redundant (GRS/RA-GRS), Geo-Zone-Redundant (GZRS/RA-GZRS).

---

## Question 4
What does LRS (Locally Redundant Storage) provide?

- A) Replication across regions
- B) Three synchronous copies within a single datacenter
- C) One copy only
- D) Replication across availability zones

**Answer: B**
LRS maintains 3 synchronous replicas in a single physical location within one region, protecting against hardware failures.

---

## Question 5
What is the difference between GRS and RA-GRS?

- A) No difference
- B) RA-GRS provides read access to the secondary region; GRS does not
- C) GRS is cheaper
- D) GRS is faster

**Answer: B**
GRS replicates to secondary region (read-only during failover). RA-GRS allows read access to secondary region anytime.

---

## Question 6
What are the storage account performance tiers?

- A) Fast and Slow
- B) Standard (HDD) and Premium (SSD)
- C) Basic and Advanced
- D) Free and Paid

**Answer: B**
Standard uses HDD for cost-effective storage. Premium uses SSD for low-latency, high-throughput scenarios.

---

## Question 7
What access tiers are available for blob storage?

- A) Only one tier
- B) Hot, Cool, Cold, Archive
- C) Fast and Slow
- D) Public and Private

**Answer: B**
Hot (frequent access), Cool (infrequent, 30+ days), Cold (rare, 90+ days), Archive (rarely accessed, 180+ days).

---

## Question 8
What is the purpose of a Storage Account access key?

- A) Encryption key
- B) Full access credential for programmatic access to storage services
- C) Read-only access
- D) Network access control

**Answer: B**
Access keys provide full administrative access to the storage account and all its data. Each account has 2 keys.

---

## Question 9
What is a Shared Access Signature (SAS)?

- A) A password
- B) A URI granting limited, time-bound access to storage resources
- C) An encryption method
- D) A network protocol

**Answer: B**
SAS tokens grant delegated access with specific permissions, time bounds, and IP restrictions without sharing account keys.

---

## Question 10
What protocol does Azure Files use?

- A) HTTP only
- B) SMB 3.0 (and NFS 4.1 for premium)
- C) FTP
- D) SFTP only

**Answer: B**
Azure Files supports SMB 3.0 protocol (mountable on Windows, Linux, macOS) and NFS 4.1 for Premium tier.
