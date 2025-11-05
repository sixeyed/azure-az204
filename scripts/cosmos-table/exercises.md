# Cosmos DB Table API - Exercise Walkthrough

## Exercise 1: Creating a Cosmos DB Table Database

Let's start by creating our Cosmos DB account with Table API support.

### Creating the Resource Group

First, we'll create a resource group for our lab resources. We're calling it "labs-cosmos-table" and placing it in West Europe. The command includes the courselabs=azure tag which helps us identify and track resources created for this course.

### Understanding the Creation Command

Before we create our Cosmos DB account, it's always good to explore the available options. The Azure CLI help flag shows us all the parameters we can use, including options for consistency levels, geo-replication, network configuration, and more. Take a moment to review these options - understanding what's available helps you make informed decisions about your database configuration.

### Creating the Cosmos DB Account

Here's the actual creation command, and notice something interesting about how Table API works. We're using the same "GlobalDocumentDB" kind that we use for the NoSQL API - this tells us that under the hood, Table API is built on top of the same document database engine that powers Cosmos DB's other APIs. The key difference is the capabilities parameter, where we specify "EnableTable". This additional capability flag tells Azure to enable the Table API compatibility layer on top of the document database engine.

This architecture is actually quite elegant - Microsoft has built multiple API surfaces on top of a single underlying storage engine, giving you flexibility in how you access your data while maintaining consistency and performance.

### Portal Exploration

Once the account is created, open it in the Azure Portal. You'll notice some key differences from other Cosmos DB APIs. The navigation structure is simpler - there are no Collections or Containers in the menu, just Account and Tables. This reflects the simpler schema of Table Storage compared to document databases.

There's also an Integrations section where you can add Azure Functions that trigger automatically when data changes in your tables. This is similar to change feed functionality in other Cosmos DB APIs, but tailored for the Table API's event model.

### Creating a Table

Now we'll create our first table called "FulfilmentLogs". Before running the command, let's check the help to see what options are available. The help output shows us the various parameters for configuring tables.

Notice how straightforward the creation command is - we just specify the table name, resource group, and account name. Unlike the SQL API where you need to think about partition keys and throughput, Table API uses simpler conventions derived from Azure Storage Table.

Open the Data Explorer in the Portal. You should see the new table listed, but it's empty - no entities yet. We'll populate it in the next exercise.

## Exercise 2: Using Cosmos Table API as a Log Sink

Now we're going to deploy an application that writes logs to a table. We'll start with legacy Table Storage to demonstrate compatibility, then switch to Cosmos DB without changing any code.

### Creating the Legacy Storage Table

Let's create a Storage Account and Table first to represent our "legacy" data store. We're creating a standard storage account with locally-redundant storage in West Europe, which is cost-effective for development and testing.

Then we create a table within that storage account with the same name - "FulfilmentLogs". This represents the existing infrastructure that many organizations already have in place. Table Storage has been around for years and is widely used for storing large amounts of structured NoSQL data cheaply.

### Creating the App Service

Next, we need somewhere to run our application. We'll use an App Service with a WebJob - this is a background worker process that runs continuously within a web app. First, we create the App Service Plan with the B1 SKU, which is a basic tier that's suitable for development and includes support for WebJobs.

Then we create the Web App itself, specifying the dotnet 6 runtime. Even though this will run a background worker rather than a website, we use the Web App resource type because WebJobs are hosted within Web Apps.

### Configuring the Web App for Background Processing

Web Apps are designed primarily for HTTP applications, but they can also run background processes through the WebJobs feature. Open the Web App in the Portal and check the WebJobs page under Settings - it's empty for now because we haven't deployed anything yet.

Since we're running a background worker that doesn't serve HTTP traffic, we need to enable the "Always On" feature. Without this, the Azure hosting environment might shut down your app after periods of inactivity to save resources. For a background worker that needs to run continuously, we want to keep it alive. We're setting the always-on parameter to true in the web app configuration.

### Configuring the Storage Connection

Now let's get the connection string for our Storage Account. We're querying for just the connection string value and outputting it in TSV format, which makes it easy to use in scripts or copy into other commands.

Next, we set this as an application setting on the web app. Notice the setting name - "Serilog__WriteTo__0__Args__connectionString". This is using the double-underscore convention that .NET configuration uses to represent hierarchical structures. At runtime, this becomes Serilog:WriteTo:0:Args:connectionString in the configuration hierarchy, which is exactly what the Serilog logging framework expects.

