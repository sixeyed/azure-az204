# Azure Storage Accounts - Exercises Narration

## Exercise 1: Exploring Storage Account Options

Let's start by exploring what options are available when creating a Storage Account.

We're opening the Azure Portal and creating a new resource. Search for "Storage Account" and take a look at the configuration options available in the creation wizard.

First, you'll notice the name field. Storage account names must be globally unique across all of Azure - not just unique to your subscription, but globally unique across every Azure customer worldwide. The naming rules are quite strict: lowercase letters and numbers only, between 3 and 24 characters. No special characters, no uppercase, no hyphens. This can make finding an available name challenging.

Next, look at the region selection. This is important because it determines where your data is physically stored. Choose a region close to your users or applications for the best performance and lowest latency. The region also affects pricing, with some regions costing more than others.

You'll also see options for performance levels - Standard or Premium. Standard uses traditional hard disk drives which are fine for most workloads, while Premium uses solid-state drives for higher performance scenarios like databases or applications that need consistent low-latency access. Premium storage costs significantly more but provides much better IOPS.

Finally, there's the redundancy level we discussed earlier - LRS for locally redundant storage, ZRS for zone-redundant storage, or GRS for geo-redundant storage. Each offers different levels of protection at different price points. LRS is the cheapest but only protects against drive failures. ZRS protects against datacenter failures within a region. GRS replicates your data to a secondary region hundreds of miles away for disaster recovery.

## Exercise 2: Creating a Storage Account with Azure CLI

Now let's create a storage account using the Azure CLI. First, we'll create a resource group to organize our resources.

We're running az group create with the name "labs-storage", setting the location to West Europe, and adding a tag "courselabs=azure" to help us track our lab resources. This tag is useful for cost tracking and resource cleanup later.

This creates a resource group named "labs-storage" in the West Europe region with a tag to help us track our lab resources.

Before we create the storage account, let's check the help documentation by running az storage account create with the --help flag. This is always a good practice when you're learning a new command.

Take a moment to review the available parameters in the help output. Notice the SKU parameter - this is particularly interesting because it combines both performance and redundancy settings into a single value. Instead of setting performance and redundancy separately like you do in the Portal, the CLI uses SKU codes that specify both.

For example, Premium_LRS is premium performance with local redundancy, while Standard_GRS is standard performance with geo redundancy. The SKU naming follows a pattern: performance level underscore redundancy type.

Now, let's create a zone-redundant storage account with standard performance. We're using az storage account create with the resource group "labs-storage", location West Europe, SKU set to Standard_ZRS for zone-redundant storage, and a unique name that you'll need to provide. Remember to replace the placeholder with your own globally unique name - something like "mystorageYYYYMMDD" with today's date often works well.

The command takes a minute or two to complete as Azure provisions your storage account across multiple availability zones for redundancy.

## Exercise 3: Working with Blob Storage

Now that we have a storage account, let's explore blob storage. We're opening the newly created storage account in the Portal to see what we can do with it.

One storage account can support multiple types of storage - blobs, files, queues, and tables. Today we'll focus on Blob storage, which stands for Binary Large Objects. This is essentially file storage in the cloud, optimized for storing unstructured data like documents, images, videos, backups, and logs.

Blob storage organizes files in containers. Think of containers like folders or buckets, but with one important limitation: blob storage is not hierarchical. You cannot have containers inside other containers - it's a flat namespace at the container level. However, you can use forward slashes in blob names to simulate a folder structure within a container, which many tools will display as folders for convenience.

Let's upload a file to test this out. In the Storage Account blade, you'll see an Upload option in the main menu. We're clicking that, browsing to the document.txt file in the labs folder, and uploading it. The upload wizard is straightforward - just select your file and specify options.

You'll need to create a container for the blob since we don't have any yet. Let's call it "drops" - this will be our container for uploaded files. We're entering that name when prompted and creating the container.

## Exercise 4: Public vs Private Access

Now let's explore access control, which is crucial for securing your storage. We're clicking on Storage browser in the left navigation and opening Blob containers to see our newly created container and uploaded file.

