# Azure Table Storage

## Reference

Table storage is a simple, scalable NoSQL database which you can host in an Azure Storage Account. It takes a no-SQL approach with a flexible schema, so you need to use dedicated libraries in your code to read and write data. It's an older part of the storage stack in Azure, existing before alternatives like MongoDB and Cosmos DB became available, so you'll see it in early Azure solutions. Cosmos DB is a better option for new projects but has compatibility with table storage, providing a migration path. The documentation covers table storage design guidelines, schema-less entity models, and OData query capabilities. The command line interface provides control through az storage table commands.

## Create a Table

Table Storage is a feature of Storage Accounts, so we'll start by creating the infrastructure we need.

**Create Infrastructure**: We're creating a Resource Group called "labs-storage-table" with course tracking tags and a Storage Account with locally redundant storage in West Europe. Remember that storage account names must be globally unique across all of Azure and can only contain lowercase letters and numbers.

**Create the Table**: We're using the storage table create command to create a table in the storage account called "students". The mandatory parameters are simple - just the table name and the storage account name. The output confirms the table has been created. It's worth noting that empty tables don't cost anything - you only pay when there's actual data stored in the table. This is different from some database services where you pay for provisioned capacity regardless of usage.

**Explore in Portal**: Let's take a look in the Azure Portal. We're navigating to the Storage Account and opening the Tables view. As expected, there's not much to see with an empty table - just the table name and some metadata. Let's switch to the Storage Browser instead, which provides a better interface for working with table data. The Storage Browser gives you a visual way to add, edit, and query entities directly through the web interface.

**Understanding Table Storage Concepts**: Table storage uses different terminology than a SQL database. Entities are the data items, like rows in SQL or objects in MongoDB - they're the individual records you store. Partition key is part of the entity's unique ID and serves as a grouping which determines where the data is stored physically in Azure's infrastructure. Row key is the unique part of the entity's ID within a partition. Together, partition key and row key form the complete unique identifier for each entity.

**Add Diverse Entities**: Use the storage browser to add several entities with different structures. For the first entity, we're setting Partition Key to "org1", Row Key to "1023", and adding properties for FirstName, LastName, and Role. For the second entity, we're using the same partition key "org1" but Row Key "1040", with similar properties but different values. Entities with the same partition key are stored together, enabling efficient querying and transactional operations within a partition.

**Demonstrate Schema Flexibility**: Now watch this - for the third entity, we're using a completely different structure. Partition Key is "org2", Row Key is "aed1895", and instead of separate name fields, we're using a single FullName property plus a CountryCode field. This is completely valid and demonstrates the schema-less nature of Table Storage.

**Minimal Entities**: For the fourth entity, we're using Partition Key "23124" which is a numeric string, Row Key "stonemane" which is a text string, and we're not adding any additional properties at all - just the mandatory keys. This demonstrates the extreme flexibility of Table Storage's schema.

**Schema Flexibility**: Note that entities can have different properties - tables do not have a fixed schema, unlike relational databases. Partition key and row key can have different formats - you can mix strings and integers based on your needs. Properties are not required beyond the keys - you can have entities with just the partition and row keys.

## Querying Table Storage with OData

Table storage provides an OData REST API, so you can query your data using simple HTTP requests with curl.

**Get Table Endpoint**: Let's print out the table storage domain name for your account using az storage account show with a query to extract the primary endpoints, specifically the table endpoint. This endpoint will be the base URL for all our table operations.

**Try Anonymous Access**: You can add the table name to the end of that URL, with an empty query in parentheses to retrieve all entities. Let's try this with curl. You'll get a "Resource not found" error. OData is supported and the REST API is available, but public access is not enabled by default for security reasons. Azure enforces authentication on all storage operations to protect your data.

## Using SAS Tokens

We need to generate a Shared Access Signature token to authenticate our requests.

**Generate SAS Token**: We're using az storage table generate-sas to create a token. For the expiry date, we're setting it to 2 hours from now - this is a security best practice, keeping the validity window as short as necessary. The permissions parameter is set to "r" for read-only access, following the principle of least privilege. Notice that we can create a fine-grained token that's restricted to just this specific table, not the entire storage account. This granular control is one of the key security features of SAS tokens.

