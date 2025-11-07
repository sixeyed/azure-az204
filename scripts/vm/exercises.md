# Virtual Machines

## Reference

Virtual Machines in the cloud provide the same isolated compute environment you'd find in a datacenter or on your desktop. You get a full operating system with administrative permissions to install and configure whatever you need. Azure supports both Linux and Windows VMs with a large selection of preconfigured images and compute sizes. The documentation covers everything from basic provisioning to advanced configuration, and the Azure CLI provides complete control through the az vm commands that we'll use throughout these exercises.

## Explore VMs in the Portal

Let's start by opening the Azure Portal and searching to create a new Virtual Machine resource. This gives us a comprehensive view of all the configuration options available.

Notice the extensive configuration options available throughout the wizard. The main ones to focus on are spread across several tabs, so let's explore each area.

First is Image Selection - Browse through the available images in the dropdown. What operating systems and pre-installed software do these images provide? You'll see Ubuntu, Red Hat, Windows Server, SQL Server pre-configured on Windows, and many specialized images from Microsoft and partners. Each image is a template that determines what software is installed when the VM starts.

Next is Size Selection - Click the "See all sizes" link and browse through the different VM sizes. How does compute capacity affect the monthly cost? Notice how costs scale dramatically with CPU cores and memory. A 2-core VM might be a few dollars per day, while a 64-core VM could be hundreds of dollars per day. The size also determines other capabilities like maximum number of data disks, network performance, and whether it supports premium storage.

Then Authentication Options - Examine the authentication methods available. For Linux VMs, you can use SSH keys which are more secure, or passwords which are simpler but less secure. For Windows VMs, you'll typically use username and password combinations. SSH key authentication is the recommended approach for Linux as it's much harder to compromise than password-based auth.

And Inbound Port Rules - Which ports will you need to open to connect to your VM? For Linux, that's typically port 22 for SSH which provides terminal access. For Windows, port 3389 for RDP which provides remote desktop access. You might also need port 80 for HTTP or 443 for HTTPS if you're running web services.

The basic options cover OS type, CPU, memory, and connectivity. But notice the required fields scattered throughout the form - what other resources do you need to create before you can deploy the VM? All resources must belong to a resource group, which provides organization and lifecycle management. And you can create these dependent resources like virtual networks and public IPs directly in the portal during VM creation.

Now click on the Disks tab. You can add multiple disks to your VM beyond just the operating system disk. Compare the performance differences between Standard HDD which uses spinning disks, Standard SSD which uses solid-state drives, and Premium SSD which uses faster SSDs with guaranteed IOPS. What are the IOPS differences? Standard HDD might provide 500 IOPS, while Premium SSD can deliver tens of thousands of IOPS with much lower latency.

Next, check the Networking tab. You can configure network access at the port level using inbound port rules. What type of Azure resource enforces these port rules behind the scenes? That's right - Network Security Groups, which act as a distributed firewall controlling traffic to your VM.

We won't actually create the VM in the portal. Instead, we'll use the Azure CLI for a more repeatable, scriptable approach that's better for automation and documentation.

## Create a Linux VM with the CLI

First, we need to create a Resource Group where the new VM and its dependent resources will live. Resource groups are the foundation of resource organization in Azure.

We're running az group create with a resource group name you choose, adding the "courselabs=azure" tag for tracking, and specifying a location. Pick a region that's close to you or to your users for better performance.

Before creating a VM, we need to find a valid VM size for our subscription and region. Availability varies by region and subscription type, so we can't just assume any size will work.

Let's find small VMs with limited cores and memory - this is good for development and keeps costs down. We're using az vm list-sizes with table output for readability, and here's the interesting part - a JMESPath query to filter the results.

The query syntax differs between PowerShell and Bash because of shell escaping rules. In PowerShell, we use double backticks before special characters, while in Bash we use backslash. We're filtering for VMs with a specific number of cores and megabytes of memory.

This JMESPath query filters the VM list by cores and memory constraints. The available sizes depend on several factors - your subscription type, the region you've chosen, and current capacity in that region. Enterprise subscriptions might have access to sizes that free-tier subscriptions don't.

Now let's create the VM using az vm create with several required parameters. We're specifying the location to match our resource group, the resource group name, a descriptive VM name, the image as "UbuntuLTS" which is an alias for Ubuntu Long Term Support, and a size from our earlier search.

