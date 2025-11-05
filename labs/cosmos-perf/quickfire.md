# Cosmos DB Performance - Quickfire Questions

## Question 1
What is the most important factor for Cosmos DB performance?


- A) Region selection only
- B) Choosing an appropriate partition key for even distribution
- C) Storage size
- D) Number of indexes

**Answer: B**
A well-chosen partition key ensures even data and request distribution, preventing hot partitions and throttling.
---
## Question 2
What causes throttling (429 errors) in Cosmos DB?


- A) Too much storage
- B) Request rate exceeding provisioned RU/s
- C) Network issues only
- D) Too many users

**Answer: B**
429 (TooManyRequests) occurs when consumed RU/s exceeds provisioned throughput. Solutions: increase RUs or implement retry logic.
---
## Question 3
What is a hot partition?


- A) A partition receiving disproportionate request volume causing throttling
- B) High-temperature storage
- C) A popular database
- D) A backup partition

**Answer: A**
Hot partitions occur with poor partition key choices, concentrating requests on few partitions while others are idle.
---
## Question 4
What query pattern is most efficient in Cosmos DB?


- A) Full table scans
- B) Queries without filters
- C) Single-partition queries with partition key in WHERE clause
- D) Cross-partition queries

**Answer: C**
Queries scoped to a single partition key are most efficient, avoiding fan-out across all partitions.
---
## Question 5
How does indexing affect performance?


- A) No impact
- B) Reduces all costs
- C) Only affects storage
- D) Improves read performance but increases write cost (RUs) and storage

**Answer: D**
Indexes speed up queries but increase write RUs (indexing overhead) and storage. Optimize by indexing only needed properties.
---
## Question 6
What is the purpose of excluding paths from indexing?


- A) Enable encryption
- B) Reduce write RU cost and storage for properties that won't be queried
- C) Improve read speed
- D) Security

**Answer: B**
Excluding unused properties from indexing reduces write costs and storage, improving write throughput.
---
## Question 7
What is direct connectivity mode?


- A) TCP-based connection to Cosmos DB backend, bypassing gateway for lower latency
- B) HTTP only
- C) VPN connection
- D) Public internet only

**Answer: A**
Direct mode uses TCP to connect directly to data nodes (lower latency). Gateway mode uses HTTPS through gateway (firewall-friendly).
---
## Question 8
What is the impact of consistency level on performance?


- A) Strong is always faster
- B) No impact
- C) Only affects storage
- D) Weaker consistency (eventual, session) offers better latency and throughput than strong consistency

**Answer: D**
Strong consistency requires synchronous replication (higher latency). Session/Eventual allow lower latency and higher throughput.
---
## Question 9
How can you monitor RU consumption?


- A) Only through support tickets
- B) Via response headers (x-ms-request-charge), Azure Monitor, or Azure Portal metrics
- C) Not possible
- D) Manual calculation only

**Answer: B**
Each response includes RU charge in headers. Azure Monitor and Portal provide aggregated metrics and diagnostics.
---
## Question 10
What is bulk mode in Cosmos DB SDKs?


- A) Backup mode
- B) Storage mode
- C) Optimized mode for high-throughput batch operations, improving parallelism
- D) A pricing tier

**Answer: C**
Bulk execution mode optimizes SDKs for large-volume operations, increasing parallelism and throughput for batch workloads.