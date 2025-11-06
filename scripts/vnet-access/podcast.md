# Securing VNet Access - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on securing Virtual Network access in Azure. Today we're diving into one of the most critical aspects of cloud security: controlling network access to your Azure resources. Whether you're preparing for the Azure AZ-204 certification or building production applications, understanding how to lock down network traffic is essential.

## The Challenge of Network Security

Imagine you're building a web application with multiple tiers. Your web servers need to be accessible from the internet so users can reach your site, but your database servers should only be reachable from within your private network. And when you need to manage these servers for updates or troubleshooting, you certainly don't want to expose SSH or RDP ports to the entire internet where attackers can probe them.

This scenario represents a fundamental challenge in cloud architecture: how do you provide necessary access while maintaining strict security?

Azure Virtual Networks give you powerful options for restricting and controlling traffic to services. In this episode, we'll explore three key capabilities that work together to solve this challenge.

First, we'll discuss Network Security Groups, or NSGs. These are the primary mechanism for defining rules that allow or deny traffic from specific sources and to specific ports. Think of them as firewalls at the network layer, controlling what can flow in and out of your networks.

Second, we'll examine Azure Bastion, which provides a way to securely access virtual machines that are in networks without public access. This is crucial when you've locked down your VMs with NSG rules but still need administrative access.

Finally, we'll explore VNet peering, which allows you to join virtual networks together when different parts of your application need to communicate with each other, even across different networks or regions.

## Network Security Groups: Your First Line of Defense

Let's start by understanding Network Security Groups in depth. An NSG acts as a virtual firewall that controls inbound and outbound traffic to Azure resources. You can think of it as a collection of security rules that either allow or deny network traffic.

When you create an NSG, Azure automatically applies a set of default rules before you add any custom ones. These defaults provide a security-first baseline. They allow incoming traffic from within the VNet so resources can communicate with each other, allow incoming from Azure Load Balancer so health probes work, and then deny all other incoming traffic by default. For outbound traffic, they allow connections to the VNet and internet for typical connectivity needs, with a default deny for everything else.

This default configuration is intentionally restrictive. It's much safer to start locked down and explicitly allow what you need, rather than starting wide open and trying to remember to block everything dangerous.

### Creating and Configuring NSGs

When you create an NSG using the Azure CLI, there's an important detail to understand about regional placement. Network Security Groups must be in the same region as the virtual networks they protect. If your NSG ends up in a different region than your VNet, you won't be able to associate them. Azure has strict rules about network resource co-location.

The Azure CLI tries to be helpful by defaulting to a region, but that default might not match where you created your VNet. That's why it's important to always explicitly specify the location parameter when creating network resources. If you forget and create an NSG in the wrong region, you'll need to delete it and recreate it in the correct location. It's a small detail, but it can save you troubleshooting time later.

### Understanding NSG Rule Priority

One of the most important concepts with NSGs is how rule priority works. Each rule has a priority number between 100 and 4096. Lower numbers are evaluated first, and once a rule matches the traffic, processing stops. This means a rule with priority 100 is checked before a rule with priority 200.

This priority system gives you fine-grained control. For example, you might want to allow HTTP traffic from the internet on port 80, which you could do with a rule at priority 100. The default deny rule that blocks all other inbound traffic has a much higher priority number, so it doesn't interfere with your allow rule.

The rules are also stateful, which is important to understand. When you allow inbound traffic on port 80, you don't need a separate rule to allow the response traffic back out. Azure automatically tracks connections and allows return traffic.

### Attaching NSGs to Subnets

NSGs can be associated at two different levels: at the subnet level or at the individual network interface card level. When you attach an NSG to a subnet, it automatically applies to all resources deployed into that subnet. This is the most common approach because it provides consistent security policies across all VMs in a subnet.

When you deploy a VM into a subnet that already has an NSG attached, the VM automatically inherits those security rules. You don't need to explicitly configure the NSG during VM creation. The association happens transparently through the subnet.

This subnet-level approach makes security management much easier. Instead of configuring rules for each individual VM, you define the security policy once at the subnet level, and it applies to everything in that subnet.

## The Problem with Traditional Remote Access

Now, here's where things get interesting. Let's say you've created a Network Security Group that allows port 80 for HTTP traffic but blocks everything else. This is great for security, but how do you manage your virtual machines?

Traditionally, you would need to open ports 22 for SSH or 3389 for RDP in your NSG rules. But opening these management ports to the internet is a significant security risk. These ports are constantly scanned and probed by attackers looking for vulnerable systems. Even with strong passwords and keys, exposing these ports increases your attack surface.

You could add NSG rules that only allow SSH from your office IP address, but what if you need to access the VMs from different locations? What if your IP address changes? Managing these rules becomes complex quickly.

