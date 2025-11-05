# Azure Front Door - Introduction Narration Script

## Opening

Welcome to this lab on Azure Front Door. In this session, we'll explore one of Azure's most powerful global load balancing and content delivery solutions.

## What is Azure Front Door?

Azure Front Door is Microsoft's modern cloud CDN that provides fast, reliable, and secure access to your applications. Think of it as Application Gateway, but with a global CDN built right in.

While Application Gateway operates at the regional level, Front Door works globally across all Azure regions. This means your users get routed to the nearest available backend, providing optimal performance regardless of where they're located.

## Key Features

Front Door brings together several critical capabilities:

First, it provides global load balancing. Unlike regional load balancers, Front Door can distribute traffic across multiple regions, ensuring high availability and optimal performance for users worldwide.

Second, it includes integrated CDN capabilities. Static resources can be cached at edge locations around the world, reducing latency and improving user experience.

Third, it supports Web Application Firewall integration. You can protect your applications from common web vulnerabilities and exploits using the same WAF functionality available in Application Gateway.

Fourth, it provides DDoS protection, helping shield your applications from distributed denial of service attacks.

Finally, it offers intelligent routing based on performance, health, and weighted load balancing configurations.

## Evolution of Azure Services

Front Door represents the evolution of various Azure load balancing and CDN services. It combines the best features of Traffic Manager, Content Delivery Network, and Application Gateway into a single, comprehensive solution.

Microsoft now recommends Front Door as the preferred option for the frontend to your HTTP services. This includes Web Apps, API Management domains, and any other HTTP-based applications you want to expose to users.

## Use Cases

Front Door is ideal when you need:

- Global load balancing across multiple regions
- CDN capabilities for static content
- Web application firewall protection
- SSL offloading and certificate management
- Advanced routing based on URL paths or headers
- Session affinity for stateful applications

## Lab Overview

In this lab, we'll create and configure Azure Front Door with Web Application Firewall. We'll deploy backend applications in multiple regions, configure Front Door to route traffic between them, and apply security policies to protect against common threats.

By the end of this lab, you'll understand how to architect and implement a globally distributed application using Azure Front Door.

Let's get started.
