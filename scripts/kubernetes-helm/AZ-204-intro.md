# Helm Package Manager: AZ-204 Exam Focus

Great work! This Helm lab addresses the "Develop solutions using containers" domain in the AZ-204 exam. While Helm isn't an Azure service, it's critical for deploying and managing containerized applications on Azure Kubernetes Service.

## What We'll Cover

We'll examine application packaging with Helm charts as the standardized way to package Kubernetes applications. Understand chart structure: Chart file with metadata, values file with configuration defaults, and template files for Kubernetes resources. Charts enable reusability - the same chart deploys to development, staging, and production with different configurations.

We'll explore templating and configuration management as one of Helm's most powerful features. The values file defines all configurable parameters like replica counts, resource limits, environment-specific settings, and feature flags. Templates reference these values using Helm syntax that replaces variables at deployment time.

The exam tests your understanding of how templating solves real-world problems. Instead of maintaining separate YAML files for each environment, you maintain one chart with multiple values files or override configurations - demonstrating infrastructure as code principles.

You'll master deployment automation as Helm commands script easily in CI/CD pipelines. Helm install creates new releases, helm upgrade updates existing releases, and helm rollback reverts to previous revisions automatically if health checks fail. Know that Helm maintains release history where every upgrade creates a new revision enabling rollback to any previous state.

We'll cover values precedence that the exam expects you to understand: default values in chart's values file are lowest priority, custom values files override defaults, and set flags override everything. This hierarchy lets you define sensible defaults while allowing specific overrides for each deployment.

You'll understand Azure service integration with Helm charts referencing images from Azure Container Registry requiring AKS cluster permissions, Azure DevOps and GitHub Actions having built-in tasks for Helm commands enabling automation, and Azure Key Vault for sensitive configuration injected as environment variables not hard-coded in Helm values.

The exam includes security considerations - always use Helm 3 or later as Helm 2's Tiller component had security issues. If questions mention Tiller, that's Helm 2 requiring upgrade to Helm 3.

We'll cover best practices aligning with exam objectives: version charts properly using semantic versioning, document values with comments explaining configuration options, use chart repositories for sharing not manual archive passing, integrate with Azure DevOps or GitHub Actions for automation, never store secrets in values files using Key Vault instead, and test charts in non-production before production releases.

Master Helm for application packaging, configuration management, and deployment automation in the AZ-204!
