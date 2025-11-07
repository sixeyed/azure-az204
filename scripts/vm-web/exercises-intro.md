We've covered Virtual Machines for hosting workloads that need 24/7 availability like web servers, but running web servers in the cloud requires understanding public IP addresses, DNS names, and network security beyond just creating VMs. Now let's deploy a web server hands-on.

When you explore VM in the Portal, focus on the Networking tab where you'll see Public IP Address configuration as a separate resource with its own lifecycle and properties. You can't choose the actual IP address value because Azure manages the pool assigning one to you, but you can choose dynamic versus static allocation. You'll see helpful options to automatically delete PIPs and NSGs when the VM is deleted, preventing orphaned resources that continue costing money.

Creating a Linux VM with a public DNS name uses az vm create with the crucial parameter public-ip-address-dns-name, providing a friendly DNS name that resolves to your VM's public IP. The DNS name must be globally unique within the Azure region in format like mywebapp-yourname-date. Azure creates the VM along with all associated resources: virtual network for infrastructure, subnet, network interface, public IP for external access, and NSG to control traffic.

You examine the Public IP using az network public-ip show to find the fqdn field in format your-dns-name.location.cloudapp.azure.com. This FQDN remains constant even if the actual IP address changes when you deallocate and restart the VM, perfect for accessing web servers. Azure automatically updates the DNS record to point to whatever IP is currently assigned.

Installing a web server on the VM means connecting via SSH using your FQDN and running sudo apt update and sudo apt install nginx. You test locally with curl localhost seeing the Nginx welcome page HTML, confirming the web server runs on port 80. But when you try external access, it times out. What's blocking it? The Network Security Group.

You configure the NSG through the Portal, discovering that port 22 is allowed for SSH but everything else is blocked by the default DenyAllInbound rule at priority 65500. You add a new rule allowing HTTP traffic on port 80 from the Internet with priority 100, and lower numbers take precedence. After the rule applies, the Nginx welcome page loads successfully from the internet.

Stopping and starting the VM teaches the critical difference between stopping and deallocating. You run az vm deallocate to release compute resources and stop billing. Checking the Public IP again shows the ipAddress field is now empty because deallocating released the dynamic public IP back to Azure's pool. If you restart later, you get a new IP but the FQDN still works because Azure updates the DNS record automatically.

The lab challenge involves configuring static IP addresses that don't change even when deallocated, a common production requirement for external systems referencing your IP directly.

Web servers need public IPs with DNS names for reliable access, NSGs control traffic with priority-based rules following default-deny security, and proper VM lifecycle management controls costs through deallocation. Let's build accessible web servers!
