# Azure Table Storage - Quickfire Questions

## Question 1
What is Azure Table Storage?

- A) A relational database
- B) A NoSQL key-value store for semi-structured data
- C) A blob storage service
- D) A file system

**Answer: B**
Table Storage is a NoSQL datastore for schema-less, structured data using key-value pairs.

---

## Question 2
What is the data model for Table Storage?

- A) Relational tables with foreign keys
- B) Tables containing entities (rows) with properties (columns), using PartitionKey and RowKey
- C) Document store
- D) Graph database

**Answer: B**
Data is organized into tables with entities. Each entity has PartitionKey and RowKey (together forming unique key).

---

## Question 3
What is the purpose of the PartitionKey?

- A) Encryption key
- B) Groups related entities together for scalability and query performance
- C) Row identifier
- D) Access control

**Answer: B**
PartitionKey groups entities, enabling horizontal scaling and efficient range queries within a partition.

---

## Question 4
What uniquely identifies an entity in Table Storage?

- A) PartitionKey only
- B) PartitionKey + RowKey combination
- C) RowKey only
- D) Timestamp

**Answer: B**
The combination of PartitionKey and RowKey uniquely identifies each entity in a table.

---

## Question 5
What query operation is most efficient in Table Storage?

- A) Querying across partitions
- B) Point query (specific PartitionKey and RowKey)
- C) Full table scan
- D) Secondary index query

**Answer: B**
Point queries using both PartitionKey and RowKey are fastest (O(1)), directly accessing a specific entity.

---

## Question 6
Does Table Storage support ACID transactions?

- A) No transactions
- B) Yes, within a single partition via Entity Group Transactions (up to 100 entities)
- C) Yes, across all partitions
- D) Only for reads

**Answer: B**
Entity Group Transactions support atomic operations on up to 100 entities within the same partition.

---

## Question 7
What is the maximum size of an entity in Table Storage?

- A) 64 KB
- B) 1 MB
- C) 10 MB
- D) Unlimited

**Answer: B**
Maximum entity size is 1 MB, including all properties (max 255 properties per entity).

---

## Question 8
What query protocol does Table Storage use?

- A) SQL
- B) OData
- C) GraphQL
- D) MongoDB query language

**Answer: B**
Table Storage uses OData query syntax for filtering and querying entities.

---

## Question 9
What is the difference between Table Storage and Cosmos DB Table API?

- A) No difference
- B) Cosmos DB Table API offers global distribution, low latency, SLAs; Table Storage is cheaper
- C) Table Storage has more features
- D) They're incompatible

**Answer: B**
Both use the same API, but Cosmos DB Table API offers premium features (turnkey global distribution, <10ms latency, 99.99% SLA).

---

## Question 10
Can you perform full-text search on Table Storage?

- A) Yes, built-in
- B) No, limited to prefix matching and equality/range on PartitionKey and RowKey
- C) Yes, using SQL
- D) Yes, using Lucene

**Answer: B**
Table Storage supports basic filtering but not full-text search. For that, consider Azure Cognitive Search with Table Storage.
