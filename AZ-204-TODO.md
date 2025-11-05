# AZ-204 Course - TODO List

## Overview

This document tracks outstanding tasks to complete the AZ-204 exam coverage for this training course. The course currently has **excellent coverage (85-90%)** of AZ-204 topics, but there are some gaps and opportunities for enhancement.

**Last Updated:** November 2025

---

## Priority 1: Missing AZ-204 Exam Topics (Critical)

### 1. Event Grid (High Priority)
**Status:** ❌ No dedicated lab exists
**AZ-204 Domain:** Connect to and Consume Azure Services (20-25%)

**Required:**
- [ ] Create new lab: `labs/eventgrid/`
  - [ ] Basic: Create Event Grid topic, subscriptions, event handlers
  - [ ] AZ-204.md: Event schemas, filtering, retry policies, webhook validation
  - [ ] Integrate with Functions, Service Bus, Event Hubs
  - [ ] Dead-letter configuration
  - [ ] System topics (Blob, Azure subscriptions)

**Exam Skills:**
- Implement solutions that use Azure Event Grid
- Create custom topics and subscriptions
- Event filtering and routing
- Webhook validation

### 2. Azure Container Apps (Medium-High Priority)
**Status:** ❌ Not covered
**AZ-204 Domain:** Develop Azure Compute Solutions (25-30%)

**Required:**
- [ ] Create new lab: `labs/container-apps/`
  - [ ] Deploy containerized app to Container Apps
  - [ ] Configure scaling (CPU, HTTP, custom)
  - [ ] Multiple revisions and traffic splitting
  - [ ] Dapr integration basics
  - [ ] AZ-204.md: Container Apps vs ACI vs AKS comparison

**Note:** This is a NEW AZ-204 topic as of 2024. We have ACI and AKS labs, but Container Apps specifically is missing.

### 3. Microsoft Graph Integration (Medium Priority)
**Status:** ❌ Not covered
**AZ-204 Domain:** Implement Azure Security (15-20%)

**Required:**
- [ ] Create new lab: `labs/microsoft-graph/`
  - [ ] Authentication with Microsoft Identity platform
  - [ ] Query user data, calendar, mail
  - [ ] Permissions and consent
  - [ ] AZ-204.md: Common Graph API operations for AZ-204

**Exam Skills:**
- Implement solutions that interact with Microsoft Graph
- Understand permission types (delegated vs application)

### 4. Azure CDN (Medium Priority)
**Status:** ⚠️ Mentioned in storage-static but not dedicated lab
**AZ-204 Domain:** Monitor, Troubleshoot, and Optimize (5-10%)

**Required:**
- [ ] Create new lab: `labs/cdn/`
  - [ ] Create CDN profile and endpoints
  - [ ] Configure caching rules
  - [ ] Purge and pre-load content
  - [ ] Custom domains and HTTPS
  - [ ] AZ-204.md: CDN for static content optimization

### 5. Advanced Application Insights (Medium Priority)
**Status:** ⚠️ Basic lab exists but needs AZ-204 enhancement
**AZ-204 Domain:** Monitor, Troubleshoot, and Optimize (5-10%)

**Required:**
- [ ] Enhance `labs/applicationinsights/`
  - [ ] Create AZ-204.md with:
    - Custom telemetry and events
    - Dependency tracking
    - Availability tests (web tests)
    - Application Map
    - Live Metrics Stream
    - Alerts and action groups
    - Sampling and filtering

### 6. Azure Cache for Redis (Low Priority)
**Status:** ✅ Basic lab exists at `labs/redis/`
**AZ-204 Domain:** Monitor, Troubleshoot, and Optimize (5-10%)

**Required:**
- [ ] Create `labs/redis/AZ-204.md`
  - [ ] Cache-aside pattern
  - [ ] Session state storage
  - [ ] Output caching
  - [ ] Redis data types and operations
  - [ ] Scaling and clustering

---

## Priority 2: Enhance Existing Labs with AZ-204.md Files

### Core Compute Labs

- [x] ✅ `labs/functions/http/AZ-204.md` - COMPLETED
- [ ] `labs/functions/timer/AZ-204.md`
- [ ] `labs/functions/blob/AZ-204.md`
- [ ] `labs/functions-durable/AZ-204.md` (consolidated for all durable patterns)
- [ ] `labs/appservice/AZ-204.md`
  - Deployment slots
  - Auto-scaling
  - App Service configuration
  - Deployment options (Git, ZIP, Docker)
- [ ] `labs/appservice-cicd/AZ-204.md`
  - GitHub Actions integration
  - Azure DevOps pipelines
- [ ] `labs/aci/AZ-204.md`
  - Container groups
  - Environment variables
  - Persistent storage with Azure Files
