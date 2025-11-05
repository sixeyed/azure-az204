# AKS with Persistent Volumes - Exercises Introduction

We've covered Kubernetes storage abstractions for managing persistent data in containerized applications. Now let's see these concepts in action and understand how data survives (or doesn't survive) container and pod lifecycle events.

## What You'll Do

You'll work with **both local Docker Desktop and AKS clusters using identical specifications**, demonstrating the portability of Kubernetes. The demo application writes to cache and database files, letting you observe how different storage types behave.

First, you'll discover that **container filesystem data is ephemeral** - when you delete a pod, all data written to the container's filesystem is lost forever. This is by design: containers are meant to be disposable.

Then you'll explore **EmptyDir volumes**, which are pod-scoped temporary storage. EmptyDir volumes survive container restarts (if a container crashes, Kubernetes can restart it and data persists), but they're deleted when the pod is deleted. This is useful for temporary data sharing between containers in the same pod, but not for data that needs to survive pod replacement.

Next comes the real solution: **PersistentVolumeClaims (PVCs)**. These request storage from Kubernetes with specific characteristics like size and access mode. When you delete and recreate a pod, the PVC remains and reconnects to the new pod - your data persists! You'll see how this works in practice by writing data, deleting the pod, and verifying the data is still there when the pod restarts.

You'll explore **Storage Classes in AKS**, which define different types of storage. The default storage class uses Azure Managed Disks, which are high-performance but support only ReadWriteOnce (single pod can mount). You'll also see Azure Files storage class, which supports ReadWriteMany (multiple pods can mount the same volume concurrently) - perfect for shared data scenarios.

The **lab challenge** involves creating a shared volume for multiple application replicas, demonstrating when ReadWriteMany is necessary and how Azure Files enables this scenario.

Let's master persistent storage in Kubernetes!
