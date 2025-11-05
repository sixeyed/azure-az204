# Azure Files Storage - Exercises Narration

## Exercise 1: Create a File Share

Let's begin by creating the infrastructure we need for Azure Files.

First, we'll create a resource group to organize our resources. We're using the Azure CLI with the "az group create" command, specifying the name "labs-storage-files", adding our course tags, and selecting a location.

```
az group create -n labs-storage-files --tags courselabs=azure -l westeurope
```

Next, we need a storage account. Azure Files is a feature of Storage Accounts, just like blob storage. We'll use the "az storage account create" command with the Standard LRS SKU for locally redundant storage.

```
az storage account create -g labs-storage-files --sku Standard_LRS -n <storage-account-name>
```

Remember to use a globally unique name for your storage account. I'm using a placeholder here, but you'll need to substitute your actual storage account name.

Now that we have a storage account, let's create a file share. We'll use the "az storage share create" command to create a share called "labs".

```
az storage share create -n labs --account-name <storage-account-name>
```

Great. Our file share is now created with default settings for tier and quota.

## Exercise 2: Working with Files in the Portal

Let's switch to the Azure Portal to see our file share visually. Navigate to your storage account and select "File shares" from the left menu.

Click on the "labs" share we just created. Notice the tier and quota values - these are using defaults, but we can modify them if needed.

Now let's add some structure and content. Click "Add directory" and create a directory called "uploads". This works similar to blob containers - we can organize our files in a hierarchical structure.

Next, navigate into the uploads directory and click "Upload". Select the document.txt file from the lab folder on your local machine.

Once uploaded, click on the file to see its properties. You'll notice there's a URL for the file. Let's try accessing it directly with curl.

```
curl -o download.txt https://<storage-account-name>.file.core.windows.net/labs/uploads/document.txt
```

As you can see, we get an XML error message. Unlike blob storage where you can enable public access, file shares default to no public access. You would need to generate a SAS token at the account level to allow HTTP access.

But that's not the typical way to use file shares. Instead, we mount them to our filesystem.

## Exercise 3: Mounting the Share Locally

Let's mount the file share on our local machine. Back in the Portal, click the "Connect" button at the top of the file share view.

You'll see connection instructions for Windows, macOS, and Linux. These instructions include the mount command with your storage account name and key embedded.

For macOS, the command looks like this:

```
open smb://<storage-account-name>:<storage-account-key>@<storage-account-name>.file.core.windows.net/labs
```

For Linux, you would use the mount command with CIFS:

```
sudo mount -t cifs //<storage-account-name>.file.core.windows.net/labs /mnt/labs -o username=<storage-account-name>,password=<storage-account-key>
```

And for Windows, you can use the net use command.

After mounting, the share appears as a regular drive or directory on your system. Navigate to it and open the document.txt file. Try editing it and saving your changes.

Now go back to the Portal and open the same file. You'll see your changes immediately reflected. This demonstrates the real-time synchronization of Azure Files.

You can also edit the file in the Portal. Make a change, save it, and check your local mount point - you'll see the updates right away.

This is the power of Azure Files - multiple clients can access and modify the same files simultaneously.

## Exercise 4: Understanding Key Rotation

Authentication to file shares uses storage account keys. Let's look at how these keys work and why you might need to rotate them.

In the Portal, go to your storage account and click "Access keys" under Security + networking. You'll see two keys - key1 and key2. Both keys provide full access to the storage account.

We can also view these keys using the CLI:

```
az storage account keys list --account-name <storage-account-name>
```

The key you used to mount the share is key1. Now let's see what happens when we rotate this key.

```
az storage account keys renew --key primary -g labs-storage-files -n <storage-account-name>
```

After rotating the key, try to access the file from your local mount point. It fails. The old key is no longer valid, so your existing mount lost authentication.

This is an important security practice. If keys are compromised or shared, you should rotate them regularly. However, all clients will need to remount with the new key.

To reconnect, use the new key from the access keys page and remount the share.

Having two keys allows for zero-downtime key rotation. You can have clients use key1, rotate key2, update some clients to use key2, then rotate key1, and finally update the remaining clients.

## Exercise 5: Mounting in a Virtual Machine

Now let's see how to mount a file share in an Azure Virtual Machine. This is useful when your applications running in VMs need shared storage.

We can automate the mounting process using cloud-init, which runs scripts during VM provisioning.

First, we need to prepare a cloud-init script. Open the mount-share.sh file in the lab folder and update it with your storage account name and key:

```bash
#!/bin/bash
apt-get update
apt-get install -y cifs-utils
mkdir -p /mnt/labs
mount -t cifs //<storage-account-name>.file.core.windows.net/labs /mnt/labs -o username=<storage-account-name>,password=<storage-account-key>
```

This script installs the necessary tools, creates a mount point, and mounts the file share.

Now let's create a VM with this cloud-init script:

```
az vm create -g labs-storage-files -n vm01 --image UbuntuLTS --custom-data @labs/storage-files/cloud-init/mount-share.sh
```

Once the VM is created, connect to it via SSH:

```
ssh <vm-ip-address>
```

Now let's verify the file share is mounted:

```
ls /mnt/labs
```

You should see the uploads directory. Let's check our document:

```
cat /mnt/labs/uploads/document.txt
```

You'll see all the edits we made earlier. Now let's add another edit from the VM:

```
echo 'Edited from Azure VM.' >> /mnt/labs/uploads/document.txt
```

Exit the SSH session and go back to the Portal. Open the document.txt file again, and you'll see the new line added by the VM.

This demonstrates how Azure Files enables file sharing across different environments - your local machine, the Portal, and VMs all accessing the same data.

## Lab Challenge

Now it's time for the lab challenge. There are two tasks:

First, file shares have a capacity limit. When they're full, clients can't write more data. Your task is to increase the quota of your existing share. Hint: look at the "az storage share update" command.

Second, Azure Files supports a premium tier using SSD storage for better performance. Create a new premium file share with 100GB capacity. You'll need to explore what's different about premium storage accounts.

Take some time to work through these challenges, and check the hints or solution if you need guidance.

## Cleanup

When you're finished with the lab, remember to clean up your resources:

```
az group delete -y -n labs-storage-files --no-wait
```

This removes all the resources we created, including the storage account, file share, and virtual machine.

That concludes our Azure Files lab. You now understand how to create file shares, mount them across different platforms, and integrate them with Azure services.
