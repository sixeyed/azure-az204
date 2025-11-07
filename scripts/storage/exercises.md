# Azure Storage Accounts

## Reference

Storage Accounts are a managed storage service for data which you can make publicly accessible or restricted to users or other Azure services. Data is replicated in multiple locations for high availability, and you can choose different levels of performance. The documentation covers everything from basic storage configurations to advanced features like geo-replication and data redundancy. The command line interface gives you complete control through the az storage commands, which we'll be using extensively in these exercises.

## Explore Storage Account options

Let's start by exploring what options are available when creating a Storage Account.

**Navigate to the Portal**: We're opening the Azure Portal and creating a new resource. Search for "Storage Account" and take a look at the configuration options available in the creation wizard before making any choices.

**Naming Requirements**: First, you'll notice the name field. Storage account names must be globally unique across all of Azure - not just unique to your subscription, but globally unique across every Azure customer worldwide. The naming rules are strict: lowercase letters and numbers only, between 3 and 24 characters. No special characters, no uppercase, no hyphens. This can make finding an available name challenging, which is why you'll often see timestamps or random numbers appended to storage account names.

**Region Selection**: The region selection is important because it determines where your data is physically stored. Choose a region close to your users or applications for the best performance and lowest latency. The region also affects pricing, with some regions costing more than others due to local infrastructure costs and market conditions.

**Performance Tiers**: You'll also see options for performance levels - Standard or Premium. Standard uses traditional hard disk drives which are fine for most workloads, providing good performance at reasonable cost. Premium uses solid-state drives for higher performance scenarios like databases or applications that need consistent low-latency access. Premium storage costs significantly more but provides much better IOPS and throughput.

**Redundancy Levels**: Finally, there's the redundancy level we'll discuss throughout this lab. Locally Redundant Storage - LRS - means the data is replicated three times within a single datacenter, protecting against drive and rack failures but not datacenter-wide disasters. Zone Redundant Storage - ZRS - replicates across three availability zones within a single region, providing protection against datacenter failures. Geo-Redundant Storage - GRS - replicates your data to a secondary region hundreds of miles away for true disaster recovery. Each offers different levels of protection at different price points. LRS is the cheapest but only protects against drive failures, ZRS protects against datacenter failures within a region, and GRS provides full geographic redundancy.

## Create a storage account

Now let's create a storage account using the Azure CLI. First, we'll create a resource group to organize our resources.

**Create a Resource Group**: We're running az group create with the name "labs-storage", setting the location to West Europe, and adding a tag "courselabs=azure" to help us track our lab resources. This tag is useful for cost tracking and resource cleanup later - you can filter and find all resources associated with this course by searching for this tag.

**Explore the Help Documentation**: Before we create the storage account, let's check the help documentation by running az storage account create with the help flag. This is always a good practice when you're learning a new command - it shows you all available parameters and their purposes.

**Understanding SKU Parameter**: Take a moment to review the available parameters in the help output. Notice the SKU parameter - this is particularly interesting because it combines both performance and redundancy settings into a single value. Instead of setting performance and redundancy separately like you do in the Portal, the CLI uses SKU codes that specify both. For example, Premium_LRS is premium performance with local redundancy, while Standard_GRS is standard performance with geo redundancy. The SKU naming follows a pattern: performance level underscore redundancy type.

**Create the Storage Account**: Now, let's create a zone-redundant storage account with standard performance. We're using az storage account create with the resource group "labs-storage", location West Europe, SKU set to Standard_ZRS for zone-redundant storage, and a unique name that you'll need to provide. Remember to replace the placeholder with your own globally unique name - something like "mystorageYYYYMMDD" with today's date often works well. The command takes a minute or two to complete as Azure provisions your storage account across multiple availability zones for redundancy.

## Upload and download blobs

Now that we have a storage account, let's explore blob storage.

**Navigate to the Storage Account**: We're opening the newly created storage account in the Portal to see what we can do with it.

**Understanding Storage Services**: One storage account can support multiple types of storage - blobs, files, queues, and tables. Today we'll focus on Blob storage, which stands for Binary Large Objects. This is essentially file storage in the cloud, optimized for storing unstructured data like documents, images, videos, backups, and logs.

**Container Organization**: Blob storage organizes files in containers. Think of containers like folders or buckets, but with one important limitation: blob storage is not hierarchical. You cannot have containers inside other containers - it's a flat namespace at the container level. However, you can use forward slashes in blob names to simulate a folder structure within a container, which many tools will display as folders for convenience.

**Upload Your First File**: Let's upload a file to test this out. In the Storage Account blade, you'll see an Upload option in the main menu. We're clicking that, browsing to the document.txt file in the labs folder, and uploading it. The upload wizard is straightforward - just select your file and specify options.

**Create a Container**: You'll need to create a container for the blob since we don't have any yet. Let's call it "drops" - this will be our container for uploaded files. We're entering that name when prompted and creating the container.

**Access Control Fundamentals**: Now let's explore access control, which is crucial for securing your storage. We're clicking on Storage browser in the left navigation and opening Blob containers to see our newly created container and uploaded file.

