# Virtual Machines - Windows: Exercises Introduction

We've covered the fundamentals of Windows Virtual Machines in Azure and why they're useful as cloud-based development workstations. Now let's put that knowledge into practice by creating and configuring a Windows 11 VM with development tools.

## What You'll Do

You'll explore Windows VM options in the Azure Portal to understand how authentication and networking differ from Linux VMs. Then you'll use the Azure CLI to find the right VM size and Windows 11 image for a development workstation.

Next, you'll create a Windows VM with appropriate resources - 4 cores and 16 GB of RAM to handle Windows smoothly. You'll add a 2TB Premium SSD data disk that persists independently from the VM itself, giving you secure storage for important development files.

Finally, you'll connect via Remote Desktop Protocol and install development tools using PowerShell and Chocolatey. The lab challenge asks you to initialize and format the data disk using Windows Disk Management so it's ready for use.

The key learning: Windows VMs require more resources than Linux, use RDP instead of SSH for access, and support data disks that persist independently - perfect for development workstations you can access from anywhere while only paying for compute time when the VM is actually running.
