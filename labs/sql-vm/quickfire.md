# SQL Server on Azure VMs - Quickfire Questions

## Question 1
When should you use SQL Server on VM vs Azure SQL Database?


- A) Always use SQL Database
- B) VMs for OS-level access, specific SQL versions, legacy compatibility; SQL DB for managed PaaS
- C) Always use VMs
- D) No difference

**Answer: B**
SQL on VMs provides full control (IaaS); Azure SQL Database provides management automation (PaaS).
---
## Question 2
What SQL Server versions are available on Azure VMs?


- A) Custom only
- B) Only Express
- C) Only latest
- D) SQL Server 2012-2022, various editions

**Answer: D**
Azure Marketplace offers SQL 2012, 2014, 2016, 2017, 2019, 2022 in various editions (Express, Web, Standard, Enterprise).
---
## Question 3
What are SQL Server VM images?


- A) Backup images
- B) Photo gallery
- C) Pre-configured VM images with SQL Server installed and licensed
- D) Screenshots

**Answer: C**
Azure provides images with SQL Server pre-installed, simplifying deployment and including pay-as-you-go licensing.
---
## Question 4
What is the SQL IaaS Agent Extension?


- A) Not recommended
- B) Security agent
- C) Extension providing automated backups, patching, licensing management for SQL VMs
- D) Monitoring only

**Answer: C**
SQL IaaS Extension enables automated backup, patching, Azure integration, portal management for SQL VMs.
---
## Question 5
What management modes does SQL IaaS Extension support?


- A) Basic and Advanced
- B) Public and Private
- C) Only one mode
- D) NoAgent, LightWeight, Full

**Answer: D**
NoAgent (limited), LightWeight (basic features, no restart), Full (all features, requires restart).
---
## Question 6
Can you use SQL Server licensing you already own?


- A) Not allowed
- B) No, must pay Azure
- C) Only for dev/test
- D) Yes, using Azure Hybrid Benefit with Software Assurance

**Answer: D**
Azure Hybrid Benefit allows using existing SQL Server licenses, significantly reducing costs.
---
## Question 7
What high availability options exist for SQL on VMs?


- A) Manual failover only
- B) Always On Availability Groups, Failover Cluster Instances
- C) None
- D) Automatic only

**Answer: B**
Always On AG (replicas across VMs), FCI (shared storage clustering) provide HA/DR.
---
## Question 8
How do you back up SQL Server on VMs?


- A) Automated backup (via extension), manual SQL backups, or Azure Backup
- B) Manual only
- C) No backups possible
- D) Automatic only

**Answer: A**
Multiple options: SQL IaaS Extension automated backup, native SQL backups to blob, Azure Backup service.
---
## Question 9
What storage options are recommended for SQL VMs?


- A) Any storage
- B) Premium SSD or Ultra Disk for data/log files
- C) No storage needed
- D) Only Standard HDD

**Answer: B**
Premium SSD provides good performance; Ultra Disk for highest IOPS/throughput requirements.
---
## Question 10
Do you need to patch/maintain SQL Server on VMs?


- A) Yes, you manage patching (though SQL IaaS Extension can automate)
- B) No, fully managed
- C) Automatic always
- D) No patching needed

**Answer: A**
IaaS model means you manage OS/SQL patching, though SQL IaaS Extension offers automated patching.