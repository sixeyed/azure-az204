# VM Configuration - Quickfire Questions

## Question 1
What is VM configuration?

- A) Network configuration only
- B) Post-deployment customization of VM settings, software, and services
- C) Storage only
- D) Billing configuration

**Answer: B**
VM configuration includes OS settings, installed software, startup scripts, and environment setup.

---

## Question 2
What is cloud-init?

- A) VM shutdown
- B) Cloud instance initialization tool for Linux VMs, runs scripts at first boot
- C) Windows tool
- D) Network initialization

**Answer: B**
Cloud-init automates Linux VM setup: install packages, create users, configure services at deployment.

---

## Question 3
What is Custom Script Extension?

- A) Scripting language
- B) VM extension that downloads and executes scripts on VMs
- C) Code editor
- D) Database script

**Answer: B**
Custom Script Extension runs PowerShell (Windows) or bash (Linux) scripts for automated configuration.

---

## Question 4
What is Desired State Configuration (DSC)?

- A) Manual configuration
- B) PowerShell-based configuration management ensuring VMs maintain desired state
- C) State machine
- D) Database state

**Answer: B**
DSC declaratively configures and maintains Windows VMs, automatically correcting configuration drift.

---

## Question 5
Can you automate VM configuration?

- A) Manual only
- B) Yes, using cloud-init, Custom Script Extension, DSC, Ansible, Chef, Puppet
- C) Not possible
- D) Requires special license

**Answer: B**
Multiple automation options available for consistent, repeatable VM configurations.

---

## Question 6
What is boot diagnostics?

- A) VM health check
- B) Screenshot and console output from VM boot process for troubleshooting
- C) Network diagnostics
- D) Storage diagnostics

**Answer: B**
Boot diagnostics captures console output and screenshots to diagnose boot failures.

---

## Question 7
What is Azure VM Agent?

- A) Antivirus
- B) Lightweight process managing VM extensions and Azure platform communication
- C) Monitoring only
- D) Backup tool

**Answer: B**
VM Agent enables extension management and communicates with Azure fabric for VM operations.

---

## Question 8
How can you join Windows VM to Active Directory?

- A) Not possible
- B) Manually, via extension, or Azure AD Domain Services
- C) Automatic only
- D) Requires on-premises

**Answer: B**
Join using PowerShell, DSC extension, or Azure AD DS for managed domain services.

---

## Question 9
What is serial console access?

- A) Physical console
- B) Text-based console access for troubleshooting when network unavailable
- C) GUI only
- D) Not available

**Answer: B**
Serial console provides direct VM access via Azure portal for troubleshooting boot/network issues.

---

## Question 10
Can you schedule VM operations?

- A) No scheduling
- B) Yes, using automation accounts, runbooks, or scheduled tasks
- C) Manual only
- D) Automatic always

**Answer: B**
Schedule start/stop, backups, patching using Azure Automation, Logic Apps, or Functions.
