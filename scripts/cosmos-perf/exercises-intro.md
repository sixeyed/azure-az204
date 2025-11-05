# Cosmos DB Performance Provisioning - Exercises Introduction

We've covered Request Units (RUs) as the currency for Cosmos DB compute cost. Now let's measure RU consumption and optimize performance.

## What You'll Do

You'll start by **creating a Cosmos DB database with fixed 500 RU/s throughput** and **a container with a custom index policy** that only indexes the ID field. Why? Because indexes improve query performance but cost RUs for writes and storage. By limiting indexes, you'll see the impact clearly.

Then you'll **load 1000 product documents** and run queries to measure RU consumption. Here's the key learning: a query on the indexed ID field costs 18-19 RUs, while the same query on a non-indexed field costs only 2.8 RUs! Wait, that seems backwards? It is - for this specific scenario, the index overhead outweighs the benefit. This teaches you that indexing isn't always the answer.

Next comes the powerful optimization: **alternative data modeling**. Instead of storing 1000 individual product documents, you'll store ALL products in a single bulk document as a nested array. Run the same queries again and discover a 90% RU reduction! Combined with application-level caching (Redis or in-memory), this pattern drastically reduces costs for read-heavy workloads.

You'll also practice **point read operations** - fetching a document by its ID and partition key. This costs exactly 1 RU regardless of document size (up to 100KB). This is the most efficient operation in Cosmos DB. If you can design your app around point reads instead of queries, you'll minimize costs.

The key insight: data modeling and access patterns matter more than hardware specs in Cosmos DB. The same functionality can cost 10x more or 90% less depending on how you structure data.

Let's optimize Cosmos DB performance and cost!
