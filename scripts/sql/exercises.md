# SQL Azure

## Reference

Azure offers multiple services for SQL Server, from serverless options where you only pay when the database is in use, to managed VMs which have complete feature parity with SQL Server in the datacenter. You'll need to know all the options, but typically one will fit for most of your workloads. The Azure SQL documentation covers everything from deployment options to performance tuning and high availability configurations. The command line interface gives you complete control through the az sql server and az sql db commands, which we'll be using extensively in these exercises to create and manage SQL resources.

## Explore Azure SQL in the Portal

Open the Portal and search to create a new Azure SQL resource to understand the different service types available.

**Service Options**: You'll see different types of services including SQL databases for Platform-as-a-Service fully managed databases, SQL managed instances for near-complete SQL Server compatibility with VNet integration, and SQL virtual machines for Infrastructure-as-a-Service with complete control. Which would you choose for a new app which has occasional SQL usage? The serverless SQL database option is perfect because it automatically pauses when not in use and you only pay for the compute you actually consume. Why might you need the Virtual Machine option? You'd choose SQL on a VM when you need complete control over the SQL Server instance for custom configurations, specific server-level settings, or legacy features not available in PaaS offerings.

**Database Creation Hierarchy**: Select the SQL databases option and choose to create a Single database. Look at the required options and notice what other resources you need to create before you get to the database. A SQL database belongs to a SQL Server instance, which belongs in a resource group. You can typically create these dependent resources directly in the portal, which is convenient for exploration.

**SQL Server Configuration**: Follow the link to create a new SQL Server for your database. You need a server name and a location. Can you use any name? No - the server name must be globally unique because it becomes part of the public DNS name in the format your-server-name.database.windows.net. You also need to select the authentication types. Windows authentication is preferred in the datacenter, but the default here is for SQL authentication. Why might that be more suitable in the cloud? SQL authentication doesn't require Active Directory infrastructure, works across all network boundaries including from the internet, and is simpler to configure for cloud-native applications.

We won't go on to create the database in the portal - we'll use the CLI instead for better automation and repeatability.

---

## Create a SQL Server with the CLI

First we need to create a Resource Group where the new SQL resources will live.

**Create the Resource Group**: We're creating the group using az group create with name set to "labs-sql", tags for course tracking, and your preferred location. This creates a container for all the SQL resources we'll create.

**Create the SQL Server**: Now you can create the SQL Server which will be the host for the database. You'll need to find a globally unique name for the server because it gets used as the public DNS name. We're using az sql server create with parameters for location, resource group, server name which must be globally unique, administrator account name, and administrator password which must meet the password policy.

**Password Requirements**: The password must meet SQL Server complexity requirements - typically at least 8 characters with a mix of uppercase, lowercase, numbers, and special characters. Choose something secure but memorable as you'll need it to connect.

**Understanding Costs**: Creating a new SQL Server takes a few minutes while Azure provisions the infrastructure. While it's running, here's an important fact - the SQL Server logical server itself has no running cost. You only pay for the databases you create within it and the compute resources they consume. The logical server is just a management container.

**Verify Creation**: When your SQL Server is created, browse to the portal and find the server properties. You can see that the server name is now your-server-name.database.windows.net, which is the endpoint applications use to connect.

---

## Create a SQL Database

The SQL Server is a container for zero or more databases. When you have a SQL Server you can use the sql db create command to create a new database in the server.

**Create the Database**: We're creating a database called "db01" in your SQL Server using az sql db create with parameters for resource group, database name, and server name. This creates a database within your SQL Server container.

**Why No Credentials?**: This will take a couple of minutes - check the portal to see the status. Notice you don't need to supply admin credentials for the new database because the database uses the same authentication configured at the SQL Server level. The administrator credentials we set when creating the server apply to all databases on that server, simplifying management.

**Default Size**: What is the default size for a new database? By default, a new database is created with the General Purpose tier using standard-series hardware with 2 vCores, though this can vary based on your Azure subscription settings. Azure SQL databases support a wide range of sizes from Basic tier with 5 DTUs for small applications to Business Critical tier with many vCores for demanding workloads.

When the database is created, it's just a standard SQL Server instance which you can connect to from a remote client using standard SQL tools.

---

## Connect to the Database

The portal view for SQL Databases shows connection strings that you can use with various clients.

**Available Clients**: You can use Visual Studio with its built-in SQL Server Object Explorer, SQL Server Management Studio for full database management capabilities, the SQL Server Extension for VS Code which is cross-platform and lightweight, or a simple client like Sqlectron for basic querying.

**Try to Connect**: When you try to connect with the SQL Server credentials, can you access the database? You'll see an error like "Cannot open server requested by the login. Client with IP address X.X.X.X is not allowed to access the server. To enable access, use the Windows Azure Management Portal or run sp_set_firewall_rule on the master database to create a firewall rule for this IP address or address range."

**Understanding the Firewall**: SQL Server has an IP block by default, so you need to explicitly allow access to clients based on the originating IP address. This is a security feature that prevents unauthorized access even if someone obtains valid credentials.

**Add Firewall Rule**: In the portal, open the SQL Server instance - not the database, but the server that contains it - and find the firewall settings. On that page you can easily add your own IP address to the rules using the "Add your client IP" button that automatically detects your current public IP address. Save the changes, then try the connection again. It should succeed now that your IP is allowed.

---

## Query the Database

When you successfully connect, you're using the administrator credentials so you can run DDL and DML statements with full control.

**Create a Table**: We're creating a table called "students" with an id column using INT IDENTITY for auto-increment and an email column using NVARCHAR(150) for variable-length Unicode text.

**Insert Data**: We're inserting into the students table with a sample email value. The id column auto-increments so we don't need to specify it.

**Query Data**: We're selecting all columns from students to verify the data. You'll see the rows with their auto-generated IDs and email addresses.

**Practical Application**: You could use an empty database with any application that uses an ORM like Entity Framework in .NET or Hibernate in Java. Simply set the connection string in your application configuration, and the ORM can automatically create the database schema when the app first runs using code-first migrations. This is a common pattern in cloud-native application development.

---

## Lab

Use the CLI to delete the SQL database and explore what happens to the data and the server.

**The Scenario**: When the database is gone the SQL Server still exists - can you retrieve the data from your deleted database? Look at Azure SQL's automated backup capabilities and point-in-time restore features. Azure maintains backups even for deleted databases for a limited time. Now delete the resource group - does the SQL Server still exist?

**Your Task**: This exercise helps you understand several important concepts including the independence of databases and servers where you can delete databases without affecting the server container, Azure's resource hierarchy where deleting a resource group cascades to all contained resources, recovery options for deleted resources, and the impact of resource group deletion where everything inside it is permanently deleted.

**Hints**: Use az sql db delete to remove the database and check if it still appears in the portal. Use az sql db show to verify its deletion. Look for restore options in the portal or CLI. Finally, use az group delete to remove the entire resource group and verify the SQL Server no longer exists by trying to access it or query for it.

---

## Cleanup

**Delete Azure Resources**: If you didn't finish the lab, you can delete the RG with az group delete using the yes flag and specifying the resource group name. This removes the resource group and all resources within it - the SQL Server, databases, and everything else we created - ensuring you don't incur ongoing charges for resources you're not using.

This cleanup step is important in lab environments to control costs and keep your subscription organized.
