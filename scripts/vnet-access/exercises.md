# Securing VNet Access

## Reference

Virtual Networks provide great capabilities for restricting traffic to services in Azure, and they give you a lot of options for securing access to resources. The Network Security Group is the main mechanism, where you can define rules allowing or denying traffic from specific sources and to specific ports. You can also join vnets together if you need different parts of an application to access each other, and use Bastion to access VMs which are in networks that don't allow public access. The documentation covers NSG rule configuration, VNet peering topologies, and Bastion deployment patterns. The az network nsg commands give you complete control over security rules and their application to subnets and network interfaces.

## Create a VM and an NSG

**Create the Foundation**: We're starting by creating a resource group, virtual network, and subnet for this lab. We're running az group create with the name "labs-vnet-access", adding our "courselabs=azure" tag for tracking, and placing it in East US. Then we're creating a virtual network with az network vnet create using the resource group "labs-vnet-access", VNet name "vnet1", and address prefix "10.10.0.0/16". This gives us a large private IP address space with 65,536 possible addresses. Then we're adding a subnet with az network vnet subnet create using the VNet name "vnet1", subnet name "subnet1", and address prefix "10.10.1.0/24" which can accommodate 256 addresses.

**Create the Network Security Group**: Now we're creating a Network Security Group that will act as our firewall. We're running az network nsg create with the resource group "labs-vnet-access" and name "nsg01". If you explore the help for network commands, you'll see nsg is the group to use for Network Security Groups.

**Check the Location**: Open the NSG in the Portal and check its location along with the default rules. There are default rules applied to all new NSGs - they allow incoming from VNet and Azure Load Balancer, deny all other incoming, allow outgoing to VNet and internet, and default deny all outgoing. Also verify the location - if you didn't set the location explicitly in the command, your VNet and NSG may be in different regions.

**Fix Location Mismatch**: If your NSG is in a different region from your VNet then they can't be associated, which is an Azure requirement for network resources. You'll need to delete the NSG and create a new one in the same region as the VNet. We're running az network nsg delete to remove it, then az network nsg create again with the location parameter explicitly set to match your VNet's region.

**Add a Custom Rule**: Let's add a new rule to allow incoming traffic from the internet on port 80. We're using az network nsg rule create with the resource group "labs-vnet-access", NSG name "nsg01", rule name "AllowHttp", direction set to Inbound, access set to Allow, priority set to 100 which is lower than the default deny rules so it takes precedence, source address prefixes set to "Internet" to allow from anywhere, and destination port ranges set to "80" for HTTP.

**Attach NSG to Subnet**: Now we need to attach this NSG to our subnet. The NSG is actually a property of the subnet itself, not a separate attachment. We're running az network vnet subnet update with the resource group "labs-vnet-access", VNet name "vnet1", subnet name "subnet1", and network-security-group set to "nsg01". You can check the help for subnet update commands to see all the properties you can configure.

**Verify in Portal**: Open the VNet in the Portal and check the subnet configuration - you can confirm that the NSG is attached here. Any services deployed into the VNet are subject to these NSG rules now. That means port 22 for SSH and 3389 for RDP are blocked, so if we had VMs running in this VNet we couldn't access them directly anymore. We'll need to use another service to manage them.

---

## Connect with Bastion

**Create a Linux VM**: Let's create a basic Linux VM, and this time we'll use password authentication instead of the default SSH key. We're running az vm create with the resource group "labs-vnet-access", VM name "ubuntu01", image set to "UbuntuLTS", VNet name "vnet1", subnet "subnet1", admin username "labs", admin password that you'll specify, and location matching your VNet. Make sure to use the same location as the VNet to avoid compatibility issues.

**Verify NSG Application**: Check the VM in the Portal and open the Networking tab - you'll see the NSG listed even though we didn't explicitly set it when we created the VM. That's because it's attached at the subnet level, so the VM automatically inherits those rules.

**Test Direct Access**: Try to connect to the machine using SSH with the public IP address. This will time out because SSH uses port 22 which is blocked by the NSG rules. The connection attempt hangs and eventually fails, demonstrating that our NSG is working as intended.

**Deploy Azure Bastion**: Azure has Bastion for accessing VMs which are in locked-down networks. We're opening the VM in the Portal, clicking Connect, and choosing Bastion from the dropdown. Then we're selecting "Create Azure Bastion using defaults". This will take a few minutes to deploy. The Bastion service is created at the VNet level, and the same Bastion instance can be used for all the VMs in the VNet, making it a shared resource.

**Connect via Bastion**: When the Bastion setup completes, we're entering "labs" as the username and the password you used to create the VM, then clicking Connect. A browser window opens with a terminal connection to the VM, but port 22 is still blocked for direct access. Bastion uses its own secure connection method that doesn't require exposing management ports publicly.