**Understanding Blob URLs**: Opening the "drops" container shows our document.txt file. Clicking on it displays the overview page with properties including a URL - this is the direct link to your blob. The URL format follows a pattern: your storage account name, followed by "blob.core.windows.net", then the container name, and finally the blob name.

**Testing Public Access**: Let's try to access it from the command line. We're copying that URL and attempting to download the file using curl, specifying an output filename and the full blob URL. The command appears to succeed - curl doesn't show any obvious errors. But let's check what was actually downloaded by examining the contents of the file.

**Security-First Approach**: Interesting! Instead of your document content, you're seeing an XML error message. The error states that public access is not permitted on this container. This is because new blob containers default to private access - a security-first approach. Even though you have the URL and you own the storage account, anonymous access is not permitted without explicitly enabling it.

**Changing Access Levels**: Let's fix this. We're browsing to the drops container in the Portal and selecting "Change access level" from the menu. You have two options for public access. Blob access allows anyone with the URL to download that specific file, but they can't list what other files exist in the container. Container access allows anyone to list all contents and download any blob - essentially making the entire container public like a web server directory.

**Enable Blob-Level Access**: For this exercise, we're setting it to blob-level access, which gives us public read access to files when we have the URL, but keeps the container listing private. Now we're trying the download again with curl, using a different output filename to see the new result. This time when we examine the file contents, we can see the correct document text. Success! The blob is now publicly accessible because we explicitly enabled that access level.

## Storage for VM disks

Blob storage has another interesting use case beyond just storing files - it can store virtual machine disks.

**Managed vs Unmanaged Disks**: While Azure uses managed disks by default today, which handle all the storage details for you, you can choose to use unmanaged disks stored in your own storage account. This gives you more control over the storage configuration and lets you manage VM disks alongside other data in your storage account.

**Create Premium Storage**: First, let's create a premium storage account specifically for our VM disks. We're running az storage account create with the resource group "labs-storage", location West Europe, SKU set to Premium_LRS for premium locally redundant storage, and a unique name for the disk storage account. Premium storage is required for production VM workloads that need consistent high performance and low latency.

**Create Container for Disks**: Next, we need a container for the disks. In blob storage terminology, even VM disks are stored as blobs - specifically, page blobs in VHD format. We're creating a container called "vm-disks" within our premium storage account using az storage container create.

**Create VM with Unmanaged Disk**: Now we can create a VM that uses this storage. This is different from the default VM creation - we need to explicitly tell Azure to use unmanaged disks and specify where to store them. We're running az vm create with the location West Europe, resource group "labs-storage", VM name "vm01", image set to Ubuntu LTS, and here's the important part: a VM size that supports premium storage like Standard_D2as_v5, the use-unmanaged-disk flag which tells Azure not to create managed disks, storage-container-name pointing to our vm-disks container, and storage-account specifying our premium storage account.

**VM Size Requirements**: Note that we need to use a VM size that supports premium storage - not all sizes do. The "s" in the size name typically indicates premium storage support, which is important when working with premium storage accounts.

**Inspect the VHD Blob**: Once the VM is created, let's browse to the storage account in the Portal. We're opening the vm-disks container and you'll see your VM's OS disk stored as a VHD blob. The file name will include the VM name and a unique identifier, and it's quite large - typically 30GB or more for a Linux VM.

**Understanding Unmanaged Disk Management**: These unmanaged disks don't appear as separate resources in the Portal like managed disks do. They're simply blobs in your storage container. This means you manage their lifecycle, backups, and snapshots manually, but you also have complete control over the storage tier, replication, and organization.

## Lab

Now it's time for a challenge. Storage Accounts have a firewall feature, similar to what we saw with Azure SQL Server. The firewall lets you restrict which IP addresses or networks can access your storage account.

**Your Task**: Configure the firewall on your original storage account to allow access only from your IP address. You'll need to find the firewall settings in the Portal under the Networking section of the storage account. Add your current public IP address to the allow list.

**Verify Local Access**: Then verify that you can still download the document.txt file using curl from your local machine - this should work because your IP is on the allow list.

**Test from VM**: Next, log into your VM using SSH - the VM was created with a public IP and SSH access enabled. Once connected to the VM, try to download the document.txt file using curl from inside the VM. This should fail because the VM's IP address is not on the allow list.

**Defense in Depth**: This demonstrates how you can use network security to control access to your storage, even for publicly accessible blobs. The blob might be set to public access level, but the storage account firewall provides an additional layer of security by restricting which networks can reach it. This is a practical exercise that demonstrates defense in depth - using multiple layers of security rather than relying on a single control.

## Cleanup

When you're finished with the lab, remember to clean up your resources to avoid ongoing charges.

**Delete the Resource Group**: We're using az group delete with -y to confirm without prompting, -n labs-storage to specify the resource group, and --no-wait to return immediately without waiting for completion. This removes all the resources we created, including the storage accounts, containers, blobs, and virtual machine. The deletion happens asynchronously in the background, which is useful when cleaning up large resource groups.
