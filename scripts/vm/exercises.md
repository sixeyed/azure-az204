# Virtual Machines - Exercises

## Exercise 1: Explore VMs in the Portal

Let's start by opening the Azure Portal and searching to create a new Virtual Machine resource.

Notice the extensive configuration options available. The main ones to focus on are:

**Image Selection** - Look at the available images. What operating systems and pre-installed software do these images provide?

**Size Selection** - Browse through the different VM sizes. How does compute capacity affect the monthly cost? Notice how costs scale with CPU cores and memory.

**Authentication Options** - Examine the authentication methods. For Linux VMs, you can use SSH keys or passwords. For Windows VMs, you'll typically use username and password combinations.

**Inbound Port Rules** - Which ports will you need to open to connect to your VM? For Linux, that's typically port NUMBER for SSH. For Windows, port NUMBER for RDP.

The basic options cover OS type, CPU, memory, and connectivity. But notice the required fields - what other resources do you need to create before you get to the VM? All resources must belong to a resource group, and you can create these dependent resources directly in the portal.

Now click on the **Disks** tab. You can add multiple disks to your VM. Compare the performance differences between Standard HDD, Standard SSD, and Premium SSD. What are the IOPS differences?

Next, check the **Networking** tab. You can configure network access at the port level. What type of Azure resource enforces these port rules? That's right - Network Security Groups.

We won't actually create the VM in the portal. Instead, we'll use the Azure CLI for a more repeatable, scriptable approach.

## Exercise 2: Create a Linux VM with the CLI

First, we need to create a Resource Group where the new VM and its dependent resources will live.

Run this command to create the resource group:

```
az group create -n RESOURCE_GROUP_NAME --tags courselabs=azure -l LOCATION
```

Before creating a VM, we need to find a valid VM size for our subscription and region. Let's find small VMs with NUMBER_OF_CORES cores or fewer and MEMORY_IN_MB MB of memory.

For PowerShell, run:
```
az vm list-sizes -o table --query "[?numberOfCores<=``NUMBER`` && memoryInMb==``MEMORY``]" --location "LOCATION"
```

Or for Bash:
```
az vm list-sizes -o table --query "[?numberOfCores<=\`NUMBER\` && memoryInMb==\`MEMORY\`]" --location "LOCATION"
```

This JMESPath query filters the VM list by cores and memory. The available sizes depend on your subscription, region, and current capacity in that region.

Now let's create the VM. We'll use the `az vm create` command with several required parameters:

```
az vm create -l LOCATION -g RESOURCE_GROUP_NAME -n VM_NAME --image UbuntuLTS --size VM_SIZE
```

Let me explain each parameter:
- `-l` specifies the location
- `-g` is the resource group name
- `-n` is the VM name
- `--image` specifies we want Ubuntu Long Term Support
- `--size` is the VM size we found earlier

Creating a new VM takes a few minutes. While it's running, you might wonder about costs. Check the Azure pricing calculator to see the running cost for your VM size. Also research why A-series or B-series VMs might not be suitable for production workloads - they're burstable instances meant for development or low-traffic scenarios.

When your VM creation completes, browse to the portal and open your resource group. Notice that the VM comes with several supporting resources - a virtual network, network interface, public IP address, network security group, and disk. Azure created all of these automatically.

## Exercise 3: Connect to the VM

Now we have a Linux VM, we can connect using SSH. The SSH command-line tool is installed by default on MacOS, Linux, and modern Windows machines.

First, we need to find the public IP address of our VM. The `vm show` command can retrieve this:

```
az vm show -g RESOURCE_GROUP_NAME -n VM_NAME --show-details
```

The `--show-details` parameter includes runtime information like the public IP address. You can see the IP in the `publicIps` field.

Let's use a JMESPath query to extract just the IP address and store it in a variable:

For PowerShell:
```
$pip=$(az vm show -g RESOURCE_GROUP_NAME -n VM_NAME --show-details --query "publicIps" -o tsv)
```

Or for Bash:
```
pip=$(az vm show -g RESOURCE_GROUP_NAME -n VM_NAME --show-details --query "publicIps" -o tsv)
```

Now connect via SSH:
```
ssh $pip
```

Notice that you can connect without specifying a username or password. That's because Azure generated an SSH key pair and configured the VM with the public key during creation. The private key was saved to your local machine.

Once connected, you're in a standard Ubuntu Server environment. Try these commands:

Run `top` to see the running processes and resource usage. Press Q to quit.

Run `uname -a` to see details about the Linux kernel version.

Run `curl https://example.com` to make an HTTP request and verify internet connectivity.

When you're done exploring, type `exit` to close the SSH session.

## Lab Challenge

For your lab exercise, use the Azure CLI to investigate the VM's disk configuration.

First, print the details of the VM's disk. What is the disk size? What is the performance in terms of read and write IOPS?

Then, delete the VM using the CLI. After deletion, check the resource group. Did the disk get deleted along with the VM, or does it still exist?

This is an important concept for cost management - understanding which resources persist after VM deletion.

## Cleanup

When you're finished with the lab, delete the resource group to remove all resources:

```
az group delete -y -n RESOURCE_GROUP_NAME
```

This will delete the VM and all associated resources, including the virtual network, network interface, public IP, network security group, and any remaining disks.