Opening the "drops" container shows our document.txt file. Clicking on it displays the overview page with properties including a URL - this is the direct link to your blob. The URL format follows a pattern: your storage account name, followed by "blob.core.windows.net", then the container name, and finally the blob name.

Let's try to access it from the command line. We're copying that URL and attempting to download the file using curl, specifying an output filename and the full blob URL.

The command appears to succeed - curl doesn't show any obvious errors. But let's check what was actually downloaded by examining the contents of the file.

Interesting! Instead of your document content, you're seeing an XML error message. The error states that public access is not permitted on this container. This is because new blob containers default to private access - a security-first approach. Even though you have the URL and you own the storage account, anonymous access is not permitted without explicitly enabling it.

Let's fix this. We're browsing to the drops container in the Portal and selecting "Change access level" from the menu.

You have two options for public access. Blob access allows anyone with the URL to download that specific file, but they can't list what other files exist in the container. Container access allows anyone to list all contents and download any blob - essentially making the entire container public like a web server directory.

For this exercise, we're setting it to blob-level access, which gives us public read access to files when we have the URL, but keeps the container listing private.

Now we're trying the download again with curl, using a different output filename to see the new result. This time when we examine the file contents, we can see the correct document text. Success! The blob is now publicly accessible because we explicitly enabled that access level.

## Exercise 5: Storage for VM Disks

Blob storage has another interesting use case beyond just storing files - it can store virtual machine disks. While Azure uses managed disks by default today, which handle all the storage details for you, you can choose to use unmanaged disks stored in your own storage account. This gives you more control over the storage configuration and lets you manage VM disks alongside other data in your storage account.

This gives you more control over the storage configuration and lets you manage VM disks alongside other data.

First, let's create a premium storage account specifically for our VM disks. We're running az storage account create with the resource group "labs-storage", location West Europe, SKU set to Premium_LRS for premium locally redundant storage, and a unique name for the disk storage account. Premium storage is required for production VM workloads that need consistent high performance.

Next, we need a container for the disks. In blob storage terminology, even VM disks are stored as blobs - specifically, page blobs in VHD format. We're creating a container called "vm-disks" within our premium storage account using az storage container create.

Now we can create a VM that uses this storage. This is different from the default VM creation - we need to explicitly tell Azure to use unmanaged disks and specify where to store them. We're running az vm create with the location West Europe, resource group "labs-storage", VM name "vm01", image set to Ubuntu LTS, and here's the important part: a VM size that supports premium storage like Standard_D2as_v5, the --use-unmanaged-disk flag which tells Azure not to create managed disks, --storage-container-name pointing to our vm-disks container, and --storage-account specifying our premium storage account.

Note that we need to use a VM size that supports premium storage - not all sizes do. The "s" in the size name typically indicates premium storage support.

Once the VM is created, let's browse to the storage account in the Portal. We're opening the vm-disks container and you'll see your VM's OS disk stored as a VHD blob. The file name will include the VM name and a unique identifier, and it's quite large - typically 30GB or more for a Linux VM.

These unmanaged disks don't appear as separate resources in the Portal like managed disks do. They're simply blobs in your storage container. This means you manage their lifecycle, backups, and snapshots manually, but you also have complete control over the storage tier, replication, and organization.

## Lab Challenge

Now it's time for a challenge. Storage Accounts have a firewall feature, similar to what we saw with Azure SQL Server. The firewall lets you restrict which IP addresses or networks can access your storage account.

Your task: Configure the firewall on your original storage account to allow access only from your IP address. You'll need to find the firewall settings in the Portal under the Networking section of the storage account. Add your current public IP address to the allow list.

Then verify that you can still download the document.txt file using curl from your local machine - this should work because your IP is on the allow list.

Next, log into your VM using SSH - the VM was created with a public IP and SSH access enabled. Once connected to the VM, try to download the document.txt file using curl from inside the VM. This should fail because the VM's IP address is not on the allow list.

This demonstrates how you can use network security to control access to your storage, even for publicly accessible blobs. The blob might be set to public access level, but the storage account firewall provides an additional layer of security by restricting which networks can reach it.

Good luck with the challenge! This is a practical exercise that demonstrates defense in depth - using multiple layers of security rather than relying on a single control.
