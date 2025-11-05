# Docker Compose - AZ-204 Exam Introduction

Great work with multi-container orchestration! While Compose itself isn't heavily tested, the patterns directly apply to Azure services on the AZ-204.

## What We'll Cover

**Container networking and DNS resolution** is heavily tested. Containers in the same network can communicate using service names as hostnames (automatic DNS). Containers in different networks cannot communicate unless explicitly connected. The exam tests understanding of when containers can reach each other and how to troubleshoot connectivity issues.

**Environment variables for configuration** separate code from configuration, enabling the same image to run in multiple environments with different settings. This pattern appears constantly in Azure - App Service app settings, ACI environment variables, AKS ConfigMaps all use this approach. The exam tests configuration management patterns.

**Desired-state deployment** where you declare what you want and the platform figures out how to achieve it. Compose compares current state to desired state and makes minimal changes. This concept translates to Azure Resource Manager templates, Bicep, and Kubernetes manifests. The exam tests understanding of declarative vs imperative approaches.

**Debugging container connectivity** requires knowing how to check logs, test DNS resolution, verify network configuration, and understand why containers can't reach each other. The exam may present troubleshooting scenarios requiring this knowledge.

**Azure Container Instances multi-container groups** use the same patterns as Compose. Containers in a group share network namespace (can communicate via localhost), share storage volumes, and start/stop together. The exam tests understanding of container groups and when to use them.

**Azure Container Apps** (newer service) natively supports Docker Compose files for deployment. Understanding Compose syntax helps with Container Apps questions.

**Azure Kubernetes Service** uses similar concepts - pods (like Compose services), services (like networks), ConfigMaps and Secrets (like environment variables). Compose knowledge transfers directly to Kubernetes questions.

We'll cover **integration with Azure Container Registry** (private images in Compose), **Key Vault references** for secrets, **Application Insights integration** for monitoring, **networking patterns**, and **common scenarios** about multi-container architectures, service discovery, and troubleshooting distributed applications.

Master multi-container patterns for the AZ-204!
