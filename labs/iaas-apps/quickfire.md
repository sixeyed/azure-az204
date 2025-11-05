# IaaS Application Deployment - Quickfire Questions

## Question 1
What is IaaS (Infrastructure as a Service)?

- A) Software service
- B) Cloud computing model providing virtualized computing resources (VMs, storage, networking)
- C) Application platform
- D) Database service

**Answer: B**
IaaS provides infrastructure components as a service, offering maximum control and flexibility.

---

## Question 2
What are advantages of IaaS for applications?

- A) No benefits
- B) Full OS control, custom configurations, legacy application support
- C) Only cost savings
- D) No management needed

**Answer: B**
IaaS enables running applications requiring specific OS versions, custom software, or kernel modifications.

---

## Question 3
What are disadvantages of IaaS vs PaaS?

- A) No disadvantages
- B) Requires more management (patching, scaling, backups)
- C) Always cheaper
- D) Better performance always

**Answer: B**
IaaS requires managing OS, patches, scaling, backups—responsibilities handled by PaaS.

---

## Question 4
How do you deploy multi-tier applications on IaaS?

- A) Single VM only
- B) Multiple VMs/VMSS across subnets (web, app, data tiers) with load balancers
- C) Not possible
- D) One tier only

**Answer: B**
Deploy tiers separately: web tier (VMSS + LB), app tier (VMSS + internal LB), database tier.

---

## Question 5
What is the typical network architecture for IaaS apps?

- A) Public internet only
- B) VNet with subnets per tier, NSGs for security, load balancers for distribution
- C) No networking
- D) Single flat network

**Answer: B**
Segmented network: public subnet for web tier, private subnets for app/data with NSG controls.

---

## Question 6
How do you achieve high availability for IaaS applications?

- A) Single VM
- B) Availability Sets/Zones, VMSS, load balancers, geo-redundant storage
- C) No HA possible
- D) Manual failover only

**Answer: B**
Combine multiple availability features for comprehensive HA and DR strategies.

---

## Question 7
What deployment automation options exist for IaaS?

- A) Manual only
- B) ARM/Bicep templates, Terraform, Ansible, Azure DevOps pipelines
- C) Not possible
- D) Portal only

**Answer: B**
Multiple IaC and automation tools for repeatable, version-controlled deployments.

---

## Question 8
How do you manage secrets in IaaS applications?

- A) Hardcode in config
- B) Azure Key Vault with VM managed identity
- C) Plain text files
- D) Environment variables only

**Answer: B**
Key Vault provides secure secret storage; managed identity enables passwordless access.

---

## Question 9
What monitoring strategy should you use for IaaS apps?

- A) No monitoring
- B) Azure Monitor (infrastructure), Application Insights (application), Log Analytics (logs)
- C) Only basic metrics
- D) Manual checks

**Answer: B**
Comprehensive monitoring: infrastructure metrics, application telemetry, centralized logging.

---

## Question 10
When should you choose IaaS over PaaS?

- A) Always IaaS
- B) Legacy migrations, custom OS/kernel, compliance requiring full control
- C) Always PaaS
- D) No difference

**Answer: B**
IaaS for specific OS versions, custom configurations, or applications incompatible with PaaS.
