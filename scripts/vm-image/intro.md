# Building Custom VM Images - Introduction Script

## Opening

Welcome to this lab on building custom VM images in Azure. In this session, we'll explore how to create reusable VM images that can significantly improve your deployment efficiency.

## The Problem

When you deploy a virtual machine in Azure, you often need to install applications and configure settings after the VM is created. This works, but there's a significant downside - every time you create a new VM, you have to wait for the entire installation and configuration process to complete. This adds deployment time and increases the complexity of your infrastructure as code.

## The Solution

The alternative approach is to create your own custom VM image from a VM that already has the application deployed and configured. Think of it like taking a snapshot of a fully configured system. Then, any time you create a new VM from that image, the application is already installed and ready to go as soon as the VM comes online.

## What We'll Cover

In this lab, we'll walk through the complete process:

First, we'll create a base VM and deploy an application to it. For this demonstration, we'll use a simple Windows application running on IIS Web Server.

Second, we'll prepare that VM for imaging using the Sysprep tool to generalize the machine.

Third, we'll create an image from the prepared VM.

Finally, we'll use that image to quickly deploy multiple VMs, all with the application pre-installed.

## Use Cases

This technique is particularly valuable when you need to:

- Deploy multiple VMs with identical configurations
- Reduce deployment time for production systems
- Standardize environments across development, testing, and production
- Create templates for commonly used server configurations

## Resources

Throughout this lab, you'll be working with several Azure resources:

- Resource Groups to organize your resources
- Virtual Machines as the base for your image
- VM Images as reusable templates
- Network Security Groups to control access

You'll use the Azure CLI to manage these resources, giving you practical command-line experience that translates directly to real-world scenarios.

Let's get started by creating our base VM.
