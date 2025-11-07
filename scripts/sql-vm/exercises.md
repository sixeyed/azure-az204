# SQL Server VMs - Exercises Script

## Explore Azure SQL in the Portal

Let's start by exploring the available options in the Azure Portal to understand what choices we have for running SQL Server.

Open the Azure Portal and search to create a new Azure SQL resource. When you see the deployment page with all the options, click on SQL Virtual Machines to check the details. This is one of the three main ways to run SQL Server in Azure - the other two being Azure SQL Database and SQL Managed Instance.

Notice the variety of choices available when you browse the options. You can choose between Linux and Windows variants - SQL Server runs on both operating systems now. Different SQL Server versions are available including 2019, 2017, and others. Multiple SKUs are offered for different performance requirements - you'll see options like Standard, Enterprise, Web, and Express editions.

We won't create the database through the portal today. Instead, we'll use the Azure CLI to get hands-on experience with infrastructure-as-code approaches. This is more repeatable and easier to automate than clicking through the portal.

## Create a Resource Group

First, we need to create a Resource Group where our new SQL resources will live, providing organization and making cleanup easier later.

Run the az group create command, using your own preferred location. We're creating a resource group called "labs-sql-vm" with -n for the name, adding --tags courselabs=azure for tracking, and using -l westeurope for the location. Remember, these are placeholder values - you would use your own naming conventions and preferred Azure region based on where your users are located or data residency requirements.

## Find the SQL Server VM Image

Next, we need to identify the right VM image to use. We're looking for SQL Server 2019 Standard on a Windows Server 2022 machine - this gives us a recent SQL Server version on the latest Windows Server.

First, find the available offers for SQL Server images using az vm image list-offers. We're specifying --publisher MicrosoftSQLServer since Microsoft publishes these official images, and using -o table for readable output. This includes both Windows and Linux options, showing all the different SQL Server versions and Windows Server combinations available.

Now, find a specific SKU within the SQL Server 2019 on Windows Server 2022 offer using az vm image list-skus. We're using -f sql2019-ws2022 to specify the offer, -p MicrosoftSQLServer for the publisher, --location westeurope to see images in our region, and -o table for formatting. This shows the different editions available like Standard, Enterprise, Web, and Express.

Finally, list all available images for our chosen configuration using az vm image list. We're specifying --sku standard for the Standard edition, -f sql2019-ws2022 for the offer, -p MicrosoftSQLServer for the publisher, --location westeurope for the region, -o table for output, and --all to see all versions rather than just the latest. This is important because sometimes you need a specific patch level or build.

Take note of the URN for the latest image version. It will look something like: MicrosoftSQLServer:sql2019-ws2022:standard:15.0.220913. The URN uniquely identifies this specific image and is what we'll use to create our VM.

## Create the SQL Server VM

Now we'll create the SQL Server VM using the standard vm create command. This is just like creating any other VM, but the image we're using has SQL Server pre-installed and configured.

We're using az vm create with -l westeurope for location, -g labs-sql-vm for the resource group, -n sql01 as the VM name, --image with your URN from the previous step, --size Standard_D2_v3 which provides 2 vCPUs and 8GB RAM - suitable for development and testing, --admin-username labs for the Windows admin account, --admin-password with a strong password meeting Azure's requirements, and --public-ip-address-dns-name with a unique DNS name so we can access the VM remotely.

Remember to replace the placeholders: use the actual image URN you identified earlier, provide a strong password with uppercase, lowercase, numbers, and special characters meeting Azure's requirements, and specify a unique DNS name that's globally unique within the Azure region.

Once created, open the VM in the Portal by navigating to your resource group and clicking on the VM. You'll notice it appears as a standard VM with the usual options - compute, networking, storage. You won't see any special SQL Server management options visible yet. This is because we created it as a regular VM - we haven't registered it for SQL Server management yet.

## Check Network Security

Let's examine the Network Security Group to understand the default security configuration. SQL Server listens on port 1433 by default for database connections. Check whether you can access it from the Internet by looking at the NSG rules.

At this point, even if you could access the VM over the network, you don't have SQL Server authentication credentials configured. You can't specify SQL Server authentication when you create a normal VM - you only get the Windows admin credentials. The SQL Server installation on the VM uses Windows authentication by default.

To add enhanced management options and configure SQL authentication, we need to register the VM with the SQL Server IaaS extension. This transforms your VM from a generic virtual machine into a managed SQL Server resource.

## Register the VM for SQL Server Management

The SQL Server extension transforms your VM by providing Azure-integrated management capabilities for SQL Server.

First, check the help text to understand the available options using az sql vm create --help. This shows all the parameters you can configure, including licensing, management level, connectivity, and authentication.

Now register your VM for SQL Server management using az sql vm create. Configure it for public access and set up SQL Authentication. We're specifying -g labs-sql-vm for the resource group, -n sql01 for the VM name matching your VM, --license-type PAYG for Pay As You Go licensing which includes SQL Server license costs in the VM pricing, --sql-mgmt-type Full for full management capabilities giving you all management options, --connectivity-type PUBLIC to allow internet access, --sql-auth-update-username labs for creating a SQL authentication login, and --sql-auth-update-pwd with a strong password for SQL authentication.

This command does several things behind the scenes. It installs the SQL IaaS extension on the VM. It configures SQL Server for SQL authentication in addition to Windows authentication. It sets up the firewall to allow SQL Server traffic. And it creates the SQL authentication login you specified.

