# AKS with Key Vault Integration - Quickfire Questions

## Question 1
Why integrate AKS with Azure Key Vault?


- A) Not necessary
- B) No benefits
- C) Secure secret management avoiding hardcoded secrets in manifests
- D) Only for compliance

**Answer: C**
Key Vault centralizes secret management with audit trails and access control.
---
## Question 2
What is the Secrets Store CSI Driver?


- A) Database driver
- B) Network driver
- C) Kubernetes driver mounting secrets from external stores (like Key Vault) as volumes
- D) Storage driver

**Answer: C**
CSI driver enables pods to access Key Vault secrets as mounted files or environment variables.
---
## Question 3
How does CSI driver authenticate to Key Vault?


- A) Pod-managed identity or Azure AD workload identity
- B) Passwords
- C) API keys
- D) No authentication

**Answer: A**
Uses Azure AD workload identity (preferred) or pod-managed identity for passwordless access.
---
## Question 4
What is Azure AD Workload Identity?


- A) User identity
- B) Network identity
- C) Kubernetes service account mapping to Azure AD identity for resource access
- D) VM identity

**Answer: C**
Workload identity federates Kubernetes service accounts with Azure AD for secure, keyless authentication.
---
## Question 5
Can secrets be automatically rotated?


- A) Manual only
- B) CSI driver can poll Key Vault for updates and refresh mounted secrets
- C) Not supported
- D) Requires pod restart always

**Answer: B**
Enable auto-rotation in CSI driver; secrets refresh periodically without pod restart.
---
## Question 6
How are Key Vault secrets exposed to pods?


- A) Not possible
- B) Mounted as files in volume or injected as environment variables
- C) Direct API calls only
- D) Manual copying

**Answer: B**
SecretProviderClass defines how secrets appear: as files in volume path or env vars.
---
## Question 7
What is a SecretProviderClass?


- A) Storage class
- B) Security classification
- C) CRD defining which Key Vault secrets to mount and how
- D) Network class

**Answer: C**
Custom resource defining Key Vault connection, secret names, and mounting configuration.
---
## Question 8
Can you sync Key Vault secrets to Kubernetes Secrets?


- A) Manual sync only
- B) Not recommended
- C) Yes, CSI driver can create Kubernetes Secret objects from Key Vault
- D) No

**Answer: C**
Enable `secretObjects` in SecretProviderClass to create Kubernetes Secrets from Key Vault.
---
## Question 9
What Key Vault object types does CSI driver support?


- A) Secrets and keys only
- B) Certificates only
- C) Secrets only
- D) Secrets, keys, certificates

**Answer: D**
Access all Key Vault object types: secrets, encryption keys, and certificates.
---
## Question 10
Do you need to modify application code?


- A) Complete rewrite
- B) No, applications read mounted files or env vars as usual
- C) Only for .NET apps
- D) Major changes required

**Answer: B**
Secrets appear as files/environment variables; applications access them normally.