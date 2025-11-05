# Securing VNet Access - Exercises Walkthrough

## Exercise 1: Creating a VM and Network Security Group

Let's start by setting up our foundational infrastructure. We'll create a resource group, a virtual network, and a subnet to work with.

First, we're creating a resource group in the East US region using az group create with the name "labs-vnet-access", adding our "courselabs=azure" tag for tracking, and specifying the location.

Now let's create our first virtual network with an address space. We're using az network vnet create with the resource group "labs-vnet-access", network name "vnet1", and address prefix "10.10.0.0/16". This gives us a large private IP address space with 65,536 possible addresses to work with.

And we'll add a subnet to this VNet. We're running az network vnet subnet create with the resource group, VNet name "vnet1", subnet name "subnet1", and address prefix "10.10.1.0/24". This subnet can accommodate 256 addresses, which is a good size for a typical subnet.

### Creating the Network Security Group

Now comes the important part - creating a Network Security Group that will act as our firewall. If you're not sure how to do this, you can explore the available commands using the help flag.

We're running az network nsg create with the resource group "labs-vnet-access" and name "nsg01".

Notice that we didn't specify a location explicitly. This is actually important - if your NSG ends up in a different region than your VNet, you won't be able to associate them. Azure has strict rules about network resource co-location. Let's check what happened and fix it if needed.

If the NSG was created in the wrong region, we would need to delete it and recreate it with an explicit location parameter. We're running az network nsg delete to remove it, then az network nsg create again with the location explicitly set to East US to match our VNet's region.

Always make sure to specify the location parameter to match your VNet's region when creating network resources - it prevents compatibility issues later.

### Understanding Default NSG Rules

Let's take a look at the NSG in the Portal to see what rules are automatically applied. Navigate to the NSG resource and look at the Inbound security rules section.

You'll notice there are already default rules applied even though we haven't added any custom ones. The defaults provide a secure baseline: Allow incoming traffic from within the VNet so resources can communicate with each other, allow incoming from Azure Load Balancer so health probes work, deny all other incoming traffic by default which is a security-first approach, allow outgoing to VNet and internet for typical connectivity needs, and a default deny for all other outgoing traffic.

These defaults provide a secure baseline, but we need to add a custom rule to allow HTTP traffic from the internet.

### Adding Custom Rules

Let's add a rule to allow HTTP traffic from the internet on port 80. We're using az network nsg rule create with the resource group "labs-vnet-access", NSG name "nsg01", rule name "AllowHttp", direction set to Inbound, access set to Allow, priority set to 100 which is lower than the default deny rules so it takes precedence, source address prefixes set to "Internet" to allow from anywhere, and destination port ranges set to "80" for HTTP.

Now we need to attach this NSG to our subnet. Remember, the NSG is actually a property of the subnet itself - it's not a separate attachment but part of the subnet configuration.

We're running az network vnet subnet update with the resource group "labs-vnet-access", VNet name "vnet1", subnet name "subnet1", and network-security-group set to "nsg01".

If you check the VNet in the Portal now, you'll see the NSG is attached to the subnet in the configuration. This means any resources we deploy into this subnet will automatically be subject to these NSG rules.

Here's something important to understand - we've allowed port 80 for HTTP, but ports 22 for SSH and 3389 for RDP are now blocked by the default deny rule. So how do we access our VMs for management? That's where Bastion comes in.

## Exercise 2: Connecting with Azure Bastion

Let's create a Linux VM in our secured network. This time we'll use password authentication instead of SSH keys for simplicity.

We're running az vm create with the resource group "labs-vnet-access", VM name "ubuntu01", image set to "UbuntuLTS", VNet name "vnet1", subnet "subnet1", admin username, admin password, and location East US.

Once the VM is created, you can check the Networking tab in the Portal - you'll see the NSG is automatically applied even though we didn't explicitly set it during VM creation. That's because it's attached at the subnet level, so any VM in that subnet inherits the rules.

### Testing Connectivity

If you try to SSH to the VM using its public IP address, you'll find it times out. Let's try it - the SSH command hangs and eventually fails because the connection can't get through.

This is expected because port 22 is blocked by our NSG rules - only port 80 is allowed.

### Setting up Azure Bastion

To access our locked-down VM, we'll use Azure Bastion, which provides secure RDP and SSH connectivity through the Azure Portal without exposing management ports to the internet.

In the Portal, opening the VM resource and clicking Connect shows a dropdown menu. Choose Bastion from the options, and select "Create Azure Bastion using defaults".

This deployment takes a few minutes as Azure provisions the Bastion infrastructure. Bastion is created at the VNet level, so one Bastion instance can serve all VMs in the VNet - it's a shared service that provides secure access to multiple VMs.

