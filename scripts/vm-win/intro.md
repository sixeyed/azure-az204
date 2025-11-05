# Virtual Machines - Windows: Introduction

## Opening

Welcome to this lab on Windows Virtual Machines in Azure. In this session, we'll explore how to create and configure Windows VMs for use as cloud-based development workstations.

## Why Windows VMs Matter

Virtual Machines are one of the core compute options in Azure, and Windows VMs serve an important role beyond traditional server workloads. They're particularly useful as workstation machines that you can access from anywhere.

Imagine having a powerful development machine with all your tools pre-configured - Visual Studio, Docker, Git, and whatever else you need - available from any location. You only pay for the compute when the VM is actually running, which makes it a cost-effective solution for developers who work remotely or need access to powerful hardware.

## What We'll Cover

In this lab, we'll walk through several key aspects of working with Windows VMs:

First, we'll explore Windows VMs in the Azure Portal to understand the configuration options and how they differ from Linux VMs.

Then, we'll use the Azure CLI to create a Windows 11 VM programmatically. This includes selecting the right VM size, finding the correct OS image, and configuring network access.

Next, we'll add a data disk to our VM. This is important because data disks persist independently from the VM itself, allowing you to retain important data even if you delete and recreate the VM.

Finally, we'll connect to the VM using Remote Desktop Protocol and install standard development tools using a PowerShell script.

## Key Concepts

Throughout this lab, you'll work with several important concepts:

**VM Sizes**: Azure offers different VM sizes with varying CPU cores, memory, and storage capacity. Windows requires more resources than Linux, so we'll use a larger size - a Standard D4s v5 with 4 cores and 16 GB of RAM.

**OS Images**: Each OS image has a URN (Uniform Resource Name) that identifies the publisher, offer, SKU, and version. For Windows 11, we'll work with images from the MicrosoftWindowsDesktop publisher.

**Disks**: VMs have an OS disk for the operating system and can have additional data disks attached. We'll work with Premium SSD storage for better performance.

**Network Access**: Unlike Linux VMs which typically use SSH on port 22, Windows VMs use Remote Desktop Protocol on port 3389.

## Prerequisites

For this lab, you'll need:

- An active Azure subscription
- The Azure CLI installed and authenticated
- A Remote Desktop client - built-in on Windows, Microsoft Remote Desktop on Mac, or Remmina on Linux
- A strong password ready for the VM admin account

Let's get started creating our Windows development VM in Azure.
