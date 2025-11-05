# Securing VNet Access: AZ-204 Exam Focus

Great work! This VNet security lab directly addresses the "Implement Azure Security" and "Implement networking for Azure solutions" objectives in the AZ-204 exam. These network security concepts appear frequently in exam scenarios.

## What We'll Cover

We'll examine Network Security Groups as virtual firewalls at the subnet or NIC level. You'll master rule priority (lower numbers evaluated first), default rules that cannot be deleted, stateful rule behavior, and how to create custom rules with specific source address prefixes and port ranges.

We'll explore Azure Bastion as Microsoft's managed solution for secure VM access. You'll understand that Bastion provides RDP/SSH through the Portal without public IPs on VMs, no need to open ports 22 or 3389, deployment at VNet level serving multiple VMs, and the dedicated AzureBastionSubnet requirement.

The exam tests your knowledge of VNet peering for connecting isolated networks - bidirectional configuration required for security, non-overlapping address spaces as a prerequisite, cross-region and cross-subscription capabilities, traffic using Microsoft backbone not public internet, and non-transitive routing behavior.

You'll understand virtual network integration for VMs deployed into specific subnets, NSG application at subnet or NIC level with inheritance, private IP assignment from subnet ranges, and optional public IPs as separate resources.

We'll cover planning address spaces to avoid conflicts when peering VNets or connecting to on-premises networks, NSG rule priority ranges from 100 to 4096, and security best practices including never exposing management ports to internet and using Bastion instead.

The exam includes troubleshooting scenarios - VM connectivity issues, NSG rule conflicts, VNet peering status problems, and cost considerations including Bastion hourly costs and VNet peering data transfer charges.

Master NSG configuration, Bastion deployment, and VNet peering for the AZ-204!
