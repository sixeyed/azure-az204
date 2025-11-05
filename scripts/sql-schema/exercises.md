# Deploying Database Schemas - Exercises

## Exercise 1: Create a SQL Server

Let's start by creating a SQL Server that will host our database.

First, we'll set up some variables to make our commands easier to work with. We're using placeholder values here, but in your own environment, you'll need to provide unique names. For the server name, you'll need a globally unique DNS name because this becomes part of the server's public address in the format your-server-name.database.windows.net. For the admin password, Azure requires a strong password that meets complexity requirements - typically at least 8 characters with uppercase, lowercase, numbers, and special characters.

Now we'll create three resources in sequence. We're creating a resource group to contain everything using az group create with the name, location, and our courselabs tag for easy cleanup later. Then we're creating a SQL Server instance using az sql server create. The SQL Server is the container that will host our databases - it's not a database itself, but rather the server infrastructure that manages databases. We're specifying an admin username and password here - you'll need these credentials later when you import the database, so make note of them.

Before we move on, let's open the Azure Portal and find our new SQL Server. Navigate to your resource group and you'll see the SQL Server resource listed there. Click on it to see the overview.

Click on the "Import Database" option in the top menu bar. Notice the configuration choices available in this wizard. You can import a database directly from the Portal, which is convenient for ad-hoc imports. However, you need the Bacpac file to already be stored in Azure - specifically in Azure Blob Storage. You can't upload directly from your local machine through the Portal import wizard. That's what we'll set up next.

## Exercise 2: Upload the Bacpac File

To import a database, the Bacpac file needs to be stored in Azure. We'll use Azure Storage for this, which is the standard approach for database import operations.

First, create a Storage Account using az storage account create. Like the SQL Server, the storage account name must be globally unique across all of Azure, and it can only contain lowercase letters and numbers - no hyphens, underscores, or uppercase letters are allowed. This is because the storage account name becomes part of the DNS name for accessing your blobs. We're using the Standard LRS SKU, which means locally redundant storage - three copies of your data within a single datacenter. This is fine for our demo purposes where we don't need geographic redundancy.

Next, create a container within the storage account using az storage container create. Think of containers like folders in a file system - they organize your blobs into logical groups. We'll call ours "databases" to indicate what it contains. Containers provide a namespace for organizing blobs and also serve as the unit for access control policies.

Now upload the Bacpac file from your local machine to the container using az storage blob upload. In Azure, files stored in blob storage are called BLOBs, which stands for Binary Large Objects. The upload command specifies several parameters: the file parameter points to your local file path, the container-name identifies which container to upload into, the name parameter specifies what to call the blob in Azure - you can change this if you want a different name than the local file, and the account-name identifies which storage account to upload to.

Once the upload completes, let's verify it in the Portal to see what we created. Open your Resource Group, find the Storage Account, and click on it. Navigate to Containers under Data Storage in the left menu, and you'll see your "databases" container. Click on the container and you'll see the uploaded Bacpac file inside with details like its size and last modified time.

Click on the file itself and you'll see its details page, including a URL. Your blob URL will look something like https://your-storage-account-name.blob.core.windows.net/databases/your-file.bacpac. Notice the first part is your storage account name - that's why it needs to be globally unique, since this URL is how you access the blob over the internet.

Can you download from that URL? Try copying it and pasting it into a new browser tab. You'll find you can't access it - you'll get an error. By default, blob containers are private, meaning they can only be accessed by authenticated requests within Azure. You can't just browse to the URL like a public website. That's exactly what we want for security - database backups shouldn't be publicly accessible on the internet.

## Exercise 3: Import the Database

Now we're ready to import our database schema from the Bacpac file we uploaded.

First, create an empty database using the az sql db create command. We're specifying the resource group, the database name, and the server name. This runs asynchronously, so you can continue with the next steps while it's being created - Azure provisions the database resources in the background.

Before we can import, we need to set up firewall rules. Azure SQL Server blocks all access by default as a security measure, so we need to explicitly allow connections from specific sources.

We'll create two firewall rules for different purposes. The first rule allows access from internal Azure services using az sql server firewall-rule create. This uses the special IP address of 0.0.0.0 which is a shorthand in Azure meaning "allow other Azure services" - this lets Azure's import service access the SQL Server. The second rule allows access from our local machine for testing and management. To find your public IP address, you can use the curl command against ifconfig.me which returns your IP, or visit whatsmyip.org in your browser. Create the firewall rule with your IP address to allow connections from your local machine.

