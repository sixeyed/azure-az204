# AZ-204 Azure Developer Associate - Lab Index

## Introduction

Welcome to the comprehensive AZ-204 exam preparation lab suite! This repository contains **65 hands-on labs** designed to help you master Azure development and pass the Microsoft AZ-204 certification exam.

### Repository Structure

Each lab directory contains two key documentation files:

- **README.md**: Step-by-step instructions for completing the lab
  - Includes setup instructions, commands, and troubleshooting
  - Suitable for hands-on practice and learning
  - Contains detailed explanations and context

- **AZ-204.md**: Exam-focused reference guide (when applicable)
  - Maps lab concepts to specific AZ-204 exam objectives
  - Highlights key facts, commands, and patterns likely to appear on the exam
  - Provides quick revision notes for exam preparation
  - **Available for 23 core labs** (marked with ✓ in tables below)

### Lab Categories

Labs are organized into three categories:

1. **Core Labs** (37 labs): Essential for AZ-204 exam preparation - you MUST complete these
2. **Supplementary Labs** (12 labs): Valuable Azure skills that enhance your knowledge but aren't exam-critical
3. **Out of Scope** (16 labs): Advanced topics (Kubernetes, IaaS) useful for broader Azure learning but not required for AZ-204

### Time Investment

- **Fast Track** (Core labs only): ~40 hours
- **Comprehensive** (Core + Selected supplementary): ~60 hours
- **Complete** (All labs): ~80+ hours

---

## Quick Reference Table

### Domain 1: Develop Azure Compute Solutions (20-25% of exam)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [signin](/home/user/azure-az204/labs/signin) | Foundation | No | 30m | Beginner | Azure authentication, subscriptions |
| [resourcegroups](/home/user/azure-az204/labs/resourcegroups) | Foundation | No | 30m | Beginner | Resource group management |
| [docker](/home/user/azure-az204/labs/docker) | Core | No | 60m | Beginner | Docker fundamentals, containers |
| [docker-build](/home/user/azure-az204/labs/docker-build) | Core | No | 60m | Intermediate | Multi-stage builds, optimization |
| [docker-compose](/home/user/azure-az204/labs/docker-compose) | Core | No | 60m | Intermediate | Multi-container apps |
| [acr](/home/user/azure-az204/labs/acr) | Core | ✓ | 60m | Intermediate | Container registry, image management |
| [aci](/home/user/azure-az204/labs/aci) | Core | ✓ | 60m | Intermediate | Azure Container Instances |
| [aci-compose](/home/user/azure-az204/labs/aci-compose) | Core | No | 90m | Advanced | Multi-container ACI, storage integration |
| [appservice](/home/user/azure-az204/labs/appservice) | Core | ✓ | 60m | Beginner | Web app deployment, Git integration |
| [appservice-api](/home/user/azure-az204/labs/appservice-api) | Core | No | 75m | Intermediate | REST APIs, distributed apps |
| [appservice-config](/home/user/azure-az204/labs/appservice-config) | Core | ✓ | 75m | Intermediate | Health checks, auto-heal, scaling |
| [appservice-cicd](/home/user/azure-az204/labs/appservice-cicd) | Core | ✓ | 90m | Advanced | CI/CD pipelines, deployment slots |
| [appservice-static](/home/user/azure-az204/labs/appservice-static) | Core | No | 60m | Beginner | Static Web Apps, GitHub integration |
| [functions/http](/home/user/azure-az204/labs/functions/http) | Core | ✓ | 60m | Beginner | HTTP triggers, serverless compute |
| [functions/blob](/home/user/azure-az204/labs/functions/blob) | Core | ✓ | 75m | Intermediate | Blob storage triggers |
| [functions/cosmos](/home/user/azure-az204/labs/functions/cosmos) | Core | No | 75m | Intermediate | Cosmos DB bindings |
| [functions/servicebus](/home/user/azure-az204/labs/functions/servicebus) | Core | No | 75m | Intermediate | Service Bus triggers |
| [functions/signalr](/home/user/azure-az204/labs/functions/signalr) | Core | No | 90m | Advanced | SignalR integration |
| [functions/timer](/home/user/azure-az204/labs/functions/timer) | Core | ✓ | 60m | Beginner | Timer triggers, scheduling |
| [functions/cicd](/home/user/azure-az204/labs/functions/cicd) | Core | No | 90m | Advanced | Functions CI/CD |
| [functions/rabbitmq](/home/user/azure-az204/labs/functions/rabbitmq) | Core | No | 75m | Intermediate | RabbitMQ bindings |
| [functions-durable/chained](/home/user/azure-az204/labs/functions-durable/chained) | Core | ✓ | 90m | Advanced | Function chaining patterns |
| [functions-durable/fan-out](/home/user/azure-az204/labs/functions-durable/fan-out) | Core | ✓ | 90m | Advanced | Fan-out/fan-in orchestration |
| [functions-durable/human](/home/user/azure-az204/labs/functions-durable/human) | Core | ✓ | 90m | Advanced | Human interaction patterns |

