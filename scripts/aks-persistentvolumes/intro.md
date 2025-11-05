# Kubernetes Storage - Introduction

Welcome to this lab on Kubernetes Storage in Azure Kubernetes Service. In this session, we'll explore how to manage persistent storage for your containerized applications running in AKS.

## What We'll Cover

Kubernetes provides multiple abstractions to help you model your applications in a generic way that works across all clusters. When it comes to storage, Kubernetes uses volumes - these are storage units that you can mount into your application Pods.

The key concept here is that storage mounts appear as part of the container filesystem, but they're actually stored outside of the container. In AKS, this is backed by standard Azure resources like managed disks and file shares. This architecture gives you two important capabilities:

First, you can push configuration settings into containers as read-only files. This is perfect for managing application configuration without rebuilding your container images.

Second, you can store application state outside of the container. This is critical because containers are ephemeral - they can be replaced at any time. By storing data outside the container, you ensure that your application state persists even when containers are recreated.

## Storage Concepts in Kubernetes

We'll be working with several storage concepts in this lab:

**Volumes and Volume Mounts** - These are the basic building blocks. A volume is defined at the Pod level, and volume mounts connect those volumes to specific paths inside your containers.

**ConfigMaps as Volumes** - You can mount ConfigMaps as read-only volumes to inject configuration files into your containers. This is a clean way to separate configuration from your container images.

**EmptyDir Volumes** - These provide temporary storage that has the lifecycle of the Pod. If your container restarts, the data survives. But if the Pod is deleted, the EmptyDir goes away too.

**PersistentVolumeClaims** - These are requests for persistent storage that outlives individual Pods. You specify how much storage you need, and Kubernetes provisions it for you based on available storage classes.

## The Demo Application

For this lab, we'll be using a simple .NET 6.0 background worker application. This app reads configuration from files and writes data to various locations. It's perfect for demonstrating different storage patterns because we can easily see what happens to the data as we manipulate Pods and volumes.

The application writes to two locations - a cache file and a database file. By applying different volume types to these locations, we'll see exactly how each storage type behaves.

## Environment Setup

We'll start by working with a local Kubernetes cluster running in Docker Desktop. This gives us a fast iteration cycle for learning the concepts. Then we'll move to an Azure Kubernetes Service cluster to see how the same specifications work in a production cloud environment.

One of the beautiful things about Kubernetes is that our application specifications will work identically in both environments. The underlying storage implementation differs - local disk versus Azure storage services - but our application doesn't need to know or care about those differences.

Let's get started by setting up our environment and deploying our first version of the application.
