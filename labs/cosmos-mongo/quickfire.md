# Cosmos DB MongoDB API - Quickfire Questions

## Question 1
What is Cosmos DB for MongoDB?

- A) A separate MongoDB service
- B) Cosmos DB with MongoDB wire protocol compatibility
- C) MongoDB running on VMs
- D) A migration tool

**Answer: B**
Cosmos DB for MongoDB provides a MongoDB-compatible API, allowing MongoDB apps to use Cosmos DB without code changes.

---

## Question 2
What MongoDB wire protocol versions are supported?

- A) Only 2.6
- B) 3.2, 3.6, 4.0, 4.2, 5.0, 6.0
- C) Only latest version
- D) All versions

**Answer: B**
Cosmos DB supports multiple MongoDB server versions (3.2, 3.6, 4.0, 4.2, 5.0, 6.0) with increasing feature parity.

---

## Question 3
Can you migrate existing MongoDB databases to Cosmos DB?

- A) No migration possible
- B) Yes, using native MongoDB tools (mongodump/mongorestore) or Azure Data Migration Service
- C) Only manual recreation
- D) Requires third-party tools only

**Answer: B**
Migration is supported via MongoDB native tools, Azure Database Migration Service, or Azure Data Factory.

---

## Question 4
Do you get Cosmos DB benefits with MongoDB API?

- A) No, just MongoDB compatibility
- B) Yes: global distribution, SLAs, autoscale, multiple consistency levels
- C) Only storage benefits
- D) No SLA

**Answer: B**
MongoDB API gets all Cosmos DB benefits: global distribution, guaranteed SLAs, elastic scale, multi-region writes.

---

## Question 5
What is the connection string format for Cosmos DB MongoDB?

- A) Same as regular MongoDB
- B) MongoDB connection string format with Cosmos DB endpoint and credentials
- C) HTTP only
- D) Custom Cosmos format

**Answer: B**
Uses standard MongoDB connection string: `mongodb://<username>:<password>@<host>:10255/?ssl=true&replicaSet=globaldb`

---

## Question 6
Are all MongoDB features supported?

- A) 100% compatible
- B) Most common features supported; some limitations (e.g., certain aggregation operators, transactions)
- C) Only basic CRUD
- D) No features supported

**Answer: B**
Most MongoDB features work, but some advanced features may have limitations. Compatibility improves with newer API versions.

---

## Question 7
What indexing capabilities does Cosmos DB MongoDB API provide?

- A) No indexing
- B) Automatic indexing by default; custom indexes supported
- C) Manual indexing only
- D) Index on _id only

**Answer: B**
Cosmos DB automatically indexes all properties by default. Custom indexes (single-field, compound, TTL) are supported.

---

## Question 8
Can you use MongoDB drivers with Cosmos DB?

- A) No, special drivers required
- B) Yes, standard MongoDB drivers work with the connection string
- C) Only .NET drivers
- D) Only JavaScript drivers

**Answer: B**
Standard MongoDB drivers (Node.js, Python, Java, .NET, etc.) work with Cosmos DB using the MongoDB connection string.

---

## Question 9
What is the capacity mode for MongoDB API?

- A) Fixed only
- B) Provisioned throughput or Serverless
- C) Unlimited free
- D) Pay per document

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
