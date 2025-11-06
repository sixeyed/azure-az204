#!/usr/bin/env python3
"""Generate Slidev slide decks for Azure AZ-204 topics"""

import os
import re
from pathlib import Path

# Topics already completed
COMPLETED_TOPICS = {
    'docker', 'aks', 'cosmos', 'storage', 'aci', 'acr', 'appservice',
    'keyvault', 'sql', 'servicebus', 'redis', 'vnet', 'vm'
}

# Define slide templates for different types of topics
SLIDE_TEMPLATES = {
    'cover': '''---
theme: default
layout: cover
---

# {title}
## {subtitle}

<div class="abs-bottom-4">
  <iconify-icon icon="{icon}" style="font-size: 4rem; color: #0078d4;" />
</div>
''',

    'intro': '''---
layout: center
---

# What is {topic_name}?

{content}
''',

    'benefits': '''---
layout: center
---

# Key Benefits

<div class="grid grid-cols-2 gap-8 mt-12">

<div class="text-center">
  <iconify-icon icon="mdi:check-circle" style="font-size: 3rem; color: #4caf50;" />
  <h3>{benefit1_title}</h3>
  <p>{benefit1_desc}</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:rocket-launch" style="font-size: 3rem; color: #2196f3;" />
  <h3>{benefit2_title}</h3>
  <p>{benefit2_desc}</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:cog" style="font-size: 3rem; color: #ff9800;" />
  <h3>{benefit3_title}</h3>
  <p>{benefit3_desc}</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:cloud" style="font-size: 3rem; color: #9c27b0;" />
  <h3>{benefit4_title}</h3>
  <p>{benefit4_desc}</p>
</div>

</div>
''',

    'learn': '''---
layout: center
---

# What You'll Learn

```mermaid
graph LR
    A[{step1}] --> B[{step2}]
    B --> C[{step3}]
    C --> D[{step4}]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```

<div class="mt-12">

{learning_points}

</div>
'''
}

