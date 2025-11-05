# Cosmos DB Performance - Quickfire Questions

## Question 1
What is the most important factor for Cosmos DB performance?

- A) Storage size
- B) Choosing an appropriate partition key for even distribution
- C) Number of indexes
- D) Region selection only

**Answer: B**
A well-chosen partition key ensures even data and request distribution, preventing hot partitions and throttling.

---

## Question 2
What causes throttling (429 errors) in Cosmos DB?

- A) Too much storage
- B) Request rate exceeding provisioned RU/s
- C) Too many users
- D) Network issues only

**Answer: B**
429 (TooManyRequests) occurs when consumed RU/s exceeds provisioned throughput. Solutions: increase RUs or implement retry logic.

---

## Question 3
What is a hot partition?

- A) A popular database
- B) A partition receiving disproportionate request volume causing throttling
- C) High-temperature storage
- D) A backup partition

**Answer: B**
Hot partitions occur with poor partition key choices, concentrating requests on few partitions while others are idle.

---

## Question 4
What query pattern is most efficient in Cosmos DB?

- A) Cross-partition queries
- B) Single-partition queries with partition key in WHERE clause
- C) Full table scans
- D) Queries without filters

**Answer: B**
Queries scoped to a single partition key are most efficient, avoiding fan-out across all partitions.

---

## Question 5
How does indexing affect performance?

- A) No impact
- B) Improves read performance but increases write cost (RUs) and storage
- C) Only affects storage
- D) Reduces all costs

**Answer: B**
Indexes speed up queries but increase write RUs (indexing overhead) and storage. Optimize by indexing only needed properties.

---

## Question 6
What is the purpose of excluding paths from indexing?

- A) Security
- B) Reduce write RU cost and storage for properties that won't be queried
- C) Improve read speed
- D) Enable encryption

**Answer: B**
Excluding unused properties from indexing reduces write costs and storage, improving write throughput.

---

## Question 7
What is direct connectivity mode?

- A) HTTP only
- B) TCP-based connection to Cosmos DB backend, bypassing gateway for lower latency
- C) Public internet only
- D) VPN connection

**Answer: B**
Direct mode uses TCP to connect directly to data nodes (lower latency). Gateway mode uses HTTPS through gateway (firewall-friendly).

---

## Question 8
What is the impact of consistency level on performance?

- A) No impact
- B) Weaker consistency (eventual, session) offers better latency and throughput than strong consistency
- C) Strong is always faster
- D) Only affects storage

**Answer: B**
Strong consistency requires synchronous replication (higher latency). Session/Eventual allow lower latency and higher throughput.

---

## Question 9
How can you monitor RU consumption?

- A) Not possible
- B) Via response headers (x-ms-request-charge), Azure Monitor, or Azure Portal metrics
- C) Only through support tickets
- D) Manual calculation only

**Answer: B**
Each response includes RU charge in headers. Azure Monitor and Portal provide aggregated metrics and diagnostics.

---

## Question 10
What is bulk mode in Cosmos DB SDKs?

- A) Storage mode
- B) Optimized mode for high-throughput batch operations, improving parallelism
- C) A pricing tier
- D) Backup mode

**Answer: B**
Bulk execution mode optimizes SDKs for large-volume operations, increasing parallelism and throughput for batch workloads.
