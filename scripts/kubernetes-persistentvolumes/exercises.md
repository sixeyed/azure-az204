# Kubernetes Persistent Volumes

## Reference

Persistent Volumes provide durable storage that survives Pod restarts and rescheduling, separating storage lifecycle from Pod lifecycle through an abstraction layer consisting of PersistentVolumes and PersistentVolumeClaims. PersistentVolumes represent actual storage resources provisioned by administrators or dynamically created using StorageClasses, while PersistentVolumeClaims are requests for storage that Pods use to mount volumes. This decoupling allows applications to request storage without knowing implementation details like whether it's backed by Azure Disks, Azure Files, or other storage systems.

## Introduction

Alright, let's get practical! In this hands-on lab, we're going to explore three different approaches to storing data in Kubernetes. We'll see firsthand what happens to data when containers and pods restart, and how persistent volumes solve our storage challenges. Let's jump right in.

---

## Part 1: Understanding the Container Writeable Layer

First, let's see the default behavior of containers. Every container has a writeable layer where applications can create and update files. But here's the catch: that data is tied to the container's lifecycle.

We're going to deploy a demo application. It's a Pi calculator website fronted by an Nginx proxy that caches responses for better performance. This is perfect for demonstrating data persistence because we can easily see whether cached data survives restarts.

Let's deploy the application by applying the specs from the persistentvolumes lab folder. Now we're browsing to the Pi calculator. We're requesting a calculation with 30,000 decimal places. Watch the response time here - it takes over a second to calculate and return the result. That's because it's doing real computation.

Now when we refresh, boom! Instant response. The result is served from Nginx's cache. Let's verify that cache exists.

We're going to exec into the Nginx proxy pod and list the temp directory. See those files? That's our cache data stored in the container's writeable layer.

Now here's where it gets interesting. Let's force the container to restart by sending a kill signal to process one, which is the main Nginx process. This will cause the container to crash and Kubernetes will automatically restart it.

Looking at kubectl get pods, the restart count went up by one. We have a fresh container now.

When we check the temp folder in the new container, it's completely empty. All our cache data is gone. And when we refresh the Pi calculator again, notice it takes that full second to recalculate. The cache is gone, so it's starting from scratch.

So what's the takeaway here? Data in the container's writeable layer only lives as long as the container itself. When the container restarts, that data disappears. For temporary data, that might be fine. But for anything important, we need a better solution.

---

## Part 2: Pod Storage with EmptyDir Volumes

Let's move up one level. Instead of storing data at the container level, we can use an EmptyDir volume. This creates an empty directory at the Pod level, which containers can mount.

The key difference is that EmptyDir volumes survive container restarts because they're tied to the Pod, not the container. Let's see this in action.

Looking at the updated deployment spec, we're defining an EmptyDir volume and mounting it to the temp directory in our Nginx container. Same path, but now it's backed by a volume at the Pod level.

Let's apply this updated configuration. Since we're changing the Pod spec, Kubernetes will create a new Pod with the EmptyDir volume. We're using kubectl wait here to pause until the new Pod is ready. This is a handy command for scripts and demonstrations where you want to ensure resources are fully initialized before proceeding.

Now let's refresh the Pi calculator. Again, we're starting fresh, so it takes time to calculate. But now the result gets cached in our EmptyDir volume. Looking at that temp directory again, you can see the cache files being created.

Now let's test the restart scenario by killing the Nginx process again to force a container restart. There's our restart count incrementing. New container, but same Pod.

And when we check the temp folder in the new container, our data is still there! The cache survived because the EmptyDir volume is attached to the Pod, not the individual container.

So when we refresh the Pi calculator, instant response. The new container immediately has access to the cached data from the previous container.

This is great for scenarios where data needs to survive container restarts but doesn't need to persist forever.

But here's the limitation. EmptyDir volumes are tied to the Pod lifecycle. If we delete the Pod, the Deployment will create a replacement Pod with a brand new, empty EmptyDir volume. All that data would be lost.

So EmptyDir is better than the container writeable layer, but it's still not truly persistent storage. For that, we need Persistent Volume Claims.

