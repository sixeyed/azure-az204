# Virtual Machines - Windows

## Reference

Virtual Machines are useful as workstation machines as well as servers, and having a dev machine you can access from anywhere is incredibly practical. You can set up a powerful VM with all the dev tools you need, and only pay when you're actually using it. Windows VMs give you full control over the operating system and installed software, making them perfect for scenarios where you need specific OS-level dependencies or specialized development tools. The Azure VM documentation covers everything from basic provisioning to advanced features like VM Scale Sets and availability zones, while the Azure CLI provides complete control through the az vm commands.

## Explore Windows VMs in the Portal

Let's start by exploring what's different about Windows VMs compared to Linux VMs in the Azure Portal.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Virtual Machine" to create a new resource. Once you're on the create page, change the image dropdown to select a Windows operating system.

**Authentication Changes**: Notice what changes immediately when you select Windows. The authentication model switches from SSH keys to username and password - Windows VMs don't typically use SSH by default, so Azure changes the authentication options to match what Windows expects. You'll need to provide both a username and a strong password that meets Microsoft's complexity requirements.

**Default Port Configuration**: Also look at the networking section near the bottom. The default incoming ports now include port 3389, which is the Remote Desktop Protocol port. This is how we'll connect to our Windows VM - RDP is to Windows what SSH is to Linux, providing remote terminal access.

**Disk Options**: Click through to the Disks section. Here you can see options for creating new virtual disks to attach to the VM beyond just the OS disk. We'll explore this programmatically in a moment, but it's useful to see the options available - you can add multiple data disks, choose different performance tiers for each disk, and configure caching options.

Don't create the VM through the portal - we'll use the CLI instead for better repeatability and to understand exactly what's being created.

---

## Create a Windows VM with the CLI

Now let's switch to the command line and start building our Windows VM.

**Create the Resource Group**: First, we need to create a resource group for our VM resources. We're running az group create with the name "labs-vm-win", adding our "courselabs=azure" tag for tracking, and specifying your preferred Azure location.

**Find a Larger VM Size**: Windows is a more demanding operating system than Linux, so we need a VM with more resources to run smoothly. Let's find a VM size with 4 CPU cores and 16 GB of memory, which provides a good balance for Windows desktop workloads.

We're running az vm list-sizes with table output, and here's the interesting part - we're using a JMESPath query to filter the results. The query syntax differs slightly between PowerShell and Bash due to escaping requirements, so make sure to use the appropriate version for your shell. In the query, we're looking for VMs where numberOfCores equals 4 and memoryInMb equals 16384 - that's 16 GB in megabytes. We're also specifying your location to ensure we get sizes that are actually available in your region.

**Understanding VM Series**: You should see several options in the results. Look for something from the D series - these are general-purpose VMs that balance compute, memory, and network capabilities. A good choice would be Standard_D4s_v5 if available - the "s" indicates it supports premium storage, and "v5" is the latest generation with better performance per dollar.

**Understanding Image URNs**: Before we can create a VM, we need to identify the exact OS image to use. Azure OS images are identified by a URN - a unified resource name - with four components: publisher, offer, SKU, and version. For Windows, Microsoft is the publisher - specifically "MicrosoftWindowsDesktop" for client operating systems like Windows 10 and 11.

**Find Available Offers**: First, we're listing all the Windows Desktop offers using az vm image list-offers with the publisher "MicrosoftWindowsDesktop", your location, and table output for easy reading. You'll see various Windows versions in the results - Windows 10, Windows 11, and different variants. We want to use Windows 11 for this lab since it's the current version.

**Find Available SKUs**: Now let's see the available SKUs for Windows 11 using az vm image list-skus. There are different editions available - Pro, Enterprise, different builds and versions. Let's use Windows 11 Pro for this exercise. Finally, let's see the specific image versions using az vm image list with the SKU "win11-22h2-pro" and the all flag to show all versions not just the most recent. This shows all the available image versions with dates and versions. You can use a specific version number for reproducibility, or just specify "latest" to always get the most recent build with all the latest patches.

**Create the VM**: Now we have everything we need to create our Windows VM. We're using az vm create with the resource group "labs-vm-win", VM name "dev01", and here's where it all comes together. The image parameter uses the full URN format: "MicrosoftWindowsDesktop:windows-11:win11-22h2-pro:latest". That's publisher colon offer colon SKU colon version. We're setting the size to Standard_D4s_v5 or whatever size you found earlier that's available in your subscription, providing an admin username, specifying a unique public IP address DNS name so we can connect easily, and creating a strong admin password.

**Password Requirements**: When you run the create command, Azure will validate your password. It needs to be strong - at least 12 characters with a mix of uppercase letters, lowercase letters, numbers, and special characters. Something like "AzurePassword123!" would work, but make it unique and secure.

**VM Creation Time**: The command takes several minutes to complete - creating a Windows Desktop VM typically takes longer than a Linux Server VM because there's much more to install and configure. Windows 11 is a full desktop operating system with GUI, services, and features that all need to be set up.

