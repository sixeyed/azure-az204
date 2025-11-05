# Cosmos DB Performance Provisioning - Exercises Walkthrough

## Exercise 1: Creating a Cosmos DB Container with Fixed Performance

### Setting Up the Resource Group

We'll start by creating a resource group for this lab. This keeps all our resources organized:

```
az group create -n <resource-group-name> -l <location> --tags courselabs=azure
```

### Creating the Cosmos DB Account

Next, we'll create the Cosmos DB account. Notice we're specifying several important parameters:

```
az cosmosdb create -g <resource-group-name> --enable-public-network --kind GlobalDocumentDB --default-consistency-level Eventual -n <cosmos-db-name>
```

We're enabling public network access for this lab, setting the database kind to GlobalDocumentDB for the SQL API, and choosing Eventual consistency level - the least strict but most performant option.

### Creating a Database with Fixed Throughput

Now let's create a SQL API database with a specific performance level of 500 Request Units per second:

```
az cosmosdb sql database create --name <database-name> -g <resource-group-name> --throughput 500 --account-name <cosmos-db-name>
```

This uses the standard provisioning model. We're paying for 500 RU/s whether we use them all or not. The alternatives would be serverless or autoscale provisioning.

### Understanding Index Policies

Cosmos DB indexes every field in a document by default. This speeds up queries but increases the cost of inserts and uses more storage.

For this exercise, we're using a custom index policy that only indexes the ID field. This is defined in a JSON file that specifies exactly which paths to index and which to exclude.

### Creating the Products Container

Let's create our Products container with a custom index policy:

```
az cosmosdb sql container create -n <container-name> -g <resource-group-name> -d <database-name> --partition-key-path '/<partition-key>' --throughput 400 --idx @<path-to-index-policy> -a <cosmos-db-name>
```

Notice we're allocating 400 RU/s to this specific container. The partition key is critical for performance - Cosmos DB uses it to distribute data across partitions.

## Exercise 2: Estimating RU Usage

### Loading Data

We have a JSON file with one thousand product documents. Each document is small and represents a single product.

Upload this file through the Azure Portal's Data Explorer using the Upload item feature.

### Query 1: Select All Items

Let's run our first query to select all items:

```
SELECT * FROM Products
```

Check the Query Stats tab. You should see approximately 7 to 8 Request Units consumed. Make note of the retrieved document size and execution time.

### Query 2: Select Specific Fields

Now let's select only specific fields:

```
SELECT p.name, p.price FROM Products p
```

Interesting - this actually costs slightly MORE Request Units, around 8 RUs compared to the previous 7.46. Why?

Look at the execution time. When you select specific fields, Cosmos DB does additional processing to filter the output, which increases execution time slightly. The retrieved document size stays the same, but the output document size is much smaller.

### Query 3: Filtering by Non-Indexed Field

Let's query for a specific product by name:

```
SELECT * FROM Products p WHERE p.name = '<product-name>'
```

This costs significantly more - around 18 to 19 Request Units. Why?

Because the name field isn't indexed, Cosmos DB has to scan every single document. You can see in the stats that it loaded all 1000 documents to find the one match.

### Query 4: Filtering by Indexed Field

Now let's query by the partition key, which IS indexed:

```
SELECT * FROM Products p WHERE p.productId = '<product-id>'
```

This only costs about 2.8 Request Units. The stats show it only loaded 1 document, with a much faster document load time and execution time.

This demonstrates the dramatic impact of indexes on query cost.

## Exercise 3: Alternative Data Modeling

### The Bulk Load Approach

Instead of storing 1000 individual documents, what if we stored all products as an array inside a single document?

This is a bulk load approach. Your application code fetches one large document cheaply, then filters the list in memory. With a caching strategy, this can be very cost-effective.

### Creating the Reference Data Container

Let's create a new container for this approach:

```
az cosmosdb sql container create -n <reference-container-name> -g <resource-group-name> -d <database-name> --partition-key-path '/<partition-key>' -a <cosmos-db-name>
```

Notice we're not specifying a custom index policy this time. We'll use the default indexing.

### Loading Alternative Format Data

Upload the reference data JSON file through the Portal. This file contains all products as an array within a single document.

### Comparing Query Costs

Let's fetch all products:

```
SELECT * FROM ReferenceData r
WHERE r.refDataType='<type-value>'
```

This costs around 3.6 Request Units - much cheaper than querying 1000 separate documents.

Now let's query for a single product within the array:

```
SELECT *
FROM p IN ReferenceData.items
WHERE p.productId='<product-id>'
```

This costs about 5 Request Units.

### The Scale Calculation

Here's where it gets interesting. Imagine you have 10 application instances, each making 10 queries per second.

With individual documents, fetching products separately would cost: 10 instances × 10 queries × 4.94 RUs = 494 RU/s. You'd nearly hit your 500 RU/s limit.

But with the bulk approach and caching, if each instance queries once per second and caches the results: 10 instances × 1 query × 3.59 RUs = 35.9 RU/s. That's less than 10% of your throughput.

This shows how data modeling and application architecture work together to control costs.

## Lab Challenge: Point Reads

The cheapest way to read a document from Cosmos DB is a point read - fetching by object ID and partition key. This costs exactly 1 Request Unit for documents up to 100KB.

Your challenge: Find the object ID for the reference data document and perform a point read. Verify that it costs 1 RU and examine the query statistics.

## Key Takeaways

- Request Units are calculated from multiple factors: execution time, document load time, number of documents retrieved, and index lookups
- Indexes dramatically reduce query costs for filtered queries
- Data modeling choices have huge impacts on RU consumption
- Application architecture patterns like caching can reduce RU usage by 90% or more
- Point reads are the most cost-effective way to fetch individual documents
