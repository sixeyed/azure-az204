# Virtual Machines - Web Server - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on deploying web servers using Azure Virtual Machines. Today we're exploring one of the most common use cases for VMs in the cloud - hosting web applications. While modern cloud architectures often favor Platform-as-a-Service options like Azure App Service, understanding how to deploy and manage web servers on VMs remains essential knowledge for the Azure AZ-204 certification and for real-world scenarios where you need full control over your hosting environment.

## The Web Server Scenario

Let's start with the fundamental requirements for running a web server in the cloud.

A web server needs to be accessible from the internet 24/7. Users around the world should be able to type a URL into their browser and reach your application. This sounds simple, but it involves several Azure components working together - the virtual machine itself, network connectivity, public IP addressing, DNS resolution, and security controls.

When you run a web server in your own datacenter, you handle these concerns differently. You might have a dedicated public IP address block, internal DNS servers, physical firewalls, and direct control over every network device. In Azure, these functions are abstracted into cloud services and configured through the portal or APIs.

Understanding how these components work together is crucial for both the AZ-204 exam and practical Azure development. You need to know not just how to create a VM, but how to make it accessible, secure it properly, and manage costs effectively.

## Public IP Addresses in Azure

Public IP addresses are a fundamental concept that appears frequently on the AZ-204 exam.

When you create a virtual machine that needs internet connectivity, Azure can create a Public IP resource and associate it with the VM's network interface. This Public IP is a separate resource with its own lifecycle and properties - it's not just a configuration setting on the VM itself.

One key aspect that surprises many people: you cannot choose the actual IP address value. Azure manages pools of public IP addresses, and you get assigned one from those pools. What you can control is whether the assignment is dynamic or static.

With **dynamic allocation**, the IP address may change when you deallocate and restart the VM. The IP is released back to Azure's pool when the VM is deallocated, and you might get a different address when you start it again. This is the default behavior and works well when you're using DNS names rather than hardcoded IP addresses.

With **static allocation**, the IP address is reserved for your resource even when the VM is deallocated. You always get the same address. This is important when external systems reference your IP address directly - perhaps in firewall rules, DNS records managed outside Azure, or configuration files that can't easily be updated.

For the AZ-204 exam, understand this distinction. Questions often present scenarios asking how to ensure a consistent IP address or why an IP address changed after VM restart. The answer involves understanding dynamic versus static allocation.

## DNS Names for Stable Access

While IP addresses are the technical foundation of networking, DNS names provide a user-friendly way to access resources that abstracts away IP address details.

When you create a Public IP in Azure, you can assign it a DNS label. Azure automatically creates a fully qualified domain name in the format `your-label.region.cloudapp.azure.com`. This FQDN remains constant even if the underlying IP address changes.

This is particularly valuable with dynamic IP allocation. When you deallocate and restart a VM, the IP might change, but the FQDN stays the same. Azure automatically updates the DNS record to point to whatever IP gets assigned. Your users or applications always use the same DNS name and automatically follow the updated IP.

For production scenarios, you'd typically use custom domain names through Azure DNS or your own DNS provider. But the Azure-provided FQDNs are perfect for development, testing, and scenarios where custom branding isn't required.

The exam tests your understanding of when to use DNS names versus raw IP addresses and how Azure manages the mapping between them.

## Network Security Groups as Firewalls

Network Security Groups are one of the most important security features in Azure and appear extensively on the AZ-204 exam.

When Azure creates a VM, it automatically creates a Network Security Group and associates it with the VM's network interface or subnet. The NSG acts as a distributed, software-defined firewall that filters traffic based on rules you define.

The default configuration follows a security-first principle: deny all inbound traffic from the internet except for ports explicitly allowed. For a Linux VM, SSH port 22 is typically allowed by default so you can connect. For Windows VMs, RDP port 3389 might be allowed. But application ports like HTTP 80 or HTTPS 443 are blocked until you create rules to allow them.

Each NSG rule specifies several components: the source of traffic (IP ranges, service tags, or "Any"), source port ranges, the destination, destination port ranges, the protocol (TCP, UDP, or Any), the action (Allow or Deny), and a priority number that determines rule order.

Priority is crucial. Lower numbers are evaluated first. Default deny rules have very high priority numbers like 65500, ensuring they're checked last. When you create custom allow rules, you typically use priorities like 100, 200, or 300, ensuring they're evaluated before the default deny.