Now for the import operation, which is the main event. We need several pieces of information to make this work. We'll use az sql db import with multiple parameters. We need the SQL Server admin credentials we set earlier when creating the server. We need the URL of the Bacpac file in storage - this is the full blob URL we looked at earlier. We need a storage access key for authentication so Azure can download the blob. And we specify the database name and server where the data should be imported.

The tricky part is getting the storage access key. We'll generate a Shared Access Signature, or SAS token, using az storage blob generate-sas. This is a time-limited authentication token that grants read access to the specific file. We're generating the SAS token with an expiration date far in the future - use a placeholder date like 2030-12-31T23:59Z. The output is a long string that serves as your access key, allowing temporary access to the blob without exposing your full storage account key.

Now run the import command, plugging in all the values we've gathered - the admin username, the admin password in quotes, the blob URI, the SAS token, the database name, and the server name. This command tells Azure to download the Bacpac from storage and import it into your database. Azure handles extracting the schema and data, creating tables, and setting up all the database objects.

The import process can take several minutes, especially for larger databases. The Bacpac format contains the entire database structure and data, and importing involves recreating all of this. You can monitor the progress in the Portal - open your SQL Server resource and look at the "Import/Export history" tab under Operations. You'll see the import operation listed with a status indicator showing whether it's in progress, completed, or failed.

## Exercise 4: Verify the Database

Once the import completes successfully, let's verify everything worked correctly and that we can access our data.

Open your database in the Portal by navigating to the database resource and navigate to the Query Editor blade on the left menu. This is a browser-based SQL client built right into Azure - you don't need SQL Server Management Studio or any other tools installed locally. It's convenient for quick queries and administration.

Log in using the admin credentials you specified when creating the server. Enter the username and password, then click OK to connect. The Query Editor uses the browser to establish a connection to your database.

Once connected, you'll see the object explorer on the left showing your database schema. Expand the tables node and you'll see the tables that were imported from the Bacpac: Assets, AssetTypes, and Locations. These came from the Bacpac file, demonstrating that both the schema structure and the actual data were successfully imported.

The Bacpac included some reference data, so the tables aren't empty. Let's run a query to verify the data is there. In the query window, run SELECT star FROM Locations. You'll see location data for different countries displayed in the results pane - rows containing country names, postal codes, and other location information.

Now try a more specific query to test filtering: SELECT PostalCode FROM Locations WHERE Country equals 'UK'. This demonstrates that both the schema structure was correctly imported - the columns and data types are right - and the data itself is intact and queryable. You'll see postal codes for UK locations returned in the results.

## Lab Exercise: Export a Database

For the lab exercise, you'll practice the reverse operation - exporting a database. First, let's add some new data that wasn't in the original Bacpac. We're using placeholder values for asset descriptions, types, and locations.

Run these three INSERT statements in the Query Editor to add new assets to your database. First statement: INSERT INTO Assets with values for Description, AssetTypeId, and LocationId. Second statement: Another INSERT with different values. Third statement: A third INSERT completing the set. Execute each one and verify they succeed.

Now here's the challenge: This data wasn't in the original Bacpac we imported. Your task is to export a new Bacpac from your Azure database that includes this additional data. The exported file will contain the original data plus the three new rows you just inserted.

Then think about how you would use that exported file. Could you recreate this database in another Azure region for disaster recovery or geographic distribution? Could you restore it to an on-premises SQL Server for hybrid scenarios? Could you share it with another team for development or testing? All of these are valid use cases for Bacpac files.

Take some time to explore the export process using either the Portal or the Azure CLI. If you get stuck, check the hints file in the lab folder, or review the solution for the complete steps. The export process is similar to import but in reverse - you'll use az sql db export to create a Bacpac from your live database.

This ability to export and import databases is powerful for several scenarios. You can use it for backup purposes, though Azure SQL also has built-in automated backups. You can create development and test environments by exporting production data and importing it elsewhere with sensitive data masked. You can migrate between different SQL Server instances, whether in Azure or on-premises. And you can share database structures and sample data with other teams or organizations.