- [ ] `labs/acr/AZ-204.md`
  - Build images in ACR
  - Geo-replication
  - Webhooks
  - Tasks and automated builds

### Core Storage Labs

- [x] ✅ `labs/storage-blob/AZ-204.md` - COMPLETED
- [x] ✅ `labs/cosmos/AZ-204.md` - COMPLETED
- [ ] `labs/storage/AZ-204.md` (base storage account)
  - Storage redundancy options
  - Storage account types
  - Access keys and SAS
- [ ] `labs/storage-table/AZ-204.md`
  - Table Storage SDK operations
  - Query syntax
  - When to use Table vs Cosmos DB
- [ ] `labs/storage-files/AZ-204.md`
  - Azure Files vs Blob Storage
  - SMB protocol
  - Mounting to VMs

### Core Security Labs

- [x] ✅ `labs/keyvault/AZ-204.md` - COMPLETED
- [ ] `labs/keyvault-access/AZ-204.md`
  - Managed Identity scenarios
  - RBAC vs Access Policies
- [ ] `labs/signin/AZ-204.md`
  - Microsoft Identity platform
  - Azure AD B2C basics
  - OAuth 2.0 flows
  - MSAL SDK usage

### Core Messaging Labs

- [x] ✅ `labs/servicebus/AZ-204.md` - COMPLETED
- [ ] `labs/servicebus-pubsub/AZ-204.md`
  - Topics and subscriptions deep dive
  - Message filtering
- [ ] `labs/eventhubs/AZ-204.md`
  - Event Hubs basics
  - Partitions and consumer groups
  - Capture to storage
- [ ] `labs/eventhubs-consumers/AZ-204.md`
  - Event processor host
  - Checkpointing

### Core API/Integration Labs

- [x] ✅ `labs/apim/AZ-204.md` - COMPLETED
- [ ] `labs/apim-policies/AZ-204.md`
  - Policy examples for common scenarios
  - Custom policies
- [ ] `labs/apim-versioning/AZ-204.md`
  - Versioning strategies
  - Revisions workflow

---

## Priority 3: Labs Not Needed for AZ-204 (Optional/Supplementary)

These labs are valuable for general Azure knowledge but not required for AZ-204 exam:

### Kubernetes/AKS Labs (Out of Scope)
- `labs/kubernetes/` - Core Kubernetes concepts
- `labs/aks/` - AKS cluster management
- `labs/aks-apps/` - Deploying to AKS
- `labs/aks-ingress/` - Ingress controllers
- `labs/aks-keyvault/` - Key Vault integration
- `labs/aks-persistentvolumes/` - Storage in AKS

**Recommendation:** Keep these labs but mark them as "Supplementary - Not required for AZ-204"

### IaaS/VM Labs (Out of Scope)
- `labs/vm/` - Virtual machines
- `labs/vm-config/` - VM configuration
- `labs/vm-image/` - Custom images
- `labs/vm-web/` - Web apps on VMs
- `labs/vm-win/` - Windows VMs
- `labs/vmss-linux/` - VM Scale Sets Linux
- `labs/vmss-win/` - VM Scale Sets Windows
- `labs/iaas-apps/` - IaaS applications
- `labs/iaas-bicep/` - IaaS with Bicep

**Recommendation:** Mark as "Supplementary - Useful for understanding IaaS vs PaaS trade-offs"

### Infrastructure as Code (Supplementary)
- `labs/arm/` - ARM templates
- `labs/arm-bicep/` - Bicep

**Recommendation:** Keep as supplementary. AZ-204 doesn't focus on ARM/Bicep, but it's useful context.

### Networking Labs (Supplementary)
- `labs/vnet/` - Virtual networks
- `labs/vnet-access/` - VNet integration
- `labs/vnet-apps/` - Apps in VNets
- `labs/appgw/` - Application Gateway
- `labs/frontdoor/` - Azure Front Door

**Recommendation:** Keep as supplementary. Some VNet integration concepts are relevant to AZ-204, but not exam-critical.

### SQL/Database Labs (Supplementary)
- `labs/sql/` - Azure SQL Database
- `labs/sql-schema/` - SQL schema management
- `labs/sql-vm/` - SQL on VMs

**Recommendation:** Keep as supplementary. AZ-204 focuses on Cosmos DB, not Azure SQL.

### Other Supplementary
- `labs/loganalytics/` - Log Analytics (useful for monitoring but not exam-critical)
- `labs/resourcegroups/` - Resource group management (basic Azure concept)
- `labs/signalr/` - SignalR (covered in Functions lab)

---

## Priority 4: Documentation Enhancements

### README Updates

