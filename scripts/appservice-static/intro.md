# App Service for Static Web Apps - Introduction

Welcome to this lab on Azure Static Web Apps and App Service for static content.

In this lab, we'll explore two different approaches for hosting static web content in Azure. While Azure App Service excels at compiling, packaging, and deploying complex web applications, there's a simpler, more streamlined option available for static HTML sites and Single Page Applications that don't require backend processing.

## What are Static Web Apps?

Azure Static Web Apps is a service designed specifically for modern web applications that consist of static content - HTML, CSS, JavaScript - and optionally serverless API backends. Unlike traditional App Service deployments, Static Web Apps are deployed directly from a Git repository, with automated build and deployment workflows managed through GitHub Actions or Azure DevOps.

## What You'll Learn

In this lab, you'll gain hands-on experience with:

1. **Creating a Static Web App from GitHub** - You'll fork a repository, configure Azure to deploy from it, and see how Azure automatically creates deployment workflows.

2. **Continuous Deployment** - You'll make changes to your content and see how GitHub Actions automatically deploy those changes to your live site.

3. **Traditional App Service for Static Content** - You'll compare the Static Web Apps approach with deploying static content to a standard App Service, understanding when each approach is appropriate.

4. **Mixed Content Scenarios** - You'll deploy a Node.js application that serves both static content and dynamic endpoints, exploring how to handle authentication and identity providers.

## Prerequisites

To complete this lab, you'll need:
- An active Azure subscription
- Azure CLI installed and configured
- A GitHub account (free accounts are sufficient)
- Git installed on your local machine

## Key Differences

Before we begin, let's understand the key differences:

**Static Web Apps:**
- Deploy directly from Git repositories
- Automatic build and deployment via GitHub Actions
- Optimized for static content and JAMstack applications
- No App Service Plan required - simpler resource model
- Built-in staging environments from pull requests

**App Service with Static Content:**
- More control over deployment methods
- Full range of App Service management options
- Can mix static and dynamic content more flexibly
- Requires an App Service Plan
- Familiar model if you're already using App Service

Let's get started and see these differences in action.
