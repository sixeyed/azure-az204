# Azure Table Storage - Hands-On Exercises

## Exercise 1: Creating a Table

Let's start by creating our Azure resources. We'll need a Resource Group and a Storage Account.

First, we'll create a resource group. I'm running the command: `az group create` with the name "labs-storage-table", adding a tag for "courselabs=azure", and placing it in the West Europe location.

Now we'll create a Storage Account within this resource group. I'm using the command `az storage account create`, specifying the resource group we just created, setting the SKU to Standard_LRS for locally redundant storage, the same West Europe location, and a unique storage account name.

Now comes the interesting part - creating a table. We'll use the `storage table create` command. The mandatory parameters are simple: just the table name and the storage account name. I'm creating a table called "students".

The output confirms the table has been created. It's worth noting that empty tables don't cost anything - you only pay when there's actual data stored in the table.

Let's take a look in the Azure Portal. I'm navigating to the Storage Account and opening the Tables view. As expected, there's not much to see with an empty table. Let's switch to the Storage Browser instead, which provides a better interface for working with table data.

## Exercise 2: Adding Entities

Now let's add some entities to understand the schema flexibility. I'll use the Storage Browser to add several entities with different structures.

For the first entity, I'm setting:
- Partition Key: "org1"
- Row Key: "1023"
- Properties: FirstName, LastName, and Role

For the second entity, same partition key "org1" but different Row Key "1040", with similar properties but different values.

Now watch this - for the third entity, I'm using a completely different structure:
- Partition Key: "org2"
- Row Key: "aed1895"
- Instead of separate name fields, I'm using a single FullName property, plus a CountryCode

And for the fourth entity, I'm mixing data types:
- Partition Key: "23124" - a numeric string
- Row Key: "stonemane" - a text string
- No additional properties at all

This demonstrates the schema flexibility I mentioned earlier. All these different entity structures coexist happily in the same table.

## Exercise 3: Querying with OData

Table Storage provides an OData REST API, which means we can query our data using simple HTTP requests with curl.

First, let's get the table storage endpoint URL. I'm running `az storage account show` to query the primary endpoints, specifically the table endpoint.

The URL format is straightforward - we append the table name to the endpoint, with an empty query in parentheses to retrieve all entities.

Let me try this curl command now... and as you can see, we get a "Resource not found" error. This is because even though OData is supported, public access isn't enabled by default for security reasons.

## Exercise 4: Using SAS Tokens

We need to generate a Shared Access Signature token to authenticate our requests. I'll use the `az storage table generate-sas` command.

For the expiry date, I'm setting it to 2 hours from now. The permissions are set to "r" for read-only access. Notice that I can create a very fine-grained token that's restricted to just this specific table.

Now with the SAS token, let's try that curl command again. The URL now includes the SAS token as query parameters. And there's our data!

Let me try some more specific queries. To get a specific entity, I specify both the PartitionKey and RowKey in the query.

By default, the response is in XML format. But we can request JSON by adding an Accept header. And if we want even cleaner JSON without the OData metadata, we can specify that in the Accept header as well.

Notice in the response data that there's an automatically generated Timestamp field that shows when each entity was created or last updated.

## Exercise 5: Using Table Storage in Applications

Now let's see Table Storage in action within an application. We're going to run a .NET application that uses Serilog, a popular logging library that can write directly to Table Storage.

First, we need to create a table for the logs. I'm creating a new table called "FulfilmentLogs" using the same storage account.

Next, we need the connection string so our application can authenticate. I'm running `az storage account show-connection-string` to get this.

The connection string format includes multiple components: the protocol, account name, account key, and endpoints for all the different storage services - blob, file, queue, and table.

Now I need to update the application configuration. In the appsettings.json file, I'm replacing the placeholder with our actual connection string.

Let's run the application using `dotnet run`. Notice that we don't see any console output - that's because all the logs are being written to Table Storage in the cloud.

I'll let this run for a few minutes to generate some log entries... and now I'll stop it.

Back in the Azure Portal, in the Storage Browser for the FulfilmentLogs table, you can see numerous log entries. Take a look at how the PartitionKey and RowKey are constructed - they're using a combination of timestamp and log level, which is a common pattern for time-series data in Table Storage.

## Exercise 6: Lab Challenge

Here's your challenge: Can you query the fulfilment log entries to find just the error events? You can approach this either through the Storage Browser interface or by using OData queries.

Once you find the errors, what do you think needs to be done to fix the underlying issue?

Take some time to explore this on your own, and when you're ready, check out the hints or solution for guidance.

## Cleanup

When you're finished experimenting, remember to clean up your resources to avoid unnecessary charges. Simply run `az group delete` with the resource group name, using the -y flag to skip confirmation and --no-wait to run it asynchronously.

That concludes our hands-on exercises with Azure Table Storage.