**Compute Total: 24 labs | Core: 22 | Foundation: 2 | Est. Time: ~28 hours**

### Domain 2: Develop for Azure Storage (15-20% of exam)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [storage](/home/user/azure-az204/labs/storage) | Core | ✓ | 60m | Beginner | Storage accounts, redundancy options |
| [storage-blob](/home/user/azure-az204/labs/storage-blob) | Core | ✓ | 75m | Intermediate | Blob containers, SAS tokens, access tiers |
| [storage-static](/home/user/azure-az204/labs/storage-static) | Core | No | 60m | Beginner | Static website hosting, CDN |
| [storage-files](/home/user/azure-az204/labs/storage-files) | Core | ✓ | 60m | Intermediate | File shares, SMB protocol |
| [storage-table](/home/user/azure-az204/labs/storage-table) | Core | ✓ | 75m | Intermediate | NoSQL table storage, OData queries |
| [cosmos](/home/user/azure-az204/labs/cosmos) | Core | ✓ | 90m | Intermediate | Cosmos DB NoSQL API, EF Core |
| [cosmos-mongo](/home/user/azure-az204/labs/cosmos-mongo) | Core | No | 75m | Intermediate | MongoDB API compatibility |
| [cosmos-perf](/home/user/azure-az204/labs/cosmos-perf) | Core | No | 90m | Advanced | Performance tuning, RU/s optimization |
| [cosmos-table](/home/user/azure-az204/labs/cosmos-table) | Core | No | 75m | Intermediate | Table API, migration from Table Storage |
| [redis](/home/user/azure-az204/labs/redis) | Core | ✓ | 75m | Intermediate | Azure Cache for Redis, caching patterns |
| [sql](/home/user/azure-az204/labs/sql) | Supplementary | No | 60m | Intermediate | Azure SQL Database |
| [sql-schema](/home/user/azure-az204/labs/sql-schema) | Supplementary | No | 60m | Intermediate | SQL schema management |

**Storage Total: 12 labs | Core: 10 | Supplementary: 2 | Est. Time: ~14 hours**

### Domain 3: Implement Azure Security (20-25% of exam)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [keyvault](/home/user/azure-az204/labs/keyvault) | Core | ✓ | 60m | Intermediate | Key Vault basics, secrets, certificates |
| [keyvault-access](/home/user/azure-az204/labs/keyvault-access) | Core | No | 75m | Advanced | Access policies, managed identities |
| [vnet](/home/user/azure-az204/labs/vnet) | Core | No | 60m | Intermediate | Virtual Networks, subnets |
| [vnet-access](/home/user/azure-az204/labs/vnet-access) | Core | No | 75m | Advanced | Network access control, NSGs |
| [vnet-apps](/home/user/azure-az204/labs/vnet-apps) | Core | No | 90m | Advanced | Key Vault + VNet + Managed Identity |

**Security Total: 5 labs | Core: 5 | Est. Time: ~6 hours**

### Domain 4: Monitor, Troubleshoot, and Optimize (15-20% of exam)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [applicationinsights](/home/user/azure-az204/labs/applicationinsights) | Core | ✓ | 75m | Intermediate | Application Insights, instrumentation |
| [loganalytics](/home/user/azure-az204/labs/loganalytics) | Core | No | 75m | Intermediate | Log Analytics, KQL queries |

**Monitoring Total: 2 labs | Core: 2 | Est. Time: ~2.5 hours**

