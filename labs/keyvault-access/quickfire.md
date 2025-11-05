# Key Vault Access Control - Quickfire Questions

## Question 1
What authentication method is recommended for applications accessing Key Vault?

- A) Connection strings
- B) Managed Identity
- C) Hardcoded passwords
- D) Public access

**Answer: B**
Managed Identity provides secure, passwordless authentication without storing credentials in code or configuration.

---

## Question 2
What is a system-assigned managed identity?

- A) User account
- B) Identity lifecycle tied to Azure resource; deleted when resource is deleted
- C) Service principal
- D) API key

**Answer: B**
System-assigned identity is automatically created/managed by Azure, tied to a single resource's lifecycle.

---

## Question 3
What is a user-assigned managed identity?

- A) Regular user account
- B) Standalone identity resource that can be assigned to multiple Azure resources
- C) System identity
- D) Group identity

**Answer: B**
User-assigned identity is created independently and can be shared across multiple resources.

---

## Question 4
What are the two permission models for Key Vault?

- A) Only one model
- B) Access Policies (vault-scoped) and Azure RBAC (Azure-wide)
- C) Public and Private
- D) Read and Write

**Answer: B**
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

- A) Only Owner
- B) Key Vault Administrator, Reader, Secrets Officer, Secrets User, Keys Officer, Certificates Officer, etc.
- C) Only custom roles
- D) No RBAC roles

**Answer: B**
Built-in roles provide granular access: full admin, read-only, or specific permissions for secrets/keys/certificates.

---

## Question 7
Can you restrict Key Vault access to specific networks?

- A) No network restrictions
- B) Yes, using firewall rules and virtual network service endpoints or private endpoints
- C) Only public access
- D) Only VPN

**Answer: B**
Key Vault firewall can restrict access to specific VNets (via service endpoint) or use private endpoints for VNet integration.

---

## Question 8
What is a private endpoint for Key Vault?

- A) Public IP
- B) Private IP in your VNet providing secure access without internet exposure
- C) API endpoint
- D) Management endpoint

**Answer: B**
Private endpoint creates a private IP in your VNet, eliminating internet exposure and enabling private connectivity.

---

## Question 9
How can you audit Key Vault access?

- A) No auditing
- B) Enable diagnostic logging to Log Analytics, Storage, or Event Hubs
- C) Only manual logs
- D) Email notifications only

**Answer: B**
Diagnostic logs capture who accessed what and when, sent to Log Analytics, Storage Account, or Event Hubs.

---

## Question 10
What is the least privilege principle for Key Vault?

- A) Give everyone full access
- B) Grant minimum necessary permissions to identities
- C) No access for anyone
- D) Random permissions

**Answer: B**
Follow least privilege: grant only required permissions (e.g., Get secret only, not List/Set/Delete if not needed).
