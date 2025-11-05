# Virtual Machines - Web Server: Exercise Walkthrough

## Exploring the Portal

Let's start by opening the Azure Portal and searching for Virtual Machine resources. This will help us understand what we're about to create using the CLI and see all the options available.

Click on "Create" and navigate through the configuration tabs to familiarize yourself with the VM creation process. Under the Networking tab, you'll see several important options we should understand.

Notice the Public IP Address configuration - this is actually a separate resource that needs to be created alongside your VM. Azure manages this automatically when you create a VM, but it's a distinct resource with its own lifecycle and properties.

Something interesting here - you can't choose the actual IP address value itself. Azure manages the pool of public IP addresses, and you get assigned one from that pool. You can choose between dynamic and static allocation, but not the specific number.

You'll also see Network Security Group configuration options. The NSG is like a firewall that controls what traffic can reach your VM. And notice the helpful checkboxes to automatically delete the PIP and NSG when the VM is deleted - this prevents orphaned resources that continue to cost money.

This exploration helps you understand the various resources involved in a complete VM deployment. Now let's create these resources using the Azure CLI for better repeatability.

## Creating the Resource Group

First, we need a Resource Group to contain all our VM-related resources. Resource groups are organizational containers that help you manage related resources as a unit.

We're using az group create with a resource group name - you can choose your own descriptive name, adding the "courselabs=azure" tag for tracking, and specifying a location. I'm using a location that's available in my subscription - you should choose one that works for you and has capacity.

The command executes quickly, and we can see our resource group has been created successfully with confirmation output showing the location, properties, and tags.

## Creating the Linux VM with DNS

Now for the main event - creating our Ubuntu Server VM. The key here is that we want to specify a public DNS name, which will make it easy to access our web server without memorizing IP addresses.

Let's check the help documentation first by running az vm create with the --help flag. This is always a good practice when learning a new command.

Looking through the parameters in the help output, we can see there's a parameter called "public-ip-address-dns-name" - that's exactly what we need. This creates a friendly DNS name that resolves to our VM's public IP.

Here's what we're doing with the vm create command: specifying the location to match our resource group, the resource group name, a VM name like "web01" to identify this as a web server, the image set to "UbuntuLTS" for Ubuntu Long Term Support, a VM size that you have quota for in your subscription, and the key parameter - public-ip-address-dns-name with a unique value.

The DNS name needs to be globally unique within the Azure region you're deploying to. Something like "mywebapp-yourname-20240315" works well - include your name and maybe a date or random numbers to ensure uniqueness.

Azure is now creating our VM along with all the associated resources - the virtual network provides the network infrastructure, a subnet within that VNet, a network interface that connects the VM to the subnet, a public IP address for external access, and a network security group to control traffic.

This will take a minute or two to complete. You'll see progress indicators as Azure provisions each component.

## Examining the Public IP

Great, our VM is created. Now let's look at the Public IP address resource that was automatically created alongside the VM.

First, let's list all the public IPs in our resource group using az network public-ip list with table output for easy reading and specifying our resource group name.

We can see our public IP resource listed here with its name, resource group, location, and allocation method. To get more detailed information including the fully qualified domain name, we're using az network public-ip show with the resource group and the PIP name from the previous listing.

In the JSON output, look for the "fqdn" field near the dns settings - it's in the format: your-dns-name.location.cloudapp.azure.com. This is your permanent DNS name.

This FQDN will remain constant even if the actual IP address changes, making it perfect for accessing our web server. If you deallocate and restart the VM, you might get a different IP address, but the DNS name stays the same and Azure automatically updates the DNS record.

## Installing Nginx

Now let's connect to our VM and install the web server. We're using SSH with our FQDN to connect. SSH is available by default on Linux, Mac, and modern Windows systems.

Type ssh followed by your FQDN. On the first connection, you'll see a message about the authenticity of the host and a fingerprint. This is normal - accept the fingerprint prompt by typing yes. SSH is now connecting to your Ubuntu VM.

Once connected, we're seeing the Ubuntu welcome message and a command prompt. Now let's install Nginx web server.

We're running sudo apt update to refresh the package manager's database, followed by sudo apt install with the -y flag to automatically accept prompts and nginx as the package name. The package manager is updating its lists and then downloading and installing Nginx. This will take a moment as it retrieves the packages and configures the service.

