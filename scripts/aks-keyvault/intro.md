# AKS with KeyVault Secret Storage - Introduction

## Opening

Welcome to this lab on integrating Azure Kubernetes Service with Azure Key Vault for secure secret storage. In this session, we'll explore how to leverage the Container Storage Interface to mount Key Vault secrets directly into your Kubernetes pods.

## What is the Container Storage Interface?

Kubernetes has a powerful, pluggable storage architecture called the Container Storage Interface, or CSI. This architecture allows different types of storage systems to be connected to a Kubernetes cluster and made available as volumes inside your Pod containers.

The beauty of CSI is its flexibility. It's not limited to traditional block storage or file systems. You can connect specialized storage providers that serve specific purposes.

## KeyVault as a Storage Provider

Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver. This is a game-changer for security and configuration management.

With this integration, you can:
- Store sensitive configuration files in Azure Key Vault
- Mount them as volumes directly in your container folders
- Keep the data secure without storing it anywhere else in Kubernetes

## Why This Matters

Traditional approaches to secrets management in Kubernetes involve storing secrets as Kubernetes Secret objects. While these are base64 encoded, they're still stored in the cluster's etcd database.

With the Key Vault CSI Driver, your secrets remain in Azure Key Vault, benefiting from all of Key Vault's security features including:
- Hardware security module protection
- Audit logging
- Azure RBAC integration
- Centralized secret management across multiple clusters

The secrets are only materialized in memory when they're mounted into your pod's filesystem, and they never exist as Kubernetes objects in your cluster.

## What We'll Cover

In this lab, you'll learn how to:
1. Create an AKS cluster with the Key Vault secrets provider add-on enabled
2. Configure the necessary managed identity permissions
3. Create and configure a Key Vault
4. Define a SecretProviderClass to map Key Vault secrets to volume mounts
5. Deploy an application that consumes Key Vault secrets as files

## Use Cases

This approach is particularly valuable when you need to:
- Share secrets across multiple clusters or applications
- Comply with security requirements that mandate centralized secret storage
- Rotate secrets without redeploying your applications
- Audit all access to sensitive configuration data

Let's get started with the hands-on exercises.
