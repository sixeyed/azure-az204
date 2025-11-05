# Key Vault Access Control - Quickfire Questions

## Question 1
What authentication method is recommended for applications accessing Key Vault?


- A) Hardcoded passwords
- B) Managed Identity
- C) Public access
- D) Connection strings

**Answer: B**
Managed Identity provides secure, passwordless authentication without storing credentials in code or configuration.
---
## Question 2
What is a system-assigned managed identity?


- A) Identity lifecycle tied to Azure resource; deleted when resource is deleted
- B) API key
- C) Service principal
- D) User account

**Answer: A**
System-assigned identity is automatically created/managed by Azure, tied to a single resource's lifecycle.
---
## Question 3
What is a user-assigned managed identity?


- A) Standalone identity resource that can be assigned to multiple Azure resources
- B) Regular user account
- C) System identity
- D) Group identity

**Answer: A**
User-assigned identity is created independently and can be shared across multiple resources.
---
## Question 4
What are the two permission models for Key Vault?


- A) Read and Write
- B) Public and Private
- C) Access Policies (vault-scoped) and Azure RBAC (Azure-wide)
- D) Only one model

**Answer: C**
Access Policies (classic, vault-specific) or Azure RBAC (unified, integrated with Azure role system).
---
## Question 5
What is the benefit of Azure RBAC for Key Vault?


- A) Lower cost
- B) Unified permission model across Azure, granular control, easier management at scale
- C) Faster access
- D) No benefits

**Answer: B**
Azure RBAC provides consistent permissions across resources, inheritance, and can apply to management and data planes.
---
## Question 6
What Key Vault built-in RBAC roles are available?


- A) Only custom roles
- B) Key Vault Administrator, Reader, Secrets Officer, Secrets User, Keys Officer, Certificates Officer, etc.
- C) Only Owner
- D) No RBAC roles

**Answer: B**
Built-in roles provide granular access: full admin, read-only, or specific permissions for secrets/keys/certificates.
---
## Question 7
Can you restrict Key Vault access to specific networks?


- A) No network restrictions
- B) Only public access
- C) Yes, using firewall rules and virtual network service endpoints or private endpoints
- D) Only VPN

**Answer: C**
Key Vault firewall can restrict access to specific VNets (via service endpoint) or use private endpoints for VNet integration.
---
## Question 8
What is a private endpoint for Key Vault?


- A) Public IP
- B) Private IP in your VNet providing secure access without internet exposure
- C) Management endpoint
- D) API endpoint

**Answer: B**
Private endpoint creates a private IP in your VNet, eliminating internet exposure and enabling private connectivity.
---
## Question 9
How can you audit Key Vault access?


- A) No auditing
- B) Only manual logs
- C) Email notifications only
- D) Enable diagnostic logging to Log Analytics, Storage, or Event Hubs

**Answer: D**
Diagnostic logs capture who accessed what and when, sent to Log Analytics, Storage Account, or Event Hubs.
---
## Question 10
What is the least privilege principle for Key Vault?


- A) Give everyone full access
- B) No access for anyone
- C) Grant minimum necessary permissions to identities
- D) Random permissions

**Answer: C**
Follow least privilege: grant only required permissions (e.g., Get secret only, not List/Set/Delete if not needed).