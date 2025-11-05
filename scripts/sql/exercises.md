# Azure SQL - Exercises Walkthrough

## Exercise 1: Explore Azure SQL in the Portal

Let's start by opening the Azure Portal and searching for "SQL" to create a new Azure SQL resource.

When you see the Azure SQL deployment page, notice there are different types of services available. We're presented with choices for SQL databases, SQL managed instances, and SQL virtual machines. These represent different levels of management and control - from fully managed Platform-as-a-Service databases to Infrastructure-as-a-Service virtual machines.

**Question to consider**: For a new application with occasional SQL usage, which option would you choose?

The answer is the serverless SQL database option. This allows the database to automatically pause when not in use, and you only pay when it's actively processing queries. This is perfect for dev/test scenarios or applications with intermittent usage patterns.

**Another consideration**: Why might you need the Virtual Machine option?

You'd choose SQL on a VM when you need complete control over the SQL Server instance - things like custom configurations, specific server-level settings, or legacy features not available in PaaS offerings. You might also need it when you're migrating applications that require specific SQL Server configurations not available in the managed database services, like CLR assemblies or linked servers to non-Azure systems.

### Understanding Database Creation Requirements

Select the SQL databases option and choose to create a Single database to see what's involved.

Notice the required fields - you need a SQL Server instance, which needs a resource group, all before you can create the database. This hierarchy is typical of Azure resources - the database belongs to a SQL Server logical server, which belongs in a resource group. Understanding this hierarchy helps you organize and manage your resources effectively.

### SQL Server Configuration

When creating a new SQL Server, you'll notice several important configuration choices.

**Server naming**: The server name must be globally unique because it becomes part of the public DNS name in the format: your-server-name.database.windows.net. This endpoint is how your applications connect to the database, so choose a name that's meaningful and follows your organization's naming conventions.

**Authentication options**: The default is SQL authentication with username and password. While Windows authentication is preferred in on-premises datacenters, SQL authentication is more suitable in the cloud for several reasons. It doesn't require Active Directory infrastructure or domain joining, it works across different network boundaries including from the internet, and it's simpler to configure for cloud-native applications that don't have Windows identities.

We won't complete the creation in the portal - instead, we'll use the Azure CLI for better automation and repeatability. The CLI approach lets us script the entire deployment and reproduce it consistently.

## Exercise 2: Create a SQL Server with the CLI

First, let's create a resource group for our SQL resources to keep everything organized.

We're using az group create with -n set to "labs-sql", adding --tags courselabs=azure for tracking purposes, and -l eastus for the location. This creates a resource group named "labs-sql" in the East US region with a tag to identify it as part of our course labs.

### Creating the SQL Server

Now we'll create the SQL Server instance. Remember, you need a globally unique name for the server since it becomes part of the public DNS.

We're using az sql server create with -l eastus for the location, -g labs-sql for the resource group we just created, -n for your unique server name, -u sqladmin for the administrator username, and -p for your administrator password.

Let me break down these parameters and their importance. The -l parameter sets the Azure region where your server runs physically - choose a region close to your users for lower latency. The -g parameter specifies which resource group contains this server for organization and access control. The -n parameter must be globally unique since it becomes your-server-name.database.windows.net. The -u parameter sets the admin username used to manage the server and databases. The -p parameter sets the admin password which must meet complexity requirements.

**Important note about passwords**: Your password must meet the SQL Server password policy - typically at least 8 characters with a mix of uppercase, lowercase, numbers, and special characters. Choose something secure but memorable, as you'll need it to connect.

The server creation takes a few minutes as Azure provisions the infrastructure. While it's running, here's an important fact: **The SQL Server logical server itself has no running cost**. You only pay for the databases you create within it and the compute resources they consume. The logical server is just a management container.

Once created, you can browse to the portal and view your SQL Server properties. Notice the fully qualified domain name is in the format: your-server-name.database.windows.net. This is the endpoint applications use to connect.

## Exercise 3: Create a SQL Database

Now that we have a SQL Server, we can create databases within it. The server can host multiple databases, each isolated from the others.

We're using az sql db create with -g labs-sql for the resource group, -n db01 as the database name, and -s with your server name to specify which server should host this database.

This command creates a database named "db01" in your SQL Server. Notice we don't need to supply admin credentials for the new database - why not? The answer is that the database uses the same authentication configured at the SQL Server level. The administrator credentials we set when creating the server apply to all databases on that server. This simplifies management - one set of admin credentials for the entire logical server.

