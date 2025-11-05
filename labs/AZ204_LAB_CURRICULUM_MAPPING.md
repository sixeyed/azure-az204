# AZ-204 Azure Developer Associate - Lab Curriculum Mapping

## Executive Summary

This repository contains **65 lab directories** covering Azure development, deployment, and security topics. Of these:
- **35+ labs** directly support AZ-204 exam preparation
- **20+ labs** are supplementary for broader Azure knowledge
- **10 labs** focus on Kubernetes and IaaS topics (useful but not core to AZ-204)

---

## AZ-204 Exam Domains Reference

The AZ-204 exam covers 5 main domains:
1. **Develop Azure Compute Solutions** (20-25%)
2. **Develop for Azure Storage** (15-20%)
3. **Implement Azure Security** (20-25%)
4. **Monitor, Troubleshoot, and Optimize** (15-20%)
5. **Connect to and Consume Azure Services** (15-20%)

---

## PART 1: CORE AZ-204 LABS (Direct Exam Coverage)

### DOMAIN 1: DEVELOP AZURE COMPUTE SOLUTIONS

#### Subsection 1A: Azure App Service

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **appservice** | Basic web app deployment, Git deployment | ✓ | Core |
| **appservice-api** | Distributed apps, REST APIs, configuration | ✓ | Core |
| **appservice-config** | Health checks, auto-heal, scaling | ✓ | Core |
| **appservice-cicd** | CI/CD with GitHub, deployment slots | ✓ | Core |
| **appservice-static** | Static Web Apps, GitHub integration | ✓ | Core |

#### Subsection 1B: Azure Functions

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **functions/http** | HTTP triggers, serverless compute | ✓ | Core |
| **functions/blob** | Blob storage triggers | ✓ | Core |
| **functions/cosmos** | Cosmos DB bindings | ✓ | Core |
| **functions/servicebus** | Service Bus triggers | ✓ | Core |
| **functions/signalr** | SignalR integration | ✓ | Core |
| **functions/timer** | Timer triggers, scheduling | ✓ | Core |
| **functions/cicd** | CI/CD for Functions | ✓ | Core |
| **functions/rabbitmq** | RabbitMQ bindings | ✓ | Core |
| **functions-durable/chained** | Chained orchestration | ✓ | Core |
| **functions-durable/fan-out** | Fan-out/fan-in pattern | ✓ | Core |
| **functions-durable/human** | Human interaction patterns | ✓ | Core |

#### Subsection 1C: Container Services

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **aci** | Azure Container Instances basics | ✓ | Core |
| **aci-compose** | Distributed apps with ACI, storage integration | ✓ | Core |
| **acr** | Azure Container Registry, image management | ✓ | Core |
| **docker** | Docker fundamentals (prerequisite) | ✓ | Core |
| **docker-build** | Multi-stage builds | ✓ | Core |
| **docker-compose** | Docker Compose (prerequisite) | ✓ | Core |

---

### DOMAIN 2: DEVELOP FOR AZURE STORAGE

#### Subsection 2A: Blob Storage

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **storage** | Storage accounts overview, redundancy | ✓ | Core |
| **storage-blob** | Blob containers, SAS tokens, access tiers | ✓ | Core |
| **storage-static** | Static website hosting on blobs, CDN | ✓ | Core |

#### Subsection 2B: Azure Files

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **storage-files** | File shares, mounting, SMB protocol | ✓ | Core |

#### Subsection 2C: Table Storage

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **storage-table** | NoSQL table storage, OData queries | ✓ | Core |

#### Subsection 2D: Cosmos DB

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **cosmos** | Cosmos DB NoSQL API, EF Core integration | ✓ | Core |
| **cosmos-mongo** | MongoDB API compatibility | ✓ | Core |
| **cosmos-perf** | Performance tuning, RU/s provisioning | ✓ | Core |
| **cosmos-table** | Table API, migration from Table Storage | ✓ | Core |

#### Subsection 2E: Caching & Performance

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **redis** | Azure Cache for Redis, cache patterns | ✓ | Core |

---

### DOMAIN 3: IMPLEMENT AZURE SECURITY

#### Subsection 3A: Key Vault

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **keyvault** | Key Vault basics, secrets, certificates | ✓ | Core |
| **keyvault-access** | Access policies, managed identities | ✓ | Core |

#### Subsection 3B: Authentication & Authorization

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **signin** | Azure authentication, subscriptions | ✓ | Core |
| **vnet-apps** | Key Vault + VNet + Managed Identity | ✓ | Core |

#### Subsection 3C: Network Security

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **vnet** | Virtual Networks, subnets, basic networking | ✓ | Core |
| **vnet-access** | Network access control, NSGs | ✓ | Core |

