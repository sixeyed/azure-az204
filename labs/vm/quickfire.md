# Azure Virtual Machines - Quickfire Questions

## Question 1
What are Azure Virtual Machines?

- A) Physical machines
- B) IaaS compute resources providing full OS control
- C) PaaS service
- D) Storage service

**Answer: B**
VMs provide virtualized compute with full control over OS, ideal for custom configurations and migrations.

---

## Question 2
What VM sizes categories exist?

- A) Only one size
- B) General purpose, Compute optimized, Memory optimized, Storage optimized, GPU
- C) Small and Large
- D) Basic and Premium

**Answer: B**
Different VM series optimized for various workloads: balanced (D-series), CPU (F-series), memory (E-series), etc.

---

## Question 3
What are availability sets?

- A) VM collections
- B) Logical grouping providing fault/update domain distribution for high availability
- C) Backup sets
- D) Storage sets

**Answer: B**
Availability sets distribute VMs across fault domains (hardware) and update domains (maintenance) for 99.95% SLA.

---

## Question 4
What is an availability zone?

- A) Time zone
- B) Physically separate datacenter within Azure region
- C) Network zone
- D) Storage zone

**Answer: B**
Availability zones provide datacenter-level isolation within region for 99.99% SLA.

---

## Question 5
What is Azure Managed Disks?

- A) Manual disk management
- B) Simplified disk management with automatic replication and no storage account management
- C) Physical disks
- D) Network disks

**Answer: B**
Managed Disks handle storage accounts automatically, provide 99.999% availability, and simplify VM management.

---

## Question 6
What disk types are available?

- A) Only one type
- B) Ultra Disk, Premium SSD, Standard SSD, Standard HDD
- C) Fast and Slow
- D) Public and Private

**Answer: B**
Ultra (highest performance), Premium SSD (production), Standard SSD (web servers), Standard HDD (backup/dev).

---

## Question 7
Can you resize a VM?

- A) Never
- B) Yes, change VM size (may require restart)
- C) Only downgrade
- D) Only upgrade

**Answer: B**
VMs can be resized to different sizes within same family or different families (with restart).

---

## Question 8
What is Azure Bastion?

- A) Security group
- B) Managed service for secure RDP/SSH access without public IPs
- C) Load balancer
- D) VPN

**Answer: B**
Bastion provides secure browser-based RDP/SSH from Azure portal without exposing VMs to internet.

---

## Question 9
What is VM Scale Sets (VMSS)?

- A) Manual VM group
- B) Automated deployment and management of identical VMs with auto-scaling
- C) Storage scaling
- D) Network scaling

**Answer: B**
VMSS creates and manages group of load-balanced VMs with automatic scaling based on demand.

---

## Question 10
What extension capabilities do VMs have?

- A) No extensions
- B) Small applications for post-deployment configuration (antivirus, monitoring, custom scripts)
- C) Only monitoring
- D) Only backups

**Answer: B**
VM extensions automate tasks: install software, run scripts, configure monitoring, join domains.
