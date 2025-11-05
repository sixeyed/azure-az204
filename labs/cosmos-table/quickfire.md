# Cosmos DB Table API - Quickfire Questions

## Question 1
What is Cosmos DB Table API?

- A) A new table format
- B) A drop-in replacement for Azure Table Storage with premium capabilities
- C) SQL tables
- D) Excel integration

**Answer: B**
Cosmos DB Table API is compatible with Azure Table Storage but adds global distribution, low latency, and better SLAs.

---

## Question 2
Can you migrate from Azure Table Storage to Cosmos DB Table API?

- A) No migration path
- B) Yes, minimal code changes (usually just connection string)
- C) Complete rewrite required
- D) Only manual data copy

**Answer: B**
Applications using Azure Table Storage SDK can migrate with minimal changes, often just updating the connection endpoint.

---

## Question 3
What advantages does Table API offer over Azure Table Storage?

- A) Only cost reduction
- B) Global distribution, guaranteed <10ms latency, automatic indexing, higher throughput
- C) Same features
- D) Only storage capacity

**Answer: B**
Table API adds Cosmos DB capabilities: global distribution, SLA-backed latency, all-property indexing, higher scalability.

---

## Question 4
Does Table API use the same data model as Azure Table Storage?

- A) No, completely different
- B) Yes, same PartitionKey/RowKey model
- C) Only RowKey
- D) Uses SQL tables

**Answer: B**
Table API uses the same entity model with PartitionKey and RowKey, ensuring compatibility with existing table storage code.

---

## Question 5
What SDKs support Cosmos DB Table API?

- A) Only custom SDKs
- B) Azure.Data.Tables (.NET), and language-specific Table Storage/Cosmos SDKs
- C) Only REST API
- D) No SDK support

**Answer: B**
Use Azure.Data.Tables SDK (unified) or Cosmos DB Table API SDKs for .NET, Java, Python, Node.js.

---

## Question 6
How is throughput managed in Table API?

- A) Fixed only
- B) Provisioned RU/s at table or database level, with autoscale support
- C) Unlimited free
- D) No throughput limits

**Answer: B**
Provision RU/s per table or share across tables at database level. Autoscale adjusts throughput automatically.

---

## Question 7
Does Table API support secondary indexes?

- A) No, only primary key
- B) Yes, automatic indexing on all properties (unlike Table Storage)
- C) Manual indexes only
- D) Only PartitionKey/RowKey

**Answer: B**
Table API automatically indexes all entity properties, enabling efficient queries on any property (major improvement over Table Storage).

---

## Question 8
What query improvements does Table API provide?

- A) None
- B) Faster queries with automatic indexing; supports $filter on any property efficiently
- C) Only OData improvements
- D) Slower than Table Storage

**Answer: B**
Automatic indexing enables efficient filtering on any property, not just PartitionKey/RowKey.

---

## Question 9
Can you use global distribution with Table API?

- A) No
- B) Yes, replicate tables to multiple regions with multi-region writes
- C) Only read replicas
- D) Requires manual setup

**Answer: B**
Table API supports Cosmos DB's global distribution with turnkey multi-region replication and optional multi-region writes.

---

## Question 10
What is the pricing difference between Table Storage and Table API?

- A) Same price
- B) Table API costs more due to premium features (guaranteed throughput, global distribution)
- C) Table API is cheaper
- D) Table API is free

**Answer: B**
Table API costs more than Table Storage due to provisioned throughput, SLAs, and premium features. Choose based on requirements.
