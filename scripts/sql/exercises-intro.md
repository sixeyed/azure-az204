# Azure SQL - Exercises Introduction

We've covered the multiple SQL Server options in Azure: serverless databases for intermittent usage, managed SQL databases as fully managed database-as-a-service, SQL Managed Instances for near-complete SQL Server compatibility, and SQL Virtual Machines for complete feature parity. Now let's work with Azure SQL databases hands-on.

## What You'll Do

You'll start by **exploring Azure SQL in the Portal** to see the different deployment options: SQL databases, SQL managed instances, and SQL virtual machines representing different management and control levels. You'll understand when to choose serverless databases (for occasional usage with automatic pause/resume) versus SQL Virtual Machines (for complete control with OS-level access).

Then you'll **create a SQL Server with the Azure CLI** using `az sql server create`. You'll learn that the SQL Server is a logical container, not a VM, and the server name must be globally unique because it becomes part of the public DNS as your-server-name.database.windows.net. Important insight: the SQL Server logical server itself has no running cost - you only pay for databases within it.

You'll **create a SQL Database** using `az sql db create` within your SQL Server. The database uses the same authentication configured at the server level - one set of admin credentials for all databases on that server. You'll understand sizing options from Basic tier with 5 DTUs to Business Critical with many vCores.

Next comes **connecting to the database** by retrieving connection strings from the Portal in different formats (ADO.NET, JDBC, PHP, ODBC). You'll encounter the IP-based firewall and learn that Azure SQL Server has default-deny security - you must explicitly allow access by adding your IP address to firewall rules.

You'll **query the database** with full administrator privileges, creating tables, inserting data, and querying results. You'll understand that Azure SQL works with any ORM like Entity Framework or Hibernate using code-first migrations for schema creation.

The lab challenge involves **database recovery** - deleting databases and understanding their independence from the SQL Server container, exploring Azure SQL's automated backups and point-in-time restore capabilities, and observing how resource group deletion cascades to all contained resources.

The key learning: Azure SQL provides multiple service options for different scenarios, requires firewall configuration for security, follows a clear hierarchy (Resource Group > SQL Server > Databases), and offers automatic backups for recovery.

Let's master Azure SQL database management!
