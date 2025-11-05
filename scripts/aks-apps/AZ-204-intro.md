# AKS Apps with Secure Networking - AZ-204 Exam Introduction

Excellent work implementing secure AKS networking! This lab addresses multiple AZ-204 exam domains, so let's focus on what you need to know for the certification.

## Exam Coverage

This topic spans several exam domains: implementing containerized solutions (AKS), using Azure security services (managed identities and Key Vault), securing Azure services (network rules), and integrating services. It represents a production-ready pattern frequently tested in scenario questions.

## What We'll Cover

**Managed identity authentication** is heavily tested. You need to understand that AKS clusters have a system-assigned managed identity that can authenticate to other Azure services without storing credentials. Know how to grant this identity access to Key Vault using access policies, and understand that this is more secure than service principals with passwords.

**Key Vault integration patterns** appear in multiple exam scenarios. The exam tests three methods to access Key Vault from containers: CSI driver (mount secrets as files), direct SDK access (application code calls Key Vault API), and App Service configuration (automatic injection into environment variables). Know when to use each approach and their tradeoffs.

**Network security with service endpoints** is a critical exam topic. Understand that service endpoints provide a secure, private path between VNets and Azure services without going over the public internet. Know the difference between service endpoints (per-service VNet integration, no extra charge) and private endpoints (dedicated private IP, requires Private Link, additional cost). The exam loves questions about when to use each.

**Azure CNI vs kubenet networking** appears in AKS questions. Azure CNI gives each pod a VNet IP address (required for service endpoints) but consumes more IP addresses. Kubenet uses an overlay network where pods get IPs from a separate CIDR range (more IP-efficient but doesn't support service endpoints). Scenario questions test which to choose based on requirements.

**Key Vault access policies** need to be understood. Know how to grant GET and LIST permissions for secrets, understand the difference between access policies and Azure RBAC (Key Vault supports both), and know that access policies are per-identity while network rules are per-source-network.

We'll also cover **storage account network rules**, the **CSI driver architecture**, **troubleshooting access issues** (managed identity permissions, network rules, RBAC), and **common exam scenarios** about securing multi-service applications.

This is one of the most comprehensive security patterns on the exam - master it!