### Deploying the Application

WebJob deployment is unique compared to other deployment methods. We need to upload a ZIP file containing the compiled application in a specific folder structure. The Azure CLI deployment source command handles this for us, uploading the ZIP and extracting it to the correct location.

Once deployment completes, check the Portal's WebJobs page. You should see a WebJob entry with status "Running" - this means the background worker has started successfully. The worker is now writing logs to your Storage Table. Open the Storage Account in Storage Browser, navigate to Tables, and you'll see data flowing into the FulfilmentLogs table. Each row represents a log entry with timestamp, severity, and message information.

## Exercise 3: Switching to Cosmos Table API

Here's where it gets exciting. We're going to switch from Table Storage to Cosmos DB Table API without changing a single line of code - just the connection string.

### Getting the Cosmos Connection String

First, we need the connection string from our Cosmos DB account. This query looks a bit complex because the CLI returns multiple connection strings, and we need to filter for specifically the "Primary Table Connection String". The JMESPath query filters the connectionStrings array for the entry where description equals "Primary Table Connection String", then extracts just the connectionString value, outputting it in TSV format.

Here's the key insight - notice that this connection string is in the same format as the Storage Account connection string. It includes an AccountName, AccountKey, and endpoints. This is why client applications don't need any changes to switch from Storage Table to Cosmos Table - they can parse the same connection string format and connect to either service.

### Updating the Configuration

Now we simply update the app setting with the new Cosmos DB connection string. We're using the exact same setting name as before - we're just changing the value to point to Cosmos DB instead of Table Storage.

When you change application configuration, Azure automatically restarts the web app to pick up the new settings. In the Portal's WebJobs page, you might see the status briefly change to "Stopped" and then back to "Running" within a few seconds. This restart is automatic and seamless.

Once the WebJob is running again, your application is now writing logs to Cosmos DB instead of Table Storage - with absolutely zero code changes! This demonstrates the power of the Table API compatibility layer. Any application written for Azure Storage Table can migrate to Cosmos DB by simply changing the connection string.

### Verifying the Switch

Open Data Explorer in the Portal for your Cosmos DB account. Expand the FulfilmentLogs table and you should see new log entries flowing in. Each entity appears as a table row with properties like PartitionKey, RowKey, Timestamp, and the custom fields from your log messages.

Your application has successfully migrated from Table Storage to Cosmos DB, gaining benefits like global distribution, guaranteed low latency, and more sophisticated query capabilities - all without touching your application code.

## Lab Challenge

Now it's your turn to explore the querying capabilities. Use Data Explorer to query the Cosmos DB Table and find just the error logs from the last hour. Think about how this query approach compares to querying the original Table Storage, or to querying Cosmos DB with the SQL API.

Some questions to consider: What query syntax does Table API use? How does it differ from the SQL syntax you'd use with the NoSQL API? What are the performance characteristics of filtering by time ranges in Table Storage versus Cosmos DB?

## Cleanup

When you're done with this lab, it's important to clean up your resources to avoid ongoing charges. The Azure CLI delete command removes the entire resource group and all resources within it - the Cosmos DB account, Storage Account, App Service Plan, and Web App all get deleted together.

The -y flag confirms the deletion without prompting, and --no-wait returns immediately without waiting for the deletion to complete in the background. Deletion can take several minutes, so the no-wait option lets you continue with other work while Azure cleans up the resources.

## Key Takeaways

The Cosmos DB Table API provides backward compatibility with Azure Storage Table, making migration straightforward for existing applications. You get the benefits of Cosmos DB's globally distributed architecture while maintaining your existing code.

The compatibility is achieved through a standardized connection string format that both services understand. This abstraction layer means your application code doesn't need to know whether it's talking to Storage Table or Cosmos DB Table.

WebJobs provide a simple way to run background processes in Azure without needing a full virtual machine or container orchestration. They're perfect for tasks like log processing, scheduled jobs, or continuous background workers.

Configuration as environment variables or app settings allows you to change runtime behavior without redeploying code - a key principle of cloud-native application design.

Understanding these patterns helps you build flexible, maintainable applications that can evolve over time without major rewrites.
