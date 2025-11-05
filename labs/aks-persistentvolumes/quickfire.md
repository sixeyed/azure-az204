# AKS Persistent Volumes - Quickfire Questions

## Question 1
Why do stateful applications need persistent volumes?


- A) Data must survive pod restarts and rescheduling
- B) For performance
- C) Not necessary
- D) Only for backups

**Answer: A**
Persistent volumes ensure data survives pod lifecycle events (crashes, updates, migrations).
---
## Question 2
What is a PersistentVolume (PV) in Kubernetes?


- A) Temporary storage
- B) Cluster storage resource with independent lifecycle from pods
- C) Memory storage
- D) Network storage

**Answer: B**
PVs represent storage resources (disks, file shares) managed independently of pods.
---
## Question 3
What is a PersistentVolumeClaim (PVC)?


- A) Legal claim
- B) Billing claim
- C) Request for storage by user/pod, binding to available PV
- D) Network claim

**Answer: C**
PVCs are storage requests specifying size and access mode, fulfilled by matching PVs.
---
## Question 4
What Azure storage options work with AKS persistent volumes?


- A) Only blob
- B) No Azure storage
- C) Only files
- D) Azure Disk (ReadWriteOnce), Azure Files (ReadWriteMany)

**Answer: D**
Azure Disk for single-pod access; Azure Files for multi-pod shared access.
---
## Question 5
What is the difference between Azure Disk and Azure Files for AKS?


- A) Same thing
- B) Disk is block storage (single pod); Files is SMB share (multi-pod)
- C) Files is faster
- D) Disk is deprecated

**Answer: B**
Disk: ReadWriteOnce (one pod at a time). Files: ReadWriteMany (multiple pods simultaneously).
---
## Question 6
What is a StorageClass in AKS?


- A) Storage size
- B) Storage quality
- C) Storage location
- D) Template defining storage type (managed disk SKU, file share) for dynamic provisioning

**Answer: D**
StorageClass abstracts storage details (Premium SSD, Standard HDD) enabling dynamic PV creation.
---
## Question 7
What is dynamic volume provisioning?


- A) Automatic PV creation when PVC is created, based on StorageClass
- B) Manual creation
- C) Not supported
- D) Static allocation

**Answer: A**
Dynamic provisioning auto-creates Azure Disks/Files when PVC references StorageClass.
---
## Question 8
What access modes does Azure Disk support?


- A) All modes
- B) ReadWriteOnce (single node)
- C) ReadOnly
- D) ReadWriteMany

**Answer: B**
Azure Disk is block storage, supporting ReadWriteOnce (one pod/node at a time).
---
## Question 9
When should you use StatefulSets with persistent volumes?


- A) Never
- B) All applications
- C) Only for storage
- D) For stateful apps requiring stable storage and network identity (databases, queues)

**Answer: D**
StatefulSets manage stateful workloads with ordered deployment and persistent storage per pod.
---
## Question 10
Can persistent volumes be backed up?


- A) Yes, using Azure Backup for AKS or disk snapshots
- B) No backups
- C) Not supported
- D) Manual copy only

**Answer: A**
Azure Backup for AKS, Azure Disk snapshots, or Velero provide PV backup/restore capabilities.