### Domain 5: Connect to and Consume Azure Services (15-20% of exam)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [servicebus](/home/user/azure-az204/labs/servicebus) | Core | ✓ | 75m | Intermediate | Service Bus queues, message patterns |
| [servicebus-pubsub](/home/user/azure-az204/labs/servicebus-pubsub) | Core | No | 90m | Advanced | Pub-Sub with topics and subscriptions |
| [eventhubs](/home/user/azure-az204/labs/eventhubs) | Core | ✓ | 75m | Intermediate | Event Hubs, partitions, throughput units |
| [eventhubs-consumers](/home/user/azure-az204/labs/eventhubs-consumers) | Core | No | 90m | Advanced | Event Hubs consumers, checkpointing |
| [apim](/home/user/azure-az204/labs/apim) | Core | ✓ | 75m | Intermediate | API Management basics, gateway, policies |
| [apim-mock](/home/user/azure-az204/labs/apim-mock) | Core | No | 60m | Intermediate | API mocking, design-first approach |
| [apim-policies](/home/user/azure-az204/labs/apim-policies) | Core | No | 75m | Advanced | Request/response policies |
| [apim-versioning](/home/user/azure-az204/labs/apim-versioning) | Core | No | 75m | Advanced | API versioning, changelog management |
| [signalr](/home/user/azure-az204/labs/signalr) | Core | No | 75m | Intermediate | Azure SignalR Service, WebSockets |

**Services Total: 9 labs | Core: 9 | Est. Time: ~11 hours**

### Supplementary Labs (Valuable but not exam-critical)

| Lab | Type | AZ-204.md | Time | Difficulty | Key Topics |
|-----|------|-----------|------|------------|------------|
| [arm](/home/user/azure-az204/labs/arm) | Supplementary | No | 75m | Intermediate | ARM JSON templates |
| [arm-bicep](/home/user/azure-az204/labs/arm-bicep) | Supplementary | No | 75m | Intermediate | Bicep templates (ARM successor) |
| [appgw](/home/user/azure-az204/labs/appgw) | Supplementary | No | 90m | Advanced | Application Gateway, WAF, layer 7 LB |
| [frontdoor](/home/user/azure-az204/labs/frontdoor) | Supplementary | No | 90m | Advanced | Azure Front Door, CDN, DDoS |

**Supplementary Total: 4 additional labs | Est. Time: ~5.5 hours**

### Out of Scope Labs (Useful for broader Azure knowledge)

#### Kubernetes (AKS) Labs

| Lab | Time | Difficulty | Key Topics |
|-----|------|------------|------------|
| [kubernetes](/home/user/azure-az204/labs/kubernetes) | 90m | Advanced | Kubernetes basics (platform-agnostic) |
| [aks](/home/user/azure-az204/labs/aks) | 90m | Advanced | Azure Kubernetes Service |
| [aks-apps](/home/user/azure-az204/labs/aks-apps) | 90m | Advanced | Deploying apps on AKS |
| [aks-ingress](/home/user/azure-az204/labs/aks-ingress) | 90m | Advanced | Kubernetes Ingress controllers |
| [aks-keyvault](/home/user/azure-az204/labs/aks-keyvault) | 90m | Advanced | Key Vault integration with AKS |
| [aks-persistentvolumes](/home/user/azure-az204/labs/aks-persistentvolumes) | 90m | Advanced | Storage in Kubernetes |

**AKS Total: 6 labs | Est. Time: ~9 hours**

#### Virtual Machines (IaaS) Labs

| Lab | Time | Difficulty | Key Topics |
|-----|------|------------|------------|
| [vm](/home/user/azure-az204/labs/vm) | 60m | Beginner | Virtual Machines basics |
| [vm-config](/home/user/azure-az204/labs/vm-config) | 75m | Intermediate | VM configuration |
| [vm-image](/home/user/azure-az204/labs/vm-image) | 90m | Advanced | Custom VM images |
| [vm-web](/home/user/azure-az204/labs/vm-web) | 75m | Intermediate | Web applications on VMs |
| [vm-win](/home/user/azure-az204/labs/vm-win) | 75m | Intermediate | Windows VMs |
| [vmss-linux](/home/user/azure-az204/labs/vmss-linux) | 90m | Advanced | Linux VM Scale Sets |
| [vmss-win](/home/user/azure-az204/labs/vmss-win) | 90m | Advanced | Windows VM Scale Sets |
| [sql-vm](/home/user/azure-az204/labs/sql-vm) | 75m | Intermediate | SQL Server on VMs |
| [iaas-apps](/home/user/azure-az204/labs/iaas-apps) | 90m | Advanced | Application deployment on IaaS |
| [iaas-bicep](/home/user/azure-az204/labs/iaas-bicep) | 90m | Advanced | IaaS infrastructure with Bicep |

**IaaS Total: 10 labs | Est. Time: ~13 hours**

---

## Labs Organized by Domain

