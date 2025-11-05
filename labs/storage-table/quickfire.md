# Azure Table Storage - Quickfire Questions

## Question 1
What is Azure Table Storage?


- A) A NoSQL key-value store for semi-structured data
- B) A blob storage service
- C) A relational database
- D) A file system

**Answer: A**
Table Storage is a NoSQL datastore for schema-less, structured data using key-value pairs.
---
## Question 2
What is the data model for Table Storage?


- A) Tables containing entities (rows) with properties (columns), using PartitionKey and RowKey
- B) Relational tables with foreign keys
- C) Graph database
- D) Document store

**Answer: A**
Data is organized into tables with entities. Each entity has PartitionKey and RowKey (together forming unique key).
---
## Question 3
What is the purpose of the PartitionKey?


- A) Row identifier
- B) Access control
- C) Groups related entities together for scalability and query performance
- D) Encryption key

**Answer: C**
PartitionKey groups entities, enabling horizontal scaling and efficient range queries within a partition.
---
## Question 4
What uniquely identifies an entity in Table Storage?


- A) PartitionKey + RowKey combination
- B) Timestamp
- C) RowKey only
- D) PartitionKey only

**Answer: A**
The combination of PartitionKey and RowKey uniquely identifies each entity in a table.
---
## Question 5
What query operation is most efficient in Table Storage?


- A) Secondary index query
- B) Point query (specific PartitionKey and RowKey)
- C) Full table scan
- D) Querying across partitions

**Answer: B**
Point queries using both PartitionKey and RowKey are fastest (O(1)), directly accessing a specific entity.
---
## Question 6
Does Table Storage support ACID transactions?


- A) Yes, within a single partition via Entity Group Transactions (up to 100 entities)
- B) No transactions
- C) Only for reads
- D) Yes, across all partitions

**Answer: A**
Entity Group Transactions support atomic operations on up to 100 entities within the same partition.
---
## Question 7
What is the maximum size of an entity in Table Storage?


- A) 1 MB
- B) Unlimited
- C) 64 KB
- D) 10 MB

**Answer: A**
Maximum entity size is 1 MB, including all properties (max 255 properties per entity).
---
## Question 8
What query protocol does Table Storage use?


- A) SQL
- B) GraphQL
- C) OData
- D) MongoDB query language

**Answer: C**
Table Storage uses OData query syntax for filtering and querying entities.
---
## Question 9
What is the difference between Table Storage and Cosmos DB Table API?


- A) Cosmos DB Table API offers global distribution, low latency, SLAs; Table Storage is cheaper
- B) Table Storage has more features
- C) No difference
- D) They're incompatible

**Answer: A**
Both use the same API, but Cosmos DB Table API offers premium features (turnkey global distribution, <10ms latency, 99.99% SLA).
---
## Question 10
Can you perform full-text search on Table Storage?


- A) No, limited to prefix matching and equality/range on PartitionKey and RowKey
- B) Yes, using Lucene
- C) Yes, built-in
- D) Yes, using SQL

**Answer: A**
Table Storage supports basic filtering but not full-text search. For that, consider Azure Cognitive Search with Table Storage.