**Install Web Server**: In your VM session, let's install the Nginx web server. We're running sudo apt update to refresh package lists, followed by sudo apt install nginx with the -y flag to automatically confirm the installation. This downloads and configures the web server.

**Test HTTP Access**: Browse to your VM's public IP address in a web browser to verify traffic is allowed through the NSG on port 80. You should see the Nginx welcome page, confirming that our HTTP rule is working correctly while management ports remain protected.

---

## Create second VNet and peer

**Why Peering Matters**: VNets are a good way of isolating parts of an application, but sometimes you want components in one VNet to be able to reach components in a different VNet. Maybe you have VNets in different regions hosting different services. You can connect those two VNets together in Azure using peering.

**Create Second VNet**: Let's create a new VNet with the IP address range "10.20.0.0/16" in a different region from the first VNet. We're running az network vnet create with the resource group "labs-vnet-access", VNet name "vnet2", address prefix "10.20.0.0/16", and location in a different region like West US. Then we're adding a new subnet using az network vnet subnet create with the VNet name "vnet2", subnet name "subnet2", and address prefix "10.20.1.0/24".

**Address Space Planning**: Notice we're using 10.20.0.0/16 instead of 10.10.0.0/16 - this is crucial because you need to plan your networking in advance. If you want to peer two VNets they need to have non-overlapping IP address ranges. Overlapping ranges make routing impossible and prevent peering from working.

**Create Second VM**: Now we're creating a new VM attached to the new VNet which has no NSG. Azure will create a new NSG for the VM with an additional default rule to allow incoming SSH traffic. We're running az vm create with the resource group "labs-vnet-access", VM name "remote01", image "UbuntuLTS", VNet name "vnet2", subnet "subnet2", and location matching vnet2's region.

**Check IP Addresses**: Let's print the private IP addresses of both VMs. We're running az vm list with the resource group "labs-vnet-access", the show-details flag to include runtime information, a query to extract just the VM name, internal private IP, and public IP, and table output for readability. You'll see something like 10.10.1.4 for ubuntu01 in the first VNet and 10.20.1.4 for remote01 in the second VNet.

**Test Connectivity Before Peering**: Connect to the new VM using SSH with its public IP address - this will work because the VM's NSG allows port 22 by default. Once connected, try to reach the web server on the first VM using its private IP address with curl. Type curl followed by the private IP of ubuntu01. This will time out because the VNets are isolated networks by default - they can't communicate even though they're in the same resource group and subscription.

**Create the Peering**: Now let's peer the VNets. You need to peer both networks in both directions - this is a security feature ensuring you can't peer onto someone else's VNet that you don't have access to. We're running az network vnet peering create to create the first peering from vnet2 to vnet1. The resource group is "labs-vnet-access", peering name "vnet2to1" describes the direction, VNet name is "vnet2" where we're creating the peering, remote VNet is "vnet1" that we're peering to, and allow-vnet-access enables connectivity. Then we're creating the reverse peering from vnet1 to vnet2 using az network vnet peering create with the name "vnet1to2", VNet name "vnet1", and remote VNet "vnet2".

**Verify Peering Status**: Open the new VNet in the Portal and navigate to the Peerings section - you should see that the VNets are peered with the status "Connected". Now VMs in subnet2 with addresses starting 10.20 can reach VMs in subnet1 with addresses starting 10.10.

**Test Peered Connectivity**: In the SSH session for your second VM, try accessing the first VM again using curl with the private IP address. Now this works! You should see the Nginx HTML response. The VMs can now communicate using their private IP addresses through the peering connection. Check your IP addresses with the ip a command to show all network adapters - you'll only see a 10.20 address. Peering doesn't add a new NIC to the VM, it takes care of routing at the Azure network fabric level transparently.

---

## Lab

**The Challenge**: Now the web server in subnet1 is accessible from any machine on the Internet, and from VMs in subnet2. But those VMs in subnet2 can access any port on the VM in subnet1, including SSH port 22 which we don't want. This is a security risk because peered networks have full connectivity by default.

**Your Task**: Update the NSG rules so that traffic is only allowed to the web server from subnet2 machines on port 80. Internet traffic should still work on port 80, but subnet2 should be restricted to only HTTP access and denied SSH or other ports. This requires careful planning of rule priorities and source address prefixes to achieve proper security isolation.

**Think About**: How would you structure multiple NSG rules with different priorities and source address prefixes? You'll need rules that specifically target the subnet2 address range while maintaining internet access. Consider that lower priority numbers are evaluated first, so you can layer your security rules appropriately.

---

## Cleanup

**Delete Azure Resources**: When you're finished with the lab, delete the resource group to remove all resources and avoid ongoing charges. We're running az group delete with the -y flag to skip confirmation, the no-wait flag to return immediately without waiting for completion, and the resource group name "labs-vnet-access". This removes everything - VMs, VNets, NSGs, Bastion, all related resources.
