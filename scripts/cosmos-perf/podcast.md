# Cosmos DB Performance Provisioning - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on Cosmos DB Performance Provisioning. Today we're diving into one of the most important aspects of using Azure Cosmos DB effectively - understanding and managing Request Units to control both performance and cost. This is crucial knowledge not just for the Azure AZ-204 certification exam, but for anyone building production applications with Cosmos DB. By the end of this episode, you'll understand how to measure, optimize, and control your Cosmos DB costs through informed technical decisions.

## Understanding Cosmos DB Pricing

Let's start with the fundamental question: how does Cosmos DB charge you? The answer comes down to two main components: storage and compute.

Storage is straightforward - it's a flat rate based on the amount of data you store, and this rate is the same regardless of your performance level. If you store 10 gigabytes, you pay for 10 gigabytes.

Compute, however, is where things get interesting and where most of your costs will likely come from. Cosmos DB measures compute in terms of Request Units, or RUs. You pay for all access operations - reads, writes, deletes, updates, and queries. Every interaction with your data consumes Request Units.

Think of Request Units as a normalized currency for database operations. A simple point read of a 1 KB document costs 1 RU. More complex operations cost proportionally more. This normalization makes it easier to reason about costs across different types of operations.

## Provisioning Models

You have two main options for how you pay for these Request Units.

First, there's the **serverless model**. With serverless, you pay only for the RUs you actually consume. There's no minimum charge, and you're not paying for idle capacity. This is great for development, testing, or applications with unpredictable workloads. If your application is used sporadically or has highly variable traffic patterns, serverless can be very cost-effective.

Second, there's the **provisioned model**. Here, you pay for a fixed level of RUs per second, whether you use them all or not. You're essentially reserving capacity. This can be more cost-effective for consistent, high-volume workloads because the per-RU cost is lower than serverless. If you know you'll consistently need a certain level of throughput, provisioned mode gives you better economics.

There's also a middle ground called **autoscale**, which is a variant of provisioned mode. With autoscale, you set a maximum capacity, and Cosmos DB automatically scales between 10% of that maximum and the full maximum based on actual usage. You pay for what you use, but within that scaling range. This gives you cost efficiency for variable workloads while maintaining the performance guarantees of provisioned mode.

## Why This Matters

Cost is often cited as a concern when considering Cosmos DB. You'll hear people say "Cosmos DB is expensive." But here's the truth - if you plan appropriately and understand how RUs work, Cosmos DB can actually be very cost-effective for its capabilities. The key is knowing how to test and measure your RU consumption.

The problem isn't that Cosmos DB is inherently expensive - it's that people don't take the time to understand and optimize their usage. They use inefficient query patterns, over-index their data, or choose poor partition keys, and then they're surprised by the costs. With proper optimization, Cosmos DB provides excellent value for its unique capabilities of global distribution, guaranteed performance, and flexible consistency models.

## Creating a Cosmos DB Container with Fixed Performance

Let's walk through setting up a Cosmos DB environment and measuring its performance. The process starts with creating a resource group to keep everything organized. Then you create the Cosmos DB account itself, specifying parameters that control how your database operates.

When creating the account, you'd enable public network access for development purposes, though in production you'd restrict this for security. You'd set the database kind to GlobalDocumentDB, which is the SQL API. For consistency level, you might choose Eventual consistency - this is the least strict but most performant option, perfect for scenarios where you don't need immediate consistency across all regions.

Once you have the account, you create a database with a specific performance level - perhaps 500 Request Units per second. This uses the standard provisioning model where you pay for a fixed capacity whether you use it all or not.

## The Impact of Indexing

Here's something fascinating about Cosmos DB - by default, it indexes every single field in every document. This speeds up queries dramatically but comes at a cost: it increases the Request Units consumed during inserts and uses more storage space. For some workloads, this trade-off isn't worth it.

For testing purposes, you might create a custom index policy that only indexes specific fields, perhaps just the ID field. This policy would be defined in a JSON file that specifies exactly which paths to index and which paths to explicitly exclude. This selective indexing approach can dramatically reduce write costs if you don't need to query on most fields.

When creating a container, you'd specify parameters like throughput - perhaps 400 RU/s specifically to this container, which is in addition to database-level throughput. The partition key is critical for performance because Cosmos DB uses it to distribute data across physical partitions, enabling horizontal scaling. You can provide the custom index policy through a parameter that reads the JSON from a file.

## Measuring RU Consumption: The Experiments