Once installation is complete, let's test it locally from within the VM. We're running curl localhost to make an HTTP request to the local web server.

Perfect! We can see the Nginx welcome page HTML in the output. The web server is running successfully on port 80.

Now let's try accessing it from outside the VM. Opening a web browser and navigating to http:// followed by your FQDN...

Hmm, the connection times out after a while. The server is definitely running since we just tested it locally, so what's blocking the connection?

## Configuring the Network Security Group

The issue is the Network Security Group - it's acting as a firewall and blocking incoming traffic on port 80. Let's fix that using the Portal, which gives us a nice visual interface for this type of network troubleshooting.

In the Portal, navigate to your Resource Group and find the Network Security Group resource. It's named after your VM with "NSG" appended to the name, like "web01NSG".

On the Overview page, you can see a summary of the inbound security rules currently in effect. Let's examine these:
- Port 22 is allowed - that's for SSH, which is why we could connect earlier
- Ports 65000 and above are allowed for Azure infrastructure services to manage the VM
- Everything else is blocked by the default DenyAllInbound rule at priority 65500

Click on "Inbound security rules" in the left menu, then click the "Add" button to create a new rule.

We'll configure it to allow HTTP traffic. Set the source to "Any" to allow traffic from anywhere on the internet, source port ranges to asterisk for all ports, destination to "Any" meaning all resources protected by this NSG, destination port ranges to 80 for HTTP, protocol to TCP, action to Allow, and give it a priority like 100 which is lower than the deny rule so it takes precedence. Name it something descriptive like "AllowHTTP".

Click "Add" and wait for the rule to be created and applied. This takes a few seconds as Azure updates the NSG and propagates the rule to all the network infrastructure.

Now let's refresh our browser with the VM's FQDN...

Excellent! The Nginx welcome page loads successfully. We can see the "Welcome to nginx!" message and all the default content. Our web server is now accessible from the internet thanks to the NSG rule we just created.

## Managing VM State

Virtual Machines incur compute charges while they're running. If you want to pause your work but keep the VM for later, you need to understand the important difference between stopping and deallocating.

If you just stop a VM through the operating system or the Portal's Stop button, you still incur charges for the allocated resources. To actually stop billing for compute, you need to deallocate the VM.

We're running az vm deallocate with the resource group name and VM name. This command tells Azure to release the compute resources - the CPU cores and memory that were reserved for your VM.

This will take a moment as Azure gracefully shuts down the VM and releases the allocated capacity back to the pool.

Now let's check our Public IP again using az network public-ip show with the resource group and PIP name.

Notice something interesting in the output - the ipAddress field is now empty or null. Deallocating the VM released the public IP address back to Azure's pool. This is the default behavior for dynamically allocated public IPs.

If we restart the VM later, it will get a new IP address from the pool, but here's the important part - the FQDN will still work. Azure automatically updates the DNS record to point to whatever IP address gets assigned, so you can always use the friendly name to access your VM.

## Lab Challenge

Here's a challenge for you to explore: what if you need a fixed IP address that doesn't change even when the VM is deallocated?

Azure supports static IP addresses for Public IPs. Your task is to configure your PIP to use a static allocation method instead of dynamic. Then verify that the IP address is retained when you start, stop, and deallocate the VM.

Look in the Portal under the Public IP resource for the configuration settings where you can change from Dynamic to Static allocation. Try deallocating the VM again after making this change, and see if the IP address persists.

This is a common requirement for production scenarios where you might have external systems that reference your IP address directly, like DNS records managed outside of Azure, firewall rules in partner organizations, or hardcoded configurations that you can't easily update.

## Cleanup

When you're done experimenting with VMs and web servers, don't forget to clean up your resources to avoid unnecessary charges.

We're running az group delete with the -y flag to skip the confirmation prompt and the resource group name.

This removes the resource group and all resources within it - the VM, the disk, the network interface, the network security group, the public IP, the virtual network, and everything else we created. It's the quickest way to clean up an entire environment.

That concludes this lab on running a web server on Azure Virtual Machines. You've learned how to create VMs with friendly DNS names, install and configure web services, manage network security with NSGs, understand public IP address behavior, and control costs through proper resource management and cleanup.
