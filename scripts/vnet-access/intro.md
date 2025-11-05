# Securing VNet Access - Introduction

Welcome to this lab on securing Virtual Network access in Azure.

In this lab, we'll explore how to lock down network access to resources using Azure's networking security features.

## What We'll Cover

Virtual Networks give you powerful options for restricting and controlling traffic to services in Azure. Today we'll focus on three key capabilities:

First, we'll work with Network Security Groups - or NSGs. These are the primary mechanism for defining rules that allow or deny traffic from specific sources and to specific ports. Think of them as firewalls at the network layer.

Second, we'll use Azure Bastion to securely access virtual machines that are in networks without public access. This is a critical capability when you've locked down your VMs with NSG rules.

Finally, we'll explore VNet peering - a way to join virtual networks together when different parts of your application need to communicate with each other, even across different networks or regions.

## Real-World Scenario

Imagine you're building a web application with multiple tiers. Your web servers need to be accessible from the internet, but your database servers should only be reachable from within your private network. And when you need to manage these servers, you don't want to expose SSH or RDP ports to the entire internet.

This is exactly the type of scenario where Network Security Groups, Bastion, and VNet peering become essential tools in your Azure toolkit.

## Learning Objectives

By the end of this lab, you'll be able to:
- Create and configure Network Security Groups with custom rules
- Understand default NSG rules and how they affect traffic
- Deploy Azure Bastion to securely access VMs in locked-down networks
- Set up VNet peering to enable communication between different virtual networks
- Apply NSG rules to control traffic between peered networks

Let's get started by creating our first virtual network and securing it with a Network Security Group.
