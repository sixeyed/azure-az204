# Cosmos DB - Performance Provisioning

## Reference

CosmosDB is charged for storage and compute. Storage is a flat rate based on the amount of data stored, and the charge is the same regardless of your performance level. Compute is charged in terms of Request Units, which represent the cost of all access operations including read, write, delete, update and query. You can choose between a serverless model where you pay for RUs consumed, or a provisioned model where you pay for a fixed level of RUs regardless of actual usage. Cost can be a deterrent for using Cosmos, but with proper planning it can be very cost-effective. Understanding how to test and measure RU consumption is essential for managing costs and optimizing performance.

## Create a CosmosDB Container with Fixed Performance

**Create Resource Group**: We're starting by creating a resource group for this lab in your preferred region with the courselabs=azure tag to track resources created for this course.

**Create Cosmos DB Account**: We're creating a new Cosmos DB account with several important parameters. We're enabling public network access for this lab, using the GlobalDocumentDB kind for the SQL API, and setting the default consistency level to Eventual. Eventual consistency is the least strict but most performant option, perfect for scenarios where you don't need immediate consistency across all regions.

**Understand Performance Levels**: Request Units per second define the level of performance of your CosmosDB. Other factors affect cost too, like the amount of replication and the multiple-writes feature, but RU consumption is the primary cost factor.

**Create Database with Throughput**: We're creating a SQL API database with a specific performance level of 500 RU per second. This uses the standard provisioning model, where you pay for a level of RU performance and get charged whether you hit that level or not. The alternative billing models are serverless, where you only pay for what you use, and autoscale, where capacity adjusts automatically based on demand.

**Work Directly with Database**: We'll work directly with the database rather than through an app, so we need to create a document container. Containers can be allocated a portion of the full database throughput, so you can focus performance where you need it.

**Understanding Index Policies**: CosmosDB indexes every field in a document by default, which speeds up queries at the expense of inserts and storage. We'll use a custom policy which only indexes the ID field. The JSON file expresses the indexing policy, specifying exactly which paths to index and which to explicitly exclude.

**Create Products Container**: We're creating a SQL container called Products for the database. We're setting the container to have 400 RU per second throughput, using productId as the partition key, and setting the custom index policy from the JSON file. The throughput parameter is for fixed performance, while max-throughput would be for autoscale. The partition key path controls how data is distributed across partitions.

---

## Estimating RU Usage

**Understand Data Modeling Impact**: How you format your data can make a lot of difference to RU consumption. We have a list of products to save in the shop database, which is reference data we can model in different ways. Using one document per product will give us 1000 small documents.

**Upload Documents**: We're uploading the documents in the products JSON file to the container using the Portal. Navigate to the container in Data Explorer, click Upload item, and select the file.

**Query All Items**: When the data is uploaded, we're creating a new SQL Query to select all items from Products. After you see the results, switch to the Query Stats page to see the RU charge. The cost should be around 7 to 8 Request Units.

**Compare Query Variations**: Is the RU count the same if you select only product name and price instead of all fields? Open a new SQL Query tab and try selecting just specific fields. You'll notice that query execution time actually increases slightly when you select specific fields, resulting in a small increase in RU cost - around 8.22 RUs compared to 7.46 RUs for selecting all fields.

**Understand the Metrics**: If you compare the stats for both queries, you'll see that execution time increases when you filter fields because of the additional processing. Retrieved document size stays the same because Cosmos has to read the entire document, but output document size is much smaller for the filtered query.

**Query for Single Product**: Try querying for one product by name and then by productId. Querying by name costs significantly more - around 18 to 19 RUs - because the name field doesn't have an index, so Cosmos has to read every row. Querying by productId only costs about 2.8 RUs because it can use the index lookup.

**Analyze Index Impact**: The difference here is dramatic. The name field query requires document load time of around 2 milliseconds and retrieves 1000 documents, while the productId query only requires 0.02 milliseconds and retrieves 1 document. You can see that RUs are calculated from multiple factors including query execution time and index lookup time.

---

## Alternative Data Modelling and RUs

**Consider Bulk Load Approach**: With a small dataset, it may be cheaper to store it as an array inside a single document. This is a bulk load approach where application code can fetch all the products in a single document from Cosmos cheaply, and then filter the list in memory. The app can use an expiration cache so the list in memory gets refreshed every few minutes.

**Create Alternative Container**: We can try this approach by creating an alternative container called ReferenceData. We're using the field refDataType as the partition key. We won't supply an index policy for this container, so it will use the default behavior of indexing all fields.

**Compare Index Settings**: Open both containers in the Portal and compare their index settings. The default is for all fields to be indexed, which uses more storage. In some cases where all fields are indexed, the index size might be bigger than the data size itself.

**Upload Reference Data**: We're uploading the documents in the refData JSON file to the new container. This represents the same product list, but structured as an array in a single document rather than 1000 separate documents.

**Query Reference Data**: Run a query to fetch all products where refDataType equals Products. This costs around 3.6 RUs to retrieve all the data. Now try querying for a single product within the array using the IN keyword. This costs around 4.94 RUs.

**Calculate Scale Impact**: Consider the difference at scale. If your app fetched every product individually from Cosmos with 10 instances making 10 queries per second, you would nearly hit the throughput limit with the individual document approach - 10 times 10 times 4.94 equals 494 out of 500 RU per second. But if your app used the bulk query and instances cached the results for at least one second, you'd use less than 10 percent of the throughput - 10 times 1 times 3.59 equals only 35.9 out of 500 RU per second.

**Key Takeaway**: You need to model your data and architect your application carefully if you intend to use CosmosDB at high scale. Data modeling choices have huge impacts on RU consumption, and application patterns like caching can reduce costs by an order of magnitude.

---

## Lab

**The Challenge**: The cheapest way to read individual documents from Cosmos is to fetch them using the object ID and partition key. That's called a point read and costs 1RU for documents up to 100KB. Find the object ID for the reference data item we inserted in the second approach and check the RU cost to fetch it using the ID and partition key. Do you get 1RU? Are there any expensive parts of the query?

**Explore Further**: This hands-on practice will help you understand the difference between point reads and queries, and why point reads are so much more cost-effective.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up resource groups.

This cleanup is important to avoid unnecessary charges on your Azure subscription.