### Domain 1: Develop Azure Compute Solutions (20-25% of exam)

This domain covers deploying and managing compute resources in Azure, including web apps, serverless functions, and containers.

#### 1.1 Azure App Service (5 labs)

Deploy and manage web applications with built-in CI/CD, scaling, and monitoring.

1. **appservice** - Basic web app deployment with Git integration
2. **appservice-api** - REST APIs and distributed application configuration
3. **appservice-config** - Health checks, auto-heal rules, and scaling strategies
4. **appservice-cicd** - GitHub Actions CI/CD pipelines and deployment slots
5. **appservice-static** - Static Web Apps with serverless backend APIs

#### 1.2 Azure Functions (11 labs)

Master serverless computing with event-driven functions and various trigger types.

**Basic Triggers:**
1. **functions/http** - HTTP triggers and REST API development
2. **functions/timer** - Scheduled functions with CRON expressions
3. **functions/blob** - Blob storage triggers for file processing

**Integration Triggers:**
4. **functions/cosmos** - Cosmos DB input/output bindings
5. **functions/servicebus** - Service Bus queue and topic triggers
6. **functions/signalr** - Real-time communication with SignalR
7. **functions/rabbitmq** - RabbitMQ message queue integration

**Advanced Patterns:**
8. **functions/cicd** - Automated deployment pipelines for Functions
9. **functions-durable/chained** - Sequential function chaining patterns
10. **functions-durable/fan-out** - Parallel execution and aggregation
11. **functions-durable/human** - Human approval and long-running workflows

#### 1.3 Container Services (6 labs)

Build, deploy, and manage containerized applications on Azure.

**Docker Fundamentals:**
1. **docker** - Docker basics: images, containers, networking
2. **docker-build** - Multi-stage builds for optimized images
3. **docker-compose** - Multi-container local development

**Azure Container Services:**
4. **acr** - Azure Container Registry for image management
5. **aci** - Single-container deployment with Azure Container Instances
6. **aci-compose** - Multi-container groups with persistent storage

---

### Domain 2: Develop for Azure Storage (15-20% of exam)

Master Azure storage services for blobs, files, tables, and NoSQL databases.

#### 2.1 Blob Storage (3 labs)

1. **storage** - Storage account types, redundancy, and access tiers
2. **storage-blob** - Container management, SAS tokens, blob properties
3. **storage-static** - Static website hosting with custom domains and CDN

#### 2.2 Azure Files (1 lab)

1. **storage-files** - File shares, SMB mounting, and cross-platform access

#### 2.3 Table Storage (1 lab)

1. **storage-table** - NoSQL table storage with partition and row keys

#### 2.4 Cosmos DB (4 labs)

1. **cosmos** - Cosmos DB NoSQL API with Entity Framework Core
2. **cosmos-mongo** - MongoDB API for migrating existing apps
3. **cosmos-perf** - Request Units (RU/s), indexing, and query optimization
4. **cosmos-table** - Table API for migrating from Azure Table Storage

#### 2.5 Caching (1 lab)

1. **redis** - Azure Cache for Redis with cache-aside and write-through patterns

---

### Domain 3: Implement Azure Security (20-25% of exam)

Implement secure solutions using Key Vault, managed identities, and network security.

#### 3.1 Key Vault (2 labs)

1. **keyvault** - Secrets, keys, and certificate management
2. **keyvault-access** - Access policies, RBAC, and managed identities

#### 3.2 Network Security (3 labs)

1. **vnet** - Virtual Network fundamentals and subnet configuration
2. **vnet-access** - Network Security Groups (NSGs) and access control
3. **vnet-apps** - Integrated security with Key Vault, VNets, and Managed Identity

---

### Domain 4: Monitor, Troubleshoot, and Optimize (15-20% of exam)

Monitor application performance and troubleshoot issues using Azure monitoring tools.

#### 4.1 Application Monitoring (2 labs)

1. **applicationinsights** - Application Insights SDK, telemetry, and alerts
2. **loganalytics** - Log Analytics workspaces and KQL (Kusto Query Language)

---

### Domain 5: Connect to and Consume Azure Services (15-20% of exam)

Integrate applications with messaging services, event processing, and API management.

#### 5.1 Messaging Services (2 labs)

1. **servicebus** - Service Bus queues with FIFO and dead-letter patterns
2. **servicebus-pubsub** - Topics, subscriptions, and message filtering

#### 5.2 Event Processing (2 labs)

