# Kubernetes Storage - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on Kubernetes Storage in Azure Kubernetes Service. Today we're exploring how to manage persistent storage for containerized applications running in AKS. Whether you're preparing for the Azure AZ-204 certification or building production Kubernetes applications, understanding storage patterns is essential for creating stateful applications that can survive container restarts and Pod replacements.

## The Storage Challenge in Containers

Let's start by understanding why storage in Kubernetes requires special attention.

Containers are designed to be ephemeral and immutable. You build a container image, and that image contains your application code and its dependencies. When you run a container, it gets its own isolated filesystem based on that image. You can write data to that filesystem while the container runs, but here's the critical point: when the container stops and is replaced, all that data disappears.

This design is intentional. It makes containers portable and reproducible. But it creates a challenge for stateful applications. If you're running a web application that needs to store user uploads, or a database that needs to persist data, or any application that creates state, you need somewhere to store that data that survives container replacements.

And in Kubernetes, containers get replaced frequently. When you update to a new container image, Kubernetes creates new containers. When a node fails, Kubernetes recreates the affected Pods on healthy nodes. When you scale down and then back up, you get new Pod instances. In all these cases, data stored in the container filesystem is lost.

This is where Kubernetes volumes come in.

## Understanding Kubernetes Volumes

Kubernetes provides multiple abstractions to help you model storage in a way that works across all clusters, whether you're running on Docker Desktop locally, on Azure Kubernetes Service, on AWS, or on on-premises infrastructure.

At the core, volumes are storage units that you can mount into your Pod containers. The key concept is that storage mounts appear as part of the container filesystem, but they're actually stored outside of the container. This separates the data lifecycle from the container lifecycle.

Kubernetes supports many types of volumes, each with different characteristics and use cases. Let me walk you through the most important ones.

## ConfigMaps as Volumes

One of the simplest volume types is a ConfigMap mounted as a volume. ConfigMaps store configuration data as key-value pairs or as complete files. When you mount a ConfigMap as a volume in a Pod, the data appears as files in the container filesystem.

This pattern is perfect for injecting configuration files into containers without rebuilding your container images. You might have an appsettings.json file for a .NET application, or a config.yaml file for any application. You store this in a ConfigMap, mount it as a volume, and your application reads it as if it were a regular file.

The beauty of this approach is separation of concerns. Your container image contains the application code, and the ConfigMap contains environment-specific configuration. The same container image can work across development, staging, and production, with different ConfigMaps providing the appropriate configuration for each environment.

ConfigMaps are typically read-only when mounted as volumes. Your application reads the configuration but doesn't modify it. This makes sense because ConfigMaps are Kubernetes objects managed through kubectl or APIs, not files your application should write to.

## EmptyDir Volumes

For temporary storage that needs to survive container restarts within the same Pod, Kubernetes provides EmptyDir volumes. When a Pod starts, Kubernetes creates an empty directory that all containers in the Pod can access. When the Pod is deleted, the EmptyDir is deleted too.

EmptyDir volumes are useful for several scenarios. Cache data that you can regenerate but want to keep between container restarts. Temporary files that multiple containers in the same Pod need to share. Workspace for processing that doesn't need to be permanent.

The key characteristic of EmptyDir is its lifecycle. If your container crashes and Kubernetes restarts it within the same Pod, the EmptyDir data survives. But if the Pod itself is deleted and recreated, the EmptyDir is new and empty.

This makes EmptyDir perfect for data that's valuable enough to keep during container restarts but doesn't need to survive Pod deletion.

## PersistentVolumes and PersistentVolumeClaims

For data that truly needs to persist - database files, user uploads, any state that must survive Pod replacements - Kubernetes provides PersistentVolumes and PersistentVolumeClaims.

This is a two-part abstraction. A PersistentVolume, or PV, represents actual storage resources in your cluster. This could be Azure Managed Disks, Azure Files, AWS EBS volumes, or any other storage system. A PersistentVolumeClaim, or PVC, is a request for storage by an application.

The pattern works like this: As a developer, you create a PVC that specifies how much storage you need and what access mode you require. Kubernetes finds or provisions a PersistentVolume that satisfies your claim and binds them together. Your Pod references the PVC, and Kubernetes mounts the underlying storage into your container.

This abstraction is powerful because it separates the storage request from the storage implementation. Your application doesn't need to know whether it's using Azure Disks or AWS volumes. You just request storage with certain characteristics, and Kubernetes handles the details.

## Storage Classes

Storage Classes add another layer to this abstraction by defining different types of storage with different properties. In AKS, you have multiple storage classes available, each backed by different Azure services.

The default storage class typically uses Azure Managed Disks. These provide excellent I/O performance with SSD-backed storage. They're perfect for databases or applications that need fast sequential or random I/O. However, Azure Managed Disks can only be attached to one node at a time. This means only one Pod can mount the volume for reading and writing. This is called ReadWriteOnce access mode.

