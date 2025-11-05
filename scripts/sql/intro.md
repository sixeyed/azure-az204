# Azure SQL - Introduction

## Overview

Welcome to this module on Azure SQL. In this session, we'll explore the various SQL Server options available in Azure and learn how to work with them using both the Azure Portal and the Azure CLI.

## What is Azure SQL?

Azure offers multiple services for SQL Server, providing flexibility to match your workload requirements:

- **Serverless options** - Where you only pay when the database is in use, perfect for applications with intermittent usage patterns
- **Managed SQL Databases** - Fully managed database as a service with automatic updates and backups
- **SQL Managed Instances** - Near 100% compatibility with on-premises SQL Server
- **SQL Virtual Machines** - Complete feature parity with SQL Server in your datacenter

## Which Option to Choose?

Understanding when to use each option is crucial for the AZ-204 exam:

**For a new app with occasional SQL usage**, you'd choose a serverless SQL Database. This option automatically pauses when not in use and resumes on demand, making it cost-effective for applications with unpredictable or intermittent usage patterns.

**The Virtual Machine option** is necessary when you need:
- Complete control over the SQL Server instance
- Features that aren't available in PaaS offerings
- To migrate legacy applications that require specific SQL Server configurations
- Custom SQL Server agent jobs or specific server-level settings

## Understanding the Azure SQL Hierarchy

When working with Azure SQL, it's important to understand the resource hierarchy:

1. **Resource Group** - The container for all your Azure resources
2. **SQL Server** - The logical server that hosts your databases
3. **SQL Database** - The actual database where your data lives

The SQL Server instance itself has no cost - you only pay for the databases you create within it. This is an important distinction from on-premises SQL Server.

## Key Concepts for This Lab

In this lab, we'll be working with:

- Creating a SQL Server instance with globally unique naming
- Understanding authentication options in the cloud
- Creating and configuring SQL databases
- Managing firewall rules for secure access
- Connecting to and querying Azure SQL databases

Let's get started by exploring the Azure Portal to see these options in action.
