# Cosmos DB Table API - Exercises Introduction

We've covered Cosmos DB Table API as a modern replacement for Azure Table Storage with zero code changes required. Now let's migrate a legacy application.

## What You'll Do

You'll start by **creating a Cosmos DB account with Table API** - note the specific creation pattern using `--kind GlobalDocumentDB` and `--capabilities EnableTable` flags. This creates a Cosmos account that speaks the Table Storage protocol.

Then you'll **deploy a background worker application** (WebJob) that writes logs to Azure Table Storage. WebJobs are App Service's built-in way to run background tasks. This simulates a legacy application using Table Storage that you want to modernize.

Next comes the migration magic: you'll **retrieve the Cosmos DB Table API connection string** and **switch the application configuration** from Table Storage to Cosmos DB. Here's the key learning - you change ONLY the connection string, no code changes at all! The application doesn't know it's talking to Cosmos DB instead of Table Storage. The APIs are 100% compatible.

You'll **verify data flowing into Cosmos DB Table** using Data Explorer. The tables appear just like they did in Table Storage. Then you'll **practice querying for specific log entries** using the familiar Table Storage query syntax.

The key insight: this migration path lets you move legacy applications to Cosmos DB with zero downtime and zero code changes. Just update the configuration and redeploy. The application gets all of Cosmos DB's benefits (global distribution, guaranteed low latency, enterprise SLA) while maintaining Table Storage compatibility.

Let's migrate a legacy application to Cosmos DB!
