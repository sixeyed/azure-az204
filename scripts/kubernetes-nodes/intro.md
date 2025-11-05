# Kubernetes Nodes - Introduction Script

**Duration:** 2-3 minutes
**Target:** AZ-204 exam candidates

---

## Slide 1: Title Slide

Welcome back! In this lesson, we're diving into Kubernetes Nodes - the fundamental building blocks of your cluster infrastructure. Understanding nodes is essential for the AZ-204 exam, especially when you're working with Azure Kubernetes Service.

---

## Slide 2: What Are Kubernetes Nodes?

So, what exactly is a node? In Kubernetes, a node is simply a worker machine - it could be a virtual machine or a physical server. Nodes are where your containerized applications actually run. Think of them as the workhorses of your cluster.

Each node contains the services necessary to run pods, which are managed by the Kubernetes control plane. When you deploy an application to Kubernetes, the control plane schedules your pods to run on available nodes.

---

## Slide 3: Node Architecture

Let's look at what's inside a node. Every node runs several key components:

First, there's the kubelet - this is the primary node agent that communicates with the Kubernetes control plane. It ensures containers are running and healthy.

Next, you have the container runtime - this is what actually runs your containers. In Azure Kubernetes Service, this is typically containerd.

Finally, there's kube-proxy - a network proxy that maintains network rules and enables communication to your pods.

---

## Slide 4: Node Pools in AKS

When working with Azure Kubernetes Service, you'll encounter node pools. A node pool is a group of nodes within a cluster that all have the same configuration.

You can have multiple node pools in a single AKS cluster, which is useful when you need different VM sizes for different workloads. For example, you might have one pool with CPU-optimized nodes for compute-intensive tasks, and another pool with memory-optimized nodes for databases.

---

## Slide 5: Node Capacity and Resources

Every node has a certain capacity - CPU cores, memory, and storage. Kubernetes tracks these resources carefully. When you request resources for your pods, Kubernetes uses this information to decide which node has enough capacity to run your workload.

You'll need to understand concepts like resource requests and limits, which we'll explore in the hands-on exercises.

---

## Slide 6: AZ-204 Exam Relevance

For the AZ-204 exam, you need to know how to:
- Inspect and query node information using kubectl
- Understand node capacity and resource allocation
- Work with node labels and selectors
- Troubleshoot node-related issues in AKS

You won't need to install or configure nodes from scratch - that's handled by AKS - but you do need to know how to work with them.

---

## Slide 7: Tools We'll Use

The primary tool for working with nodes is kubectl - the Kubernetes command-line interface. Throughout this lesson, you'll learn essential kubectl commands like:
- kubectl get nodes - to list nodes
- kubectl describe nodes - to see detailed information
- kubectl explain - to learn about Kubernetes resources

These commands are your bread and butter for cluster management.

---

## Slide 8: What's Next

In the exercises that follow, we'll get hands-on with kubectl. You'll learn how to examine nodes, query their properties, and extract specific information using different output formats.

By the end of this lesson, you'll be comfortable navigating your cluster's node infrastructure - a crucial skill for both the exam and real-world Azure development.

Let's get started!