Let me explain each parameter and why it matters. The location parameter determines where the VM physically runs - this affects latency, data residency compliance, and pricing. The resource group provides organization and a deletion boundary. The name identifies your VM and becomes part of the hostname. The image specifies which operating system and software to install. And the size determines the compute resources allocated - CPU cores, RAM, temporary storage, and network bandwidth.

Creating a new VM takes a few minutes as Azure provisions all the components. While it's running, you might wonder about the actual costs. Check the Azure pricing calculator to see the running cost for your specific VM size. Also research why A-series or B-series VMs might not be suitable for production workloads - they're burstable instances meant for development or low-traffic scenarios, where performance can vary significantly. B-series VMs accumulate CPU credits when idle and consume them when busy, which makes pricing unpredictable for steady-state workloads.

When your VM creation completes, browse to the portal and open your resource group. Notice that the VM comes with several supporting resources that Azure created automatically - a virtual network provides the network infrastructure, a network interface connects the VM to that network, a public IP address enables external access, a network security group controls traffic like a firewall, and a managed disk stores the operating system. All of these were created with sensible defaults.

## Connect to the VM

Now we have a Linux VM, we can connect using SSH. The SSH command-line tool is installed by default on MacOS, Linux, and modern Windows 10/11 machines. If you're on an older Windows version, you might need to install PuTTY.

First, we need to find the public IP address of our VM. The vm show command can retrieve this information, but by default it only shows static configuration.

We're running az vm show with the resource group name, VM name, and the crucial --show-details parameter. This parameter includes runtime information like the current public IP address and power state, not just the configuration settings.

The --show-details parameter includes runtime information like the public IP address. You can see the IP in the publicIps field of the JSON output.

Let's use a JMESPath query to extract just the IP address and store it in a variable for easy reuse. This is much cleaner than manually copying from the JSON.

For PowerShell, we're creating a variable called pip by capturing the output of az vm show with a query that extracts just the publicIps field in tab-separated value format.

For Bash, the syntax is similar but without the dollar sign before the variable name in the assignment.

Now we can connect via SSH using the IP address stored in our variable. Type ssh followed by the variable reference.

Notice that you can connect without specifying a username or password explicitly. That's because Azure generated an SSH key pair during VM creation and configured the VM with the public key. The private key was saved to your local machine in the .ssh directory. SSH automatically finds and uses this key for authentication, which is both more secure and more convenient than passwords.

Once connected, you're in a standard Ubuntu Server environment. The prompt shows your username and the hostname. Try these commands to explore the environment:

Run "top" to see the running processes and resource usage in real-time. You'll see the CPU usage, memory consumption, and a list of processes. Press Q to quit when you're done looking.

Run "uname -a" to see details about the Linux kernel version, the architecture, and when it was built. This gives you information about the operating system underpinning your VM.

Run "curl https://example.com" to make an HTTP request and verify internet connectivity from the VM. You should see the HTML of the example.com website, confirming that your VM has outbound internet access through Azure's network infrastructure.

When you're done exploring the VM environment, type "exit" to close the SSH session and return to your local terminal.

## Lab

For your lab exercise, use the Azure CLI to investigate the VM's disk configuration and understand the lifecycle of VM resources.

First task: Print the details of the VM's disk using az commands. What is the disk size in gigabytes? What is the performance tier - standard or premium? What are the performance characteristics in terms of read and write IOPS and throughput?

Second task: Delete the VM using the CLI with az vm delete. After deletion completes, check the resource group by listing its contents. Did the disk get deleted along with the VM, or does it still exist as a separate resource?

This is an important concept for cost management - understanding which resources persist after VM deletion. By default, the OS disk is configured to be deleted when the VM is deleted, but this behavior can be changed. Data disks, network interfaces, public IPs, and other resources might persist depending on configuration, which can lead to orphaned resources that continue to cost money even though the VM is gone.

## Cleanup

When you're finished with the lab and completed the challenge, delete the resource group to remove all remaining resources.

We're running az group delete with the -y flag to skip the interactive confirmation prompt and the resource group name.

This will delete the VM if it still exists, and all associated resources including the virtual network, network interface, public IP, network security group, and any remaining disks. It's a clean sweep that ensures you're not charged for resources you're no longer using. The deletion process takes a minute or two as Azure removes each resource in dependency order.
