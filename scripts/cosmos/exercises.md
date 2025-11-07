# Cosmos DB

## Reference

Cosmos DB is Azure's globally distributed, multi-model database service designed for planet-scale applications. You can start with a single-region deployment and expand to global replication with multi-region writes as your needs grow. The service supports multiple API drivers including NoSQL, MongoDB, Cassandra, Gremlin, and Table Storage, all using the same underlying distributed database engine. The documentation covers everything from basic database operations to advanced features like consistency levels, change feeds, and performance optimization. The command line interface provides complete control through the az cosmosdb commands for managing accounts, databases, and containers.

## Create a Cosmos DB database

**Navigate to the Portal**: We're opening the Azure Portal and searching for "cosmos" to create a new Azure Cosmos DB resource. When you select it, you'll be prompted to choose an API. For this lab, we're choosing NoSQL, which is Microsoft's native document database API. This was previously called the SQL API, and you'll still see that name in the CLI and some documentation, but the Portal now calls it NoSQL.

**Explore Configuration Options**: Before creating anything, let's look at what's available. The Capacity Mode setting offers provisioned throughput or serverless options. Provisioned mode allows you to use the free tier and set price caps for predictable costs, which is useful when you want to control spending. Serverless mode charges only for what you use, making it cost-effective for sporadic workloads.

**Understand Geo-Redundancy**: The geo-redundancy options enable data synchronization across multiple Azure regions for high availability and disaster recovery. You can even enable multi-region writes, allowing applications to write to the nearest region for better availability and lower latency.

**Review Backup Policy**: The Backup Policy section lets you configure automated data backups with customizable retention periods. This is crucial for compliance and disaster recovery scenarios. CosmosDB is an enterprise-grade database, so make sure you understand the pricing model before creating resources.

**Create Resource Group**: We're creating a resource group called "labs-cosmos" in your preferred region with the courselabs=azure tag. This tag helps you track resources created for this course, which is a best practice for organizing and managing resources.

**Explore Create Command**: Before creating the Cosmos DB account, let's check what options are available using the help flag. You'll see many more options than what appears in the Portal's initial creation screen, including settings for consistency levels, network rules, geo-replication, and backup policies.

**Create Your Account**: We're creating the Cosmos DB account with public network access enabled so we can connect from anywhere during development. In production, you'd typically restrict this with firewall rules or private endpoints. The kind parameter is set to GlobalDocumentDB, which is the internal name for Cosmos DB's NoSQL API. Remember to replace the placeholder with a globally unique name.

**Understand the Hierarchy**: This command creates a Cosmos DB account, not a database. The account is a grouping mechanism that will contain one or more databases, similar to how a server hosts multiple databases in traditional database systems. Think of it as the management and coordination point for your databases.

**Wait for Provisioning**: The command will take a few minutes to complete because Azure is provisioning the distributed database infrastructure across availability zones.

**Portal Review**: Open the new resource in the Portal. This is just a CosmosDB account, a grouping mechanism for databases. On the resource page there's a Quick start wizard with helpful guidance for getting started. Notice that databases under a Cosmos DB account don't show as separate resources in your resource group, similar to how apps in an App Service plan work.

**Create Database**: We're creating a database using the SQL API - remember, this is what the CLI calls the NoSQL driver. Before running the creation command, check the help to understand the available parameters. You'll see options for throughput provisioning, shared throughput, and autoscale settings.

**Execute Database Creation**: We're creating a database called AssetsDb within our Cosmos DB account. This creates quickly since it's just a logical container at this point - no physical storage is allocated until we add containers and data.

**Verify in Portal**: Check in the Portal now and you can see the new database. Open the Data Explorer for the account and you'll see the database listed. It's empty right now, but ready to use.

**View Connection Information**: Open the Keys blade to see the connection string for client apps. You'll see the primary and secondary connection strings, along with individual keys and endpoint URIs. Make a note of the primary connection string, but never commit this to source control or share it publicly. Having primary and secondary keys allows you to rotate keys without downtime.

