# AKS with Persistent Volumes - AZ-204 Exam Introduction

Great job working with Kubernetes storage! Now let's focus on what the AZ-204 exam expects you to know about persistent storage in containerized applications.

## Exam Coverage

This addresses the containerized solutions domain of AZ-204, specifically AKS storage concepts and abstractions. Expect questions about choosing appropriate storage types, understanding data lifecycle, and troubleshooting storage issues.

## What We'll Cover

**Storage lifecycle** is fundamental and heavily tested. Container filesystems are ephemeral - data is lost when containers are deleted (even if the pod remains). EmptyDir volumes survive container restarts but not pod deletion - they're pod-scoped. PersistentVolumes survive pod deletion and can be reattached to new pods - they're cluster-scoped. The exam tests your understanding of what happens to data during various failure and replacement scenarios.

**PersistentVolumeClaims with Storage Classes** appear on almost every AKS exam question involving storage. A PVC is a request for storage with specific requirements (size, access mode, storage class). Storage Classes define the provisioner (what creates the actual storage) and parameters. In AKS, the default storage class uses Azure Managed Disks with dynamic provisioning - storage is automatically created when you create a PVC. Know how to create PVCs and reference them in pod specs.

**Azure Managed Disks vs Azure Files** is a critical exam topic. Managed Disks support only ReadWriteOnce access mode - only one pod can mount the volume at a time. They're high-performance, SSD-backed, and ideal for databases. Azure Files supports ReadWriteMany - multiple pods can mount concurrently. It uses SMB/NFS protocols, is slightly slower, and ideal for shared data scenarios. Scenario questions test which to choose based on whether you need shared access.

**Access modes** need to be memorized. ReadWriteOnce (RWO) - mounted read-write by single node. ReadOnlyMany (ROX) - mounted read-only by many nodes. ReadWriteMany (RWX) - mounted read-write by many nodes. Know that Azure Managed Disks support only RWO, while Azure Files supports all three modes. The exam tests which mode to request based on application requirements.

**ConfigMaps for application configuration** is a related exam topic. ConfigMaps store non-sensitive configuration as key-value pairs or files, and can be mounted as volumes or exposed as environment variables. Know when to use ConfigMaps (non-sensitive config) vs Secrets (sensitive data) vs PersistentVolumes (application data).

We'll cover **dynamic provisioning**, **storage class parameters**, **volume snapshots and backups**, **troubleshooting mount issues**, and **common exam scenarios** about choosing storage solutions for different application patterns like stateful sets, shared caches, and database workloads.

Master persistent storage for the AZ-204 exam!