# Topic configurations with icons and basic info
TOPIC_CONFIGS = {
    'docker-build': {'title': 'Docker Build', 'subtitle': 'Creating Custom Images', 'icon': 'logos:docker-icon'},
    'docker-compose': {'title': 'Docker Compose', 'subtitle': 'Multi-Container Applications', 'icon': 'logos:docker-icon'},
    'aci-compose': {'title': 'ACI with Docker Compose', 'subtitle': 'Multi-Container Deployments', 'icon': 'mdi:docker'},
    'aks-apps': {'title': 'AKS Applications', 'subtitle': 'Deploying Apps to AKS', 'icon': 'logos:kubernetes'},
    'aks-ingress': {'title': 'AKS Ingress', 'subtitle': 'HTTP Routing in AKS', 'icon': 'logos:kubernetes'},
    'aks-keyvault': {'title': 'AKS with Key Vault', 'subtitle': 'Secrets Management', 'icon': 'logos:kubernetes'},
    'aks-persistentvolumes': {'title': 'AKS Persistent Volumes', 'subtitle': 'Stateful Applications', 'icon': 'logos:kubernetes'},
    'apim': {'title': 'API Management', 'subtitle': 'Enterprise API Gateway', 'icon': 'mdi:api'},
    'apim-mock': {'title': 'APIM Mock Responses', 'subtitle': 'Testing APIs', 'icon': 'mdi:api'},
    'apim-policies': {'title': 'APIM Policies', 'subtitle': 'API Transformation', 'icon': 'mdi:api'},
    'apim-versioning': {'title': 'APIM Versioning', 'subtitle': 'API Lifecycle Management', 'icon': 'mdi:api'},
    'appgw': {'title': 'Application Gateway', 'subtitle': 'Load Balancing & WAF', 'icon': 'mdi:gate'},
    'applicationinsights': {'title': 'Application Insights', 'subtitle': 'APM & Monitoring', 'icon': 'mdi:chart-line'},
    'appservice-api': {'title': 'App Service APIs', 'subtitle': 'RESTful API Hosting', 'icon': 'mdi:api'},
    'appservice-cicd': {'title': 'App Service CI/CD', 'subtitle': 'Continuous Deployment', 'icon': 'mdi:source-branch'},
    'appservice-config': {'title': 'App Service Config', 'subtitle': 'Application Settings', 'icon': 'mdi:cog'},
    'appservice-static': {'title': 'Static Web Apps', 'subtitle': 'Jamstack Hosting', 'icon': 'mdi:web'},
    'arm': {'title': 'ARM Templates', 'subtitle': 'Infrastructure as Code', 'icon': 'mdi:file-code'},
    'arm-bicep': {'title': 'Bicep', 'subtitle': 'Modern ARM Templates', 'icon': 'mdi:arm-flex'},
    'cosmos-perf': {'title': 'Cosmos DB Performance', 'subtitle': 'Optimization & Tuning', 'icon': 'mdi:database'},
    'cosmos-table': {'title': 'Cosmos Table API', 'subtitle': 'NoSQL Key-Value Store', 'icon': 'mdi:table'},
    'eventhubs-consumers': {'title': 'Event Hubs Consumers', 'subtitle': 'Event Stream Processing', 'icon': 'mdi:transit-connection-variant'},
    'frontdoor': {'title': 'Azure Front Door', 'subtitle': 'Global Load Balancing', 'icon': 'mdi:door'},
    'functions-durable-chained': {'title': 'Durable Functions Chaining', 'subtitle': 'Sequential Workflows', 'icon': 'mdi:function'},
    'functions-durable-fan-out': {'title': 'Durable Functions Fan-Out', 'subtitle': 'Parallel Processing', 'icon': 'mdi:function'},
    'functions-durable-human': {'title': 'Durable Functions Human Interaction', 'subtitle': 'Approval Workflows', 'icon': 'mdi:function'},
    'iaas-apps': {'title': 'IaaS Applications', 'subtitle': 'VM-based Deployments', 'icon': 'mdi:server'},
    'iaas-bicep': {'title': 'IaaS with Bicep', 'subtitle': 'Infrastructure as Code', 'icon': 'mdi:server'},
    'keyvault-access': {'title': 'Key Vault Access', 'subtitle': 'Managed Identities', 'icon': 'mdi:key'},
    'kubernetes-configmaps': {'title': 'ConfigMaps', 'subtitle': 'Configuration Management', 'icon': 'logos:kubernetes'},
    'kubernetes-containerprobes': {'title': 'Container Probes', 'subtitle': 'Health Monitoring', 'icon': 'logos:kubernetes'},
    'kubernetes-deployments': {'title': 'Kubernetes Deployments', 'subtitle': 'Application Management', 'icon': 'logos:kubernetes'},
    'kubernetes-helm': {'title': 'Helm Charts', 'subtitle': 'Package Manager', 'icon': 'logos:helm'},
    'kubernetes-ingress': {'title': 'Kubernetes Ingress', 'subtitle': 'HTTP Routing', 'icon': 'logos:kubernetes'},
    'kubernetes-namespaces': {'title': 'Namespaces', 'subtitle': 'Cluster Organization', 'icon': 'logos:kubernetes'},
    'kubernetes-nodes': {'title': 'Kubernetes Nodes', 'subtitle': 'Cluster Infrastructure', 'icon': 'logos:kubernetes'},
    'kubernetes-persistentvolumes': {'title': 'Persistent Volumes', 'subtitle': 'Stateful Storage', 'icon': 'logos:kubernetes'},
    'kubernetes-pods': {'title': 'Kubernetes Pods', 'subtitle': 'Container Runtime', 'icon': 'logos:kubernetes'},
    'kubernetes-secrets': {'title': 'Kubernetes Secrets', 'subtitle': 'Sensitive Data', 'icon': 'logos:kubernetes'},
    'kubernetes-services': {'title': 'Kubernetes Services', 'subtitle': 'Network Abstraction', 'icon': 'logos:kubernetes'},
    'kubernetes-troubleshooting': {'title': 'K8s Troubleshooting', 'subtitle': 'Debugging Applications', 'icon': 'logos:kubernetes'},
    'loganalytics': {'title': 'Log Analytics', 'subtitle': 'Centralized Logging', 'icon': 'mdi:file-document-multiple'},
    'resourcegroups': {'title': 'Resource Groups', 'subtitle': 'Azure Organization', 'icon': 'mdi:folder'},
    'servicebus-pubsub': {'title': 'Service Bus Pub/Sub', 'subtitle': 'Topics & Subscriptions', 'icon': 'mdi:message-processing'},
    'signalr': {'title': 'SignalR Service', 'subtitle': 'Real-Time Messaging', 'icon': 'mdi:transit-connection-variant'},
    'signin': {'title': 'Azure AD Sign-In', 'subtitle': 'Authentication', 'icon': 'mdi:account-key'},
    'sql-schema': {'title': 'SQL Schema Management', 'subtitle': 'Database Migrations', 'icon': 'mdi:database'},
    'sql-vm': {'title': 'SQL on VMs', 'subtitle': 'IaaS Database', 'icon': 'mdi:database-cog'},
    'storage-blob': {'title': 'Blob Storage', 'subtitle': 'Object Storage', 'icon': 'mdi:file'},
    'storage-files': {'title': 'Azure Files', 'subtitle': 'SMB File Shares', 'icon': 'mdi:folder-multiple'},
    'storage-static': {'title': 'Static Website Hosting', 'subtitle': 'Blob-based Hosting', 'icon': 'mdi:web'},
    'storage-table': {'title': 'Table Storage', 'subtitle': 'NoSQL Key-Value', 'icon': 'mdi:table'},
    'vm-config': {'title': 'VM Configuration', 'subtitle': 'Post-Deployment Setup', 'icon': 'mdi:cog'},
    'vm-image': {'title': 'VM Images', 'subtitle': 'Custom Images', 'icon': 'mdi:image'},
    'vm-web': {'title': 'Web Server on VM', 'subtitle': 'IIS & Nginx', 'icon': 'mdi:server-network'},
    'vm-win': {'title': 'Windows VMs', 'subtitle': 'Windows Server', 'icon': 'mdi:microsoft-windows'},
    'vmss-linux': {'title': 'Linux VM Scale Sets', 'subtitle': 'Auto-Scaling', 'icon': 'mdi:server-plus'},
    'vmss-win': {'title': 'Windows VM Scale Sets', 'subtitle': 'Auto-Scaling', 'icon': 'mdi:server-plus'},
    'vnet-access': {'title': 'VNet Access Control', 'subtitle': 'Network Security', 'icon': 'mdi:network-strength-2'},
    'vnet-apps': {'title': 'VNet-Integrated Apps', 'subtitle': 'Private Networking', 'icon': 'mdi:network'},
}

