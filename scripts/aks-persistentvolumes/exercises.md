# Kubernetes Storage - Exercise Walkthrough

## Exercise 1: Setting Up the Environment

Let's start by creating a new Resource Group for our lab.

**Create the Resource Group**: We're creating a resource group called "labs-aks-persistentvolumes" in the East US region with a courselabs tag to help track our lab resources.

**Create the AKS Cluster**: Now we'll create a small AKS cluster. We're specifying one node with a Standard D2s v5 VM size to keep costs down, and using the no-wait flag so the cluster creates in the background while we continue working. This allows us to be productive while Azure provisions the infrastructure.

**Switch to Local Context**: While that's creating, we'll work with our local Docker Desktop cluster. First, let's make sure we're connected to the right context using kubectl config use-context docker-desktop.

**Verify Connection**: We're verifying we're connected to the local cluster by running kubectl get nodes. We should see our Docker Desktop node listed with a Ready status.

## Exercise 2: Working with ConfigMaps and Volume Mounts

Now let's deploy the first version of our application. This version uses a ConfigMap to load configuration settings.

**Understanding the Architecture**: If you look at the ConfigMap specification, you'll see it contains a complete appsettings.json file with logging and application configuration. The Deployment spec defines a Pod that loads this ConfigMap as a volume, mounting the appsettings.json file into the /app directory. It's important to understand the layers here: The ConfigMap stores the JSON file. The Pod defines the ConfigMap as a volume. And the container mounts that volume at a specific path.

**Deploy Version 1**: Let's deploy it using kubectl apply pointing to the v1 specs directory.

**Find the Pod**: Now we're finding our Pod using kubectl get pods. You should see a pod with a name starting with "queue-worker".

**Check the Logs**: Let's check the logs to verify the app is working using kubectl logs with the follow flag. You should see the application doing some work and then sleeping for 20 seconds in a loop. This is our background worker in action, processing messages from a simulated queue.

**Inspect Container Files**: Now, here's something useful - we can execute commands inside running containers using kubectl exec. Let's look at the cache file the app is writing using kubectl exec with the cat command to read /mnt/cache/app.cache. You'll see timestamped entries showing the worker's activity.

**Check the Database File**: Similarly, we're examining the database file at /mnt/database/app.db. Notice that each line includes the hostname, which in Kubernetes is actually the Pod name. This will help us track which Pod wrote which data, which becomes important when we test Pod replacement.

## Exercise 3: Understanding Container Storage Lifecycle

Here's a critical concept: When you write data inside a container without using volumes, that data has the same lifecycle as the container. Let's prove this.

**Delete the Pod**: We're deleting your Pod using kubectl delete pod. The Deployment will immediately start creating a replacement Pod - this is the self-healing nature of Kubernetes at work.

**Watch Pod Recreation**: We're watching it happen using kubectl get pods with the watch flag. You'll see the old Pod terminating while a new one is created and starts running.

**Check the Database Again**: When the new Pod is running, we're checking the database file again. You'll see that the database file only has entries from the new Pod. All the data from the previous Pod is gone - completely lost. This happens every time you update to a new container image, change any part of the Pod spec, or experience a node failure. The data lives and dies with the container.

## Exercise 4: EmptyDir and PersistentVolumeClaims

Now let's deploy version 2 of our application, which adds two writeable volumes to handle this problem.

**Understanding the Changes**: The v2 Deployment mounts the cache directory to an EmptyDir volume and the database directory to a PersistentVolumeClaim volume. There's also a separate PVC specification that models our persistent storage request.

As a reminder - EmptyDir is storage that lives with the Pod. If the container restarts, the data survives because the Pod is still there. But if the Pod gets deleted, so does the EmptyDir. It's useful for temporary data that needs to survive container restarts but doesn't need to survive Pod recreation.

PersistentVolumeClaim is different - it's a request for the cluster to provide storage that the Pod can attach to. We're just specifying the amount we need and the access mode, not the type of storage. Kubernetes finds suitable storage and binds it to our claim.

**Deploy Version 2**: We're deploying version 2 using kubectl apply pointing to the v2 specs directory.

**Let It Run**: Let the Pod run for a minute or so to generate some data, then we're checking both files using kubectl exec. You'll see entries accumulating in both the cache and database files.

**Delete the Pod Again**: Now we're deleting the Pod again to see what happens with our volumes.

**Watch the Replacement**: We're watching the replacement start using kubectl get pods with the watch flag.

**Compare the Results**: When it's running, we're checking both files again. Here's what you'll see: The cache file is new and only contains entries from the new Pod - the EmptyDir volume in this Pod replaced the old one. But the database file is retained - you'll see entries from both the old Pod and the new one, all in chronological order.

This is the key difference. The PersistentVolume has a separate lifecycle from any Pod, so the data persists until the volume itself is explicitly deleted.

## Exercise 5: Moving to AKS

Now let's try the same thing on our AKS cluster. First, we're connecting to it using az aks get-credentials. The overwrite flag replaces any existing credentials for a cluster with the same name.

**The Beauty of Portability**: The beautiful thing about Kubernetes is that we can use the exact same specifications. We're deploying v2 on AKS using the same kubectl apply command we used locally.

**Watch the Pod Start**: We're watching the Pod start using kubectl get pods with the watch flag.

**Test Pod Replacement**: Let it run for a bit, then we're deleting it to test persistence. Watch the replacement Pod come up, then check the database file using kubectl exec. You'll see entries from both Pods, just like on Docker Desktop. But where is this data actually stored?

## Exercise 6: Storage Classes

Kubernetes uses Storage Classes to define different types of storage. Let's see what's available using kubectl get storageclass.

**Understanding Platform Differences**: These are platform-specific. AKS offers Azure storage services - managed disks and file shares. Docker Desktop just uses the disk on your machine. But they both have a default Storage Class, which is why our PVC works without specifying a storage class - Kubernetes automatically uses the default.

**AKS Default Storage**: The default in AKS uses Azure managed disks. These provide excellent I/O performance with SSD-backed storage, but they can only be attached to one node at a time. This is called ReadWriteOnce access mode - one Pod can mount the volume for reading and writing, but you can't share it across multiple Pods on different nodes.

## Lab Challenge

For the lab exercise, you'll work with the Azure Files storage class. Unlike managed disks, Azure Files provides shared storage that can be accessed by multiple Pods on multiple nodes simultaneously using the ReadWriteMany access mode.

**Your Task**: Create a new PVC that specifies the azurefile storage class. Update the Deployment to use this new PVC for the database volume. Scale the Deployment to 3 replicas.

The application will work the same way, but now all three Pods will be writing to the same shared file. This means the database file will contain interleaved entries from all three Pods. And if you explore the Azure Portal, you should be able to navigate to your Storage Account, find the File Share that was automatically created, and download the database file directly - proving that it's real Azure Files storage.

This demonstrates an important concept: different storage types support different access patterns, and you need to choose the right one for your workload.

## Cleanup

When you're done, we're cleaning up by deleting the Resource Group using az group delete with the yes flag to skip confirmation and the no-wait flag to return immediately without waiting.

We're also switching back to Docker Desktop using kubectl config use-context. This ensures future kubectl commands target your local environment.

This cleanup removes all resources including the persistent volumes. In production, you'd want to be more careful - persistent volumes often contain important data that you want to back up or migrate before deletion.
