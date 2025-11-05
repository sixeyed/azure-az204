# Cosmos DB Performance Provisioning - AZ-204 Exam Introduction

Excellent work optimizing Cosmos DB! Request Units and cost management are critical AZ-204 exam topics.

## What We'll Cover

**Request Units (RUs) as compute cost metric** is fundamental. Every operation (read, write, query) consumes RUs. Complex operations consume more RUs (queries with filters, writes to multiple indexes). Point reads (get by ID and partition key) cost exactly 1 RU. The exam tests understanding of what affects RU consumption and how to measure it.

**Index policies and tradeoffs** are heavily tested. Indexes improve query performance but increase write costs (every write updates indexes) and storage costs (indexes consume space). Default policy indexes everything (good for unknown workloads). Selective indexing reduces write/storage costs but may slow specific queries. The exam tests when to customize index policies and the consequences.

**Data modeling impacts on RU consumption** can be massive. Individual documents versus nested structures can differ by 10x in cost. Aggregating related data (bulk documents) reduces RU consumption for reads but increases document size and may complicate updates. The exam tests understanding of modeling tradeoffs and choosing patterns based on access patterns.

**Provisioning models** need to be memorized. Standard provisioned (fixed RU/s allocation, predictable cost, can be low when idle, set at database or container level). Autoscale (dynamic scaling between min/max RU/s, handles variable traffic, costs more than provisioned at constant load). Serverless (pay per RU consumed, no provisioning required, limited to 5000 RU/s, good for sporadic workloads). The exam tests when to choose each model.

**Partition key selection effects** on query costs are important. Queries with partition key in WHERE clause are "point queries" that search only one partition (very low RU cost). Queries without partition key are "cross-partition queries" that search all partitions (high RU cost). The exam tests choosing partition keys that minimize cross-partition queries.

**Point read optimization** is the most efficient pattern. Fetching by ID and partition key costs only 1 RU regardless of size (up to 100KB). If you can design access patterns around point reads rather than queries, you dramatically reduce costs. The exam tests recognizing when point read optimization is possible.

We'll cover **RU measurement and monitoring**, **caching strategies with Redis**, **bulk document patterns**, **throughput sharing across containers**, and **common scenarios** about troubleshooting performance issues, optimizing costs, and choosing appropriate provisioning models.

Master Cosmos DB cost optimization for the AZ-204!
