# SQL Server on Azure VMs - Quickfire Questions

## Question 1
When should you use SQL Server on VM vs Azure SQL Database?

- A) Always use VMs
- B) VMs for OS-level access, specific SQL versions, legacy compatibility; SQL DB for managed PaaS
- C) Always use SQL Database
- D) No difference

**Answer: B**
SQL on VMs provides full control (IaaS); Azure SQL Database provides management automation (PaaS).

---

## Question 2
What SQL Server versions are available on Azure VMs?

- A) Only latest
- B) SQL Server 2012-2022, various editions
- C) Only Express
- D) Custom only

**Answer: B**
Azure Marketplace offers SQL 2012, 2014, 2016, 2017, 2019, 2022 in various editions (Express, Web, Standard, Enterprise).

---

## Question 3
What are SQL Server VM images?

- A) Screenshots
- B) Pre-configured VM images with SQL Server installed and licensed
- C) Backup images
- D) Photo gallery

**Answer: B**
Azure provides images with SQL Server pre-installed, simplifying deployment and including pay-as-you-go licensing.

---

## Question 4
What is the SQL IaaS Agent Extension?

- A) Security agent
- B) Extension providing automated backups, patching, licensing management for SQL VMs
- C) Monitoring only
- D) Not recommended

**Answer: B**
SQL IaaS Extension enables automated backup, patching, Azure integration, portal management for SQL VMs.

---

## Question 5
What management modes does SQL IaaS Extension support?

- A) Only one mode
- B) NoAgent, LightWeight, Full
- C) Basic and Advanced
- D) Public and Private

**Answer: B**
NoAgent (limited), LightWeight (basic features, no restart), Full (all features, requires restart).

---

## Question 6
Can you use SQL Server licensing you already own?

- A) No, must pay Azure
- B) Yes, using Azure Hybrid Benefit with Software Assurance
- C) Only for dev/test
- D) Not allowed

**Answer: B**
Azure Hybrid Benefit allows using existing SQL Server licenses, significantly reducing costs.

---

## Question 7
What high availability options exist for SQL on VMs?

- A) None
- B) Always On Availability Groups, Failover Cluster Instances
- C) Automatic only
- D) Manual failover only

**Answer: B**
Always On AG (replicas across VMs), FCI (shared storage clustering) provide HA/DR.

---

## Question 8
How do you back up SQL Server on VMs?

- A) No backups possible
- B) Automated backup (via extension), manual SQL backups, or Azure Backup
- C) Automatic only
- D) Manual only

**Answer: B**
Multiple options: SQL IaaS Extension automated backup, native SQL backups to blob, Azure Backup service.

---

## Question 9
What storage options are recommended for SQL VMs?

- A) Any storage
- B) Premium SSD or Ultra Disk for data/log files
- C) Only Standard HDD
- D) No storage needed

**Answer: B**
Premium SSD provides good performance; Ultra Disk for highest IOPS/throughput requirements.

---

## Question 10
Do you need to patch/maintain SQL Server on VMs?

- A) No, fully managed
- B) Yes, you manage patching (though SQL IaaS Extension can automate)
- C) Automatic always
- D) No patching needed

**Answer: B**
IaaS model means you manage OS/SQL patching, though SQL IaaS Extension offers automated patching.
