# Azure Storage Accounts - Exercises Narration

## Exercise 1: Exploring Storage Account Options

Let's start by exploring what options are available when creating a Storage Account.

Open the Azure Portal and create a new resource. Search for "Storage Account" and take a look at the configuration options.

First, you'll notice the name field. Storage account names must be globally unique across all of Azure. Not just unique to your subscription - globally unique. The naming rules are quite strict: lowercase letters and numbers only, between 3 and 24 characters.

Next, look at the region selection. This is important because it determines where your data is physically stored. Choose a region close to your users or applications for the best performance.

You'll also see options for performance levels - Standard or Premium. Standard uses traditional hard disk drives, while Premium uses SSDs for higher performance scenarios.

Finally, there's the redundancy level we discussed earlier - LRS, ZRS, or GRS. Each offers different levels of protection at different price points.

## Exercise 2: Creating a Storage Account with Azure CLI

Now let's create a storage account using the Azure CLI. First, we'll create a resource group to organize our resources.

Run the following command:

```
az group create -n labs-storage -l westeurope --tags courselabs=azure
```

This creates a resource group named "labs-storage" in the West Europe region with a tag to help us track our lab resources.

Before we create the storage account, let's check the help documentation:

```
az storage account create --help
```

Take a moment to review the available parameters. Notice the SKU parameter - this combines both performance and redundancy settings into a single value.

For example:
- Premium underscore LRS is premium performance with local redundancy
- Standard underscore GRS is standard performance with geo redundancy

Now, let's create a zone-redundant storage account with standard performance. The command looks like this:

```
az storage account create -g labs-storage -l westeurope --sku Standard_ZRS -n <your-unique-name>
```

Remember to replace the placeholder with your own globally unique name.

## Exercise 3: Working with Blob Storage

Now that we have a storage account, let's explore blob storage. Open your newly created storage account in the Portal.

One storage account can support multiple types of storage. Today we'll focus on Blob storage - that's Binary Large Objects - which is essentially file storage in the cloud.

Blob storage organizes files in containers. Think of containers like folders, but with one important limitation: blob storage is not hierarchical. You cannot have containers inside other containers. However, you can use forward slashes in blob names to simulate a folder structure.

Let's upload a file. In the Storage Account blade, you'll see an Upload option in the main menu. Click that, browse to the document dot txt file in the labs folder, and upload it.

You'll need to create a container for the blob. Let's call it "drops". Enter that name when prompted.

## Exercise 4: Public vs Private Access

Now let's explore access control. Click on Storage browser in the left navigation and open Blob containers.

Open the "drops" container and you'll see your document dot txt file. Click on it and look at the overview. You'll see a URL - this is the direct link to your blob.

Let's try to access it. Copy that URL and try to download the file using curl:

```
curl -o download.txt https://<your-storage-account>.blob.core.windows.net/drops/document.txt
```

The command appears to succeed. But let's check the contents:

```
cat download.txt
```

Interesting! Instead of your document content, you're seeing an XML error message. This is because new blob containers default to private access. Even though you have the URL, anonymous access is not permitted.

Let's fix this. Browse to the drops container in the Portal and select "Change access level".

You have two options:
- Blob access allows anyone with the URL to download that specific file
- Container access allows anyone to list all contents and download any blob

For this exercise, set it to blob-level access.

Now try downloading again:

```
curl -o download2.txt https://<your-storage-account>.blob.core.windows.net/drops/document.txt
cat download2.txt
```

Success! Now you can see the correct contents.

## Exercise 5: Storage for VM Disks

Blob storage has another interesting use case - storing virtual machine disks. While Azure uses managed disks by default, you can choose to use unmanaged disks stored in your own storage account.

This gives you more control over the storage configuration and lets you manage VM disks alongside other data.

First, let's create a premium storage account for our VM disks:

```
az storage account create -g labs-storage -l westeurope --sku Premium_LRS -n <disk-storage-name>
```

Next, we need a container for the disks:

```
az storage container create -n vm-disks --account-name <disk-storage-name>
```

Now we can create a VM that uses this storage. Note that we need to use a VM size that supports premium storage:

```
az vm create -l westeurope -g labs-storage -n vm01 --image UbuntuLTS --size Standard_D2as_v5 --use-unmanaged-disk --storage-container-name vm-disks --storage-account <disk-storage-name>
```

Once the VM is created, browse to the storage account. Open the vm-disks container and you'll see your VM's OS disk stored as a VHD blob.

These unmanaged disks don't appear as separate resources in the Portal like managed disks do. They're simply blobs in your storage container.

## Lab Challenge

Now it's time for a challenge. Storage Accounts have a firewall feature, similar to Azure SQL Server.

Your task: Configure the firewall on your original storage account to allow access only from your IP address. Verify that you can still download the document dot txt file. Then, log into your VM and confirm that it cannot download the file.

This demonstrates how you can use network security to control access to your storage, even for publicly accessible blobs.

Good luck with the challenge!
