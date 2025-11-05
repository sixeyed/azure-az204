# Kubernetes Secrets: AZ-204 Exam Focus

Great work! This Secrets lab is essential for the "Implement Azure Security" objective in the AZ-204 exam. Understanding secure credential management is critical for Azure Kubernetes Service.

## What We'll Cover

We'll examine Secrets versus ConfigMaps where Secrets store sensitive data with base64 encoding and additional access controls while ConfigMaps store non-sensitive configuration in plain text. Know that Secrets are not encrypted by default in etcd requiring encryption at rest configuration.

We'll explore consumption methods tested on the exam: environment variables for simple use cases with limitations of visibility to all processes and no automatic updates, volume mounts for file-based secrets with automatic updates and better security, and projected volumes for combining multiple secrets and configmaps.

You'll master Azure Key Vault integration as the recommended approach for production. Secrets Store CSI Driver syncs secrets from Key Vault into pods, managed identity authenticates to Key Vault, secrets appear as mounted volumes in containers, and audit logs track secret access.

The exam tests secret types including Opaque for arbitrary data, kubernetes.io/dockerconfigjson for image pull secrets, kubernetes.io/tls for TLS certificates, and kubernetes.io/service-account-token for service accounts. Know when to use each type.

We'll cover security best practices the exam emphasizes: never commit secrets to source control, use Azure Key Vault for enterprise scenarios, implement RBAC limiting secret access, enable encryption at rest for etcd, rotate secrets regularly with documented procedures, and use managed identities avoiding credentials in code.

You'll understand secret rotation strategies where manual rotation requires updating secrets and restarting pods, Azure Key Vault rotation happens centrally with CSI driver syncing updates, and applications should monitor secret files for changes implementing hot-reload.

The exam includes troubleshooting scenarios: pods stuck in ContainerCreating often indicates missing secrets, image pull failures suggest incorrect registry secrets, and certificate errors point to expired or misconfigured TLS secrets.

Master Secrets management, Azure Key Vault integration, and security best practices for the AZ-204!
