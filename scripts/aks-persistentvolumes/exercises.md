# Kubernetes Storage - Exercise Walkthrough

## Exercise 1: Setting Up the Environment

Let's start by creating a new Resource Group for our lab. I'm going to create a resource group called "labs-aks-persistentvolumes" in the East US region with a courselabs tag:

```
az group create -n labs-aks-persistentvolumes --tags courselabs=azure -l eastus
```

Now we'll create a small AKS cluster. I'm specifying one node with a Standard D2s v5 VM size, and using the no-wait flag so the cluster creates in the background:

```
az aks create -g labs-aks-persistentvolumes -n aks02 --node-count 1 --node-vm-size Standard_D2s_v5 --no-wait --location eastus
```

While that's creating, we'll work with our local Docker Desktop cluster. First, let's make sure we're connected to the right context:

```
kubectl config use-context docker-desktop
```

And verify we're connected to the local cluster:

```
kubectl get nodes
```

Perfect. We should see our Docker Desktop node listed.

## Exercise 2: Working with ConfigMaps and Volume Mounts

Now let's deploy the first version of our application. This version uses a ConfigMap to load configuration settings.

If you look at the ConfigMap specification, you'll see it contains a complete appsettings.json file with logging and application configuration. The Deployment spec defines a Pod that loads this ConfigMap as a volume, mounting the appsettings.json file into the /app directory.

It's important to understand the layers here: The ConfigMap stores the JSON file. The Pod defines the ConfigMap as a volume. And the container mounts that volume at a specific path.

Let's deploy it:

```
kubectl apply -f labs/aks-persistentvolumes/specs/v1
```

Now let's find our Pod:

```
kubectl get pods
```

And check the logs to verify the app is working:

```
kubectl logs -f <pod-name>
```

You should see the application doing some work and then sleeping for 20 seconds in a loop. This is our background worker in action.

Now, here's something useful - we can execute commands inside running containers using kubectl exec. Let's look at the files the app is writing:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/cache/app.cache
```

And the database file:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/database/app.db
```

Notice that each line includes the hostname, which in Kubernetes is actually the Pod name. This will help us track which Pod wrote which data.

## Exercise 3: Understanding Container Storage Lifecycle

Here's a critical concept: When you write data inside a container without using volumes, that data has the same lifecycle as the container. Let's prove this.

Delete your Pod:

```
kubectl delete pod <pod-name>
```

The Deployment will immediately start creating a replacement Pod. Watch it happen:

```
kubectl get pods --watch
```

When the new Pod is running, check the database file again:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/database/app.db
```

You'll see that the database file only has entries from the new Pod. All the data from the previous Pod is gone. This happens every time you update to a new container image or change any part of the Pod spec.

## Exercise 4: EmptyDir and PersistentVolumeClaims

Now let's deploy version 2 of our application, which adds two writeable volumes to handle this problem.

The v2 Deployment mounts the cache directory to an EmptyDir volume and the database directory to a PersistentVolumeClaim volume. There's also a separate PVC specification that models our persistent storage request.

As a reminder - EmptyDir is storage that lives with the Pod. If the container restarts, the data survives. But if the Pod gets deleted, so does the EmptyDir.

PersistentVolumeClaim is different - it's a request for the cluster to provide storage that the Pod can attach to. We're just specifying the amount we need, not the type of storage.

Deploy version 2:

```
kubectl apply -f ./labs/aks-persistentvolumes/specs/v2
```

Let the Pod run for a minute or so, then check both files:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/cache/app.cache
kubectl exec -it deploy/queue-worker -- cat /mnt/database/app.db
```

Now delete the Pod again:

```
kubectl delete pod <pod-name>
```

Watch the replacement start:

```
kubectl get pods --watch
```

When it's running, check both files again:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/cache/app.cache
kubectl exec -it deploy/queue-worker -- cat /mnt/database/app.db
```

Here's what you'll see: The cache file is new - the EmptyDir volume in this Pod replaced the old one. But the database file is retained - you'll see entries from both the old Pod and the new one.

This is the key difference. The PersistentVolume has a separate lifecycle from any Pod, so the data persists until the volume itself is deleted.

## Exercise 5: Moving to AKS

Now let's try the same thing on our AKS cluster. First, connect to it:

```
az aks get-credentials -g labs-aks-persistentvolumes -n aks02 --overwrite
```

The beautiful thing about Kubernetes is that we can use the exact same specifications. Deploy v2 on AKS:

```
kubectl apply -f ./labs/aks-persistentvolumes/specs/v2
```

Watch the Pod start:

```
kubectl get pods --watch
```

Let it run for a bit, then delete it:

```
kubectl delete pod <pod-name>
```

Watch the replacement:

```
kubectl get pods --watch
```

Check the database file:

```
kubectl exec -it deploy/queue-worker -- cat /mnt/database/app.db
```

You'll see entries from both Pods, just like on Docker Desktop. But where is this data actually stored?

## Exercise 6: Storage Classes

Kubernetes uses Storage Classes to define different types of storage. Let's see what's available:

```
kubectl get storageclass
```

These are platform-specific. AKS offers Azure storage services - managed disks and file shares. Docker Desktop just uses the disk on your machine. But they both have a default Storage Class, which is why our PVC works without specifying a storage class.

The default in AKS uses Azure managed disks. These provide excellent I/O performance, but they can only be attached to one node at a time.

## Lab Challenge

For the lab exercise, you'll work with the Azure Files storage class. Unlike managed disks, Azure Files provides shared storage that can be accessed by multiple Pods on multiple nodes simultaneously.

Your task is to:
1. Create a new PVC that specifies the azurefile storage class
2. Update the Deployment to use this new PVC for the database volume
3. Scale the Deployment to 3 replicas

The application will work the same way, but now all three Pods will be writing to the same shared file. And if you explore the Azure Portal, you should be able to access and download the database file directly from the Azure File Share.

## Cleanup

When you're done, clean up by deleting the Resource Group:

```
az group delete -y --no-wait -n labs-aks-persistentvolumes
```

And switch back to Docker Desktop:

```
kubectl config use-context docker-desktop
```

This removes all resources including the persistent volumes.
