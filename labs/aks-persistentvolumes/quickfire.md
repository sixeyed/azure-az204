# AKS Persistent Volumes - Quickfire Questions

## Question 1
Why do stateful applications need persistent volumes?

- A) For performance
- B) Data must survive pod restarts and rescheduling
- C) Only for backups
- D) Not necessary

**Answer: B**
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
- B) Request for storage by user/pod, binding to available PV
- C) Billing claim
- D) Network claim

**Answer: B**
PVCs are storage requests specifying size and access mode, fulfilled by matching PVs.

---

## Question 4
What Azure storage options work with AKS persistent volumes?

- A) Only blob
- B) Azure Disk (ReadWriteOnce), Azure Files (ReadWriteMany)
- C) Only files
- D) No Azure storage

**Answer: B**
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

- A) Storage quality
- B) Template defining storage type (managed disk SKU, file share) for dynamic provisioning
- C) Storage size
- D) Storage location

**Answer: B**
StorageClass abstracts storage details (Premium SSD, Standard HDD) enabling dynamic PV creation.

---

## Question 7
What is dynamic volume provisioning?

- A) Manual creation
- B) Automatic PV creation when PVC is created, based on StorageClass
- C) Static allocation
- D) Not supported

**Answer: B**
Dynamic provisioning auto-creates Azure Disks/Files when PVC references StorageClass.

---

## Question 8
What access modes does Azure Disk support?

- A) ReadWriteMany
- B) ReadWriteOnce (single node)
- C) All modes
- D) ReadOnly

**Answer: B**
Azure Disk is block storage, supporting ReadWriteOnce (one pod/node at a time).

---

## Question 9
When should you use StatefulSets with persistent volumes?

- A) Never
- B) For stateful apps requiring stable storage and network identity (databases, queues)
- C) Only for storage
- D) All applications

**Answer: B**
StatefulSets manage stateful workloads with ordered deployment and persistent storage per pod.

---

## Question 10
Can persistent volumes be backed up?

- A) No backups
- B) Yes, using Azure Backup for AKS or disk snapshots
- C) Manual copy only
- D) Not supported

**Answer: B**
Azure Backup for AKS, Azure Disk snapshots, or Velero provide PV backup/restore capabilities.
