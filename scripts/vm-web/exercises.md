# Virtual Machines - Web Server: Exercise Walkthrough

## Exploring the Portal

Let's start by opening the Azure Portal and searching for Virtual Machine resources. This will help us understand what we're about to create using the CLI.

Click on "Create" and navigate through the configuration tabs. Notice under the Networking tab, you'll see options for:
- Public IP Address - this is a separate resource that needs to be created
- You can't choose the actual IP address itself - Azure manages that
- Network Security Group configuration
- Options to automatically delete the PIP and NSG when the VM is deleted

This exploration helps you understand the resources involved. Now let's create these resources using the Azure CLI.

## Creating the Resource Group

First, we need a Resource Group to contain all our VM-related resources.

We'll use the command:
```
az group create -n [resource-group-name] --tags courselabs=azure -l [location]
```

Replace the bracketed values with your preferred resource group name and location. I'm using a location that's available in my subscription.

The command executes, and we can see our resource group has been created successfully.

## Creating the Linux VM with DNS

Now for the main event - creating our Ubuntu Server VM. The key here is that we want to specify a public DNS name, which will make it easy to access our web server.

Let's check the help first:
```
az vm create --help
```

Looking through the parameters, we can see there's a parameter called `public-ip-address-dns-name` - that's exactly what we need.

Here's the command:
```
az vm create -l [location] -g [resource-group-name] -n [vm-name] --image UbuntuLTS --size [vm-size] --public-ip-address-dns-name [unique-dns-name]
```

The DNS name needs to be unique within the region. Azure is now creating our VM along with all the associated resources - the virtual network, subnet, network interface, public IP, and network security group.

This will take a minute or two to complete.

## Examining the Public IP

Great, our VM is created. Now let's look at the Public IP address that was automatically created.

First, let's list all the PIPs in our resource group:
```
az network public-ip list -o table -g [resource-group-name]
```

We can see our public IP resource listed here. To get more details including the fully qualified domain name:
```
az network public-ip show -g [resource-group-name] -n [pip-name]
```

In the output, you'll see the FQDN - it's in the format: your-dns-name.location.cloudapp.azure.com

This FQDN will remain constant even if the actual IP address changes, making it perfect for accessing our web server.

## Installing Nginx

Now let's connect to our VM and install the web server. Using SSH with our FQDN:
```
ssh [your-fqdn]
```

Accept the fingerprint prompt, and we're connected to our Ubuntu VM.

Now let's install Nginx:
```
sudo apt update && sudo apt install -y nginx
```

The package manager is updating and installing Nginx. This will take a moment.

Once installation is complete, let's test it locally:
```
curl localhost
```

Perfect! We can see the Nginx welcome page HTML. The web server is running on the VM.

Now let's try accessing it from outside. Opening a browser and navigating to http://[your-fqdn]...

Hmm, the connection times out. The server is running, so what's the problem?

## Configuring the Network Security Group

The issue is the Network Security Group - it's blocking incoming traffic on port 80. Let's fix that using the Portal, which gives us a nice visual interface for this type of troubleshooting.

In the Portal, navigate to your Resource Group and find the Network Security Group resource - it's named after your VM with "NSG" appended.

On the Overview page, you can see the inbound security rules:
- Port 22 is allowed - that's for SSH, which is why we could connect
- Ports 65000 and above are allowed for Azure services
- Everything else is blocked by the default DenyAllInbound rule

Click on "Inbound security rules" on the left menu, then "Add" to create a new rule.

We'll configure it to:
- Allow HTTP traffic (port 80)
- From any source
- To any destination
- Give it an appropriate name and priority

Click "Add" and wait for the rule to be created.

Now let's refresh our browser...

Excellent! The Nginx welcome page loads successfully. Our web server is now accessible from the internet.

## Managing VM State

Virtual Machines are billed while they're running. If you want to pause your work but keep the VM for later, you need to understand the difference between stopping and deallocating.

Simply stopping a VM still incurs charges. To stop billing, you need to deallocate the VM:
```
az vm deallocate -g [resource-group-name] -n [vm-name]
```

This will take a moment as Azure releases the resources.

Now let's check our Public IP again:
```
az network public-ip show -g [resource-group-name] -n [pip-name]
```

Notice something interesting - the IP address field is now empty. Deallocating the VM released the public IP address back to Azure's pool.

If we restart the VM, it will get a new IP address, but the FQDN will still work because Azure automatically updates the DNS record.

## Lab Challenge

Here's a challenge for you: what if you need a fixed IP address that doesn't change even when the VM is deallocated?

Azure supports static IP addresses for Public IPs. Try configuring your PIP to use a static allocation method instead of dynamic, then verify the IP address is retained when you start, stop, and deallocate the VM.

This is a common requirement for production scenarios where you might have external systems that reference your IP address directly.

## Cleanup

When you're done experimenting, don't forget to clean up your resources to avoid unnecessary charges:
```
az group delete -y -n [resource-group-name]
```

This removes the resource group and all resources within it.

That concludes this lab on running a web server on Azure Virtual Machines. You've learned how to create VMs, manage networking, configure security, and control costs through proper resource management.