Another storage class uses Azure Files. Azure Files provides file shares using the SMB protocol. Unlike managed disks, Azure Files supports ReadWriteMany access mode, meaning multiple Pods on multiple nodes can mount the same volume simultaneously for reading and writing. This is ideal for shared storage scenarios where multiple application instances need access to the same files.

When you create a PersistentVolumeClaim, you can specify which storage class to use. If you don't specify one, Kubernetes uses the default. This dynamic provisioning means Kubernetes automatically creates the Azure storage resources needed to satisfy your claim.

## Demonstrating the Lifecycle Differences

Let me walk you through a practical example that demonstrates these different storage types and their lifecycles.

Imagine you have a background worker application that writes to two files: a cache file for temporary data and a database file for persistent data. In the first version, you deploy this application without any volumes. The application writes both files directly to the container filesystem.

When you check the files, you see data accumulating. But when you delete the Pod, Kubernetes creates a replacement. When you check the files in the new Pod, all the data is gone. The database file only has entries from the new Pod. Everything from the previous Pod was lost because it was stored in the container filesystem, which has the same lifecycle as the container.

Now you deploy a second version with proper volume configuration. You mount the cache directory to an EmptyDir volume and the database directory to a PersistentVolumeClaim. You let the application run and generate data in both files.

When you delete the Pod this time and check the replacement, the results are different. The cache file is new - it only contains entries from the new Pod. That's because the EmptyDir in this Pod is a new directory, replacing the old one. But the database file contains entries from both the old Pod and the new Pod, all in chronological order. The PersistentVolume has a separate lifecycle from any Pod, so the data persists across Pod replacements.

This demonstrates the fundamental differences between these storage types and why choosing the right one matters for your application.

## Kubernetes Portability

One of the beautiful aspects of Kubernetes is portability. The same application specifications work across different Kubernetes platforms with minimal or no changes.

You can develop and test your application on Docker Desktop running on your laptop. The PersistentVolumeClaim uses local disk storage on your machine. Then you deploy the exact same YAML specifications to Azure Kubernetes Service. The PersistentVolumeClaim now provisions Azure Managed Disks. But your application doesn't know or care about this difference. It just sees storage mounted at the specified path.

This portability is enabled by the abstraction layers. Your application code doesn't interact directly with Azure APIs or local disk APIs. It just reads and writes files. Kubernetes handles the platform-specific implementation details.

## Access Modes and Multi-Pod Storage

Understanding access modes is important when you have multiple Pods that need to share data.

ReadWriteOnce mode, abbreviated RWO, means the volume can be mounted as read-write by one node. This doesn't mean just one Pod - multiple Pods on the same node can mount it, but it can't be mounted by Pods on different nodes simultaneously. This is the mode Azure Managed Disks support.

ReadWriteMany mode, abbreviated RWX, means the volume can be mounted as read-write by many nodes simultaneously. This is what Azure Files supports. With RWX storage, you can scale your application to multiple Pods across multiple nodes, and they can all read and write to the same shared storage.

Choosing between these depends on your application requirements. If you're running a database that should only have one instance writing to the data files, RWO is appropriate. If you're running multiple application instances that need to share uploaded files, RWX is necessary.

## Relevance to the AZ-204 Exam

Understanding Kubernetes storage is important for the Azure AZ-204 Developer Associate certification. Let me connect these concepts to specific exam objectives.

### Implementing Containerized Solutions

The exam includes a domain on implementing containerized solutions, which covers both Azure Container Instances and Azure Kubernetes Service. For AKS, you need to understand storage abstractions, how to request persistent storage using PersistentVolumeClaims, how Storage Classes work, and when to use different storage types.

The exam may present scenarios where you need to determine what happens to data when containers or Pods are replaced. Understanding the lifecycle of container filesystem versus EmptyDir versus PersistentVolumes is crucial.

### Configuration Management

The exam tests your understanding of how to configure containerized applications. ConfigMaps are a common pattern that appears in exam questions. You should know how to create a ConfigMap containing configuration files, how to mount it as a volume in a Pod, and that ConfigMaps are typically read-only when mounted.

### Azure Storage Integration

A key exam topic is understanding how AKS integrates with Azure storage services. Azure Managed Disks provide the default storage class with high-performance block storage for single-node access. Azure Files provide the azurefile storage class for shared storage across multiple nodes. The exam might present scenarios where you need to choose between these options based on requirements.

### Common Exam Scenarios

Let me share typical scenario-based questions you might encounter.

"You're deploying a web application with a database to AKS. The database needs persistent storage that survives Pod restarts and updates. What should you use?" The answer is to create a PersistentVolumeClaim and mount it to the database container. The PVC will provision Azure storage that persists beyond individual Pods.

