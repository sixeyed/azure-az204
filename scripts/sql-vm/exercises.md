# SQL Server VMs - Exercises Script

## Exercise 1: Explore Azure SQL in the Portal

Let's start by exploring the available options in the Azure Portal.

Open the Azure Portal and search to create a new Azure SQL resource. When you see the options, click on SQL Virtual Machines to check the details.

Notice the variety of choices available:
- You can choose between Linux and Windows variants
- Different SQL Server versions are available
- Multiple SKUs are offered for different performance requirements

We won't create the database through the portal today. Instead, we'll use the Azure CLI to get hands-on experience with infrastructure-as-code approaches.

## Exercise 2: Create a Resource Group

First, we need to create a Resource Group where our new SQL resources will live.

Run the following command, using your own preferred location:

```bash
az group create -n labs-sql-vm --tags courselabs=azure -l westeurope
```

This creates a resource group called "labs-sql-vm" in the westeurope region. Remember, these are placeholder values - you would use your own naming conventions and preferred Azure region.

## Exercise 3: Find the SQL Server VM Image

Next, we need to identify the right VM image to use. We're looking for SQL Server 2019 Standard on a Windows Server 2022 machine.

First, find the available offers for SQL Server images. This includes both Windows and Linux options:

```bash
az vm image list-offers --publisher MicrosoftSQLServer -o table
```

Now, find a specific SKU:

```bash
az vm image list-skus -f sql2019-ws2022 -p MicrosoftSQLServer --location westeurope -o table
```

Finally, list all available images for our chosen configuration:

```bash
az vm image list --sku standard -f sql2019-ws2022 -p MicrosoftSQLServer --location westeurope -o table --all
```

Take note of the URN for the latest image version. It will look something like: MicrosoftSQLServer:sql2019-ws2022:standard:15.0.220913

## Exercise 4: Create the SQL Server VM

Now we'll create the SQL Server VM using the standard vm create command.

```bash
az vm create -l westeurope -g labs-sql-vm -n sql01 --image <urn> --size Standard_D2_v3 --admin-username labs --admin-password <your-strong-password> --public-ip-address-dns-name <your-dns-name>
```

Remember to replace:
- <urn> with the actual image URN you identified
- <your-strong-password> with a strong password meeting Azure's requirements
- <your-dns-name> with a unique DNS name

Once created, open the VM in the Portal. You'll notice it appears as a standard VM with no special SQL Server management options visible yet.

## Exercise 5: Check Network Security

Let's examine the Network Security Group. SQL Server listens on port 1433 by default. Check whether you can access it from the Internet.

At this point, even if you could access the VM, you don't have SQL Server authentication credentials configured. You can't specify SQL Server authentication when you create a normal VM.

To add enhanced management options, we need to register the VM with the SQL Server IaaS extension.

## Exercise 6: Register the VM for SQL Server Management

The SQL Server extension transforms your VM into something more like a managed database service.

First, check the help text to understand the available options:

```bash
az sql vm create --help
```

Now register your VM for SQL Server management. Configure it for public access and set up SQL Authentication:

```bash
az sql vm create -g labs-sql-vm -n sql01 --license-type PAYG --sql-mgmt-type Full --connectivity-type PUBLIC --sql-auth-update-username labs --sql-auth-update-pwd <strong-password>
```

This command:
- Uses PAYG (Pay As You Go) licensing
- Configures Full management for all management options
- Sets up PUBLIC connectivity
- Creates SQL authentication credentials with username "labs" and your chosen password

Now browse to the VM in the Portal. The UI looks similar, but check the Resource Group - you'll see a new SQL Virtual Machine resource has been created.

## Exercise 7: Verify Security Configuration

In the Portal, navigate to your SQL Virtual Machine resource and open the Security Configuration blade.

Verify that:
- Connectivity is set to Public
- The Network Security Group has a new rule allowing incoming traffic on port 1433

This rule was automatically added when we registered the VM with the SQL Server extension.

## Exercise 8: Enable RDP Access

SQL Server images come with SQL Server Management Studio pre-installed, so we can log in and use the UI to work with the database. First, we need to enable RDP access.

Find the name of your Network Security Group:

```bash
az network nsg list -g labs-sql-vm -o table
```

Add an NSG rule to allow port 3389 connections for RDP:

```bash
az network nsg rule create -g labs-sql-vm --nsg-name sql01NSG -n rdp --priority 150 --source-address-prefixes Internet --destination-port-ranges 3389 --access Allow
```

Now you can connect to the VM using Remote Desktop Protocol.

## Exercise 9: Create a Custom User-Defined Function

We'll demonstrate a SQL Server feature that isn't available on managed services: creating a custom function that calls .NET code.

First, copy the DLL file from labs/sql-vm/udf/FormattedDate.dll to the root of the C: drive on your VM. This binary file contains the .NET code we want to make available through SQL Server.

Launch SQL Server Management Studio on the VM. The default connection settings use the machine name and Windows authentication, which will work fine.

Connect to the server and click New Query. Run this SQL to register a User-Defined Function:

```sql
sp_configure 'show advanced options', 1
RECONFIGURE
GO

sp_configure 'clr enabled', 1
RECONFIGURE
GO

sp_configure 'clr strict security', 0
RECONFIGURE
GO

CREATE ASSEMBLY FormattedDate FROM 'C:\FormattedDate.dll';
GO

CREATE FUNCTION LegacyDate() RETURNS NVARCHAR(7)
AS EXTERNAL NAME FormattedDate.FormattedDate.LegacyNow;
GO
```

This sequence:
- Enables advanced configuration options
- Enables CLR (Common Language Runtime) integration
- Disables CLR strict security for this demonstration
- Creates an assembly from our DLL file
- Creates a function that calls into the .NET code

You couldn't perform these operations with Azure SQL Database or SQL Managed Instance because you don't have access to upload files to disk, and some of these commands would be restricted.

## Exercise 10: Test the User-Defined Function

Now let's test the UDF we just created:

```sql
SELECT dbo.LegacyDate();
GO
```

You'll see the current date returned in a legacy system format. This date was generated by the .NET code you uploaded in the DLL, demonstrating the power and flexibility of SQL Server VMs.

## Lab Challenge

For your final challenge, you'll create a new SQL Server login with custom credentials.

Your task:
1. Create a new SQL Server login with a username and password
2. Configure appropriate permissions
3. Connect to the database server from your own machine using those credentials
4. Run the SELECT dbo.LegacyDate() query to verify access

This demonstrates another key advantage of SQL VMs: you can own authentication without using standard Azure auth, and you can create multiple users with whatever access levels you need.

## Cleanup

When you're finished with the lab, clean up your resources to avoid unnecessary charges:

```bash
az group delete -y -n labs-sql-vm
```

This removes the resource group and all resources within it.

Great work completing this lab on SQL Server Virtual Machines!
