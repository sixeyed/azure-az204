# Cosmos DB Performance Provisioning - Exercises Walkthrough

## Exercise 1: Creating a Cosmos DB Container with Fixed Performance

### Setting Up the Resource Group

We'll start by creating a resource group for this lab. This keeps all our resources organized and makes cleanup easier at the end. We're creating a resource group with a descriptive name in your chosen Azure region, and adding the courselabs=azure tag which helps us identify and track resources created for this course - this is a best practice for organizing resources.

### Creating the Cosmos DB Account

Next, we're creating the Cosmos DB account. This command specifies several important parameters that control how your database operates. We're enabling public network access for this lab so you can connect from anywhere - in production, you'd typically restrict this. The database kind is set to GlobalDocumentDB, which is the SQL API that we'll be using throughout this exercise. For the consistency level, we're choosing Eventual consistency - this is the least strict but most performant option, perfect for scenarios where you don't need immediate consistency across all regions.

### Creating a Database with Fixed Throughput

Now let's create a SQL API database with a specific performance level of 500 Request Units per second. This uses the standard provisioning model where you pay for a fixed capacity whether you use it all or not. The alternative approaches would be serverless provisioning, where you only pay for what you use, or autoscale provisioning, where capacity adjusts automatically based on demand. For this exercise, we're using fixed throughput so we can precisely control and measure the Request Unit consumption.

### Understanding Index Policies

Here's something fascinating about Cosmos DB - by default, it indexes every single field in every document. This speeds up queries dramatically but comes at a cost: it increases the Request Units consumed during inserts and uses more storage space. For some workloads, this trade-off isn't worth it.

For this exercise, we're using a custom index policy that only indexes the ID field. This policy is defined in a JSON file that specifies exactly which paths to index and which paths to explicitly exclude. This selective indexing approach can dramatically reduce write costs if you don't need to query on most fields.

### Creating the Products Container

Let's create our Products container with that custom index policy. We're allocating 400 Request Units per second specifically to this container - notice this is in addition to the 500 RU/s we allocated to the database earlier. The partition key is critical for performance because Cosmos DB uses it to distribute data across physical partitions, enabling horizontal scaling. The idx parameter points to our custom index policy file using the at symbol, which tells the CLI to read the JSON from the specified file.

## Exercise 2: Estimating RU Usage

### Loading Data

We have a JSON file containing one thousand product documents. Each document is relatively small, representing a single product with fields like name, price, and product ID. We're going to upload this file through the Azure Portal's Data Explorer using the Upload item feature. This gives us a dataset to query and analyze.

### Query 1: Select All Items

Let's run our first query to select all items from the Products container. This is the simplest possible query - just selecting everything with no filters or projections.

After running the query, check the Query Stats tab in the Data Explorer. You should see approximately 7 to 8 Request Units consumed. Make note of the retrieved document size and execution time - we'll compare these metrics across different queries to understand what affects RU consumption.

### Query 2: Select Specific Fields

Now let's select only specific fields instead of using the asterisk wildcard. We're projecting just the name and price fields from each product, aliasing the container as "p" for convenience.

Here's something interesting - this query actually costs slightly MORE Request Units, around 8 RUs compared to the previous 7.46. Why would selecting less data cost more?

Look at the execution time in the stats. When you select specific fields, Cosmos DB does additional processing to filter and project the output, which increases execution time slightly. The retrieved document size from storage stays the same because Cosmos DB still has to read the entire document, but the output document size delivered to your client is much smaller. So you're trading a small increase in RU cost for reduced network bandwidth.

### Query 3: Filtering by Non-Indexed Field

Let's query for a specific product by name. We're filtering the Products container where the name field equals a specific product name.

This costs significantly more - around 18 to 19 Request Units. Why such a dramatic increase?

Because the name field isn't indexed in our custom index policy, Cosmos DB has to perform a full scan of every single document in the container. You can see in the Query Stats that it loaded all 1000 documents just to find the one matching document. This is the database equivalent of searching through an entire filing cabinet when you don't have an organized index.

### Query 4: Filtering by Indexed Field

