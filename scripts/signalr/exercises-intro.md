# Azure SignalR Service - Exercises Introduction

We've covered Azure SignalR Service as a managed solution for real-time, two-way communication between web applications and clients, solving the scaling challenges of self-hosted SignalR. Now let's implement real-time broadcasting across multiple server instances.

## What You'll Do

You'll start by **running a SignalR chat application locally** on a single server to understand how SignalR works at its core. You'll exchange messages between browser windows and observe real-time updates without client-side refreshing - this is SignalR using WebSockets to push updates.

Then you'll **observe the scaling problem** by running multiple instances on different ports. Messages aren't shared between servers because each SignalR server maintains its own isolated list of connections in memory. Users see completely different conversations depending on which server they're connected to - exactly the problem Azure SignalR Service solves.

You'll **create an Azure SignalR Service instance** using the Azure CLI with the Free tier, which is perfect for learning and testing. You'll see the Keys blade showing two authentication approaches: connection strings with access keys for development, and connection strings for Managed Identities for production.

Next, you'll **connect your local application to Azure SignalR Service** by passing configuration settings enabling SignalR Service mode. Both server instances use the same SignalR connection string, pointing to the same Azure service. Now messages are shared between clients on different servers - the Azure SignalR Service acts as the central hub.

You'll **deploy the application to Azure App Service** using the webapp up command, which creates and deploys everything in one operation. Then comes the important part: **configuring Managed Identity authentication** instead of connection strings with keys.

You'll **enable System-Assigned Managed Identity** on the App Service and **configure role-based access** with the SignalR App Server role. This demonstrates the separation of authentication (proving identity) and authorization (granting permissions) - the Managed Identity authenticates, but needs explicit role assignment to be authorized.

The key learning: Azure SignalR Service solves the scaling challenge by centralizing connection management, enabling multiple web server instances to share connections. Managed Identities with role-based access control eliminate the need to manage connection strings with embedded secrets.

Let's build scalable real-time applications with SignalR!
