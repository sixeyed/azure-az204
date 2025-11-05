# Virtual Machines - Web Server: Introduction

Welcome to this lab on deploying a web server using Azure Virtual Machines.

## Overview

Virtual Machines are one of the simplest ways to get a workload running in the cloud. They're particularly useful for applications that need to be available 24/7, like web servers. But running a web server in the cloud isn't just about creating a VM - there are additional requirements you need to consider.

## What You'll Learn

In this lab, we'll explore how to:
- Create a Linux virtual machine in Azure
- Configure networking components including public IP addresses
- Set up a DNS name for easy access
- Manually deploy and configure a web server
- Manage network security with Network Security Groups
- Understand the lifecycle of VMs and their associated resources

## Key Concepts

### Public IP Addresses
Web servers need to be accessible from the internet. In Azure, this means you'll need a public IP address resource. Public IPs have their own lifecycle and can be managed independently of the VMs they're attached to.

### DNS Names
While IP addresses can change, especially when you stop and start VMs, a DNS name provides a constant way to access your resources. Azure allows you to assign a fully qualified domain name to your public IP address.

### Network Security Groups
By default, Azure protects your VMs with a Network Security Group, which acts like a firewall. Understanding how to configure these security rules is essential for making your web server accessible while keeping it secure.

## The Scenario

We'll be creating a Linux VM running Ubuntu Server, then manually installing and configuring the Nginx web server. This hands-on approach will give you a clear understanding of what's happening behind the scenes - knowledge that's valuable even when you move to more automated deployment methods later.

Let's get started by exploring what's available in the Azure Portal.