This is the exact problem that Azure Bastion solves.

## Azure Bastion: Secure Management Access

Azure Bastion is a fully managed service that provides secure RDP and SSH connectivity to your virtual machines through the Azure Portal, without exposing those management ports to the internet.

Here's how it works: Bastion is deployed at the VNet level as a managed service. It sits in its own dedicated subnet called AzureBastionSubnet. When you want to connect to a VM, you initiate the connection through the Azure Portal, and Bastion establishes a secure connection to your VM using the private IP address.

The beauty of this approach is that your VM never needs a public IP for management access, and you never need to open ports 22 or 3389 in your NSG rules. Bastion handles the connectivity using its own secure channel.

From the user's perspective, when you connect through Bastion, a new browser window opens with a terminal session to your VM. You enter your credentials, and you're connected. But under the hood, Bastion is using HTML5 to stream the RDP or SSH session through a secure websocket connection. Port 22 remains completely blocked for direct access from the internet.

One Bastion instance can serve all VMs in a VNet, making it a cost-effective solution. Instead of needing jump boxes or VPN connections for each environment, you deploy Bastion once per VNet, and all your VMs in that network can be accessed securely through it.

### Bastion Deployment

When you deploy Bastion through the Portal, Azure handles the infrastructure provisioning for you. It creates the dedicated subnet if it doesn't exist, provisions the Bastion host with appropriate compute resources, and configures all the necessary networking. This takes a few minutes, but once it's ready, it's immediately available for connecting to VMs.

The deployment creates a managed service, which means you don't have to worry about patching, updating, or maintaining the Bastion infrastructure. Microsoft handles all of that. You just use the service to connect to your VMs.

### Testing Secured Access

Once you've deployed Bastion and connected to a VM, you can test that your security is working correctly. For example, if you install a web server like Nginx on the VM, you should be able to browse to the VM's public IP on port 80 and see the web page, because your NSG allows that traffic. But if you try to SSH directly to the public IP on port 22, the connection will time out and fail, because that port is blocked by the NSG.

This demonstrates the power of combining NSGs with Bastion. You get granular control over which services are accessible from the internet, while still maintaining secure administrative access through Bastion.

## VNet Peering: Connecting Networks

Now let's talk about a different but related challenge: connecting virtual networks together.

In Azure, virtual networks are isolated by default. Even if two VNets are in the same resource group and subscription, resources in one VNet cannot communicate with resources in another VNet without additional configuration. This isolation is intentional for security, but sometimes different parts of your application architecture need to communicate across network boundaries.

VNet peering is the solution. It creates a connection between two virtual networks, allowing resources to communicate using private IP addresses.

### Planning Address Spaces

Before you can peer virtual networks, you need to ensure they have non-overlapping address spaces. This is a fundamental requirement. If two VNets both use the 10.10.0.0/16 address range, Azure won't be able to route traffic between them, because it won't know which network a particular 10.10.x.x address belongs to.

That's why planning your address spaces in advance is so important. You might use 10.10.0.0/16 for one VNet and 10.20.0.0/16 for another, ensuring they're completely separate ranges with no overlap.

This planning becomes especially important when you need to connect to on-premises networks or plan for future growth. You want to allocate address spaces that won't conflict with other networks you might need to connect to later.

### Creating Bidirectional Peering

VNet peering must be configured in both directions. This might seem redundant, but it's actually an important security feature. You can't peer onto someone else's VNet without their permission. Each VNet administrator must explicitly create the peering connection from their side.

So if you want to connect VNet1 and VNet2, you create one peering from VNet1 to VNet2, and another peering from VNet2 to VNet1. Only when both peerings are in place and show a "Connected" status can resources communicate between the networks.

The configuration uses the Azure CLI with commands that specify the resource group, the name for the peering connection, which VNet you're creating the peering in, which remote VNet you're peering to, and flags to allow VNet access.

### How Peering Works

One interesting aspect of VNet peering is that it's completely transparent to the virtual machines. When you peer two VNets and then check the network interfaces on a VM, you won't see any new network adapters or routes added. The VM just has its single network interface with its private IP address from its subnet.

The peering operates at the Azure network fabric level, below the VM's awareness. When a VM tries to send traffic to an IP address in a peered VNet's address range, Azure's software-defined networking automatically routes that traffic through the peering connection. Your VM doesn't need to know anything about the peering. It just sends packets to an IP address, and Azure delivers them through the appropriate path.

This is very different from traditional VPN connections, which often require configuration on the endpoints. With VNet peering, it's purely a network-level configuration in Azure's infrastructure.

### Cross-Region Peering