When you deploy a web server on a VM and can't access it from the internet, the first troubleshooting step is checking NSG rules. This scenario appears frequently on the exam - understanding that network access must be explicitly configured is essential knowledge.

## The Deployment Process

Let's walk through the complete process of deploying a web server on an Azure VM.

You start by creating a resource group to organize your resources. Then you create the VM itself using the Azure CLI, specifying parameters for the location, image, size, and importantly, the public IP DNS name.

When you run the vm create command, Azure provisions multiple resources automatically - the VM itself, a virtual network providing the network infrastructure, a subnet within that VNet, a network interface connecting the VM to the subnet, a public IP address for external access, and a network security group for traffic control.

This automatic provisioning is convenient but important to understand. Each of these is a separate resource that can be managed independently. When you eventually delete the VM, some of these resources might persist if not configured otherwise, potentially continuing to cost money.

Once the VM is running, you connect via SSH using either the IP address or the FQDN. From within the VM, you install your web server software - perhaps Nginx for Linux or IIS for Windows. The installation happens just like it would on a physical or on-premises virtual machine; you're working with a standard operating system with full administrative access.

After installation, you can test locally by connecting to localhost from within the VM. This confirms the web server is running. But when you try to access it from the internet using the public IP or FQDN, the connection fails. This is where NSG configuration comes in.

## Configuring Network Access

The NSG blocks HTTP traffic by default, so you need to create a rule to allow it.

Using the Portal provides a visual interface for NSG management. You navigate to the NSG resource, examine existing rules to understand the current configuration, and create a new rule for HTTP traffic on port 80.

The rule specifies the source as "Any" to allow traffic from anywhere on the internet, the destination port as 80, the protocol as TCP, and the action as Allow. You assign a priority lower than the default deny rule - say, 100 - ensuring your allow rule is evaluated first.

Once the rule is created and propagated, HTTP traffic can reach your VM, and your web server becomes accessible from the internet. Users can now access your application using the public IP or FQDN.

For production scenarios, you'd implement more sophisticated security - perhaps restricting source IPs to known ranges, using HTTPS with SSL certificates, configuring Web Application Firewall, or placing VMs behind Azure Application Gateway or Azure Front Door. But the fundamental concept remains: explicitly configure network access through NSG rules.

## VM State and Cost Management

Understanding VM states and their cost implications is crucial for both the exam and production operations.

When a VM is running, you pay for compute resources - the CPU cores and memory allocated to that VM. This is the primary cost driver for VMs, often more significant than storage or networking costs.

If you stop a VM through the operating system or click Stop in the Portal without deallocating, the compute resources remain allocated. Azure holds those resources for your VM even though it's not running. You continue paying compute charges in this state.

To actually stop compute billing, you must **deallocate** the VM. This releases the compute resources back to Azure's pool. The VM's disks remain (you still pay storage costs), but you're no longer paying for CPU and memory.

When you deallocate a VM with a dynamically allocated public IP, that IP address is released back to the pool. When you start the VM again, you might get a different IP. But if you configured a DNS name, it continues to work because Azure updates the DNS record automatically.

For static public IPs, the address is retained even when the VM is deallocated. This ensures consistency at the cost of ongoing IP address charges - static public IPs cost a small amount even when not in use.

Understanding these state transitions and their billing implications appears regularly on the exam. Questions might ask how to minimize costs during non-business hours, why charges continue after stopping a VM, or how to ensure IP address consistency.

## Resource Lifecycle and Cleanup

One of the most important operational concepts for Azure VMs is resource lifecycle management.

When you create a VM, multiple dependent resources are created. When you delete the VM, what happens to these resources? The answer depends on configuration.

By default, some resources like the OS disk are configured to be deleted when the VM is deleted. But other resources - the network interface, public IP address, network security group, and virtual network - might persist. These orphaned resources continue to cost money even though their associated VM is gone.

This is a common source of unexpected costs and appears on the exam in scenarios about cost optimization. The answer often involves properly cleaning up resources or configuring automatic deletion.

The cleanest cleanup approach is deleting the entire resource group. This cascades to all contained resources, ensuring nothing is left behind. For production environments where resource groups contain many different resources, you might delete VMs individually and explicitly remove associated resources.

The Portal provides options during VM creation to automatically delete dependent resources when the VM is deleted. Enabling these options prevents orphaned resources and simplifies lifecycle management.