1. **eventhubs** - Event Hubs fundamentals, partitions, and consumer groups
2. **eventhubs-consumers** - Event processing with checkpointing

#### 5.3 API Management (4 labs)

1. **apim** - API Management gateway, products, and subscriptions
2. **apim-mock** - Mock APIs for frontend development
3. **apim-policies** - Transformation, throttling, and security policies
4. **apim-versioning** - API versioning strategies and version management

#### 5.4 Real-Time Communication (1 lab)

1. **signalr** - Azure SignalR Service for WebSocket communication

---

## Recommended Learning Paths

### Path 1: Fast Track (Core Labs Only) - ~40 hours

**For students with limited time who need to focus only on exam-essential content.**

This path includes the 37 core labs that directly map to AZ-204 exam objectives.

#### Week 1-2: Foundations & Compute (14 hours)
- signin, resourcegroups (1 hour)
- docker, docker-build, docker-compose (3 hours)
- acr, aci (2 hours)
- appservice, appservice-api, appservice-config (3.5 hours)
- functions/http, functions/timer, functions/blob (3.25 hours)

#### Week 3: Storage (10 hours)
- storage, storage-blob, storage-static (3.25 hours)
- storage-files, storage-table (2.25 hours)
- cosmos, cosmos-mongo, cosmos-table (4 hours)
- redis (1.25 hours)

#### Week 4: Advanced Compute & Functions (8 hours)
- functions/cosmos, functions/servicebus, functions/rabbitmq (3.75 hours)
- appservice-cicd, functions/cicd (3 hours)
- aci-compose (1.5 hours)

#### Week 5: Integration & Services (8 hours)
- servicebus, servicebus-pubsub (2.75 hours)
- eventhubs, eventhubs-consumers (2.75 hours)
- signalr, functions/signalr (2.75 hours)

#### Week 6: Security, Monitoring & API Management (10 hours)
- keyvault, keyvault-access (2.25 hours)
- vnet, vnet-access, vnet-apps (3.75 hours)
- applicationinsights, loganalytics (2.5 hours)
- apim, apim-mock, apim-policies, apim-versioning (4.75 hours)

#### Week 7: Advanced Functions & Review (6 hours)
- functions-durable/chained, functions-durable/fan-out, functions-durable/human (4.5 hours)
- cosmos-perf, appservice-static (2.5 hours)

**Total: 37 core labs | ~40 hours**

---

### Path 2: Comprehensive (Core + Selected Supplementary) - ~60 hours

**For students who want strong exam preparation plus practical Azure skills.**

Includes all 37 core labs plus 8 supplementary labs for Infrastructure as Code and advanced networking.

**Weeks 1-7:** Complete Fast Track path (40 hours)

#### Week 8-9: Supplementary Skills (10 hours)
- arm, arm-bicep (2.5 hours) - Infrastructure as Code fundamentals
- sql, sql-schema (2 hours) - Azure SQL Database
- appgw (1.5 hours) - Application Gateway and WAF
- frontdoor (1.5 hours) - Global load balancing and CDN

#### Week 10: Practice & Review (10 hours)
- Re-do challenging labs
- Review AZ-204.md files for all 23 core labs with exam guides
- Practice KQL queries, ARM/Bicep templates
- Mock exam scenarios

**Total: 45 labs | ~60 hours**

---

### Path 3: Complete (All Labs) - ~80+ hours

**For students preparing for AZ-204 AND broader Azure roles (DevOps, Solutions Architect).**

Includes all 65 labs for comprehensive Azure mastery.

**Weeks 1-10:** Complete Comprehensive path (60 hours)

#### Week 11-12: Kubernetes & AKS (9 hours)
- kubernetes, aks, aks-apps (4.5 hours)
- aks-ingress, aks-keyvault, aks-persistentvolumes (4.5 hours)

#### Week 13-14: Virtual Machines & IaaS (13 hours)
- vm, vm-config, vm-web, vm-win (4.75 hours)
- vmss-linux, vmss-win, sql-vm (4.25 hours)
- iaas-apps, iaas-bicep (3 hours)

#### Week 15: Integration & Mastery (8 hours)
- Build end-to-end solutions combining multiple services
- Deploy microservices architectures
- Implement hybrid cloud scenarios
- Practice advanced troubleshooting

**Total: 65 labs | ~80+ hours**

---

## Lab Difficulty Progression

### Beginner Labs (Start Here!)

These labs introduce fundamental concepts with step-by-step guidance.

