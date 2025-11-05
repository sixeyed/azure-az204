# App Service for Web Apps - Introduction

## Welcome

Welcome to this lab on Azure App Service for Web Apps. In this session, we'll explore one of Azure's most popular Platform-as-a-Service offerings and see how it simplifies web application deployment and management.

## Understanding PaaS vs IaaS

Before we dive in, let's understand the difference between Infrastructure-as-a-Service and Platform-as-a-Service.

IaaS options, like virtual machines, are great when you need access to the host machine to configure and deploy your application. You have complete control over the operating system, runtime environment, and server configuration. However, this control comes with significant management overhead - you're responsible for patching, updates, security, scaling, and all the infrastructure concerns.

Platform-as-a-Service takes care of all that infrastructure management for you. With PaaS, you can focus on your application code while Azure handles the underlying servers, operating systems, runtime environments, and scaling. The trade-off is that your application needs to be supported within the PaaS environment's constraints.

## What is Azure App Service?

Azure App Service is one of Azure's most popular PaaS offerings. It's a fully managed platform for building, deploying, and scaling web applications. App Service supports multiple programming languages and frameworks including .NET, Java, Node.js, Python, and PHP.

Key features include:
- Built-in auto-scaling capabilities
- Continuous deployment from various sources
- Integration with Azure DevOps and GitHub
- Staging environments for testing
- Built-in load balancing
- Automatic HTTPS

## What We'll Build Today

In this lab, you'll create an App Service deployment by pushing source code directly from your local machine. Azure will compile and configure the application for you automatically.

Specifically, we'll:
- Create an App Service Plan to host our application
- Create a Web App configured for Git deployment
- Deploy an ASP.NET application by pushing code to Azure
- Configure application settings
- Explore the deployment process and the runtime environment

## Lab Prerequisites

For this lab, you'll need:
- An active Azure subscription
- Azure CLI installed and configured
- Git installed on your local machine
- Access to the course repository with the sample application code

## What to Expect

The entire deployment process will take just a few minutes. You'll see how Azure handles compilation, configuration, and deployment automatically. By the end, you'll have a live web application running on Azure without managing any virtual machines or infrastructure.

Let's get started!