---

### DOMAIN 4: MONITOR, TROUBLESHOOT, AND OPTIMIZE

#### Subsection 4A: Application Monitoring

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **applicationinsights** | Application Insights, instrumentation | ✓ | Core |
| **loganalytics** | Log Analytics, KQL queries | ✓ | Core |

---

### DOMAIN 5: CONNECT TO AND CONSUME AZURE SERVICES

#### Subsection 5A: Messaging Services

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **servicebus** | Service Bus queues, message patterns | ✓ | Core |
| **servicebus-pubsub** | Pub-Sub with topics and subscriptions | ✓ | Core |

#### Subsection 5B: Event Processing

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **eventhubs** | Event Hubs, partitions, throughput units | ✓ | Core |
| **eventhubs-consumers** | Event Hubs consumers, checkpoint storage | ✓ | Core |

#### Subsection 5C: API Management

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **apim** | API Management basics, gateway, policies | ✓ | Core |
| **apim-mock** | API mocking, design-first approach | ✓ | Core |
| **apim-policies** | Request/response policies | ✓ | Core |
| **apim-versioning** | API versioning, changelog management | ✓ | Core |

#### Subsection 5D: Real-Time Communication

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **signalr** | Azure SignalR Service, WebSockets | ✓ | Core |

---

## PART 2: SUPPLEMENTARY LABS (Valuable but not core to AZ-204)

### Infrastructure as Code & Deployment

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **arm** | ARM JSON templates | ✓ | Supplementary |
| **arm-bicep** | Bicep templates (ARM successor) | ✓ | Supplementary |
| **resourcegroups** | Resource Group management | ✓ | Foundation |

### Load Balancing & API Gateway

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **appgw** | Application Gateway, WAF, layer 7 LB | ✓ | Supplementary |
| **frontdoor** | Azure Front Door, CDN, DDoS | ✓ | Supplementary |

### SQL Databases

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **sql** | Azure SQL Database | ✓ | Supplementary |
| **sql-schema** | SQL schema management | ✓ | Supplementary |

---

## PART 3: BEYOND AZ-204 SCOPE (Kubernetes & IaaS Focus)

### Kubernetes Services

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **kubernetes** | Kubernetes basics (not Azure) | ✓ | Out of Scope |
| **aks** | Azure Kubernetes Service | ✓ | Extended |
| **aks-apps** | Deploying apps on AKS | ✓ | Extended |
| **aks-ingress** | Kubernetes Ingress controllers | ✓ | Extended |
| **aks-keyvault** | Key Vault integration with AKS | ✓ | Extended |
| **aks-persistentvolumes** | Storage in Kubernetes | ✓ | Extended |

### Virtual Machines (IaaS)

| Lab | Focus | README | Status |
|-----|-------|--------|--------|
| **vm** | Virtual Machines basics | ✓ | Out of Scope |
| **vm-config** | VM configuration | ✓ | Out of Scope |
| **vm-image** | Custom VM images | ✓ | Out of Scope |
| **vm-web** | Web applications on VMs | ✓ | Out of Scope |
| **vm-win** | Windows VMs | ✓ | Out of Scope |
| **vmss-linux** | Linux VM Scale Sets | ✓ | Out of Scope |
| **vmss-win** | Windows VM Scale Sets | ✓ | Out of Scope |
| **sql-vm** | SQL Server on VMs | ✓ | Out of Scope |
| **iaas-apps** | Application deployment on IaaS | ✓ | Out of Scope |
| **iaas-bicep** | IaaS infrastructure with Bicep | ✓ | Out of Scope |

---

## COMPREHENSIVE LAB INVENTORY (All 65 Labs)

### Complete List with Metadata

