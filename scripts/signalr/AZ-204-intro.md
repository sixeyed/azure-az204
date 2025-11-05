# Azure SignalR Service - AZ-204 Exam Introduction

Great work with SignalR! This service appears in the AZ-204 exam's compute solutions domain, focusing on real-time communication capabilities.

## What We'll Cover

**Service configuration and deployment** is tested on the exam. You should know CLI commands for creating SignalR resources including resource group, SKU, location, and naming requirements. The service name becomes part of a public DNS endpoint at your-name.service.signalr.net. SKU selection matters: Free tier for development/testing with connection limits, Standard tier for production workloads, and Premium tier for higher scale.

**Authentication approaches** must be understood. Connection strings with access keys provide simpler approach for getting started but require managing sensitive credentials. Managed Identities are the preferred production approach - System-Assigned or User-Assigned identities on compute resources, connection strings using Managed Identity format with AuthType=azure.msi, and role assignments for authorization. The exam tests knowing when to use each approach.

**Role-Based Access Control** for SignalR requires knowing specific roles. SignalR App Server role is for application servers managing connections and sending messages. SignalR Service Owner provides full access. SignalR REST API Owner and Reader control REST API access. The exam may test understanding of which role to assign for different scenarios.

**Service modes** determine message routing. Default mode manages both server and client connections. Serverless mode is for Azure Functions integration where only clients connect to the service. Classic mode provides legacy behavior for backward compatibility. The exam tests understanding of when each mode is appropriate.

**Integration patterns** are important. App Service integration has web applications connecting to SignalR Service to broadcast messages, configured through app settings using Azure__SignalR__Enabled and Azure__SignalR__ConnectionString (double-underscore syntax for hierarchical configuration). Azure Functions integration uses SignalR bindings for serverless architectures. The exam tests understanding of configuration approaches.

**Scaling considerations** explain why SignalR Service exists. Without it, each web server maintains its own client connections causing users on different servers to not communicate. SignalR Service provides centralized hub architecture where all web servers send to the service, which broadcasts to all clients. This enables stateless web applications that easily scale. The exam tests understanding of the problem it solves.

**Limitations and considerations** include: not a persistence layer (broadcasts messages in real-time but doesn't store them), service mode implications affecting application architecture, connection limits requiring appropriate tier selection for production, and regional deployment with latency implications. The exam may present scenarios testing these limitations.

We'll cover **authentication and authorization separation** (authentication proves identity, authorization grants permissions through role assignments), **monitoring with Live Trace** for debugging message flow, **common scenarios** about choosing SignalR for real-time updates, troubleshooting authentication failures, and securing access with Managed Identities.

Master SignalR Service for the AZ-204!
