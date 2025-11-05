# Azure SQL - AZ-204 Exam Introduction

Great work with Azure SQL! This is essential knowledge for the AZ-204 exam's data storage domain.

## What We'll Cover

**Azure SQL service options** must be understood for the exam. SQL Database (PaaS) is for new cloud-native applications, variable/unpredictable workloads with serverless tier, automatic updates/backups/high availability, and multi-tenant SaaS with elastic pools. SQL Managed Instance is for migrating from on-premises SQL Server, near 100% compatibility, SQL Server Agent/cross-database queries/linked servers, and VNet integration. SQL Virtual Machines are for complete control, OS-level access, minimal-change migrations, and features not available in PaaS. The exam presents scenarios requiring you to choose the appropriate option.

**Service tiers and compute options** appear frequently. Basic tier offers 5 DTU max for small workloads. Standard tier provides up to 3000 DTUs for medium workloads. Premium tier delivers up to 4000 DTUs for high-performance needs. General Purpose tier offers 2-80 vCores with balanced performance. Business Critical tier provides 2-80 vCores with low latency and high availability. Hyperscale tier supports databases up to 100TB. Serverless compute automatically pauses when inactive and bills per second for compute used. The exam tests choosing appropriate tiers.

**Authentication methods** are critical. SQL Authentication uses username and password stored in SQL Server, works across all network boundaries, and is the default for Azure SQL. Azure Active Directory Authentication integrates with Azure AD, supports multi-factor authentication, provides centralized identity management, and can use managed identities from applications - this is the best practice for production. The exam tests understanding of when to use each method.

**Network security with firewall rules** is heavily tested. Azure SQL has default-deny firewall requiring explicit access configuration. Server-level firewall rules apply to all databases on the server and are configured in Portal or CLI. Database-level firewall rules apply to specific databases via T-SQL. Virtual Network rules allow access from specific Azure VNets for network isolation. The exam may present connection failures requiring firewall configuration.

**Resource hierarchy** must be memorized: Resource Group contains SQL Server (logical container, not a VM), which contains multiple Databases. The server name must be globally unique, becomes your-server.database.windows.net. The server has no compute cost by itself. Databases inherit server-level authentication. Deleting a server deletes all its databases. Deleting a resource group deletes everything inside. The exam tests understanding of this hierarchy.

**Connection strings** follow standard formats. ADO.NET format includes server with fully qualified domain name and port 1433, Initial Catalog for database name, User ID and Password for SQL authentication, Encrypt=True for SSL/TLS, and Connection Timeout. Best practice: store in Azure Key Vault (most secure), App Service Application Settings, or Azure App Configuration - never hardcode. The exam may test identifying connection string issues.

**Backup and recovery** is testable. Automatic backups include full backups weekly, differential backups every 12-24 hours, transaction log backups every 5-10 minutes, with default retention of 7 days (extendable to 35 days) and long-term retention up to 10 years. Point-in-time restore can restore to any point within retention period, creates a new database, and can restore deleted databases within retention. The exam tests understanding of recovery capabilities.

We'll cover **CLI commands** (`az sql server create`, `az sql db create`, `az sql server firewall-rule create`), **cost optimization** (serverless for variable workloads, elastic pools for multi-tenant, reserved capacity for predictable workloads), **security best practices** (Azure AD auth, VNet integration, Private Link, Key Vault for credentials), and **common scenarios** about connection failures, choosing the right service, securing access, and optimizing costs.

Master Azure SQL for the AZ-204!
