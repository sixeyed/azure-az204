# Virtual Machines - Windows: Exercises Narration

## Exercise 1: Explore Windows VMs in the Portal

Let's start by exploring what's different about Windows VMs compared to Linux VMs in the Azure Portal.

Open the Azure Portal and search for "Virtual Machine" to create a new resource. Once you're on the create page, change the image dropdown to select a Windows operating system.

Notice what changes immediately. The authentication model switches from SSH keys to username and password - Windows VMs don't typically use SSH, so we need password authentication instead.

Also look at the networking section. The default incoming ports now include port 3389, which is the Remote Desktop Protocol port. This is how we'll connect to our Windows VM.

Click through to the Disks section. Here you can see options for creating new virtual disks to attach to the VM. We'll do this programmatically in a moment, but it's useful to see the options available.

Don't create the VM through the portal - we'll use the CLI instead.

## Exercise 2: Find the Right VM Size

Now let's switch to the command line. First, we need to create a resource group for our VM resources.

Run the following command, using your preferred Azure region:

```
az group create -n labs-vm-win --tags courselabs=azure -l <your-location>
```

Windows is a more demanding operating system than Linux, so we need a VM with more resources. Let's find a VM size with 4 CPU cores and 16 GB of memory.

Run this query command. The syntax differs slightly between PowerShell and Bash due to escaping, so use the appropriate version for your shell:

```
az vm list-sizes -o table --query "[?numberOfCores==\`4\` && memoryInMb==\`16384\`]" --location "<your-location>"
```

You should see several options. Look for something from the D series - these are general-purpose VMs. A good choice would be Standard underscore D4s underscore v5.

## Exercise 3: Find the Windows Image

Before we can create a VM, we need to identify the exact OS image to use. Azure OS images are identified by a URN with four components: publisher, offer, SKU, and version.

For Windows, Microsoft is the publisher. Let's explore what's available.

First, list all the Windows Desktop offers:

```
az vm image list-offers --publisher MicrosoftWindowsDesktop --location <your-location> -o table
```

You'll see various Windows versions. We want Windows 11. Now let's see the available SKUs:

```
az vm image list-skus -l <your-location> -f windows-11 -p MicrosoftWindowsDesktop -o table
```

There are different editions - Pro, Enterprise, etc. Let's use Windows 11 Pro. Finally, let's see the specific image versions:

```
az vm image list --sku win11-22h2-pro -f windows-11 -p MicrosoftWindowsDesktop --location <your-location> -o table --all
```

This shows all the available image versions. You can use a specific version number, or just specify "latest" to get the most recent build.

## Exercise 4: Create the Windows VM

Now we have everything we need to create our Windows VM. We'll need to specify several parameters:

- The resource group name
- The VM name
- The image URN
- The VM size we found earlier
- Admin username and password
- A public DNS name so we can connect without remembering an IP address

The full URN for a Windows 11 image looks like this: MicrosoftWindowsDesktop colon windows-11 colon win11-22h2-pro colon latest

When you run the create command, Azure will validate your password. It needs to be strong - at least 12 characters with uppercase, lowercase, numbers, and special characters.

```
az vm create -l <your-location> -g labs-vm-win -n dev01 --image <image-urn> --size Standard_D4s_v5 --admin-username <username> --public-ip-address-dns-name <unique-dns-name> --admin-password <strong-password>
```

This will take several minutes - creating a Windows Desktop VM typically takes longer than a Linux Server VM because there's more to install and configure.

While it's running, switch back to the Portal and navigate to your resource group. You'll see several resources being created:

- The virtual machine itself
- A virtual network and subnet
- A network interface
- A public IP address
- A network security group
- An OS disk

Look at the Network Security Group and find the inbound security rule that allows port 3389. This is what enables Remote Desktop access to your VM.

## Exercise 5: Add a Data Disk

Once your VM is created, let's add a data disk. This is useful for storing data that should persist independently from the VM. If you delete the VM, you typically delete the OS disk too, but data disks can be retained.

We'll create a new 2 terabyte Premium SSD disk and attach it to the VM:

```
az vm disk attach -g labs-vm-win --vm-name dev01 --name dev01data --new --sku Premium_LRS --size-gb 2048
```

Premium storage uses fast solid-state disks in the datacenter, providing much better performance than standard disks. Keep in mind that disks are charged separately from VMs. Even when a VM is deallocated, you still pay for the storage, and large Premium disks can be expensive.

## Exercise 6: Connect and Install Tools

Now we're ready to connect to our VM using Remote Desktop.

If you're on Windows, use the built-in Remote Desktop Connection application. On Mac, install Microsoft Remote Desktop from the App Store. On Linux, a good option is Remmina.

Use the DNS name you specified earlier and your admin credentials to connect. You'll see the Windows desktop load - you're now logged into your cloud-based Windows machine.

Once connected, we need to install some development tools. There's a PowerShell script called setup dot ps1 in the lab folder. You can copy and paste it into the VM, or download it directly from the GitHub repository.

Open PowerShell as Administrator - this is important, as the script needs elevated privileges. Then run the setup script. This will install Git and Visual Studio Code, getting your development environment ready to use.

## Lab Challenge: Initialize the Data Disk

Here's your lab challenge. Open Windows Explorer on the VM and look at the available drives. You'll see the C drive, which is your OS disk. But where's the data disk we attached?

Check in the Azure Portal - you'll see the data disk is definitely attached to the VM. So why isn't it showing up in Windows Explorer?

The disk is attached at the hardware level, but Windows hasn't been told to use it yet. You need to initialize and format the disk before Windows will make it available as a drive letter.

Your task is to figure out how to initialize this disk and make it accessible in Windows. Look for disk management tools in Windows.

Once you've completed this, you'll have a fully configured Windows development VM with both OS and data storage ready to use.

## Cleanup

When you're finished with the lab, remember to clean up your resources to avoid ongoing charges:

```
az group delete -y -n labs-vm-win
```

This will delete the resource group and all the resources within it - the VM, disks, network resources, everything.

That completes our exploration of Windows Virtual Machines in Azure. You've learned how to create and configure Windows VMs, manage storage, and set up a development environment in the cloud.