## Infrastructure as Code Considerations

While we've discussed interactive deployment using the Portal and CLI, production environments use Infrastructure as Code approaches.

The Azure CLI commands we use interactively can be scripted for repeatability. The same `az vm create` command works in scripts, CI/CD pipelines, and automation workflows.

Beyond CLI scripts, you might use ARM templates or Bicep files for declarative infrastructure definitions. These approaches let you define the desired end state - "I want a VM with these properties, a public IP with this DNS name, and an NSG with these rules" - and Azure figures out how to create everything.

For the AZ-204 exam, understand that automated, repeatable deployments are best practice. Questions about scalable infrastructure or consistent environments often point toward Infrastructure as Code solutions.

## Web Servers and the AZ-204 Exam

Let's connect this specifically to the Azure AZ-204 certification.

VMs appear in the "Implement IaaS Solutions" domain. While PaaS services get more exam coverage, understanding IaaS fundamentals is essential for complete Azure knowledge.

### Key Exam Concepts

Know how to create VMs with public IP addresses and DNS names using the Azure CLI. Understand the parameters and their purposes.

Understand NSG rule configuration - sources, destinations, ports, protocols, priorities, and actions. Be able to troubleshoot connectivity issues by identifying missing rules.

Know the difference between stopping and deallocating VMs and their cost implications. Understand dynamic versus static IP allocation.

Understand resource dependencies and lifecycle. Know what gets created automatically and what persists after VM deletion.

### Common Exam Scenarios

**Scenario 1**: "You deploy a web application to a VM but users cannot access it. What should you check?"

The answer involves verifying NSG rules allow traffic on the appropriate port.

**Scenario 2**: "You need to ensure a VM's public IP address remains constant even when the VM is deallocated. What should you configure?"

Configure the public IP with static allocation.

**Scenario 3**: "You want to minimize costs for development VMs overnight while retaining their configuration. What should you do?"

Deallocate the VMs during non-business hours using automation or schedules.

**Scenario 4**: "After deleting test VMs, your Azure bill still shows charges. What's the likely cause?"

Orphaned resources like static public IPs or premium disks that weren't deleted with the VMs.

## Comparing with PaaS Alternatives

A key exam skill is knowing when to use VMs versus PaaS alternatives like Azure App Service.

Choose VMs when you need full OS control, are running legacy applications that can't be containerized, have specific OS or software requirements, or are lifting and shifting from on-premises.

Choose App Service when you want to focus on application code rather than infrastructure, need automatic scaling and deployment features, want built-in high availability, or are building new cloud-native applications.

The exam presents scenarios and asks you to recommend appropriate services. Understanding the tradeoffs - control versus management overhead, flexibility versus simplicity - helps you make informed recommendations.

## Best Practices for Production

Several best practices emerge from production use of VMs for web servers.

**Use load balancers or Application Gateway** to distribute traffic across multiple VMs for reliability and scale. Don't rely on a single VM for production workloads.

**Implement proper monitoring** with Azure Monitor, Application Insights, and diagnostic logs. Visibility into performance and issues is crucial for production operations.

**Automate configuration** using VM extensions, custom images, or configuration management tools. Manual configuration doesn't scale and leads to inconsistencies.

**Use availability sets or availability zones** to protect against hardware failures and datacenter outages. Understand the SLAs different configurations provide.

**Secure network access** using NSGs, private endpoints, or Azure Firewall. Follow defense-in-depth principles rather than relying on single security layers.

**Plan for updates and patching** to keep the OS and applications secure. Automated patch management or blue-green deployments minimize downtime.

## Final Thoughts

Running web servers on Azure VMs demonstrates fundamental IaaS concepts essential for the AZ-204 certification. While modern applications increasingly use PaaS and serverless options, understanding VMs provides the foundation for appreciating higher-level services and knowing when each is appropriate.

For the exam, focus on networking concepts - public IPs, DNS, and NSGs. Understand VM states and billing. Know resource dependencies and lifecycle. Practice creating and configuring VMs using the CLI. These practical skills translate directly to exam questions and real-world Azure development.

Thanks for listening to this episode on deploying web servers with Azure Virtual Machines. Understanding these IaaS fundamentals provides important foundation knowledge for the AZ-204 certification and practical skills for managing Azure infrastructure. Good luck with your preparation!