Now let's talk about what happens when you actually run queries and measure their costs. Imagine you have a thousand product documents loaded into your container. Each document represents a single product with fields like name, price, and product ID. Now you start running queries and examining the statistics.

**Query 1: Select All Items** - The simplest possible query just selects everything with no filters or projections. When you run this, you might see approximately 7 to 8 Request Units consumed. You'd note the retrieved document size and execution time to compare against other queries.

**Query 2: Select Specific Fields** - Instead of using SELECT asterisk, you project just the name and price fields from each product. Here's something interesting and counterintuitive - this query actually costs slightly MORE Request Units, around 8 RUs compared to the previous 7.46. Why would selecting less data cost more?

The answer lies in execution time. When you select specific fields, Cosmos DB does additional processing to filter and project the output, which increases execution time slightly. The retrieved document size from storage stays the same because Cosmos DB still has to read the entire document, but the output document size delivered to your client is much smaller. So you're trading a small increase in RU cost for reduced network bandwidth.

**Query 3: Filtering by Non-Indexed Field** - When you query for a specific product by name, filtering on the name field, this costs significantly more - around 18 to 19 Request Units. Why such a dramatic increase?

Because if the name field isn't indexed in your custom index policy, Cosmos DB has to perform a full scan of every single document in the container. The statistics would show it loaded all 1000 documents just to find the one matching document. This is the database equivalent of searching through an entire filing cabinet when you don't have an organized index. Every document must be examined to see if it matches your criteria.

**Query 4: Filtering by Indexed Field** - When you query by a field that is indexed - perhaps the product ID which is also your partition key - this only costs about 2.8 Request Units. That's a dramatic difference compared to the previous query. The statistics would show it only loaded 1 document, with much faster document load time and execution time. When Cosmos DB can use an index, it goes directly to the relevant data without scanning everything.

This demonstrates the dramatic impact of indexes on query cost. The difference between an indexed and non-indexed query can be an order of magnitude in both cost and performance. For the same query, you're looking at 2.8 RUs versus 18 RUs - that's more than six times the cost just because of indexing.

## Alternative Data Modeling: The Bulk Load Pattern

Now let's talk about a completely different approach to data modeling that can dramatically reduce costs. Instead of storing 1000 individual documents, what if you stored all products as an array inside a single large document? This is a radically different data modeling approach with very different cost characteristics.

With this bulk load pattern, your application code fetches one large document cheaply from Cosmos DB, then filters and processes the list in memory. Combined with a caching strategy where you keep this document cached for a period of time, this can be extremely cost-effective for reference data that doesn't change frequently.

Think about it - many applications have relatively static reference data like product catalogs, country lists, or configuration settings. This data might change occasionally, but not on every request. For this type of data, fetching individual items repeatedly is wasteful.

When you create a container for this bulk loading approach and use the default indexing behavior, you can load a single document containing all products as an array, along with some metadata about the reference data type.

Now when you query to fetch all products using this structure, selecting from the container where a metadata field equals a specific value, this costs around 3.6 Request Units - much cheaper than querying 1000 separate documents. You're reading one document instead of a thousand, even though that one document contains all the data.

When you query for a single product within the array, using SQL features to query into the array and filter for a specific product, this costs about 5 Request Units. Even though you're searching within an array, it's still much cheaper than scanning 1000 separate documents.

## The Scale Calculation: Where It Really Matters

Here's where this pattern really shows its value at scale. Imagine you have 10 application instances, each making 10 queries per second to fetch product information.

With individual documents, if each query costs about 4.94 RUs, your total consumption would be: 10 instances times 10 queries per second times 4.94 RUs equals 494 Request Units per second. You'd nearly hit your 500 RU/s capacity limit just serving this one query pattern. You'd have no headroom for other operations, and you'd risk throttling during traffic spikes.

But with the bulk approach combined with application caching, if each instance queries once per second to refresh its cache and then serves requests from memory, your consumption would be: 10 instances times 1 query per second times 3.59 RUs equals only 35.9 Request Units per second. That's less than 10% of your throughput, leaving plenty of capacity for other operations.

This shows how data modeling and application architecture work together to control costs. The technical decision of how to structure your data has direct financial implications. This isn't just an academic exercise - at scale, this difference could mean thousands of dollars per month in cost savings.

## Point Reads: The Ultimate Optimization

The cheapest possible way to read a document from Cosmos DB is called a point read - fetching a document by its exact object ID and partition key. This operation costs exactly 1 Request Unit for documents up to 100KB in size, regardless of what's in the document.

