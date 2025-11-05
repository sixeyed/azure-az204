# Linux VM Scale Sets - Quickfire Questions

## Question 1
What is a VM Scale Set (VMSS)?

- A) Single large VM
- B) Group of identical VMs that can auto-scale based on demand
- C) Storage scaling
- D) Network scaling

**Answer: B**
VMSS creates and manages identical VMs with integrated load balancing and auto-scaling.

---

## Question 2
What are the benefits of VMSS?

- A) Manual management
- B) Auto-scaling, high availability, simplified management of identical VMs
- C) Only cost savings
- D) No benefits

**Answer: B**
VMSS provides automatic scaling, fault distribution, and simplified updates for large deployments.

---

## Question 3
What Linux distributions are available for VMSS?

- A) Only one
- B) Ubuntu, Red Hat, CentOS, Debian, SUSE, Oracle Linux, etc.
- C) Windows only
- D) Custom only

**Answer: B**
All major Linux distributions available in Azure Marketplace work with VMSS.

---

## Question 4
How does auto-scaling work in VMSS?

- A) Manual only
- B) Automatically adds/removes instances based on metrics (CPU, memory) or schedule
- C) Fixed size
- D) Random scaling

**Answer: B**
Define scale rules: scale out when CPU > 70%, scale in when CPU < 30%, or schedule-based.

---

## Question 5
What is the maximum number of instances in VMSS?

- A) 10
- B) 1000 (standard), 600 (with single placement group disabled)
- C) 100
- D) Unlimited

**Answer: B**
Up to 1000 VMs with Marketplace images, 600 with custom images (large scale sets).

---

## Question 6
How do you deploy applications to VMSS?

- A) Manual installation per VM
- B) Custom Script Extension, cloud-init, custom image, or CI/CD pipelines
- C) Not possible
- D) Copy files manually

**Answer: B**
Automate deployment using extensions, images with pre-installed software, or deployment pipelines.

---

## Question 7
What update models are available for VMSS?

- A) Manual only
- B) Manual, Automatic, Rolling
- C) Immediate only
- D) No updates

**Answer: B**
Manual (control when), Automatic (immediate), Rolling (gradual with health checks).

---

## Question 8
What is orchestration mode in VMSS?

- A) Music mode
- B) Uniform (identical VMs) or Flexible (heterogeneous VMs)
- C) Single mode only
- D) Not configurable

**Answer: B**
Uniform for identical instances, Flexible for varied VM sizes and availability zones.

---

## Question 9
Can VMSS integrate with load balancers?

- A) No
- B) Yes, with Azure Load Balancer or Application Gateway
- C) Manual configuration only
- D) Not supported

**Answer: B**
VMSS automatically integrates with load balancers for traffic distribution.

---

## Question 10
How do you update application code on running VMSS?

- A) Delete and recreate
- B) Rolling update with new image/extension, or in-place deployment
- C) Not possible
- D) Manual per instance

**Answer: B**
Update model image or run deployment scripts, VMSS upgrades instances based on policy.
