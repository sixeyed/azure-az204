# Azure Container Registry - AZ-204 Exam Introduction

Excellent work with the hands-on exercises! Now let's focus on what the AZ-204 exam expects you to know about Azure Container Registry.

## Exam Weight

ACR falls under the "Implement containerized solutions" domain, which represents 15-20% of the exam. You'll face questions about creating registries, managing images, authentication methods, and integration with Azure services.

## What We'll Cover

First up is **registry naming and access**. You need to know the DNS structure: how a registry name becomes `<registry-name>.azurecr.io`, and how full image names are formatted. The exam tests whether you know the naming rules - globally unique, 5-50 characters, lowercase letters and numbers only, no hyphens. This is a common gotcha since most Azure resources allow hyphens.

**SKU feature comparison** appears frequently. You must know the differences between Basic, Standard, and Premium tiers, particularly when to recommend Premium. The key differentiators are geo-replication and private endpoints - only Premium supports these. Know the storage limits: 10GB for Basic, 100GB for Standard, 500GB for Premium. Scenario questions often ask "which SKU should you use for..." and you need to match requirements to capabilities.

**Authentication methods** is heavily tested. You need to know four approaches: individual Azure AD identity with `az acr login` (for development, 3-hour tokens), service principals with username/password (for CI/CD pipelines), admin accounts (for testing only, not recommended for production), and managed identities (for Azure services, most secure). The exam wants you to recommend managed identities over service principals when possible.

We'll cover **essential CLI commands** that appear on nearly every exam. Creating registries with `az acr create`, logging in with `az acr login`, pushing and pulling images with Docker commands, building images in Azure with ACR Tasks, and managing repositories. Know the syntax cold - the exam tests parameter names and command structure.

**ACR Tasks** is an important feature that lets you build container images in Azure without Docker installed locally. The exam tests quick tasks (`az acr build`), multi-step tasks for complex workflows, and triggered tasks that run automatically on source code commits or base image updates.

**Integration with Azure services** comes up in scenario questions. How do you deploy from ACR to Azure Container Instances? Configure ACR with Azure Kubernetes Service? Set up webhooks to trigger automation? You need to know the authentication flow and configuration requirements for each integration.

We'll cover **image management best practices** including tagging strategies, retention policies, and security scanning. The exam may ask about container image scanning for vulnerabilities or implementing automated cleanup of old images.

Finally, we'll work through common exam scenarios and review the quick-reference commands you need to memorize for test day.

Ready to master ACR for the AZ-204? Let's dive into the exam content!
