# Securing VNet Access - Exercises Walkthrough

## Exercise 1: Creating a VM and Network Security Group

Let's start by setting up our foundational infrastructure. We'll create a resource group, a virtual network, and a subnet.

First, I'll create a resource group in the East US region:

```
az group create -n labs-vnet-access --tags courselabs=azure -l eastus
```

Now let's create our first virtual network with an address space of 10.10.0.0/16:

```
az network vnet create -g labs-vnet-access -n vnet1 --address-prefix "10.10.0.0/16"
```

And we'll add a subnet to this VNet with the range 10.10.1.0/24:

```
az network vnet subnet create -g labs-vnet-access --vnet-name vnet1 -n subnet1 --address-prefix "10.10.1.0/24"
```

### Creating the Network Security Group

Now comes the important part - creating a Network Security Group. If you're not sure how to do this, you can explore the available commands using the help flag. Let me show you:

```
az network nsg create -g labs-vnet-access -n nsg01
```

Notice that I didn't specify a location. This is important - if your NSG ends up in a different region than your VNet, you won't be able to associate them. Always make sure to specify the location parameter to match your VNet's region.

If you need to recreate the NSG in the correct region, you would delete it and recreate it like this:

```
az network nsg delete -g labs-vnet-access -n nsg01
az network nsg create -g labs-vnet-access -n nsg01 -l eastus
```

### Understanding Default NSG Rules

Let's take a look at the NSG in the Portal. You'll notice there are already default rules applied:
- Allow incoming traffic from within the VNet
- Allow incoming from Azure Load Balancer
- Deny all other incoming traffic
- Allow outgoing to VNet and internet
- Default deny all other outgoing traffic

These defaults provide a secure baseline, but we need to add a custom rule.

### Adding Custom Rules

Let's add a rule to allow HTTP traffic from the internet on port 80:

```
az network nsg rule create -g labs-vnet-access --nsg-name nsg01 -n 'AllowHttp' --direction Inbound --access Allow --priority 100 --source-address-prefixes 'Internet' --destination-port-ranges '80'
```

Now we need to attach this NSG to our subnet. Remember, the NSG is actually a property of the subnet itself:

```
az network vnet subnet update -g labs-vnet-access --vnet-name vnet1 --name subnet1 --network-security-group nsg01
```

If you check the VNet in the Portal now, you'll see the NSG is attached to the subnet. This means any resources we deploy into this subnet will be subject to these rules.

Here's something important to understand - we've allowed port 80, but ports 22 for SSH and 3389 for RDP are now blocked. So how do we access our VMs? That's where Bastion comes in.

## Exercise 2: Connecting with Azure Bastion

Let's create a Linux VM in our secured network. This time we'll use password authentication instead of SSH keys:

```
az vm create -g labs-vnet-access -n ubuntu01 --image UbuntuLTS --vnet-name vnet1 --subnet subnet1 --admin-username labs --admin-password SecurePassword123! -l eastus
```

Once the VM is created, you can check the Networking tab in the Portal - you'll see the NSG is automatically applied even though we didn't explicitly set it during VM creation. That's because it's attached at the subnet level.

### Testing Connectivity

If you try to SSH to the VM using its public IP, you'll find it times out. That's expected because port 22 is blocked by our NSG rules:

```
ssh labs@20.12.34.56
```

This will hang because the connection can't get through.

### Setting up Azure Bastion

To access our locked-down VM, we'll use Azure Bastion. In the Portal:
1. Open the VM
2. Click Connect and choose Bastion from the dropdown
3. Select "Create Azure Bastion using defaults"

This deployment takes a few minutes. Bastion is created at the VNet level, so one Bastion instance can serve all VMs in the VNet.

Once it's ready, enter "labs" as the username and your password, then click Connect. A new browser window opens with a terminal session to your VM - but port 22 is still blocked for direct access. Bastion uses its own secure connection method.

### Testing the Web Server

In your Bastion session, let's install Nginx:

```
sudo apt update && sudo apt install -y nginx
```

Now browse to your VM's public IP address in a browser. You should see the Nginx welcome page, confirming that traffic is allowed on port 80.

## Exercise 3: VNet Peering

Now let's explore a more complex scenario - connecting two virtual networks together.

### Creating the Second VNet

We'll create a second VNet in a different region with a different IP address range. This is important - peered VNets must have non-overlapping address spaces:

```
az network vnet create -g labs-vnet-access -n vnet2 --address-prefix "10.20.0.0/16" -l westus

az network vnet subnet create -g labs-vnet-access --vnet-name vnet2 -n subnet2 --address-prefix "10.20.1.0/24"
```

Notice we're using 10.20.x.x instead of 10.10.x.x - no overlap.

Let's create a VM in this new network. Since we haven't attached an NSG to this subnet, Azure will create a default NSG for the VM that allows SSH:

```
az vm create -g labs-vnet-access -n remote01 --image UbuntuLTS --vnet-name vnet2 --subnet subnet2 -l westus
```

### Checking Connectivity Before Peering

Let's list our VMs and their IP addresses:

```
az vm list -g labs-vnet-access --show-details --query "[].{VM:name, InternalIP:privateIps, PublicIP:publicIps}" -o table
```

You'll see both private IPs - something like 10.10.1.4 for ubuntu01 and 10.20.1.4 for remote01.

SSH to the second VM - this will work because its NSG allows port 22:

```
ssh azureuser@40.23.45.67
```

Now try to reach the first VM using its private IP address:

```
curl 10.10.1.4
```

This will time out. Even though both VMs are in the same resource group, they're in different VNets and can't communicate yet.

### Creating the Peering

To connect these networks, we need to create peering in both directions. This is a security feature - you can't peer onto someone else's VNet without their permission:

```
az network vnet peering create -g labs-vnet-access -n vnet2to1 --vnet-name vnet2 --remote-vnet vnet1 --allow-vnet-access

az network vnet peering create -g labs-vnet-access -n vnet1to2 --vnet-name vnet1 --remote-vnet vnet2 --allow-vnet-access
```

In the Portal, check the Peerings section of either VNet - you should see the status is "Connected".

### Testing Peered Connectivity

Back in your SSH session to remote01, try the curl command again:

```
curl 10.10.1.4
```

Now it works! You should see the Nginx HTML response. The VMs can now communicate using their private IP addresses.

Check the network interfaces on remote01:

```
ip a
```

You'll only see the 10.20.x.x address - no new interface was added. The peering handles routing at the network level transparently.

## Lab Challenge

Here's the challenge: right now, the web server in subnet1 is accessible from the entire internet AND from VMs in subnet2. But those VMs in subnet2 can access ANY port on ubuntu01, including SSH.

Your task is to update the NSG rules so that:
- Internet traffic can still reach port 80
- Subnet2 VMs can only reach port 80, not SSH
- The network remains secure

Think about how you would structure multiple NSG rules with different priorities and source address prefixes to achieve this.

Take some time to work through this challenge, and refer to the hints if you get stuck.
