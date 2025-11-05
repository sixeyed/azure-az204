# Cosmos DB - AZ-204 Exam Introduction

Great work with Cosmos DB! This is a major AZ-204 exam topic covering NoSQL databases and global distribution.

## What We'll Cover

**Account/Database/Container/Item hierarchy** is fundamental. Account is the top-level billing and management unit (globally unique DNS name). Database is a logical container for multiple containers (like a database in SQL). Container holds items and has throughput settings (like a table but schema-less). Item is a JSON document (like a row but flexible structure). The exam tests understanding of this hierarchy and resource URLs.

**Partition keys** are heavily tested. Every container must have a partition key that determines data distribution across physical partitions. Choose a key with high cardinality (many distinct values) for even distribution, used in most queries for performance, and stable (doesn't change). The exam tests choosing appropriate partition keys for different scenarios like user data (userId), IoT telemetry (deviceId), or multi-tenant apps (tenantId).

**Connection string security** is important. Connection strings contain account endpoint and master keys granting full access. Never commit to source control, use Key Vault for storage in production, rotate keys regularly using primary/secondary key pair. The exam tests secure credential management patterns.

**Schema flexibility** in containers allows mixed document structures. Unlike SQL databases, Cosmos containers don't enforce schemas - different items can have different fields. This flexibility enables evolutionary design but requires code to handle variations. The exam tests understanding of schema-less storage and when this is beneficial.

**The lowercase "id" field requirement** is a common gotcha. Cosmos requires every item to have an "id" property (case-sensitive lowercase) that's unique within the partition. Using "Id" or "ID" causes errors. The exam may test understanding of item uniqueness and the id field.

**Entity Framework integration** demonstrates using familiar tools with Cosmos DB. The EF provider translates LINQ queries to Cosmos SQL API queries, handles serialization/deserialization automatically, supports change tracking for updates. The exam tests understanding of SDK options and when to use ORMs versus direct SDK access.

We'll cover **Azure CLI with JMESPath** for automation, **SQL-like query syntax** for NoSQL data, **consistency levels** (strong, bounded staleness, session, consistent prefix, eventual), **request units and performance**, **global distribution**, and **common scenarios** about data modeling, partitioning strategies, and cost optimization.

Master Cosmos DB for the AZ-204!
