# Windows VM Scale Sets - Quickfire Questions

## Question 1
What is unique about Windows VMSS compared to Linux?


- A) Same auto-scaling concepts, different OS and configuration methods
- B) No difference
- C) Completely different
- D) Windows doesn't support VMSS

**Answer: A**
VMSS functionality is same; differences in OS, configuration tools (DSC vs cloud-init), and licensing.
---
## Question 2
How do you configure Windows instances in VMSS?


- A) Manual only
- B) Not configurable
- C) Custom Script Extension, DSC, custom images, or Azure Automation
- D) Automatic only

**Answer: C**
PowerShell DSC, Custom Script Extension, or pre-configured custom images for consistency.
---
## Question 3
What licensing options exist for Windows VMSS?


- A) Enterprise only
- B) Free only
- C) Pay-as-you-go or Azure Hybrid Benefit with existing licenses
- D) No licensing

**Answer: C**
Use included licensing (charged per VM-hour) or bring existing licenses with Hybrid Benefit.
---
## Question 4
Can Windows VMSS join Active Directory?


- A) Only Azure AD
- B) Not supported
- C) No
- D) Yes, using DSC extension or Azure AD Domain Services

**Answer: D**
Domain join via PowerShell DSC extension or integrate with Azure AD DS.
---
## Question 5
What web servers can run on Windows VMSS?


- A) IIS, Apache, Nginx, or any Windows-compatible web server
- B) Linux servers only
- C) None
- D) Only IIS

**Answer: A**
IIS most common, but any web server supporting Windows can be installed.
---
## Question 6
How do you handle application updates in Windows VMSS?


- A) Manual updates per instance
- B) Not possible
- C) Rolling updates with new custom image or deployment automation
- D) Delete and recreate

**Answer: C**
Create updated custom image or use deployment pipelines with rolling update policy.
---
## Question 7
What monitoring is available for Windows VMSS?


- A) Only basic metrics
- B) Azure Monitor, Application Insights, performance counters, event logs
- C) Manual monitoring only
- D) No monitoring

**Answer: B**
Full monitoring via Azure Monitor VM Insights, custom metrics, and application telemetry.
---
## Question 8
Can Windows VMSS use proximity placement groups?


- A) No
- B) Only Linux VMSS
- C) Yes, for low-latency requirements by co-locating instances
- D) Not needed

**Answer: C**
Proximity placement groups reduce latency by placing VMs physically close together.
---
## Question 9
What patching strategies exist for Windows VMSS?


- A) Third-party only
- B) No patching
- C) Manual only
- D) Azure Update Management, WSUS, automatic OS updates

**Answer: D**
Automated patching via Update Management, automatic OS updates, or custom solutions.
---
## Question 10
Can you mix instance sizes in VMSS?


- A) Not recommended
- B) Always mixed
- C) No, all identical
- D) With Flexible orchestration mode, yes; Uniform mode requires identical instances

**Answer: D**
Uniform mode: identical VMs. Flexible mode: allows different VM sizes for heterogeneous workloads.