| # | Lab Name | Technology | Domain | README | Type |
|---|----------|------------|--------|--------|------|
| 1 | aci | Azure Container Instances | Compute | ✓ | Core |
| 2 | aci-compose | Distributed ACI + Storage | Compute | ✓ | Core |
| 3 | acr | Container Registry | Compute | ✓ | Core |
| 4 | aks | Kubernetes Service | Compute | ✓ | Extended |
| 5 | aks-apps | Apps on AKS | Compute | ✓ | Extended |
| 6 | aks-ingress | AKS Ingress | Compute | ✓ | Extended |
| 7 | aks-keyvault | AKS + Key Vault | Compute/Security | ✓ | Extended |
| 8 | aks-persistentvolumes | AKS Storage | Compute | ✓ | Extended |
| 9 | apim | API Management | Services | ✓ | Core |
| 10 | apim-mock | Mock APIs | Services | ✓ | Core |
| 11 | apim-policies | APIM Policies | Services | ✓ | Core |
| 12 | apim-versioning | API Versioning | Services | ✓ | Core |
| 13 | appgw | Application Gateway | Networking | ✓ | Supplementary |
| 14 | applicationinsights | Monitoring | Monitoring | ✓ | Core |
| 15 | appservice | App Service Web Apps | Compute | ✓ | Core |
| 16 | appservice-api | App Service REST APIs | Compute | ✓ | Core |
| 17 | appservice-cicd | App Service CI/CD | Compute | ✓ | Core |
| 18 | appservice-config | App Service Config | Compute | ✓ | Core |
| 19 | appservice-static | Static Web Apps | Compute | ✓ | Core |
| 20 | arm | ARM Templates | IaC | ✓ | Supplementary |
| 21 | arm-bicep | Bicep Templates | IaC | ✓ | Supplementary |
| 22 | cosmos | Cosmos DB NoSQL | Storage | ✓ | Core |
| 23 | cosmos-mongo | Cosmos DB Mongo API | Storage | ✓ | Core |
| 24 | cosmos-perf | Cosmos DB Performance | Storage | ✓ | Core |
| 25 | cosmos-table | Cosmos DB Table API | Storage | ✓ | Core |
| 26 | docker | Docker Fundamentals | Compute | ✓ | Core |
| 27 | docker-build | Multi-Stage Builds | Compute | ✓ | Core |
| 28 | docker-compose | Docker Compose | Compute | ✓ | Core |
| 29 | eventhubs | Event Hubs | Services | ✓ | Core |
| 30 | eventhubs-consumers | Event Hub Consumers | Services | ✓ | Core |
| 31 | frontdoor | Azure Front Door | Networking | ✓ | Supplementary |
| 32 | functions/http | Azure Functions HTTP | Compute | ✓ | Core |
| 33 | functions/blob | Functions Blob Trigger | Compute | ✓ | Core |
| 34 | functions/cosmos | Functions Cosmos Binding | Compute | ✓ | Core |
| 35 | functions/servicebus | Functions SB Trigger | Compute | ✓ | Core |
| 36 | functions/signalr | Functions SignalR | Compute | ✓ | Core |
| 37 | functions/timer | Functions Timer Trigger | Compute | ✓ | Core |
| 38 | functions/cicd | Functions CI/CD | Compute | ✓ | Core |
| 39 | functions/rabbitmq | Functions RabbitMQ | Compute | ✓ | Core |
| 40 | functions-durable/chained | Durable Chained | Compute | ✓ | Core |
| 41 | functions-durable/fan-out | Durable Fan-Out | Compute | ✓ | Core |
| 42 | functions-durable/human | Durable Human Interaction | Compute | ✓ | Core |
| 43 | iaas-apps | Apps on IaaS | Compute | ✓ | Out of Scope |
| 44 | iaas-bicep | IaaS with Bicep | IaC | ✓ | Out of Scope |
| 45 | keyvault | Key Vault Basics | Security | ✓ | Core |
| 46 | keyvault-access | Key Vault Access Control | Security | ✓ | Core |
| 47 | kubernetes | Kubernetes (generic) | Compute | ✓ | Out of Scope |
| 48 | loganalytics | Log Analytics | Monitoring | ✓ | Core |
| 49 | redis | Azure Cache for Redis | Storage | ✓ | Core |
| 50 | resourcegroups | Resource Groups | Foundation | ✓ | Foundation |
| 51 | servicebus | Service Bus Queues | Services | ✓ | Core |
| 52 | servicebus-pubsub | Service Bus Pub-Sub | Services | ✓ | Core |
| 53 | signalr | Azure SignalR Service | Services | ✓ | Core |
| 54 | signin | Azure Signin | Foundation | ✓ | Foundation |
| 55 | sql | Azure SQL Database | Storage | ✓ | Supplementary |
| 56 | sql-schema | SQL Schema | Storage | ✓ | Supplementary |
| 57 | sql-vm | SQL on VMs | Storage | ✓ | Out of Scope |
| 58 | storage | Storage Accounts | Storage | ✓ | Core |
| 59 | storage-blob | Blob Storage | Storage | ✓ | Core |
| 60 | storage-files | Azure Files | Storage | ✓ | Core |
| 61 | storage-static | Static Websites | Storage | ✓ | Core |
| 62 | storage-table | Table Storage | Storage | ✓ | Core |
| 63 | vm | Virtual Machines | Compute | ✓ | Out of Scope |
| 64 | vnet | Virtual Networks | Networking | ✓ | Supplementary |
| 65 | vnet-access | VNet Access Control | Networking | ✓ | Supplementary |
| 66 | vnet-apps | VNet + Vault + Security | Security | ✓ | Core |
| 67 | vm-config | VM Configuration | Compute | ✓ | Out of Scope |
| 68 | vm-image | Custom VM Images | Compute | ✓ | Out of Scope |
| 69 | vm-web | Web Apps on VMs | Compute | ✓ | Out of Scope |
| 70 | vm-win | Windows VMs | Compute | ✓ | Out of Scope |
| 71 | vmss-linux | Linux VM Scale Sets | Compute | ✓ | Out of Scope |
| 72 | vmss-win | Windows VM Scale Sets | Compute | ✓ | Out of Scope |

