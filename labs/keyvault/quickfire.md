# Azure Key Vault - Quickfire Questions

## Question 1
What is Azure Key Vault?

- A) A physical vault
- B) A cloud service for securely storing and accessing secrets, keys, and certificates
- C) A database
- D) A file storage service

**Answer: B**
Key Vault provides secure storage for secrets (passwords, connection strings), cryptographic keys, and SSL/TLS certificates.

---

## Question 2
What are the main object types in Key Vault?

- A) Only passwords
- B) Secrets, Keys, Certificates
- C) Only files
- D) Only tokens

**Answer: B**
Secrets (strings/small data), Keys (cryptographic keys for encrypt/decrypt), Certificates (X.509 certificates).

---

## Question 3
What is a secret in Key Vault?

- A) Public information
- B) Any sensitive string data (password, connection string, API key)
- C) Only passwords
- D) Encryption algorithm

**Answer: B**
Secrets store any sensitive string or binary data up to 25KB, like database passwords or API keys.

---

## Question 4
What are the Key Vault pricing tiers?

- A) Free only
- B) Standard and Premium
- C) Basic and Enterprise
- D) One tier

**Answer: B**
Standard (software-protected keys) and Premium (adds HSM-protected keys for compliance).

---

## Question 5
What is HSM in Key Vault Premium?

- A) High-Speed Memory
- B) Hardware Security Module providing FIPS 140-2 Level 2 validated hardware key protection
- C) Host Security Manager
- D) HTTP Security Method

**Answer: B**
HSM provides hardware-backed key protection meeting compliance requirements for sensitive workloads.

---

## Question 6
How can applications authenticate to Key Vault?

- A) Only passwords
- B) Managed Identity, Service Principal, Certificate
- C) Only API keys
- D) Anonymous access

**Answer: B**
Managed Identity (recommended), Service Principal with secret/certificate, or User credentials via Azure AD.

---

## Question 7
What is soft-delete in Key Vault?

- A) Permanent deletion
- B) Retention of deleted objects for recovery period (90 days default)
- C) Temporary disable
- D) Compression

**Answer: B**
Soft-delete retains deleted vaults, secrets, keys, and certificates for recovery, preventing accidental permanent loss.

---

## Question 8
What is purge protection?

- A) Data compression
- B) Prevents permanent deletion of soft-deleted items until retention period expires
- C) Virus protection
- D) Network security

**Answer: B**
Purge protection enforces retention period, preventing immediate permanent deletion even by privileged users.

---

## Question 9
What are Key Vault access policies?

- A) Network policies
- B) Permissions defining what identities can do with secrets, keys, and certificates
- C) Pricing policies
- D) Backup policies

**Answer: B**
Access policies grant granular permissions (get, list, set, delete) for secrets, keys, and certificates to Azure AD identities.

---

## Question 10
Can Key Vault references be used in App Service?

- A) No integration
- B) Yes, app settings can reference Key Vault secrets using special syntax
- C) Only manually
- D) Requires custom code

**Answer: B**
App Service supports `@Microsoft.KeyVault(SecretUri=...)` syntax to load secrets from Key Vault at runtime.
