# Deploying Database Schemas - Introduction

## Opening

Welcome to this lab on deploying database schemas to Azure SQL Database. In this session, we'll explore how to work with existing database schemas and deploy them to Azure using Microsoft's data tier application packages.

## The Problem

When you're working with Azure SQL Database, you often start with an empty database. That's fine if your application uses an ORM like Entity Framework that can create its own schema automatically. But what if you're working with an existing database? What if you have a legacy application, or a database that was designed and developed outside of your application code?

Many real-world scenarios require you to deploy a pre-existing database schema to Azure. You might be migrating from an on-premises SQL Server, or you might be deploying a packaged application that comes with its own database structure.

## The Solution

Microsoft provides a packaging format specifically for this purpose. You can package your database schema - and optionally the data - into a file, upload it to Azure, and deploy it to an Azure SQL Database instance. This makes it ready for your application to use immediately.

## Key Concepts

There are two main file formats you'll work with:

**Bacpac files** contain both the database schema AND the data. Think of this as a complete backup of your database - structure and content together. You can export a Bacpac from an existing database and import it into a new Azure SQL Database, recreating everything exactly as it was.

**Dacpac files** contain only the database schema - the table definitions, stored procedures, views, and other database objects - but no data. These are useful when you want to deploy just the structure and let your application populate the data.

## What We'll Build

In this lab, we'll take an existing Bacpac file and deploy it to Azure SQL Database. The file contains a simple assets management database with tables for locations, asset types, and assets.

We'll walk through:
- Creating an Azure SQL Server
- Uploading the Bacpac file to Azure Storage
- Importing the schema and data into a new database
- Verifying the deployment by querying the data

By the end of this lab, you'll understand how to migrate existing databases to Azure, which is a critical skill for cloud developers working with legacy systems or packaged applications.

Let's get started.
