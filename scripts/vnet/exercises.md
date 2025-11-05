# Virtual Networks - Exercises Script

## Exercise 1: Exploring Virtual Networks in the Portal

Let's start by opening the Azure Portal and searching for Virtual Network. Click the Create button to see the configuration options.

Notice there aren't as many options as some other services we've covered. Let me walk you through what you'll see:

The name field - remember, this doesn't need to be globally unique, just unique within your Resource Group.

IP addresses - here's where you select an address range for the whole VNet. You'll choose from the private CIDR ranges. Common choices are 10.0.0.0/16, 172.16.0.0/12, or 192.168.0.0/16.

Subnets - when you create a VNet in the Portal, it will prompt you to create at least one subnet. You'll give the subnet its own IP range within the VNet's range.

Now let's switch over to the CLI to create our VNet with more control.

## Exercise 2: Creating a Virtual Network with the CLI

First, let's create a Resource Group for this lab. I'm using the East US region, but you can use your preferred region:

```
az group create -n labs-vnet --tags courselabs=azure -l eastus
```

Now we'll create a Virtual Network. We'll call it vnet1 and use the address space 10.10.0.0/16. Let me show you the command:

```
az network vnet create -g labs-vnet -n vnet1 --address-prefix "10.10.0.0/16"
```

This creates the VNet with our specified address range. But here's something interesting - let's check what was created:

```
az network vnet show -g labs-vnet -n vnet1
```

If you look at the output, you'll notice there are no subnets yet. When you create a VNet through the Portal, it creates a default subnet, but the basic CLI command doesn't. Since subnets are where you actually deploy services, we need to create at least one.

## Exercise 3: Creating Subnets

Let's create two subnets - a frontend subnet and a backend subnet. This is a common pattern where you might put web servers in the frontend and databases in the backend.

Here are the commands:

```
az network vnet subnet create -g labs-vnet --vnet-name vnet1 -n frontend --address-prefix "10.10.1.0/24"

az network vnet subnet create -g labs-vnet --vnet-name vnet1 -n backend --address-prefix "10.10.2.0/24"
```

Notice how the subnet address ranges fall within our VNet's 10.10.0.0/16 range. The frontend uses 10.10.1.0/24 and the backend uses 10.10.2.0/24.

Here's a question to consider: What happens if you try to create overlapping IP address ranges, or use a range that isn't within the parent VNet? I encourage you to try it - the CLI will show you exactly what's allowed and what isn't.

## Exercise 4: Deploying a Virtual Machine into the VNet

Now let's deploy a Virtual Machine into our VNet. We covered VMs in detail in the VM lab, so we'll move quickly here. We're using a VM as an easy way to test our networking setup.

Let's create a Linux VM running Ubuntu Server in the frontend subnet:

```
az vm create -g labs-vnet -n vm01 --image UbuntuLTS --vnet-name vnet1 --subnet frontend --generate-ssh-keys
```

This command takes care of setting up SSH so you can log into the machine remotely. When it completes, you'll see the public IP address in the output.

The generate-ssh-keys parameter automatically creates and configures SSH keys for secure access.

## Exercise 5: Working with VM Images

If you wanted to create a Windows VM instead, you'd need to use a different image. Let me show you how to find available images.

You can list all VM images, but that takes a while. Instead, filter by the OS name:

```
az vm image list --offer Windows -o table
```

You'll see lots of images with long names, but notice the alias column. For Windows Server 2019, the alias is Win2019Datacenter. You can use that alias in the vm create command.

## Exercise 6: Connecting to the VM

Once the VM is created, let's get its public IP address. The show command has a special flag for this:

```
az vm show -g labs-vnet -n vm01 --show-details --query publicIps -o tsv
```

This gives us just the IP address without all the other details.

Now we can connect using SSH:

```
ssh <public-ip-address>
```

Once you're connected, check the IP address configuration:

```
ip address
```

Here's something important to note: the VM only knows about its private IP address on the VNet. You should see an IP in the 10.10.1.x range - that's from our frontend subnet.

The public IP address is managed outside of the VM by Azure. The private IP is assigned by the VNet and is what the VM uses for communication within Azure.

Type exit to return to your local machine.

## Exercise 7: Exploring Networking Resources in the Portal

Let's go back to the Portal and open our labs-vnet Resource Group. You'll notice several resources that we didn't explicitly create:

- A disk - this is the virtual storage unit attached to the VM
- A NIC (Network Interface Card) - this connects the VM to the VNet
- A Network Security Group - this controls network access to the VM, like a firewall
- A Public IP Address - this is what allows external access

Click on Resource Visualizer to see a diagram of how all these resources are connected. It's a great way to understand the relationships between components.

All of these were created with default configurations by the vm create command. In production scenarios, you might want to create and configure these resources independently for more control.

## Lab Challenge

Now here's a challenge for you. The az command is powerful, but it has one drawback - it's an imperative approach. You tell Azure what to do step by step. If you need to re-run scripts, you'll get errors about resources already existing.

Azure also supports a declarative approach using Azure Resource Manager templates, or ARM templates. With ARM templates, you describe what the end result should be, and you can run them repeatedly to always get the same result.

Your challenge: Export an ARM template for the labs-vnet Resource Group, then use it to deploy a copy of all the resources in a new Resource Group called labs-vnet2.

This will give you hands-on experience with infrastructure as code in Azure.

## Cleanup

When you're finished with the lab, delete the Resource Groups to remove all resources:

```
az group delete -y -n labs-vnet
az group delete -y -n labs-vnet2
```

This ensures you're not charged for resources you're no longer using.
