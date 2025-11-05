# Kubernetes Secrets: Exercises Introduction

We've covered how Secrets store sensitive data like passwords, tokens, and keys separately from pod specifications. Now let's create and use Secrets securely.

## What You'll Do

You'll create Secrets using kubectl create secret for imperative creation from literals or files, and YAML manifests for declarative management with base64-encoded values. You'll understand that base64 is encoding not encryption.

Then you'll consume Secrets as environment variables injecting secret data into containers. You'll use env and envFrom fields referencing secret keys, understanding that environment variables are visible to all container processes.

You'll mount Secrets as volumes creating files in container filesystem where each secret key becomes a file. This is more secure than environment variables and supports automatic updates when secrets change.

Next, you'll work with built-in secrets including default service account tokens automatically mounted in pods, TLS secrets for Ingress, and docker-registry secrets for pulling private images from Azure Container Registry.

You'll explore Azure Key Vault integration using Secrets Store CSI Driver to sync secrets from Azure Key Vault into Kubernetes secrets. This provides centralized secret management with Key Vault's enhanced security and audit capabilities.

You'll understand secret rotation and updates where mounted secrets update automatically when changed but environment variables require pod restart. Applications should implement hot-reload for mounted secret files.

The lab challenge asks you to configure an application using Azure Key Vault provider for Secrets Store CSI Driver, avoiding storing sensitive data directly in Kubernetes secrets and leveraging Azure's managed secret service.

The key learning: Never store sensitive data in ConfigMaps or source control. Use Secrets for basic scenarios and Azure Key Vault integration for enterprise security requirements with audit logging and access policies.
