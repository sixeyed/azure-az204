# Virtual Networks

## Reference

Virtual Networks are private network infrastructure in Azure where your services can communicate with each other without being accessible on the public Internet. This is a core component for deploying secure solutions in Azure, and you should aim to use vnets in all your applications, provided the services you're using support them. You create the vnet first and deploy other services into it. You can't typically move resources between vnets, so you need to plan your networking up front. The documentation covers everything from basic vnet creation to advanced scenarios like peering and hybrid connectivity. The az network commands give you complete control over vnets, subnets, and all related networking resources.

## Explore Virtual Networks in the Portal

Let's start by getting familiar with Virtual Network options in the Portal.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Virtual Network" to create a new resource. Before creating anything, let's explore the available options to understand what vnets offer.

**Name Configuration**: The name field is first, and there's good news here - unlike storage accounts or Key Vaults, vnet names don't need to be globally unique. They only need to be unique within your Resource Group. You can use descriptive names like "production-vnet" or "development-network" without worrying about someone else having used that name.

**IP Address Selection**: The IP addresses configuration is where you select an address range for the whole vnet. You'll choose from the private CIDR ranges defined in RFC 1918. Common choices are 10.0.0.0/16 which gives you 65,536 addresses, 172.16.0.0/12 which is a larger range often used in enterprise environments, or 192.168.0.0/16 which is familiar from home networking. The /16 notation means the first 16 bits are fixed, leaving 16 bits for host addresses.

**Subnet Configuration**: Subnets are the next important setting because every vnet needs at least one subnet. When you create a vnet in the Portal, it will prompt you to create at least one subnet since vnets aren't very useful without them. You'll give each subnet its own IP range within the vnet's range. For example, if your vnet is 10.0.0.0/16, you might have a frontend subnet at 10.0.1.0/24 and a backend subnet at 10.0.2.0/24. You can create multiple subnets to isolate workloads in a single vnet.

Back to the CLI to create a vnet and some services inside it.

---

## Create a Virtual Network with the CLI

**Create a Resource Group**: Every Azure resource needs a home, so we're starting by creating a resource group for this lab. We're calling it "labs-vnet" and placing it in the East US region. You can use your preferred region, but remember to use the same region consistently throughout the lab. The tags parameter helps you track resources created for this course.

**Create Your Virtual Network**: Let's explore what options are available for creating a vnet by running az network vnet create with the help flag. We're creating a new vnet called "vnet1" with the address space "10.10.0.0/16". This gives us a private network with 65,536 possible IP addresses to allocate.

**Check What Was Created**: We're using az network vnet show to examine what was actually created. The command takes the resource group "labs-vnet" and network name "vnet1". If you look at the JSON output, you'll notice there are no subnets listed yet. When you create a vnet through the Portal, it automatically creates a default subnet for convenience, but the basic CLI command doesn't. Since subnets are where you actually deploy services like VMs and App Services, we need to create at least one subnet to make this vnet useful.

**Understanding Subnets**: Subnets are where you actually deploy services, so you need at least one in your vnet.

---

## Create a Virtual Machine in the VNet

**Create Two Subnets**: Let's create two subnets to demonstrate a common network design pattern - separating frontend and backend resources. This is typical in multi-tier applications where you might put web servers in the frontend and databases in the backend. We're creating the frontend subnet first using az network vnet subnet create with the resource group "labs-vnet", vnet name "vnet1", subnet name "frontend", and address prefix "10.10.1.0/24". This subnet can hold 256 IP addresses. Then we're creating the backend subnet with az network vnet subnet create, using the subnet name "backend" and address prefix "10.10.2.0/24".

**Understanding Address Ranges**: Notice how the subnet address ranges fall within our vnet's 10.10.0.0/16 range. The frontend uses 10.10.1.0/24 giving it addresses from 10.10.1.0 to 10.10.1.255, and the backend uses 10.10.2.0/24 for addresses 10.10.2.0 to 10.10.2.255. Both are carved out of the larger 10.10.0.0/16 space.

**Test Your Understanding**: Here's a question to consider and experiment with - what happens if you try to create overlapping IP address ranges, or use a range that isn't within the parent vnet? The CLI will show you exactly what's allowed and what isn't, which helps you understand the constraints. Azure will reject configurations that would cause routing problems.

**Deploy a VM**: Now let's deploy a Virtual Machine into our vnet to test the networking setup. We covered VMs in detail in the VM lab, so we'll move quickly here. We're using a VM as an easy way to test our networking configuration. We're creating a Linux VM running Ubuntu Server in the frontend subnet using az vm create with the resource group "labs-vnet", VM name "vm01", image "UbuntuLTS", vnet name "vnet1", subnet "frontend", and the generate-ssh-keys flag.

