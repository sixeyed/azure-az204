# AKS with Key Vault Integration - AZ-204 Exam Introduction

Excellent work integrating Key Vault with AKS! This topic covers multiple AZ-204 exam domains and represents a critical security pattern. Let's focus on what you need to know for the certification.

## Exam Coverage

This spans containerized solutions (AKS), Azure security (managed identities and Key Vault), and configuration management. Expect questions about secret management patterns, troubleshooting access issues, and choosing the right integration method.

## What We'll Cover

**Three methods to access Key Vault from containers** is a key exam concept. First, the CSI driver mounts secrets as files (what you just learned - good for any application, no code changes, automatic rotation). Second, direct SDK access where application code calls the Key Vault API (maximum flexibility, requires code changes, custom caching and rotation logic). Third, App Service configuration where Key Vault references are automatically injected as environment variables (easiest for App Service, but this is an AKS lab so not applicable here). Know when to use each approach.

**System-assigned vs user-assigned managed identities** appears on every exam. System-assigned identities are created with the resource and deleted with it - lifecycle is tied together, simple but inflexible. User-assigned identities are standalone resources you can assign to multiple services - more complex to manage but reusable across resources. The exam tests when to recommend each and how to configure them.

**Key Vault access policies** need to be understood thoroughly. Access policies define which identities can perform which operations (GET, LIST, SET, DELETE for secrets, keys, and certificates). They're identity-centric - you grant permissions to specific Azure AD principals. Know the difference between access policies (classic, granular per-operation) and Azure RBAC (newer, uses standard roles, easier to manage at scale). Key Vault supports both models.

**CSI driver architecture** may appear in troubleshooting questions. The driver runs as a DaemonSet (one pod per node), uses the AKS managed identity to authenticate, fetches secrets on pod startup, and refreshes them periodically (default every 2 minutes). If secrets aren't appearing, check the CSI driver pod logs, verify access policies, and ensure the SecretProviderClass is correctly configured.

**Secret rotation strategies** are tested. The CSI driver automatically refreshes mounted secrets every 2 minutes, but applications must detect file changes and reload configuration. Some apps support hot reload, others require restart. The exam tests your understanding of this behavior and how to design applications that handle secret rotation gracefully.

We'll cover **SecretProviderClass configuration**, **troubleshooting common issues**, **comparing Key Vault access methods**, and **exam scenarios** about multi-environment secret management and audit logging.

Master Key Vault integration for secure AKS applications!
