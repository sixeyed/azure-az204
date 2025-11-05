# IaaS Apps - Exercises Narration Script

## Exercise 1: Create Resource Group

Let's begin by setting up our environment variables and creating a resource group.

First, we'll set some variables that we'll reuse throughout the lab. In PowerShell, we're setting the location to westeurope, the resource group name to labs-iaas-apps, and defining names for our SQL server and database.

Notice that the server name needs to be globally unique across Azure. Choose something that's likely to be unique to you - maybe including your initials and some numbers is a good approach.

Now let's create the resource group using the Azure CLI. We're using the group create command with parameters for the name, location, and tags. The courselabs equals azure tag helps us track resources created for this course, which is a best practice for organizing and managing resources.

Great! Our resource group is created and ready to hold our resources.

## Exercise 2: Create SQL Database

The application we'll deploy needs a SQL database to store user information. We'll create both a SQL Server and a database.

First, let's create the SQL Server. We're specifying the resource group, location, server name, and administrator credentials using the sql server create command. The username is set to sqladmin, and we're providing a password.

Important note: In production, you'd use a much stronger password and store it securely, perhaps in Azure Key Vault. Never hardcode production credentials like this.

Now let's create the database. We're using the sql db create command with parameters for the resource group, database name, and server name. The no-wait flag is particularly useful here - it allows us to continue with other tasks while the database provisions in the background. Database provisioning can take several minutes, so this parallelism saves us time.

The database is now being created in the background. We can move on to setting up our virtual machine.

## Exercise 3: Create Windows Server VM

Our .NET Framework application requires Windows Server. Let's create a VM using the Windows Server 2022 Datacenter Core image.

First, let me show you how to find available Windows Server images. We'll list the SKUs for the WindowsServer offer using the vm image list-skus command. This shows us all the available variations of Windows Server images in our chosen region.

We're looking for the 2022-datacenter-core-g2 SKU, which is a second-generation VM image. The "g2" designation means it uses the newer generation of Azure's hypervisor, which offers better performance and more features.

Now let's create the virtual machine using the vm create command. We're specifying the location, resource group, and VM name "app01". The image parameter uses the full image URN format - publisher colon offer colon SKU colon version. We're choosing the Standard D2s v5 size, which provides 2 virtual CPUs and 8 gigabytes of memory - plenty for our application. The admin-username parameter sets the local administrator account name, and we're providing a password. The public-ip-address-dns-name parameter creates a friendly DNS name that makes it easier to connect to the VM.

This command creates several resources automatically: the VM itself, a network interface, a virtual network, a subnet, and a public IP address. Azure handles all of this infrastructure provisioning for you. The DNS name we specified will become part of the fully qualified domain name, making our VM accessible at something like myapp-vm-12345 dot westeurope dot cloudapp dot azure dot com.

The VM creation takes a few minutes. While we wait, let's discuss what Windows Server Core means. It's a minimal installation without the full graphical interface - no Start menu, no desktop, just a command prompt. This makes it lighter on resources, faster to boot, and more secure because there are fewer components that could be exploited. It's perfect for server workloads where you don't need the GUI.

## Exercise 4: Deploy the Application

Now that our VM is running, let's connect using Remote Desktop and deploy our application.

We're connecting to the VM using the DNS name and the credentials we specified during creation. When you connect to a Server Core VM, you'll see a command prompt rather than the familiar Windows desktop. This can be disorienting at first, but everything you need is accessible through PowerShell.

### Step 4.1: Verify .NET Framework

First, let's verify that .NET Framework 4.8 is installed. We'll run a PowerShell command that queries the Windows registry to check installed .NET Framework versions. This command looks at the registry key where Microsoft stores .NET Framework installation information, retrieving the version and release numbers for all installed frameworks.

Perfect! We can see that .NET Framework 4.8 Full is installed. This is exactly what our application needs, and it comes pre-installed with Windows Server 2022.

### Step 4.2: Install Web Server

Next, we need to install IIS and the ASP.NET components. Let's first verify that IIS isn't already installed using the Get-WindowsFeature PowerShell command. This lists all available Windows features and their installation status.

As expected, the web server features show as Available, not Installed. Let's install them now using the Install-WindowsFeature command. We're installing three components: Web-Server for IIS itself, NET-Framework-45-ASPNET for the ASP.NET runtime, and Web-Asp-Net45 for the ASP.NET integration with IIS.

This installs IIS, the ASP.NET runtime, and other required components. The installation completes quickly on Windows Server - usually just a minute or two. You'll see a progress bar and then a success message indicating whether a restart is required. In most cases, no restart is needed.

### Step 4.3: Install the Application

Our application is packaged as an MSI file hosted on GitHub. Let's download it using curl. We're saving it to a file called signup dot msi in the current directory.

Now we'll install it silently using msiexec. The Start-Process command launches msiexec with several arguments: the /i flag indicates installation, we specify our MSI file name, /quiet suppresses any user interface, and /norestart prevents an automatic reboot. The NoNewWindow and Wait parameters ensure we can see the output and the command doesn't return until installation completes.

Let's verify the installation was successful by listing the application directory. We're looking in the /docker4.net/SignUp.Web folder where our installer places files.

Good! We can see the application files - DLL files, configuration files, and web content. Let's also check that it's registered with IIS using the Get-WebApplication PowerShell command.