**Time: 30-60 minutes each**

1. **signin** - Azure authentication and subscriptions
2. **resourcegroups** - Resource organization basics
3. **docker** - Container fundamentals
4. **appservice** - Deploy your first web app
5. **appservice-static** - Static website hosting
6. **functions/http** - First serverless function
7. **functions/timer** - Scheduled functions
8. **storage** - Storage account basics
9. **storage-static** - Static website on blob storage
10. **vm** - Virtual machine basics (out of scope for AZ-204)

**Key Skills:** Azure CLI basics, portal navigation, basic deployments

---

### Intermediate Labs (Build Your Skills)

These labs require foundational knowledge and introduce more complex scenarios.

**Time: 60-90 minutes each**

**Compute:**
- docker-build, docker-compose
- acr, aci
- appservice-api, appservice-config
- functions/blob, functions/cosmos, functions/servicebus, functions/rabbitmq

**Storage:**
- storage-blob, storage-files, storage-table
- cosmos, cosmos-mongo, cosmos-table
- redis

**Security:**
- keyvault, vnet

**Services:**
- servicebus, eventhubs, apim, apim-mock, signalr

**Monitoring:**
- applicationinsights, loganalytics

**Supplementary:**
- arm, arm-bicep, sql, sql-schema
- vm-config, vm-web, vm-win, sql-vm

**Key Skills:** Service integration, configuration management, basic security patterns

---

### Advanced Labs (Master Azure Development)

These labs involve complex architectures, multiple service integrations, and production patterns.

**Time: 90-120+ minutes each**

**Compute & Orchestration:**
- aci-compose
- appservice-cicd, functions/cicd
- functions/signalr
- functions-durable/chained, functions-durable/fan-out, functions-durable/human

**Storage:**
- cosmos-perf

**Security & Networking:**
- keyvault-access, vnet-access, vnet-apps

**Services:**
- servicebus-pubsub, eventhubs-consumers
- apim-policies, apim-versioning

**Supplementary:**
- appgw, frontdoor

**Out of Scope (Advanced Topics):**
- All AKS labs (kubernetes, aks, aks-apps, aks-ingress, aks-keyvault, aks-persistentvolumes)
- Advanced IaaS (vm-image, vmss-linux, vmss-win, iaas-apps, iaas-bicep)

**Key Skills:** Durable Functions, advanced networking, CI/CD pipelines, production patterns, orchestration

---

## Prerequisites and Dependencies

### Foundation Prerequisites (Complete First)

Before starting any other labs, complete these foundations:

1. **signin** - Required for all labs (Azure authentication)
2. **resourcegroups** - Required for all labs (resource organization)
3. **docker** - Required before: docker-build, docker-compose, acr, aci, aci-compose

### Lab Dependencies

Some labs build on concepts from previous labs. Follow these recommended sequences:

#### Container Workflow
```
docker → docker-build → docker-compose → acr → aci → aci-compose
```

#### App Service Progression
```
appservice → appservice-api → appservice-config → appservice-cicd
appservice → appservice-static
```

#### Functions Progression
```
functions/http → functions/timer → functions/blob
functions/blob → functions/cosmos
functions/http → functions/servicebus → functions-durable/*
```

#### Storage Progression
```
storage → storage-blob → storage-static
storage → storage-files
storage → storage-table → cosmos-table
cosmos → cosmos-mongo → cosmos-perf
```

#### Cosmos DB Track
```
cosmos → cosmos-mongo
cosmos → cosmos-table
cosmos → cosmos-perf (requires cosmos + cosmos-mongo)
```

#### Messaging Progression
```
servicebus → servicebus-pubsub → functions/servicebus
eventhubs → eventhubs-consumers
```

#### API Management Progression
```
apim → apim-mock
apim → apim-policies → apim-versioning
```

#### Security Progression
```
keyvault → keyvault-access
vnet → vnet-access → vnet-apps (also requires keyvault)
```

#### Durable Functions Prerequisites
```
functions/http + functions/timer → functions-durable/chained
functions-durable/chained → functions-durable/fan-out
functions-durable/chained → functions-durable/human
```

#### Kubernetes Progression (Out of Scope)
```
docker → docker-compose → kubernetes → aks → aks-apps
aks-apps → aks-ingress
aks-apps + keyvault → aks-keyvault
aks-apps → aks-persistentvolumes
```

#### IaaS Progression (Out of Scope)
```
vm → vm-config → vm-image
vm → vm-web
vm → vm-win
vm → vmss-linux, vmss-win
sql → sql-vm
```

