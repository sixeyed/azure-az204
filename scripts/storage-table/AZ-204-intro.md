# Azure Table Storage - AZ-204 Exam Introduction

Great work with Table Storage! This is an important topic for the AZ-204 exam's "Develop solutions that use Azure Storage" domain.

## What We'll Cover

**Table Storage fundamentals** must be understood. Entities are data units analogous to rows in SQL databases or documents in MongoDB. Partition Key is part of the unique identifier determining physical storage location affecting performance and scalability. Row Key is the unique part of identifier - together, partition and row keys form composite primary key uniquely identifying each entity. The exam tests understanding of this terminology and structure.

**Schema flexibility** is a key differentiator. Table Storage does NOT enforce a fixed schema - entities within the same table can have completely different properties. This is fundamentally different from relational databases. The exam may test understanding of when this flexibility is advantageous versus when it could cause issues.

**Authentication methods** are critical for the exam. Connection strings include account name, account key, and endpoints for all storage services. Shared Access Signatures (SAS) provide time-limited access with specific permissions and duration at table, partition, or row level - three types are User delegation SAS (most secure using Azure AD), Service SAS, and Account SAS. Azure AD Authentication is preferred for applications using managed identities. The exam tests choosing appropriate security methods.

**Querying with OData** appears on the exam. OData REST API provides standardized querying over HTTP. URL format appends table name to endpoint. Filter by PartitionKey and RowKey for most efficient queries. Response formats: XML default or JSON with Accept headers. The exam may test OData query syntax and usage patterns.

**Client libraries** are developer-focused. Azure.Data.Tables SDK for .NET performs CRUD operations programmatically with async operations. The exam may test SDK usage patterns and best practices.

**Partition key design** is critical for performance questions. Good partition keys distribute data evenly avoiding "hot" partitions with disproportionate traffic. Consider query patterns when designing keys. Understand impact on parallel operations. The exam tests recognizing good vs bad partition key designs.

**Integration scenarios** demonstrate practical usage. Logging and diagnostics use Table Storage as a sink for application logs with timestamp-based partition strategies. Cost optimization: no cost for empty tables, pay per transaction and storage used. The exam tests understanding of use cases and cost optimization.

**Cosmos DB migration path** is testable. Cosmos DB Table API provides compatibility with Table Storage enabling migration. The exam tests understanding of when to choose Table Storage vs Cosmos DB based on requirements like global distribution, low latency SLAs, and complex queries.

We'll cover **common exam scenarios** (choosing storage for semi-structured data, redesigning partition keys for performance, providing time-limited access, deciding between Table Storage and Cosmos DB), **CLI commands** (`az storage account create`, `az storage table create`, `az storage table generate-sas`), and **technical limits** (1 MB max entity size, 64 KB max property size, 255 max properties per entity).

Master Table Storage for the AZ-204!
