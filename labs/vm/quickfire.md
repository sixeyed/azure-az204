# Azure Virtual Machines - Quickfire Questions

## Question 1
What are Azure Virtual Machines?


- A) PaaS service
- B) Storage service
- C) Physical machines
- D) IaaS compute resources providing full OS control

**Answer: D**
VMs provide virtualized compute with full control over OS, ideal for custom configurations and migrations.
---
## Question 2
What VM sizes categories exist?


- A) Small and Large
- B) General purpose, Compute optimized, Memory optimized, Storage optimized, GPU
- C) Only one size
- D) Basic and Premium

**Answer: B**
Different VM series optimized for various workloads: balanced (D-series), CPU (F-series), memory (E-series), etc.
---
## Question 3
What are availability sets?


- A) VM collections
- B) Backup sets
- C) Storage sets
- D) Logical grouping providing fault/update domain distribution for high availability

**Answer: D**
Availability sets distribute VMs across fault domains (hardware) and update domains (maintenance) for 99.95% SLA.
---
## Question 4
What is an availability zone?


- A) Time zone
- B) Storage zone
- C) Physically separate datacenter within Azure region
- D) Network zone

**Answer: C**
Availability zones provide datacenter-level isolation within region for 99.99% SLA.
---
## Question 5
What is Azure Managed Disks?


- A) Physical disks
- B) Manual disk management
- C) Network disks
- D) Simplified disk management with automatic replication and no storage account management

**Answer: D**
Managed Disks handle storage accounts automatically, provide 99.999% availability, and simplify VM management.
---
## Question 6
What disk types are available?


- A) Ultra Disk, Premium SSD, Standard SSD, Standard HDD
- B) Fast and Slow
- C) Public and Private
- D) Only one type

**Answer: A**
Ultra (highest performance), Premium SSD (production), Standard SSD (web servers), Standard HDD (backup/dev).
---
## Question 7
Can you resize a VM?


- A) Only upgrade
- B) Never
- C) Yes, change VM size (may require restart)
- D) Only downgrade

**Answer: C**
VMs can be resized to different sizes within same family or different families (with restart).
---
## Question 8
What is Azure Bastion?


- A) Security group
- B) VPN
- C) Load balancer
- D) Managed service for secure RDP/SSH access without public IPs

**Answer: D**
Bastion provides secure browser-based RDP/SSH from Azure portal without exposing VMs to internet.
---
## Question 9
What is VM Scale Sets (VMSS)?


- A) Manual VM group
- B) Automated deployment and management of identical VMs with auto-scaling
- C) Network scaling
- D) Storage scaling

**Answer: B**
VMSS creates and manages group of load-balanced VMs with automatic scaling based on demand.
---
## Question 10
What extension capabilities do VMs have?


- A) Only monitoring
- B) Small applications for post-deployment configuration (antivirus, monitoring, custom scripts)
- C) Only backups
- D) No extensions

**Answer: B**
VM extensions automate tasks: install software, run scripts, configure monitoring, join domains.