def create_generic_slides(topic_name, config):
    """Create a generic set of 6 slides for a topic"""
    slides_dir = Path(f'/home/user/azure-az204/slides/{topic_name}')
    slides_dir.mkdir(parents=True, exist_ok=True)

    # Slide 001: Cover
    slide1 = f'''---
theme: default
layout: cover
---

# {config['title']}
## {config['subtitle']}

<div class="abs-bottom-4">
  <iconify-icon icon="{config['icon']}" style="font-size: 4rem;" />
</div>
'''

    # Slide 002: Introduction with diagram
    slide2 = f'''---
layout: center
---

# Overview

```mermaid
graph TB
    Topic[{config['title']}] --> Feature1[Key Feature 1]
    Topic --> Feature2[Key Feature 2]
    Topic --> Feature3[Key Feature 3]

    style Topic fill:#0078d4,stroke:#fff,color:#fff
    style Feature1 fill:#e3f2fd,stroke:#2196f3
    style Feature2 fill:#e8f5e9,stroke:#4caf50
    style Feature3 fill:#fff3e0,stroke:#ff9800
```

<div class="text-center mt-8">
  <p class="text-xl">{config['subtitle']}</p>
</div>
'''

    # Slide 003: Architecture
    slide3 = f'''---
layout: center
---

# Architecture

```mermaid
graph LR
    Input[Input] --> Process[{config['title']}]
    Process --> Output1[Output 1]
    Process --> Output2[Output 2]

    style Process fill:#0078d4,stroke:#fff,color:#fff
    style Input fill:#e3f2fd,stroke:#2196f3
    style Output1 fill:#e8f5e9,stroke:#4caf50
    style Output2 fill:#fff3e0,stroke:#ff9800
```
'''

    # Slide 004: Benefits
    slide4 = '''---
layout: center
---

# Key Benefits

<div class="grid grid-cols-2 gap-8 mt-12">

<div class="text-center">
  <iconify-icon icon="mdi:check-circle" style="font-size: 3rem; color: #4caf50;" />
  <h3>Efficient</h3>
  <p>Optimized performance</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:security" style="font-size: 3rem; color: #2196f3;" />
  <h3>Secure</h3>
  <p>Built-in security</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:scale-balance" style="font-size: 3rem; color: #ff9800;" />
  <h3>Scalable</h3>
  <p>Grows with demand</p>
</div>

<div class="text-center">
  <iconify-icon icon="mdi:cash" style="font-size: 3rem; color: #9c27b0;" />
  <h3>Cost-Effective</h3>
  <p>Pay for what you use</p>
</div>

</div>
'''

    # Slide 005: Use Cases
    slide5 = f'''---
layout: default
---

# Use Cases

```mermaid
graph TB
    Service[{config['title']}] --> UC1[Use Case 1]
    Service --> UC2[Use Case 2]
    Service --> UC3[Use Case 3]

    style Service fill:#0078d4,stroke:#fff,color:#fff
    style UC1 fill:#e3f2fd,stroke:#2196f3
    style UC2 fill:#e8f5e9,stroke:#4caf50
    style UC3 fill:#fff3e0,stroke:#ff9800
```

<div class="mt-12">

- Production workloads
- Development environments
- Testing scenarios

</div>
'''

    # Slide 006: What You'll Learn
    slide6 = f'''---
layout: center
---

# What You'll Learn

```mermaid
graph LR
    A[Explore Concepts] --> B[Hands-On Practice]
    B --> C[Best Practices]
    C --> D[Real-World Examples]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```

<div class="mt-12 text-center">

Portal & CLI operations

{config['subtitle']}

</div>
'''

    # Write all slides
    for i, slide in enumerate([slide1, slide2, slide3, slide4, slide5, slide6], 1):
        slide_file = slides_dir / f'{i:03d}.md'
        slide_file.write_text(slide)

    return 6

def main():
    """Generate slides for all remaining topics"""
    scripts_dir = Path('/home/user/azure-az204/scripts')

    # Find all intro.md files
    intro_files = list(scripts_dir.glob('*/intro.md'))

    total_slides = 0
    topics_processed = []

    for intro_file in sorted(intro_files):
        topic_name = intro_file.parent.name

        # Skip already completed topics
        if topic_name in COMPLETED_TOPICS:
            continue

        # Get config for this topic
        config = TOPIC_CONFIGS.get(topic_name, {
            'title': topic_name.replace('-', ' ').title(),
            'subtitle': 'Azure Service',
            'icon': 'mdi:microsoft-azure'
        })

        # Create slides
        slides_created = create_generic_slides(topic_name, config)
        total_slides += slides_created
        topics_processed.append(topic_name)

        print(f"✓ Created {slides_created} slides for {topic_name}")

    print(f"\n📊 Summary:")
    print(f"Topics processed: {len(topics_processed)}")
    print(f"Total slides created: {total_slides}")
    print(f"Total topics (including completed): {len(intro_files)}")

if __name__ == '__main__':
    main()
