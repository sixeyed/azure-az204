# Virtual Networks: Exercises Introduction

We've covered why Virtual Networks are fundamental to Azure security and how you need to plan networking architecture up front before deploying applications. Now let's create VNets and subnets, then deploy resources into them.

## What You'll Do

You'll explore Virtual Networks in the Azure Portal to understand the configuration options including address spaces from private CIDR ranges and subnet configuration. You'll see that VNet names don't need to be globally unique - just unique within your Resource Group.

Then you'll use the Azure CLI to create a VNet with the 10.10.0.0/16 address space, giving you 65,536 IP addresses. You'll discover that unlike the Portal, the basic CLI command doesn't create a default subnet - you'll add that yourself.

You'll create two subnets to demonstrate network isolation - a frontend subnet at 10.10.1.0/24 and backend subnet at 10.10.2.0/24. Both carved from the larger VNet address space for organizing different application tiers.

Next, you'll deploy a Linux VM into the frontend subnet and learn how to find VM images using the offer parameter and alias shortcuts. You'll connect via SSH and verify the VM only knows its private IP from the VNet - the public IP is managed externally by Azure.

You'll explore the Portal's Resource Visualizer to see all the networking resources Azure created automatically - the NIC connecting VM to VNet, NSG controlling access, and public IP for external connectivity.

The key learning: VNets provide private network infrastructure where resources communicate securely using private IPs, but you can't typically move resources between VNets later - plan your addressing and subnets carefully from the start.
