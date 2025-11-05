# Azure AZ-204 Developer Training Course

A comprehensive, hands-on training course for the **Microsoft Certified: Azure Developer Associate (AZ-204)** certification exam. This course provides practical labs covering all exam domains with extensive Azure CLI and SDK examples.

## 🎯 Course Overview

This repository contains **65+ hands-on labs** designed to prepare you for the AZ-204 certification exam. Each core lab includes:
- **README.md**: Introductory exercises and fundamental concepts
- **AZ-204.md**: Advanced exam-specific exercises, SDK examples, and exam tips

**Current AZ-204 Coverage: 95%+** of all exam topics

## 📚 What You'll Learn

The AZ-204 exam tests your ability to design, build, test, and maintain cloud applications and services on Microsoft Azure. This course covers all five exam domains:

### 1. Develop Azure Compute Solutions (25-30%)
- Azure Functions (HTTP, Timer, Blob triggers, Durable Functions)
- Azure App Service (Web Apps, deployment slots, auto-scaling)
- Azure Container Instances and Azure Container Apps
- Container registries and container management

### 2. Develop for Azure Storage (15-20%)
- Azure Blob Storage (lifecycle management, SAS tokens, metadata)
- Azure Cosmos DB (consistency levels, partitioning, change feed)
- Azure Table Storage and Azure Files
- Storage account configuration and security

### 3. Implement Azure Security (15-20%)
- Azure Key Vault (secrets, keys, certificates)
- Managed Identities (system-assigned and user-assigned)
- Microsoft Identity Platform and Microsoft Graph API
- Secure application configuration

### 4. Monitor, Troubleshoot, and Optimize (5-10%)
- Application Insights (custom telemetry, availability tests)
- Azure Cache for Redis (caching patterns)
- Performance optimization strategies

### 5. Connect to and Consume Azure Services (20-25%)
- Azure Event Grid (custom topics, event filtering)
- Azure Event Hubs (partitions, Event Processor)
- Azure Service Bus (queues, topics, sessions)
- Azure API Management (policies, versioning)

## 🚀 Quick Start

### Prerequisites

