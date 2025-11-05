# AKS with Application Gateway Ingress - AZ-204 Exam Introduction

Great job setting up Application Gateway ingress! Now let's focus on what the AZ-204 exam expects you to know about AKS networking and ingress patterns.

## Exam Coverage

This topic covers containerized solutions (AKS deployment and configuration), networking (Application Gateway integration), and security (VNet segmentation and RBAC). Expect scenario questions about choosing the right load balancing solution and troubleshooting ingress issues.

## What We'll Cover

**Layer 4 vs Layer 7 load balancing** is fundamental. Azure Load Balancer operates at Layer 4 (transport layer) and makes routing decisions based on IP address and port - it's fast but not content-aware. Application Gateway operates at Layer 7 (application layer) and can route based on HTTP headers, paths, and domains - it's more intelligent but adds latency. The exam tests when to use each.

**Service types in Kubernetes** appear frequently. ClusterIP makes services accessible only within the cluster (internal communication). NodePort exposes services on a specific port on every node (rarely used in production). LoadBalancer provisions an Azure Load Balancer with public IP (each service gets its own IP). Ingress uses Layer 7 routing to share a single IP across multiple services. Know when to use each type.

**Azure CNI vs kubenet networking plugins** is a common exam topic. Azure CNI gives each pod a VNet IP address, enabling service endpoints and network policies, but consumes more IP addresses from your VNet. Kubenet uses an overlay network where pods get IPs from a separate range, which is more IP-efficient but doesn't support service endpoints. Scenario questions test which to choose based on requirements like IP address availability and security needs.

**Application Gateway requirements** need to be understood. AGIC requires Standard_v2 or WAF_v2 SKU (v1 isn't supported). Application Gateway needs its own dedicated subnet that can't contain other resources. The subnet must be large enough for scale-out instances. Know these constraints for design questions.

**AGIC architecture** may appear in troubleshooting scenarios. Understand that AGIC runs as a pod in your cluster, watches Kubernetes Ingress resources, and translates them into Application Gateway configuration via Azure ARM API. If ingress isn't working, check AGIC pod logs, verify managed identity permissions, and ensure Application Gateway is in the same VNet.

We'll cover **ingress annotations** for controlling Application Gateway behavior, **SSL termination** patterns, **WAF integration** for security, and **common exam scenarios** about choosing and troubleshooting ingress solutions.

Master ingress patterns for the AZ-204!