**Query with SAS**: Now with the SAS token, let's try that curl command again. The URL now includes the SAS token as query parameters - these parameters include the signature, expiry time, permissions, and other security information. And there's our data returned in the response - the authentication worked successfully.

**Specific Entity Query**: To get a specific entity, we specify both the PartitionKey and RowKey in the query URL. This is the most efficient query pattern because it targets a single entity directly using its unique identifier.

**Format Options**: By default, the response is in XML format, which is OData's standard format. But we can request JSON by adding an Accept header set to "application/json". And if we want even cleaner JSON without the OData metadata wrapper, we can specify "application/json;odata=nometadata" in the Accept header. This gives us just the entity data without all the OData protocol information.

**Auto-Generated Fields**: Notice in the response data that there's an automatically generated Timestamp field that shows when each entity was created or last updated. Azure manages this timestamp automatically - you can't set it yourself, but it's useful for tracking changes and implementing optimistic concurrency patterns.

## Using table storage as a log sink

Now let's see Table Storage in action within an application.

**Understanding Serilog Integration**: We're going to run a .NET application that uses Serilog, a popular logging library that has built-in support for writing log events directly to Azure Table Storage. This demonstrates a real-world use case where Table Storage excels - storing high-volume, semi-structured log data.

**Create Log Table**: First, we need to create a table for the logs. We're creating a new table called "FulfilmentLogs" using az storage table create with the same storage account we've been working with. The application will write all its log events to this table.

**Get Connection String**: Next, we need the connection string so our application can authenticate and connect to the storage account. We're running az storage account show-connection-string to retrieve this. The output format is tab-separated values which makes it easy to capture in a variable or use directly in configuration. The connection string format includes multiple components separated by semicolons - the protocol specification, the account name, the account key for authentication, and endpoints for all the different storage services including blob, file, queue, and table.

**Configure Application**: Now we need to update the application configuration. In the appsettings.json file in the project directory, there's a placeholder for the connection string. We're replacing that placeholder with our actual connection string, which allows the logging library to connect to our Table Storage account.

**Run Application**: Let's run the application using dotnet run from the project directory. Notice that we don't see any console output - that's because the application is configured to write all logs to Table Storage in the cloud rather than to the console. The application is running and processing orders, but the logs are being sent to Azure instead of displaying locally. We'll let this run for a few minutes to generate a meaningful number of log entries.

**Examine Log Entries**: Back in the Azure Portal, navigating to the Storage Browser for the FulfilmentLogs table, you can see numerous log entries that the application created. Take a look at how the PartitionKey and RowKey are constructed - they're using a combination of reverse chronological timestamp and log level. This is a clever pattern for time-series data in Table Storage because the reverse timestamp means the most recent logs come first when you query by partition key, and grouping by log level within the partition makes it easy to filter for errors or warnings.

## Lab

Here's your challenge - can you query the fulfilment log entries to find just the error events?

**Your Task**: You can approach this either through the Storage Browser interface using the filter options, or by constructing OData queries with the appropriate filter expressions. The Storage Browser provides a filter textbox where you can write OData query expressions. You'll want to filter based on the properties that indicate error-level log events. Think about what property name Serilog might use to store the log level.

**Analyze Errors**: Once you find the errors, look at the log message content. What do you think needs to be done to fix the underlying issue causing these errors? The error messages should give you clues about what's failing in the application logic.

**Explore on Your Own**: Take some time to explore this on your own, examining both the structure of the log entities and the content of the error messages. When you're ready, check out the hints or solution files for guidance on the OData syntax and interpretation of the errors.

## Cleanup

When you're finished experimenting with Table Storage, remember to clean up your resources to avoid unnecessary charges.

**Delete Resource Group**: Simply run az group delete with the resource group name "labs-storage-table", using the -y flag to skip the confirmation prompt and --no-wait to run the deletion asynchronously without waiting for completion. This removes the resource group and all contained resources - the storage account, all tables, and all data.

That concludes our hands-on exercises with Azure Table Storage. You've learned how to create tables, work with the schema-less entity model, query data using OData, secure access with SAS tokens, and integrate Table Storage into applications for real-world scenarios like logging.