"Your application needs to read configuration files that are the same across all Pods. The configuration should be updated without redeploying containers. What's the best approach?" The answer is to use a ConfigMap to store the configuration and mount it as a volume in your Pods.

"You have multiple Pods that need to read and write to the same files simultaneously. Which storage class should you use?" The answer is to use the azurefile storage class in your PVC because Azure Files supports multiple concurrent connections.

"Your application generates temporary cache files that don't need to persist beyond the Pod lifecycle. What's the most efficient storage approach?" The answer is to use an EmptyDir volume, which provides fast local storage that's automatically cleaned up when the Pod is deleted.

## Connection to Other Exam Topics

Kubernetes storage connects to several other AZ-204 exam domains. Understanding how AKS uses Azure Managed Disks and Azure Files relates to the broader Azure Storage domain. Using ConfigMaps demonstrates cloud-native configuration management, which relates to Azure App Configuration. Understanding storage access modes helps you design scalable solutions.

The exam may also test troubleshooting skills. Knowing how to use kubectl exec to inspect files inside containers, how to check PVC status, and how to identify storage-related issues is important.

## Best Practices

When working with Kubernetes storage, several best practices apply:

Match storage to requirements. Choose based on whether you need persistence, sharing capabilities, and specific performance characteristics. Consider the lifecycle of your data. Think about what happens when containers, Pods, or nodes are replaced.

Use abstractions properly. Prefer PersistentVolumeClaims over directly specifying Azure resources. This provides portability and follows Kubernetes best practices. Understand the defaults. Know what happens when you don't specify a storage class or access mode in your PVC.

Think about cost. Azure Managed Disks and Azure Files have different pricing models. The exam may present cost optimization scenarios where you need to choose the most economical option.

Plan for backup and disaster recovery. Persistent data needs backup strategies. Consider using Azure Backup for AKS or other backup solutions.

## Dynamic Provisioning

An important concept is dynamic provisioning. When you create a PersistentVolumeClaim, Kubernetes can automatically provision the underlying Azure storage resources. You don't need to manually create Azure Disks or File Shares through the Azure Portal. Kubernetes calls Azure APIs to create the resources based on the storage class and size you specified in your PVC.

This automation is powerful but means you need to ensure your AKS cluster has appropriate permissions to create Azure resources. AKS uses either a service principal or managed identity to interact with Azure, and these need contributor-level permissions on the resource group or subscription.

## StatefulSets and Persistent Storage

While this lab focused on Deployments, there's another Kubernetes workload type called StatefulSet that's specifically designed for stateful applications. StatefulSets provide stable network identities and stable persistent storage for each Pod replica.

When you scale a StatefulSet, each Pod gets its own PersistentVolumeClaim automatically. This is perfect for databases or other applications where each instance needs its own storage. Understanding when to use StatefulSets versus Deployments is exam knowledge.

## Key Takeaways

Let me summarize the essential points about Kubernetes storage.

Container filesystems are ephemeral. Data written to the container filesystem is lost when the container is recreated. ConfigMaps provide read-only configuration files that can be mounted as volumes, separating configuration from container images.

EmptyDir volumes survive container restarts within the same Pod but are lost when the Pod is deleted. They're ideal for temporary data and caching. PersistentVolumeClaims request storage that outlives individual Pods, providing true persistent storage for stateful applications.

Storage Classes define different types of storage with different properties. In AKS, Azure Managed Disks provide high-performance single-node storage, while Azure Files provide shared storage for multiple nodes. Understanding access modes - ReadWriteOnce versus ReadWriteMany - helps you choose the appropriate storage type.

For the AZ-204 exam, understand the lifecycle differences between storage types, know how to create and use PersistentVolumeClaims, understand when to use different Azure storage services through storage classes, and be able to identify the appropriate storage solution for different scenarios.

## Final Thoughts

Storage management is a critical aspect of running stateful applications in Kubernetes. The abstractions Kubernetes provides - volumes, PersistentVolumes, PersistentVolumeClaims, and Storage Classes - give you a powerful and portable way to work with storage across different platforms.

In Azure Kubernetes Service, these abstractions map to Azure storage services seamlessly. You get the benefits of Kubernetes portability while leveraging Azure's reliable, scalable storage infrastructure.

For the AZ-204 exam, this topic combines Kubernetes knowledge with Azure storage services knowledge. The exam tests both your understanding of the concepts and your ability to apply them to real-world scenarios. Practice creating applications with different storage patterns, experiment with different storage classes, and understand the behavior when Pods are deleted and recreated.

Thanks for listening to this episode on Kubernetes Storage in Azure Kubernetes Service. I hope this gives you a solid understanding of how to manage persistent storage in Kubernetes and how these concepts relate to the AZ-204 certification. Good luck with your studies!
