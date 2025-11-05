# Securing VNet Access: Exercises Introduction

We've covered the powerful security features Azure provides for controlling network access including Network Security Groups, Azure Bastion, and VNet peering. Now let's apply these capabilities to lock down and secure virtual networks.

## What You'll Do

You'll create a VNet and subnet, then create a Network Security Group to act as a firewall. You'll examine the default NSG rules that provide a secure baseline - allowing VNet internal traffic and denying all other inbound by default.

Then you'll add a custom rule to allow HTTP traffic on port 80 from the internet and attach the NSG to your subnet. Any resources deployed into that subnet will automatically inherit the security rules.

You'll create a Linux VM in the secured subnet and discover that SSH is now blocked by the NSG - the connection times out because only port 80 is allowed. This is where Azure Bastion comes in.

You'll deploy Bastion at the VNet level to provide secure RDP and SSH access through the Azure Portal without exposing management ports publicly. You'll connect through Bastion and install Nginx, then verify the web server is accessible on the allowed port.

Next, you'll create a second VNet in a different region with non-overlapping address space (10.20.0.0/16 versus 10.10.0.0/16). You'll test connectivity and confirm the VNets are isolated by default - VMs cannot communicate even though they're in the same subscription.

You'll create VNet peering in both directions to connect the networks, then verify VMs can now communicate using private IPs through the peering connection. The lab challenge asks you to update NSG rules so internet traffic reaches port 80 but peered VMs can only access port 80 and not SSH.

The key learning: NSGs provide network-level security, Bastion enables secure management access, and VNet peering connects isolated networks with non-overlapping address spaces - all essential for building secure, multi-tier Azure applications.
