# Azure Container Registry (ACR) - Quickfire Questions

## Question 1
What is Azure Container Registry (ACR)?


- A) A monitoring service
- B) A virtual machine service
- C) A container orchestrator
- D) A managed private Docker registry service for storing and managing container images

**Answer: D**
ACR is a managed private registry for storing, managing, and securing Docker and OCI container images.
---
## Question 2
What are the ACR service tiers?


- A) Free and Paid
- B) Developer and Production
- C) Basic, Standard, Premium
- D) Small, Medium, Large

**Answer: C**
ACR offers Basic (development), Standard (production), and Premium (high-volume, geo-replication) tiers.
---
## Question 3
What additional features does the Premium tier offer?


- A) Geo-replication, content trust, private link, higher throughput
- B) Free bandwidth
- C) Different container formats
- D) Only more storage

**Answer: A**
Premium adds geo-replication for global distribution, private endpoints, content trust signing, and higher storage/throughput.
---
## Question 4
How do you authenticate to ACR?


- A) Only username/password
- B) No authentication
- C) Azure AD identity, service principal, admin account, or token
- D) SSH keys

**Answer: C**
ACR supports Azure AD identities (including managed identity), service principals, admin account, and repository-scoped tokens.
---
## Question 5
What is the recommended authentication method for production workloads?


- A) Admin account
- B) Anonymous access
- C) Shared password
- D) Azure AD service principal or managed identity

**Answer: D**
Managed identities or service principals provide secure, auditable access without managing credentials.
---
## Question 6
Can ACR build container images?


- A) Only locally
- B) No, only stores images
- C) Requires separate build service
- D) Yes, using ACR Tasks for cloud-based image builds

**Answer: D**
ACR Tasks can build images in the cloud from source code, eliminating need for local Docker daemon.
---
## Question 7
What is ACR geo-replication used for?


- A) Replicating registry across multiple Azure regions for low-latency access globally
- B) Load balancing
- C) Backup only
- D) Cost reduction

**Answer: A**
Geo-replication maintains registry copies in multiple regions, reducing latency for global deployments.
---
## Question 8
What image formats does ACR support?


- A) Docker images, OCI images, Helm charts, OCI artifacts
- B) Only Docker images
- C) Only Windows containers
- D) Only Linux containers

**Answer: A**
ACR supports Docker/OCI container images, Helm charts, and other OCI artifacts.
---
## Question 9
What is a webhook in ACR?


- A) A billing alert
- B) A monitoring tool
- C) A security feature
- D) A notification triggered by registry events like image push/delete

**Answer: D**
Webhooks notify external services when registry events occur, enabling CI/CD automation.
---
## Question 10
Can Azure services pull images from ACR without credentials?


- A) Yes, using managed identities (for ACI, App Service, AKS, etc.)
- B) No, always need credentials
- C) Only from same region
- D) Only for public images

**Answer: A**
Azure services can use system or user-assigned managed identities to authenticate to ACR without managing credentials.