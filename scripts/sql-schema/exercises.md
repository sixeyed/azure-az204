# Deploying Database Schemas - Exercises

## Exercise 1: Create a SQL Server

Let's start by creating a SQL Server that will host our database.

First, we'll set up some variables to make our commands easier to work with. We're using placeholder values here, but in your own environment, you'll need to provide unique names.

For the server name, you'll need a globally unique DNS name because this becomes part of the server's public address.

For the admin password, Azure requires a strong password that meets complexity requirements.

Now we'll create three resources:
- A resource group to contain everything
- A SQL Server instance
- And we'll tag it with our courselabs identifier for easy cleanup later

The SQL Server is the container that will host our databases. Notice we're specifying an admin username and password - you'll need these credentials later when you import the database.

Before we move on, let's open the Azure Portal and find our new SQL Server.

Click on the "Import Database" option in the top menu. Notice the configuration choices available. You can import a database directly from the Portal, but you need the Bacpac file to already be stored in Azure. That's what we'll set up next.

## Exercise 2: Upload the Bacpac File

To import a database, the Bacpac file needs to be stored in Azure. We'll use Azure Storage for this.

First, create a Storage Account. Like the SQL Server, the storage account name must be globally unique, and it can only contain lowercase letters and numbers.

We're using the Standard LRS SKU, which means locally redundant storage - fine for our demo purposes.

Next, create a container within the storage account. Think of containers like folders in a file system. We'll call ours "databases."

Now upload the Bacpac file from your local machine to the container. In Azure, files stored in blob storage are called BLOBs, which stands for Binary Large Objects.

The upload command specifies the local file path, the container name, the name to use in Azure, and the storage account.

Once the upload completes, let's verify it in the Portal. Open your Resource Group, find the Storage Account, navigate to Containers under Data Storage, and you'll see your "databases" container with the uploaded file inside.

Click on the file and you'll see its details, including a URL. Your blob URL will look something like this placeholder. Notice the first part is your storage account name - that's why it needs to be globally unique.

Can you download from that URL? Try it - you'll find you can't. By default, blob containers are private, meaning they can only be accessed within Azure. That's exactly what we want for security.

## Exercise 3: Import the Database

Now we're ready to import our database schema.

First, create an empty database using the az sql db create command. This runs asynchronously, so you can continue with the next steps while it's being created.

Before we can import, we need to set up firewall rules. Azure SQL Server blocks all access by default, so we need to explicitly allow connections.

We'll create two firewall rules:
- One to allow access from internal Azure services - this uses the special IP address of zero zero zero zero
- And one to allow access from our local machine for testing

To find your public IP address, you can use the curl command against ifconfig.me, or visit whatsmyip.org in your browser.

Now for the import. We need several pieces of information:
- The SQL Server admin credentials we set earlier
- The URL of the Bacpac file in storage
- A storage access key for authentication
- The database name and server

The tricky part is getting the storage access key. We'll generate a Shared Access Signature, or SAS token. This is a time-limited authentication token that grants read access to the specific file.

Generate the SAS token with an expiration date far in the future - we're using a placeholder date here. The output is a long string that serves as your access key.

Now run the import command, plugging in all the values. This tells Azure to download the Bacpac from storage and import it into your database.

The import process can take several minutes, especially for larger databases. You can monitor the progress in the Portal - open your SQL Server and look at the "Import/Export history" tab to see the status.

## Exercise 4: Verify the Database

Once the import completes, let's verify everything worked correctly.

Open your database in the Portal and navigate to the Query Editor blade. This is a browser-based SQL client built right into Azure.

Log in using the admin credentials you specified when creating the server.

Once connected, you'll see the object explorer on the left showing your database schema. Expand the tables and you'll see the tables that were imported from the Bacpac: Assets, AssetTypes, and Locations.

The Bacpac included some reference data, so the tables aren't empty. Let's run a query to verify.

Run SELECT star FROM Locations. You'll see location data for different countries.

Now try a more specific query: SELECT PostalCode FROM Locations WHERE Country equals 'UK'. This demonstrates that both the schema and data were successfully imported.

## Lab Exercise: Export a Database

For the lab exercise, you'll insert some additional data into the Assets table. We're using placeholder values for asset descriptions, types, and locations.

Run these three INSERT statements to add the new assets to your database.

Now here's the challenge: This data wasn't in the original Bacpac. Export a new Bacpac from your Azure database that includes this additional data.

Then think about how you would use that exported file. Could you recreate this database in another Azure region? Could you restore it to an on-premises SQL Server? Could you share it with another team?

Take some time to explore the export process. If you get stuck, check the hints file, or review the solution for the complete steps.

This ability to export and import databases is powerful for backup scenarios, for creating development and test environments, and for migrating between different SQL Server instances.
