# Azure SQL Database - Quickfire Questions

## Question 1
What is Azure SQL Database?

- A) NoSQL database
- B) Fully managed relational database service based on Microsoft SQL Server
- C) File storage
- D) Cache service

**Answer: B**
Azure SQL Database is a PaaS relational database offering automatic management, scaling, and high availability.

---

## Question 2
What are the purchasing models for SQL Database?

- A) Only one model
- B) DTU-based and vCore-based
- C) Free and Paid
- D) Small and Large

**Answer: B**
DTU (Database Transaction Unit) bundles compute/storage. vCore provides granular control over CPU/memory/storage.

---

## Question 3
What is a DTU?

- A) Data Transfer Unit
- B) Database Transaction Unit - blended measure of compute, memory, I/O
- C) Disk Transfer Unit
- D) Database Type Unit

**Answer: B**
DTU abstracts resource allocation into single unit, simplifying purchasing for typical workloads.

---

## Question 4
What service tiers are available in vCore model?

- A) Only one tier
- B) General Purpose, Business Critical, Hyperscale
- C) Basic and Premium
- D) Free and Paid

**Answer: B**
General Purpose (balanced), Business Critical (high performance, high availability), Hyperscale (large databases, fast scaling).

---

## Question 5
What is the maximum database size in Hyperscale?

- A) 1 TB
- B) 100 TB (practically unlimited)
- C) 10 TB
- D) 4 TB

**Answer: B**
Hyperscale supports up to 100 TB and can scale storage dynamically without downtime.

---

## Question 6
What high availability is built into SQL Database?

- A) No HA
- B) 99.99% SLA with automatic replicas and failover
- C) Manual failover only
- D) Best effort

**Answer: B**
Built-in HA uses replicas. Business Critical tier includes readable secondaries for load distribution.

---

## Question 7
What is geo-replication in SQL Database?

- A) Local replication only
- B) Asynchronous replication to secondary databases in other regions
- C) Synchronous only
- D) Not available

**Answer: B**
Active geo-replication creates readable secondaries in different regions for DR and read scale-out.

---

## Question 8
What is a failover group?

- A) User group
- B) Group of databases with automatic failover to secondary region
- C) Server group
- D) Backup group

**Answer: B**
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

- A) SQL auth only
- B) SQL authentication and Azure AD authentication
- C) Anonymous
- D) No authentication

**Answer: B**
Both SQL authentication (username/password) and Azure AD authentication (integrated, MFA-enabled).
