We've covered deploying traditional .NET Framework applications to Azure using IaaS, providing a migration path for legacy workloads that can't easily move to Platform-as-a-Service. Now let's build a complete IaaS environment from scratch.

Working through creating a resource group gives you a place to organize all your infrastructure components with tagging for cost tracking. You'll use variables in your shell session to make commands more readable and to avoid repeating values like region names and resource names throughout the deployment.

When you create a SQL Database, you're setting up the data tier for your application. You'll create both a SQL Server logical server and a database within it, starting with basic configuration that you'll secure later. The database can be provisioned asynchronously while you work on the VM, showing how you can parallelize infrastructure setup to save time.

Creating a Windows Server VM involves selecting the right image SKU for your needs. You'll use the 2022 Datacenter Core generation 2 image which is the modern Windows Server experience without the full GUI, just a PowerShell console. When you connect via Remote Desktop, you'll be dropped into this terminal-based environment which might seem unfamiliar but actually provides full server capabilities through command-line management.

The deploy the app section walks you through the manual deployment process that simulates a traditional enterprise workflow. You'll verify .NET Framework 4.8 is installed since your application depends on it, then install IIS and ASP.NET using PowerShell with Install-WindowsFeature commands. You'll download and run an MSI installer package which represents the traditional Windows deployment model many enterprises still use. After installation, you'll update the connection string configuration file to point to your Azure SQL Database, showing how traditional config file-based applications get configured.

The lab challenge requires you to configure network security and verify everything works end-to-end. You need to open NSG rules to allow HTTP traffic from the internet to your VM, configure SQL Database firewall rules to allow access from your VM's subnet using service endpoints for secure private connectivity, and then test the application through a browser to verify it's working and storing data in the database.

The key learning is that IaaS gives you complete control but requires managing everything manually including OS updates, security patches, application deployment, and monitoring. This is appropriate for legacy apps that can't easily move to PaaS but comes with significantly more operational overhead.

Let's deploy a complete IaaS application!
