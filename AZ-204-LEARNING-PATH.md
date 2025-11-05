# AZ-204 Learning Path Guide

**Your Complete Roadmap to Azure Developer Associate Certification**

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites Setup](#prerequisites-setup)
3. [Learning Paths Overview](#learning-paths-overview)
4. [Path A: Fast Track (40-50 hours)](#path-a-fast-track-core-only)
5. [Path B: Comprehensive (60-70 hours)](#path-b-comprehensive-recommended)
6. [Path C: Complete Azure Developer (80+ hours)](#path-c-complete-azure-developer)
7. [Dependency Graph](#dependency-graph)
8. [Checkpoints & Self-Assessment](#checkpoints--self-assessment)
9. [Alternative Paths by Role](#alternative-paths-by-role)
10. [Tips & Best Practices](#tips--best-practices)

---

## Introduction

### How Learning Paths Work

This guide provides **three distinct learning paths** to AZ-204 certification, each designed for different goals and time constraints. All paths cover the essential exam topics, but differ in depth and breadth.

**Key Principles:**
- **Hands-on first**: Learn by doing, not just reading
- **Progressive complexity**: Build from fundamentals to advanced topics
- **Domain-focused**: Complete related topics together for better retention
- **Practical scenarios**: Real-world applications, not just CLI commands
- **Self-paced**: Adapt timing to your schedule and learning speed

### Choosing the Right Path

| Path | Time Investment | Best For | Outcome |
|------|----------------|----------|---------|
| **Path A: Fast Track** | 40-50 hours | Experienced Azure devs, focused exam prep | Pass AZ-204 exam |
| **Path B: Comprehensive** | 60-70 hours | Most learners, career development | Excel at AZ-204 + practical Azure skills |
| **Path C: Complete** | 80+ hours | Career changers, thorough understanding | Master Azure development ecosystem |

**Still not sure?**
- New to Azure or cloud? → **Path B or C**
- Already using Azure at work? → **Path A or B**
- Career change to cloud? → **Path C**
- Just need the cert quickly? → **Path A**

---

## Prerequisites Setup

### Required Tools & Accounts

#### 1. Azure Subscription
```bash
# Create a free account (includes $200 credit)
# Visit: https://azure.microsoft.com/free/

# Verify your subscription
az account show
```

**Cost Management Tips:**
- Use free tier services whenever possible
- Delete resource groups immediately after labs
- Set up billing alerts in Azure Portal
- Expected total cost: $20-50 for all labs

#### 2. Development Environment

**Required:**
```bash
# Azure CLI (latest version)
az --version  # Should be 2.50.0 or higher

# Git
git --version

# Docker Desktop
docker --version
```

**Programming Language (choose at least one):**
```bash
# .NET 6 or .NET 8 SDK (recommended for AZ-204)
dotnet --version

# OR Python 3.8+
python --version

# OR Node.js 16+ (for JavaScript/TypeScript)
node --version
```

**Recommended IDE:**
- Visual Studio Code (with Azure extensions)
- OR Visual Studio 2022

#### 3. Azure CLI Login
```bash
# Login to Azure
az login

# Set your default subscription (if multiple)
az account list --output table
az account set --subscription "<subscription-name-or-id>"

# Verify authentication
az account show
```

#### 4. Essential VS Code Extensions

If using VS Code, install:
- Azure Account
- Azure Functions
- Azure App Service
- Azure Storage
- Docker
- C# (if using .NET)

#### 5. Azure Functions Core Tools

Required for Functions labs:
```bash
# Install Azure Functions Core Tools
# Windows (with npm):
npm install -g azure-functions-core-tools@4

# macOS:
brew tap azure/functions
brew install azure-functions-core-tools@4

# Verify installation
func --version
```

### Verification Checklist

Before starting labs, verify:
- [ ] Azure subscription active and accessible
- [ ] Azure CLI installed and logged in
- [ ] Development language SDK installed (.NET/Python/Node.js)
- [ ] Docker Desktop running
- [ ] Azure Functions Core Tools installed
- [ ] Git configured
- [ ] Code editor ready (VS Code or Visual Studio)

---

## Learning Paths Overview

### Quick Comparison

| Feature | Path A | Path B | Path C |
|---------|--------|--------|--------|
| **Core AZ-204 Labs** | 25 labs | 38 labs | 50+ labs |
| **Supplementary Labs** | 0 labs | 5 labs | 10+ labs |
| **Time Investment** | 40-50 hrs | 60-70 hrs | 80-100 hrs |
| **Exam Coverage** | 85% | 95% | 100% |
| **Practical Skills** | Good | Excellent | Master |
| **Decision-Making Skills** | Basic | Strong | Expert |
| **Kubernetes/AKS** | No | Optional | Yes |
| **IaaS (VMs)** | No | Comparison only | Yes |

---

## Path A: Fast Track (Core Only)

**Target Audience:** Developers with Azure experience who need certification quickly

**Total Time:** 40-50 hours
**Labs:** 25 essential labs
**Exam Readiness:** 85%

### Phase 1: Foundation & Setup (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 1 | `setup/` | Initial setup verification | 30 min | Azure account |
| 2 | `signin` | Azure authentication, subscriptions | 45 min | Azure CLI |
| 3 | `resourcegroups` | Resource group management | 30 min | signin |
| 4 | `docker` | Docker fundamentals | 90 min | Docker Desktop |

**Checkpoint 1:** You can create resources and run containers

---

### Phase 2: Azure Compute - Web Apps (5 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 5 | `appservice` | Deploy web apps, Git integration | 90 min | resourcegroups |
| 6 | `appservice-config` | App settings, connection strings | 60 min | appservice |
| 7 | `appservice-cicd` | Deployment slots, CI/CD | 90 min | appservice |
| 8 | `storage` | Storage accounts basics | 60 min | resourcegroups |
| 9 | `storage-blob` | Blob containers, SAS tokens | 60 min | storage |

**Checkpoint 2:** Deploy and configure production-ready web apps

---

### Phase 3: Azure Functions (6 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 10 | `functions/http` | HTTP triggers, serverless basics | 90 min | Functions Core Tools |
| 11 | `functions/timer` | Scheduled executions | 60 min | functions/http |
| 12 | `functions/blob` | Blob storage triggers | 75 min | storage-blob |
| 13 | `functions/servicebus` | Service Bus integration | 75 min | servicebus |
| 14 | `functions-durable/chained` | Function orchestration | 90 min | functions/http |

**Checkpoint 3:** Build serverless applications with multiple trigger types

---

### Phase 4: Containers (4 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 15 | `acr` | Container registry, push images | 60 min | docker |
| 16 | `aci` | Azure Container Instances | 75 min | acr |
| 17 | `container-apps` | Azure Container Apps | 90 min | acr |
| 18 | `docker-build` | Multi-stage builds | 75 min | docker |

**Checkpoint 4:** Containerize and deploy applications

---

### Phase 5: Storage & Data (5 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 19 | `cosmos` | Cosmos DB NoSQL API | 90 min | resourcegroups |
| 20 | `cosmos-perf` | Performance tuning, RU/s | 75 min | cosmos |
| 21 | `storage-table` | Table storage, NoSQL queries | 60 min | storage |
| 22 | `redis` | Azure Cache for Redis | 90 min | appservice |

**Checkpoint 5:** Work with multiple data storage solutions

---

### Phase 6: Security (4 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 23 | `keyvault` | Secrets, keys, certificates | 90 min | resourcegroups |
| 24 | `keyvault-access` | Managed identities, access policies | 90 min | keyvault |
| 25 | `microsoft-graph` | Microsoft Graph API | 90 min | signin |

**Checkpoint 6:** Implement secure Azure solutions

---

### Phase 7: Messaging & Events (5 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 26 | `servicebus` | Service Bus queues | 75 min | resourcegroups |
| 27 | `servicebus-pubsub` | Topics and subscriptions | 75 min | servicebus |
| 28 | `eventhubs` | Event Hubs, partitions | 90 min | resourcegroups |
| 29 | `eventgrid` | Event-driven architecture | 90 min | storage-blob |

**Checkpoint 7:** Build event-driven and message-based solutions

---

### Phase 8: API Management (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 30 | `apim` | API gateway, policies basics | 90 min | appservice |
| 31 | `apim-policies` | Transformation, throttling | 90 min | apim |

**Checkpoint 8:** Manage and secure APIs

---

### Phase 9: Monitoring (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 32 | `applicationinsights` | APM, telemetry | 90 min | appservice |
| 33 | `loganalytics` | KQL queries, log analysis | 90 min | applicationinsights |

**Checkpoint 9:** Monitor and troubleshoot Azure solutions

---

### Phase 10: Review & Practice (8 hours)

| Activity | Time | Notes |
|----------|------|-------|
| Review AZ-204.md files | 3 hrs | Advanced exercises in core labs |
| Practice exam scenarios | 3 hrs | Common exam questions |
| Hands-on review | 2 hrs | Rebuild key components from memory |

**Final Checkpoint:** Ready for AZ-204 exam

---

## Path B: Comprehensive (Recommended)

**Target Audience:** Most learners seeking both certification and practical Azure skills

**Total Time:** 60-70 hours
**Labs:** 38 labs (25 core + 13 supplementary)
**Exam Readiness:** 95%

### All Phase 1-9 from Path A, PLUS:

---

### Phase 11: Advanced App Service (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 34 | `appservice-api` | RESTful APIs, distributed apps | 90 min | appservice |
| 35 | `appservice-static` | Static Web Apps, Jamstack | 90 min | storage-static |

---

### Phase 12: Advanced Functions (4 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 36 | `functions/cosmos` | Cosmos DB bindings | 60 min | cosmos |
| 37 | `functions-durable/fan-out` | Fan-out/fan-in pattern | 90 min | functions-durable/chained |
| 38 | `functions-durable/human` | Human interaction patterns | 90 min | functions-durable/fan-out |

---

### Phase 13: Advanced Storage (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 39 | `storage-files` | Azure Files, SMB shares | 60 min | storage |
| 40 | `storage-static` | Static website hosting | 60 min | storage-blob |
| 41 | `cosmos-mongo` | MongoDB API | 60 min | cosmos |

---

### Phase 14: Advanced Containers (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 42 | `docker-compose` | Multi-container applications | 90 min | docker |
| 43 | `aci-compose` | Multi-container ACI deployments | 90 min | aci |

---

### Phase 15: Advanced Messaging (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 44 | `eventhubs-consumers` | Consumer groups, checkpointing | 90 min | eventhubs |
| 45 | `signalr` | Real-time communication | 90 min | appservice |

---

### Phase 16: Advanced API Management (2 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 46 | `apim-versioning` | API versions, revisions | 60 min | apim |
| 47 | `apim-mock` | Mock APIs, design-first | 60 min | apim |

---

### Phase 17: Networking & Security (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 48 | `vnet` | Virtual networks, subnets | 90 min | resourcegroups |
| 49 | `vnet-access` | NSGs, service endpoints | 90 min | vnet |
| 50 | `vnet-apps` | VNet + Key Vault + Managed ID | 90 min | keyvault-access, vnet |

---

### Phase 18: Infrastructure Comparison (3 hours)

**Purpose:** Understand PaaS vs IaaS trade-offs for exam scenarios

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 51 | `vm` | Virtual machines basics | 60 min | resourcegroups |
| 52 | `vm-web` | Web apps on VMs vs App Service | 60 min | vm, appservice |
| 53 | `aks` | AKS intro (comparison to ACI) | 60 min | aci |

**Note:** These are for comparison/decision-making, not deep IaaS knowledge

---

### Phase 19: Infrastructure as Code (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 54 | `arm` | ARM templates basics | 90 min | resourcegroups |
| 55 | `arm-bicep` | Bicep (ARM successor) | 90 min | arm |

---

### Phase 20: Review & Advanced Practice (8 hours)

| Activity | Time | Notes |
|----------|------|-------|
| Review all AZ-204.md files | 4 hrs | SDK examples, exam scenarios |
| Build mini-project | 2 hrs | Combine 5+ services |
| Practice exams | 2 hrs | Full exam simulations |

**Final Checkpoint:** Highly prepared for AZ-204 exam + strong Azure skills

---

## Path C: Complete Azure Developer

**Target Audience:** Career changers, thorough learners, cloud architects

**Total Time:** 80-100 hours
**Labs:** 50+ labs (all core + all supplementary)
**Exam Readiness:** 100%

### All Phases from Path B, PLUS:

---

### Phase 21: Complete Kubernetes Journey (8 hours)

**Purpose:** Deep understanding of container orchestration

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 56 | `kubernetes/pods` | Pod fundamentals | 60 min | docker |
| 57 | `kubernetes/deployments` | Deployments, ReplicaSets | 60 min | kubernetes/pods |
| 58 | `kubernetes/services` | Service discovery | 60 min | kubernetes/deployments |
| 59 | `aks-apps` | Deploy apps to AKS | 90 min | aks |
| 60 | `aks-ingress` | Ingress controllers | 90 min | aks-apps |
| 61 | `aks-persistentvolumes` | Persistent storage in K8s | 90 min | aks-apps |
| 62 | `aks-keyvault` | Key Vault integration | 90 min | aks-apps, keyvault |

---

### Phase 22: Complete IaaS Understanding (6 hours)

**Purpose:** Full spectrum of Azure compute options

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 63 | `vm-config` | VM extensions, cloud-init | 60 min | vm |
| 64 | `vm-image` | Custom VM images | 90 min | vm |
| 65 | `vmss-linux` | VM Scale Sets | 90 min | vm |
| 66 | `iaas-apps` | Complete IaaS application | 90 min | vm-web |
| 67 | `iaas-bicep` | IaaS with Bicep templates | 90 min | arm-bicep |

---

### Phase 23: Networking & Load Balancing (4 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 68 | `appgw` | Application Gateway, WAF | 90 min | vnet |
| 69 | `frontdoor` | Azure Front Door, CDN | 90 min | appservice |

---

### Phase 24: Database Depth (3 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 70 | `cosmos-table` | Table API, migration | 60 min | cosmos |
| 71 | `sql` | Azure SQL Database | 90 min | resourcegroups |
| 72 | `sql-schema` | Schema management, migrations | 60 min | sql |

---

### Phase 25: Advanced Functions (2 hours)

| # | Lab | Focus | Time | Prerequisites |
|---|-----|-------|------|---------------|
| 73 | `functions/signalr` | SignalR Functions binding | 60 min | signalr |
| 74 | `functions/rabbitmq` | RabbitMQ integration | 60 min | functions/http |
| 75 | `functions/cicd` | Functions CI/CD pipelines | 60 min | appservice-cicd |

---

### Phase 26: Capstone Projects (10 hours)

Build complete solutions combining multiple services:

1. **E-commerce Platform** (4 hours)
   - App Service frontend
   - Functions for order processing
   - Cosmos DB for data
   - Service Bus for queuing
   - Key Vault for secrets
   - Application Insights for monitoring

2. **IoT Data Pipeline** (3 hours)
   - Event Hubs for ingestion
   - Functions for processing
   - Blob Storage for archival
   - Redis for caching
   - APIM for APIs

3. **Microservices Application** (3 hours)
   - ACI or AKS for services
   - ACR for containers
   - Event Grid for events
   - Cosmos DB for persistence
   - Front Door for routing

---

### Phase 27: Comprehensive Review (10 hours)

| Activity | Time | Notes |
|----------|------|-------|
| All AZ-204.md exercises | 4 hrs | Complete every advanced exercise |
| Decision matrix practice | 2 hrs | When to use which service |
| Practice exams | 3 hrs | Multiple full simulations |
| White paper review | 1 hr | Azure Well-Architected Framework |

**Final Checkpoint:** Complete Azure developer mastery

---

## Dependency Graph

### Visual Representation

```
Foundation Layer (Start Here)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌────────┐  ┌──────────────┐  ┌────────┐
│ signin │  │ resourcegroups│  │ docker │
└───┬────┘  └──────┬───────┘  └───┬────┘
    │              │              │
    └──────┬───────┴──────┬───────┘
           │              │
    ┌──────▼──────┐   ┌───▼────┐
    │   storage   │   │   acr  │
    └──────┬──────┘   └───┬────┘
           │              │
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Compute Track
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌────────────┐        ┌─────────────┐
│ appservice │◄───┬───│ functions/* │
└─────┬──────┘    │   └──────┬──────┘
      │           │          │
      ▼           │          ▼
┌────────────┐    │   ┌──────────────┐
│   apim     │    │   │ functions-   │
└────────────┘    │   │  durable/*   │
                  │   └──────────────┘
                  │
            ┌─────▼──────┐
            │    aci     │
            └─────┬──────┘
                  │
            ┌─────▼────────┐
            │ container-   │
            │    apps      │
            └──────────────┘

Storage & Data Track
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────┐       ┌────────┐
│ storage-blob│       │ cosmos │
└──────┬──────┘       └───┬────┘
       │                  │
       ├──────┬───────────┼──────┬──────────┐
       │      │           │      │          │
       ▼      ▼           ▼      ▼          ▼
  ┌────────┐ ┌──────┐  ┌─────┐ ┌──────┐ ┌──────┐
  │storage-│ │storage│  │cosmos│ │cosmos│ │cosmos│
  │ static │ │ table │  │-mongo│ │-perf │ │-table│
  └────────┘ └──────┘  └──────┘ └──────┘ └──────┘

Messaging & Events Track
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌────────────┐       ┌───────────┐
│ servicebus │       │ eventhubs │
└─────┬──────┘       └─────┬─────┘
      │                    │
      ▼                    ▼
┌──────────────┐    ┌──────────────┐
│ servicebus-  │    │ eventhubs-   │
│   pubsub     │    │  consumers   │
└──────────────┘    └──────────────┘
      │                    │
      └──────┬─────────────┘
             ▼
      ┌──────────┐
      │eventgrid │
      └──────────┘

Security Track
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌──────────┐
│ keyvault │
└────┬─────┘
     │
     ▼
┌──────────────┐       ┌────────┐
│ keyvault-    │       │  vnet  │
│   access     │       └───┬────┘
└──────┬───────┘           │
       │                   ▼
       │            ┌────────────┐
       │            │vnet-access │
       │            └──────┬─────┘
       │                   │
       └──────┬────────────┘
              ▼
       ┌───────────┐
       │ vnet-apps │
       └───────────┘

Monitoring Track
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌───────────────────┐
│ applicationinsights│
└─────────┬──────────┘
          │
          ▼
┌──────────────┐
│ loganalytics │
└──────────────┘
```

### Critical Dependencies

**Must Complete First:**
1. `signin` → Everything
2. `resourcegroups` → All Azure resource labs
3. `docker` → All container labs
4. `storage` → All storage-* labs
5. `functions/http` → All other functions labs

**Common Dependency Chains:**
```
docker → acr → aci → container-apps
storage → storage-blob → functions/blob
cosmos → cosmos-perf → functions/cosmos
servicebus → servicebus-pubsub → functions/servicebus
keyvault → keyvault-access → vnet-apps
appservice → appservice-config → appservice-cicd
```

---

## Checkpoints & Self-Assessment

### Checkpoint 1: Foundation Complete (After 3-5 hours)

**Can you:**
- [ ] Login to Azure CLI and view your subscription
- [ ] Create and delete resource groups
- [ ] Deploy resources using Azure CLI
- [ ] Build and run Docker containers locally
- [ ] Understand basic Azure pricing models

**Self-Assessment Quiz:**
1. What command creates a resource group in East US?
2. How do you list all resources in a resource group?
3. What's the difference between `docker run` and `docker build`?

---

### Checkpoint 2: Compute Services (After 15-20 hours)

**Can you:**
- [ ] Deploy a web app to Azure App Service
- [ ] Configure app settings and connection strings
- [ ] Use deployment slots for staging
- [ ] Create HTTP-triggered Azure Functions
- [ ] Deploy containerized apps to ACI
- [ ] Push images to Azure Container Registry

**Self-Assessment Quiz:**
1. When would you choose App Service over ACI?
2. How do you configure environment variables in Functions?
3. What's the difference between hot swap and cold start?

**Mini-Project:** Deploy a .NET/Python web app with staging slot

---

### Checkpoint 3: Storage & Data (After 25-30 hours)

**Can you:**
- [ ] Create storage accounts with appropriate redundancy
- [ ] Upload blobs and generate SAS tokens
- [ ] Create Cosmos DB databases and containers
- [ ] Choose appropriate consistency levels
- [ ] Implement caching with Redis
- [ ] Query Table Storage using OData

**Self-Assessment Quiz:**
1. When to use Blob vs File vs Table storage?
2. What consistency level for financial transactions?
3. How does partition key affect Cosmos DB performance?

**Mini-Project:** Build a blob upload API with SAS token generation

---

### Checkpoint 4: Security (After 35-40 hours)

**Can you:**
- [ ] Store secrets in Key Vault
- [ ] Configure managed identities
- [ ] Access Key Vault from App Service without passwords
- [ ] Create and rotate secrets
- [ ] Implement network security with VNets
- [ ] Use Microsoft Graph API

**Self-Assessment Quiz:**
1. System-assigned vs user-assigned managed identity?
2. How to grant Function App access to Key Vault?
3. What's the secret rotation best practice?

**Mini-Project:** Secure web app with Key Vault and managed identity

---

### Checkpoint 5: Messaging & Events (After 45-50 hours)

**Can you:**
- [ ] Send and receive Service Bus messages
- [ ] Implement pub-sub with topics/subscriptions
- [ ] Stream events through Event Hubs
- [ ] Use Event Grid for event-driven architecture
- [ ] Choose between Queue vs Service Bus vs Event Hubs

**Self-Assessment Quiz:**
1. Queue Storage vs Service Bus Queue - when to use each?
2. How do Event Hub partitions affect throughput?
3. What's the difference between events and messages?

**Mini-Project:** Order processing system with Service Bus

---

### Checkpoint 6: APIs & Integration (After 55-60 hours)

**Can you:**
- [ ] Create and configure APIM instances
- [ ] Apply policies (throttling, transformation)
- [ ] Version and revision APIs
- [ ] Mock APIs for testing
- [ ] Implement real-time communication with SignalR

**Self-Assessment Quiz:**
1. API version vs API revision - what's the difference?
2. How does rate limiting policy work?
3. When to use SignalR vs webhooks?

**Mini-Project:** API gateway with versioning and throttling

---

### Checkpoint 7: Monitoring & Optimization (After 60-65 hours)

**Can you:**
- [ ] Configure Application Insights
- [ ] Write KQL queries in Log Analytics
- [ ] Create custom telemetry
- [ ] Set up availability tests
- [ ] Analyze performance bottlenecks
- [ ] Implement caching strategies

**Self-Assessment Quiz:**
1. How to trace a request across multiple services?
2. What KQL query finds errors in last 24 hours?
3. Cache-aside vs read-through pattern?

**Mini-Project:** Add full observability to existing application

---

### Final Checkpoint: Exam Ready

**Complete Self-Assessment:**

**Domain 1: Azure Compute (25-30%)**
- [ ] Can explain when to use Functions vs App Service vs Containers
- [ ] Understand all Function trigger types
- [ ] Know deployment slot best practices
- [ ] Can implement Durable Functions patterns

**Domain 2: Azure Storage (15-20%)**
- [ ] Master blob operations and access tiers
- [ ] Understand Cosmos DB consistency levels
- [ ] Can choose appropriate storage type for scenarios
- [ ] Know caching patterns and Redis use cases

**Domain 3: Azure Security (15-20%)**
- [ ] Configure Key Vault and managed identities
- [ ] Implement SAS tokens correctly
- [ ] Understand Azure RBAC
- [ ] Can secure apps without hardcoded secrets

**Domain 4: Monitoring (5-10%)**
- [ ] Configure Application Insights
- [ ] Write basic KQL queries
- [ ] Understand performance optimization
- [ ] Can troubleshoot using logs and metrics

**Domain 5: Azure Services (20-25%)**
- [ ] Know all messaging patterns (queue, pub-sub, streaming)
- [ ] Configure APIM policies
- [ ] Implement event-driven architectures
- [ ] Can choose appropriate messaging service

**Practice Exam Score:** Aim for 85%+ on practice tests

---

## Alternative Paths by Role

### Backend Developer Path (50 hours)

**Focus:** APIs, data, messaging, functions

**Recommended Order:**

**Weeks 1-2: Foundation & Compute**
1. signin, resourcegroups, docker
2. appservice, appservice-api, appservice-config
3. functions/http, functions/timer, functions/blob
4. acr, aci

**Weeks 3-4: Data & Storage**
5. storage, storage-blob, cosmos, cosmos-perf
6. storage-table, redis
7. functions/cosmos

**Weeks 5-6: Messaging & Integration**
8. servicebus, servicebus-pubsub, eventhubs
9. apim, apim-policies, apim-versioning
10. functions/servicebus, eventgrid

**Weeks 7-8: Security & Advanced**
11. keyvault, keyvault-access, microsoft-graph
12. applicationinsights, loganalytics
13. functions-durable (all 3), vnet-apps

**Why this order?**
- Early focus on APIs and data (your primary work)
- Messaging integrated throughout
- Security builds on compute knowledge
- Advanced patterns at the end

---

### Frontend Developer Path (45 hours)

**Focus:** Static sites, APIs, real-time, authentication

**Recommended Order:**

**Weeks 1-2: Web Fundamentals**
1. signin, resourcegroups
2. storage-static, appservice-static
3. storage, storage-blob (for file uploads)
4. appservice, appservice-config

**Weeks 3-4: APIs & Integration**
5. functions/http, apim, apim-policies
6. signalr (real-time updates)
7. microsoft-graph (identity)
8. redis (caching for performance)

**Weeks 5-6: Backend Services**
9. cosmos (data for APIs)
10. servicebus, eventgrid (backend integration)
11. keyvault, keyvault-access (secure config)

**Weeks 7-8: Deployment & Monitoring**
12. appservice-cicd, functions/cicd
13. applicationinsights (user tracking)
14. docker, aci (containerized apps)
15. container-apps (full-stack deployments)

**Why this order?**
- Immediate static site deployment wins
- API consumption before creation
- Real-time features early (common need)
- Backend understanding builds gradually

---

### DevOps Engineer Path (65 hours)

**Focus:** Deployment, IaC, monitoring, containers

**Recommended Order:**

**Weeks 1-2: Infrastructure Foundation**
1. signin, resourcegroups, arm, arm-bicep
2. docker, docker-build, docker-compose
3. acr, aci, container-apps

**Weeks 3-4: Compute Platforms**
4. appservice, appservice-cicd, appservice-config
5. functions/http, functions/cicd
6. vm, vmss-linux, iaas-bicep
7. aks, aks-apps

**Weeks 5-6: Networking & Security**
8. vnet, vnet-access, vnet-apps
9. keyvault, keyvault-access
10. appgw, frontdoor

**Weeks 7-8: Monitoring & Data**
11. applicationinsights, loganalytics
12. storage, storage-blob, cosmos
13. servicebus, eventhubs

**Weeks 9: Advanced Topics**
14. aks-ingress, aks-keyvault, aks-persistentvolumes
15. apim, redis
16. Complete review

**Why this order?**
- IaC and containers first (your domain)
- Platform knowledge builds systematically
- Networking early (critical for troubleshooting)
- Monitoring integrated throughout

---

### Cloud Architect Path (80 hours)

**Focus:** All services, decision-making, design patterns

**Recommended Order:**
Follow **Path C** (Complete Azure Developer) sequentially

**Additional Focus Areas:**
- Complete ALL comparison labs (VM vs App Service vs ACI vs AKS)
- Deep dive into all AZ-204.md advanced sections
- Build decision matrices for service selection
- Study Azure Well-Architected Framework
- Complete all capstone projects

**Why sequential?**
- Architects need comprehensive knowledge
- Comparison requires understanding both options
- Design patterns build on complete service knowledge

---

### Career Changer Path (90 hours)

**Focus:** Solid fundamentals, all core services, practical projects

**Recommended Order:**

**Month 1: Cloud Fundamentals (20 hours)**
1. Complete all foundation labs (signin, resourcegroups, docker)
2. Build understanding of cloud concepts
3. Practice Azure CLI extensively
4. Complete Microsoft Learn "Azure Fundamentals" path

**Month 2: Core Services (25 hours)**
5. All App Service labs
6. All Functions labs (except durable)
7. Container basics (acr, aci)
8. Storage fundamentals

**Month 3: Data & Integration (20 hours)**
9. Cosmos DB (all variants)
10. Messaging (Service Bus, Event Hubs, Event Grid)
11. APIM basics
12. Redis

**Month 4: Security & Advanced (25 hours)**
13. Key Vault (all labs)
14. Durable Functions
15. Monitoring
16. Advanced App Service

**Why this pace?**
- More time per lab for learning fundamentals
- Spaced repetition improves retention
- Project-based reinforcement
- Builds confidence progressively

---

## Tips & Best Practices

### Path A: Fast Track Tips

**Maximize Efficiency:**
1. **Skip README basics** if you know Docker/Azure CLI - go straight to AZ-204.md
2. **Use lab solutions** to check your work, don't struggle for hours
3. **Focus on SDK code** - exam tests programming, not portal clicking
4. **Create cheat sheets** for each domain (your own quick reference)
5. **Time-box labs** - if stuck >15 min, check hints

**Cost Savings:**
- Delete resources immediately after each lab
- Use consumption plans (Functions, APIM)
- Skip optional exploration exercises
- Reuse resource groups when possible

**Common Pitfalls:**
- Don't skip Docker fundamentals (needed for containers)
- Don't ignore AZ-204.md files (that's where exam prep is)
- Don't just follow commands - understand what they do

**When to Use:**
- You have Azure experience (6+ months)
- Time-constrained (need cert in 1-2 months)
- Good at self-directed learning
- Already understand cloud concepts

---

### Path B: Comprehensive Tips

**Maximize Learning:**
1. **Do both README and AZ-204.md** for each lab
2. **Experiment beyond exercises** - "what if I change X?"
3. **Build connections** - how does this integrate with other services?
4. **Create mini-projects** combining multiple services
5. **Review AZ-204-CURRICULUM.md** frequently

**Best Practices:**
- Take notes on decision criteria (when to use X vs Y)
- Build mental models of service relationships
- Practice explaining concepts (teach to learn)
- Complete all "Extra Credit" sections in labs

**Study Rhythm:**
- 5-7 hours per week = 10-12 weeks total
- 10-12 hours per week = 6-8 weeks total
- Mix theory (30%) and hands-on (70%)

**When to Use:**
- Most learners (recommended path)
- Career development, not just exam
- Want strong practical skills
- Time for 2-3 months study

---

### Path C: Complete Tips

**Maximize Mastery:**
1. **Read all documentation links** in labs
2. **Compare services hands-on** (deploy same app to VM, App Service, ACI, AKS)
3. **Build reference architectures** for common scenarios
4. **Contribute improvements** to labs (great learning)
5. **Teach others** - help on forums/communities

**Architecture Focus:**
- Create decision trees for service selection
- Understand cost implications deeply
- Learn operational differences (scaling, monitoring, etc.)
- Study real customer case studies

**Capstone Project Ideas:**
1. **E-commerce Platform:** Frontend (Static Web App) + Backend (Functions) + Data (Cosmos) + Queue (Service Bus) + Cache (Redis) + Monitoring (App Insights)

2. **IoT Data Pipeline:** Ingestion (Event Hubs) + Processing (Functions) + Storage (Blob/Cosmos) + API (APIM) + Dashboard (App Service)

3. **Multi-tenant SaaS:** Containers (ACI/AKS) + Identity (Entra ID) + Secrets (Key Vault) + Data (Cosmos) + CDN (Front Door)

**When to Use:**
- Career change to cloud
- Want architect-level understanding
- Building commercial applications
- 3-4 months available

---

### General Tips (All Paths)

**Lab Execution:**
```bash
# Always prefix resources with your initials to avoid conflicts
export PREFIX="js"  # Your initials
export LOCATION="eastus"
export RG="${PREFIX}-az204-rg"

# Create naming convention
# Pattern: {prefix}-{service}-{environment}
# Example: js-app-dev, js-cosmos-prod
```

**Cost Management:**
```bash
# Always clean up after labs
az group delete --name $RG --yes --no-wait

# Set up billing alerts
# In Azure Portal: Cost Management > Budgets > Create

# Use consumption/basic tiers
# Functions: Consumption Plan
# App Service: B1 (Basic)
# Cosmos: Serverless or 400 RU/s
```

**Troubleshooting:**
1. Check `hints.md` files first
2. Review `solution.md` if still stuck
3. Use `az <command> --help` liberally
4. Check Azure Activity Log in portal
5. Search error messages on Microsoft Learn

**SDK Learning:**
```csharp
// Always practice with SDKs, not just CLI
// Example: Blob storage with .NET
var blobClient = new BlobClient(connectionString, containerName, blobName);
await blobClient.UploadAsync(stream);
```

**Exam Preparation:**
- Complete practice exams weekly
- Review incorrect answers thoroughly
- Focus on "why" not just "what"
- Understand pricing models
- Know service limits

**Study Groups:**
- Join Azure Discord/Slack communities
- Weekly study sessions with peers
- Share lab solutions and discuss
- Teach concepts to each other

**Resource Cleanup Checklist:**
```bash
# After each session, verify cleanup
az group list --output table
az resource list --output table

# Delete any lingering resources
az group delete --name {resource-group-name} --yes --no-wait
```

---

## Time Estimates by Experience Level

### Beginners (New to Azure/Cloud)
- **Path A:** 50-60 hours (not recommended - try Path B)
- **Path B:** 70-80 hours (recommended)
- **Path C:** 100-120 hours

**Adjust for:**
- New to programming: +20%
- New to CLI: +15%
- First certification: +10%

### Intermediate (Some Azure Experience)
- **Path A:** 40-50 hours (good choice)
- **Path B:** 60-70 hours (recommended)
- **Path C:** 80-90 hours

**Adjust for:**
- Used Azure for 3-6 months: -10%
- Strong programming background: -15%

### Advanced (Daily Azure Use)
- **Path A:** 35-45 hours (recommended)
- **Path B:** 50-60 hours (for depth)
- **Path C:** 70-80 hours

**Adjust for:**
- Azure dev for 1+ year: -20%
- Other cloud certs: -15%

---

## Frequently Asked Questions

**Q: Can I skip labs I already know?**
A: Yes for Path A/B. But review the AZ-204.md file - it has exam-specific exercises.

**Q: Should I do labs in order?**
A: Follow the phase order, but within a phase you can adapt based on dependencies.

**Q: What if I don't have time for full path?**
A: Minimum viable: Foundation + Compute + Storage + Security + Messaging = ~30 hours

**Q: Do I need all three programming languages?**
A: No, one is sufficient. .NET is most common in labs, but Python works too.

**Q: How much will the labs cost?**
A: $20-50 total if you delete resources immediately. Use free tier when possible.

**Q: When should I take the exam?**
A: When you score 85%+ consistently on practice exams.

**Q: What if I fail the exam?**
A: Review weak areas from exam feedback. Redo relevant labs. Retake available after 24 hours.

**Q: Can I do multiple paths?**
A: Yes! Start with Path A, extend to B or C as needed.

---

## Path Decision Flowchart

```
                    ┌──────────────────────┐
                    │ Do you have Azure    │
                    │ experience (6+ mo)?  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
              YES                            NO
                │                             │
                ▼                             ▼
    ┌──────────────────────┐      ┌──────────────────────┐
    │ Just need the cert?  │      │ Career change or     │
    │ (exam only)          │      │ new to cloud?        │
    └──────────┬───────────┘      └──────────┬───────────┘
               │                              │
        ┌──────┴──────┐                       │
      YES            NO                      YES
        │              │                       │
        ▼              ▼                       ▼
   ┌────────┐    ┌─────────┐         ┌────────────┐
   │PATH A  │    │PATH B   │         │  PATH C    │
   │Fast    │    │Compre-  │         │  Complete  │
   │Track   │    │hensive  │         │            │
   └────────┘    └─────────┘         └────────────┘
   40-50 hrs     60-70 hrs            80-100 hrs
```

---

## Success Metrics

### After Path A:
- [ ] Can deploy production apps to Azure
- [ ] Understand all AZ-204 exam domains
- [ ] Score 85%+ on practice exams
- [ ] Built 2-3 functional projects
- **Expected Exam Score:** 750-850 (pass = 700)

### After Path B:
- [ ] Can design Azure solutions
- [ ] Explain service trade-offs
- [ ] Score 90%+ on practice exams
- [ ] Built 5+ integrated projects
- **Expected Exam Score:** 800-900

### After Path C:
- [ ] Can architect complex Azure solutions
- [ ] Deep understanding of all services
- [ ] Score 95%+ on practice exams
- [ ] Built comprehensive portfolio
- **Expected Exam Score:** 850-950

---

## Final Recommendations

**For most learners: Start with Path B**
- Best balance of efficiency and depth
- Strong practical skills
- High exam pass rate
- Career-ready knowledge

**Upgrade/Downgrade as needed:**
- Struggling with fundamentals? → Add Path C foundation content
- Ahead of schedule? → Add Path B supplementary labs
- Time running out? → Focus on Path A essentials

**Remember:**
- Hands-on practice beats reading
- Understanding "why" matters more than memorizing "what"
- Real projects solidify learning
- Community helps (study groups, forums)
- Consistency beats intensity

---

## Next Steps

1. **Choose your path** based on experience and goals
2. **Set up prerequisites** (Azure account, CLI, tools)
3. **Block calendar time** for labs (consistency is key)
4. **Join study community** for support
5. **Start with Phase 1** - foundation labs
6. **Track progress** through checkpoints
7. **Adjust as needed** - paths are flexible
8. **Schedule exam** when scoring 85%+ on practice tests

---

**Good luck on your AZ-204 journey!**

For detailed curriculum information, see [AZ-204-CURRICULUM.md](AZ-204-CURRICULUM.md)

For week-by-week study schedules, see [AZ-204-STUDY-GUIDE.md](AZ-204-STUDY-GUIDE.md) (if available)

For lab details, see [labs/README.md](labs/README.md) or individual lab directories

---

*Last Updated: November 2025*
*Paths designed for AZ-204 exam version: July 2025*