Now let's query by the product ID, which happens to be our partition key and is therefore indexed. We're filtering where the productId field equals a specific value.

This only costs about 2.8 Request Units - a dramatic difference compared to the previous query. Looking at the stats, you can see it only loaded 1 document, with much faster document load time and execution time. When Cosmos DB can use an index, it goes directly to the relevant data without scanning everything.

This demonstrates the dramatic impact of indexes on query cost. The difference between an indexed and non-indexed query can be an order of magnitude in both cost and performance.

## Exercise 3: Alternative Data Modeling

### The Bulk Load Approach

Instead of storing 1000 individual documents, what if we stored all products as an array inside a single large document? This is a completely different data modeling approach.

With this bulk load pattern, your application code fetches one large document cheaply from Cosmos DB, then filters and processes the list in memory. Combined with a caching strategy where you keep this document cached for a period of time, this can be extremely cost-effective for reference data that doesn't change frequently.

### Creating the Reference Data Container

Let's create a new container specifically for this bulk loading approach. Notice we're not specifying a custom index policy this time - we'll use the default indexing behavior which indexes all fields. This makes sense because we'll still want to query efficiently on the document metadata.

### Loading Alternative Format Data

Upload the reference data JSON file through the Portal. This file is structured differently from before - it contains all products as an array within a single document, along with some metadata about the reference data type.

### Comparing Query Costs

Let's fetch all products using this new structure. We're selecting from ReferenceData where the refDataType field equals a specific value - this metadata field helps us identify what kind of reference data this document contains.

This costs around 3.6 Request Units - much cheaper than querying 1000 separate documents. You're reading one document instead of a thousand, even though that one document contains all the data.

Now let's query for a single product within the array. We're using the IN keyword to query into the items array, filtering where the productId matches what we're looking for.

This costs about 5 Request Units. Notice that even though we're searching within an array, it's still much cheaper than scanning 1000 separate documents.

### The Scale Calculation

Here's where this pattern really shows its value. Imagine you have 10 application instances, each making 10 queries per second to fetch product information.

With individual documents, if each query costs about 4.94 RUs, your total consumption would be: 10 instances times 10 queries per second times 4.94 RUs equals 494 Request Units per second. You'd nearly hit your 500 RU/s capacity limit just serving this one query pattern.

But with the bulk approach combined with application caching, if each instance queries once per second to refresh its cache and then serves requests from memory, your consumption would be: 10 instances times 1 query per second times 3.59 RUs equals only 35.9 Request Units per second. That's less than 10% of your throughput, leaving plenty of capacity for other operations.

This shows how data modeling and application architecture work together to control costs. The technical decision of how to structure your data has direct financial implications.

## Lab Challenge: Point Reads

The cheapest possible way to read a document from Cosmos DB is called a point read - fetching a document by its exact object ID and partition key. This operation costs exactly 1 Request Unit for documents up to 100KB in size, regardless of what's in the document.

Your challenge is to find the object ID for the reference data document we created, then perform a point read operation to fetch it. Verify that it costs exactly 1 RU by checking the Query Statistics, and examine what makes a point read so much more efficient than a query.

Hint: A point read is different from a query - it's a direct fetch operation by ID, not a query that gets executed by the query engine.

## Key Takeaways

Request Units are calculated from multiple factors working together: execution time, document load time, the number of documents retrieved, and whether the query uses index lookups or full scans. All of these contribute to the final RU charge.

Indexes dramatically reduce query costs for filtered queries, but they increase the cost of writes and consume additional storage. It's a trade-off you need to manage based on your workload patterns.

Data modeling choices have huge impacts on RU consumption. The decision to store data as individual documents versus nested structures can change your costs by an order of magnitude.

Application architecture patterns like caching can reduce RU usage by 90% or more for read-heavy workloads with relatively static reference data.

Point reads are the most cost-effective way to fetch individual documents when you know the exact ID and partition key - they cost exactly 1 RU regardless of document size up to 100KB.

Understanding these patterns and their cost implications is essential for building cost-effective solutions with Cosmos DB.