VNet peering can work across Azure regions, which is called Global VNet Peering. You might have a VNet in East US and another in West Europe, and you can peer them together. Resources in your East US network can communicate with resources in West Europe using private IP addresses, and that traffic flows over Microsoft's global backbone network, not the public internet.

This provides better security, lower latency, and more reliable connectivity compared to routing traffic over the public internet. The ability to peer across regions is powerful for building globally distributed applications with private connectivity between components.

### Testing Peered Connectivity

When you first create two VNets without peering, VMs in different VNets cannot communicate, even if they're in the same subscription and resource group. If you SSH to a VM in one VNet and try to use curl to reach a web server in another VNet by its private IP, the connection times out.

But as soon as you create the peering connections in both directions, connectivity is immediately established. Running the same curl command again succeeds, and you can see the web server's response. The VMs can now communicate using their private IP addresses through the peering.

This demonstrates how VNets are isolated by default, and how peering explicitly connects them together.

## Security Across Peered Networks

Here's an important security consideration: when you peer two VNets, resources in the peered networks can communicate with each other. But what if you want to control exactly which ports they can use?

This is where NSG rules become even more important. In the examples we've discussed, we might have an NSG that allows port 80 from the internet. But VMs in a peered VNet can access any port on the target VM, including SSH on port 22 and any other services running.

You can create more sophisticated NSG rules that use the peered subnet's address prefix as the source. For example, you could add a rule that explicitly denies port 22 from the peered subnet's address range, while still allowing port 80. By using different priority numbers, you can layer these rules to create exactly the security policy you need.

You might create a deny rule for SSH from the peered subnet with priority 90, which is evaluated before your general allow rule for HTTP with priority 100. This way, internet traffic can still reach port 80, but the peered VMs are blocked from accessing SSH while still able to access the web service.

This layered approach to security rules gives you very granular control over cross-network access.

## Relevance to the AZ-204 Exam

Understanding network security is absolutely critical for the Azure AZ-204 Developer Associate certification. These concepts appear throughout the exam in multiple domains.

### Network Security Groups in the Exam

For NSGs, the exam expects you to understand that they act as virtual firewalls at the subnet or network interface level, rules are evaluated by priority with lower numbers first, default rules provide a secure baseline, and you create custom rules to allow specific traffic patterns.

Common exam scenarios include questions like: "A web application needs to be accessible on port 443 but protected from SSH access" - which requires NSG configuration. Or "Isolate database tier from public internet" - which uses subnet-level NSG application. Or "Allow traffic only from a specific IP range" - which tests your understanding of source address prefix configuration.

You should know the Azure CLI commands for creating NSGs, creating rules, and associating NSGs with subnets. The exam often includes questions where you need to identify the correct command syntax or parameters.

### Azure Bastion in the Exam

For Bastion, the exam expects you to know that it provides secure RDP and SSH access through the Azure Portal without public IPs on VMs, no need to open ports 22 or 3389 in NSG rules, it's deployed at the VNet level and can serve multiple VMs, and it requires a dedicated subnet named AzureBastionSubnet.

Common scenarios include: "Provide secure access to VMs without public IPs" where Bastion is the solution, or "Administrator access to production VMs in locked-down network" as a Bastion use case, or "Eliminate need for jump boxes" as a Bastion advantage.

The key concept for the exam is that Bastion is the recommended approach over traditional jump boxes or opening SSH and RDP ports to the internet.

### VNet Peering in the Exam

VNet peering is a critical networking concept that frequently appears on the exam. You need to understand that peering connects two VNets allowing resources to communicate, must be configured bidirectionally, VNets must have non-overlapping address spaces, can work across regions with Global VNet Peering, and can work across subscriptions.

You also need to know that traffic between peered VNets uses Microsoft's backbone network, not the public internet, and that peering is non-transitive. This last point is important: if VNet A peers to VNet B, and VNet B peers to VNet C, that doesn't mean VNet A can reach VNet C. Each peering connection is independent.

Common exam scenarios include connecting application VNets to database VNets using peering, enabling cross-region VM communication with Global VNet Peering, and recognizing when peering is not possible, such as when two VNets have overlapping address spaces.

### Troubleshooting Scenarios

The exam frequently includes troubleshooting scenarios where you need to diagnose connectivity problems. Common issues include: "VM cannot communicate with another VM" - check NSG rules and VNet peering status. "Cannot access VM via SSH" - check NSG rules or consider Bastion. "Web traffic not reaching application" - check NSG rules and verify rule priorities. "VNet peering shows disconnected" - check that both sides are configured and verify permissions.

Understanding the systematic approach to troubleshooting these issues is just as important as knowing how to configure them correctly in the first place.

### Planning and Best Practices

