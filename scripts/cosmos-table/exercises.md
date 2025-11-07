# Cosmos DB - Table API

## Reference

The Cosmos DB Table API is a straight replacement for Azure Table Storage. It offers an easy migration path for older apps built with Table Storage. You can use Cosmos Table API without changing those apps, and move to the modern storage option with the scale and capabilities of Cosmos. The underlying Cosmos DB storage engine is the same whichever API you choose, so the main features of the service are consistent across all APIs. The choice is about how you want applications to connect and what compatibility you need with existing systems.

## Create a Cosmos DB Table database

**Explore Portal Options**: We're creating a new resource in the Portal. Search for "cosmos" and create a new CosmosDB, choosing the Table API. Notice that the options are the same as the SQL API - the underlying database engine is the document DB for both. This tells us that Table API is built on top of Cosmos DB's distributed document database.

**Create Resource Group**: We're creating a resource group for our lab resources in your preferred region with the courselabs=azure tag to track resources created for this course.

**Check Available Options**: Before creating the account, let's explore the available options using the help flag. You'll see all the parameters we can use, including options for consistency levels, geo-replication, network configuration, and more.

**Create Cosmos DB Account**: We're creating the Cosmos DB account with an interesting parameter combination. We're using the same GlobalDocumentDB kind that we use for the NoSQL API, but the key difference is the capabilities parameter where we specify EnableTable. This additional capability flag tells Azure to enable the Table API compatibility layer on top of the document database engine.

**Understand the Architecture**: This architecture is elegant - Microsoft has built multiple API surfaces on top of a single underlying storage engine, giving you flexibility in how you access your data while maintaining consistency and performance.

**Explore Portal Differences**: Once the account is created, open it in the Azure Portal. You'll notice some key differences from other Cosmos DB APIs. There are no Collections or Containers in the menu - the Table API just has one level in the structure: Account followed by Tables. There's also an Integrations section where you can add an Azure Function which will be triggered when data changes.

**Create Table**: We're creating a database called FulfilmentLogs using the Table API. Before running the command, check the help to see what options are available. Notice how straightforward the creation command is - we just specify the table name, resource group, and account name. Unlike the SQL API where you need to think about partition keys and throughput, Table API uses simpler conventions derived from Azure Storage Table.

**Verify in Portal**: Open Data Explorer in the Portal for your CosmosDB. You'll see the new table listed, but expand it and there are no entities yet. We'll populate it in the next exercise.

---

## Using Cosmos Table API as a log sink

**Understand the Application**: We're going to deploy an application that writes logs to a table. We'll start with legacy Table Storage to demonstrate compatibility, then switch to Cosmos DB without changing any code. The app's logging configuration has the Storage Account connection string as a placeholder - we'll set the real value as an application setting in Azure.

**Create Legacy Storage**: Let's create a Storage Account and Table first to represent our "legacy" data store. We're creating a standard storage account with locally-redundant storage, which is cost-effective for development and testing. Then we create a table within that storage account with the same name - FulfilmentLogs. This represents the existing infrastructure that many organizations already have in place. Table Storage has been around for years and is widely used for storing large amounts of structured NoSQL data cheaply.

**Create App Service Plan**: Next, we need somewhere to run our application. We'll use an App Service with a WebJob - this is a background worker process that runs continuously within a web app. We're creating the App Service Plan with the B1 SKU, which is a basic tier that's suitable for development and includes support for WebJobs.

**Create Web App**: We're creating the Web App itself, specifying the dotnet 6 runtime. Even though this will run a background worker rather than a website, we use the Web App resource type because WebJobs are hosted within Web Apps.

**Configure Always On**: Web Apps are designed primarily for HTTP applications, but they can also run background processes through the WebJobs feature. Open the Web App in the Portal and check the WebJobs page - it's empty for now. Since we're running a background worker that doesn't serve HTTP traffic, we need to enable the Always On feature so the Azure hosting environment doesn't shut down after periods of inactivity.

**Configure Connection String**: Now let's get the connection string for our Storage Account and set it as an application setting on the web app. Notice the setting name uses the double-underscore convention that .NET configuration uses to represent hierarchical structures. At runtime, this becomes the proper hierarchical path that the Serilog logging framework expects.

**Deploy the Application**: WebJob deployment is unique compared to other deployment methods. We need to upload a ZIP file containing the compiled application in a specific folder structure. The Azure CLI deployment source command handles this, uploading the ZIP and extracting it to the correct location.

**Verify Deployment**: Once deployment completes, check the Portal's WebJobs page. You should see a WebJob entry with status Running - this means the background worker has started successfully. The worker is now writing logs to your Storage Table. Open the Storage Account in Storage Browser, navigate to Tables, and you should see data flowing into the FulfilmentLogs table.

---

## Switching to Cosmos Table API as the log sink

**The Key Insight**: We're going to switch from Table Storage to Cosmos DB Table API without changing a single line of code - just the connection string. The app is still running and generating logs continuously.

**Get Cosmos Connection String**: We need the connection string from our Cosmos DB account. We're querying for specifically the Primary Table Connection String using a filter. Notice that this connection string is in the same format as the Storage Account connection string - it includes an AccountName, AccountKey, and endpoints. This is why client applications don't need any changes to switch from Storage Table to Cosmos Table.

**Update Configuration**: Now we simply update the app setting with the new Cosmos DB connection string. We're using the exact same setting name as before - we're just changing the value to point to Cosmos DB instead of Table Storage.

**Automatic Restart**: When you change application configuration, Azure automatically restarts the web app to pick up the new settings. In the Portal's WebJobs page, you might see the status briefly change to Stopped and then back to Running within a few seconds.

**Verify the Switch**: Once the WebJob is running again, your application is now writing logs to Cosmos DB instead of Table Storage - with absolutely zero code changes. Open Data Explorer in the Portal for your Cosmos DB account and you should see new log entries flowing in.

**Understand the Benefits**: Your application has successfully migrated from Table Storage to Cosmos DB, gaining benefits like global distribution, guaranteed low latency, and more sophisticated query capabilities - all without touching your application code.

---

## Lab

**The Challenge**: Query the Cosmos DB Table using Data Explorer to find just the error logs from the last hour. Think about how this query approach compares to querying the original Table Storage, or to querying Cosmos DB with the SQL API.

**Consider the Differences**: What query syntax does Table API use? How does it differ from the SQL syntax you'd use with the NoSQL API? What are the performance characteristics of filtering by time ranges in Table Storage versus Cosmos DB?

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up resource groups.

This cleanup is important to avoid unnecessary charges on your Azure subscription.
