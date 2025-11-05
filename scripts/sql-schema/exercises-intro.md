# Deploying Database Schemas - Exercises Introduction

We've covered how to deploy pre-existing database schemas to Azure SQL Database using Microsoft's data tier application packages - essential for migrating from on-premises SQL Server or deploying packaged applications with their own database structures. Now let's deploy a Bacpac file to Azure.

## What You'll Do

You'll start by **creating a SQL Server and database** using Azure CLI, understanding that the SQL Server logical container has no cost by itself - you only pay for databases within it. You'll set admin credentials for the server that you'll need later for import operations.

Then you'll **upload a Bacpac file to Azure Blob Storage** using a storage account and container. Bacpac files contain both schema and data - a complete backup of database structure and content together. You'll learn that Azure's import service requires the Bacpac to already be in Azure Storage, not uploaded directly from your local machine.

Next, you'll **configure firewall rules** because Azure SQL Server blocks all access by default as a security measure. You'll create two rules: one allowing Azure internal services (using the special 0.0.0.0 IP) and another allowing your local machine's IP for management access.

You'll **import the database** using `az sql db import`, providing SQL Server admin credentials, the Bacpac blob URL, and a Shared Access Signature (SAS) token for authentication. The SAS token grants time-limited read access without exposing your full storage account key. The import process downloads the Bacpac and recreates all tables and data in your Azure SQL database.

Finally, you'll **verify the deployment** using the Azure Portal's Query Editor - a browser-based SQL client built into Azure. You'll query the imported tables (Assets, AssetTypes, Locations) to confirm both schema structure and data were correctly imported. The lab challenge involves adding new data and then exporting a new Bacpac that includes your additions.

The key learning: Bacpac and Dacpac files represent Microsoft's approach to database lifecycle management - Bacpac includes schema and data for migrations and backups, while Dacpac includes only schema for version control and DevOps pipelines.

Let's master database deployment to Azure!
