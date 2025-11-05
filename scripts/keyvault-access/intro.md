# Securing Key Vault Access - Introduction

Welcome to this lab on securing Azure Key Vault access. In this session, we'll explore how to properly lock down access to your Key Vaults to ensure only authorized resources can access your sensitive data.

## Why Key Vault Security Matters

Key Vaults store your most sensitive data - passwords, connection strings, API keys, and certificates. Because of this, securing access to Key Vault is absolutely critical. A misconfigured Key Vault could expose your secrets to unauthorized users or services, potentially compromising your entire application infrastructure.

## Two Layers of Security

Azure Key Vault provides two distinct layers of security that work together:

First, there's network-level security. This controls whether a request can even reach the Key Vault service. By default, Key Vaults are accessible from any network, but you can restrict access to specific virtual networks.

Second, there's identity-based security. Even if a request can reach the Key Vault over the network, the caller still needs to authenticate as an authorized principal. Azure uses the term "principal" to refer to any identity - whether that's a user account, a group of users, a service principal, or a managed identity.

## What We'll Cover

In this lab, we'll work through both layers of security. We'll start by creating a Key Vault and storing a secret. Then we'll lock down network access so only resources in a specific virtual network can reach the vault.

Next, we'll create a virtual machine in that network and configure it with a managed identity. This will demonstrate how managed identities provide a secure way for Azure resources to authenticate with Key Vault without requiring any credentials in your code.

By the end of this lab, you'll understand how to implement defense in depth for your Key Vaults, using both network restrictions and identity-based access control.

## Key Concepts

Let's quickly review some key concepts you'll encounter:

**Access Policies** define what a principal is allowed to do with secrets, keys, or certificates. You configure these in the Key Vault itself.

**Service Endpoints** allow Azure services like Key Vault to communicate with resources inside a virtual network subnet.

**Managed Identities** are Azure-managed identities that Azure services can use to authenticate with other Azure services. There's no password or credential you need to manage - Azure handles everything automatically.

**Principals** is Azure's general term for any authenticated identity - users, groups, service principals, or managed identities.

Let's get started by creating our Key Vault and setting up the initial configuration.
