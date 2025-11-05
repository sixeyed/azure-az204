# Cosmos DB Table API - Quickfire Questions

## Question 1
What is Cosmos DB Table API?


- A) SQL tables
- B) A new table format
- C) A drop-in replacement for Azure Table Storage with premium capabilities
- D) Excel integration

**Answer: C**
Cosmos DB Table API is compatible with Azure Table Storage but adds global distribution, low latency, and better SLAs.
---
## Question 2
Can you migrate from Azure Table Storage to Cosmos DB Table API?


- A) Complete rewrite required
- B) Yes, minimal code changes (usually just connection string)
- C) Only manual data copy
- D) No migration path

**Answer: B**
Applications using Azure Table Storage SDK can migrate with minimal changes, often just updating the connection endpoint.
---
## Question 3
What advantages does Table API offer over Azure Table Storage?


- A) Same features
- B) Only storage capacity
- C) Global distribution, guaranteed <10ms latency, automatic indexing, higher throughput
- D) Only cost reduction

**Answer: C**
Table API adds Cosmos DB capabilities: global distribution, SLA-backed latency, all-property indexing, higher scalability.
---
## Question 4
Does Table API use the same data model as Azure Table Storage?


- A) Yes, same PartitionKey/RowKey model
- B) No, completely different
- C) Only RowKey
- D) Uses SQL tables

**Answer: A**
Table API uses the same entity model with PartitionKey and RowKey, ensuring compatibility with existing table storage code.
---
## Question 5
What SDKs support Cosmos DB Table API?


- A) Azure.Data.Tables (.NET), and language-specific Table Storage/Cosmos SDKs
- B) No SDK support
- C) Only custom SDKs
- D) Only REST API

**Answer: A**
Use Azure.Data.Tables SDK (unified) or Cosmos DB Table API SDKs for .NET, Java, Python, Node.js.
---
## Question 6
How is throughput managed in Table API?


- A) No throughput limits
- B) Fixed only
- C) Provisioned RU/s at table or database level, with autoscale support
- D) Unlimited free

**Answer: C**
Provision RU/s per table or share across tables at database level. Autoscale adjusts throughput automatically.
---
## Question 7
Does Table API support secondary indexes?


- A) No, only primary key
- B) Only PartitionKey/RowKey
- C) Yes, automatic indexing on all properties (unlike Table Storage)
- D) Manual indexes only

**Answer: C**
Table API automatically indexes all entity properties, enabling efficient queries on any property (major improvement over Table Storage).
---
## Question 8
What query improvements does Table API provide?


- A) Slower than Table Storage
- B) None
- C) Only OData improvements
- D) Faster queries with automatic indexing; supports $filter on any property efficiently

**Answer: D**
Automatic indexing enables efficient filtering on any property, not just PartitionKey/RowKey.
---
## Question 9
Can you use global distribution with Table API?


- A) Only read replicas
- B) Requires manual setup
- C) No
- D) Yes, replicate tables to multiple regions with multi-region writes

**Answer: D**
Table API supports Cosmos DB's global distribution with turnkey multi-region replication and optional multi-region writes.
---
## Question 10
What is the pricing difference between Table Storage and Table API?


- A) Table API costs more due to premium features (guaranteed throughput, global distribution)
- B) Table API is free
- C) Table API is cheaper
- D) Same price

**Answer: A**
Table API costs more than Table Storage due to provisioned throughput, SLAs, and premium features. Choose based on requirements.