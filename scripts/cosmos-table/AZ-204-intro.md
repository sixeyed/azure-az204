# Cosmos DB Table API - AZ-204 Exam Introduction

Great work migrating to Cosmos DB Table API! This topic tests your understanding of compatibility layers and migration scenarios.

## What We'll Cover

**When to use Table API** is important. Migration scenarios (existing Table Storage apps), Legacy application support (can't modify code), Simple key-value workloads (don't need SQL API features), Minimal code changes required (just connection string). The exam tests recognizing these scenarios versus when SQL API would be better (complex queries, nested documents, flexible schema).

**Creation pattern requiring both flags** is specific to Table API. Must use `--kind GlobalDocumentDB` (creates Cosmos DB account) AND `--capabilities EnableTable` (enables Table API compatibility). Without EnableTable, you get SQL API by default. The exam may test the correct command syntax for creating Table API accounts.

**Connection string compatibility** enables seamless migration. Table Storage connection strings and Cosmos DB Table API connection strings have identical format. Applications using Azure.Data.Tables or Microsoft.Azure.Cosmos.Table SDKs work with both. Just update the connection string in configuration - zero code changes. The exam tests understanding of this migration path.

**WebJobs for background processing** in App Service appear in integration scenarios. WebJobs run continuously or on schedules within App Service, share the same App Service Plan as web apps, good for log processing, scheduled tasks, message queue processing. The exam tests when to use WebJobs versus Azure Functions (similar but more flexible).

**Configuration as code best practice** separating configuration from code enables zero-downtime changes. Store connection strings in application settings, not in code or config files. Change settings in Portal or via CLI without redeploying code. The exam tests understanding of configuration management patterns.

**Structural differences** between Table API and SQL API need to be understood. Table API: Account → Table (flat structure, no database container). SQL API: Account → Database → Container (hierarchical structure). Table API simpler for basic key-value scenarios, SQL API more powerful for complex data models. The exam tests choosing appropriate API based on requirements.

We'll cover **Table Storage vs Cosmos DB feature comparison**, **pricing model differences**, **partition and row key concepts**, **query patterns**, **migration strategies**, and **common scenarios** about modernizing legacy applications and choosing between Table API and SQL API for new projects.

Master Cosmos DB Table API migration for the AZ-204!