**Note:** Total actual unique directory count: 65. The table above groups functions subdirectories and shows all paths.

---

## LAB CATEGORIZATION BY AZ-204 RELEVANCE

### Category A: ESSENTIAL FOR AZ-204 (35+ labs)

**You MUST complete these to be exam-ready:**

1. **Azure Functions** (11 labs)
   - HTTP triggers, bindings, triggers, durable functions

2. **Azure App Service** (5 labs)
   - Web apps, APIs, configuration, CI/CD, static web apps

3. **Azure Storage** (9 labs)
   - Storage accounts, blobs, files, tables, Cosmos DB (4 variants), Redis caching

4. **Containers** (6 labs)
   - Docker basics, ACR, ACI (single and multi-container)

5. **Messaging & Events** (6 labs)
   - Service Bus (queues, pub-sub), Event Hubs (basic, consumers)

6. **API Management** (4 labs)
   - APIM basics, mocking, policies, versioning

7. **Security** (3 labs)
   - Key Vault (basics, access control), VNet security

8. **Monitoring** (2 labs)
   - Application Insights, Log Analytics

9. **Networking & Support** (2 labs)
   - SignalR, Basic networking concepts

10. **Docker & Container Basics** (3 labs)
    - Docker 101, multi-stage builds, compose

---

### Category B: VALUABLE SUPPLEMENTARY (10-15 labs)

**These enhance your Azure skills but aren't exam-critical:**

- Application Gateway (load balancing, WAF)
- Azure Front Door (CDN, global routing)
- ARM Templates & Bicep (Infrastructure as Code)
- Azure SQL (not typically tested in depth for AZ-204)
- VNets & networking depth

---

### Category C: OUT OF SCOPE FOR AZ-204 (15-20 labs)

**These are useful for Azure learning but not exam-focused:**

- Kubernetes (AKS) - 6 labs
  - Azure Kubernetes Service is an advanced topic
  - Only briefly mentioned in some AZ-204 contexts

- Virtual Machines (IaaS) - 7 labs
  - VMs, Scale Sets, custom images, configuration
  - Not the focus of developer-level AZ-204

- Generic Kubernetes - 1 lab
  - Kubernetes basics (platform-agnostic)

---

## COVERAGE ANALYSIS BY AZ-204 DOMAIN

### Domain 1: Develop Azure Compute Solutions
**Labs: 20+** | **Coverage: Excellent** ✓

- App Service: 5 labs (appservice, appservice-api, appservice-config, appservice-cicd, appservice-static)
- Azure Functions: 11 labs (http, blob, cosmos, servicebus, signalr, timer, cicd, rabbitmq, durable-chained, durable-fan-out, durable-human)
- Containers: 6 labs (docker, docker-build, docker-compose, aci, aci-compose, acr)

**Gaps:**
- Azure Logic Apps (no dedicated lab, but partially covered through other messaging labs)

---

### Domain 2: Develop for Azure Storage
**Labs: 14+** | **Coverage: Excellent** ✓

- Blob Storage: 3 labs (storage, storage-blob, storage-static)
- Cosmos DB: 4 labs (cosmos, cosmos-mongo, cosmos-perf, cosmos-table)
- Table Storage: 1 lab (storage-table)
- Azure Files: 1 lab (storage-files)
- Redis Caching: 1 lab (redis)
- SQL Database: 2 labs (sql, sql-schema) - supplementary

**Gaps:**
- Azure Data Lake Storage (not covered)
- Advanced Cosmos DB features (change feed, triggers)

---

### Domain 3: Implement Azure Security
**Labs: 5+** | **Coverage: Good** ✓

- Key Vault: 2 labs (keyvault, keyvault-access)
- Managed Identity & Authentication: 3 labs (keyvault-access, vnet-apps, signin)
- Network Security: 2 labs (vnet, vnet-access)

