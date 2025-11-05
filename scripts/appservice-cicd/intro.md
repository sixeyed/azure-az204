# App Service CI/CD - Introduction Script

## Opening

Welcome to this lab on Azure App Service Continuous Integration and Continuous Deployment. In this session, we'll explore how to automate deployments to Azure App Service using GitHub integration and deployment slots.

## What is App Service CI/CD?

Azure App Service provides two powerful features for continuous deployment:

First, **deployments** - these can be automatically triggered every time source code is changed and pushed to a Git repository. This eliminates manual deployment steps and ensures your application is always up to date with your latest code.

Second, **deployment slots** - these allow you to deploy your application to a staging environment where you can test it thoroughly before promoting it to production. This reduces risk and ensures quality in your production environment.

## Lab Overview

In this lab, we'll be working with a random number API. We'll:

1. Deploy the application from your own GitHub repository
2. Set up manual deployment first to understand the process
3. Configure continuous deployment so changes are automatically deployed
4. Create a staging slot for testing changes
5. Learn how to swap slots to promote tested code to production

## Prerequisites

Before we begin, you'll need:

- An active Azure subscription
- A GitHub account with a fork of the lab repository
- Azure CLI installed and configured
- Basic understanding of Git and GitHub workflows

The application we're deploying is a .NET Core API that generates random numbers. It's simple, but perfect for demonstrating CI/CD concepts.

## Why This Matters

Continuous Integration and Deployment are essential practices in modern software development. They:

- Reduce manual errors in the deployment process
- Enable faster iteration and feedback cycles
- Provide a consistent, repeatable deployment process
- Allow for safe testing of new releases before they reach production

For the AZ-204 exam, understanding App Service deployment options, deployment slots, and how to configure CI/CD pipelines is crucial knowledge.

## Let's Get Started

We'll begin by setting up our Azure resources and configuring the initial deployment from GitHub. Then we'll progressively enhance our deployment pipeline with automation and staging environments.

Are you ready? Let's dive in.
