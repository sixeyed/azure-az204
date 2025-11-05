# Azure SQL - Exercises Walkthrough

## Exercise 1: Explore Azure SQL in the Portal

Let's start by opening the Azure Portal and searching for "SQL" to create a new Azure SQL resource.

When you see the Azure SQL deployment page, notice there are different types of services available. We're presented with choices for SQL databases, SQL managed instances, and SQL virtual machines.

**Question to consider**: For a new application with occasional SQL usage, which option would you choose?

The answer is the serverless SQL database option. This allows the database to automatically pause when not in use, and you only pay when it's actively processing queries.

**Another consideration**: Why might you need the Virtual Machine option?

You'd choose SQL on a VM when you need complete control over the SQL Server instance, or when you're migrating applications that require specific SQL Server configurations not available in the PaaS offerings.

### Understanding Database Creation Requirements

Select the SQL databases option and choose to create a Single database.

Notice the required fields - you need:
- A SQL Server instance
- Which needs a resource group
- All before you can create the database

This hierarchy is typical of Azure resources. The database belongs to a SQL Server instance, which belongs in a resource group.

### SQL Server Configuration

When creating a new SQL Server, you'll notice:

**Server naming**: The server name must be globally unique because it becomes part of the public DNS name in the format: your-server-name.database.windows.net

**Authentication options**: The default is SQL authentication. While Windows authentication is preferred in datacenters, SQL authentication is more suitable in the cloud because:
- It doesn't require Active Directory infrastructure
- It works across different network boundaries
- It's simpler to configure for cloud-native applications

We won't complete the creation in the portal - instead, we'll use the Azure CLI for better automation and repeatability.

## Exercise 2: Create a SQL Server with the CLI

First, let's create a resource group for our SQL resources.

```bash
az group create -n labs-sql --tags courselabs=azure -l eastus
```

This creates a resource group named "labs-sql" in the East US region with a tag to identify it as part of our course labs.

### Creating the SQL Server

Now we'll create the SQL Server instance. Remember, you need a globally unique name for the server.

```bash
az sql server create -l eastus -g labs-sql -n YOUR-SERVER-NAME -u sqladmin -p YOUR-PASSWORD
```

Let me break down these parameters:
- `-l eastus` - The location (region) for the server
- `-g labs-sql` - The resource group we just created
- `-n YOUR-SERVER-NAME` - A globally unique name for your server
- `-u sqladmin` - The administrator username
- `-p YOUR-PASSWORD` - The administrator password (must meet complexity requirements)

**Important note about passwords**: Your password must meet the SQL Server password policy - typically at least 8 characters with a mix of uppercase, lowercase, numbers, and special characters.

The server creation takes a few minutes. While it's running, here's an important fact: **The SQL Server instance itself has no running cost**. You only pay for the databases you create within it.

Once created, you can browse to the portal and view your SQL Server properties. Notice the fully qualified domain name is in the format: your-server-name.database.windows.net

## Exercise 3: Create a SQL Database

Now that we have a SQL Server, we can create databases within it.

```bash
az sql db create -g labs-sql -n db01 -s YOUR-SERVER-NAME
```

This command creates a database named "db01" in your SQL Server. Notice we don't need to supply admin credentials for the new database - why not?

The answer is that the database uses the same authentication configured at the SQL Server level. The administrator credentials we set when creating the server apply to all databases on that server.

**Database sizing**: By default, a new database is created with the General Purpose tier, using the standard-series hardware with 2 vCores. However, Azure SQL databases support a wide range of sizes from very small (Basic tier) to very large (Business Critical tier).

The database creation also takes a couple of minutes. You can monitor the progress in the portal.

## Exercise 4: Connect to the Database

Once the database is created, you can find connection strings in the portal. Navigate to your database and look for the "Connection strings" option.

You'll see connection strings for different platforms:
- ADO.NET
- JDBC
- PHP
- ODBC

All of these follow a similar pattern with the server name, database name, and placeholders for credentials.

### Setting Up Firewall Rules

Let's try to connect using a SQL client. You might use:
- Visual Studio
- SQL Server Management Studio
- The SQL Server Extension for VS Code
- A simple client like Sqlectron

When you first attempt to connect using the server credentials, you'll encounter an error like:

"Cannot open server requested by the login. Client with IP address X.X.X.X is not allowed to access the server."

This is because Azure SQL Server has an IP-based firewall. You need to explicitly allow access to clients based on their originating IP address.

**To fix this**:
1. Open the SQL Server instance in the portal (not the database)
2. Navigate to the Networking or Firewall settings
3. Add your current IP address to the allowed rules
4. The portal makes this easy with an "Add your client IP" button

After adding your IP to the firewall rules, try the connection again - it should succeed.

## Exercise 5: Query the Database

Once successfully connected with administrator credentials, you can run both DDL (Data Definition Language) and DML (Data Manipulation Language) statements.

Let's create a simple table:

```sql
CREATE TABLE students (
    id INT IDENTITY,
    email NVARCHAR(150)
)
```

Insert some data:

```sql
INSERT INTO students(email) VALUES ('user@example.com')
```

And query it:

```sql
SELECT * FROM students
```

**Practical application**: You could use an empty Azure SQL database with any application that uses an ORM like Entity Framework in .NET or Hibernate in Java. Simply set the connection string in your application config, and the ORM can automatically create the database schema when the app first runs.

## Lab Exercise: Database Recovery

Your lab challenge is to:

1. Use the CLI to delete the SQL database
2. After the database is gone, check if the SQL Server still exists
3. Try to determine if you can retrieve the data from your deleted database
4. Finally, delete the entire resource group
5. Verify whether the SQL Server still exists

This exercise helps you understand:
- The independence of databases and servers
- Azure's resource hierarchy
- Recovery options for deleted resources
- The impact of resource group deletion

Remember, when you delete a resource group, all resources within it are also deleted.

## Cleanup

When you're done with the lab, clean up all resources:

```bash
az group delete -y -n labs-sql
```

This removes the resource group and all resources within it, ensuring you don't incur ongoing charges.
