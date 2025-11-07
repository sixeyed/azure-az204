# Azure Files Storage

## Reference

Azure Files is a storage service which you can mount into your filesystem using the standard SMB protocol for network file shares. It's a good way to share files between components in the cloud and on-premises. The documentation covers everything from basic file share creation to advanced features like premium tiers and Azure File Sync. The command line interface provides complete control through az storage share and az storage file commands, which we'll be using throughout these exercises.

## Create a File Share

Azure Files is a feature of a Storage Account, so we'll start by creating the infrastructure we need.

**Create the Resource Group**: First, we'll create a resource group to organize our resources. We're using the Azure CLI with az group create, specifying the name "labs-storage-files", adding our course tags with courselabs equals azure for tracking, and selecting West Europe as our location. These tags help you track and manage resources that belong to specific projects or learning exercises.

**Create the Storage Account**: Next, we need a storage account. Azure Files is a feature of Storage Accounts, just like blob storage - they're both services provided by the same storage infrastructure. We'll use az storage account create with the resource group labs-storage-files, SKU Standard_LRS for locally redundant storage which gives us three copies of our data in a single datacenter, and a unique storage account name. Remember to use a globally unique name for your storage account - it must be unique across all of Azure, and can only contain lowercase letters and numbers.

**Create the File Share**: Now that we have a storage account, let's create a file share. We'll use az storage share create to create a share called "labs" with the account name parameter pointing to your storage account. Our file share is now created with default settings for tier and quota - we can modify these later if needed, but the defaults are fine for getting started with the basics.

**Check in Portal**: Let's check the share in the Portal to see what we've created. Navigate to your storage account and select File shares from the left menu under Data storage. You'll see the tier and quota have used the default values - these determine performance characteristics and maximum size respectively.

**Work with Files**: Open the share and you'll see you can work with files in a similar way to blobs. We're creating a new directory called "uploads" - this works similar to blob containers, but file shares support true hierarchical directories, not just virtual ones. This is one of the key differences from blob storage - file shares work like real file systems with nested folders.

**Upload a File**: Next, navigate into the uploads directory by clicking on it, and click Upload at the top. Select the document.txt file from your lab folder on your local machine and upload it. The upload happens through your browser with a progress indicator.

**Try Direct Access**: Once uploaded, click on the file to see its properties. You'll notice there's a URL for the file. Let's try accessing it directly with curl to see what happens. We're using curl with the save to file option, followed by the full file URL. As you can see, we get an XML error message indicating access is denied. Unlike blob storage where you can enable public access at the container level, file shares default to no public access and don't have an easy option to make files publicly accessible via HTTP.

**Understanding File Share Access**: You would need to generate a SAS token at the account level to allow HTTP access to file shares. But that's not the typical way to use file shares anyway. Instead, we mount them to our filesystem using standard file sharing protocols like SMB on Windows or CIFS on Linux. This is what makes Azure Files different from Blob Storage - it's designed to work like a network file share, not like web storage.

## Mounting the share & rotating keys

Let's mount the file share on our local machine so we can access it like any other drive or directory.

**Get Mount Instructions**: Back in the Portal, click the Connect button at the top of the file share view. You'll see connection instructions for Windows, macOS, and Linux - Azure Files supports all major platforms. These instructions include the mount command with your storage account name and key embedded, making it easy to copy and paste.

**Platform-Specific Mounting**: For macOS, the command uses the open command with the SMB protocol, including your credentials in the URL. For Linux, you would use the mount command with CIFS file system type, which might require installing cifs-utils first if it's not already on your system. For Windows, you can use the net use command to map a network drive, specifying a drive letter and the UNC path to the file share.

**Access Mounted Share**: After mounting using the appropriate command for your platform, the share appears as a regular drive or directory on your system. Navigate to it using your file explorer or terminal and open the document.txt file we uploaded earlier. Try editing it and saving your changes - make a modification to the text and save the file.

**Verify Changes**: Now go back to the Portal and open the same file through the web interface. You'll see your changes immediately reflected. This demonstrates the real-time synchronization of Azure Files - changes made on one client appear immediately on all other clients accessing the same share.

**Edit in Portal**: You can also edit the file in the Portal. Click the Edit button, make a change to the text, save it, and then check your local mount point - you'll see the updates right away on your local machine. This is the power of Azure Files - multiple clients can access and modify the same files simultaneously, with changes synchronized in real-time. It's perfect for shared configuration files, logs, or any scenario where multiple systems need access to the same data.

**Understanding Authentication**: Authentication to file shares uses storage account keys by default. Let's look at how these keys work and why you might need to rotate them for security. In the Portal, go to your storage account and click Access keys under Security and networking in the left menu. You'll see two keys - key1 and key2. Both keys provide full access to the storage account - they're equivalent in terms of permissions. This dual-key system exists to support zero-downtime key rotation.

