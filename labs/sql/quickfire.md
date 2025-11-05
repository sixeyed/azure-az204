# Azure SQL Database - Quickfire Questions

## Question 1
What is Azure SQL Database?


- A) Cache service
- B) NoSQL database
- C) Fully managed relational database service based on Microsoft SQL Server
- D) File storage

**Answer: C**
Azure SQL Database is a PaaS relational database offering automatic management, scaling, and high availability.
---
## Question 2
What are the purchasing models for SQL Database?


- A) Free and Paid
- B) Small and Large
- C) Only one model
- D) DTU-based and vCore-based

**Answer: D**
DTU (Database Transaction Unit) bundles compute/storage. vCore provides granular control over CPU/memory/storage.
---
## Question 3
What is a DTU?


- A) Database Type Unit
- B) Data Transfer Unit
- C) Database Transaction Unit - blended measure of compute, memory, I/O
- D) Disk Transfer Unit

**Answer: C**
DTU abstracts resource allocation into single unit, simplifying purchasing for typical workloads.
---
## Question 4
What service tiers are available in vCore model?


- A) Only one tier
- B) Basic and Premium
- C) General Purpose, Business Critical, Hyperscale
- D) Free and Paid

**Answer: C**
General Purpose (balanced), Business Critical (high performance, high availability), Hyperscale (large databases, fast scaling).
---
## Question 5
What is the maximum database size in Hyperscale?


- A) 4 TB
- B) 10 TB
- C) 100 TB (practically unlimited)
- D) 1 TB

**Answer: C**
Hyperscale supports up to 100 TB and can scale storage dynamically without downtime.
---
## Question 6
What high availability is built into SQL Database?


- A) Best effort
- B) No HA
- C) Manual failover only
- D) 99.99% SLA with automatic replicas and failover

**Answer: D**
Built-in HA uses replicas. Business Critical tier includes readable secondaries for load distribution.
---
## Question 7
What is geo-replication in SQL Database?


- A) Not available
- B) Asynchronous replication to secondary databases in other regions
- C) Local replication only
- D) Synchronous only

**Answer: B**
Active geo-replication creates readable secondaries in different regions for DR and read scale-out.
---
## Question 8
What is a failover group?


- A) Backup group
- B) Server group
- C) User group
- D) Group of databases with automatic failover to secondary region

**Answer: D**
Failover groups enable automatic failover of multiple databases with single read-write and read-only listener endpoints.
---
## Question 9
Does SQL Database support automatic backups?


- A) No backups
- B) Yes, automatic full, differential, and transaction log backups with point-in-time restore
- C) Manual only
- D) Weekly only

**Answer: B**
Automated backups enable point-in-time restore up to 7-35 days (configurable retention).
---
## Question 10
What authentication methods does SQL Database support?


- A) SQL authentication and Azure AD authentication
- B) Anonymous
- C) SQL auth only
- D) No authentication

**Answer: A**
Both SQL authentication (username/password) and Azure AD authentication (integrated, MFA-enabled).