**Get Connection String from CLI**: You can also get the connection string from the CLI using the keys list command. The command returns all connection strings in JSON format.

**Extract Specific Values**: For scripting purposes, you often need just the Primary SQL Connection String value to inject into application configuration. We're building a query that selects the connectionStrings array, filters for the object where description equals "Primary SQL Connection String", extracts just the connectionString value, and outputs it in TSV format. This type of query is essential when you're automating deployments.

---

## Run an app using Cosmos DB with Entity Framework

**Understand Data Partitioning**: CosmosDB scales incredibly well because of its partitioning strategy. Data is distributed across multiple physical storage locations called partitions, and those partitions can all be read from and written to simultaneously. To increase capacity, Cosmos DB just adds more partitions automatically. This horizontal scaling is what enables Cosmos DB to handle massive workloads.

**Note Data Structure Differences**: This distributed architecture is all managed automatically, but it does mean that data in Cosmos DB has a different format from a standard SQL database. Items in the same container don't need to have identical schemas, and there are special fields like partition keys and the lowercase id field.

**Review Application Code**: We have a simple .NET application which can use CosmosDB for storage. It is built with the CosmosDB NoSQL library, but the data model is not Cosmos-specific. The Asset.cs file is a POCO with data fields and relationships, the AssetContext.cs file is the EF context object providing access to entities, and the Dependencies.cs file manages the different storage options the app can use, configuring Cosmos DB in SQL mode.

**Run the Application**: We're running the app locally - you'll need the .NET 6 SDK installed. We're using parameters to set the database type and connection string. Make sure to quote the connection string since it contains special characters.

**Browse the Application**: When you browse to the app at localhost:5208, you'll see reference data items with random IDs. The application uses an ORM to set up the database schema and insert this reference data. Check the logs in your terminal and you'll see lots of SQL statements - these are the queries the ORM generates to interact with Cosmos DB.

---

## Explore the data

**Navigate to Data Explorer**: In the Cosmos Data browser you can see containers. Containers are kind of like tables, except that items in a container don't need to have the same schema. This schema flexibility is a hallmark of NoSQL databases.

**Understand Container Structure**: In this app one container is used for all the object types. Check the items and you'll see Location objects and AssetType objects mixed together. Each has different properties, but they coexist happily in the same container.

**Add New Location Manually**: Let's add a new location using Data Explorer. We're creating a JSON document with several important fields. The Discriminator field is set to "Location" - this is an ORM mechanism for identifying the object type when multiple types share a container. The uppercase Id is an object property, while the lowercase id is the item identifier which includes the discriminator as a prefix.

**Test the Addition**: Refresh the browser with your Asset Manager website. It might take a while to reload - is the new location shown? The application queries all items with the Location discriminator and displays them.

**Experiment with Errors**: What happens if you insert a new item without any ID columns? Try adding a location document without the required ID fields. CosmosDB will automatically generate the id field if you don't specify it, but when you reload the website you'll see an error.

**Fix the Data**: The app expects the uppercase Id property to exist, and it expects the lowercase id field to follow a specific pattern with the discriminator prefix. To fix this, go back to the Data Explorer and edit the item. Copy the id field to a new field called Id, then edit the id field, inserting "Location|" in front of the actual identifier. Save your changes and refresh the website - now all locations display correctly.

---

## Lab

**The Challenge**: Is it SQL or NoSQL? The NoSQL driver actually supports SQL queries, though not the full SQL syntax. Run some queries in the Data Explorer to find all the asset types showing just the ID and description, and count the locations with a "1" in the postal code.

**Explore Query Syntax**: Take some time to experiment with different queries. Try filtering by different fields, counting records, and selecting various properties. This hands-on practice will help cement your understanding of how Cosmos DB's SQL-like query language works.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up resource groups.

This cleanup is important to avoid unnecessary charges on your Azure subscription.