Point reads are special because they don't go through the query engine at all. Cosmos DB knows exactly where the document is stored based on the ID and partition key, and it retrieves it directly. There's no query parsing, no index scanning, no filtering - just a direct fetch.

This is why designing your access patterns to use point reads whenever possible is so important. If you frequently need to fetch specific items and you know their IDs and partition keys, point reads are incredibly cost-effective. The difference between a point read at 1 RU and even an efficient query at 3-5 RUs adds up quickly at scale.

## Key Factors in RU Consumption

Let's synthesize what affects Request Unit consumption. Several factors work together to determine the final RU charge.

**Execution time** is fundamental - the longer a query takes to execute, the more computational resources it consumes, and thus more RUs. Complex queries with multiple operations naturally cost more.

**Document load time** matters - how long it takes to read documents from storage. If you're scanning many documents, you're spending more time loading data.

**Number of documents retrieved** is critical - scanning 1000 documents costs far more than reading 1 document, even if you only return one result. The work happens during scanning, not just in returning results.

**Index usage** dramatically affects cost - queries that use indexes to locate data efficiently cost far less than full scans. The difference between indexed and non-indexed queries can be an order of magnitude.

**Query complexity** plays a role - projections, filters, joins, and aggregations all add processing overhead that increases RU consumption.

All of these factors contribute to the final RU charge you see for an operation.

## The Indexing Tradeoff

Indexes dramatically reduce query costs for filtered queries, but they increase the cost of writes and consume additional storage. This is a fundamental tradeoff you need to manage based on your workload patterns.

If you have a read-heavy workload with many queries that filter on specific fields, comprehensive indexing makes sense. The query savings outweigh the write costs. But if you have a write-heavy workload with few queries, or if you only query on a small subset of fields, selective indexing can save significant costs.

The default "index everything" approach is convenient and safe, but it's rarely optimal for production workloads. Taking the time to design a custom index policy based on your actual query patterns pays dividends.

## Data Modeling Impact

Data modeling choices have huge impacts on RU consumption. The decision to store data as individual documents versus nested structures can change your costs by an order of magnitude, as we saw with the bulk load example.

This is where understanding your access patterns becomes crucial. If you frequently need to access many related items together, embedding them might make sense. If you typically access items individually, separate documents might be better. If you have reference data that's queried frequently but changes rarely, the bulk load pattern with caching can be incredibly effective.

There's no universal "right" answer - it depends on your specific workload. The key is to understand the options and their cost implications, then make informed decisions.

## Application Architecture Patterns

Application architecture patterns like caching can reduce RU usage by 90% or more for read-heavy workloads with relatively static reference data. We saw this in the scale calculation where caching reduced consumption from 494 RU/s to under 36 RU/s.

Caching doesn't work for every scenario - you need to consider data freshness requirements, cache invalidation strategies, and memory constraints. But for appropriate use cases, it's incredibly powerful.

Other patterns that help include batching writes instead of writing individually, using bulk operations when available, implementing read replicas in regions where you primarily read, and using appropriate consistency levels that match your actual requirements.

## Cosmos DB and the AZ-204 Exam

This topic is heavily tested on the AZ-204 exam under the "Develop for Azure Storage" domain. Let's talk about what you need to know.

You need to understand **partitioning schemes** - how partition keys affect data distribution, how to choose appropriate partition keys, and why partition key queries use fewer Request Units. We've seen this throughout our examples.

You need to know about **consistency levels** and understand that consistency level affects both performance and cost. We mentioned Eventual consistency in our examples, which provides the best performance but weakest guarantees.

You need to be able to **create Cosmos DB containers** using Azure CLI, configure throughput at container and database levels, and understand provisioned versus serverless versus autoscale models.

You need to understand **scaling**, including allocating Request Units at database and container levels, distributing throughput across containers, and measuring actual RU consumption to inform scaling decisions.

For **optimizing performance**, you need to know about implementing index policies to reduce costs, understanding point reads versus queries, and data modeling for optimal performance and cost.

## Request Units as an Exam Topic

The exam expects you to understand Request Units thoroughly. You need to know what operations consume RUs, how to measure RU consumption, how different query patterns affect RU cost, and the difference between provisioned and consumed RUs.

A common exam question is "What is the cost of a point read in Azure Cosmos DB?" The answer: 1 RU for documents up to 100KB. This is a specific fact worth memorizing.

You might see questions about which consistency level provides the best read performance - that's Eventual consistency. Or questions about how to reduce the cost of querying a large dataset - multiple answers include using indexes, selecting specific fields, including partition keys, and implementing caching.

## Index Policies on the Exam

