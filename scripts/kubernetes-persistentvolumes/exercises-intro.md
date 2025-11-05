# Kubernetes Persistent Volumes: Exercises Introduction

We've covered how Persistent Volumes provide durable storage that survives pod restarts and how they decouple storage provisioning from consumption. Now let's work with PVs, PVCs, and storage classes.

## What You'll Do

You'll explore storage concepts understanding the difference between ephemeral container storage that disappears with pods and persistent volumes that retain data across pod lifecycle.

Then you'll create Persistent Volumes manually defining storage resources with capacity, access modes, and reclaim policies. You'll see how PVs exist independently from pods as cluster-level resources.

You'll create Persistent Volume Claims that request storage with specific size and access mode requirements. PVCs bind to available PVs meeting their criteria, acting as storage requests from applications.

Next, you'll mount PVCs in pods treating them as volumes in container specs. Multiple pods can share the same PVC depending on access mode, enabling data sharing between replicas.

You'll work with Storage Classes for dynamic provisioning where PVCs automatically trigger PV creation. Azure Disk and Azure Files storage classes in AKS provide different performance characteristics and access patterns.

You'll explore access modes including ReadWriteOnce for single-node access, ReadOnlyMany for multi-node reads, and ReadWriteMany for multi-node read-write requiring special storage types like Azure Files.

The lab challenge asks you to configure stateful applications using StatefulSets with persistent volume claim templates, ensuring each pod gets its own dedicated storage.

The key learning: Persistent storage is essential for databases, file shares, and any stateful workload. Understanding PVs, PVCs, and storage classes enables proper storage architecture in Kubernetes.
