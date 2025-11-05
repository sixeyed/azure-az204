# Azure Container Registry - Introduction

## What is Azure Container Registry?

Azure Container Registry, or ACR, is Azure's private container registry service. While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications. ACR provides this capability with full Azure integration.

## Why Use a Private Registry?

Public registries like Docker Hub are excellent for sharing open source software, but for your production applications, you need:

- **Security and access control** - Keep your proprietary images private and control who can access them
- **Regional deployment** - Store images in the same Azure region as your compute services for faster pulls and lower latency
- **Azure integration** - Leverage Azure Active Directory for authentication and role-based access control
- **Compliance** - Meet organizational requirements for where container images are stored

## Key Features of ACR

Azure Container Registry offers several important capabilities:

- **Multiple SKU tiers** - Basic, Standard, and Premium options with different features and performance characteristics
- **Geo-replication** - Replicate your registry across multiple Azure regions (Premium SKU)
- **Private networking** - Use Azure Private Link to secure your registry (Premium SKU)
- **Customer-managed encryption** - Encrypt registry content with your own keys (Premium SKU)
- **Content trust** - Sign and verify images to ensure integrity
- **Webhooks** - Trigger automation when images are pushed or deleted
- **Azure integration** - Works seamlessly with Azure Container Instances, Azure Kubernetes Service, and other Azure services

## Registry Naming and DNS

When you create an ACR instance, you choose a registry name that becomes your DNS hostname:

- Registry name: `mycompanyregistry`
- Full login server: `mycompanyregistry.azurecr.io`

The registry name must be globally unique across all of Azure and follow specific naming rules - only lowercase letters and numbers are allowed.

## Understanding Container Registry Concepts

Before diving into the exercises, it's important to understand a few key concepts:

**Container Registries** are services that host container images. They provide:
- Storage for images
- API for pushing and pulling images
- Authentication and access control
- Image scanning and security features

**Docker Image Names** include several components:
- Registry domain (e.g., `docker.io` or `myregistry.azurecr.io`)
- Repository path (e.g., `labs-acr/nginx`)
- Tag/version (e.g., `alpine-2204` or `latest`)

Full example: `myregistry.azurecr.io/labs-acr/nginx:alpine-2204`

**Authentication** to ACR can be done multiple ways:
- Individual Azure AD identity (for development)
- Service principals (for CI/CD pipelines)
- Admin account (for testing, not recommended for production)
- Managed identities (for Azure services)

## What You'll Learn

In this lab, you'll explore Azure Container Registry hands-on:

1. **Portal exploration** - Understanding SKU options and configuration choices
2. **CLI creation** - Creating a registry using Azure CLI commands
3. **Image management** - Pulling images from Docker Hub and pushing them to ACR
4. **Custom builds** - Building your own container images and storing them in ACR
5. **Portal management** - Using the Azure Portal to browse repositories and manage images

By the end of this lab, you'll understand how to create and manage your own private container registry in Azure, and how to work with container images using both Docker and Azure CLI tools.
