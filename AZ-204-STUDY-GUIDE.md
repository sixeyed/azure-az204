# AZ-204 Azure Developer Associate - Comprehensive Study Guide

## Welcome to Your AZ-204 Exam Journey!

This study guide provides a structured 8-week plan to prepare for the Microsoft AZ-204: Developing Solutions for Microsoft Azure certification exam. Whether you're new to Azure or have some experience, this guide will help you master the concepts and hands-on skills needed to pass the exam with confidence.

---

## Table of Contents

1. [How to Use This Study Guide](#how-to-use-this-study-guide)
2. [Prerequisites](#prerequisites)
3. [Exam Overview](#exam-overview)
4. [Study Plan Overview](#study-plan-overview)
5. [Week-by-Week Breakdown](#week-by-week-breakdown)
6. [Study Strategies](#study-strategies)
7. [Resource Links](#resource-links)
8. [Final Week Strategy](#final-week-strategy)
9. [Exam Day Tips](#exam-day-tips)
10. [After the Exam](#after-the-exam)

---

## How to Use This Study Guide

### Time Commitment

**Total Estimated Time:** 80-120 hours over 8 weeks

- **Study time per week:** 10-15 hours
- **Hands-on labs:** 60-70% of time
- **Theory & documentation:** 30-40% of time

### Study Approach

1. **Read First:** Start each topic by reading the Microsoft Learn modules and official documentation
2. **Lab Practice:** Complete the hands-on labs in this repository - practice is crucial!
3. **Document:** Take notes on key concepts, CLI commands, and gotchas
4. **Review:** End each week by reviewing notes and completing the self-assessment
5. **Iterate:** If you struggle with a topic, revisit it before moving forward

### Flexibility

This is an 8-week plan, but you can adjust based on your:
- **Background:** Azure experience can reduce time needed
- **Schedule:** Study full-time or part-time
- **Learning style:** Some prefer intensive study, others need more time to absorb

**Key Point:** Quality over speed. Better to take 10 weeks and pass than rush through in 6 weeks and fail.

---

## Prerequisites

### Required Knowledge

- **Programming:** Proficiency in C#, JavaScript, Python, or another language (C# recommended)
- **Web Development:** Understanding of REST APIs, HTTP, JSON
- **Cloud Basics:** Familiarity with cloud computing concepts
- **Command Line:** Comfortable with terminal/command prompt

### Required Setup

Before starting, ensure you have:

1. **Azure Account**
   - Free account: https://azure.microsoft.com/free/
   - Includes $200 credit for 30 days

2. **Development Environment**
   - [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) installed
   - [Docker Desktop](https://www.docker.com/products/docker-desktop) installed
   - [Git](https://git-scm.com/downloads) installed
   - [Visual Studio Code](https://code.visualstudio.com/) (recommended)

3. **VS Code Extensions (Recommended)**
   - Azure Account
   - Azure Functions
   - Azure App Service
   - Azure Storage
   - Docker

4. **Clone This Repository**
   ```bash
   git clone https://github.com/courselabs/azure.git
   cd azure
   ```

### Nice to Have

- GitHub account (for CI/CD labs)
- Basic understanding of .NET or Node.js
- Familiarity with JSON and YAML

---

## Exam Overview

### AZ-204 Exam Structure

**Exam Code:** AZ-204: Developing Solutions for Microsoft Azure

**Format:**
- 40-60 questions
- Multiple choice, multiple response, drag-and-drop, case studies
- 120 minutes (2 hours) + 30 minutes for reading instructions
- Passing score: 700/1000

**Cost:** $165 USD (varies by region)

**Exam Registration:** https://docs.microsoft.com/certifications/exams/az-204

### Exam Domains (Skill Areas)

The AZ-204 exam covers 5 main domains:

| Domain | Weight | Key Topics |
|--------|--------|------------|
| **1. Develop Azure Compute Solutions** | 25-30% | App Service, Azure Functions, Containers (ACI, Container Apps, AKS basics) |
| **2. Develop for Azure Storage** | 15-20% | Blob Storage, Cosmos DB, Azure Cache for Redis |
| **3. Implement Azure Security** | 20-25% | Key Vault, Managed Identities, App Configuration, Secure data |
| **4. Monitor, Troubleshoot, and Optimize** | 15-20% | Application Insights, instrumentation, caching, content delivery |
| **5. Connect to and Consume Azure Services** | 15-20% | API Management, Service Bus, Event Hubs, Event Grid |

### Question Types

1. **Multiple Choice:** Select one correct answer
2. **Multiple Response:** Select all correct answers (2-4 typically)
3. **Drag and Drop:** Order steps or match items
4. **Case Studies:** Multi-question scenarios (3-5 questions per case)
5. **Practical Scenarios:** CLI commands, code snippets to analyze

### Skills Measured

You'll need to demonstrate:
- **Design and implementation** of Azure solutions
- **Security configuration** and identity management
- **Monitoring and troubleshooting** applications
- **Integration** of Azure services
- **Optimization** for performance and cost

---

## Study Plan Overview

### 8-Week Roadmap

```
Week 1: Foundations & Docker Basics
Week 2: Azure App Service Deep Dive
Week 3: Containers & Azure Functions
Week 4: Azure Storage Solutions
Week 5: Messaging & Integration
Week 6: Security & Networking
Week 7: Monitoring & Advanced Topics
Week 8: Review & Exam Preparation
```

### Lab Breakdown by Week

- **Total Core Labs:** 40+ labs
- **Average labs per week:** 5-7 labs
- **Lab time:** 1-3 hours per lab

---

## Week-by-Week Breakdown

---

## Week 1: Foundations & Azure Basics

### Focus Area
Establish foundational knowledge of Azure basics and containerization with Docker.

### Objectives
- Set up Azure environment and authenticate
- Understand resource groups and resource management
- Master Docker fundamentals (essential for container labs)
- Learn basic Azure CLI commands

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Signing In | `/labs/signin/README.md` | 30 min |
| Resource Groups | `/labs/resourcegroups/README.md` | 45 min |
| Docker 101 | `/labs/docker/README.md` | 2 hours |
| Docker Build | `/labs/docker-build/README.md` | 1.5 hours |
| Docker Compose | `/labs/docker-compose/README.md` | 1.5 hours |
| ARM Templates | `/labs/arm/README.md` | 2 hours |
| Bicep Templates | `/labs/arm-bicep/README.md` | 2 hours |

**Total Lab Time:** ~10-11 hours

### Key Concepts to Master

1. **Azure Fundamentals**
   - Azure hierarchy: Management Groups → Subscriptions → Resource Groups → Resources
   - Regions and availability zones
   - Azure Resource Manager (ARM)

2. **Azure CLI**
   - `az login` and authentication
   - `az group create/delete`
   - Common CLI patterns and flags
   - JSON queries with `--query` (JMESPath)

3. **Docker Essentials**
   - Docker images vs containers
   - Dockerfile syntax (FROM, RUN, COPY, CMD, ENTRYPOINT)
   - Multi-stage builds for optimization
   - Docker Compose for multi-container apps
   - Volumes and networking

4. **Infrastructure as Code**
   - ARM template structure (JSON)
   - Bicep syntax (ARM alternative)
   - Parameters and variables
   - Template deployment

### Microsoft Learn Modules

- [Azure Fundamentals](https://docs.microsoft.com/learn/paths/az-900-describe-cloud-concepts/)
- [Manage resources in Azure](https://docs.microsoft.com/learn/paths/manage-resources-in-azure/)
- [Introduction to Docker containers](https://docs.microsoft.com/learn/modules/intro-to-docker-containers/)

### Practice Activities

1. **CLI Practice:**
   ```bash
   # Create and manage resource groups
   az group create -n practice-rg -l eastus
   az group list --output table
   az group delete -n practice-rg --yes
   ```

2. **Docker Practice:**
   - Build a custom Docker image with a simple web app
   - Run containers with port mapping
   - Use Docker Compose to orchestrate a multi-container application

3. **ARM/Bicep Practice:**
   - Create a Bicep file that deploys a storage account
   - Deploy the template and verify resources

### End-of-Week Assessment

**Quiz Questions:**

1. What is the Azure resource hierarchy from top to bottom?
2. What is the difference between `docker run` and `docker exec`?
3. In a Dockerfile, what's the difference between `CMD` and `ENTRYPOINT`?
4. What are the benefits of multi-stage Docker builds?
5. How do you pass parameters to an ARM template deployment?
6. What is the purpose of a Resource Group?
7. Name 3 ways to authenticate with Azure CLI.
8. What is the difference between ARM templates and Bicep?

**Hands-On Challenge:**
Create a Bicep template that deploys a Resource Group and a storage account with specific tags. Deploy it using Azure CLI.

<details>
<summary>View Answers</summary>

1. Management Groups → Subscriptions → Resource Groups → Resources
2. `docker run` creates and starts a new container; `docker exec` runs a command in an existing running container
3. `CMD` provides defaults that can be overridden; `ENTRYPOINT` defines the main executable
4. Smaller final image size, better security (no build tools in production), faster deployments
5. Using `--parameters` flag with `az deployment group create`
6. Logical container to group related resources, shared lifecycle, access control, billing organization
7. Interactive login, service principal, managed identity
8. Bicep is a DSL that transpiles to ARM JSON, more concise and readable

</details>

---

## Week 2: Azure App Service Deep Dive

### Focus Area
Master Azure App Service for web applications, APIs, and deployment strategies.

### Objectives
- Deploy web applications to App Service
- Configure App Service settings and scaling
- Implement CI/CD pipelines
- Deploy static web applications
- Understand deployment slots and traffic routing

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| App Service Basics | `/labs/appservice/README.md` | 2 hours |
| App Service Static | `/labs/appservice-static/README.md` | 1.5 hours |
| App Service APIs | `/labs/appservice-api/README.md` | 2 hours |
| App Service Config | `/labs/appservice-config/README.md` | 2 hours |
| App Service CI/CD | `/labs/appservice-cicd/README.md` | 2.5 hours |

**Total Lab Time:** ~10 hours

### Key Concepts to Master

1. **App Service Plans**
   - Pricing tiers: Free, Shared, Basic, Standard, Premium, Isolated
   - Scaling options: Scale up (vertical) vs Scale out (horizontal)
   - When to use each tier

2. **Deployment Methods**
   - Git deployment (local Git)
   - GitHub Actions
   - Azure DevOps
   - FTP/FTPS
   - ZIP deploy
   - Docker container deployment

3. **Configuration**
   - Application settings (environment variables)
   - Connection strings
   - Path mappings
   - Handler mappings
   - Virtual applications and directories

4. **Deployment Slots**
   - Staging vs production slots
   - Slot settings vs swappable settings
   - Traffic routing and A/B testing
   - Slot swap with preview

5. **Static Web Apps**
   - Jamstack architecture
   - GitHub integration
   - API routes
   - Custom domains and SSL

6. **Health and Monitoring**
   - Health check endpoints
   - Auto-heal rules
   - Diagnostic logs
   - Application Insights integration

### Microsoft Learn Modules

- [Deploy a website to Azure with Azure App Service](https://docs.microsoft.com/learn/paths/deploy-a-website-with-azure-app-service/)
- [Secure your cloud data](https://docs.microsoft.com/learn/paths/secure-your-cloud-data/)
- [Stage a web app deployment for testing and rollback](https://docs.microsoft.com/learn/modules/stage-deploy-app-service-deployment-slots/)

### Practice Activities

1. **Deploy a Sample App:**
   - Use `az webapp up` for quick deployment
   - Configure custom app settings
   - Enable diagnostic logging

2. **CI/CD Pipeline:**
   - Set up GitHub Actions workflow
   - Configure deployment slots
   - Implement blue-green deployment

3. **Static Web App:**
   - Deploy a React/Vue/Angular app
   - Configure API routes
   - Set up custom domain

### End-of-Week Assessment

**Quiz Questions:**

1. What's the difference between "scale up" and "scale out"?
2. Which App Service settings are "sticky" to a slot by default?
3. How do you configure environment variables in App Service?
4. What is the benefit of using deployment slots?
5. Can you host multiple apps in a single App Service Plan?
6. What deployment methods support zero-downtime deployments?
7. How does Static Web Apps differ from regular App Service?
8. What happens during a slot swap operation?

**Hands-On Challenge:**
Deploy a web API to App Service with:
- Production slot with v1 of the app
- Staging slot with v2 of the app
- 10% traffic to staging for canary testing
- Auto-scaling rule based on CPU usage

<details>
<summary>View Answers</summary>

1. Scale up = upgrade to larger VM size; Scale out = add more VM instances
2. None by default - you must explicitly mark settings as slot-specific
3. Configuration → Application settings in portal, or `az webapp config appsettings set`
4. Zero-downtime deployments, test in production-like environment, quick rollback
5. Yes, all apps share the same compute resources
6. Slot swaps, blue-green deployments, rolling deployments
7. Static Web Apps are optimized for static content with API routes, includes built-in authentication
8. VIPs are swapped, connection strings and slot-specific settings remain in place

</details>

---

## Week 3: Containers & Azure Functions

### Focus Area
Deep dive into container services and serverless computing with Azure Functions.

### Objectives
- Build and push container images to Azure Container Registry
- Deploy containers to Azure Container Instances
- Master Azure Container Apps
- Create and trigger Azure Functions
- Understand function bindings and triggers

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Azure Container Registry | `/labs/acr/README.md` | 1.5 hours |
| Azure Container Instances | `/labs/aci/README.md` | 1.5 hours |
| ACI with Compose | `/labs/aci-compose/README.md` | 2 hours |
| Container Apps | `/labs/container-apps/README.md` | 2 hours |
| Functions HTTP Trigger | `/labs/functions/http/README.md` | 1.5 hours |
| Functions Timer Trigger | `/labs/functions/timer/README.md` | 1.5 hours |
| Functions Blob Trigger | `/labs/functions/blob/README.md` | 2 hours |

**Total Lab Time:** ~12 hours

### Key Concepts to Master

1. **Azure Container Registry (ACR)**
   - Push/pull Docker images
   - ACR tasks for automated builds
   - Geo-replication
   - Webhooks and security scanning

2. **Azure Container Instances (ACI)**
   - Single container deployment
   - Container groups (multi-container pods)
   - Volume mounts (Azure Files, secrets)
   - Networking and DNS
   - Restart policies

3. **Azure Container Apps**
   - Environment and container app concepts
   - Ingress configuration
   - Scaling rules (HTTP, CPU, custom)
   - Revisions and traffic splitting
   - Dapr integration
   - Scale-to-zero capability

4. **Azure Functions Core Concepts**
   - Hosting plans: Consumption, Premium, Dedicated
   - Triggers (HTTP, Timer, Blob, Queue, etc.)
   - Input and output bindings
   - Function.json structure
   - Durable Functions (introduction)

5. **Function Triggers**
   - HTTP trigger: REST APIs, webhooks
   - Timer trigger: CRON expressions, scheduled tasks
   - Blob trigger: Process uploaded files
   - Queue trigger: Process messages asynchronously

### Microsoft Learn Modules

- [Deploy and run a containerized web app with Azure App Service](https://docs.microsoft.com/learn/modules/deploy-run-container-app-service/)
- [Build and store container images with Azure Container Registry](https://docs.microsoft.com/learn/modules/build-and-store-container-images/)
- [Run container images in Azure Container Instances](https://docs.microsoft.com/learn/modules/run-docker-with-azure-container-instances/)
- [Create serverless applications](https://docs.microsoft.com/learn/paths/create-serverless-applications/)

### Practice Activities

1. **ACR Practice:**
   ```bash
   # Build and push an image
   az acr build --registry myacr --image myapp:v1 .

   # Run ACR task
   az acr task create --registry myacr --name buildtask \
     --image myapp:{{.Run.ID}} \
     --context https://github.com/user/repo.git \
     --file Dockerfile \
     --commit-trigger-enabled true
   ```

2. **Container Apps Practice:**
   - Deploy a simple API
   - Configure auto-scaling
   - Test traffic splitting between revisions

3. **Functions Practice:**
   - Create an HTTP-triggered function
   - Create a timer-triggered function that runs every 5 minutes
   - Create a blob-triggered function that processes uploaded images

### End-of-Week Assessment

**Quiz Questions:**

1. What's the difference between ACI and Container Apps?
2. When should you use ACR vs Docker Hub?
3. What are the three Azure Functions hosting plans?
4. What is a function binding vs a trigger?
5. How do you scale Container Apps to zero?
6. What is a container group in ACI?
7. Can Azure Functions run on a schedule? How?
8. What is the purpose of Container Apps revisions?

**Hands-On Challenge:**
Create a complete workflow:
1. Build a Docker image with a REST API
2. Push to ACR
3. Deploy to Container Apps with auto-scaling
4. Create an HTTP-triggered function that calls your API
5. Test the complete flow

<details>
<summary>View Answers</summary>

1. ACI is for simple single/multi-container deployments; Container Apps offer auto-scaling, revisions, ingress, and better microservices support
2. ACR when you need private registry, Azure integration, geo-replication, security scanning
3. Consumption (pay-per-execution), Premium (always warm), Dedicated (App Service Plan)
4. Trigger starts execution; binding connects to external resources without writing connection code
5. Set `--min-replicas 0` in scaling configuration
6. Group of containers scheduled together on the same host, share resources
7. Yes, using Timer trigger with CRON expression
8. Versioning of app deployments, enables traffic splitting and blue-green deployments

</details>

---

## Week 4: Azure Storage Solutions

### Focus Area
Master Azure storage services including Blob Storage, Cosmos DB, Table Storage, and caching.

### Objectives
- Work with Azure Blob Storage (containers, tiers, SAS tokens)
- Implement Cosmos DB with multiple APIs
- Use Table Storage for NoSQL data
- Implement Azure Files for shared storage
- Configure Azure Cache for Redis

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Storage Accounts | `/labs/storage/README.md` | 2 hours |
| Blob Storage | `/labs/storage-blob/README.md` | 2 hours |
| Static Website Storage | `/labs/storage-static/README.md` | 1.5 hours |
| Azure Files | `/labs/storage-files/README.md` | 1.5 hours |
| Table Storage | `/labs/storage-table/README.md` | 1.5 hours |
| Cosmos DB | `/labs/cosmos/README.md` | 2.5 hours |
| Cosmos DB Mongo API | `/labs/cosmos-mongo/README.md` | 2 hours |
| Cosmos DB Performance | `/labs/cosmos-perf/README.md` | 2 hours |
| Redis Cache | `/labs/redis/README.md` | 2 hours |

**Total Lab Time:** ~17 hours

### Key Concepts to Master

1. **Storage Account Basics**
   - Storage account types: General Purpose v2, Blob Storage, File Storage
   - Replication options: LRS, ZRS, GRS, RA-GRS, GZRS, RA-GZRS
   - Performance tiers: Standard vs Premium
   - Access tiers: Hot, Cool, Archive

2. **Blob Storage**
   - Container creation and access levels (Private, Blob, Container)
   - Blob types: Block blobs, Append blobs, Page blobs
   - Access tiers and lifecycle management
   - SAS tokens (Account SAS, Service SAS, User delegation SAS)
   - Blob leases for concurrency control

3. **Azure Files**
   - SMB and NFS protocols
   - File shares and mounting
   - Snapshots and soft delete
   - Azure File Sync

4. **Table Storage**
   - NoSQL key-value store
   - Partition key and row key
   - Querying with OData filters
   - Batch operations

5. **Cosmos DB**
   - Core (SQL) API - primary API
   - MongoDB API - compatibility layer
   - Table API - upgrade path from Table Storage
   - Gremlin API (Graph) - graph databases
   - Cassandra API - Cassandra compatibility

6. **Cosmos DB Key Concepts**
   - Request Units (RU/s) - throughput measurement
   - Partition keys and data distribution
   - Consistency levels: Strong, Bounded Staleness, Session, Consistent Prefix, Eventual
   - Global distribution and multi-region writes
   - Indexing policies

7. **Azure Cache for Redis**
   - Cache-aside pattern
   - Redis data structures
   - Pub/sub messaging
   - Persistence and clustering

### Microsoft Learn Modules

- [Store data in Azure](https://docs.microsoft.com/learn/paths/store-data-in-azure/)
- [Work with NoSQL data in Azure Cosmos DB](https://docs.microsoft.com/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)
- [Optimize your web applications by caching read-only data with Redis](https://docs.microsoft.com/learn/modules/optimize-your-web-apps-with-redis/)

### Practice Activities

1. **Blob Storage Practice:**
   ```bash
   # Create container and upload blob
   az storage container create -n mycontainer
   az storage blob upload -f myfile.txt -c mycontainer -n myblob

   # Generate SAS token
   az storage blob generate-sas -c mycontainer -n myblob \
     --permissions r --expiry 2024-12-31
   ```

2. **Cosmos DB Practice:**
   - Create a Cosmos DB account with SQL API
   - Design partition key for a blog post database
   - Query data using SQL syntax
   - Experiment with consistency levels

3. **Redis Practice:**
   - Implement cache-aside pattern in a web app
   - Use Redis for session storage
   - Test pub/sub messaging

### End-of-Week Assessment

**Quiz Questions:**

1. What's the difference between Hot, Cool, and Archive tiers?
2. Which Cosmos DB consistency level provides the lowest latency?
3. What is a partition key in Cosmos DB and why is it important?
4. How do you secure access to blob storage without sharing keys?
5. What is the difference between Table Storage and Cosmos DB Table API?
6. When should you use Azure Files vs Blob Storage?
7. What are Request Units (RUs) in Cosmos DB?
8. How does the cache-aside pattern work with Redis?

**Hands-On Challenge:**
Build a web application that:
1. Uploads images to Blob Storage
2. Stores image metadata in Cosmos DB
3. Generates SAS tokens for secure image access
4. Caches frequently accessed data in Redis
5. Implements proper error handling and retry logic

<details>
<summary>View Answers</summary>

1. Hot (frequent access, higher storage cost), Cool (infrequent, 30+ days), Archive (rare, 180+ days, offline)
2. Eventual consistency (but Session is default and recommended for most scenarios)
3. Logical partition for data distribution; poor choice leads to hot partitions and throttling
4. Shared Access Signatures (SAS tokens) with limited permissions and expiry
5. Table API is globally distributed, offers better SLAs, automatic indexing, and throughput control
6. Azure Files for shared file systems (SMB), Blob Storage for unstructured data and large objects
7. Normalized measure of throughput - combines CPU, memory, and IOPS into single metric
8. Check cache first; if miss, load from database and populate cache; subsequent requests hit cache

</details>

---

## Week 5: Messaging & Integration Services

### Focus Area
Master Azure messaging services and API Management for building distributed systems.

### Objectives
- Implement Service Bus queues and topics
- Process events with Event Hubs
- Build event-driven architectures with Event Grid
- Configure and manage API Management
- Create functions with messaging triggers

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Service Bus Queues | `/labs/servicebus/README.md` | 2 hours |
| Service Bus Pub/Sub | `/labs/servicebus-pubsub/README.md` | 2 hours |
| Event Hubs | `/labs/eventhubs/README.md` | 2 hours |
| Event Hubs Consumers | `/labs/eventhubs-consumers/README.md` | 2 hours |
| Event Grid | `/labs/eventgrid/README.md` | 2 hours |
| API Management | `/labs/apim/README.md` | 2.5 hours |
| APIM Mocking | `/labs/apim-mock/README.md` | 1.5 hours |
| APIM Policies | `/labs/apim-policies/README.md` | 2 hours |
| APIM Versioning | `/labs/apim-versioning/README.md` | 1.5 hours |
| Functions Service Bus | `/labs/functions/servicebus/README.md` | 1.5 hours |

**Total Lab Time:** ~19.5 hours

### Key Concepts to Master

1. **Service Bus Fundamentals**
   - Queues vs Topics
   - Messages, sessions, and dead-letter queues
   - At-least-once vs exactly-once delivery
   - Message deferral and scheduling
   - Transactions and duplicate detection

2. **Service Bus Queues**
   - Point-to-point messaging
   - Competing consumers pattern
   - Peek-lock vs receive-and-delete
   - Message TTL and max delivery count

3. **Service Bus Topics & Subscriptions**
   - Publish-subscribe pattern
   - Topic filters and actions
   - SQL filters for message routing
   - Subscription rules

4. **Event Hubs**
   - Streaming data ingestion
   - Partitions and throughput units
   - Consumer groups
   - Capture to blob storage
   - Event Processor Host
   - Checkpointing

5. **Event Grid**
   - Event-driven architecture
   - System topics (built-in Azure events)
   - Custom topics
   - Event subscriptions and filtering
   - Event handlers (webhooks, functions, etc.)
   - Event schemas
   - Retry policies and dead-lettering

6. **Service Bus vs Event Hubs vs Event Grid**
   - Service Bus: Enterprise messaging, guaranteed delivery
   - Event Hubs: Big data streaming, millions of events/sec
   - Event Grid: Reactive programming, event distribution

7. **API Management (APIM)**
   - Products, APIs, and operations
   - Subscriptions and API keys
   - Gateway, portal, and management plane
   - Developer portal customization

8. **APIM Policies**
   - Inbound, backend, outbound, on-error sections
   - Rate limiting and quotas
   - Request/response transformation
   - Caching policies
   - CORS configuration
   - Authentication (JWT validation, OAuth)

9. **API Versioning**
   - Versioning schemes: Path, Query, Header
   - Breaking vs non-breaking changes
   - API revisions vs versions

### Microsoft Learn Modules

- [Implement message-based communication workflows with Azure Service Bus](https://docs.microsoft.com/learn/modules/implement-message-workflows-with-service-bus/)
- [Enable reliable messaging for Big Data applications using Azure Event Hubs](https://docs.microsoft.com/learn/modules/enable-reliable-messaging-for-big-data-apps-using-event-hubs/)
- [React to state changes in your Azure services by using Event Grid](https://docs.microsoft.com/learn/modules/react-to-state-changes-using-event-grid/)
- [Publish and manage your APIs with Azure API Management](https://docs.microsoft.com/learn/modules/publish-manage-apis-with-azure-api-management/)

### Practice Activities

1. **Service Bus Practice:**
   ```bash
   # Send message to queue
   az servicebus queue send \
     --namespace-name mynamespace \
     --name myqueue \
     --body "Hello World"

   # Create topic subscription with filter
   az servicebus topic subscription create \
     --namespace-name mynamespace \
     --topic-name mytopic \
     --name mysub \
     --filter "priority='high'"
   ```

2. **Event Grid Practice:**
   - Subscribe to Storage Account blob created events
   - Create custom topic and publish events
   - Implement retry logic and dead-lettering

3. **APIM Practice:**
   - Import an existing API
   - Create rate limiting policy (10 calls/min)
   - Set up mock responses for testing
   - Implement request transformation

### End-of-Week Assessment

**Quiz Questions:**

1. When should you use Service Bus queues vs Service Bus topics?
2. What is the purpose of partitions in Event Hubs?
3. How does Event Grid differ from Service Bus?
4. What is a consumer group in Event Hubs?
5. What are the four sections where APIM policies can be applied?
6. How do you implement rate limiting in APIM?
7. What's the difference between API versions and revisions?
8. What is a dead-letter queue and when is it used?

**Hands-On Challenge:**
Build an order processing system:
1. Submit orders to Service Bus queue
2. Process orders with Azure Function
3. Publish "OrderProcessed" events to Event Grid
4. Subscribe multiple handlers (email, logging, inventory)
5. Expose order status API via APIM with:
   - Rate limiting (100 calls/hour)
   - JWT validation
   - Response caching

<details>
<summary>View Answers</summary>

1. Queues for point-to-point; Topics for pub-sub with multiple subscribers
2. Partitions enable parallel processing and ordering within partition
3. Event Grid is for event distribution/notification; Service Bus for reliable message delivery
4. Logical group of event consumers that maintain independent read position
5. Inbound, Backend, Outbound, On-Error
6. Using `rate-limit` or `rate-limit-by-key` policy in inbound section
7. Versions for breaking changes; Revisions for non-breaking iterative changes
8. Storage for messages that can't be processed after max delivery attempts

</details>

---

## Week 6: Security & Networking

### Focus Area
Implement security best practices with Key Vault, Managed Identities, and Virtual Networks.

### Objectives
- Secure secrets and keys with Azure Key Vault
- Implement Managed Identities for passwordless authentication
- Configure virtual networks and network security
- Integrate security across Azure services

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Key Vault Basics | `/labs/keyvault/README.md` | 2 hours |
| Key Vault Access | `/labs/keyvault-access/README.md` | 2.5 hours |
| Virtual Networks | `/labs/vnet/README.md` | 2 hours |
| VNet Access Control | `/labs/vnet-access/README.md` | 2 hours |
| VNet + Key Vault + Apps | `/labs/vnet-apps/README.md` | 3 hours |
| AKS with Key Vault | `/labs/aks-keyvault/README.md` | 2 hours (optional) |

**Total Lab Time:** ~11.5-13.5 hours

### Key Concepts to Master

1. **Azure Key Vault**
   - Secrets, keys, and certificates
   - Soft delete and purge protection
   - Key rotation strategies
   - Access policies vs RBAC
   - HSM-backed keys (Premium tier)

2. **Managed Identities**
   - System-assigned vs User-assigned
   - How managed identities work (Azure AD authentication)
   - Services that support managed identities
   - Accessing Key Vault with managed identity
   - No secrets in code!

3. **Key Vault Integration**
   - App Service integration
   - Function Apps integration
   - Key Vault references in configuration
   - Azure Key Vault provider for Secrets Store CSI driver (AKS)

4. **Virtual Networks (VNet)**
   - Address spaces and subnets
   - Network Security Groups (NSGs)
   - Service endpoints
   - Private endpoints vs service endpoints
   - VNet peering

5. **Network Security**
   - NSG rules (priority, direction, protocol)
   - Application Security Groups (ASGs)
   - Azure Firewall
   - DDoS Protection

6. **Service Integration with VNet**
   - App Service VNet integration
   - Private endpoints for PaaS services
   - Service endpoints for Azure services
   - Key Vault firewall rules

7. **Azure AD and Authentication**
   - Service principals
   - OAuth 2.0 flows
   - Azure AD authentication for APIs
   - JWT token validation

### Microsoft Learn Modules

- [Secure your Azure resources with Azure Key Vault](https://docs.microsoft.com/learn/modules/protect-against-security-threats-azure/)
- [Manage secrets in your server apps with Azure Key Vault](https://docs.microsoft.com/learn/modules/manage-secrets-with-azure-key-vault/)
- [Secure and isolate access to Azure resources by using network security groups and service endpoints](https://docs.microsoft.com/learn/modules/secure-and-isolate-with-nsg-and-service-endpoints/)

### Practice Activities

1. **Key Vault Practice:**
   ```bash
   # Create Key Vault
   az keyvault create -n myvault -g mygroup

   # Add secret
   az keyvault secret set --vault-name myvault \
     --name "DbPassword" --value "SecureP@ssw0rd"

   # Grant access to managed identity
   az keyvault set-policy --name myvault \
     --object-id <managed-identity-id> \
     --secret-permissions get list
   ```

2. **Managed Identity Practice:**
   - Enable system-assigned identity on App Service
   - Access Key Vault from code using managed identity
   - No connection strings or passwords in code!

3. **VNet Practice:**
   - Create VNet with multiple subnets
   - Configure NSG rules
   - Set up private endpoint for Storage Account
   - Test connectivity from App Service

### End-of-Week Assessment

**Quiz Questions:**

1. What's the difference between system-assigned and user-assigned managed identities?
2. How do you access Key Vault secrets from App Service without storing credentials?
3. What is the purpose of soft delete in Key Vault?
4. What's the difference between service endpoints and private endpoints?
5. How do NSG rules work (priority, evaluation)?
6. Can you store certificates in Key Vault? What's the benefit?
7. What authentication methods can be used with Azure Key Vault?
8. How do you restrict Key Vault access to specific VNets?

**Hands-On Challenge:**
Build a secure architecture:
1. Create App Service with system-assigned managed identity
2. Store database connection string in Key Vault
3. Grant App Service access to Key Vault
4. Configure App Service to use VNet integration
5. Create private endpoint for Key Vault
6. Configure NSG to restrict access
7. Access secret from app code using managed identity

<details>
<summary>View Answers</summary>

1. System-assigned is tied to resource lifecycle; User-assigned is independent and can be shared
2. Enable managed identity, grant Key Vault access policy, use DefaultAzureCredential in code
3. Recovery period (90 days default) before permanent deletion; prevents accidental data loss
4. Service endpoints route traffic over Azure backbone; Private endpoints use private IP in your VNet
5. Rules evaluated by priority (100-4096, lower first); first matching rule applies
6. Yes; automatic renewal, centralized management, TLS/SSL integration
7. Managed identities, service principals, Azure AD users, access keys (legacy)
8. Configure Key Vault firewall with VNet rules or use private endpoints

</details>

---

## Week 7: Monitoring & Advanced Topics

### Focus Area
Implement monitoring, optimize performance, and master advanced patterns like durable functions.

### Objectives
- Instrument applications with Application Insights
- Query logs with Log Analytics and KQL
- Implement durable functions patterns
- Use SignalR for real-time communication
- Optimize application performance

### Labs to Complete

| Lab | Path | Estimated Time |
|-----|------|----------------|
| Application Insights | `/labs/applicationinsights/README.md` | 2.5 hours |
| Log Analytics | `/labs/loganalytics/README.md` | 2 hours |
| Functions CI/CD | `/labs/functions/cicd/README.md` | 2 hours |
| Durable Functions - Chained | `/labs/functions-durable/chained/README.md` | 2.5 hours |
| Durable Functions - Fan-out | `/labs/functions-durable/fan-out/README.md` | 2.5 hours |
| Durable Functions - Human | `/labs/functions-durable/human/README.md` | 2 hours |
| Functions Cosmos Trigger | `/labs/functions/cosmos/README.md` | 1.5 hours |
| SignalR Service | `/labs/signalr/README.md` | 2 hours |
| Functions SignalR Output | `/labs/functions/signalr/README.md` | 1.5 hours |

**Total Lab Time:** ~18.5 hours

### Key Concepts to Master

1. **Application Insights**
   - Automatic instrumentation
   - Custom telemetry (events, metrics, traces)
   - Dependency tracking
   - Application Map
   - Live Metrics Stream
   - Availability tests
   - Sampling to control data volume

2. **Log Analytics & KQL**
   - Kusto Query Language basics
   - Common query patterns
   - Aggregations and time-series analysis
   - Joins across multiple tables
   - Visualizations and workbooks

3. **Performance Optimization**
   - Caching strategies (Redis, CDN)
   - Async/await patterns
   - Connection pooling
   - Retry policies and circuit breakers
   - Content Delivery Network (CDN)

4. **Durable Functions**
   - Orchestration functions
   - Activity functions
   - Entity functions
   - Durable patterns:
     - Function chaining
     - Fan-out/fan-in
     - Async HTTP APIs
     - Monitor pattern
     - Human interaction
     - Aggregator (stateful entities)

5. **SignalR Service**
   - Real-time bidirectional communication
   - WebSockets abstraction
   - Connection management
   - Azure SignalR Service benefits
   - Integration with Azure Functions

6. **Azure Monitor**
   - Metrics vs Logs
   - Alerts and action groups
   - Autoscale rules
   - Diagnostic settings

### Microsoft Learn Modules

- [Monitor app performance](https://docs.microsoft.com/learn/modules/monitor-app-performance/)
- [Analyze your Azure infrastructure by using Azure Monitor logs](https://docs.microsoft.com/learn/modules/analyze-infrastructure-with-azure-monitor-logs/)
- [Create a long-running serverless workflow with Durable Functions](https://docs.microsoft.com/learn/modules/create-long-running-serverless-workflow-with-durable-functions/)

### Practice Activities

1. **Application Insights Practice:**
   ```csharp
   // Custom telemetry
   telemetryClient.TrackEvent("OrderPlaced");
   telemetryClient.TrackMetric("OrderValue", orderValue);
   telemetryClient.TrackDependency("SQL", "GetUser", startTime, duration, success);
   ```

2. **KQL Practice:**
   ```kql
   // Find failed requests in last 24 hours
   requests
   | where timestamp > ago(24h)
   | where success == false
   | summarize count() by resultCode
   | order by count_ desc

   // Find slowest dependencies
   dependencies
   | where timestamp > ago(1h)
   | summarize avg(duration), percentile(duration, 95) by name
   | order by avg_duration desc
   ```

3. **Durable Functions Practice:**
   - Implement function chaining for order processing
   - Implement fan-out/fan-in for parallel processing
   - Implement human interaction with timeout

### End-of-Week Assessment

**Quiz Questions:**

1. What types of telemetry does Application Insights automatically collect?
2. What is KQL and where is it used?
3. What is the difference between orchestration and activity functions?
4. Which durable function pattern would you use for parallel processing?
5. How does SignalR maintain real-time connections?
6. What is the purpose of sampling in Application Insights?
7. How do you implement a long-running approval workflow?
8. What are the benefits of using Azure SignalR Service vs self-hosted?

**Hands-On Challenge:**
Build a document processing system:
1. Orchestrator function receives document URL
2. Fan-out to multiple activity functions for:
   - Text extraction
   - Image processing
   - Sentiment analysis
3. Fan-in to aggregate results
4. Store results in Cosmos DB
5. Send real-time updates via SignalR
6. Track entire workflow in Application Insights
7. Create KQL queries to monitor performance

<details>
<summary>View Answers</summary>

1. Requests, dependencies, exceptions, page views, custom events
2. Kusto Query Language - used for querying logs in Log Analytics and Application Insights
3. Orchestrator coordinates workflow; Activity performs actual work unit
4. Fan-out/fan-in pattern
5. WebSockets primarily, with fallback to Server-Sent Events and long polling
6. Control data volume and cost while maintaining statistical significance
7. Use human interaction pattern with external events and timers
8. Scale to millions of connections, built-in backplane, no server management

</details>

---

## Week 8: Review & Exam Preparation

### Focus Area
Consolidate knowledge, practice exam scenarios, and address weak areas.

### Objectives
- Review all five exam domains
- Take practice exams
- Identify and strengthen weak areas
- Practice exam scenarios
- Build confidence

### Activities

#### Day 1-2: Domain Review

**Review all domains with focus on:**
- Key services and when to use each
- Common patterns and architectures
- CLI commands and SDK usage
- Configuration and best practices

**Domain Checklist:**

- [ ] **Compute:** App Service, Functions, Containers (ACI, Container Apps)
- [ ] **Storage:** Blob, Cosmos DB, Table, Files, Redis
- [ ] **Security:** Key Vault, Managed Identities, VNet
- [ ] **Monitoring:** Application Insights, Log Analytics
- [ ] **Integration:** Service Bus, Event Hubs, Event Grid, APIM

#### Day 3-4: Practice Exams

Take multiple practice exams to:
- Familiarize with question format
- Identify knowledge gaps
- Practice time management

**Recommended Practice Resources:**
- [Microsoft Official Practice Assessment](https://docs.microsoft.com/certifications/exams/az-204/practice/assessment)
- [MeasureUp Practice Tests](https://www.measureup.com/microsoft-practice-test-az-204-developing-solutions-for-microsoft-azure.html)
- [Whizlabs AZ-204 Practice Tests](https://www.whizlabs.com/microsoft-azure-certification-az-204/)

#### Day 5-6: Weak Area Deep Dive

**Common Weak Areas:**

1. **Durable Functions Patterns**
   - Review each pattern thoroughly
   - Understand when to use each
   - Practice code scenarios

2. **Cosmos DB Concepts**
   - Partition key selection
   - Consistency levels trade-offs
   - Request Units calculations

3. **Security Best Practices**
   - Managed identities vs service principals
   - Key Vault integration patterns
   - RBAC vs access policies

4. **APIM Policies**
   - Policy execution order
   - Common policy elements
   - Error handling

**Remediation Activities:**
- Re-read documentation on weak topics
- Redo relevant labs
- Watch video tutorials
- Explain concepts to someone else

#### Day 7: Scenario Practice

**Practice common exam scenarios:**

1. **Architecture Design:**
   - Given requirements, choose appropriate services
   - Consider cost, performance, scalability
   - Implement security best practices

2. **Troubleshooting:**
   - Application is slow - how to diagnose?
   - Function not triggering - what to check?
   - Authentication failing - where to look?

3. **Code Completion:**
   - Complete code snippets
   - Choose correct SDK methods
   - Fix buggy code

4. **CLI Commands:**
   - Choose correct command for task
   - Identify syntax errors
   - Order commands correctly

### Quick Reference Cards

Create reference cards for:
- **Service Comparison Tables** (when to use which service)
- **Common CLI Commands** by service
- **Key Concepts** for each domain
- **Security Checklists**
- **Pricing Tier Comparison**

### End-of-Week Assessment

**Full Mock Exam:**
- 50-60 questions
- 120 minutes
- Aim for 75%+ score

**Self-Assessment Questions:**

1. Can you explain all 5 exam domains confidently?
2. Are you comfortable with Azure CLI commands?
3. Can you design solutions based on requirements?
4. Do you understand security best practices?
5. Can you troubleshoot common issues?
6. Do you know when to use each Azure service?

**If answering "no" to any:**
- Spend extra days on those topics
- Don't rush to exam if not ready
- Better to delay and pass than fail

---

## Study Strategies

### Effective Learning Techniques

1. **Hands-On Practice (Most Important!)**
   - Azure is learned by doing
   - Complete every lab in this guide
   - Experiment beyond lab instructions
   - Break things and fix them
   - 70% of your time should be hands-on

2. **Active Learning**
   - Don't just read - type commands yourself
   - Explain concepts out loud or in writing
   - Teach someone else what you learned
   - Create mind maps and diagrams

3. **Spaced Repetition**
   - Review previous week's material daily
   - Use flashcards for key concepts
   - Revisit difficult topics multiple times
   - Don't cram - spread learning over weeks

4. **Documentation Reading**
   - Microsoft Learn is your friend
   - Read official documentation thoroughly
   - Bookmark important pages
   - Understand "why" not just "how"

5. **Community Engagement**
   - Join Azure community forums
   - Participate in Azure discussions
   - Read others' questions and solutions
   - Share your learning journey

### Time Management

**Daily Study Schedule Example:**

- **Morning (2 hours):** Theory, documentation reading, video tutorials
- **Afternoon/Evening (2 hours):** Hands-on labs, coding practice
- **Breaks:** 10-15 minutes every hour
- **Weekend:** Extended lab sessions (3-4 hours each day)

**Weekly Rhythm:**

- **Monday-Friday:** 2-3 hours daily
- **Saturday:** 4-5 hours (longer lab sessions)
- **Sunday:** 3-4 hours + weekly review
- **Total:** 15-20 hours per week

### Note-Taking Strategy

**Create a Study Notebook:**

1. **Concept Pages:** One page per major concept with:
   - Definition
   - When to use
   - CLI commands
   - Code examples
   - Common mistakes

2. **Command Reference:** Organized by service:
   ```
   # App Service Commands
   az webapp create ...
   az webapp config appsettings set ...
   az webapp deployment slot create ...
   ```

3. **Comparison Tables:** Side-by-side comparisons:
   - Service Bus vs Event Hubs vs Event Grid
   - ACI vs Container Apps vs AKS
   - Consistency levels in Cosmos DB

4. **Personal Gotchas:** Things you struggled with

### Dealing with Overwhelming Content

**When Feeling Overwhelmed:**

1. **Break It Down:** Focus on one service at a time
2. **Take Breaks:** Step away, go for a walk
3. **Review Basics:** Go back to fundamentals
4. **Ask for Help:** Community forums, study groups
5. **Adjust Pace:** It's okay to take longer than 8 weeks
6. **Celebrate Small Wins:** Completed a lab? Celebrate!

### Lab Best Practices

1. **Before Starting Lab:**
   - Read README completely
   - Understand objectives
   - Check prerequisites

2. **During Lab:**
   - Type commands yourself (don't copy-paste)
   - Read error messages carefully
   - Experiment beyond instructions
   - Take notes on interesting findings

3. **After Lab:**
   - Review what you learned
   - Try the "Lab" challenge section
   - Delete resources (avoid charges!)
   - Document any issues encountered

4. **Cost Management:**
   - Always clean up resources after labs
   - Use "az group delete" to remove resource groups
   - Set up spending alerts
   - Use free tiers when available

### Resource Management

**Avoid Unexpected Charges:**

```bash
# Clean up resource groups after each lab
az group delete -n labs-resourcegroup --yes --no-wait

# List all resource groups
az group list --output table

# Delete multiple groups
az group list --query "[?tags.courselabs=='azure'].name" -o tsv | \
  xargs -I {} az group delete -n {} --yes --no-wait
```

---

## Resource Links

### Official Microsoft Resources

**Microsoft Learn - Primary Study Resource:**
- [AZ-204 Exam Page](https://docs.microsoft.com/certifications/exams/az-204)
- [AZ-204 Learning Paths](https://docs.microsoft.com/certifications/azure-developer/)
- [Microsoft Learn AZ-204](https://docs.microsoft.com/learn/certifications/exams/az-204)

**Microsoft Documentation:**
- [Azure Documentation](https://docs.microsoft.com/azure/)
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/)
- [Azure SDK for .NET](https://docs.microsoft.com/dotnet/azure/)
- [Azure SDK for Python](https://docs.microsoft.com/python/azure/)
- [Azure SDK for JavaScript](https://docs.microsoft.com/javascript/azure/)

**Azure Architecture Center:**
- [Cloud Design Patterns](https://docs.microsoft.com/azure/architecture/patterns/)
- [Best Practices](https://docs.microsoft.com/azure/architecture/best-practices/)

### Service-Specific Documentation

**Compute:**
- [App Service](https://docs.microsoft.com/azure/app-service/)
- [Azure Functions](https://docs.microsoft.com/azure/azure-functions/)
- [Container Instances](https://docs.microsoft.com/azure/container-instances/)
- [Container Apps](https://docs.microsoft.com/azure/container-apps/)
- [Container Registry](https://docs.microsoft.com/azure/container-registry/)

**Storage:**
- [Blob Storage](https://docs.microsoft.com/azure/storage/blobs/)
- [Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/)
- [Azure Cache for Redis](https://docs.microsoft.com/azure/azure-cache-for-redis/)
- [Table Storage](https://docs.microsoft.com/azure/storage/tables/)

**Security:**
- [Key Vault](https://docs.microsoft.com/azure/key-vault/)
- [Managed Identities](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/)
- [Azure AD](https://docs.microsoft.com/azure/active-directory/)

**Messaging:**
- [Service Bus](https://docs.microsoft.com/azure/service-bus-messaging/)
- [Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Event Grid](https://docs.microsoft.com/azure/event-grid/)

**Integration:**
- [API Management](https://docs.microsoft.com/azure/api-management/)
- [SignalR Service](https://docs.microsoft.com/azure/azure-signalr/)

**Monitoring:**
- [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview)
- [Log Analytics](https://docs.microsoft.com/azure/azure-monitor/logs/log-analytics-overview)

### Practice & Testing

**Practice Exams:**
- [Microsoft Official Practice Assessment](https://docs.microsoft.com/certifications/exams/az-204/practice/assessment) - FREE
- [MeasureUp](https://www.measureup.com/) - Paid, high quality
- [Whizlabs](https://www.whizlabs.com/) - Paid, good value

**Hands-On Practice:**
- [Microsoft Learn Sandbox](https://docs.microsoft.com/learn/) - Free Azure environment
- [Azure Free Account](https://azure.microsoft.com/free/) - $200 credit

### Community & Support

**Forums & Communities:**
- [Microsoft Q&A - Azure](https://docs.microsoft.com/answers/products/azure)
- [Stack Overflow - Azure Tag](https://stackoverflow.com/questions/tagged/azure)
- [Reddit r/AZURE](https://reddit.com/r/AZURE)
- [Reddit r/AzureCertification](https://reddit.com/r/AzureCertification)

**Study Groups:**
- LinkedIn Azure study groups
- Discord Azure communities
- Local Azure user groups

### Video Resources

**Microsoft Official:**
- [John Savill's Technical Training](https://www.youtube.com/c/NTFAQGuy) - Excellent Azure content
- [Azure Friday](https://azure.microsoft.com/resources/videos/azure-friday/) - Weekly show

**Third-Party Courses:**
- [Pluralsight AZ-204 Path](https://www.pluralsight.com/) - Comprehensive courses
- [A Cloud Guru](https://acloudguru.com/) - Interactive learning
- [Udemy AZ-204 Courses](https://www.udemy.com/) - Various instructors

### Books

- **Exam Ref AZ-204 Developing Solutions for Microsoft Azure** - Official Microsoft exam guide
- **Azure for Developers** - Comprehensive Azure development guide

### Tools & Utilities

**Development Tools:**
- [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli)
- [Azure PowerShell](https://docs.microsoft.com/powershell/azure/)
- [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/)
- [Postman](https://www.postman.com/) - API testing
- [Azure Data Studio](https://docs.microsoft.com/sql/azure-data-studio/)

**VS Code Extensions:**
- Azure Account
- Azure App Service
- Azure Functions
- Azure Storage
- Azure Databases
- Azure API Management
- Docker
- REST Client

### Cheat Sheets & Quick References

- [Azure CLI Cheat Sheet](https://docs.microsoft.com/cli/azure/reference-index)
- [Azure Architecture Icons](https://docs.microsoft.com/azure/architecture/icons/)
- [Azure Service Comparison](https://azure.microsoft.com/solutions/architecture/)

---

## Final Week Strategy

### Week 8 Detailed Schedule

#### Monday & Tuesday: Comprehensive Review

**Morning:**
- Review notes from all weeks
- Go through comparison tables
- Review CLI command reference
- Watch recap videos

**Afternoon:**
- Take first practice exam
- Note questions missed
- Research correct answers
- Update notes with clarifications

**Key Focus Areas:**
- Service selection (when to use what)
- Security best practices
- Integration patterns
- Troubleshooting approaches

#### Wednesday & Thursday: Weak Area Deep Dive

**Morning:**
- Review practice exam results
- Identify top 3 weak areas
- Read documentation on weak topics
- Watch videos on weak topics

**Afternoon:**
- Redo labs related to weak areas
- Practice CLI commands
- Code scenarios
- Take second practice exam

**Target Weak Areas Often Include:**
1. Durable Functions orchestration patterns
2. Cosmos DB partition key strategy
3. APIM policy syntax and execution order
4. Managed Identity integration
5. Event Grid vs Event Hubs vs Service Bus

#### Friday: Exam Scenarios & Time Management

**Practice Scenario-Based Questions:**

1. **Design Scenarios:**
   - "Design a serverless order processing system"
   - "Implement secure API for mobile app"
   - "Build real-time chat application"

2. **Troubleshooting Scenarios:**
   - Function not triggering from blob storage
   - High Cosmos DB costs
   - App Service authentication failures
   - APIM returning 500 errors

3. **Code Completion:**
   - Fill in SDK method calls
   - Complete Azure CLI commands
   - Fix code bugs

**Time Management Practice:**
- Aim for 1.5-2 minutes per question
- Mark uncertain questions for review
- Don't get stuck on any single question
- Case studies may take 10-15 minutes

#### Saturday: Full Practice Exam Day

**Morning:**
- Take full-length practice exam (2 hours)
- Simulate real exam conditions:
  - No distractions
  - Timer set for 120 minutes
  - No reference materials
  - Track flagged questions

**Afternoon:**
- Review exam thoroughly
- Research every missed question
- Understand why wrong answers are wrong
- Update notes with new learnings

**Target Score:** 75%+ (850/1000)

If scoring below 70%, consider delaying exam by 1-2 weeks.

#### Sunday: Light Review & Relaxation

**Morning (2 hours):**
- Review flashcards
- Quick skim of notes
- Read through comparison tables
- Watch a favorite Azure tutorial

**Afternoon:**
- Relax and recharge
- Light exercise
- Avoid cramming
- Get good sleep

**Don't:**
- Try to learn new topics
- Stay up late studying
- Stress about gaps in knowledge
- Overwork yourself

### Final Days Before Exam

**2 Days Before:**
- Review key concepts
- Practice CLI commands
- Light lab work
- Confidence building

**1 Day Before:**
- Light review only (1-2 hours)
- Prepare logistics (exam location, ID, etc.)
- Relax and rest
- Good night's sleep (8+ hours)

**Exam Day Morning:**
- Light breakfast
- Arrive 15 minutes early (online or test center)
- Don't study right before exam
- Stay calm and confident

---

## Exam Day Tips

### Before the Exam

**What to Bring (Test Center):**
- Two forms of ID (check requirements)
- Confirmation email
- Arrive 15 minutes early

**Online Exam Setup:**
- Test system requirements 24 hours before
- Clean desk and room
- Close all applications
- Have ID ready
- Good internet connection
- Quiet environment

**Morning Routine:**
- Eat a good breakfast
- Stay hydrated
- Avoid caffeine overload
- Get to test center early
- Stay calm and positive

### During the Exam

**General Strategy:**

1. **Read Questions Carefully:**
   - Read entire question before looking at answers
   - Watch for words like "NOT", "EXCEPT", "LEAST"
   - Understand what's being asked

2. **Time Management:**
   - 120 minutes for 40-60 questions
   - ~1.5-2 minutes per question
   - Don't spend >3 minutes on any question
   - Flag difficult questions for review
   - Leave time to review (10-15 minutes)

3. **Elimination Strategy:**
   - Eliminate obviously wrong answers first
   - Narrow down to 2-3 options
   - Use knowledge to select best answer
   - Trust your preparation

4. **Case Studies:**
   - Read scenario completely first
   - Take notes on key requirements
   - Answer questions based on scenario
   - May take 10-15 minutes per case study

**Question Type Strategies:**

**Multiple Choice (Select One):**
- Only one correct answer
- Eliminate wrong answers
- Choose most complete/accurate answer

**Multiple Response (Select All):**
- Usually 2-3 correct answers
- All correct answers must be selected
- Partial credit not given

**Drag and Drop:**
- Order matters (especially for CLI commands)
- Think through sequence logically
- Double-check before moving on

**Code/CLI Questions:**
- Syntax matters
- Check for correct service names
- Verify parameter order
- Look for missing required parameters

### Common Pitfalls to Avoid

1. **Rushing Through Questions:**
   - Take your time to read carefully
   - Don't make assumptions

2. **Second-Guessing:**
   - Trust your first instinct
   - Only change answers if you're certain

3. **Overthinking:**
   - Questions are usually straightforward
   - Don't look for tricks

4. **Getting Stuck:**
   - Flag and move on
   - Come back with fresh perspective

5. **Panic:**
   - Stay calm if you don't know an answer
   - Use elimination method
   - Make educated guess if needed

### Managing Exam Anxiety

**If Feeling Anxious:**
- Take deep breaths
- Close eyes for 10 seconds
- Stretch at your seat
- Remember: You've prepared well
- One question at a time

**If Stuck on Question:**
- Flag it
- Move on
- Come back later with fresh mind
- Don't let one question derail you

### Review Period

**If Time Permits:**
- Review flagged questions
- Double-check answers you were uncertain about
- Verify you answered all questions
- Check for silly mistakes

**Don't:**
- Change answers without good reason
- Rush through review
- Second-guess too much

### After Submitting

**Immediate Results:**
- Exam results shown immediately
- Pass/Fail and score displayed
- Detailed score report by domain

**If You Pass:**
- Congratulations!
- Certificate available in 1-2 days
- Update LinkedIn, resume
- Celebrate your achievement!

**If You Don't Pass:**
- Don't be discouraged
- Review score report carefully
- Identify weak domains
- Study those areas thoroughly
- Retake when ready (24-hour wait)

---

## After the Exam

### If You Pass - Congratulations!

**Immediate Steps:**

1. **Download Certificate:**
   - Available in Microsoft certification dashboard
   - Usually within 24-48 hours
   - Digital badge for LinkedIn

2. **Update Professional Profiles:**
   - LinkedIn: Add certification to profile
   - Resume: Add to certifications section
   - Email signature: Include credentials

3. **Share Achievement:**
   - Post on LinkedIn
   - Share with professional network
   - Thank study partners and mentors

**Maintaining Certification:**
- AZ-204 valid for 1 year
- Renewal required annually
- Free online renewal assessment
- Stay current with Azure updates

**Next Steps:**

1. **Apply Knowledge:**
   - Work on real Azure projects
   - Build portfolio applications
   - Contribute to open source

2. **Continue Learning:**
   - Stay updated with Azure announcements
   - Follow Azure blog and updates
   - Join Azure community events

3. **Advanced Certifications:**
   - Azure Solutions Architect Expert (AZ-305)
   - Azure DevOps Engineer Expert (AZ-400)
   - Specialty certifications (AI, Security, etc.)

4. **Share Knowledge:**
   - Write blog posts about your journey
   - Help others prepare for AZ-204
   - Speak at meetups/conferences

### If You Don't Pass - Keep Going!

**Don't Be Discouraged:**
- Many people don't pass on first attempt
- It's a learning opportunity
- You're now more prepared for next time

**Analyze Score Report:**
- Review percentage scores by domain
- Identify domains below 70%
- Focus study on weak areas

**Create Remediation Plan:**

1. **Week 1-2:** Focus on weakest domain
   - Redo relevant labs
   - Read documentation thoroughly
   - Watch video tutorials
   - Practice CLI commands

2. **Week 3:** Second weakest domain
   - Same intensive review process

3. **Week 4:** Take practice exams
   - Target 85%+ score
   - Review all missed questions

4. **Schedule Retake:**
   - When consistently scoring 80%+ on practice exams
   - When confident in weak areas
   - Don't rush - be ready

**Retake Logistics:**
- 24-hour waiting period minimum
- Discount vouchers sometimes available
- Learn from first attempt experience

**Stay Motivated:**
- Remember why you started
- Visualize success
- Seek support from community
- Celebrate small progress

---

## Additional Tips for Success

### Service Comparison Tables

**When to Use Which Storage Service:**

| Need | Service | Why |
|------|---------|-----|
| Unstructured data, large files | Blob Storage | Cost-effective, scalable |
| NoSQL, global distribution | Cosmos DB | Low latency, multi-model |
| Simple key-value NoSQL | Table Storage | Cheapest NoSQL option |
| Shared file system | Azure Files | SMB protocol, mounting |
| Caching, sessions | Redis | In-memory, fast |

**When to Use Which Messaging Service:**

| Need | Service | Why |
|------|---------|-----|
| Reliable message delivery | Service Bus | Transactions, dead-letter |
| Pub-sub messaging | Service Bus Topics | Multiple subscribers |
| Big data streaming | Event Hubs | Millions events/sec |
| Event notifications | Event Grid | Reactive programming |

**When to Use Which Compute Service:**

| Need | Service | Why |
|------|---------|-----|
| Web apps, APIs | App Service | Managed platform, easy deployment |
| Event-driven, serverless | Functions | Pay-per-execution, auto-scale |
| Simple containers | ACI | Fast startup, no orchestration |
| Microservices, serverless containers | Container Apps | Auto-scale, revisions, Dapr |
| Full Kubernetes control | AKS | Complete orchestration |

### Common CLI Command Patterns

```bash
# Resource Groups
az group create -n <name> -l <location>
az group delete -n <name> --yes --no-wait
az group list --output table

# App Service
az appservice plan create -n <name> -g <group> --sku B1
az webapp create -n <name> -g <group> --plan <plan>
az webapp deployment source config --name <name> --repo-url <url>
az webapp deployment slot create --name <name> --slot staging

# Storage
az storage account create -n <name> -g <group> --sku Standard_LRS
az storage container create -n <name> --account-name <account>
az storage blob upload -f <file> -c <container> -n <name>

# Functions
az functionapp create -n <name> -g <group> --storage-account <sa> \
  --consumption-plan-location <location>

# Key Vault
az keyvault create -n <name> -g <group>
az keyvault secret set --vault-name <name> --name <key> --value <value>
az keyvault secret show --vault-name <name> --name <key>

# Cosmos DB
az cosmosdb create -n <name> -g <group>
az cosmosdb sql database create --account-name <name> --name <db>
az cosmosdb sql container create --account-name <name> \
  --database-name <db> --name <container> --partition-key-path /id

# Container Registry
az acr create -n <name> -g <group> --sku Basic
az acr build -r <name> -t <image>:<tag> .

# Service Bus
az servicebus namespace create -n <name> -g <group>
az servicebus queue create --namespace-name <ns> --name <queue>
az servicebus topic create --namespace-name <ns> --name <topic>
```

### Key Concepts Summary

**Security Best Practices:**
1. Always use managed identities (no passwords in code)
2. Store secrets in Key Vault
3. Enable soft delete on Key Vault
4. Use HTTPS/TLS for all communication
5. Implement least privilege access (RBAC)
6. Enable diagnostic logging
7. Use private endpoints for sensitive services

**Performance Best Practices:**
1. Use Redis for caching
2. Enable CDN for static content
3. Choose appropriate Cosmos DB partition key
4. Use async/await patterns
5. Implement connection pooling
6. Use Application Insights for monitoring
7. Enable auto-scaling

**Cost Optimization:**
1. Use consumption plans for intermittent workloads
2. Enable auto-scale rules
3. Use lifecycle management for blob storage
4. Choose appropriate Cosmos DB throughput
5. Delete unused resources
6. Use reserved instances for predictable workloads
7. Monitor costs with Azure Cost Management

---

## Motivational Conclusion

### You Can Do This!

Preparing for the AZ-204 exam is a significant undertaking, but you've got this! Here's what you've accomplished by following this guide:

**What You've Learned:**
- 40+ hands-on labs completed
- 5 major Azure domains mastered
- 20+ Azure services understood deeply
- Real-world scenarios practiced
- Security and best practices learned

**What This Means:**
- You're ready for the exam
- You have practical Azure skills
- You can build production systems
- You understand cloud architecture
- You're a valuable Azure developer

### Final Encouragement

**Remember:**
- **Consistent effort beats cramming:** Your 8 weeks of steady study are more valuable than last-minute panic
- **Hands-on experience matters most:** You've built real things, not just memorized
- **It's okay to not know everything:** The exam tests practical knowledge, not perfection
- **You've prepared well:** Trust your preparation and your abilities

**On Exam Day:**
- Trust your preparation
- Stay calm and focused
- Read questions carefully
- Use your time wisely
- Believe in yourself

**After the Exam:**
- Regardless of result, you've grown
- You've gained valuable Azure skills
- Certification is one step in your journey
- Keep building, keep learning, keep growing

### Good Luck!

You've put in the work. You've completed the labs. You've studied the concepts. Now it's time to demonstrate what you know.

**Go ace that exam!**

---

*"The only way to do great work is to love what you do." - Steve Jobs*

*"Success is the sum of small efforts repeated day in and day out." - Robert Collier*

**You've got this! Best of luck on your AZ-204 journey!**

---

## Appendix: Quick Reference

### Exam Registration Links

- **Schedule Exam:** https://docs.microsoft.com/certifications/exams/az-204
- **Certification Dashboard:** https://aka.ms/certdashboard
- **Pearson VUE:** https://home.pearsonvue.com/microsoft

### Important Azure Limits

| Service | Limit | Notes |
|---------|-------|-------|
| App Service | 10 apps per plan (Free tier) | More on paid tiers |
| Functions | 10 GB storage, 200 apps | Consumption plan |
| Storage Account | 5 PB max | 500 TB default |
| Cosmos DB | 20 GB free tier | 1000 RU/s included |
| Key Vault | 25,000 transactions/10s | Soft throttling |

### Default Ports

| Service | Port | Protocol |
|---------|------|----------|
| HTTP | 80 | TCP |
| HTTPS | 443 | TCP |
| SQL Server | 1433 | TCP |
| MySQL | 3306 | TCP |
| PostgreSQL | 5432 | TCP |
| Redis | 6379 | TCP |

### Time Zones

Exam questions may reference time zones:
- Use UTC for consistency
- Azure uses UTC by default
- Convert to local as needed

---

**Document Version:** 1.0
**Last Updated:** 2025-11-05
**Repository:** https://github.com/courselabs/azure

**Need Help?** Open an issue in the repository or reach out to the Azure community!

---

**COMPLETED - Your AZ-204 Study Guide is Ready!**
