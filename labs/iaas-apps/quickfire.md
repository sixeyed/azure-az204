# IaaS Application Deployment - Quickfire Questions

## Question 1
What is IaaS (Infrastructure as a Service)?


- A) Cloud computing model providing virtualized computing resources (VMs, storage, networking)
- B) Software service
- C) Database service
- D) Application platform

**Answer: A**
IaaS provides infrastructure components as a service, offering maximum control and flexibility.
---
## Question 2
What are advantages of IaaS for applications?


- A) Full OS control, custom configurations, legacy application support
- B) No benefits
- C) Only cost savings
- D) No management needed

**Answer: A**
IaaS enables running applications requiring specific OS versions, custom software, or kernel modifications.
---
## Question 3
What are disadvantages of IaaS vs PaaS?


- A) Better performance always
- B) No disadvantages
- C) Requires more management (patching, scaling, backups)
- D) Always cheaper

**Answer: C**
IaaS requires managing OS, patches, scaling, backups—responsibilities handled by PaaS.
---
## Question 4
How do you deploy multi-tier applications on IaaS?


- A) Not possible
- B) Multiple VMs/VMSS across subnets (web, app, data tiers) with load balancers
- C) Single VM only
- D) One tier only

**Answer: B**
Deploy tiers separately: web tier (VMSS + LB), app tier (VMSS + internal LB), database tier.
---
## Question 5
What is the typical network architecture for IaaS apps?


- A) VNet with subnets per tier, NSGs for security, load balancers for distribution
- B) Single flat network
- C) Public internet only
- D) No networking

**Answer: A**
Segmented network: public subnet for web tier, private subnets for app/data with NSG controls.
---
## Question 6
How do you achieve high availability for IaaS applications?


- A) Single VM
- B) Manual failover only
- C) Availability Sets/Zones, VMSS, load balancers, geo-redundant storage
- D) No HA possible

**Answer: C**
Combine multiple availability features for comprehensive HA and DR strategies.
---
## Question 7
What deployment automation options exist for IaaS?


- A) Not possible
- B) Portal only
- C) ARM/Bicep templates, Terraform, Ansible, Azure DevOps pipelines
- D) Manual only

**Answer: C**
Multiple IaC and automation tools for repeatable, version-controlled deployments.
---
## Question 8
How do you manage secrets in IaaS applications?


- A) Azure Key Vault with VM managed identity
- B) Plain text files
- C) Hardcode in config
- D) Environment variables only

**Answer: A**
Key Vault provides secure secret storage; managed identity enables passwordless access.
---
## Question 9
What monitoring strategy should you use for IaaS apps?


- A) No monitoring
- B) Only basic metrics
- C) Azure Monitor (infrastructure), Application Insights (application), Log Analytics (logs)
- D) Manual checks

**Answer: C**
Comprehensive monitoring: infrastructure metrics, application telemetry, centralized logging.
---
## Question 10
When should you choose IaaS over PaaS?


- A) No difference
- B) Always PaaS
- C) Always IaaS
- D) Legacy migrations, custom OS/kernel, compliance requiring full control

**Answer: D**
IaaS for specific OS versions, custom configurations, or applications incompatible with PaaS.