# Azure Cosmos DB - Quickfire Questions

## Question 1
What is Azure Cosmos DB?

- A) A relational database only
- B) A globally distributed, multi-model NoSQL database service
- C) A file storage service
- D) A messaging service

**Answer: B**
Cosmos DB is a fully managed NoSQL database with turnkey global distribution, multi-model APIs, and guaranteed low latency.

---

## Question 2
What APIs does Cosmos DB support?

- A) Only SQL
- B) NoSQL (SQL), MongoDB, Cassandra, Table, Gremlin (Graph)
- C) Only MongoDB
- D) Only Key-Value

**Answer: B**
Cosmos DB supports multiple APIs: NoSQL (formerly SQL API), MongoDB, Cassandra, Table, and Gremlin for different data models.

---

## Question 3
What is a Request Unit (RU) in Cosmos DB?

- A) Storage unit
- B) Abstracted measure of compute, memory, and I/O cost for database operations
- C) Network bandwidth
- D) User account

**Answer: B**
RU/s (Request Units per second) represents the throughput cost. Reading 1 KB = 1 RU; writes and queries cost more.

---

## Question 4
What consistency levels does Cosmos DB offer?

- A) Only strong consistency
- B) Strong, Bounded Staleness, Session, Consistent Prefix, Eventual
- C) Only eventual consistency
- D) One size fits all

**Answer: B**
Five levels balancing consistency, availability, latency, and throughput from Strong (highest consistency) to Eventual (lowest latency).

---

## Question 5
What is the default consistency level for Cosmos DB?

- A) Strong
- B) Session
- C) Eventual
- D) No default

**Answer: B**
Session consistency provides the best balance for most applications: strong consistency within a session, eventual across sessions.

---

## Question 6
What is a partition key in Cosmos DB?

- A) Encryption key
- B) Property used to distribute data across physical partitions for scale
- C) Primary key
- D) Index key

**Answer: B**
Partition key determines how data is distributed. Good partition keys have high cardinality and evenly distribute requests.

---

## Question 7
What is global distribution in Cosmos DB?

- A) CDN integration
- B) Ability to replicate data across multiple Azure regions with automatic failover
- C) Load balancing only
- D) Backup to multiple regions

**Answer: B**
Cosmos DB can replicate data to any Azure region with single-click, providing low-latency access globally.

---

## Question 8
What is the difference between provisioned and serverless throughput?

- A) No difference
- B) Provisioned reserves RU/s capacity; Serverless pays per request without reservation
- C) Serverless is always cheaper
- D) Provisioned is slower

**Answer: B**
Provisioned: reserve RU/s (predictable cost). Serverless: pay per request (good for sporadic/unpredictable workloads).

---

## Question 9
What is autoscale in Cosmos DB?

- A) Manual scaling only
- B) Automatically adjusts RU/s between configured min/max based on demand
- C) Scales storage only
- D) Fixed scaling

**Answer: B**
Autoscale automatically scales throughput from 10% to 100% of max RU/s based on actual usage.

---

## Question 10
What SLA does Cosmos DB provide?

- A) 99% availability
- B) 99.99% (single region) to 99.999% (multi-region) with guarantees for latency, throughput, consistency
- C) No SLA
- D) Best effort

**Answer: B**
Cosmos DB offers comprehensive SLAs covering availability, latency (<10ms reads/writes at P99), throughput, and consistency.
