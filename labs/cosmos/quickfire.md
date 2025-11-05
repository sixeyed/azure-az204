# Azure Cosmos DB - Quickfire Questions

## Question 1
What is Azure Cosmos DB?


- A) A relational database only
- B) A globally distributed, multi-model NoSQL database service
- C) A messaging service
- D) A file storage service

**Answer: B**
Cosmos DB is a fully managed NoSQL database with turnkey global distribution, multi-model APIs, and guaranteed low latency.
---
## Question 2
What APIs does Cosmos DB support?


- A) Only Key-Value
- B) NoSQL (SQL), MongoDB, Cassandra, Table, Gremlin (Graph)
- C) Only SQL
- D) Only MongoDB

**Answer: B**
Cosmos DB supports multiple APIs: NoSQL (formerly SQL API), MongoDB, Cassandra, Table, and Gremlin for different data models.
---
## Question 3
What is a Request Unit (RU) in Cosmos DB?


- A) Abstracted measure of compute, memory, and I/O cost for database operations
- B) Storage unit
- C) Network bandwidth
- D) User account

**Answer: A**
RU/s (Request Units per second) represents the throughput cost. Reading 1 KB = 1 RU; writes and queries cost more.
---
## Question 4
What consistency levels does Cosmos DB offer?


- A) Strong, Bounded Staleness, Session, Consistent Prefix, Eventual
- B) Only strong consistency
- C) One size fits all
- D) Only eventual consistency

**Answer: A**
Five levels balancing consistency, availability, latency, and throughput from Strong (highest consistency) to Eventual (lowest latency).
---
## Question 5
What is the default consistency level for Cosmos DB?


- A) Session
- B) No default
- C) Strong
- D) Eventual

**Answer: A**
Session consistency provides the best balance for most applications: strong consistency within a session, eventual across sessions.
---
## Question 6
What is a partition key in Cosmos DB?


- A) Property used to distribute data across physical partitions for scale
- B) Encryption key
- C) Index key
- D) Primary key

**Answer: A**
Partition key determines how data is distributed. Good partition keys have high cardinality and evenly distribute requests.
---
## Question 7
What is global distribution in Cosmos DB?


- A) Ability to replicate data across multiple Azure regions with automatic failover
- B) Backup to multiple regions
- C) CDN integration
- D) Load balancing only

**Answer: A**
Cosmos DB can replicate data to any Azure region with single-click, providing low-latency access globally.
---
## Question 8
What is the difference between provisioned and serverless throughput?


- A) Serverless is always cheaper
- B) Provisioned reserves RU/s capacity; Serverless pays per request without reservation
- C) No difference
- D) Provisioned is slower

**Answer: B**
Provisioned: reserve RU/s (predictable cost). Serverless: pay per request (good for sporadic/unpredictable workloads).
---
## Question 9
What is autoscale in Cosmos DB?


- A) Fixed scaling
- B) Scales storage only
- C) Manual scaling only
- D) Automatically adjusts RU/s between configured min/max based on demand

**Answer: D**
Autoscale automatically scales throughput from 10% to 100% of max RU/s based on actual usage.
---
## Question 10
What SLA does Cosmos DB provide?


- A) Best effort
- B) 99% availability
- C) 99.99% (single region) to 99.999% (multi-region) with guarantees for latency, throughput, consistency
- D) No SLA

**Answer: C**
Cosmos DB offers comprehensive SLAs covering availability, latency (<10ms reads/writes at P99), throughput, and consistency.