**SSH Configuration**: This command takes care of setting up SSH authentication automatically so you can log into the machine remotely. Azure generates an SSH key pair if you don't already have one, configures the VM with the public key, and stores the private key on your local machine. When the command completes, you'll see the public IP address in the JSON output.

**Finding Windows Images**: If you wanted to create a Windows VM instead of Linux, you'd need to use a different image parameter. Let's explore how to find available images. The az vm image list command will take a long time and return thousands of results. Instead, we can filter by OS name using the offer parameter set to "Windows" and table output for readability. You'll see lots of images with long URN names like "MicrosoftWindowsServer:WindowsServer:2019-Datacenter:latest", but notice the alias column on the right. For Windows Server 2019, the alias is "Win2019Datacenter". You can use that alias in the vm create command's image parameter instead of typing out the full URN.

---

## Connect to the VM

**Get the Public IP**: Once the VM is created, let's get its public IP address. The show command has a special flag for including runtime information. We're using az vm show with the resource group "labs-vnet", VM name "vm01", the show-details flag to include runtime data, a query to extract just the publicIps field, and tab-separated value output. This gives us just the IP address without all the other JSON structure, making it easy to copy or store in a variable.

**Connect via SSH**: Now we can connect using SSH by typing ssh followed by the public IP address. Once you're connected to the VM, check the IP address configuration using the ip address command or just "ip a" for short.

**Understanding IP Addresses**: Here's something important to note - the VM only knows about its private IP address on the vnet. You should see an IP in the 10.10.1.x range, which is from our frontend subnet that uses the 10.10.1.0/24 address space. The VM has no idea about the public IP address. The public IP address is managed outside of the VM by Azure's networking infrastructure. It's part of the public IP resource we saw in the Portal. The private IP is assigned by the vnet and is what the VM uses for all communication within Azure - between VMs, to Azure services, and even for outbound internet traffic which gets NAT'd through the public IP.

**Exit the Session**: Type exit to return to your local machine and close the SSH session.

---

## Explore Networking in the Portal

**View All Resources**: Let's go back to the Portal and open our labs-vnet Resource Group to see all the resources that were created. You'll notice several resources that we didn't explicitly create when we ran the vm create command.

**Automatically Created Resources**: There's a disk resource which is the virtual storage unit attached to the VM containing the operating system and file system. A NIC or Network Interface Card resource connects the VM to the vnet - it's the bridge between the compute resource and the network. A Network Security Group resource controls network access to the VM, acting like a firewall with inbound and outbound rules. A Public IP Address resource is what allows external access to the VM from the internet.

**Resource Visualizer**: Click on Resource Visualizer in the resource group menu to see a diagram of how all these resources are connected. It's a great visual way to understand the relationships between components - you can see the VM connected to the NIC, the NIC connected to the subnet, the NSG applied to the NIC, and the public IP associated with the NIC.

**Default Configurations**: All of these were created with default configurations by the vm create command. In production scenarios, you might want to create and configure these resources independently for more granular control over networking, security, and IP addressing.

---

## Lab

**The Scenario**: The az command line tool is a great tool, but it has one drawback - it's an imperative approach. When you create resources you tell Azure what to do step by step - create this, then create that, then configure this. If you need to re-run scripts, you'll get errors about resources already existing.

**The Solution**: Azure also supports a declarative approach where you describe what the end result should be. These are Azure Resource Manager templates, or ARM templates. With ARM templates, you describe what the end result should be rather than the steps to get there, and you can run them repeatedly to always get the same result - they're idempotent.

**Your Task**: Try exporting an ARM template for the labs-vnet Resource Group. Can you use it to deploy a copy of the resources in a new Resource Group called labs-vnet2? This will give you hands-on experience with infrastructure as code in Azure. Look for the export template option in the Portal for the resource group, download the template JSON file, and then use az deployment group create to deploy it to a new resource group. You might need to modify some parameters like names to avoid conflicts.

**Why This Matters**: This is a valuable skill because ARM templates and other infrastructure as code tools like Bicep and Terraform are how production Azure environments are managed at scale.

---

## Cleanup

**Delete Azure Resources**: When you're finished with the lab and the challenge, delete the Resource Groups to remove all resources and avoid ongoing charges. We're running az group delete with the -y flag to skip confirmation, and the resource group name "labs-vnet". If you completed the challenge, also delete the second resource group using az group delete with the -y flag and resource group name "labs-vnet2".

**Why Cleanup Matters**: This ensures you're not charged for resources you're no longer using. The deletion process removes all resources within each group - VMs, disks, network interfaces, NSGs, public IPs, vnets, subnets, everything.