---

## Service Integration Map

Understanding which labs work together helps you build complex solutions:

### Blob Storage Integration
- **storage-blob** (core) → **functions/blob** (triggers) → **aci-compose** (storage mounting)

### Cosmos DB Integration
- **cosmos** (core) → **functions/cosmos** (bindings) → **cosmos-perf** (optimization)

### Service Bus Integration
- **servicebus** (queues) → **functions/servicebus** (triggers) → **servicebus-pubsub** (pub-sub)

### Key Vault Integration
- **keyvault** (core) → **keyvault-access** (managed identity) → **vnet-apps** (network integration)
- **keyvault** → **aks-keyvault** (Kubernetes secrets)

### Monitoring Integration
- **applicationinsights** integrates with: appservice, functions, aci
- **loganalytics** integrates with: AKS, VMs, all PaaS services

### SignalR Integration
- **signalr** (standalone) → **functions/signalr** (serverless backend)

### API Management Integration
- **apim** fronts: appservice-api, functions/http, aks-apps, aci

### Network Security Integration
- **vnet** (core) → **vnet-access** (NSGs) → **vnet-apps** (private endpoints)

---

## Labs with AZ-204.md Exam Guides

The following **23 labs** include dedicated AZ-204.md files that map lab content to specific exam objectives:

### Compute (9 labs with exam guides)
1. aci
2. acr
3. appservice
4. appservice-cicd
5. appservice-config
6. functions/http
7. functions/blob
8. functions/timer
9. functions-durable (covers chained, fan-out, human)

### Storage (7 labs with exam guides)
10. storage
11. storage-blob
12. storage-files
13. storage-table
14. cosmos
15. redis

### Security (1 lab with exam guide)
16. keyvault

### Monitoring (1 lab with exam guide)
17. applicationinsights

### Services (5 labs with exam guides)
18. servicebus
19. eventhubs
20. apim

### New Labs (3 additional labs with exam guides)
21. eventgrid
22. container-apps
23. microsoft-graph

**Note:** eventgrid, container-apps, and microsoft-graph have AZ-204.md files but may be newer additions. Check their README files for lab status.

---

## Quick Start Guide

### First-Time Setup

1. **Install Prerequisites:**
   ```bash
   # Azure CLI
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

   # Docker (for container labs)
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh

   # .NET SDK (for function labs)
   wget https://dot.net/v1/dotnet-install.sh
   bash dotnet-install.sh
   ```

2. **Authenticate to Azure:**
   ```bash
   cd /home/user/azure-az204/labs/signin
   # Follow README.md instructions
   ```

3. **Create Resource Group:**
   ```bash
   cd /home/user/azure-az204/labs/resourcegroups
   # Follow README.md instructions
   ```

4. **Start with Docker Basics:**
   ```bash
   cd /home/user/azure-az204/labs/docker
   # Follow README.md instructions
   ```

### Recommended Study Strategy

1. **Review AZ-204 Exam Objectives** - Understand what Microsoft expects
2. **Choose Your Learning Path** - Fast Track (40h), Comprehensive (60h), or Complete (80h)
3. **Follow Prerequisites** - Don't skip foundation labs
4. **Hands-On First** - Complete each lab's README.md fully
5. **Exam Focus** - Review AZ-204.md files before exam
6. **Build Projects** - Combine multiple services in custom projects
7. **Practice Troubleshooting** - Break things intentionally and fix them

### Lab Completion Checklist

For each lab:
- [ ] Read the README.md thoroughly
- [ ] Complete all exercises
- [ ] Verify all resources deployed successfully
- [ ] Review the AZ-204.md file (if available)
- [ ] Take notes on key commands and concepts
- [ ] Clean up resources to avoid charges
- [ ] Mark lab as complete in your tracking system

---

## Azure Resource Management

### Cost Management

Most labs use low-cost or free-tier resources, but follow these practices:

1. **Delete Resources After Labs:** Always clean up when finished
   ```bash
   az group delete --name <resource-group-name> --yes --no-wait
   ```

2. **Use Free Tiers:**
   - App Service: F1 (Free tier)
   - Functions: Consumption plan
   - Storage: LRS (Locally Redundant Storage)
   - Cosmos DB: Serverless mode or 400 RU/s minimum

3. **Stop Services When Not In Use:**
   - Pause Azure SQL databases
   - Deallocate VMs
   - Scale down App Service plans

