# Cosmos DB MongoDB API - Quickfire Questions

## Question 1
What is Cosmos DB for MongoDB?


- A) MongoDB running on VMs
- B) A migration tool
- C) Cosmos DB with MongoDB wire protocol compatibility
- D) A separate MongoDB service

**Answer: C**
Cosmos DB for MongoDB provides a MongoDB-compatible API, allowing MongoDB apps to use Cosmos DB without code changes.
---
## Question 2
What MongoDB wire protocol versions are supported?


- A) Only latest version
- B) 3.2, 3.6, 4.0, 4.2, 5.0, 6.0
- C) All versions
- D) Only 2.6

**Answer: B**
Cosmos DB supports multiple MongoDB server versions (3.2, 3.6, 4.0, 4.2, 5.0, 6.0) with increasing feature parity.
---
## Question 3
Can you migrate existing MongoDB databases to Cosmos DB?


- A) Requires third-party tools only
- B) Only manual recreation
- C) No migration possible
- D) Yes, using native MongoDB tools (mongodump/mongorestore) or Azure Data Migration Service

**Answer: D**
Migration is supported via MongoDB native tools, Azure Database Migration Service, or Azure Data Factory.
---
## Question 4
Do you get Cosmos DB benefits with MongoDB API?


- A) No SLA
- B) Only storage benefits
- C) Yes: global distribution, SLAs, autoscale, multiple consistency levels
- D) No, just MongoDB compatibility

**Answer: C**
MongoDB API gets all Cosmos DB benefits: global distribution, guaranteed SLAs, elastic scale, multi-region writes.
---
## Question 5
What is the connection string format for Cosmos DB MongoDB?


- A) MongoDB connection string format with Cosmos DB endpoint and credentials
- B) Same as regular MongoDB
- C) HTTP only
- D) Custom Cosmos format

**Answer: A**
Uses standard MongoDB connection string: `mongodb://<username>:<password>@<host>:10255/?ssl=true&replicaSet=globaldb`
---
## Question 6
Are all MongoDB features supported?


- A) Only basic CRUD
- B) 100% compatible
- C) Most common features supported; some limitations (e.g., certain aggregation operators, transactions)
- D) No features supported

**Answer: C**
Most MongoDB features work, but some advanced features may have limitations. Compatibility improves with newer API versions.
---
## Question 7
What indexing capabilities does Cosmos DB MongoDB API provide?


- A) Manual indexing only
- B) No indexing
- C) Index on _id only
- D) Automatic indexing by default; custom indexes supported

**Answer: D**
Cosmos DB automatically indexes all properties by default. Custom indexes (single-field, compound, TTL) are supported.
---
## Question 8
Can you use MongoDB drivers with Cosmos DB?


- A) Only JavaScript drivers
- B) No, special drivers required
- C) Yes, standard MongoDB drivers work with the connection string
- D) Only .NET drivers

**Answer: C**
Standard MongoDB drivers (Node.js, Python, Java, .NET, etc.) work with Cosmos DB using the MongoDB connection string.
---
## Question 9
What is the capacity mode for MongoDB API?


- A) Unlimited free
- B) Provisioned throughput or Serverless
- C) Pay per document
- D) Fixed only

**Answer: B**
Like other Cosmos APIs, MongoDB API supports provisioned throughput (with autoscale) or serverless capacity modes.
---
## Question 10
Does MongoDB API support aggregation pipeline?


- A) No aggregation support
- B) Yes, aggregation pipeline is supported (coverage depends on API version)
- C) Only map-reduce
- D) Only in Enterprise tier

**Answer: B**
Aggregation pipeline is supported with increasing operator coverage in newer API versions (4.0+, 4.2+, 5.0+, 6.0).