---

## Part 3: External Storage with Persistent Volume Claims

Now we're getting to the real solution for persistent storage. Persistent Volume Claims let us use external storage that has its own lifecycle, completely separate from containers and pods.

Let's start by looking at what storage options are available in our cluster. We're running kubectl get storageclass. This command shows the storage classes defined in our cluster. In Docker Desktop or k3d, you'll typically see just one default storage class. But in a production environment like Azure Kubernetes Service, you'd see multiple classes with different properties.

You might have premium SSD storage, standard HDD storage, or Azure Files for shared access. Each storage class has a provisioner that can create storage resources on demand.

Now let's create a Persistent Volume Claim. This is a pretty simple PVC spec. We're requesting 100 megabytes of storage with ReadWriteOnce access mode, which means one node can mount it for both reading and writing. We're not specifying a storage class, so it'll use the default.

Let's create that PVC by applying the configuration. As soon as we create it, the storage provisioner goes to work. Looking at kubectl get pvc and pv, we can see our PVC here. Depending on the provisioner, it might create the Persistent Volume immediately, or it might wait until a Pod actually claims it. In many cases, you'll see the PVC in a pending state until it's bound to a Pod.

Now let's update our Nginx deployment to use this PVC. This deployment spec references our PVC by name in the volumes section. The container mounts this volume to the temp directory, just like before. But now it's backed by persistent storage.

Let's apply this configuration and wait for the Pod to be ready. Now looking at the status with kubectl get pvc and pv commands again, the PVC is bound, and we can see the Persistent Volume that was created for it. The volume shows the size we requested and the access mode from our PVC spec. This is dynamic provisioning in action.

The PVC starts empty, so let's refresh our Pi calculator to populate the cache. There's our cache data being written to the Persistent Volume.

Now comes the real test. Let's verify that this data survives not just container restarts, but Pod replacements too.

First, let's restart the container by killing the Nginx process. Container restarted - new container, same Pod, same PVC. Our cache data is definitely still there. And the app serves the cached response instantly.

But here's the big test. Let's completely replace the Pod using kubectl rollout restart. This forces Kubernetes to replace the Pod entirely. This is different from a container restart. We're getting a brand new Pod.

Watch the Pod name - the old Pod terminates and a new Pod gets created with a different name. This is a completely new Pod instance.

But when we check the temp directory in this new Pod, all our cache data is still there! That's because the Persistent Volume exists independently. When the new Pod starts, it mounts the same PVC, which is bound to the same Persistent Volume with all our data intact.

And sure enough, the Pi calculator still serves the cached response instantly. Data persistence across Pod replacements. That's the power of Persistent Volume Claims.

So let's recap what we've learned about data lifecycles in Kubernetes. Container writeable layer - data lives as long as the container. EmptyDir volumes - data lives as long as the Pod. Persistent Volumes - data has its own lifecycle and survives until you explicitly delete the Persistent Volume.

This is crucial for running stateful applications like databases, content management systems, or anything else that needs to maintain state across restarts and updates.

---

## Lab Challenge Section

Now, here's a challenge for you. There's actually an easier way to get persistent storage that doesn't require a PVC, but it's not as flexible and it comes with serious security concerns.

The challenge is to run a simple sleep Pod with a different type of volume called a host path volume. This gives you direct access to the node's filesystem where the Pod is running.

Your mission, should you choose to accept it, is to use that sleep Pod to find the cache files from the Nginx Pod. Where on the node's filesystem are those cache files actually stored?

This is a great exercise to understand how Persistent Volumes work under the hood and why Kubernetes provides these abstractions rather than just letting everyone access the host filesystem directly.

Give it a try, and check the hints file if you get stuck. There's also a solution file, but try to figure it out yourself first. That's where the real learning happens.

---

## Closing

Great work! You've now seen three different approaches to storage in Kubernetes, each with its own use cases and lifecycle characteristics. Understanding these options is essential for designing resilient applications in Kubernetes.

In the next video, we'll connect this to the AZ-204 exam and discuss how these concepts specifically apply to Azure Kubernetes Service. See you there!