Perfect! The application is registered at the /signup path. This means IIS knows about our application and will serve it when users request that URL path.

### Step 4.4: Test and Troubleshoot

Let's try accessing the application locally using curl. We're making a request to localhost on port 80 with the /signup path. The -L flag tells curl to follow redirects.

As expected, we get an error. The application is running, but it can't connect to the database yet. Let's look at the connection string configuration by viewing the contents of the connectionStrings dot config file.

The application is using a default connection string pointing to a local SQL Server at localhost with a database named SignUpDb. But our database is in Azure SQL, not on this VM. We need to update this configuration with our Azure SQL Database connection details.

## Exercise 5: Configure Database Connection

Let's edit the configuration file to use our Azure SQL Database. We'll open it in Notepad - even in Server Core, we have access to basic GUI applications like Notepad.

We're replacing the connection string with our Azure SQL Database details. The format specifies the Server as our Azure SQL server's fully qualified domain name - something like myserver12345 dot database dot windows dot net. The Database parameter is set to "signup", matching the database we created earlier. The User Id is sqladmin, and the Password matches what we set during SQL Server creation. We're also adding a Connect Timeout parameter set to 10 seconds to avoid hanging indefinitely if there's a connection problem.

After saving the file, let's test again using curl.

We're getting a different error now. The database exists, but our VM can't access it due to firewall rules. This is actually good security - Azure SQL databases aren't publicly accessible by default. We need to explicitly grant network access.

## Exercise 6: Configure Network Access

Let's switch to the Azure Portal to configure network access. We're opening the SQL Server resource and navigating to the Networking tab under Security settings.

To allow access from our VM, we need to add a virtual network rule. But notice the message Azure is showing us - we need to add a service endpoint to the VM's subnet first. This is a prerequisite.

Service endpoints provide a secure path from Azure virtual networks to Azure services. Instead of going through the public internet, traffic stays on the Microsoft backbone network. This is more secure and often faster.

Let's navigate to the virtual network resource and select the subnet where our VM is connected. Under Service Endpoints, we'll add Microsoft dot Sql. This enables SQL Database connectivity for all resources in this subnet.

Now back to the SQL Server networking settings, we can add the virtual network rule, selecting the virtual network and subnet where our VM resides. This creates a firewall rule that allows connections from any resource in that subnet.

Let's test the application again from the VM using curl.

Excellent! We're getting HTML content with no errors. The application is successfully connecting to the Azure SQL Database, processing the request, and returning the web page. This confirms our networking configuration is correct.

## Exercise 7: Make the Application Publicly Accessible

Currently, the application is only accessible from within the VM. To access it from the internet, we need to configure the Network Security Group.

In the Portal, we're navigating to the VM's Network Security Group. This is the firewall that controls what traffic can reach the VM. We'll add an inbound security rule to allow HTTP traffic.

The rule configuration specifies the source as "Any" - meaning any IP address on the internet. The source port ranges are set to asterisk for any port. The destination is also "Any" - any IP in the virtual network. The destination port is 80 for HTTP traffic. The protocol is TCP, and the action is Allow. We'll give it a priority number like 1000 - lower numbers are evaluated first. A descriptive name like "Allow-HTTP" helps identify the rule's purpose.

Now we can browse to the application from our local machine using the DNS name we configured. The URL is http colon slash slash myapp-vm-12345 dot westeurope dot cloudapp dot azure dot com slash signup.

Perfect! The Sign Up application homepage loads in our browser. We're accessing it over the public internet, going through the Network Security Group firewall, hitting IIS on our VM, which is running our application that connects to Azure SQL Database. The full end-to-end architecture is working.

Let me create a test user by filling out the form - entering a first name, last name, email address, and selecting a role - then clicking Sign Up.

The form submission completes successfully, and we see a confirmation message. The data has been saved to our database.

## Exercise 8: Verify Database Storage

Let's verify that the data was saved to our SQL Database. In the Portal, we're opening the SQL Database and navigating to the Query Editor. This browser-based tool lets us run SQL queries without needing SQL Server Management Studio.

After authenticating with our SQL admin credentials, we'll run a simple SELECT query: SELECT asterisk FROM Prospects. This retrieves all rows from the Prospects table where our application stores user signups.

Excellent! We can see the test user data we just entered through the web application. The first name, last name, email, and role are all there, along with a timestamp showing when the record was created. This confirms the complete data flow - from web form, through our application, into Azure SQL Database.

## Summary

In this lab, we've successfully created an Azure SQL Database, deployed a Windows Server VM, installed IIS and a .NET Framework application, configured secure connectivity between the VM and database using virtual network service endpoints, made the application publicly accessible through Network Security Group rules, and verified end-to-end functionality from web form to database storage.

This demonstrates the complete lifecycle of deploying a traditional application to Azure IaaS. While this approach requires more management than Platform-as-a-Service options, it gives you complete control over the infrastructure and is often necessary when migrating legacy applications to the cloud.

## Cleanup

Remember to delete your resources when you're done. We'll use the group delete command with the yes flag to skip confirmation and provide the resource group name. This deletes the resource group and all resources within it - the VM, virtual network, SQL server, database, all of it.

This removes everything we created in this lab, ensuring you won't incur ongoing charges.
