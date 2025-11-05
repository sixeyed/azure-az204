# Docker - AZ-204 Exam Introduction

Great work with Docker fundamentals! While the exam won't test Docker CLI commands directly, understanding containers is essential for AZ-204's "Implement containerized solutions" domain.

## What We'll Cover

**Container fundamentals** translate directly to Azure services. The concepts you learned with Docker Desktop (images, containers, environment variables, port mappings) work identically in Azure Container Instances, App Service containers, and Azure Kubernetes Service. The exam tests your understanding of how these concepts apply in Azure.

**Images vs containers** is fundamental. Images are immutable blueprints (like classes in OOP), containers are running instances (like objects). You can't change an image - you build a new version. Containers are disposable - delete and recreate them rather than trying to fix them. The exam tests understanding of this immutability pattern and why it matters for reliable deployments.

**Environment variables for configuration** in Docker become App Settings in Azure. The same pattern of separating configuration from images enables deploying one image across dev/test/prod environments with different settings. The exam heavily tests configuration management patterns using environment variables.

**Port mappings** in Docker (8080:80) translate to exposed ports in Azure Container Instances. Understanding how containers expose services on specific ports and how to map them to external ports is critical for networking questions.

**Multi-stage builds** keep images small and secure by separating build-time dependencies from runtime dependencies. This pattern appears in Azure Container Registry scenarios where smaller images mean faster deployments and lower costs.

We'll cover **integration with Azure Container Registry** (pushing images to ACR), **Azure Container Instances** (running Docker containers in Azure), **App Service containers** (custom container deployment), **Azure Kubernetes Service** (orchestrating containers at scale), **Azure Monitor integration** for container logs, **Key Vault integration** for secrets, and **Virtual Network integration** for secure networking.

The exam expects you to know when to use containers versus other compute options, how to configure containerized applications in Azure, and how to troubleshoot common container issues.

Master container fundamentals for AZ-204!
