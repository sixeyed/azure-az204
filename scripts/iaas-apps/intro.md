# IaaS Apps - Introduction Narration Script

## Opening
Welcome to this lab on deploying applications using Azure Infrastructure-as-a-Service.

## What You'll Learn
In this hands-on lab, you'll learn how to deploy traditional applications to Azure using IaaS resources. While Platform-as-a-Service solutions are often the end goal for cloud-native applications, IaaS provides a straightforward migration path for existing workloads.

## Lab Scenario
Today, we'll be working with a legacy .NET Framework application - the kind of application many organizations still run in production. This application uses Windows Server and SQL Server, both of which are fully supported in Azure.

## Key Concepts
Infrastructure-as-a-Service gives you complete control over your virtual machines. You manage the operating system, runtime, and application configuration. This makes IaaS an excellent choice when:
- Migrating existing applications to the cloud
- Applications require specific operating system configurations
- You need full control over the infrastructure

## What We'll Build
We'll create a complete application environment including:
- A SQL Database to store application data
- A Windows Server virtual machine running the latest Windows Server 2022
- An IIS web server hosting a .NET Framework application
- Network configuration to securely connect these components

## Prerequisites
Before we begin, make sure you have:
- An active Azure subscription
- Azure CLI installed and configured
- A Remote Desktop client for connecting to Windows VMs
- Basic familiarity with PowerShell commands

## Lab Architecture
Our architecture is straightforward: a Windows Server VM in a virtual network, connected to an Azure SQL Database. The VM runs IIS as the web server, hosting our .NET Framework 4.8 application.

## Time to Complete
This lab typically takes about 45 minutes to complete, including resource provisioning time.

Let's get started by creating our Azure resources.