The exam also tests your knowledge of Azure security best practices. Always use NSGs to limit network access. Never expose management ports to the internet. Use Bastion instead of public IPs for VM management. Apply the principle of least privilege in NSG rules, allowing only the minimum necessary access. And use subnet-level NSGs for broad policies with NIC-level NSGs for specific exceptions when needed.

Planning address spaces is another exam topic. You need to understand CIDR notation and be able to identify when address ranges will conflict. The exam might present a scenario where you need to peer VNets later, so you must choose non-overlapping address spaces from the beginning. Or you might need to avoid conflicts with on-premises networks when planning hybrid connectivity.

### Cost Considerations

The exam may also test cost optimization knowledge. Bastion has a fixed hourly cost regardless of the number of VMs it serves, making it economical for multiple VMs. VNet peering has data transfer charges, with ingress free but egress charged. NSGs themselves are free, with no cost for rules or associations. And public IPs have small hourly costs that can add up across many VMs.

## Integration with Other Azure Services

These networking concepts don't exist in isolation. As an Azure developer, you'll use NSGs, Bastion, and VNet peering in combination with other Azure services.

For example, when deploying microservices architectures, you might use VNet peering to connect the network hosting your AKS cluster to a network with managed databases, while using NSGs to control exactly which services can communicate.

When building multi-tier web applications, you might have one subnet for web servers with NSG rules allowing port 443 from the internet, another subnet for application servers with rules only allowing traffic from the web tier, and a third subnet for databases allowing only application tier access.

For hybrid scenarios connecting to on-premises systems, you might use VPN Gateway or ExpressRoute for the site-to-site connection, then use VNet peering to extend that connectivity to other VNets in Azure, with NSGs controlling security boundaries.

When implementing DevOps pipelines, you might use Bastion to securely access build agents in locked-down networks, or use VNet peering to connect deployment networks to target environments.

## Related Topics for Further Study

This lab connects to several related topics that you should study for the AZ-204 exam:

Service Endpoints allow you to extend VNet private address space to Azure PaaS services like Storage and SQL Database, allowing you to secure those services to only be accessible from specific VNets.

Private Link provides private connectivity to Azure services using private IP addresses, bringing PaaS services into your VNet.

Application Gateway and Web Application Firewall provide layer 7 load balancing and web security.

Azure Firewall provides network-level protection with sophisticated threat intelligence and logging.

And Network Watcher provides monitoring, diagnostics, and troubleshooting tools for Azure networking.

Each of these builds on the foundational concepts we've covered today.

## Practical Application

In real-world Azure development, these skills are essential. You'll use them when deploying production applications with security requirements, implementing compliance frameworks that mandate network isolation, building multi-region architectures with private connectivity, integrating with on-premises systems, securing APIs and web applications, and implementing zero-trust security models.

The hands-on experience with these concepts is invaluable. The AZ-204 exam includes scenario-based questions that require practical knowledge, not just memorization. Understanding how to create and configure NSGs, when to use Bastion versus other access methods, how to set up VNet peering and its limitations, how to plan network architecture with proper address spaces, and how to troubleshoot common networking issues gives you real skills that apply both to the exam and to your career.

## Key Takeaways

Let me summarize the key points for securing VNet access:

Network Security Groups provide firewall capabilities at the subnet and network interface level, with rules evaluated by priority to allow or deny traffic. Default rules provide a secure baseline, and you layer custom rules on top to enable necessary access.

Azure Bastion provides secure RDP and SSH access to VMs without exposing management ports to the internet. It's a managed service deployed at the VNet level that eliminates the need for jump boxes and reduces your attack surface.

VNet peering connects virtual networks together, allowing private IP communication between resources in different VNets. It must be configured bidirectionally, requires non-overlapping address spaces, and can work across regions and subscriptions.

These three capabilities work together to give you granular control over network security in Azure. You can expose exactly the services you need to the internet, secure administrative access through Bastion, and connect networks privately through peering, all while maintaining strict security controls through NSG rules.

## Final Thoughts

Network security is foundational to building secure Azure solutions. Whether you're preparing for the AZ-204 exam or building production applications, understanding these concepts is essential.

The exam tests both your theoretical knowledge and practical skills. You need to know the concepts, understand when to apply them, and be able to configure them using the Azure CLI and Portal. The scenarios we've discussed represent real-world challenges that you'll face as an Azure developer.

As you continue studying, practice creating these configurations yourself. Set up VNets with different address spaces, create NSG rules with different priorities, deploy Bastion and connect to secured VMs, and configure VNet peering to see how it enables connectivity. This hands-on experience will make the concepts concrete and give you confidence both for the exam and for real projects.

Thanks for listening to this episode on securing VNet access in Azure. I hope this gives you a solid understanding of Network Security Groups, Azure Bastion, and VNet peering, and how they relate to the AZ-204 certification. Good luck with your studies!
