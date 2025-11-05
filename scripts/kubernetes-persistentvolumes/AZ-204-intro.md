# Kubernetes Persistent Volumes: AZ-204 Exam Focus

Great work! This persistent storage lab is crucial for the "Implement containerized solutions" objective in the AZ-204 exam. Understanding stateful workloads is essential for Azure Kubernetes Service.

## What We'll Cover

We'll examine the storage architecture with three components the exam tests: Persistent Volumes as cluster-level storage resources, Persistent Volume Claims as namespace-scoped storage requests, and Storage Classes enabling dynamic provisioning with different performance tiers.

We'll explore Azure storage integration where Azure Disk provides block storage with ReadWriteOnce access suitable for databases, Azure Files provides file shares with ReadWriteMany access enabling multiple pod access, and Azure Blob through CSI drivers for object storage scenarios.

You'll master access modes that determine sharing capabilities. ReadWriteOnce allows single-node mounting typical for databases, ReadOnlyMany allows multi-node read access for shared configuration, and ReadWriteMany allows multi-node read-write requiring Azure Files or similar.

The exam tests dynamic provisioning with Storage Classes defining provisioner, parameters, and reclaim policy. PVCs reference storage classes automatically triggering PV creation. Understand default storage classes and how to specify alternatives.

We'll cover StatefulSets for stateful applications providing stable pod identities, ordered deployment and scaling, and persistent volume claim templates ensuring each pod gets dedicated storage. This is essential for databases, message queues, and similar workloads.

You'll understand backup and disaster recovery with Azure Backup for AKS, volume snapshots using CSI drivers, and replication strategies across regions. The exam tests recovery point objectives and recovery time objectives for stateful applications.

Master persistent storage patterns, Azure storage integration, and stateful application deployment for the AZ-204!
