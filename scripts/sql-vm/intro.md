# SQL Server VMs - Introduction Script

## Opening

Welcome to this lab on SQL Server Virtual Machines in Azure. In this session, we'll explore when and why you might choose SQL Server VMs over managed database options.

## Why SQL Server VMs?

While managed SQL Server databases like Azure SQL Database and SQL Managed Instance should be your preferred choice for most scenarios, they don't support 100% of the features you get with SQL Server in the datacentre. There will be occasions where you need a feature that isn't available in the managed options.

That's where Azure SQL Server VMs come in. The SQL VM service lets you set up the underlying operating system and SQL Server deployment exactly how you need to, giving you complete control and access to all SQL Server features.

## What We'll Cover

In this lab, we'll work through several key topics:

First, we'll explore Azure SQL options in the Portal to understand the different choices available, including SQL Virtual Machines with Linux and Windows variants, different SQL Server versions, and various SKUs.

Next, we'll create a SQL Server VM using the Azure CLI. We'll start by finding the right VM image - SQL Server 2019 Standard on Windows Server 2022 - and create our virtual machine.

Then, we'll register the VM with the SQL Server IaaS extension. This effectively transforms your standard VM into something more like a managed database service, giving you enhanced management capabilities.

We'll configure public access to the database and set up SQL authentication with a username and password.

Finally, we'll demonstrate a real-world use case: creating a custom User-Defined Function that calls .NET code. This is a feature that isn't available with managed database options because you need direct access to the file system and elevated SQL Server permissions.

## Lab Scenario

Throughout this lab, you'll be working with placeholder values. When you see resource names like "labs-sql-vm", locations like "westeurope", or VM names like "sql01", remember to substitute these with appropriate values for your own environment.

For security credentials, we'll use placeholders like "your-strong-password" and "your-dns-name". In a real implementation, you would use secure, unique values that meet Azure's password complexity requirements.

## Prerequisites

Before we begin, make sure you have:
- Azure CLI installed and configured
- Access to an Azure subscription
- Basic familiarity with Azure Resource Groups and Virtual Machines
- Understanding of SQL Server fundamentals

Let's get started with exploring SQL Server VMs in Azure.