- [ ] Update main `README.md` with:
  - [ ] Clear AZ-204 focus statement
  - [ ] Link to `AZ-204-CURRICULUM.md`
  - [ ] Recommended learning path for AZ-204 prep
  - [ ] Prerequisites (Azure subscription, tools)
  - [ ] Estimated time to complete

### Lab Organization

- [ ] Create `labs/README.md` with:
  - [ ] Index of all labs
  - [ ] Which labs are AZ-204 core vs supplementary
  - [ ] Recommended order for AZ-204 preparation
  - [ ] Lab difficulty levels

### Study Guides

- [ ] Create `AZ-204-STUDY-GUIDE.md`:
  - [ ] Week-by-week study plan
  - [ ] Mapping labs to exam domains
  - [ ] Additional resources (Microsoft Learn paths)
  - [ ] Practice exam tips
  - [ ] Common exam scenarios

---

## Priority 5: Code Samples and Solutions

### .NET SDK Examples
- [ ] Create `src/az204-samples/` directory with:
  - [ ] Blob Storage SDK examples
  - [ ] Cosmos DB SDK examples
  - [ ] Service Bus SDK examples
  - [ ] Key Vault SDK examples
  - [ ] Function bindings examples
  - [ ] APIM policy examples

### Python SDK Examples (Optional)
- [ ] Add Python equivalents for key scenarios
- [ ] Multi-language support for diverse learners

---

## Priority 6: Practice Scenarios

### Real-World Integration Labs

- [ ] Create `labs/az204-project-1/` - E-commerce Backend
  - Combines: Functions, Cosmos DB, Service Bus, Key Vault, App Insights
  - End-to-end scenario for order processing

- [ ] Create `labs/az204-project-2/` - Document Processing Pipeline
  - Combines: Blob Storage, Functions, Cosmos DB, Event Grid
  - Automated document processing workflow

- [ ] Create `labs/az204-project-3/` - API Gateway Pattern
  - Combines: APIM, Functions, Service Bus, Key Vault
  - Secure API with authentication and rate limiting

- [ ] Create `labs/az204-project-4/` - Monitoring and Diagnostics
  - Combines: Application Insights, Log Analytics, Alerts
  - Full observability stack

---

## Summary Statistics

### Current Status

| Category | Status |
|----------|--------|
| **Total Labs** | 65 |
| **AZ-204 Core Labs** | 37+ (57%) |
| **AZ-204 Supplementary** | 12 (18%) |
| **Out of Scope** | 16 (25%) |
| **AZ-204.md Created** | 6 so far |
| **AZ-204.md Needed** | ~25 more |

### Coverage by Exam Domain

| Domain | Coverage | Status |
|--------|----------|--------|
| Develop Azure Compute Solutions (25-30%) | 90% | ⚠️ Missing: Container Apps |
| Develop for Azure Storage (15-20%) | 95% | ✅ Excellent |
| Implement Azure Security (15-20%) | 75% | ⚠️ Missing: Microsoft Graph, enhance App Insights |
| Monitor, Troubleshoot, Optimize (5-10%) | 70% | ⚠️ Missing: CDN, enhance App Insights/Redis |
| Connect to Azure Services (20-25%) | 85% | ⚠️ Missing: Event Grid |

### Overall AZ-204 Readiness: 85-90%

---

## Recommended Action Plan

### Phase 1: Critical Gaps (1-2 weeks)
1. Create Event Grid lab (most critical missing topic)
2. Create Container Apps lab (new AZ-204 requirement)
3. Create Microsoft Graph lab
4. Enhance Application Insights lab with AZ-204.md

### Phase 2: Complete AZ-204.md Files (2-3 weeks)
1. Create AZ-204.md for all Function labs
2. Create AZ-204.md for App Service labs
3. Create AZ-204.md for remaining storage labs
4. Create AZ-204.md for messaging labs

### Phase 3: Integration Projects (1-2 weeks)
1. Create 4 end-to-end project labs
2. Combine multiple services in realistic scenarios

### Phase 4: Documentation (1 week)
1. Update all README files
2. Create study guide
3. Create learning path document

---

## Notes

- **Priority Focus:** Complete AZ-204.md files for existing labs before creating new labs
- **Time Estimate:** 6-8 weeks to complete all priorities 1-4
- **Maintainability:** Each AZ-204.md should be standalone and exam-focused
- **Quality over Quantity:** Better to have 30 high-quality labs than 65 mixed-quality ones

---

## Contributing

To contribute to completing this TODO list:
1. Pick a task from Priority 1 or 2
2. Follow the existing AZ-204.md format (see `storage-blob`, `functions/http`, `keyvault`, `cosmos`, `servicebus`, `apim`)
3. Include exam tips, common scenarios, and best practices
4. Update this TODO when tasks are completed

---

**Document Version:** 1.0
**Last Review:** November 2025
**Next Review:** After Phase 1 completion
