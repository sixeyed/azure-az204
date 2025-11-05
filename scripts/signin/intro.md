# Azure Signin - Introduction

Welcome to this module on Azure authentication and sign-in. In this lesson, we'll explore how to access Azure using different methods and understand the fundamental concepts of Azure accounts and subscriptions.

## What You'll Learn

Azure uses Microsoft accounts for authentication and authorization. Whether you're working in a corporate environment with managed accounts or using a personal account for learning, understanding how to sign in and manage your Azure access is the foundation of working with Azure services.

In this module, we'll cover:
- The relationship between Microsoft accounts and Azure Subscriptions
- How one account can have permissions across multiple Subscriptions
- Three different ways to interact with Azure: the Portal, the CLI, and the Cloud Shell

## Azure Accounts and Subscriptions

Think of your Microsoft account as your identity in Azure. This single account can have access to one or more Azure Subscriptions. Each Subscription is a logical container for your Azure resources and has its own billing and access management.

In a corporate environment, your account would be managed by your organization's Azure Active Directory. For learning and personal projects, you can create your own Microsoft account and Azure Subscription.

## Three Ways to Access Azure

There are three primary ways to interact with Azure:

**The Azure Portal** - A web-based graphical interface where you can browse services, create resources, and manage your Azure environment. It's great for exploration and visual management, but it's not easily automated.

**The Azure CLI** - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources. This is the recommended approach for developers and anyone who needs to automate Azure operations.

**The Azure Cloud Shell** - A browser-based shell environment that comes with Azure tools pre-installed and configured. Perfect for when you can't install the CLI locally but need command-line access to Azure.

## Why Learn Multiple Access Methods?

Each method has its strengths:
- The Portal is ideal for discovery and visual exploration
- The CLI is best for automation and repeatable deployments
- The Cloud Shell provides quick access without local installation requirements

As an Azure developer, you'll likely use all three methods depending on the task at hand. Understanding when to use each approach is an important skill.

Let's begin by exploring the Azure Portal.
