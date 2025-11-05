# AKS Ingress and Application Gateway - Introduction

## Opening

Welcome to this lab on Ingress and Application Gateway in Azure Kubernetes Service. In this session, we'll explore how to efficiently route network traffic into a Kubernetes cluster using Azure Application Gateway as an ingress controller.

## The Challenge

When you start running applications on Kubernetes, you quickly face a networking challenge. While you can route traffic using LoadBalancer Services that give you public IP addresses, this approach doesn't scale well.

Imagine running multiple applications on a single cluster. Do you really want to manage lots of random IP addresses? Probably not. That's where ingress comes in.

## The Solution

Instead of multiple IP addresses, you want a single entry point that routes incoming traffic based on HTTP domain names. This means a single Kubernetes cluster can serve multiple domains - like myapp.com, api.myapp.com, and otherapp.co.uk - all from one public IP address that you set in your DNS service.

Kubernetes supports this with Ingress objects, which integrate beautifully with the Azure Application Gateway service.

## What is Azure Application Gateway?

Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. It's more than just a standard load balancer - it operates at the application layer and can make routing decisions based on HTTP request attributes.

Key features include:
- Layer 7 load balancing
- URL-based routing
- SSL termination
- Web Application Firewall capabilities
- Auto-scaling support

## Application Gateway Ingress Controller

When you combine Application Gateway with AKS, the Application Gateway acts as an ingress controller. This means it automatically configures itself based on the Kubernetes Ingress resources you create in your cluster.

No manual configuration of routing rules needed - everything is managed through Kubernetes manifests.

## Lab Overview

In this lab, you'll:
1. Create an Azure Application Gateway with proper networking setup
2. Deploy an AKS cluster integrated with the Application Gateway
3. Use the AGIC add-on to connect them together
4. Deploy an application and expose it through an Ingress resource
5. Explore how the routing works in the Portal

This is a production-grade deployment pattern that you'll use for scalable, reliable, public-facing applications on Kubernetes.

Let's get started.
