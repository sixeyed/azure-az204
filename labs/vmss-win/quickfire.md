# Windows VM Scale Sets - Quickfire Questions

## Question 1
What is unique about Windows VMSS compared to Linux?

- A) Completely different
- B) Same auto-scaling concepts, different OS and configuration methods
- C) Windows doesn't support VMSS
- D) No difference

**Answer: B**
VMSS functionality is same; differences in OS, configuration tools (DSC vs cloud-init), and licensing.

---

## Question 2
How do you configure Windows instances in VMSS?

- A) Manual only
- B) Custom Script Extension, DSC, custom images, or Azure Automation
- C) Not configurable
- D) Automatic only

**Answer: B**
PowerShell DSC, Custom Script Extension, or pre-configured custom images for consistency.

---

## Question 3
What licensing options exist for Windows VMSS?

- A) Free only
- B) Pay-as-you-go or Azure Hybrid Benefit with existing licenses
- C) Enterprise only
- D) No licensing

**Answer: B**
Use included licensing (charged per VM-hour) or bring existing licenses with Hybrid Benefit.

---

## Question 4
Can Windows VMSS join Active Directory?

- A) No
- B) Yes, using DSC extension or Azure AD Domain Services
- C) Only Azure AD
- D) Not supported

**Answer: B**
Domain join via PowerShell DSC extension or integrate with Azure AD DS.

---

## Question 5
What web servers can run on Windows VMSS?

- A) Only IIS
- B) IIS, Apache, Nginx, or any Windows-compatible web server
- C) None
- D) Linux servers only

**Answer: B**
IIS most common, but any web server supporting Windows can be installed.

---

## Question 6
How do you handle application updates in Windows VMSS?

- A) Manual updates per instance
- B) Rolling updates with new custom image or deployment automation
- C) Delete and recreate
- D) Not possible

**Answer: B**
Create updated custom image or use deployment pipelines with rolling update policy.

---

## Question 7
What monitoring is available for Windows VMSS?

- A) No monitoring
- B) Azure Monitor, Application Insights, performance counters, event logs
- C) Only basic metrics
- D) Manual monitoring only

**Answer: B**
Full monitoring via Azure Monitor VM Insights, custom metrics, and application telemetry.

---

## Question 8
Can Windows VMSS use proximity placement groups?

- A) No
- B) Yes, for low-latency requirements by co-locating instances
- C) Only Linux VMSS
- D) Not needed

**Answer: B**
Proximity placement groups reduce latency by placing VMs physically close together.

---

## Question 9
What patching strategies exist for Windows VMSS?

- A) Manual only
- B) Azure Update Management, WSUS, automatic OS updates
- C) No patching
- D) Third-party only

**Answer: B**
Automated patching via Update Management, automatic OS updates, or custom solutions.

---

## Question 10
Can you mix instance sizes in VMSS?

- A) No, all identical
- B) With Flexible orchestration mode, yes; Uniform mode requires identical instances
- C) Always mixed
- D) Not recommended

**Answer: B**
Uniform mode: identical VMs. Flexible mode: allows different VM sizes for heterogeneous workloads.