You need to know how to create custom index policies, the tradeoff between query performance and write/storage costs, when to exclude paths from indexing, and how index policies are defined in JSON.

The exam might present a scenario where write costs are high and ask how to optimize - the answer often involves customizing the index policy to exclude unnecessary paths.

## Data Modeling for the Exam

The exam may test your understanding of when to denormalize data, when to embed data versus reference it, how to model for specific query patterns, and the tradeoffs between different modeling approaches.

Our bulk load example demonstrates exactly this type of decision - when is it appropriate to embed an entire collection in a single document versus storing items separately? The answer depends on the access patterns and freshness requirements.

## CLI Commands for the Exam

While the exam is scenario-based, knowing CLI syntax helps. You should be familiar with commands like `az cosmosdb create`, `az cosmosdb sql database create`, and `az cosmosdb sql container create`.

Key parameters include `--throughput` for standard provisioned capacity, `--max-throughput` for autoscale, `--partition-key-path` for partitioning, `--idx` for index policies, and `--default-consistency-level` for consistency settings.

## Real-World Application

Beyond passing the exam, these skills are immediately applicable to production scenarios. Understanding RU consumption is critical for controlling Cosmos DB costs in real applications. The techniques we've discussed - measuring queries, optimizing indexes, and choosing data models - directly translate to cost savings.

Knowing that a poorly-indexed query costs seven times more RUs than an indexed query helps you design better applications from the start. Being able to calculate RU consumption helps you right-size your Cosmos DB provisioning, avoiding both under-provisioning that causes throttling and over-provisioning that wastes money.

The bulk load pattern we demonstrated is a real architectural pattern used in production systems to reduce database load. It's not just a theoretical optimization - it's a proven technique for reference data scenarios.

## Cost Optimization Strategy

Here's a practical strategy for optimizing Cosmos DB costs. First, instrument your application to log RU consumption for different operations. This gives you visibility into where your costs come from.

Second, identify your most expensive queries - both in terms of RU cost per query and total cost when considering frequency. A query that costs 10 RUs but runs 1000 times per second is more important to optimize than a query that costs 100 RUs but runs once per day.

Third, optimize those expensive queries. Add appropriate indexes, include partition keys, use point reads where possible, and consider whether data modeling changes could help.

Fourth, implement caching for appropriate use cases. Not everything should be cached, but for reference data or data with relaxed freshness requirements, caching can dramatically reduce database load.

Fifth, monitor and iterate. Cosmos DB provides metrics and diagnostics that help you understand your usage patterns. Use these to continuously optimize.

## Common Pitfalls

Let me highlight some common mistakes people make with Cosmos DB costs. First, using cross-partition queries when they should be using partition-scoped queries. Every cross-partition query scans all partitions, which is expensive.

Second, not customizing index policies and accepting the default "index everything" approach. This increases write costs unnecessarily.

Third, poor partition key selection that creates hot partitions. If most of your data goes to one partition, you're not getting the benefit of horizontal scaling.

Fourth, not implementing caching for read-heavy workloads. Making the same query repeatedly when the data doesn't change is wasteful.

Fifth, not monitoring RU consumption during development. Finding out your queries are expensive in production is too late - you should be measuring and optimizing during development.

## Final Thoughts

Cosmos DB performance provisioning and cost optimization isn't just about memorizing facts for the exam - it's about developing an intuition for how distributed databases work and what makes operations expensive or cheap.

The Request Unit model gives you unprecedented visibility into database costs. Unlike traditional databases where you might pay a fixed monthly fee and wonder why performance varies, with Cosmos DB you can measure the exact cost of every operation. This transparency enables optimization, but it requires understanding.

For the AZ-204 exam, focus on understanding the relationship between Request Units, query patterns, indexing, and data modeling. Practice measuring RU consumption with different approaches. Understand when to use point reads versus queries, when to customize indexes, and how data modeling affects costs. Know the CLI commands for creating and configuring Cosmos DB resources.

But beyond the exam, develop the mindset of measuring and optimizing. Ask yourself "How much will this query cost?" and "Is there a more efficient way to structure this data?" These questions will serve you well building production systems.

The techniques we've discussed - selective indexing, bulk load patterns, caching, point reads, and partition-aware queries - are all tools in your optimization toolkit. The key is knowing when to apply each one based on your specific workload characteristics.

Thanks for listening to this deep dive on Cosmos DB Performance Provisioning. I hope this gives you both the exam knowledge and practical skills you need to work effectively with Cosmos DB and build cost-efficient, high-performance applications. Good luck with your studies and your projects!