**Database sizing**: By default, a new database is created with the General Purpose tier, using the standard-series hardware with 2 vCores. However, Azure SQL databases support a wide range of sizes from very small - Basic tier with 5 DTUs suitable for small applications - to very large Business Critical tier with many vCores for demanding workloads. You can also use serverless compute which automatically scales and pauses based on activity.

The database creation also takes a couple of minutes as Azure provisions the compute and storage. You can monitor the progress in the portal by navigating to your SQL Server resource and viewing the list of databases.

## Exercise 4: Connect to the Database

Once the database is created, you can find connection strings in the portal. Navigate to your database resource and look for the "Connection strings" option in the left menu.

You'll see connection strings for different platforms including ADO.NET for .NET applications, JDBC for Java, PHP for PHP applications, and ODBC for other languages and tools. All of these follow a similar pattern with the server name, database name, and placeholders for credentials that you need to fill in.

### Setting Up Firewall Rules

Let's try to connect using a SQL client. You might use Visual Studio with its built-in SQL Server Object Explorer, SQL Server Management Studio for full database management capabilities, the SQL Server Extension for VS Code which is cross-platform and lightweight, or a simple client like Sqlectron for basic querying.

When you first attempt to connect using the server credentials, you'll encounter an error message like: "Cannot open server requested by the login. Client with IP address X.X.X.X is not allowed to access the server." This is a security error, not an authentication error.

This is because Azure SQL Server has an IP-based firewall by default. You need to explicitly allow access to clients based on their originating IP address. This prevents unauthorized access even if someone obtains valid credentials.

**To fix this**, open the SQL Server instance in the portal - not the database, but the server that contains it. Navigate to the Networking or Firewall settings blade in the left menu. Add your current IP address to the allowed rules. The portal makes this easy with an "Add your client IP" button that automatically detects and adds your current public IP address. Click Save to apply the changes.

After adding your IP to the firewall rules, try the connection again using your SQL client - it should succeed. You'll be connected to the database and can start running queries.

## Exercise 5: Query the Database

Once successfully connected with administrator credentials, you can run both DDL (Data Definition Language) and DML (Data Manipulation Language) statements. You have full control over the database structure and content.

Let's create a simple table to demonstrate. We're creating a table called students with an id column using INT IDENTITY which auto-increments, and an email column using NVARCHAR(150) for variable-length Unicode text up to 150 characters.

Insert some data to populate the table. We're inserting into the students table with the email column, providing a value like 'user@example.com'. The id column auto-increments so we don't need to specify it.

And query it to verify the data is there. We're selecting all columns from students using SELECT star. You'll see the rows we inserted with their auto-generated IDs and email addresses.

**Practical application**: You could use an empty Azure SQL database with any application that uses an ORM like Entity Framework in .NET or Hibernate in Java. Simply set the connection string in your application configuration file, and the ORM can automatically create the database schema when the app first runs using code-first migrations. This is a common pattern in cloud-native application development.

## Lab Exercise: Database Recovery

Your lab challenge is to explore database lifecycle management and understand the relationship between databases and servers.

1. Use the CLI to delete the SQL database using az sql db delete. Watch what happens in the portal.
2. After the database is gone, check if the SQL Server still exists by viewing it in the portal or using az sql server show.
3. Try to determine if you can retrieve the data from your deleted database. Hint: Look at Azure SQL's automated backup capabilities and point-in-time restore features. Can you restore a deleted database?
4. Finally, delete the entire resource group using az group delete.
5. Verify whether the SQL Server still exists by trying to access it or query for it.

This exercise helps you understand several important concepts. The independence of databases and servers - you can delete databases without affecting the server container. Azure's resource hierarchy - deleting a resource group cascades to all contained resources. Recovery options for deleted resources - Azure SQL maintains backups even for deleted databases for a limited time. And the impact of resource group deletion - when you delete a resource group, everything inside it is permanently deleted.

Remember, when you delete a resource group, all resources within it are also deleted - the SQL Server, all databases, and any other resources. This is why resource groups should be thoughtfully organized.

## Cleanup

When you're done with the lab, clean up all resources to avoid ongoing charges.

We're using az group delete with -y to confirm without prompting and -n labs-sql to specify the resource group name. This removes the resource group and all resources within it - the SQL Server, databases, and anything else we created - ensuring you don't incur ongoing charges for resources you're not using.

This cleanup step is important in lab environments to control costs and keep your subscription organized.
