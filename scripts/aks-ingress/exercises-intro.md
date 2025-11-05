# AKS with Application Gateway Ingress - Exercises Introduction

We've discussed the challenge of managing multiple LoadBalancer services with random IP addresses, and how Application Gateway provides a centralized Layer 7 load balancing solution. Now let's implement it.

## What You'll Do

You'll start by **manually creating an Application Gateway** with its own dedicated subnet and public IP address. This gives you more control than automatic provisioning and helps you understand all the components involved. Application Gateway needs its own subnet that can't contain other resources - this is a key Azure networking requirement.

Then you'll **create an AKS cluster with Azure CNI networking**, which is required for Application Gateway integration. You'll **enable the AGIC (Application Gateway Ingress Controller) add-on** during cluster creation, which installs components that automatically configure Application Gateway based on Kubernetes Ingress resources.

Next, you'll **deploy the whoami application with an Ingress resource**. The Ingress is a Kubernetes object that defines HTTP routing rules - which domain names and paths should route to which services. You'll see how AGIC watches for Ingress resources and automatically translates them into Application Gateway configuration.

The really interesting part is **exploring the Portal to see the translation**. You'll examine how AGIC creates backend pools pointing to your AKS nodes, health probes to check pod availability, HTTP settings defining how to communicate with backends, and routing rules that map incoming requests to backend pools. This visual exploration helps you understand the automatic integration between Kubernetes and Azure networking.

You'll **test the application** using the Application Gateway's public IP address and see how it routes traffic to your pods. All your applications can now share a single public IP, with routing based on HTTP paths and domain names.

Let's implement centralized ingress for your AKS applications!