Now browse to the VM in the Portal and look at the resource list. The UI looks similar for the VM itself, but check the Resource Group - you'll see a new SQL Virtual Machine resource has been created. This is a separate Azure resource that provides SQL-specific management capabilities.

## Verify Security Configuration

In the Portal, navigate to your SQL Virtual Machine resource and open the Security Configuration blade to see what changed.

Verify that Connectivity is set to Public, allowing connections from the internet. Check that the Network Security Group has a new rule allowing incoming traffic on port 1433. Click on the networking section and you'll see this rule was automatically added when we registered the VM with the SQL Server extension. This is one of the conveniences of the extension - it handles common configuration tasks automatically.

## Enable RDP Access

SQL Server images come with SQL Server Management Studio pre-installed, so we can log in remotely and use the graphical UI to work with the database. First, we need to enable RDP access so we can connect to the Windows desktop.

Find the name of your Network Security Group using az network nsg list with -g labs-sql-vm for the resource group and -o table for readable output. It will typically be named after your VM, something like sql01NSG.

Add an NSG rule to allow port 3389 connections for RDP using az network nsg rule create. We're specifying -g labs-sql-vm for the resource group, --nsg-name sql01NSG for the NSG name you just found, -n rdp as the rule name, --priority 150 which must be unique and lower numbers have higher priority, --source-address-prefixes Internet to allow connections from anywhere, --destination-port-ranges 3389 for the RDP port, and --access Allow to permit the traffic.

Now you can connect to the VM using Remote Desktop Protocol. In the Portal, click the Connect button on your VM, download the RDP file, and open it. Enter your Windows admin credentials - the labs username and password you specified when creating the VM.

## Create a Custom User-Defined Function

We'll demonstrate a SQL Server feature that isn't available on managed services like Azure SQL Database: creating a custom function that calls .NET code. This showcases the flexibility you get with full control over SQL Server.

First, copy the DLL file from your lab folder at labs/sql-vm/udf/FormattedDate.dll to the root of the C: drive on your VM. You can do this through the RDP session by copying from your local machine or downloading it from a file share. This binary file contains the .NET code we want to make available through SQL Server.

Launch SQL Server Management Studio on the VM - it should be available in the Start menu or taskbar. The default connection settings use the machine name and Windows authentication, which will work fine since you're logged in with the admin account. Connect to the server by clicking Connect in the dialog.

Click New Query to open a query window. Run this SQL script to register a User-Defined Function. The script does several things in sequence. First, we're running sp_configure 'show advanced options', 1 followed by RECONFIGURE to enable advanced configuration options. Then sp_configure 'clr enabled', 1 and RECONFIGURE to enable CLR integration which allows .NET code to run in SQL Server. Then sp_configure 'clr strict security', 0 and RECONFIGURE to disable CLR strict security for this demonstration - in production you'd use signed assemblies instead. Then CREATE ASSEMBLY FormattedDate FROM 'C:\FormattedDate.dll' to load the DLL into SQL Server. Finally, CREATE FUNCTION LegacyDate() RETURNS NVARCHAR(7) AS EXTERNAL NAME FormattedDate.FormattedDate.LegacyNow to create a function that calls into the .NET code.

You couldn't perform these operations with Azure SQL Database or SQL Managed Instance for several reasons. You don't have access to upload files to disk since those are fully managed services. Some of these configuration commands would be restricted because they affect server-level settings. The managed services prioritize security and consistency, so they don't allow arbitrary .NET code execution. This demonstrates why you might choose a VM - you get complete control at the cost of managing the infrastructure yourself.

## Test the User-Defined Function

Now let's test the UDF we just created to see it in action.

Run this SQL query: SELECT dbo.LegacyDate() followed by GO. You'll see the current date returned in a legacy system format - perhaps something like a two-digit year format that older systems used. This date was generated by the .NET code you uploaded in the DLL, not by SQL Server's built-in date functions. This demonstrates the power and flexibility of SQL Server VMs - you can extend the database engine with custom functionality.

## Lab Challenge

For your final challenge, you'll create a new SQL Server login with custom credentials, demonstrating another advantage of having full control over SQL Server.

Your task includes several steps. Create a new SQL Server login with a username and password of your choosing using CREATE LOGIN. Configure appropriate permissions using GRANT statements to give the login access to specific databases. Connect to the database server from your own machine using those credentials rather than the admin account - you'll use SQL Server Management Studio or another SQL client installed locally. Run the SELECT dbo.LegacyDate() query to verify access and confirm the function works for this new login.

This demonstrates another key advantage of SQL VMs: you can own authentication without using standard Azure auth mechanisms. You can create multiple users with whatever access levels you need. You have complete control over security policies and configurations. This level of control isn't available with managed database services.

## Reference

- [Azure documentation](https://docs.microsoft.com/azure/)

## Cleanup

When you're finished with the lab, clean up your resources to avoid unnecessary charges from the running VM.

Use az group delete with -y to confirm without prompting and -n labs-sql-vm to specify the resource group. This removes the resource group and all resources within it - the VM, the SQL Virtual Machine resource, disks, network interfaces, public IPs, and everything else we created.

Great work completing this lab on SQL Server Virtual Machines! You've learned when and why to use VMs versus managed services, and you've gained hands-on experience with the unique capabilities that full control provides.
