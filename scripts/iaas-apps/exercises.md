# IaaS Apps - Exercises Narration Script

## Exercise 1: Create Resource Group

Let's begin by setting up our environment variables and creating a resource group.

First, I'll set some variables that we'll reuse throughout the lab. In PowerShell, I'm setting the location to westeurope, the resource group name to labs-iaas-apps, and defining names for our SQL server and database.

```
$location='westeurope'
$rg='labs-iaas-apps'
$server='myserver12345'
$database='signup'
```

Notice that the server name needs to be globally unique across Azure. Choose something that's likely to be unique to you.

Now let's create the resource group using the Azure CLI:

```
az group create -n $rg -l $location --tags courselabs=azure
```

Great! Our resource group is created and ready to hold our resources.

## Exercise 2: Create SQL Database

The application we'll deploy needs a SQL database to store user information. We'll create both a SQL Server and a database.

First, let's create the SQL Server. I'm specifying the resource group, location, server name, and administrator credentials:

```
az sql server create -g $rg -l $location -n $server -u sqladmin -p 'MySecurePassword123!'
```

Important note: In production, you'd use a much stronger password and store it securely, perhaps in Azure Key Vault.

Now let's create the database. I'm using the no-wait flag so we can continue with other tasks while the database provisions:

```
az sql db create -g $rg -n $database -s $server --no-wait
```

The database is now being created in the background. We can move on to setting up our virtual machine.

## Exercise 3: Create Windows Server VM

Our .NET Framework application requires Windows Server. Let's create a VM using the Windows Server 2022 Datacenter Core image.

First, let me show you how to find available Windows Server images. We'll list the SKUs for the WindowsServer offer:

```
az vm image list-skus -l westeurope -p MicrosoftWindowsServer -f WindowsServer -o table
```

We're looking for the 2022-datacenter-core-g2 SKU, which is a second-generation VM image.

Now let's create the virtual machine:

```
az vm create -l $location -g $rg -n app01 --image MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest --size Standard_D2s_v5 --admin-username labsadmin --public-ip-address-dns-name myapp-vm-12345 --admin-password 'MyVMPassword123!'
```

This command creates several resources: the VM itself, a network interface, a virtual network, a subnet, and a public IP address. The DNS name makes it easier to connect to the VM.

The VM creation takes a few minutes. While we wait, let's discuss what Windows Server Core means. It's a minimal installation without the full graphical interface, making it lighter and more secure.

## Exercise 4: Deploy the Application

Now that our VM is running, let's connect using Remote Desktop and deploy our application.

I'm connecting to the VM using the DNS name and credentials we specified. When you connect to a Server Core VM, you'll see a command prompt rather than the familiar Windows desktop.

### Step 4.1: Verify .NET Framework

First, let's verify that .NET Framework 4.8 is installed. I'll run a PowerShell command to check:

```
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -recurse |
Get-ItemProperty -name Version,Release -EA 0 |
Where { $_.PSChildName -match '^(?!S)\p{L}'} |
Select PSChildName, Version, Release
```

Perfect! We can see that .NET Framework 4.8 Full is installed.

### Step 4.2: Install Web Server

Next, we need to install IIS and the ASP.NET components. Let's first verify that IIS isn't already installed:

```
Get-WindowsFeature
```

As expected, the web server features show as Available, not Installed. Let's install them now:

```
Install-WindowsFeature Web-Server,NET-Framework-45-ASPNET,Web-Asp-Net45
```

This installs IIS, the ASP.NET runtime, and other required components. The installation completes quickly on Windows Server.

### Step 4.3: Install the Application

Our application is packaged as an MSI file hosted on GitHub. Let's download it:

```
curl -o signup.msi https://github.com/courselabs/azure/releases/download/labs-iaas-apps-1.0/SignUp-1.0.msi
```

Now we'll install it silently using msiexec:

```
Start-Process msiexec.exe -ArgumentList '/i', 'signup.msi', '/quiet', '/norestart' -NoNewWindow -Wait
```

Let's verify the installation was successful:

```
ls /docker4.net/SignUp.Web
```

Good! We can see the application files. Let's also check that it's registered with IIS:

```
Get-WebApplication
```

Perfect! The application is registered at the /signup path.

### Step 4.4: Test and Troubleshoot

Let's try accessing the application locally:

```
curl.exe -L http://localhost/signup
```

As expected, we get an error. The application can't connect to the database yet. Let's look at the connection string configuration:

```
cat C:\docker4.net\SignUp.Web\connectionStrings.config
```

The application is using a default connection string pointing to a local SQL Server. We need to update this with our Azure SQL Database connection details.

## Exercise 5: Configure Database Connection

Let's edit the configuration file to use our Azure SQL Database. I'll open it in Notepad:

```
notepad C:\docker4.net\SignUp.Web\connectionStrings.config
```

I'm replacing the connection string with our Azure SQL Database details. The format should be:

```
Server=myserver12345.database.windows.net;Database=signup;User Id=sqladmin;Password=MySecurePassword123!;Connect Timeout=10;
```

After saving the file, let's test again:

```
curl.exe -L http://localhost/signup
```

We're getting a different error now. The database exists, but our VM can't access it due to firewall rules.

## Exercise 6: Configure Network Access

Let's switch to the Azure Portal to configure network access. I'm opening the SQL Server resource and navigating to the Networking tab.

To allow access from our VM, I need to add a virtual network rule. But notice the message - we need to add a service endpoint to the VM's subnet first.

I'll navigate to the virtual network resource and select the subnet where our VM is connected. Under Service Endpoints, I'm adding Microsoft.Sql.

Now back to the SQL Server networking settings, I can add the virtual network rule, selecting the vnet and subnet where our VM resides.

Let's test the application again from the VM:

```
curl.exe -L http://localhost/signup
```

Excellent! We're getting HTML content with no errors. The application is successfully connecting to the database.

## Exercise 7: Make the Application Publicly Accessible

Currently, the application is only accessible from within the VM. To access it from the internet, we need to configure the Network Security Group.

In the Portal, I'm navigating to the VM's Network Security Group. I'll add an inbound security rule to allow HTTP traffic on port 80 from any source.

Now I can browse to the application from my local machine using the DNS name:

```
http://myapp-vm-12345.westeurope.cloudapp.azure.com/signup
```

Perfect! The Sign Up application homepage loads. Let me create a test user by filling out the form and clicking Sign Up.

## Exercise 8: Verify Database Storage

Let's verify that the data was saved to our SQL Database. In the Portal, I'm opening the SQL Database and navigating to the Query Editor.

After authenticating, I'll run a simple query:

```
SELECT * FROM Prospects
```

Excellent! We can see the test user data we just entered through the web application.

## Summary

In this lab, we've successfully:
- Created an Azure SQL Database
- Deployed a Windows Server VM
- Installed IIS and a .NET Framework application
- Configured secure connectivity between the VM and database
- Made the application publicly accessible
- Verified end-to-end functionality

This demonstrates the complete lifecycle of deploying a traditional application to Azure IaaS.

## Cleanup

Remember to delete your resources when you're done:

```
az group delete -y -n $rg
```

This deletes the resource group and all resources within it.
