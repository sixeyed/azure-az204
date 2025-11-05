# IaaS Apps - Exercises Introduction

We've covered deploying traditional .NET Framework applications to Azure using IaaS, providing a migration path for legacy workloads. Now let's build a complete IaaS environment.

## What You'll Do

You'll start by **provisioning Azure SQL Database** for your data tier. Then you'll **create a Windows Server 2022 VM** using Azure CLI, selecting the appropriate image and VM size. You'll **connect via Remote Desktop** to Windows Server Core (no GUI, just PowerShell console - the modern Windows Server approach).

Once connected, you'll **verify .NET Framework 4.8 is installed** (it comes with Server 2022), then **install IIS and ASP.NET** using PowerShell. This demonstrates that even without a GUI, you have full control over the server configuration. You'll **deploy an MSI application package** - the traditional installer-based deployment model that many enterprises still use.

Next comes **configuration** - setting the database connection string so your application can connect to Azure SQL. Then you'll implement **security with service endpoints and firewall rules**. Service endpoints provide a secure, private path between your VNet and Azure SQL without going over the public internet. You'll configure VNet rules on the SQL Database to only accept connections from your VM's subnet.

Finally, you'll **configure NSG rules** to allow HTTP traffic from the internet to your VM, making your application publicly accessible. You'll **test via browser** to see your application running, and **verify data storage** by checking records in SQL Database.

The key learning: IaaS gives you complete control but requires managing everything manually - OS updates, security patches, application deployment, monitoring. This is appropriate for legacy apps that can't easily move to PaaS.

Let's deploy a complete IaaS application!
