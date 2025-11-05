# Azure Key Vault - Quickfire Questions

## Question 1
What is Azure Key Vault?


- A) A physical vault
- B) A database
- C) A file storage service
- D) A cloud service for securely storing and accessing secrets, keys, and certificates

**Answer: D**
Key Vault provides secure storage for secrets (passwords, connection strings), cryptographic keys, and SSL/TLS certificates.
---
## Question 2
What are the main object types in Key Vault?


- A) Secrets, Keys, Certificates
- B) Only passwords
- C) Only files
- D) Only tokens

**Answer: A**
Secrets (strings/small data), Keys (cryptographic keys for encrypt/decrypt), Certificates (X.509 certificates).
---
## Question 3
What is a secret in Key Vault?


- A) Encryption algorithm
- B) Any sensitive string data (password, connection string, API key)
- C) Public information
- D) Only passwords

**Answer: B**
Secrets store any sensitive string or binary data up to 25KB, like database passwords or API keys.
---
## Question 4
What are the Key Vault pricing tiers?


- A) One tier
- B) Free only
- C) Standard and Premium
- D) Basic and Enterprise

**Answer: C**
Standard (software-protected keys) and Premium (adds HSM-protected keys for compliance).
---
## Question 5
What is HSM in Key Vault Premium?


- A) Host Security Manager
- B) HTTP Security Method
- C) High-Speed Memory
- D) Hardware Security Module providing FIPS 140-2 Level 2 validated hardware key protection

**Answer: D**
HSM provides hardware-backed key protection meeting compliance requirements for sensitive workloads.
---
## Question 6
How can applications authenticate to Key Vault?


- A) Managed Identity, Service Principal, Certificate
- B) Only API keys
- C) Only passwords
- D) Anonymous access

**Answer: A**
Managed Identity (recommended), Service Principal with secret/certificate, or User credentials via Azure AD.
---
## Question 7
What is soft-delete in Key Vault?


- A) Permanent deletion
- B) Compression
- C) Retention of deleted objects for recovery period (90 days default)
- D) Temporary disable

**Answer: C**
Soft-delete retains deleted vaults, secrets, keys, and certificates for recovery, preventing accidental permanent loss.
---
## Question 8
What is purge protection?


- A) Virus protection
- B) Network security
- C) Prevents permanent deletion of soft-deleted items until retention period expires
- D) Data compression

**Answer: C**
Purge protection enforces retention period, preventing immediate permanent deletion even by privileged users.
---
## Question 9
What are Key Vault access policies?


- A) Pricing policies
- B) Network policies
- C) Permissions defining what identities can do with secrets, keys, and certificates
- D) Backup policies

**Answer: C**
Access policies grant granular permissions (get, list, set, delete) for secrets, keys, and certificates to Azure AD identities.
---
## Question 10
Can Key Vault references be used in App Service?


- A) Yes, app settings can reference Key Vault secrets using special syntax
- B) Requires custom code
- C) Only manually
- D) No integration

**Answer: A**
App Service supports `@Microsoft.KeyVault(SecretUri=...)` syntax to load secrets from Key Vault at runtime.