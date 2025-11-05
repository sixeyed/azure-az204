# Kubernetes Services: Exercises Introduction

We've covered how Services provide stable networking endpoints for pods enabling service discovery and load balancing. Now let's create different service types and understand their use cases.

## What You'll Do

You'll create ClusterIP services providing internal cluster networking with stable IP addresses and DNS names. Pods access services via DNS regardless of which backend pods are currently running.

Then you'll explore NodePort services exposing applications on static ports across all nodes. This provides external access for development and testing but isn't ideal for production due to port management challenges.

You'll work with LoadBalancer services in Azure Kubernetes Service that automatically provision Azure Load Balancers with public IP addresses. This is the standard way to expose production HTTP and TCP services externally.

Next, you'll understand service selectors using labels to identify backend pods. Services automatically maintain endpoint lists as pods are created, updated, or deleted, ensuring traffic only reaches healthy pods.

You'll explore session affinity and load balancing algorithms including round-robin for default distribution and client IP affinity for sticky sessions when applications require consistent routing to the same pod.

You'll work with headless services where ClusterIP is set to None providing direct DNS records for individual pods. This enables custom load balancing for stateful applications like databases.

The lab challenge asks you to configure an Ingress Controller with a LoadBalancer service, then create multiple applications accessed through a single external IP using Ingress path-based routing.

The key learning: Services abstract pod networking providing stable endpoints, automatic load balancing, and service discovery via DNS - essential for building reliable microservices architectures in Kubernetes.
