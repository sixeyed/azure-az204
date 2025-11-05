# Azure Table Storage - Hands-On Exercises

## Exercise 1: Creating a Table

Let's start by creating our Azure resources. We'll need a Resource Group and a Storage Account.

First, we're creating a resource group using the az group create command with the name "labs-storage-table", adding a tag for "courselabs=azure" which helps us track and organize our course resources, and placing it in the West Europe location. The tag is a best practice for resource management - it allows you to easily identify and filter resources that belong to specific projects or environments.

Now we'll create a Storage Account within this resource group. We're using the az storage account create command, specifying the resource group we just created, setting the SKU to Standard LRS for locally redundant storage which provides durability by keeping multiple copies of your data within a single datacenter, using the same West Europe location to keep everything co-located, and providing a unique storage account name. Remember that storage account names must be globally unique across all of Azure, so you'll need to choose something distinctive.

Now comes the interesting part - creating a table. We're using the storage table create command. The mandatory parameters are simple: just the table name and the storage account name. We're creating a table called "students" which will store our entity data.

The output confirms the table has been created. It's worth noting that empty tables don't cost anything - you only pay when there's actual data stored in the table. This is different from some database services where you pay for provisioned capacity regardless of usage.

Let's take a look in the Azure Portal. We're navigating to the Storage Account and opening the Tables view. As expected, there's not much to see with an empty table - just the table name and some metadata. Let's switch to the Storage Browser instead, which provides a better interface for working with table data. The Storage Browser gives you a visual way to add, edit, and query entities directly.

## Exercise 2: Adding Entities

Now let's add some entities to understand the schema flexibility. We'll use the Storage Browser to add several entities with different structures, which demonstrates one of Table Storage's key features - schema-less design.

For the first entity, we're setting the Partition Key to "org1", the Row Key to "1023", and adding properties for FirstName, LastName, and Role. Remember that Partition Key and Row Key together form the unique identifier for each entity - they're the only required properties, and everything else is optional.

For the second entity, we're using the same partition key "org1" but a different Row Key "1040", with similar properties but different values. Entities with the same partition key are stored together, which enables efficient querying and transactional operations within a partition.

Now watch this - for the third entity, we're using a completely different structure. The Partition Key is "org2", the Row Key is "aed1895", and instead of separate name fields, we're using a single FullName property, plus a CountryCode field. This is completely valid - each entity can have its own unique set of properties.

And for the fourth entity, we're mixing data types in interesting ways. The Partition Key is "23124" which is a numeric string, the Row Key is "stonemane" which is a text string, and we're not adding any additional properties at all - just the mandatory keys. This demonstrates the extreme flexibility of Table Storage's schema.

This demonstrates the schema flexibility I mentioned earlier. All these different entity structures coexist happily in the same table. You're not locked into a rigid schema like you would be with a traditional relational database. This flexibility makes Table Storage particularly useful for scenarios where your data structure might evolve over time or where different types of entities need to share the same table.

## Exercise 3: Querying with OData

Table Storage provides an OData REST API, which means we can query our data using simple HTTP requests with curl. OData is an open protocol that provides a standardized way to query and manipulate data over HTTP.

First, let's get the table storage endpoint URL. We're running az storage account show with a query to extract the primary endpoints, specifically the table endpoint. This endpoint will be the base URL for all our table operations.

The URL format is straightforward - we append the table name to the endpoint, with an empty query in parentheses to retrieve all entities. This follows the OData URI conventions for querying table data.

Let me try this curl command now to fetch all entities from our table... and as you can see, we get a "Resource not found" error. This might seem surprising since we know the table exists and has data. The issue here is that even though OData is supported and the REST API is available, public access isn't enabled by default for security reasons. Azure enforces authentication on all storage operations to protect your data.

## Exercise 4: Using SAS Tokens

We need to generate a Shared Access Signature token to authenticate our requests. A SAS token is a secure way to grant temporary, limited access to your storage resources without exposing your account keys. We'll use the az storage table generate-sas command to create one.

For the expiry date, we're setting it to 2 hours from now - this is a security best practice, keeping the validity window as short as necessary for your task. The permissions parameter is set to "r" for read-only access, which follows the principle of least privilege. Notice that we can create a very fine-grained token that's restricted to just this specific table, not the entire storage account. This granular control is one of the key security features of SAS tokens.