4. **Monitor Costs:**
   ```bash
   az consumption usage list --start-date 2025-11-01 --end-date 2025-11-30
   ```

### Resource Naming Conventions

Use consistent naming to organize your lab resources:

```
<service>-<project>-<env>-<region>-<instance>

Examples:
- app-az204-dev-eastus-001
- func-az204-dev-eastus-001
- st-az204-dev-eastus-001 (storage accounts: lowercase, no hyphens)
- kv-az204-dev-eastus-001
```

---

## Troubleshooting Common Issues

### Azure CLI Issues
```bash
# Update Azure CLI
az upgrade

# Clear cache
az cache purge

# Re-authenticate
az login --use-device-code
```

### Docker Issues
```bash
# Check Docker status
sudo systemctl status docker

# Restart Docker
sudo systemctl restart docker

# Clean up Docker resources
docker system prune -a
```

### Resource Deployment Failures
```bash
# Check deployment status
az deployment group show --name <deployment-name> --resource-group <rg-name>

# View deployment logs
az monitor activity-log list --resource-group <rg-name>

# Check service-specific logs
az webapp log tail --name <app-name> --resource-group <rg-name>
```

### Quota and Limit Issues
```bash
# Check current quotas
az vm list-usage --location eastus --output table

# Request quota increases (use Azure Portal)
```

---

## Additional Resources

### Official Microsoft Documentation
- [AZ-204 Exam Page](https://learn.microsoft.com/en-us/certifications/exams/az-204)
- [AZ-204 Study Guide](https://learn.microsoft.com/en-us/certifications/resources/study-guides/az-204)
- [Azure Documentation](https://learn.microsoft.com/en-us/azure/)
- [Azure Code Samples](https://github.com/Azure-Samples)

### Practice Exams
- Microsoft Learn Practice Assessments
- MeasureUp Practice Tests
- Whizlabs AZ-204 Practice Tests

### Community Resources
- [Azure Developer Community](https://techcommunity.microsoft.com/t5/azure-developer-community/ct-p/AzureDevCommunity)
- [Azure Friday Videos](https://learn.microsoft.com/en-us/shows/azure-friday/)
- [Azure Tips and Tricks](https://microsoft.github.io/AzureTipsAndTricks/)

---

## Curriculum Statistics

### Lab Distribution by Category

| Category | Count | Percentage | Est. Time |
|----------|-------|------------|-----------|
| **Core AZ-204 Labs** | 37 | 57% | ~40 hours |
| **Supplementary Labs** | 12 | 18% | ~12 hours |
| **Out of Scope (K8s/IaaS)** | 16 | 25% | ~22 hours |
| **Total Labs** | 65 | 100% | ~74 hours |

### Lab Distribution by Difficulty

| Difficulty | Count | Percentage |
|------------|-------|------------|
| **Beginner** | 10 | 15% |
| **Intermediate** | 35 | 54% |
| **Advanced** | 20 | 31% |

### Lab Distribution by Domain

| Domain | Core Labs | Percentage | Est. Time |
|--------|-----------|------------|-----------|
| **Domain 1: Compute** | 22 | 59% | ~26 hours |
| **Domain 2: Storage** | 10 | 27% | ~12 hours |
| **Domain 3: Security** | 5 | 14% | ~6 hours |
| **Domain 4: Monitoring** | 2 | 5% | ~2.5 hours |
| **Domain 5: Services** | 9 | 24% | ~11 hours |

### Labs with Exam Guides

| Status | Count | Percentage |
|--------|-------|------------|
| **Has AZ-204.md** | 23 | 35% of all labs |
| **Core labs with AZ-204.md** | 20 | 54% of core labs |
| **No AZ-204.md** | 42 | 65% of all labs |

---

## Changelog

### Version 1.0 (2025-11-05)
- Initial comprehensive lab index
- Organized 65 labs across 5 AZ-204 domains
- Created 3 learning paths (Fast Track, Comprehensive, Complete)
- Added difficulty progression and prerequisites
- Documented 23 labs with AZ-204.md exam guides

---

## Contributing

Found an issue or want to improve a lab? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This lab curriculum is provided as-is for educational purposes to help students prepare for the Microsoft AZ-204 certification exam.

---

**Ready to start? Begin with the [signin lab](/home/user/azure-az204/labs/signin) and [resourcegroups lab](/home/user/azure-az204/labs/resourcegroups) to set up your Azure environment!**

**Good luck with your AZ-204 certification journey! 🚀**
