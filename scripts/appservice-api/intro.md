# App Service for Distributed Apps - Introduction

## Welcome

Welcome to this lab on using Azure App Service for distributed applications. In this session, we'll explore how to deploy and configure multiple applications within a single App Service Plan, demonstrating a cost-effective approach to running distributed systems in Azure.

## Lab Overview

In this lab, you'll learn how to:
- Deploy multiple applications to a single App Service Plan to share compute resources
- Configure application settings to enable communication between components
- Use Azure App Service configuration to manage environment-specific values
- Scale App Service Plans and understand SKU limitations
- Work with CORS policies for cross-origin API requests

## Scenario

We'll be working with a distributed random number generator application that consists of:
- A REST API backend built with .NET 6.0
- A web front-end application that consumes the API
- A static single-page application as an alternative front-end

This architecture is typical of modern microservices applications where you have separate components that need to communicate with each other across different environments.

## Key Concepts

### App Service Plans
An App Service Plan defines the compute resources for your web apps. One plan can host multiple App Services, allowing you to optimize costs by sharing infrastructure across multiple application components.

### Configuration Management
App Service provides a centralized way to manage application configuration through environment variables and application settings. These settings are injected into your application at runtime, making it easy to deploy the same code across different environments with different configurations.

### Deployment Methods
We'll use the `az webapp up` command, which is a convenient shortcut that combines:
- Creating an App Service
- Packaging your application code
- Deploying the code to Azure
- All in a single command

## Prerequisites

Before starting this lab, ensure you have:
- Azure CLI installed and configured
- An active Azure subscription
- Basic understanding of REST APIs
- Familiarity with command-line tools

## What You'll Build

By the end of this lab, you'll have:
- A fully functional REST API deployed to Azure App Service
- A web application that consumes the API
- Proper configuration connecting the components
- An understanding of how to scale and manage App Service Plans
- Experience with CORS configuration for secure API access

Let's get started!
