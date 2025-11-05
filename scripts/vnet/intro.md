# Virtual Networks - Introduction Script

## Opening

Welcome to this lab on Azure Virtual Networks. In this session, we'll explore one of the foundational components of Azure networking that you'll need to understand for both the AZ-204 exam and real-world cloud solutions.

## What are Virtual Networks?

Virtual Networks, or VNets as they're commonly called, are private networks in Azure. They allow your services to communicate with each other securely, without being exposed to the public Internet. Think of a VNet as your own private datacenter network in the cloud.

## Why Virtual Networks Matter

Virtual Networks are a core component in deploying secure solutions in Azure. If you're building production applications, you should aim to use VNets for all your services, provided those services support them.

Here's something critical to understand: once you deploy resources into a VNet, you typically can't move them to a different VNet. This means you need to plan your networking architecture up front, before you start deploying your applications.

## Key Concepts

Let me walk you through the essential concepts you'll need to understand:

### Address Spaces

Every VNet needs an IP address range. You'll use a private CIDR range - typically something like 10.0.0.0/16 or 192.168.0.0/16. This is the overall address space for your entire virtual network.

### Subnets

Within your VNet, you'll create subnets. Every VNet needs at least one subnet, and this is where you actually deploy your services. Each subnet has its own IP range that must fall within the parent VNet's address space.

For example, if your VNet uses 10.10.0.0/16, you might create a frontend subnet with 10.10.1.0/24 and a backend subnet with 10.10.2.0/24.

### Why Multiple Subnets?

You can create multiple subnets to isolate different workloads within a single VNet. This is a common pattern for security and organization - perhaps you want your web servers in one subnet and your database servers in another.

## Naming Requirements

Here's a nice detail: unlike many Azure resources, VNet names don't need to be globally unique. They just need to be unique within the Resource Group. This gives you more flexibility in your naming conventions.

## What You'll Learn

In this lab, we'll:
- Explore Virtual Networks through the Azure Portal
- Create VNets and subnets using the Azure CLI
- Deploy a Virtual Machine into a VNet
- Understand the networking resources that Azure creates automatically
- Learn about Azure Resource Manager templates for network deployment

Let's get started by exploring Virtual Networks in the Azure Portal.