Once it's ready, enter your username and password in the Bastion connection form, then click Connect. A new browser window opens with a terminal session to your VM - but notice that port 22 is still blocked for direct access. Bastion uses its own secure connection method that doesn't require opening SSH or RDP ports publicly.

### Testing the Web Server

In your Bastion session, let's install Nginx to test that our HTTP rule works. We're running sudo apt update to refresh package lists, followed by sudo apt install nginx with the -y flag to automatically confirm.

The package manager is updating and installing Nginx. This will take a moment as it downloads and configures the web server.

Now browse to your VM's public IP address in a browser on your local machine. You should see the Nginx welcome page, confirming that traffic is allowed on port 80 through the NSG.

## Exercise 3: VNet Peering

Now let's explore a more complex scenario - connecting two virtual networks together so resources in different VNets can communicate.

### Creating the Second VNet

We'll create a second VNet in a different region with a different IP address range. This is important - peered VNets must have non-overlapping address spaces, otherwise routing wouldn't work.

We're running az network vnet create with the resource group "labs-vnet-access", VNet name "vnet2", address prefix "10.20.0.0/16" which doesn't overlap with our 10.10.x.x range, and location West US which is a different region.

Then we're adding a subnet using az network vnet subnet create with the VNet name "vnet2", subnet name "subnet2", and address prefix "10.20.1.0/24".

Notice we're using 10.20.x.x instead of 10.10.x.x - completely separate address space with no overlap.

Let's create a VM in this new network. Since we haven't attached an NSG to this subnet, Azure will create a default NSG for the VM that allows SSH by default.

We're running az vm create with the resource group, VM name "remote01", image "UbuntuLTS", VNet name "vnet2", subnet "subnet2", and location West US.

### Checking Connectivity Before Peering

Let's list our VMs and their IP addresses to see what we have. We're running az vm list with the resource group "labs-vnet-access", --show-details flag, and a query to extract just the VM name, internal private IP, and public IP, showing it in table format.

You'll see both private IPs - something like 10.10.1.4 for ubuntu01 in the first VNet and 10.20.1.4 for remote01 in the second VNet.

Now SSH to the second VM using its public IP - this will work because its NSG allows port 22.

Once connected, try to reach the first VM using its private IP address with curl. Type curl followed by the private IP of ubuntu01, something like 10.10.1.4.

This will time out and fail. Even though both VMs are in the same resource group and subscription, they're in different VNets which are isolated networks by default. They can't communicate yet.

### Creating the Peering

To connect these networks, we need to create peering in both directions. This is a security feature - you can't peer onto someone else's VNet without their permission, so peering requires configuration on both sides.

We're running az network vnet peering create to create the first peering from vnet2 to vnet1. The resource group is "labs-vnet-access", peering name "vnet2to1" describes the direction, VNet name is "vnet2" where we're creating the peering, remote VNet is "vnet1" that we're peering to, and allow-vnet-access enables connectivity.

Then we're creating the reverse peering from vnet1 to vnet2 using az network vnet peering create with the name "vnet1to2", VNet name "vnet1", and remote VNet "vnet2".

In the Portal, checking the Peerings section of either VNet shows you should see the status is "Connected" on both sides.

### Testing Peered Connectivity

Back in your SSH session to remote01, try the curl command again to the first VM's private IP.

Now it works! You should see the Nginx HTML response. The VMs can now communicate using their private IP addresses through the peering connection.

Check the network interfaces on remote01 using the ip a command to show all network adapters.

You'll only see the 10.20.x.x address assigned to the VM - no new interface was added for the peering. The peering handles routing at the Azure network fabric level transparently. Your VM doesn't need to know anything about the peering - it just routes traffic to the 10.10.0.0/16 network and Azure's network fabric delivers it through the peering.

## Lab Challenge

Here's the challenge to deepen your understanding of NSG rules and security: right now, the web server in subnet1 is accessible from the entire internet on port 80 AND from VMs in subnet2. But those VMs in subnet2 can access ANY port on ubuntu01, including SSH port 22 and any other services.

Your task is to update the NSG rules so that Internet traffic can still reach port 80, subnet2 VMs can only reach port 80 and not SSH or other ports, and the network remains secure overall.

Think about how you would structure multiple NSG rules with different priorities and source address prefixes to achieve this. You'll need to add a rule that specifically allows port 80 from the subnet2 address range, and a higher-priority rule that denies other ports from that subnet.

Remember that lower priority numbers are evaluated first, so you can create a deny rule with priority 90 to block SSH from subnet2, and your existing allow rule at priority 100 still allows HTTP from anywhere.

Take some time to work through this challenge and test the connectivity from both the internet and from subnet2, and refer to the hints or solution files if you get stuck.
