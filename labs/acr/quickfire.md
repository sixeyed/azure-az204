# Azure Container Registry (ACR) - Quickfire Questions

## Question 1
What is Azure Container Registry (ACR)?

- A) A container orchestrator
- B) A managed private Docker registry service for storing and managing container images
- C) A monitoring service
- D) A virtual machine service

**Answer: B**
ACR is a managed private registry for storing, managing, and securing Docker and OCI container images.

---

## Question 2
What are the ACR service tiers?

- A) Free and Paid
- B) Basic, Standard, Premium
- C) Small, Medium, Large
- D) Developer and Production

**Answer: B**
ACR offers Basic (development), Standard (production), and Premium (high-volume, geo-replication) tiers.

---

## Question 3
What additional features does the Premium tier offer?

- A) Only more storage
- B) Geo-replication, content trust, private link, higher throughput
- C) Different container formats
- D) Free bandwidth

**Answer: B**
Premium adds geo-replication for global distribution, private endpoints, content trust signing, and higher storage/throughput.

---

## Question 4
How do you authenticate to ACR?

- A) Only username/password
- B) Azure AD identity, service principal, admin account, or token
- C) SSH keys
- D) No authentication

**Answer: B**
ACR supports Azure AD identities (including managed identity), service principals, admin account, and repository-scoped tokens.

---

## Question 5
What is the recommended authentication method for production workloads?

- A) Admin account
- B) Azure AD service principal or managed identity
- C) Anonymous access
- D) Shared password

**Answer: B**
Managed identities or service principals provide secure, auditable access without managing credentials.

---

## Question 6
Can ACR build container images?

- A) No, only stores images
- B) Yes, using ACR Tasks for cloud-based image builds
- C) Only locally
- D) Requires separate build service

**Answer: B**
ACR Tasks can build images in the cloud from source code, eliminating need for local Docker daemon.

---

## Question 7
What is ACR geo-replication used for?

- A) Backup only
- B) Replicating registry across multiple Azure regions for low-latency access globally
- C) Load balancing
- D) Cost reduction

**Answer: B**
Geo-replication maintains registry copies in multiple regions, reducing latency for global deployments.

---

## Question 8
What image formats does ACR support?

- A) Only Docker images
- B) Docker images, OCI images, Helm charts, OCI artifacts
- C) Only Windows containers
- D) Only Linux containers

**Answer: B**
ACR supports Docker/OCI container images, Helm charts, and other OCI artifacts.

---

## Question 9
What is a webhook in ACR?

- A) A monitoring tool
- B) A notification triggered by registry events like image push/delete
- C) A security feature
- D) A billing alert

**Answer: B**
Webhooks notify external services when registry events occur, enabling CI/CD automation.

---

## Question 10
Can Azure services pull images from ACR without credentials?

- A) No, always need credentials
- B) Yes, using managed identities (for ACI, App Service, AKS, etc.)
- C) Only from same region
- D) Only for public images

**Answer: B**
Azure services can use system or user-assigned managed identities to authenticate to ACR without managing credentials.
