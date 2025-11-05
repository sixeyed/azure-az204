# Cosmos DB Table API - Exercise Walkthrough

## Exercise 1: Creating a Cosmos DB Table Database

Let's start by creating our Cosmos DB account with Table API support.

### Creating the Resource Group

First, we'll create a resource group for our lab resources:

```
az group create -n labs-cosmos-table --tags courselabs=azure -l westeurope
```

We're creating a resource group called "labs-cosmos-table" in West Europe.

### Understanding the Creation Command

Now let's look at the command to create our Cosmos DB account. Notice the `--help` flag - it's always good to explore your options:

```
az cosmosdb create --help
```

### Creating the Cosmos DB Account

Here's the actual creation command:

```
az cosmosdb create -g labs-cosmos-table --enable-public-network --kind GlobalDocumentDB --capabilities EnableTable -n <cosmos-db-name>
```

Notice something interesting here - we're using the same "GlobalDocumentDB" kind that we use for the NoSQL API. The key difference is the `--capabilities EnableTable` flag. This additional capability enables the Table API on top of the document database engine.

### Portal Exploration

Once the account is created, open it in the Azure Portal. You'll notice some key differences from other Cosmos DB APIs:
- There are no Collections or Containers - just Account and Tables
- There's an Integrations section where you can add Azure Functions that trigger when data changes

### Creating a Table

Now we'll create our first table called "FulfilmentLogs". Let's check the help first:

```
az cosmosdb table create --help
```

And here's the command:

```
az cosmosdb table create --name FulfilmentLogs -g labs-cosmos-table --account-name <cosmos-db-name>
```

Open the Data Explorer in the Portal. You should see the new table, but it's empty - no entities yet.

## Exercise 2: Using Cosmos Table API as a Log Sink

Now we're going to deploy an application that writes logs to a table. We'll start with legacy Table Storage, then switch to Cosmos.

### Creating the Legacy Storage Table

Let's create a Storage Account and Table first:

```
az storage account create -g labs-cosmos-table --sku Standard_LRS -l westeurope -n <storage-account-name>

az storage table create -n FulfilmentLogs --account-name <storage-account-name>
```

This represents our "legacy" data store that we'll migrate from.

### Creating the App Service

Next, we need somewhere to run our application. We'll use an App Service with a WebJob. First, create the App Service Plan:

```
az appservice plan create -g labs-cosmos-table -n app-plan-01 --sku B1 --number-of-workers 1
```

Then create the Web App:

```
az webapp create -g labs-cosmos-table --plan app-plan-01 --runtime dotnet:6 -n <web-app-name>
```

### Configuring the Web App for Background Processing

Web Apps are designed for HTTP applications, but they can also run background processes. Open the Web App in the Portal and check the WebJobs page - it's empty for now.

Since we're running a background worker, not a website, we need to enable "Always On" so the hosting environment doesn't shut down:

```
az webapp config set --always-on true -g labs-cosmos-table -n <web-app-name>
```

### Configuring the Storage Connection

Now let's get the connection string for our Storage Account:

```
az storage account show-connection-string -g labs-cosmos-table --query connectionString -o tsv -n <storage-account-name>
```

Set it as an application setting:

```
az webapp config appsettings set --settings Serilog__WriteTo__0__Args__connectionString='<storage-connection-string>' -g labs-cosmos-table -n <web-app-name>
```

### Deploying the Application

WebJob deployment is unique - we need to upload a ZIP file with the compiled application:

```
az webapp deployment source config-zip -g labs-cosmos-table --src src/fulfilment-processor/deploy.zip -n <web-app-name>
```

Once deployment completes, check the Portal. You should see a WebJob with status "Running". The background worker is now writing logs to your Storage Table. Open it in Storage Browser and you'll see data flowing in.

## Exercise 3: Switching to Cosmos Table API

Here's where it gets exciting. We're going to switch from Table Storage to Cosmos DB without changing any code - just the connection string.

### Getting the Cosmos Connection String

First, we need the connection string from our Cosmos DB account:

```
az cosmosdb keys list --type connection-strings -g labs-cosmos-table --query "connectionStrings[?description==\`Primary Table Connection String\`].connectionString" -o tsv -n <cosmos-db-name>
```

Notice that this connection string is in the same format as the Storage Account connection string. This is why clients don't need any changes - they can read the connection data and connect to either service.

### Updating the Configuration

Now we simply update the app setting with the new connection string:

```
az webapp config appsettings set --settings Serilog__WriteTo__0__Args__connectionString='<cosmos-connection-string>' -g labs-cosmos-table -n <web-app-name>
```

When you change configuration, the WebJob automatically restarts. In the Portal, you might see the status briefly change to "Stopped" and then back to "Running".

Once it's running again, your application is now writing logs to Cosmos DB instead of Table Storage - with zero code changes!

### Verifying the Switch

Open Data Explorer in the Portal for your Cosmos DB account. Expand the FulfilmentLogs table and you should see data flowing in. Your application has successfully migrated from Table Storage to Cosmos DB.

## Lab Challenge

Now it's your turn. Use Data Explorer to query the Cosmos DB and find just the error logs from the last hour. Think about how this query approach compares to querying the original Table Storage, or to Cosmos DB with the SQL API.

## Cleanup

When you're done, clean up your resources:

```
az group delete -y -n labs-cosmos-table --no-wait
```

This will delete everything we created in this lab.
