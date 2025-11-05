# Virtual Machines - Web Server - Exercises Introduction

We've covered Virtual Machines for hosting workloads that need 24/7 availability like web servers - but running web servers in the cloud requires understanding public IP addresses, DNS names, and network security beyond just creating VMs. Now let's deploy a web server hands-on.

## What You'll Do

You'll start by **exploring the Portal** to understand VM creation options, focusing on the Networking tab where you'll see Public IP Address configuration as a separate resource with its own lifecycle and properties. You can't choose the actual IP address value - Azure manages the pool assigning one to you - but you can choose dynamic vs static allocation. You'll see helpful options to automatically delete PIPs and NSGs when the VM is deleted, preventing orphaned resources that continue costing money.

Then you'll **create a Linux VM with DNS** using `az vm create` with the crucial parameter `--public-ip-address-dns-name` providing a friendly DNS name that resolves to your VM's public IP. The DNS name must be globally unique within the Azure region in format like "mywebapp-yourname-date". Azure creates the VM along with all associated resources: virtual network for infrastructure, subnet, network interface, public IP for external access, and NSG to control traffic.

You'll **examine the Public IP** using `az network public-ip show` to find the "fqdn" field in format "your-dns-name.location.cloudapp.azure.com". This FQDN remains constant even if the actual IP address changes when you deallocate and restart the VM - perfect for accessing web servers. Azure automatically updates the DNS record.

Next comes **installing Nginx** by connecting via SSH using your FQDN and running `sudo apt update && sudo apt install nginx -y`. You'll test locally with `curl localhost` seeing the Nginx welcome page HTML, confirming the web server runs on port 80. But external access times out - what's blocking it?

You'll **configure the NSG** through the Portal discovering that port 22 is allowed for SSH but everything else is blocked by the default "DenyAllInbound" rule at priority 65500. You'll add a new rule allowing HTTP traffic on port 80 from the Internet with priority 100 (lower numbers take precedence). After the rule applies, the Nginx welcome page loads successfully from the internet.

Finally, you'll **manage VM state** learning the critical difference between stopping and deallocating. You'll run `az vm deallocate` to release compute resources and stop billing. Checking the Public IP again shows the ipAddress field is now empty - deallocating released the dynamic public IP back to Azure's pool. If you restart later, you get a new IP but the FQDN still works - Azure updates the DNS record automatically.

The lab challenge involves **configuring static IP addresses** that don't change even when deallocated - a common production requirement for external systems referencing your IP directly.

The key learning: Web servers need public IPs with DNS names for reliable access, NSGs control traffic with priority-based rules following default-deny security, and proper VM lifecycle management controls costs through deallocation.

Let's build accessible web servers!
