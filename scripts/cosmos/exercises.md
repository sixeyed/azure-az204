# Cosmos DB - Basic Exercises Narration Script

## Exercise Overview

In this hands-on lab, we'll create a Cosmos DB account, set up a database using the NoSQL API, and run a real application that uses Cosmos DB for data storage. Let's dive in.

## Creating a Cosmos DB Account via the Portal

First, let's explore the Azure Portal to see what options are available when creating a Cosmos DB account.

Open the Azure Portal and navigate to the new resource page. Search for "cosmos" and select Azure Cosmos DB. You'll be prompted to select the API you want to use - for this lab, we'll choose NoSQL, which is what Microsoft calls their native document database API.

Notice the configuration options available. The Capacity Mode setting lets you choose between provisioned throughput or serverless. Provisioned mode allows you to use the free tier and set price caps to control costs - this is useful when you want predictable pricing. Serverless mode only charges for what you actually use, which can be more cost-effective for sporadic workloads.

Geo-Redundancy enables data synchronization across multiple Azure regions for high availability and disaster recovery. You can even enable multi-region writes, allowing applications to write to the nearest region for even better availability and lower latency.

The Backup Policy section lets you configure automated data backups with customizable retention periods. This is crucial for compliance and disaster recovery scenarios.

Take a moment to review these options, but don't create the account through the Portal yet - we'll use the Azure CLI for a more repeatable and scriptable approach.

## Creating Resources with Azure CLI

Now let's create our resources using the Azure CLI, which gives us better control and repeatability.

First, we're creating a resource group called "labs-cosmos" in West Europe, with the courselabs=azure tag to help identify resources created for this course.

Before creating the Cosmos DB account, we can check the available options using the help flag. Take a moment to review the parameters - you'll see options for consistency levels, geo-replication, network access, and many other settings.

Now we're creating the Cosmos DB account. We're enabling public network access so we can connect from anywhere during development - in production, you'd typically restrict this with firewall rules or private endpoints. The kind parameter is set to GlobalDocumentDB, which is the internal name for Cosmos DB's NoSQL API. Remember to replace the placeholder with a globally unique name.

This command will take a few minutes to complete because Azure is provisioning the distributed database infrastructure across availability zones.

Here's an important concept - we've created a Cosmos DB account, not a database. The account is a grouping and management mechanism that will contain one or more databases. Think of it like a server in traditional database systems - you have one server that hosts multiple databases.

## Exploring the Portal

While the account is being created, open the Azure Portal and navigate to your resource group. Once the account creation completes, open it and you'll see a Quick start wizard with helpful guidance for getting started.

The account itself doesn't store any data - it's just a container and coordination point for databases. Let's create a database now.

## Creating a Database

We're creating a database using the SQL API - remember, this is what the CLI calls the NoSQL driver. The naming can be confusing, but "SQL API" just means the native Cosmos DB API that supports SQL-like queries.

Before running the creation command, let's check the help to understand the available parameters. You'll see options for throughput provisioning, shared throughput, and autoscale settings.

Now we're creating a database called AssetsDb within our Cosmos DB account. This creates quickly since it's just a logical container at this point - no physical storage is allocated until we add containers and data.

Check the Azure Portal now. Notice that databases under a Cosmos DB account don't show as separate resources in your resource group list. This is similar to how apps in an App Service plan work - they're managed within the parent resource rather than as independent resources.

## Working with Connection Strings

Every application that connects to Cosmos DB needs a connection string containing the endpoint and authentication key. Let's see how to retrieve it.

In the Portal, open your Cosmos DB account and navigate to the Keys blade. You'll see the primary and secondary connection strings, along with the individual keys and endpoint URIs. Having primary and secondary keys allows you to rotate keys without downtime - applications can use one key while you regenerate the other.

Make a note of the primary connection string - but never commit this to source control or share it publicly. This connection string provides full access to your database, including the ability to read, write, and delete data.

You can also retrieve connection strings using the CLI. The command lists all connection strings, returning them in JSON format.

But what if you only want the Primary SQL Connection String value for scripting purposes? Maybe you need to inject it into an application configuration or another command. This is where JMESPath queries become invaluable.

We're building a query that selects the connectionStrings array, filters for the object where description equals "Primary SQL Connection String", extracts just the connectionString value, and outputs it in TSV format for easy scripting. This type of query is essential when you're automating deployments and need to inject configuration values into applications.

## Understanding Cosmos DB Data Structure

Before we run the application, let's talk about how Cosmos DB structures data.

Cosmos DB scales incredibly well because of its partitioning strategy. Data is distributed across multiple physical storage locations called partitions, and those partitions can all be read from and written to simultaneously in parallel. To increase capacity, Cosmos DB just adds more partitions automatically. This horizontal scaling is what enables Cosmos DB to handle massive workloads.

This distributed architecture is all managed automatically by Azure, but it does mean that data in Cosmos DB has a different structure than a traditional SQL database. Items in the same container don't need to have identical schemas - you can mix different document structures in the same container. There are also special fields like partition keys that control how data is distributed, and the lowercase "id" field that uniquely identifies each document.

## Running the Asset Manager Application

Now let's run a real .NET application that uses Cosmos DB with Entity Framework. This application demonstrates how traditional object-relational patterns can work with a NoSQL database.

Let's look at the code structure. The Asset.cs file is a Plain Old C# Object with data fields and relationships - there's nothing Cosmos-specific about it. This is just standard C# code.

The AssetContext.cs file is the Entity Framework context that provides access to entity objects. This uses the standard EF Core patterns that developers are already familiar with.

