# Windows VMs - Quickfire Questions

## Question 1
What Windows versions are available for Azure VMs?

- A) Only latest
- B) Windows Server 2008 R2-2022, Windows 10/11 (multi-session for AVD)
- C) Only Windows 10
- D) No Windows support

**Answer: B**
Wide range of Windows Server versions plus Windows 10/11 Enterprise multi-session.

---

## Question 2
How do you connect to Windows VMs?

- A) SSH only
- B) RDP (Remote Desktop Protocol), Azure Bastion, Serial Console
- C) FTP
- D) Cannot connect

**Answer: B**
Primary method is RDP on port 3389, or Azure Bastion for secure browser-based access.

---

## Question 3
What is Windows Admin Center?

- A) User account
- B) Browser-based management tool for Windows Server
- C) Antivirus
- D) Backup tool

**Answer: B**
Modern management interface for Windows Server administration tasks in browser.

---

## Question 4
Can you run Active Directory on Azure VMs?

- A) No
- B) Yes, deploy AD Domain Controllers on VMs for hybrid scenarios
- C) Only read-only
- D) Not supported

**Answer: B**
Common pattern: run AD DS on Azure VMs for hybrid identity or isolated domains.

---

## Question 5
What is Azure Hybrid Benefit for Windows?

- A) Storage discount
- B) Use existing Windows Server licenses to save on Azure VM costs
- C) Free upgrades
- D) Network benefit

**Answer: B**
Bring your own Windows Server licenses with Software Assurance for significant savings.

---

## Question 6
Do Windows VMs include anti-malware?

- A) Yes, always included
- B) Microsoft Antimalware extension available but must be configured
- C) No security
- D) Third-party only

**Answer: B**
Microsoft Antimalware extension provides real-time protection, can be deployed via ARM/Bicep.

---

## Question 7
What is Windows Update management for VMs?

- A) Automatic only
- B) Manual updates, WSUS, Azure Update Management, or third-party tools
- C) No updates needed
- D) Not possible

**Answer: B**
Multiple options for patch management depending on requirements and architecture.

---

## Question 8
Can you use PowerShell Remoting with Azure VMs?

- A) No
- B) Yes, over public IP or via VPN/ExpressRoute/Bastion
- C) Only locally
- D) Not supported

**Answer: B**
Enable PowerShell Remoting for remote management (consider security implications).

---

## Question 9
What backup options exist for Windows VMs?

- A) No backups
- B) Azure Backup, Windows Server Backup, third-party solutions
- C) Manual only
- D) Snapshots only

**Answer: B**
Azure Backup provides agent-less VM backup with retention policies and recovery.

---

## Question 10
Can you run SQL Server on Windows VMs?

- A) No database support
- B) Yes, SQL Server VMs common for IaaS database workloads
- C) Only Linux
- D) Not recommended

**Answer: B**
SQL Server on Windows VMs provides full SQL functionality with IaaS control.
