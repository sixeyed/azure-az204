# Cosmos DB - Exercises Introduction

We've covered Cosmos DB as a globally distributed, multi-model database for planet-scale applications. Now let's work with Cosmos DB NoSQL API hands-on.

## What You'll Do

You'll start by **creating a Cosmos DB account and NoSQL database** using Azure CLI with public network access for development. Then you'll **retrieve connection strings** both via Portal (visual) and CLI with JMESPath queries (automation). This connection string contains account endpoint and keys - treat it like a password!

Next, you'll **run a .NET application using Entity Framework** to demonstrate CRUD operations against Cosmos DB. The app creates, reads, updates, and deletes products, showing how familiar ORMs work with Cosmos. You'll see SQL-like LINQ queries translated to Cosmos DB operations automatically.

Then you'll **explore data in the Portal's Data Explorer**. This built-in tool lets you browse containers, view documents, and run queries without any code. You'll **manually add items** to understand document structure - Cosmos requires a lowercase "id" field (not "Id" or "ID"), and the value must be unique within a partition. You'll learn about partition keys and how they enable Cosmos to distribute data across multiple nodes.

Finally, you'll **practice SQL-like queries** against the NoSQL container. Despite being a NoSQL database, Cosmos DB supports a SQL-style query language! You'll filter documents with WHERE clauses, count results, and see how queries work across partitioned data.

The key learning: Cosmos DB looks like SQL for queries but stores schema-less JSON documents. You get the flexibility of NoSQL with the familiarity of SQL syntax.

Let's explore Cosmos DB NoSQL API!