The Dependencies.cs file manages different storage options. In SQL mode, it configures the app to use Cosmos DB, but the same application can also use SQL Server or in-memory storage. The beauty here is that the application code doesn't need to be tightly coupled to Cosmos DB - Entity Framework handles the translation between objects and database storage.

To run the application, you'll need the .NET 6 SDK installed. We're using the dotnet run command with parameters to configure the database connection. The Database:Api parameter tells the app to use SQL mode for Cosmos DB, and ConnectionStrings:AssetsDb provides the actual connection string. Make sure to quote the connection string since it contains special characters.

The application starts and listens on port 5208. Browse to localhost on that port and you'll see reference data items with randomly generated IDs.

What just happened? The application used Entity Framework to automatically create the database schema in Cosmos DB, insert some reference data, and then query and display that data. Check your terminal and you'll see SQL statements logged - these are the queries Entity Framework generated to interact with Cosmos DB.

## Exploring Data in Cosmos DB

Let's explore what was created in Cosmos DB. Open the Data Explorer in the Azure Portal.

You'll see containers - these are similar to tables in a relational database, but with a key difference: items in a container don't need to have the same schema. This schema flexibility is a hallmark of NoSQL databases.

In our application, one container stores all object types. Browse the items and you'll see Location objects and AssetType objects mixed together. Each has different properties, but they coexist happily in the same container. This is enabled by the Discriminator field, which identifies the object type.

## Adding Data Manually

Let's add a new location manually to see how Cosmos DB works. In the Data Explorer, you can create a new item by providing a JSON document.

We're creating a location with several important fields. The uppercase Id field is an application property used by Entity Framework. The AddressLine1, Country, and PostalCode are business data. The Discriminator field is set to "Location" - this is how Entity Framework identifies the object type when multiple types share a container.

The lowercase id field is the Cosmos DB item identifier - it's required and must be unique within the partition. In this case, the id field includes the discriminator as a prefix, creating a composite identifier.

After adding the item, refresh your browser with the Asset Manager application. It might take a moment to reload. Is the new location displayed? Yes - the application queries all items with the Location discriminator and displays them. Entity Framework filtered the mixed container to show only Location objects.

## Handling Errors

Let's experiment with what happens if we add an item incorrectly. Try inserting a location document without providing the Id field or a properly formatted id field.

Cosmos DB accepts this because it automatically generates an "id" field if you don't provide one. But now reload the website - you'll see an error.

Why? The application expects the uppercase Id property to exist, and it expects the lowercase id field to follow a specific pattern with the discriminator prefix. When these conventions aren't followed, Entity Framework can't properly reconstruct the object.

To fix this, go back to the Data Explorer and edit the item. Copy the auto-generated id value to create a new field called Id, then edit the id field to add "Location|" as a prefix.

Save your changes and refresh the website - now all locations display correctly. This demonstrates the importance of understanding both the database requirements and your application's conventions.

## Querying with SQL

Here's something interesting - even though Cosmos DB NoSQL is a document database, it supports SQL-like queries. This makes it accessible if you're already familiar with SQL syntax.

In the Data Explorer, try running a query to get all asset types showing just the ID and description. You're selecting specific fields from a container aliased as "c", filtering where the Discriminator equals "AssetType".

Try another query to count locations with "1" in the postal code. This uses SELECT VALUE COUNT to return a scalar value instead of an object, and the CONTAINS function for substring matching.

The SQL syntax is similar to standard SQL, but there are some differences. You query from a single container rather than joining multiple tables. You can use document-specific functions like CONTAINS. And SELECT VALUE returns a single value rather than a row object.

## Key Takeaways

Let's review what we've learned. Cosmos DB accounts contain databases, which contain containers, which contain items - this is the hierarchy you need to understand.

The NoSQL driver supports SQL-like queries despite the confusing name. It's called NoSQL because it's a document database, but it uses SQL syntax for queries.

Connection strings provide access to your database and should be kept secure. Never commit them to source control - use Azure Key Vault or managed identities in production.

Containers are schema-flexible, allowing items with different structures to coexist. This flexibility is powerful but requires careful application design.

The lowercase id field is required and must be unique within a partition. This is a Cosmos DB requirement separate from your application's own ID fields.

Entity Framework can work with Cosmos DB, abstracting many of the database-specific details and allowing you to use familiar programming patterns.

The Azure CLI provides powerful querying capabilities with JMESPath for automation and scripting scenarios.

## Lab Challenge

Now it's your turn to practice. Use the Data Explorer to run SQL queries and find all asset types, showing just the ID and description. Then count the locations that have a "1" in the postal code.

Take a few minutes to experiment with different queries. Try filtering by different fields, counting records, and selecting various properties. This hands-on practice will help cement your understanding.

## Cleanup

When you're done with the lab, clean up your resources to avoid unnecessary charges. The az group delete command removes the resource group and everything in it, including the Cosmos DB account, database, and all data.

The -y flag confirms the deletion without prompting, and --no-wait returns immediately without waiting for deletion to complete. Deletion happens asynchronously in the background.

## Closing

In this lab, you've created a Cosmos DB account, worked with databases and containers, run a real application using Entity Framework with Cosmos DB, and explored data using both the Portal and SQL queries.

You now have a solid foundation for working with Cosmos DB. In future videos, we'll dive deeper into AZ-204 exam-specific topics like consistency levels, partitioning strategies, change feeds, and performance optimization.

Stop the application with Ctrl-C if it's still running, and I'll see you in the next video.
