# Securing AKS Apps with Key Vault and Virtual Networks - Introduction

## Opening

Welcome to this lab on securing Azure Kubernetes Service applications with Key Vault and Virtual Networks. In this session, we'll explore how to implement defense-in-depth security patterns by leveraging Azure's networking capabilities to restrict access to sensitive resources.

## Concept Overview

When running applications in AKS, security should be a primary concern. While AKS provides a managed Kubernetes environment, it's our responsibility to secure the resources our applications use - things like storage accounts and key vaults that contain sensitive data and credentials.

Let me explain the key concepts we'll be working with today.

## Azure Network Provider for AKS

By default, AKS can use kubenet networking, where Pods get IP addresses from a separate address space. However, Azure also supports the Azure CNI - Container Network Interface - which allows AKS clusters to run inside Azure Virtual Networks.

When you use Azure CNI, each Pod in your cluster gets an IP address directly from the VNet subnet. This is powerful because now your Pods are first-class citizens in your Azure network infrastructure. They can communicate directly with other Azure resources, and more importantly, those resources can identify and restrict access based on the subnet the Pods are running in.

## Service Endpoints and Network Security

Many Azure services support virtual network service endpoints. This includes Key Vault and Storage Accounts. Service endpoints allow you to secure these services to only accept traffic from specific subnets in your virtual network.

Think of it this way: instead of having your Key Vault or Storage Account accessible from the entire Internet - even if protected by authentication - you can lock it down so it only accepts connections from your AKS subnet. This dramatically reduces your attack surface.

## Managed Identities for Authentication

Authentication is handled through Azure Managed Identities. We've seen this pattern before in other labs, but it's especially powerful in AKS. The AKS KeyVault add-on creates a managed identity that can authenticate to Key Vault on behalf of your Pods.

This means your application code never needs to handle credentials for accessing Key Vault. The identity is managed by Azure, rotated automatically, and can be granted specific permissions through Azure RBAC or Key Vault access policies.

## The Lab Scenario

In today's lab, we'll deploy a sample application called Asset Manager to AKS. This application uses Azure Blob Storage to persist data. The connection string for the storage account contains sensitive credentials, so we'll store it in Azure Key Vault.

Here's what makes this scenario interesting from a security perspective:

First, the AKS cluster will run inside a dedicated VNet using Azure CNI networking. All Pods will have IP addresses from our subnet.

Second, we'll configure the Key Vault to only accept connections from the AKS subnet. Even though the vault is technically accessible via the Internet, the firewall rules will deny all traffic except what comes from our Pods.

Third, we'll extend this same pattern to the Storage Account itself - locking it down so only the AKS Pods can access the stored data.

Finally, we'll use the AKS KeyVault Secrets Provider add-on to mount the connection string secret directly into the Pod filesystem, making it seamlessly available to the application.

## Security Benefits

This architecture provides multiple layers of security:

Network isolation: Resources are only accessible from specific subnets
Identity-based access: No credentials stored in code or environment variables
Principle of least privilege: Each component has only the permissions it needs
Defense in depth: Multiple security controls protecting the same resources

## What You'll Learn

By the end of this lab, you'll understand how to:

- Deploy an AKS cluster into a virtual network using Azure CNI
- Configure service endpoints on a subnet for Key Vault and Storage
- Restrict Key Vault access using network rules
- Grant AKS managed identity access to Key Vault secrets
- Deploy applications that consume Key Vault secrets as mounted volumes
- Secure Storage Accounts with virtual network firewall rules

This is a critical pattern for production AKS deployments where security and compliance are requirements.

Let's get started by setting up our infrastructure.
