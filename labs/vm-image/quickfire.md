# VM Custom Images - Quickfire Questions

## Question 1
What is a custom VM image?


- A) Profile picture
- B) Wallpaper
- C) Snapshot of configured VM used as template for deploying new VMs
- D) Icon set

**Answer: C**
Custom images capture VM configuration, OS, and software for consistent, rapid deployment.
---
## Question 2
When should you use custom images?


- A) Only for testing
- B) For standardized deployments with pre-installed software and configuration
- C) Never
- D) Always required

**Answer: B**
Custom images ensure consistency, reduce deployment time, and enforce standards.
---
## Question 3
What is Azure Compute Gallery (formerly Shared Image Gallery)?


- A) Backup storage
- B) Repository for storing and sharing custom VM images across subscriptions and regions
- C) Photo storage
- D) Art gallery

**Answer: B**
Compute Gallery manages image versions, replication, and sharing for enterprise image management.
---
## Question 4
What is generalization (sysprep/waagent)?


- A) Removing machine-specific information to create reusable image
- B) Making image public
- C) General settings
- D) Compression

**Answer: A**
Generalization removes unique identifiers, allowing image to be used for multiple VMs.
---
## Question 5
What happens if you don't generalize before creating image?


- A) No problem
- B) Image is better
- C) Nothing
- D) VMs from image may have duplicate SIDs, hostname conflicts, licensing issues

**Answer: D**
Un-generalized images cause identity conflicts and potential licensing violations.
---
## Question 6
Can you version custom images?


- A) Yes, Azure Compute Gallery supports versioning and rollback
- B) Manual only
- C) No versioning
- D) Not recommended

**Answer: A**
Image versions enable tracking changes, A/B testing, and rollback to previous versions.
---
## Question 7
Can custom images be replicated across regions?


- A) No, single region only
- B) Manual copy only
- C) Not possible
- D) Yes, Compute Gallery supports multi-region replication

**Answer: D**
Regional replication reduces deployment latency and provides disaster recovery.
---
## Question 8
What is the difference between image and snapshot?


- A) Snapshot is newer
- B) Same thing
- C) Snapshot is point-in-time disk copy; image is generalized template for new VMs
- D) Image is smaller

**Answer: C**
Snapshots for backup/restore. Images for deploying new VMs from template.
---
## Question 9
Can you create image from running VM?


- A) Only Windows
- B) Only Linux
- C) Not recommended; VM should be stopped and generalized
- D) Yes, always safe

**Answer: C**
Capture from stopped, generalized VM to ensure consistency and avoid corruption.
---
## Question 10
What formats does Azure support for custom images?


- A) Only proprietary format
- B) VHD, VHDX (converted to VHD), Compute Gallery image
- C) Only ISO
- D) Any format

**Answer: B**
Upload VHD/VHDX disks or create images in Compute Gallery from existing VMs.