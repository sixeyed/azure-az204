# Azure Kubernetes Service - AZ-204 Exam Introduction

Great work deploying your first AKS cluster! Now let's focus on what the AZ-204 exam expects you to know about Azure Kubernetes Service.

## Exam Coverage

AKS appears in the "Implement containerized solutions" domain of the AZ-204 exam. While you won't be expected to be a Kubernetes expert, you need to understand how to deploy and manage containerized applications using AKS, and how AKS integrates with other Azure services.

## What We'll Cover

First, **creating and managing AKS clusters**. You need to know the `az aks create` command with essential parameters: resource group, cluster name, location, node count, and VM sizes. The exam may test your understanding of the managed resource group (prefixed with "MC_") that contains underlying infrastructure - and the critical rule that you should never manually modify resources in this managed group.

**Connecting to AKS clusters** is fundamental. Know the `az aks get-credentials` command that downloads cluster credentials and configures kubectl. This modifies your kubeconfig file to enable kubectl communication with your AKS cluster. The exam may also touch on Azure Active Directory integration and service principals for production authentication scenarios.

**Deploying applications to AKS** requires understanding key Kubernetes resources: Deployments (define how apps run, including container images, replicas, and update strategies), Services (expose apps to network traffic internally or externally), ConfigMaps (store configuration data), and Secrets (store sensitive data like connection strings). Know the `kubectl apply -f` command for deploying YAML manifests.

**Scaling applications** appears frequently on the exam. Understand horizontal pod scaling with `kubectl scale deployment` or by modifying the replicas field in your YAML. Also know about cluster scaling - adding or removing nodes using `az aks scale`.

**Integration with Azure Container Registry** is a key exam topic. AKS can pull images from ACR without additional authentication when properly configured. Know how to attach ACR to AKS using `az aks update --attach-acr`.

**Monitoring and diagnostics** involves understanding how to view pod logs with `kubectl logs`, describe resources with `kubectl describe`, and access container metrics. The exam may test troubleshooting scenarios.

We'll cover **AKS networking concepts** including ClusterIP (internal-only services), LoadBalancer (external services with public IPs), and NodePort services. Understand when to use each type.

**Node pools** let you have different VM types in the same cluster - Linux nodes, GPU nodes, Windows nodes. Know that you can have multiple node pools with different configurations serving different workload requirements.

Finally, we'll explore **common exam scenarios**: choosing between ACI and AKS, implementing auto-scaling, integrating with ACR securely, and troubleshooting common deployment issues.

Ready to master AKS for the AZ-204 exam? Let's dive into the exam-focused content!
