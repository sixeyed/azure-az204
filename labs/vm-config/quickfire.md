# VM Configuration - Quickfire Questions

## Question 1
What is VM configuration?


- A) Post-deployment customization of VM settings, software, and services
- B) Storage only
- C) Billing configuration
- D) Network configuration only

**Answer: A**
VM configuration includes OS settings, installed software, startup scripts, and environment setup.
---
## Question 2
What is cloud-init?


- A) Windows tool
- B) Cloud instance initialization tool for Linux VMs, runs scripts at first boot
- C) VM shutdown
- D) Network initialization

**Answer: B**
Cloud-init automates Linux VM setup: install packages, create users, configure services at deployment.
---
## Question 3
What is Custom Script Extension?


- A) Code editor
- B) VM extension that downloads and executes scripts on VMs
- C) Database script
- D) Scripting language

**Answer: B**
Custom Script Extension runs PowerShell (Windows) or bash (Linux) scripts for automated configuration.
---
## Question 4
What is Desired State Configuration (DSC)?


- A) Database state
- B) PowerShell-based configuration management ensuring VMs maintain desired state
- C) Manual configuration
- D) State machine

**Answer: B**
DSC declaratively configures and maintains Windows VMs, automatically correcting configuration drift.
---
## Question 5
Can you automate VM configuration?


- A) Not possible
- B) Manual only
- C) Requires special license
- D) Yes, using cloud-init, Custom Script Extension, DSC, Ansible, Chef, Puppet

**Answer: D**
Multiple automation options available for consistent, repeatable VM configurations.
---
## Question 6
What is boot diagnostics?


- A) Network diagnostics
- B) Storage diagnostics
- C) VM health check
- D) Screenshot and console output from VM boot process for troubleshooting

**Answer: D**
Boot diagnostics captures console output and screenshots to diagnose boot failures.
---
## Question 7
What is Azure VM Agent?


- A) Monitoring only
- B) Backup tool
- C) Lightweight process managing VM extensions and Azure platform communication
- D) Antivirus

**Answer: C**
VM Agent enables extension management and communicates with Azure fabric for VM operations.
---
## Question 8
How can you join Windows VM to Active Directory?


- A) Manually, via extension, or Azure AD Domain Services
- B) Requires on-premises
- C) Not possible
- D) Automatic only

**Answer: A**
Join using PowerShell, DSC extension, or Azure AD DS for managed domain services.
---
## Question 9
What is serial console access?


- A) GUI only
- B) Not available
- C) Text-based console access for troubleshooting when network unavailable
- D) Physical console

**Answer: C**
Serial console provides direct VM access via Azure portal for troubleshooting boot/network issues.
---
## Question 10
Can you schedule VM operations?


- A) Yes, using automation accounts, runbooks, or scheduled tasks
- B) No scheduling
- C) Manual only
- D) Automatic always

**Answer: A**
Schedule start/stop, backups, patching using Azure Automation, Logic Apps, or Functions.