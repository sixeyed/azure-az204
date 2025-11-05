# Kubernetes Persistent Volumes - Introduction

## Video Narration Script (2-3 minutes)

---

### Opening (15 seconds)

Welcome back! Today we're diving into one of the most critical aspects of running stateful applications in Kubernetes: Persistent Volumes and Persistent Volume Claims.

If you've ever wondered how applications store data that survives pod restarts, or how Kubernetes handles database storage, you're in the right place. Let's get started.

---

### Slide 1: The Storage Challenge (30 seconds)

So here's the problem we're solving. By default, when a container writes data to its filesystem, that data lives inside the container. When the container restarts or gets replaced, all that data disappears.

Imagine running a database where all your data vanishes every time a pod restarts. That's obviously not going to work for production applications. We need storage that persists beyond the lifecycle of individual containers and pods.

---

### Slide 2: The Kubernetes Storage Abstraction (45 seconds)

This is where Kubernetes really shines with its storage abstraction layer. Instead of your application having to know whether it's running on AWS, Azure, or on-premises hardware, Kubernetes provides a clean separation between storage consumers and storage providers.

At the center of this abstraction are two key resources: Persistent Volumes and Persistent Volume Claims. Think of it like this: a Persistent Volume is the actual storage resource, like a disk or network file share. A Persistent Volume Claim is your application's request for storage.

Your application says "I need 100 gigabytes of storage with read-write access" and Kubernetes handles the rest. The application doesn't need to know if that's an Azure Disk, an AWS EBS volume, or local storage. This abstraction is powerful because it keeps your application portable.

---

### Slide 3: Storage Classes and Dynamic Provisioning (45 seconds)

Now, let's talk about Storage Classes. In a production Kubernetes cluster, especially in cloud environments like Azure Kubernetes Service, you'll have multiple storage options available. Each one has different characteristics.

You might have fast SSD storage for databases, slower but cheaper storage for backups, or shared file systems for applications that need concurrent access. Storage Classes define these different types of storage available in your cluster.

The real magic happens with dynamic provisioning. When your application creates a Persistent Volume Claim, Kubernetes can automatically provision the storage on-demand. You don't need to pre-create volumes. You just describe what you need, and the storage provisioner creates it for you. This makes scaling and managing applications much simpler.

---

### Slide 4: Access Modes (20 seconds)

Let's quickly cover access modes. When you request storage, you specify how it can be accessed. Read-Write Once means one node can mount it for reading and writing. Read-Only Many allows multiple nodes to mount it read-only. And Read-Write Many lets multiple nodes mount it with write access. The mode you choose depends on your application's requirements.

---

### Slide 5: AZ-204 Exam Relevance (25 seconds)

For those of you preparing for the AZ-204 exam, persistent storage is absolutely critical. You need to understand how Azure Kubernetes Service integrates with Azure Disks and Azure Files. You'll encounter scenarios about stateful applications, data persistence strategies, and choosing the right storage solution for different workload types.

The exam expects you to know when to use managed disks versus file shares, how to configure persistent volume claims, and how applications consume persistent storage in AKS.

---

### Closing (10 seconds)

Alright, now that we've covered the concepts, let's get hands-on. In the next section, we'll walk through practical examples showing different storage options in action. See you there!

---

## Slide Deck Structure

### Slide 1: Title Slide
- Title: "Kubernetes Persistent Volumes"
- Subtitle: "Storage That Survives Pod Restarts"
- Visual: Kubernetes logo with storage icons

### Slide 2: The Storage Challenge
- Diagram showing container lifecycle
- Container writing data → Container crashes → Data lost
- Highlight the problem statement in red

### Slide 3: The Kubernetes Storage Abstraction
- Layered architecture diagram:
  - Top: Application Pod
  - Middle: Persistent Volume Claim (abstraction layer)
  - Bottom: Persistent Volume (actual storage)
- Show cloud provider logos (Azure, AWS, GCP) at bottom

### Slide 4: Storage Classes and Dynamic Provisioning
- Table showing different storage types:
  - Storage Class | Performance | Use Case
  - Premium SSD | High | Databases
  - Standard HDD | Medium | General purpose
  - Azure Files | Shared | Multi-pod apps
- Animation showing PVC → Storage Class → Auto-provision PV

### Slide 5: Access Modes
- Three boxes with icons:
  - ReadWriteOnce (RWO) - Single node access
  - ReadOnlyMany (ROX) - Multi-node read
  - ReadWriteMany (RWX) - Multi-node write
- Color code by usage frequency (green for common, yellow for less common)

### Slide 6: AZ-204 Exam Relevance
- Checklist of key topics:
  - ✓ Azure Disk integration with AKS
  - ✓ Azure Files for shared storage
  - ✓ Stateful application patterns
  - ✓ PVC configuration and binding
  - ✓ Storage class selection
- Badge or icon representing AZ-204 certification

### Slide 7: Coming Up Next
- Screenshot preview of lab environment
- Bullet points of what we'll demonstrate
- "Let's get hands-on!" call-to-action
