# Cosmos DB - Basic Exercises Narration Script

## Exercise Overview

In this hands-on lab, we'll create a Cosmos DB account, set up a database using the NoSQL API, and run a real application that uses Cosmos DB for data storage. Let's dive in.

## Creating a Cosmos DB Account via the Portal

First, let's explore the Azure Portal to see what options are available when creating a Cosmos DB account.

Open the Azure Portal and navigate to the new resource page. Search for "cosmos" and select Azure Cosmos DB. You'll be prompted to select the API you want to use - for this lab, we'll choose NoSQL.

Notice the configuration options available:

**Capacity Mode**: You can choose between provisioned throughput or serverless. Provisioned mode allows you to use the free tier and set price caps to control costs.

**Geo-Redundancy**: You can enable data synchronization across multiple Azure regions, with optional multi-region writes for even better availability.

**Backup Policy**: Configure automated data backups and specify backup storage retention.

Take a moment to review these options, but don't create the account through the Portal yet - we'll use the Azure CLI for a more repeatable approach.

## Creating Resources with Azure CLI

Now let's create our resources using the Azure CLI, which gives us better control and repeatability.

First, create a resource group:

```bash
az group create -n labs-cosmos --tags courselabs=azure -l westeurope
```

Before creating the Cosmos DB account, let's check the available options:

```bash
az cosmosdb create --help
```

Take a moment to review the parameters. You'll see options for consistency levels, geo-replication, network access, and more.

Now create the Cosmos DB account:

```bash
az cosmosdb create -g labs-cosmos --enable-public-network --kind GlobalDocumentDB -n <cosmos-db-name>
```

Remember to replace `<cosmos-db-name>` with a globally unique name. This command will take a few minutes to complete.

**Important**: Notice that we've created a Cosmos DB **account**, not a database. The account is a grouping mechanism that will contain one or more databases.

## Exploring the Portal

While that's creating, open the Azure Portal and navigate to your resource group. Once the account is created, open it and you'll see a Quick start wizard with helpful guidance.

The account itself doesn't store data - it's just a container for databases. Let's create one now.

## Creating a Database

Create a database using the SQL API - remember, this is what the CLI calls the NoSQL driver:

```bash
az cosmosdb sql database create --help
```

Review the parameters, then create the database:

```bash
az cosmosdb sql database create --name AssetsDb -g labs-cosmos --account-name <cosmos-db-name>
```

This creates quickly since it's just a logical container at this point.

Now check the Azure Portal. Notice that databases under a Cosmos DB account don't show as separate resources in your resource group, similar to how apps in an App Service plan work. They're managed within the account resource.

## Working with Connection Strings

Every application that connects to Cosmos DB needs a connection string. Let's see how to retrieve it.

In the Portal, open your Cosmos DB account and navigate to the Keys blade. You'll see the primary and secondary connection strings, along with the individual keys.

Make a note of the primary connection string - but never commit this to source control or share it publicly. It provides full access to your database.

You can also retrieve connection strings using the CLI:

```bash
az cosmosdb keys list --type connection-strings -g labs-cosmos -n <cosmos-db-name>
```

This returns JSON with all connection strings. But what if you only want the Primary SQL Connection String value for scripting purposes?

This is where JMESPath queries come in handy. Let's build a query that:
- Selects the connectionStrings array
- Filters for the object where description equals "Primary SQL Connection String"
- Extracts just the connectionString value
- Outputs it in TSV format for easy scripting

Here's the command:

```bash
az cosmosdb keys list --type connection-strings -g labs-cosmos --query "connectionStrings[?description==\`Primary SQL Connection String\`].connectionString" -o tsv -n <cosmos-db-name>
```

This type of query is essential when you're automating deployments and need to inject configuration values into applications.

## Understanding Cosmos DB Data Structure

Before we run the application, let's talk about how Cosmos DB structures data.

Cosmos DB scales incredibly well because of its partitioning strategy. Data is distributed across multiple storage locations - called partitions - and those locations can all be read from and written to simultaneously. To increase capacity, Cosmos DB just adds more partitions.

This is all managed automatically, but it does mean that data in Cosmos DB has a different structure than a traditional SQL database. Items in the same container don't need to have the same schema, and there are special fields like partition keys that control data distribution.

## Running the Asset Manager Application

Now let's run a real .NET application that uses Cosmos DB with Entity Framework. This application demonstrates how traditional object-relational patterns can work with Cosmos DB.

Let's look at the code structure:

**Asset.cs**: This is a Plain-Old C# Object with data fields and relationships - nothing Cosmos-specific about it.

**AssetContext.cs**: The Entity Framework context that provides access to entity objects. This uses the standard EF Core patterns.

**Dependencies.cs**: This manages different storage options. In SQL mode, it configures the app to use Cosmos DB.

The beauty here is that the application code doesn't need to be tightly coupled to Cosmos DB - Entity Framework handles the translation.

To run the application, you'll need the .NET 6 SDK installed. Then use these parameters to configure the database connection:

```bash
dotnet run --project src/asset-manager --Database:Api=Sql --ConnectionStrings:AssetsDb='<cosmos-connection-string>'
```

Make sure to quote the connection string since it contains special characters.

The application starts on port 5208. Browse to http://localhost:5208 and you'll see reference data items with randomly generated IDs.

**What just happened?** The application used Entity Framework to:
1. Create the database schema in Cosmos DB
2. Insert reference data
3. Query and display that data

Check your terminal and you'll see SQL statements logged. These are the queries Entity Framework generated to interact with Cosmos DB.

## Exploring Data in Cosmos DB

Let's explore what was created in Cosmos DB. Open the Data Explorer in the Azure Portal.

You'll see **containers** - these are similar to tables in a relational database, but with a key difference: items in a container don't need to have the same schema.

In our application, one container stores all object types. Browse the items and you'll see Location objects and AssetType objects mixed together. Each has different properties, but they coexist in the same container.

## Adding Data Manually

Let's add a new location manually to see how Cosmos DB works. In the Data Explorer, create a new item:

```json
{
    "Id": "64eb3e9f-e92d-4a63-b234-08da7b01d0d6",
    "AddressLine1": "Parliament House",
    "Country": "Australia",
    "Discriminator": "Location",
    "PostalCode": "2600",
    "id": "Location|64eb3e9f-e92d-4a63-b234-08da7b01d0d6"
}
```

Notice two important fields:

**Discriminator**: This is an Entity Framework mechanism for identifying the object type when multiple types share a container.

**id vs Id**: The lowercase "id" is the Cosmos DB item identifier - it's required and must be unique. The uppercase "Id" is an application property. In this case, the id field includes the discriminator as a prefix.

After adding the item, refresh your browser with the Asset Manager application. It might take a moment to reload. Is the new location displayed? Yes - the application queries all items with the Location discriminator and displays them.

## Handling Errors

Let's experiment with what happens if we add an item incorrectly. Try inserting this item without proper ID fields:

```json
{
    "AddressLine1": "1 Parliament Place",
    "Country": "Singapore",
    "Discriminator": "Location",
    "PostalCode": "178880"
}
```

Cosmos DB accepts this because it automatically generates an "id" field if you don't provide one. But now reload the website - you'll see an error.

Why? The application expects:
1. The "Id" property to exist (the uppercase one)
2. The "id" field to follow a specific pattern with the discriminator prefix

To fix this, go back to the Data Explorer and edit the item:
1. Copy the auto-generated "id" value to a new field called "Id"
2. Edit the "id" field to add "Location|" as a prefix

Save your changes and refresh the website - now all locations display correctly.

This demonstrates the importance of understanding both the database requirements and your application's conventions.

## Querying with SQL

Here's something interesting: even though Cosmos DB NoSQL is a document database, it supports SQL-like queries. This makes it accessible if you're already familiar with SQL.

In the Data Explorer, try these queries:

**Get all asset types with just ID and description**:
```sql
SELECT c.Id, c.Description FROM c WHERE c.Discriminator = 'AssetType'
```

**Count locations with '1' in the postal code**:
```sql
SELECT VALUE COUNT(1) FROM c WHERE c.Discriminator = 'Location' AND CONTAINS(c.PostalCode, '1')
```

The SQL syntax is similar to standard SQL, but there are some differences:
- You query from a single container (aliased as 'c')
- You can use the CONTAINS function for substring matching
- SELECT VALUE returns a scalar value instead of an object

## Key Takeaways

Let's review what we've learned:

1. **Cosmos DB accounts** contain databases, which contain containers, which contain items

2. **The NoSQL driver** supports SQL-like queries despite the name

3. **Connection strings** provide access to your database and should be kept secure

4. **Containers** are schema-flexible - items don't need identical structures

5. **The "id" field** is required and must be unique within a partition

6. **Entity Framework** can work with Cosmos DB, abstracting many of the database-specific details

7. **The Azure CLI** provides powerful querying capabilities for automation

## Lab Challenge

Now it's your turn. Use the Data Explorer to run SQL queries and find:

1. All asset types, showing just the ID and description
2. The count of locations with a '1' in the postal code

Take a few minutes to experiment with different queries. Try filtering, counting, and selecting different properties.

## Cleanup

When you're done with the lab, clean up your resources:

```bash
az group delete -y --no-wait -n labs-cosmos
```

This deletes the resource group and everything in it, including the Cosmos DB account, database, and all data.

## Closing

In this lab, you've created a Cosmos DB account, worked with databases and containers, run a real application using Entity Framework with Cosmos DB, and explored data using both the Portal and SQL queries.

You now have a foundation for working with Cosmos DB. In the next video, we'll dive deeper into AZ-204 exam-specific topics like consistency levels, partitioning strategies, change feeds, and performance optimization.

Stop the application with Ctrl-C or Cmd-C if it's still running, and I'll see you in the next video.
