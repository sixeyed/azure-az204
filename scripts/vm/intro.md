# Virtual Machines - Introduction

Welcome to this lab on Azure Virtual Machines. In this session, we'll explore how Azure VMs provide cloud-based compute resources that function just like VMs in your datacenter or on your desktop.

## What Are Azure Virtual Machines?

Virtual Machines in Azure are isolated compute environments running a full operating system. You have complete administrative permissions to install and configure whatever software you need. Azure supports both Linux and Windows VMs, with a large selection of preconfigured images and compute sizes to choose from.

## Key Concepts We'll Cover

In this lab, you'll learn about:

**VM Images** - Understanding what preconfigured operating system images are available and how to select the right one for your workload.

**VM Sizes** - How to choose the appropriate compute capacity based on your requirements, and how size affects your costs.

**Authentication and Connectivity** - Different methods to securely connect to your virtual machines, including SSH for Linux and RDP for Windows.

**Resource Dependencies** - What other Azure resources are required to run a VM, such as virtual networks, network interfaces, and disks.

**Disk Configuration** - How to add storage to your VMs and understand the performance differences between disk types.

**Network Security** - Configuring network access at the port level using Network Security Groups.

## What You'll Do

First, we'll explore Virtual Machines through the Azure Portal to understand all the configuration options available.

Then, we'll use the Azure CLI to create and manage a Linux VM. You'll create a resource group named RESOURCE_GROUP_NAME in LOCATION. We'll deploy an Ubuntu Server VM and learn how to connect to it via SSH.

By the end of this lab, you'll understand how to provision and manage virtual machines in Azure using both the portal and command-line tools.

Let's get started by exploring VMs in the Azure Portal.
