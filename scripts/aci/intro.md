# Azure Container Instances - Introduction

## Welcome

Welcome to the Azure Container Instances lab. In this session, we'll explore one of Azure's simplest and most efficient ways to run containerized applications in the cloud.

## What is Azure Container Instances?

Azure Container Instances, or ACI, is a managed container service that lets you run Docker containers in Azure without managing any virtual machines or orchestration infrastructure. It's the fastest and simplest way to run a container in Azure.

Think of it this way: you've built a Docker container that runs perfectly on your local machine. With ACI, you can take that exact same container and run it in Azure with just a single command. No servers to provision, no clusters to configure - just your application running in the cloud.

## Key Benefits

**Portability**: Your Docker containers run the same way everywhere. If it works in Docker Desktop, it works in ACI. This is the fundamental promise of containerization.

**Simplicity**: Unlike Azure Kubernetes Service or Azure App Service, ACI has minimal configuration. You specify an image, some compute resources, and you're running.

**Speed**: ACI containers start in seconds. This makes it perfect for burst workloads, task automation, or development and testing scenarios.

**Cost-effectiveness**: You pay per second for exactly what you use. No idle virtual machines consuming your budget.

## When to Use ACI

ACI is ideal for several scenarios:

- **Simple web applications**: Single container apps that don't need complex orchestration
- **Batch processing**: Run tasks on-demand and tear them down when complete
- **Build agents**: Temporary CI/CD build environments
- **Development and testing**: Quick environment spin-up without infrastructure overhead
- **Event-driven applications**: Combined with Azure Functions or Logic Apps for responsive workloads

## What We'll Cover

In this lab, you'll learn how to:

1. **Explore ACI capabilities** through the Azure Portal
2. **Deploy containers** using the Azure CLI with `az container` commands
3. **Manage running containers** by viewing logs and monitoring status
4. **Use Docker CLI integration** to deploy to ACI using familiar Docker commands
5. **Work with different container types** including Linux and Windows containers

## Architecture Overview

When you deploy a container to ACI, Azure handles:
- The underlying compute infrastructure
- Network configuration and DNS
- Storage for container logs
- Security and isolation between container instances

You control:
- The container image to run
- CPU and memory allocation
- Network ports to expose
- Environment variables and configuration
- Restart policies and lifecycle

## Key Concepts

**Container Registry**: Where your container images are stored. This could be Docker Hub (public), Azure Container Registry (private), or other registries.

**DNS Name Label**: ACI provides automatic DNS naming. You can assign a friendly DNS prefix and ACI creates a full domain name for accessing your container.

**Resource Allocation**: You specify exactly how much CPU and memory your container needs, with granular control from fractional CPUs to multiple cores.

**Networking**: Containers can expose ports to the internet or remain private. ACI handles all the underlying networking complexity.

## Prerequisites

Before starting the exercises, ensure you have:
- Azure CLI installed and configured
- Docker Desktop installed (for Docker integration exercises)
- An active Azure subscription
- Basic familiarity with Docker and containers

Let's get started and see how easy it is to run containers in Azure!
