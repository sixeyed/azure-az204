# VM Configuration Automation - Introduction

Welcome to this lab on automating VM configuration in Azure.

## The Challenge

When you create new virtual machines in Azure, they start with a base operating system image, but they rarely have everything you need for your specific workload. You need to install software, configure settings, and prepare the environment.

Doing this manually is problematic. It's time-consuming - you have to log into each VM and run commands. It's error-prone - you might miss steps or make typos. And it doesn't scale - imagine doing this for dozens or hundreds of VMs.

## Azure Solutions

Azure provides multiple options to automate VM configuration. You can configure VMs during deployment, or after they're created. In this lab, we'll explore several approaches:

**VM Extensions** are add-on components that run after the VM is created. They can execute scripts, install monitoring agents, or configure security settings. The custom script extension is particularly useful - it can run shell scripts on Linux or PowerShell scripts on Windows.

**VM Applications** let you package and distribute software as reusable components that can be attached to multiple VMs.

**Cloud-init** is a Linux-specific tool that configures VMs during the first boot. It's widely used in cloud environments for initial setup tasks.

**Run Commands** provide an alternative approach - they execute scripts on demand without installing an extension first.

## What You'll Learn

In this lab, you'll use the custom script extension to install a web server on a Linux VM. You'll configure network security to allow web traffic. You'll also use run commands on a Windows VM to install development tools.

By the end of this lab, you'll understand how to automate VM configuration and eliminate manual setup tasks.

Let's get started.
