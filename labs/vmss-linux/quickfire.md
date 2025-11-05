# Linux VM Scale Sets - Quickfire Questions

## Question 1
What is a VM Scale Set (VMSS)?


- A) Group of identical VMs that can auto-scale based on demand
- B) Single large VM
- C) Network scaling
- D) Storage scaling

**Answer: A**
VMSS creates and manages identical VMs with integrated load balancing and auto-scaling.
---
## Question 2
What are the benefits of VMSS?


- A) Auto-scaling, high availability, simplified management of identical VMs
- B) No benefits
- C) Manual management
- D) Only cost savings

**Answer: A**
VMSS provides automatic scaling, fault distribution, and simplified updates for large deployments.
---
## Question 3
What Linux distributions are available for VMSS?


- A) Custom only
- B) Only one
- C) Ubuntu, Red Hat, CentOS, Debian, SUSE, Oracle Linux, etc.
- D) Windows only

**Answer: C**
All major Linux distributions available in Azure Marketplace work with VMSS.
---
## Question 4
How does auto-scaling work in VMSS?


- A) Fixed size
- B) Random scaling
- C) Manual only
- D) Automatically adds/removes instances based on metrics (CPU, memory) or schedule

**Answer: D**
Define scale rules: scale out when CPU > 70%, scale in when CPU < 30%, or schedule-based.
---
## Question 5
What is the maximum number of instances in VMSS?


- A) Unlimited
- B) 10
- C) 1000 (standard), 600 (with single placement group disabled)
- D) 100

**Answer: C**
Up to 1000 VMs with Marketplace images, 600 with custom images (large scale sets).
---
## Question 6
How do you deploy applications to VMSS?


- A) Copy files manually
- B) Custom Script Extension, cloud-init, custom image, or CI/CD pipelines
- C) Manual installation per VM
- D) Not possible

**Answer: B**
Automate deployment using extensions, images with pre-installed software, or deployment pipelines.
---
## Question 7
What update models are available for VMSS?


- A) No updates
- B) Manual only
- C) Immediate only
- D) Manual, Automatic, Rolling

**Answer: D**
Manual (control when), Automatic (immediate), Rolling (gradual with health checks).
---
## Question 8
What is orchestration mode in VMSS?


- A) Music mode
- B) Uniform (identical VMs) or Flexible (heterogeneous VMs)
- C) Not configurable
- D) Single mode only

**Answer: B**
Uniform for identical instances, Flexible for varied VM sizes and availability zones.
---
## Question 9
Can VMSS integrate with load balancers?


- A) Manual configuration only
- B) No
- C) Not supported
- D) Yes, with Azure Load Balancer or Application Gateway

**Answer: D**
VMSS automatically integrates with load balancers for traffic distribution.
---
## Question 10
How do you update application code on running VMSS?


- A) Delete and recreate
- B) Not possible
- C) Rolling update with new image/extension, or in-place deployment
- D) Manual per instance

**Answer: C**
Update model image or run deployment scripts, VMSS upgrades instances based on policy.