# Azure Signin - Exercises Introduction

We've covered Azure authentication and how Microsoft accounts provide access to Azure Subscriptions, with one account potentially having permissions across multiple Subscriptions. Now let's explore the three ways to interact with Azure.

## What You'll Do

You'll start by **exploring the Azure Portal** at portal.azure.com, signing in with your Microsoft account. You'll browse "All services" to see the complete catalog of Azure services, view your Subscriptions to understand the name and unique ID (GUID) for each, and explore what's involved in creating resources like Virtual Machines to see the extensive configuration options required.

Then you'll **use the Azure CLI** with the "az" command for scriptable, repeatable management. You'll run `az login` to authenticate through a browser, `az account list` to see your subscriptions in JSON format, and experiment with different output formats: `-o table` for human-readable columns, `-o yaml` for nested data structures, and `-o tsv` for tab-separated values useful in scripts.

The CLI advantages you'll observe: always up-to-date with latest Azure features, integrated help system with `-h` flags, usable in scripts and CI/CD pipelines for automation, cross-platform compatibility with same commands on Windows/Linux/macOS, and consistent, repeatable operations.

Next comes **the Azure Cloud Shell** accessed at shell.azure.com, providing a browser-based terminal with pre-installed tools. First-time setup creates storage for persisting files and command history. The key benefit: you're already authenticated without running `az login` since you signed in to access Cloud Shell.

You'll **explore pre-installed tools** including .NET SDK, Python, Git, and kubectl - all ready to use without installation. Then you'll **run a practical exercise** creating a .NET console project, uploading your code, and running it entirely in the cloud without local development environment setup.

The key learning: Each access method has its strengths - Portal for visual exploration and learning, CLI for automation and repeatable operations, and Cloud Shell for browser-based access with pre-configured tools. Professional Azure development primarily uses the CLI for its scriptable, automatable approach.

Let's master Azure access methods!
