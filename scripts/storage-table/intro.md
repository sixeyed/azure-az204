# Azure Table Storage - Introduction

## Welcome

Welcome to this module on Azure Table Storage. In this session, we'll explore one of Azure's NoSQL storage solutions and understand when and how to use it in your applications.

## What is Azure Table Storage?

Azure Table Storage is a simple, scalable NoSQL database service that you can host in an Azure Storage Account. Unlike traditional relational databases, Table Storage takes a NoSQL approach, which means you'll need to use dedicated libraries in your code to read and write data.

While Table Storage is an older part of the Azure storage stack, having been around before alternatives like MongoDB, you'll still encounter it in many early Azure solutions. It's important to note that Azure Cosmos DB is generally a better option for new projects, but it offers compatibility with Table Storage, providing a clear migration path when needed.

## Key Concepts

Let's understand the core terminology that Table Storage uses, which differs from traditional SQL databases:

First, we have **entities**. Think of entities as your data items, similar to rows in a SQL database or documents in MongoDB.

Next is the **partition key**. This is part of the entity's unique identifier. It's a grouping mechanism that Azure uses to determine where the data is physically stored, which affects performance and scalability.

Finally, there's the **row key**. This is the unique part of the entity's identifier. Together, the partition key and row key form a composite primary key that uniquely identifies each entity.

## Flexibility and Schema Design

One of Table Storage's interesting characteristics is its schema flexibility. Unlike SQL databases with rigid schemas, Table Storage entities can have different properties. You can have:

- Entities with different properties within the same table
- Partition keys and row keys in different formats - you can mix strings and integers
- Even empty entities with no properties beyond the keys

This flexibility can be powerful, but it also requires careful design consideration.

## When to Use Table Storage

Table Storage is ideal for scenarios where you need:

- Simple, fast access to large amounts of structured data
- A cost-effective storage solution for semi-structured data
- High availability and durability without complex setup
- Integration with existing Azure services and workflows

## Module Overview

In this module, we'll work through practical examples of:

- Creating and configuring Table Storage in Azure
- Understanding how data is stored and accessed
- Querying tables using OData REST APIs
- Using Table Storage as a log sink in .NET applications
- Best practices for partition and row key design

Let's get started with creating our first table.