- **Azure Subscription**: [Create a free account](https://azure.microsoft.com/free/)
- **Azure CLI**: [Install instructions](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- **Development Tools**:
  - [.NET 6 SDK](https://dotnet.microsoft.com/download) or [.NET 8 SDK](https://dotnet.microsoft.com/download)
  - [Python 3.8+](https://www.python.org/downloads/) (optional)
  - [Visual Studio Code](https://code.visualstudio.com/) (recommended)
  - [Docker Desktop](https://www.docker.com/products/docker-desktop) (for container labs)
  - [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

### Setup

```bash
# Clone the repository
git clone https://github.com/sixeyed/azure-az204.git
cd azure-az204

# Login to Azure
az login

# Set your default subscription (if you have multiple)
az account set --subscription "<subscription-id>"

# Verify your setup
az account show
```

## 📖 Getting Started

### For AZ-204 Exam Preparation

1. **Start Here**: Read [AZ-204-CURRICULUM.md](AZ-204-CURRICULUM.md) for complete exam details
2. **Study Plan**: Follow [AZ-204-STUDY-GUIDE.md](AZ-204-STUDY-GUIDE.md) for a structured 6-8 week plan
3. **Learning Path**: See [AZ-204-LEARNING-PATH.md](AZ-204-LEARNING-PATH.md) for recommended lab order
4. **Lab Index**: Browse [labs/README.md](labs/README.md) for all available labs organized by topic

### Recommended Learning Sequence

**Week 1-2: Azure Compute**
- Functions (HTTP, Timer, Blob triggers)
- App Service (deployment, slots, scaling)
- Container Apps and ACI

**Week 3-4: Azure Storage & Data**
- Blob Storage (advanced features)
- Cosmos DB (partitioning, consistency)
- Table Storage and Azure Files

**Week 5: Security**
- Key Vault (secrets, managed identities)
- Microsoft Graph API
- Authentication and authorization

**Week 6: Integration & Messaging**
- Event Grid (event-driven architecture)
- Event Hubs and Service Bus
- API Management

**Week 7-8: Monitoring & Review**
- Application Insights
- Redis Cache
- Practice exams and review

## 📂 Repository Structure

```
azure-az204/
├── README.md                          # This file
├── AZ-204-CURRICULUM.md               # Complete 2025 exam curriculum
├── AZ-204-STUDY-GUIDE.md             # Week-by-week study plan
├── AZ-204-LEARNING-PATH.md           # Recommended lab order
├── AZ-204-TODO.md                     # Outstanding items and future work
│
├── labs/                              # All hands-on labs
│   ├── README.md                      # Lab index and organization
│   │
│   ├── Core AZ-204 Labs/
│   │   ├── functions/                 # Azure Functions labs
│   │   │   ├── http/                  # HTTP trigger functions
│   │   │   │   ├── README.md          # Basic exercises
│   │   │   │   └── AZ-204.md         # Exam-specific exercises
│   │   │   ├── timer/                 # Timer trigger functions
│   │   │   ├── blob/                  # Blob trigger functions
│   │   │   └── ...                    # Other function triggers
│   │   │
│   │   ├── appservice/                # Azure App Service
│   │   ├── container-apps/            # Azure Container Apps
│   │   ├── aci/                       # Azure Container Instances
│   │   ├── acr/                       # Azure Container Registry
│   │   │
│   │   ├── storage-blob/              # Blob Storage
│   │   ├── storage-table/             # Table Storage
│   │   ├── storage-files/             # Azure Files
│   │   ├── cosmos/                    # Cosmos DB
│   │   │
│   │   ├── keyvault/                  # Azure Key Vault
│   │   ├── microsoft-graph/           # Microsoft Graph API
│   │   │
│   │   ├── eventgrid/                 # Event Grid
│   │   ├── eventhubs/                 # Event Hubs
│   │   ├── servicebus/                # Service Bus
│   │   ├── apim/                      # API Management
│   │   │
│   │   ├── applicationinsights/       # Application Insights
│   │   └── redis/                     # Azure Cache for Redis
│   │
│   └── Supplementary Labs/            # Additional Azure topics
│       ├── kubernetes/                # Kubernetes basics
│       ├── aks/                       # Azure Kubernetes Service
│       ├── vm/                        # Virtual Machines
│       └── ...                        # Other infrastructure topics
│
└── src/                               # Sample applications
    ├── asset-manager/                 # Sample .NET app
    └── ...                            # Other sample code
```

## 🎓 Course Features

### Comprehensive Coverage
- **65+ labs** covering Azure compute, storage, security, messaging, and monitoring
- **29+ AZ-204.md files** with exam-specific exercises and advanced topics
- **95%+ exam coverage** of official AZ-204 objectives

### Hands-On Learning
- Practical exercises using Azure CLI and Azure Portal
- SDK code examples in C# and Python
- Real-world scenarios and best practices
- Interactive challenges with hints and solutions

### Exam-Focused Content
- "AZ-204 Exam Tip" highlights throughout
- Common exam scenarios with solutions
- Decision matrices (when to use which service)
- Key concepts study points
- Sample questions and answers

### Progressive Difficulty
- **README.md**: Start with basics and fundamentals
- **AZ-204.md**: Progress to advanced exam topics
- Clear prerequisites and learning paths
- Self-paced with optional challenges

## 📊 Lab Categories

### Core AZ-204 Labs (37+ labs)
These labs directly cover AZ-204 exam topics and should be completed for exam preparation:

**Compute**: functions, appservice, container-apps, aci, acr, docker

**Storage**: storage, storage-blob, storage-table, storage-files, storage-static, cosmos (all variants)

**Security**: keyvault, keyvault-access, signin, microsoft-graph

**Monitoring**: applicationinsights, redis

**Integration**: eventgrid, eventhubs, servicebus, apim (all variants)

### Supplementary Labs (20+ labs)
These labs provide valuable Azure knowledge but are not specifically required for AZ-204:

**Kubernetes**: kubernetes, aks (all variants) - useful for understanding container orchestration

**IaaS**: vm, vmss, iaas-apps - understanding IaaS vs PaaS trade-offs

**Infrastructure**: arm, arm-bicep, vnet, resourcegroups - useful context

**Databases**: sql, sql-schema - AZ-204 focuses on Cosmos DB, not Azure SQL

## 💡 Study Tips

### For Exam Success

1. **Hands-On Practice**: Complete labs in Azure, don't just read
2. **Focus on SDK**: Know how to use Azure SDKs, not just CLI
3. **Understand "When to Use"**: Know which service to choose for scenarios
4. **Security First**: Managed identities, Key Vault, secure configuration
5. **Read Exam Tips**: Every "AZ-204 Exam Tip" is based on exam objectives
6. **Practice Scenarios**: Common exam scenarios are throughout the AZ-204.md files
7. **Use Free Tier**: Most labs can be done with free/low-cost resources

### Cost Management

- Use **Azure free account** for $200 credit
- Delete resource groups after each lab (`az group delete`)
- Use **consumption plans** for Functions (pay only when used)
- Use **Basic/Standard tiers** instead of Premium where possible
- Monitor your spending in Azure Portal

### Time Investment

- **Complete course**: 60-80 hours
- **Core AZ-204 labs only**: 40-50 hours
- **Review and practice**: 20-30 hours
- **Total preparation**: 80-110 hours recommended

## 🔗 Additional Resources

### Official Microsoft Resources
- [AZ-204 Exam Page](https://learn.microsoft.com/en-us/certifications/exams/az-204/)
- [Official Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204)
- [Microsoft Learn AZ-204 Path](https://learn.microsoft.com/en-us/certifications/azure-developer/)
- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)

### Practice Exams
- [Microsoft Official Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/az-204/practice/assessment)
- [MeasureUp Practice Tests](https://www.measureup.com/microsoft-practice-test-az-204-developing-solutions-for-microsoft-azure.html)

### Community Resources
- [Azure Developer Community](https://techcommunity.microsoft.com/t5/azure-developer-community/ct-p/AzureDevCommunity)
- [Azure Friday YouTube Channel](https://www.youtube.com/c/AzureFriday)
- [Azure Tips and Tricks](https://microsoft.github.io/AzureTipsAndTricks/)

## 🤝 Contributing

Contributions are welcome! If you find issues or want to add content:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please follow the existing format for labs:
- README.md for basic/introductory content
- AZ-204.md for exam-specific content
- Include CLI examples and SDK code where appropriate
- Add "AZ-204 Exam Tip" highlights for important concepts

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Microsoft Azure documentation and samples
- Azure community contributors
- AZ-204 exam candidates who provided feedback

## 📧 Questions?

- **Issues**: Use GitHub Issues for bug reports or questions
- **Discussions**: Use GitHub Discussions for general questions

---

**Ready to start?** Head to [AZ-204-STUDY-GUIDE.md](AZ-204-STUDY-GUIDE.md) for your personalized study plan!

**Good luck with your AZ-204 certification!** 🎉
