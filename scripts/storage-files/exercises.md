# Azure Files Storage - Exercises Narration

## Exercise 1: Create a File Share

Let's begin by creating the infrastructure we need for Azure Files.

First, we'll create a resource group to organize our resources. We're using the Azure CLI with the az group create command, specifying the name "labs-storage-files" with -n, adding our course tags with --tags courselabs=azure for tracking, and selecting West Europe as our location with -l westeurope.

Next, we need a storage account. Azure Files is a feature of Storage Accounts, just like blob storage - they're both services provided by the same storage infrastructure. We'll use the az storage account create command with -g labs-storage-files for the resource group, --sku Standard_LRS for locally redundant storage which gives us three copies of our data in a single datacenter, and -n with your storage account name. Remember to use a globally unique name for your storage account - it must be unique across all of Azure, and can only contain lowercase letters and numbers.

Now that we have a storage account, let's create a file share. We'll use the az storage share create command to create a share called "labs" with -n labs for the name and --account-name with your storage account name. Great. Our file share is now created with default settings for tier and quota - we can modify these later if needed, but the defaults are fine for getting started.

## Exercise 2: Working with Files in the Portal

Let's switch to the Azure Portal to see our file share visually and interact with it through the graphical interface. Navigate to your storage account by finding it in your resource group, and select "File shares" from the left menu under Data storage.

Click on the "labs" share we just created. Notice the tier and quota values displayed at the top - these are using defaults, but we can modify them if needed. The tier determines performance characteristics and pricing, while the quota sets the maximum size for the share.

Now let's add some structure and content. Click "Add directory" at the top and create a directory called "uploads". This works similar to blob containers - we can organize our files in a hierarchical structure just like a regular file system. This is one of the key differences from blob storage - file shares support true hierarchical directories, not just virtual ones.

Next, navigate into the uploads directory by clicking on it, and click "Upload" at the top. Select the document.txt file from your lab folder on your local machine and upload it. The upload happens through your browser, and you'll see a progress indicator.

Once uploaded, click on the file to see its properties. You'll notice there's a URL for the file displayed in the properties. Let's try accessing it directly with curl to see what happens. We're using curl with -o download.txt to save the output, followed by the full file URL like https://your-storage-account-name.file.core.windows.net/labs/uploads/document.txt.

As you can see, we get an XML error message indicating access is denied. Unlike blob storage where you can enable public access at the container level, file shares default to no public access and don't have an easy option to make files publicly accessible via HTTP. You would need to generate a SAS token at the account level to allow HTTP access to file shares.

But that's not the typical way to use file shares anyway. Instead, we mount them to our filesystem using standard file sharing protocols like SMB on Windows or CIFS on Linux. This is what makes Azure Files different from Blob Storage - it's designed to work like a network file share, not like web storage.

## Exercise 3: Mounting the Share Locally

Let's mount the file share on our local machine so we can access it like any other drive or directory. Back in the Portal, click the "Connect" button at the top of the file share view.

You'll see connection instructions for Windows, macOS, and Linux - Azure Files supports all major platforms. These instructions include the mount command with your storage account name and key embedded, making it easy to copy and paste.

For macOS, the command looks like this: open smb:// followed by your storage account name, colon, your storage account key, at symbol, your storage account name again, dot file dot core dot windows dot net, slash labs. This uses the SMB protocol which macOS supports natively.

For Linux, you would use the mount command with CIFS file system type: sudo mount -t cifs with double slash, your storage account name dot file dot core dot windows dot net slash labs, a space, your mount point like /mnt/labs, -o username equals your storage account name comma password equals your storage account key. You might need to install cifs-utils first if it's not already on your system.

And for Windows, you can use the net use command to map a network drive, specifying a drive letter and the UNC path to the file share.

After mounting using the appropriate command for your platform, the share appears as a regular drive or directory on your system. Navigate to it using your file explorer or terminal and open the document.txt file we uploaded earlier. Try editing it and saving your changes - make a modification to the text and save the file.

Now go back to the Portal and open the same file through the web interface. You'll see your changes immediately reflected. This demonstrates the real-time synchronization of Azure Files - changes made on one client appear immediately on all other clients.

You can also edit the file in the Portal. Click the Edit button, make a change to the text, save it, and then check your local mount point - you'll see the updates right away on your local machine. This is the power of Azure Files - multiple clients can access and modify the same files simultaneously, with changes synchronized in real-time. It's perfect for shared configuration files, logs, or any scenario where multiple systems need access to the same data.

## Exercise 4: Understanding Key Rotation

Authentication to file shares uses storage account keys by default. Let's look at how these keys work and why you might need to rotate them for security.

In the Portal, go to your storage account and click "Access keys" under Security + networking in the left menu. You'll see two keys - key1 and key2. Both keys provide full access to the storage account - they're equivalent in terms of permissions. This dual-key system exists to support zero-downtime key rotation.