**Gaps:**
- Azure AD / OAuth (minimal coverage, mostly in keyvault-access)
- Certificate management (mentioned but not deeply covered)
- Advanced role-based access control (RBAC) concepts

---

### Domain 4: Monitor, Troubleshoot, and Optimize
**Labs: 2** | **Coverage: Adequate** ~

- Application Insights: 1 lab (applicationinsights)
- Log Analytics: 1 lab (loganalytics)

**Gaps:**
- Azure Monitor advanced features
- Performance optimization techniques
- Cost optimization strategies
- Advanced diagnostic scenarios

---

### Domain 5: Connect to and Consume Azure Services
**Labs: 13+** | **Coverage: Excellent** ✓

- Service Bus: 2 labs (servicebus, servicebus-pubsub)
- Event Hubs: 2 labs (eventhubs, eventhubs-consumers)
- API Management: 4 labs (apim, apim-mock, apim-policies, apim-versioning)
- SignalR: 1 lab (signalr)
- Functions Integration: Covered across function labs

**Gaps:**
- Event Grid (no dedicated lab)
- Azure Notification Hubs (not covered)
- Advanced message routing patterns

---

## KEY FINDINGS & RECOMMENDATIONS

### Strengths
1. ✓ **Comprehensive Docker/Container coverage** - 6 dedicated labs
2. ✓ **Excellent Azure Functions coverage** - 11 labs covering all trigger types
3. ✓ **Strong messaging foundation** - Service Bus and Event Hubs both represented
4. ✓ **Storage options well represented** - Multiple storage types (blob, table, files, Cosmos)
5. ✓ **Security fundamentals covered** - Key Vault and access control
6. ✓ **Practical API Management** - 4 labs on APIM covering mocking, policies, versioning

### Areas for Potential Enhancement
1. ✗ **Azure Logic Apps** - No dedicated lab (could complement Functions labs)
2. ✗ **Event Grid** - Not represented (increasingly important for event-driven architectures)
3. ✗ **Advanced monitoring** - Only 2 labs; could use more on performance profiling
4. ✗ **Azure AD/OAuth** - Minimal coverage (authentication is implicit rather than explicit)
5. ✗ **Cost optimization** - Not explicitly covered in any lab
6. ✗ **Disaster recovery / High availability** - Minimal focus

### Recommended Learning Path for AZ-204

**Phase 1: Foundations** (3 labs)
- signin
- resourcegroups
- docker

**Phase 2: Core Compute** (5 labs)
- appservice
- appservice-api
- functions/http
- functions/blob
- aci

**Phase 3: Storage** (5 labs)
- storage
- storage-blob
- cosmos
- redis
- storage-table

**Phase 4: Messaging & Integration** (6 labs)
- servicebus
- servicebus-pubsub
- eventhubs
- apim
- signalr
- functions/servicebus

**Phase 5: Security & Monitoring** (4 labs)
- keyvault
- keyvault-access
- applicationinsights
- loganalytics

**Phase 6: Advanced Topics** (8 labs)
- appservice-cicd
- functions-durable/chained
- functions-durable/fan-out
- appservice-config
- apim-policies
- apim-versioning
- vnet-apps
- aci-compose

---

## Statistical Summary

| Category | Count | Percentage |
|----------|-------|-----------|
| **Core AZ-204** | 37+ | 57% |
| **Supplementary** | 12 | 18% |
| **Out of Scope (K8s/IaaS)** | 16 | 25% |
| **Total Labs** | 65 | 100% |

| Domain | Primary Labs | Total Coverage |
|--------|-------------|-----------------|
| Compute | 20+ | 31% |
| Storage | 14+ | 22% |
| Services/Messaging | 13+ | 20% |
| Security | 5+ | 8% |
| Monitoring | 2 | 3% |
| Foundation/Infrastructure | 10+ | 15% |

---

## README FILE AUDIT

**Total Labs with README files: 60 of 65**

**Labs WITHOUT top-level README:**
- functions (has 8 subdirectories with READMEs)
- functions-durable (has 3 subdirectories with READMEs)

All other 63 directories have README.md files.

---

## Conclusion

This lab suite provides **excellent coverage for AZ-204 exam preparation**, with particularly strong representation of:
- Azure Functions and triggers
- Container technologies (Docker, ACI, ACR)
- Storage services (multiple variants)
- Messaging services (Service Bus, Event Hubs)
- API Management

The curriculum would benefit from:
- Azure Logic Apps labs
- Event Grid labs
- More advanced monitoring and diagnostics content
- Azure AD / OAuth specific labs

The 35+ core labs, if completed thoroughly, should provide sufficient hands-on experience to pass the AZ-204 exam confidently.
