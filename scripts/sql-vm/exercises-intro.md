# SQL Server VMs - Exercises Introduction

We've covered SQL Server Virtual Machines as the IaaS option when managed database services don't support features you need - providing complete control and access to all SQL Server capabilities. Now let's deploy and configure a SQL VM with custom functionality.

## What You'll Do

You'll start by **exploring Azure SQL options in the Portal** to understand the different choices: SQL Virtual Machines with Linux and Windows variants, different SQL Server versions (2019, 2017), and various SKUs (Standard, Enterprise, Web, Express). This helps you understand when VMs are appropriate versus managed options.

Then you'll **find the right SQL Server VM image** using Azure CLI commands - `az vm image list-offers` to see SQL Server offerings, `az vm image list-skus` to find specific editions, and `az vm image list` to get the URN for a specific version. You'll learn the URN format that uniquely identifies VM images like `MicrosoftSQLServer:sql2019-ws2022:standard:version`.

You'll **create the SQL Server VM** using standard `az vm create` command, specifying the image URN, VM size (Standard_D2_v3 for 2 vCPUs and 8GB RAM), admin credentials, and a unique DNS name for remote access. The VM is created with SQL Server pre-installed but appears as a standard VM initially.

Next comes **registering the VM with the SQL Server IaaS extension** using `az sql vm create`. This transforms your VM from generic infrastructure into a managed SQL Server resource, providing Azure-integrated management capabilities. You'll configure public connectivity, enable SQL authentication in addition to Windows authentication, and set up automatic firewall rules for SQL Server traffic.

You'll **enable RDP access** by adding a Network Security Group rule for port 3389, allowing you to connect to the Windows desktop. Once connected, you'll **create a custom User-Defined Function** that calls .NET code - a feature unavailable in managed services because it requires file system access and elevated SQL Server permissions. You'll enable CLR integration, upload a DLL, and register it as a SQL function.

The lab challenge involves creating new SQL Server logins with custom credentials, demonstrating another advantage of full control - you own authentication without using standard Azure mechanisms.

The key learning: SQL VMs provide complete control and all SQL Server features at the cost of managing infrastructure yourself. Choose VMs when you need features not available in PaaS options like CLR integration, specific server-level settings, or OS-level access.

Let's explore SQL Server VMs!
