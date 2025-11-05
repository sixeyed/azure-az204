# SQL Server VMs - AZ-204 Exam Introduction

Excellent work with SQL VMs! This topic is important for the AZ-204 exam's compute and decision-making domains.

## What We'll Cover

**Service selection criteria** is critical for the exam. Use SQL Server VMs when you need features not available in PaaS options (Azure SQL Database or SQL Managed Instance), require full control over SQL Server configuration, need to upload files to the file system for database operations, have specific OS-level requirements, or are migrating legacy applications requiring specific SQL Server features. Don't use SQL Server VMs when PaaS options meet requirements, you want Azure to handle patching/backups/high availability, you want to minimize operational overhead, or you don't need OS-level access. The exam presents scenarios requiring you to choose the appropriate option.

**IaaS implementation concepts** appear throughout the exam. Creating and configuring virtual machines using Azure CLI with `az vm create`. Understanding VM images, SKUs, and sizing options - the URN format uniquely identifies images. Managing VM networking with NSGs controlling traffic via rules. Working with VM extensions to enhance functionality - the SQL IaaS Agent Extension transforms basic VMs into specialized services. The exam tests understanding of IaaS fundamentals through SQL VM scenarios.

**SQL Server IaaS Agent Extension** is exam-testable. The extension provides Azure-integrated management capabilities, installs automatically when registered with `az sql vm create`. Key parameters include license-type (PAYG for Pay As You Go includes SQL Server costs, or BYOL for Bring Your Own License), sql-mgmt-type (Full for all management capabilities), connectivity-type (PUBLIC for internet access or PRIVATE for VNet only), and sql-auth-update for creating SQL authentication logins. The exam tests understanding of when and how to use the extension.

**Network security** must be understood. NSG rules control traffic with priority (lower numbers have higher priority), source (Internet, specific IPs, or VNets), destination ports (1433 for SQL Server, 3389 for RDP), and access (Allow or Deny). Port 1433 is default for SQL Server database connections. Port 3389 is for RDP to Windows desktop. The exam tests understanding of securing VM access appropriately.

**Authentication approaches** offer flexibility. Windows authentication is default for SQL Server on VMs using domain credentials or local machine accounts. SQL authentication uses username and password stored in SQL Server, works across all network boundaries, and is configured through the IaaS extension or manually. The exam tests understanding of authentication methods and security implications.

**SQL Server features requiring VMs** include: CLR integration for .NET code in SQL Server (requires file system access and elevated permissions), server-level configuration options not available in PaaS, SQL Server Agent with custom jobs, linked servers to non-Azure systems, and custom assemblies or extended stored procedures. The exam tests recognizing scenarios requiring these features.

We'll cover **CLI commands** (`az vm create`, `az vm image list`, `az sql vm create`, `az network nsg rule create`), **cost management** (VM sizing affects cost, SQL Server licensing models, storage costs, network egress), **comparison with PaaS options** (SQL Database for fully managed common scenarios, SQL Managed Instance for better on-premises compatibility, SQL VMs for complete control), and **common scenarios** about choosing the right service, migrating applications, and implementing custom functionality.

Master SQL Server VMs for the AZ-204!
