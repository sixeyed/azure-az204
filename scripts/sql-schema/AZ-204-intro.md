# Deploying Database Schemas - AZ-204 Exam Introduction

Great work with database deployment! This topic supports several AZ-204 exam objectives across storage, security, and Azure services domains.

## What We'll Cover

**Data tier applications** must be understood for the exam. Bacpac files include schema and data - use these for backups, migrations, and creating complete database copies. Dacpac files include only schema - use these for version control and deploying schema changes in DevOps pipelines. You can import from a Bacpac to create a new database. You can export to a Bacpac to backup an existing database. The exam tests understanding of when to use each file type.

**Azure Blob Storage for database operations** is frequently tested. Shared Access Signatures (SAS) provide time-limited access to storage resources with specific permissions and duration. SAS tokens are a security best practice because they provide granular access without exposing storage account keys. The structure of blob URLs includes storage account name forming part of the public address. The exam may test understanding of storage access patterns for database import/export operations.

**SQL Server firewall rules** demonstrate defense-in-depth security. Default deny blocks all access requiring explicit allow configuration. Server-level rules apply to all databases. The special IP address 0.0.0.0 allows Azure services internal access. IP-based rules restrict access to specific IP ranges for client applications. Virtual network rules provide better security than IP-based rules in production. The exam tests understanding of firewall configuration for database access scenarios.

**Azure SQL Database infrastructure** needs to be understood. Resource hierarchy: Resource Group contains SQL Server (logical container, not a VM) which contains multiple databases. Server name must be globally unique becoming your-server.database.windows.net. The server has no compute cost - only databases incur charges. Databases inherit server-level authentication. Deleting a server deletes all databases. The exam tests understanding of this resource organization.

**Migration scenarios** appear frequently. Migrate on-premises SQL Server database to Azure SQL Database using Bacpac import. Clone production database to create test environment by exporting and importing. Move database between Azure regions for disaster recovery or data residency. Restore database from backup using Bacpac files. Other options include Database Migration Service for live migrations, transactional replication for continuous sync, and geo-replication for disaster recovery. The exam tests choosing appropriate migration approach for given requirements.

We'll cover **CLI commands** (`az sql server create`, `az sql db create`, `az sql db import`, `az sql db export`, `az storage blob upload`, `az storage blob generate-sas`), **security best practices** (strong passwords, restrictive firewall rules, SAS tokens instead of storage account keys), **monitoring import/export operations** (checking Import/Export history in Portal), and **common scenarios** about database lifecycle management, migration planning, and troubleshooting connection failures.

Master database deployment for the AZ-204!