**View Keys with CLI**: We can also view these keys using the CLI with az storage account keys list followed by your storage account name. You'll see both keys displayed with their values and permissions.

**Rotate a Key**: The key you used to mount the share is key1 - that's the default key returned by the connection instructions. Now let's see what happens when we rotate this key for security purposes. We're using az storage account keys renew with the key parameter set to primary to regenerate the first key, resource group labs-storage-files, and your storage account name. This generates a completely new key1, invalidating the old one.

**Test After Rotation**: After rotating the key, try to access files from your local mount point. It fails with an authentication error. The old key is no longer valid, so your existing mount loses authentication. The connection breaks because the credentials are now wrong.

**Zero-Downtime Rotation**: This is an important security practice for managing storage accounts. If keys are compromised or shared inappropriately, you should rotate them regularly. However, all clients will need to remount with the new key after rotation. Having two keys allows for zero-downtime key rotation using a clever process. You can have clients use key1, rotate key2 which doesn't affect current connections, update some clients to use the new key2, then rotate key1, and finally update the remaining clients to the new key1. This way, you always have at least one valid key during the rotation process.

## Mount the share in a VM

Now let's see how to mount a file share in an Azure Virtual Machine. This is useful when your applications running in VMs need shared storage that multiple instances can access.

**Automate with Cloud-Init**: We can automate the mounting process using cloud-init, which runs scripts during VM provisioning. This means the file share is automatically available when the VM starts, without manual intervention.

**Prepare the Script**: First, we need to prepare a cloud-init script. Open the mount-share.sh file in your lab folder and update it with your storage account name and key. The script does several things: it runs apt-get update to refresh package lists, installs cifs-utils which provides the tools needed to mount file shares, creates a mount point directory at /mnt/labs, and mounts the file share using the mount command with CIFS specifying the share path and credentials.

**Create VM with Cloud-Init**: Now let's create a VM with this cloud-init script using az vm create with resource group labs-storage-files, VM name vm01, image UbuntuLTS for the operating system, and custom-data pointing to your mount-share.sh file with the @ symbol to read from file. The VM is created and the script runs automatically during first boot, mounting the file share.

**Verify the Mount**: Once the VM is created, connect to it via SSH using the VM's IP address from the command output. Now let's verify the file share is mounted correctly. Run ls /mnt/labs to list the contents. You should see the uploads directory we created earlier. This confirms the share is mounted and accessible.

**Check File Contents**: Let's check our document by running cat /mnt/labs/uploads/document.txt. You'll see all the edits we made earlier from both the Portal and your local machine. The VM sees the same data because it's accessing the same Azure file share.

**Add Edit from VM**: Now let's add another edit from the VM to demonstrate the shared nature of the storage. Use echo to append a new line to the file. This adds a new line to the file from the VM.

**Verify Everywhere**: Exit the SSH session to return to your local machine. Go back to the Portal, navigate to your file share, find the uploads directory, and open the document.txt file again. You'll see the new line added by the VM appearing in the Portal. This demonstrates how Azure Files enables file sharing across different environments - your local machine, the Portal web interface, and VMs all accessing the same data with changes visible everywhere instantly.

## Lab

Now it's time for the lab challenge. There are two tasks to complete on your own.

**Increase Quota**: First, file shares have a capacity limit defined by the quota setting. When they're full, clients can't write more data and will receive errors. Your task is to increase the quota of your existing share to allow more data. Hint: look at the az storage share update command in the CLI documentation to see how to modify share properties. You can also do this through the Portal in the share's properties.

**Create Premium Share**: Second, Azure Files supports a premium tier using SSD storage for better performance compared to the standard tier which uses HDD storage. Create a new premium file share with 100GB capacity. You'll need to explore what's different about premium storage accounts - premium file shares require a special type of storage account called FileStorage, not the general-purpose accounts we've been using. The premium tier provides guaranteed IOPS and throughput, making it suitable for performance-sensitive workloads.

**Explore on Your Own**: Take some time to work through these challenges, experimenting with the CLI and Portal. Check the hints or solution files if you need guidance, but try to figure it out on your own first.

## Cleanup

When you're finished with the lab, remember to clean up your resources to avoid ongoing charges.

**Delete Resource Group**: We're using az group delete with -y to confirm without prompting, -n labs-storage-files to specify the resource group, and --no-wait to return immediately without waiting for completion. This removes all the resources we created, including the storage account, file share, and virtual machine. The deletion happens asynchronously in the background.

That concludes our Azure Files lab. You now understand how to create file shares, mount them across different platforms using SMB/CIFS, manage access with storage account keys and key rotation, and integrate them with Azure services like Virtual Machines. Azure Files provides enterprise-grade shared storage that works just like traditional file servers but with cloud scale and reliability.
