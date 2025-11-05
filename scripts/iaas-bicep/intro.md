# IaaS Bicep - Introduction Narration Script

## Opening

Welcome to this lab on automating application deployment with Infrastructure as a Service using Bicep.

## The IaaS Automation Story

When we think about Infrastructure as a Service, it's easy to imagine manually logging into virtual machines and deploying applications by hand. But that's not how we work in modern cloud environments. IaaS doesn't mean manual - it means we have full control over our infrastructure, and we can automate every aspect of it.

In this lab, we're going to demonstrate the power of combining IaaS with Infrastructure as Code using Bicep. We'll model out an entire application stack - including a Windows virtual machine and a SQL Server database - and we'll automate the complete deployment process from infrastructure to application.

## What We'll Build

The scenario we're working with is a .NET web application that needs a SQL Server backend. In a traditional environment, this might take hours or days to set up: provisioning VMs, configuring networks, installing SQL Server, deploying the application, and setting up all the configuration.

With Bicep and Azure IaaS, we can automate all of that into a repeatable, reliable deployment that runs in minutes.

## The Bicep Approach

What makes this approach powerful is how Bicep lets us split our infrastructure model across multiple files. Instead of one massive template that's hard to read and maintain, we can organize our infrastructure logically:

- Core networking resources in one file
- Database resources in another
- Application VMs in a third

These files can reference each other and share variable names, giving us a clean, modular approach to infrastructure as code.

## The Automation Story

But we're not stopping at infrastructure. One of the most powerful features we'll demonstrate is the VM custom script extension. This lets us run PowerShell scripts automatically when the VM is created - scripts that can install dependencies, deploy applications, and configure everything exactly how we need it.

By the end of this lab, we'll have a fully automated deployment pipeline. Run a few commands, and you'll have a complete application stack running in Azure, with no manual intervention required.

Let's get started.