**Explore Resources in Portal**: While it's running, you can switch back to the Portal and navigate to your resource group. You'll see several resources being created in real-time - the virtual machine itself, a virtual network and subnet providing network infrastructure, a network interface connecting the VM to the network, a public IP address for external access, a network security group controlling traffic, and an OS disk for the operating system. Look at the Network Security Group and find the inbound security rule that allows port 3389. This is what enables Remote Desktop access to your VM - without this rule, you wouldn't be able to connect even with the correct password.

---

## Add a data disk to the VM

Once your VM is created, let's add a data disk. This is useful for storing data that should persist independently from the VM.

**Understanding Disk Persistence**: If you delete the VM, you typically delete the OS disk too since it's specific to that VM instance, but data disks can be retained and even attached to different VMs. This separation is important for managing application data that should survive VM replacements or reconfigurations.

**Attach a New Disk**: We're running az vm disk attach with the resource group "labs-vm-win", VM name "dev01", disk name "dev01data", the new flag to create a new disk rather than attaching an existing one, SKU set to "Premium_LRS" for premium locally redundant storage, and size set to 2048 GB which is 2 terabytes.

**Premium Storage Benefits**: Premium storage uses fast solid-state disks in Azure's datacenter, providing much better performance than standard storage - lower latency, higher IOPS, better throughput. This is ideal for databases, applications with heavy disk I/O, or any workload where storage performance matters.

**Cost Considerations**: Keep in mind that disks are charged separately from VMs. Even when a VM is deallocated and not incurring compute charges, you still pay for the storage. And large Premium disks can be expensive - a 2TB Premium SSD costs significantly more per month than standard storage, so choose your disk sizes and performance tiers carefully based on actual needs.

---

## Connect and install dev tools

Now we're ready to connect to our VM using Remote Desktop Protocol.

**Remote Desktop Clients**: If you're on Windows, use the built-in Remote Desktop Connection application - just search for "Remote Desktop" in the start menu. On Mac, install Microsoft Remote Desktop from the App Store - it's a free application from Microsoft. On Linux, a good option is Remmina which supports RDP connections.

**Connect to the VM**: Use the DNS name you specified earlier in the create command, and provide your admin credentials - the username and password you set. RDP will connect to port 3389 on your VM. You might see a certificate warning - this is normal for a new VM that doesn't have a proper SSL certificate configured. Accept the certificate to continue connecting.

**Windows Desktop Experience**: You'll see the Windows desktop load - you're now logged into your cloud-based Windows machine running in Azure. It looks and feels like a local Windows computer, but it's running in a Microsoft datacenter.

**Install Development Tools**: Once connected, we need to install some development tools to make this a useful development environment. There's a PowerShell script called setup.ps1 in the lab folder. You can copy and paste the script content into the VM, or download it directly from the GitHub repository using PowerShell in the VM.

**Run the Setup Script**: Open PowerShell as Administrator on the VM - this is important because the script needs elevated privileges to install software. Right-click PowerShell and choose "Run as Administrator". Then run the setup script. This script uses Chocolatey, which is a package manager for Windows similar to apt on Linux or Homebrew on Mac. The script installs Chocolatey first if it's not already present, then uses it to install Git for version control and Visual Studio Code as a code editor. Watch the installation progress - you'll see Chocolatey downloading and installing each package. This takes a few minutes depending on internet speed and the size of the packages.

---

## Lab

Open Windows Explorer on your VM and look at the available drives. You'll see the C drive, which is your OS disk containing Windows and all the system files. But where's the 2TB data disk we attached?

Check in the Azure Portal - you'll see the data disk is definitely attached to the VM under the Disks section. So why isn't it showing up in Windows Explorer?

The answer is that the disk is attached at the hardware level - Windows can see it as a physical device - but Windows hasn't been told to use it yet. The disk needs to be initialized, partitioned, and formatted before Windows will assign it a drive letter and make it accessible.

Your task is to figure out how to initialize this disk and make it accessible in Windows. Look for disk management tools in Windows - there's a Disk Management console that you can access by right-clicking the Start button and selecting Disk Management, or by running "diskmgmt.msc" from the Run dialog. Once you open Disk Management, you should see the unallocated 2TB disk. You'll need to initialize it with either MBR or GPT partition style, create a new volume on it, assign a drive letter, and format it with a file system like NTFS.

---

## Cleanup

When you're finished with the lab, remember to clean up your resources to avoid ongoing charges. Windows VMs are relatively expensive compared to Linux, and that 2TB premium disk adds significant cost.

We're running az group delete with the yes flag to skip confirmation and the resource group name "labs-vm-win". This will delete the resource group and all the resources within it - the VM, both disks including the OS disk and data disk, all network resources, everything. The deletion takes a few minutes to complete as Azure cleans up all the associated resources.
