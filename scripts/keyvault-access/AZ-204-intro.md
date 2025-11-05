# Key Vault Access Security - AZ-204 Exam Introduction

Excellent work with Key Vault security! This topic combines multiple AZ-204 domains: security, networking, and identity management.

## What We'll Cover

**Key Vault access policies with principle of least privilege** grant minimum necessary permissions. Permissions are granular per operation: Get, List, Set, Delete, Backup, Restore for secrets. Only grant what's needed - applications usually need only Get and List. The exam tests designing appropriate access policies for different scenarios.

**Network security with virtual network service endpoints** restricts which networks can reach Key Vault. Service endpoints extend your VNet address space to Azure services, creating a secure path on the Azure backbone (not public internet). Traffic never leaves Microsoft's network. The exam tests understanding of service endpoint benefits and configuration.

**Managed identities for passwordless authentication** eliminate credential management. System-assigned (lifecycle tied to resource, automatically cleaned up, simpler) versus user-assigned (shared across resources, more complex but reusable). The exam heavily tests when to use each type and their lifecycle implications.

**Authentication flow using Azure Instance Metadata Service** (IMDS) provides managed identity tokens. Applications make HTTP requests to IMDS (169.254.169.254), receive Azure AD tokens, use tokens to authenticate to Key Vault. This happens automatically with Azure SDK. The exam tests understanding of how passwordless authentication works under the hood.

**Service endpoints vs private endpoints** is a common comparison question. Service endpoints: free, traffic on Azure backbone (not truly private), simple configuration. Private endpoints: dedicated private IP in your VNet, true network isolation, higher cost, more complex (requires DNS). The exam tests when to choose each based on security and cost requirements.

**Access policies (traditional) vs RBAC (modern)** for authorization must be understood. Access policies: per-vault configuration, granular per-operation control, traditional model. RBAC: uses standard Azure roles, consistent across all Azure services, easier to manage at scale, modern recommended approach. The exam tests choosing between them.

We'll cover **Azure AD authentication integration**, **virtual network fundamentals**, **troubleshooting access denied errors**, **monitoring audit logs**, **common scenarios** about securing production applications, and **implementing zero-trust security patterns**.

Master Key Vault security for the AZ-204!
