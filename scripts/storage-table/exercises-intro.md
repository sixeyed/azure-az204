# Azure Table Storage - Exercises Introduction

We've covered Azure Table Storage as a simple, scalable NoSQL database service in Azure Storage Accounts with schema flexibility where entities can have different properties - an older part of Azure's storage stack but still encountered in many solutions. Now let's work with Table Storage hands-on.

## What You'll Do

You'll start by **creating a table** in a storage account using `az storage table create`. The mandatory parameters are simple: just table name and storage account name. Important insight: empty tables don't cost anything - you only pay when there's actual data stored, unlike some database services where you pay for provisioned capacity regardless of usage.

Then you'll **add entities with different structures** using the Storage Browser, demonstrating schema flexibility. You'll create entities with varied properties: one with FirstName/LastName/Role, another with similar but different values, a third with completely different structure using FullName and CountryCode instead, and a fourth mixing data types with numeric partition key and no additional properties beyond mandatory keys. This extreme flexibility makes Table Storage useful for evolving data structures.

You'll **query with OData** using the REST API with curl requests. OData is an open protocol providing standardized querying over HTTP. You'll discover that public access isn't enabled by default for security - Azure enforces authentication on all storage operations.

Next comes **using SAS tokens** for authentication with `az storage table generate-sas`. The SAS token provides time-limited access (e.g., 2 hours), read-only permissions following least privilege, and fine-grained control restricted to specific tables rather than entire storage accounts. This granular security is a key feature of SAS tokens.

You'll **work with OData query capabilities** - get specific entities by PartitionKey and RowKey (most efficient pattern targeting single entities directly), request JSON instead of XML using Accept headers, and get cleaner JSON without OData metadata wrapper using `application/json;odata=nometadata`.

Finally, you'll **use Table Storage in applications** by running a .NET app using Serilog that writes log events directly to Azure Table Storage. This demonstrates a real-world use case where Table Storage excels: storing high-volume, semi-structured log data. You'll see clever partition/row key patterns using reverse chronological timestamps so recent logs come first.

The key learning: Table Storage provides schema-less NoSQL storage in Azure with OData querying, SAS token security, and integration with logging frameworks for real-world scenarios.

Let's master Azure Table Storage!