We can also view these keys using the CLI with az storage account keys list followed by --account-name with your storage account name. You'll see both keys displayed with their values and permissions.

The key you used to mount the share is key1 - that's the default key returned by the connection instructions. Now let's see what happens when we rotate this key for security purposes.

We're using az storage account keys renew with --key primary to regenerate the first key, -g labs-storage-files for the resource group, and -n for your storage account name. This generates a completely new key1, invalidating the old one.

After rotating the key, try to access files from your local mount point. It fails with an authentication error. The old key is no longer valid, so your existing mount loses authentication. The connection breaks because the credentials are now wrong.

This is an important security practice for managing storage accounts. If keys are compromised or shared inappropriately, you should rotate them regularly. However, all clients will need to remount with the new key after rotation. There's a brief period where access is interrupted while you update clients.

To reconnect, use the new key from the access keys page and remount the share with the updated credentials. Your access will be restored with the new key.

Having two keys allows for zero-downtime key rotation using a clever process. You can have clients use key1, rotate key2 which doesn't affect current connections, update some clients to use the new key2, then rotate key1, and finally update the remaining clients to the new key1. This way, you always have at least one valid key during the rotation process.

## Exercise 5: Mounting in a Virtual Machine

Now let's see how to mount a file share in an Azure Virtual Machine. This is useful when your applications running in VMs need shared storage that multiple instances can access.

We can automate the mounting process using cloud-init, which runs scripts during VM provisioning. This means the file share is automatically available when the VM starts, without manual intervention.

First, we need to prepare a cloud-init script. Open the mount-share.sh file in your lab folder and update it with your storage account name and key. The script does several things: it runs apt-get update to refresh package lists, installs cifs-utils which provides the tools needed to mount file shares, creates a mount point directory at /mnt/labs, and mounts the file share using the mount command with CIFS specifying the share path and credentials.

Now let's create a VM with this cloud-init script using az vm create with -g labs-storage-files for the resource group, -n vm01 as the VM name, --image UbuntuLTS for the operating system, and --custom-data pointing to your mount-share.sh file with @ symbol to read from file. The VM is created and the script runs automatically during first boot, mounting the file share.

Once the VM is created, connect to it via SSH using ssh followed by the VM's IP address from the command output.

Now let's verify the file share is mounted correctly. Run ls /mnt/labs to list the contents. You should see the uploads directory we created earlier. This confirms the share is mounted and accessible.

Let's check our document by running cat /mnt/labs/uploads/document.txt. You'll see all the edits we made earlier from both the Portal and your local machine. The VM sees the same data because it's accessing the same Azure file share.

Now let's add another edit from the VM to demonstrate the shared nature of the storage. Run echo 'Edited from Azure VM.' followed by two greater-than symbols to append, then /mnt/labs/uploads/document.txt. This adds a new line to the file from the VM.

Exit the SSH session to return to your local machine. Go back to the Portal, navigate to your file share, find the uploads directory, and open the document.txt file again. You'll see the new line added by the VM appearing in the Portal. This demonstrates how Azure Files enables file sharing across different environments - your local machine, the Portal web interface, and VMs all accessing the same data with changes visible everywhere instantly.

## Lab Challenge

Now it's time for the lab challenge. There are two tasks to complete on your own.

First, file shares have a capacity limit defined by the quota setting. When they're full, clients can't write more data and will receive errors. Your task is to increase the quota of your existing share to allow more data. Hint: look at the az storage share update command in the CLI documentation to see how to modify share properties. You can also do this through the Portal in the share's properties.

Second, Azure Files supports a premium tier using SSD storage for better performance compared to the standard tier which uses HDD storage. Create a new premium file share with 100GB capacity. You'll need to explore what's different about premium storage accounts - premium file shares require a special type of storage account called FileStorage, not the general-purpose accounts we've been using. The premium tier provides guaranteed IOPS and throughput, making it suitable for performance-sensitive workloads.

Take some time to work through these challenges, experimenting with the CLI and Portal. Check the hints or solution files if you need guidance, but try to figure it out on your own first.

## Cleanup

When you're finished with the lab, remember to clean up your resources to avoid ongoing charges.

We're using az group delete with -y to confirm without prompting, -n labs-storage-files to specify the resource group, and --no-wait to return immediately without waiting for completion. This removes all the resources we created, including the storage account, file share, and virtual machine. The deletion happens asynchronously in the background.

That concludes our Azure Files lab. You now understand how to create file shares, mount them across different platforms using SMB/CIFS, manage access with storage account keys and key rotation, and integrate them with Azure services like Virtual Machines. Azure Files provides enterprise-grade shared storage that works just like traditional file servers but with cloud scale and reliability.