Now with the SAS token, let's try that curl command again. The URL now includes the SAS token as query parameters - these parameters include the signature, expiry time, permissions, and other security information. And there's our data returned in the response - the authentication worked.

Let me try some more specific queries to demonstrate OData's capabilities. To get a specific entity, we specify both the PartitionKey and RowKey in the query URL. This is the most efficient query pattern because it targets a single entity directly using its unique identifier.

By default, the response is in XML format, which is OData's standard format. But we can request JSON by adding an Accept header set to "application/json". And if we want even cleaner JSON without the OData metadata wrapper, we can specify "application/json;odata=nometadata" in the Accept header. This gives us just the entity data without all the OData protocol information.

Notice in the response data that there's an automatically generated Timestamp field that shows when each entity was created or last updated. Azure manages this timestamp automatically - you can't set it yourself, but it's useful for tracking changes and implementing optimistic concurrency patterns.

## Exercise 5: Using Table Storage in Applications

Now let's see Table Storage in action within an application. We're going to run a .NET application that uses Serilog, a popular logging library that has built-in support for writing log events directly to Azure Table Storage. This demonstrates a real-world use case where Table Storage excels - storing high-volume, semi-structured log data.

First, we need to create a table for the logs. We're creating a new table called "FulfilmentLogs" using the az storage table create command with the same storage account we've been working with. The application will write all its log events to this table.

Next, we need the connection string so our application can authenticate and connect to the storage account. We're running az storage account show-connection-string to retrieve this. The output format is tab-separated values which makes it easy to capture in a variable or use directly in configuration.

The connection string format includes multiple components separated by semicolons: the protocol specification, the account name, the account key for authentication, and endpoints for all the different storage services - blob, file, queue, and table. This single connection string provides complete access to all storage features.

Now we need to update the application configuration. In the appsettings.json file in the project directory, there's a placeholder for the connection string. We're replacing that placeholder with our actual connection string, which allows the logging library to connect to our Table Storage account.

Let's run the application using dotnet run from the project directory. Notice that we don't see any console output - that's because the application is configured to write all logs to Table Storage in the cloud rather than to the console. The application is running and processing orders, but the logs are being sent to Azure instead of displaying locally.

We'll let this run for a few minutes to generate a meaningful number of log entries, giving us data to explore and query... and now we'll stop it with Ctrl+C.

Back in the Azure Portal, navigating to the Storage Browser for the FulfilmentLogs table, you can see numerous log entries that the application created. Take a look at how the PartitionKey and RowKey are constructed - they're using a combination of reverse chronological timestamp and log level. This is a clever pattern for time-series data in Table Storage because the reverse timestamp (using a large number minus the current ticks) means the most recent logs come first when you query by partition key, and grouping by log level within the partition makes it easy to filter for errors or warnings.

## Exercise 6: Lab Challenge

Here's your challenge: Can you query the fulfilment log entries to find just the error events? You can approach this either through the Storage Browser interface using the filter options, or by constructing OData queries with the appropriate filter expressions.

The Storage Browser provides a filter textbox where you can write OData query expressions. You'll want to filter based on the properties that indicate error-level log events. Think about what property name Serilog might use to store the log level.

Once you find the errors, look at the log message content. What do you think needs to be done to fix the underlying issue causing these errors? The error messages should give you clues about what's failing in the application logic.

Take some time to explore this on your own, examining both the structure of the log entities and the content of the error messages. When you're ready, check out the hints or solution files for guidance on the OData syntax and interpretation of the errors.

## Cleanup

When you're finished experimenting with Table Storage, remember to clean up your resources to avoid unnecessary charges. Simply run az group delete with the resource group name "labs-storage-table", using the -y flag to skip the confirmation prompt and --no-wait to run the deletion asynchronously without waiting for completion. This removes the resource group and all contained resources - the storage account, all tables, and all data.

That concludes our hands-on exercises with Azure Table Storage. You've learned how to create tables, work with the schema-less entity model, query data using OData, secure access with SAS tokens, and integrate Table Storage into applications for real-world scenarios like logging.
