# Azure SignalR Service - Quickfire Questions

## Question 1
What is Azure SignalR Service?


- A) A database service
- B) A managed service for real-time web functionality using WebSockets
- C) A messaging queue
- D) A monitoring service

**Answer: B**
Azure SignalR Service enables real-time bi-directional communication between servers and clients using WebSockets and fallback protocols.
---
## Question 2
What protocol does SignalR primarily use?


- A) SMTP
- B) FTP
- C) WebSockets with fallbacks (Server-Sent Events, Long Polling)
- D) HTTP only

**Answer: C**
SignalR prefers WebSockets but automatically falls back to Server-Sent Events or Long Polling if WebSockets aren't available.
---
## Question 3
What are common use cases for SignalR?


- A) Static websites
- B) File storage
- C) Real-time dashboards, chat apps, live notifications, collaborative apps
- D) Batch processing only

**Answer: C**
SignalR excels at scenarios requiring instant updates: dashboards, chat, gaming, IoT, live collaboration.
---
## Question 4
What are the SignalR service modes?


- A) Default, Serverless, Classic
- B) Public and Private
- C) Only one mode
- D) Fast and Slow

**Answer: A**
Default (app server manages connections), Serverless (Azure Functions only), Classic (backward compatibility).
---
## Question 5
What is the difference between Default and Serverless mode?


- A) Default uses app server for logic; Serverless uses only Azure Functions
- B) Serverless is always cheaper
- C) No difference
- D) Default doesn't work

**Answer: A**
Default mode: app server handles hub logic. Serverless mode: Azure Functions handle all logic without app server.
---
## Question 6
What is a SignalR hub?


- A) A monitoring dashboard
- B) A hardware device
- C) A storage container
- D) High-level pipeline enabling server and client to call methods on each other

**Answer: D**
Hubs provide the abstraction for bi-directional RPC-style communication between server and clients.
---
## Question 7
How can you scale SignalR across multiple servers?


- A) Requires load balancer only
- B) Cannot scale
- C) Azure SignalR Service acts as backplane, managing connections across multiple app servers
- D) Manual configuration only

**Answer: C**
SignalR Service manages all client connections and message routing, allowing your app servers to scale out seamlessly.
---
## Question 8
What authentication options does SignalR support?


- A) Only anonymous
- B) Only passwords
- C) Access keys, Azure AD, custom JWT validation
- D) None

**Answer: C**
SignalR supports access key authentication, Azure AD authentication, and custom JWT token validation.
---
## Question 9
Can SignalR work with Azure Functions?


- A) Requires VMs
- B) No integration
- C) Yes, using SignalR bindings for serverless real-time apps
- D) Only with App Service

**Answer: C**
Azure Functions have SignalR input/output bindings enabling serverless real-time applications.
---
## Question 10
What is the pricing model for SignalR Service?


- A) Free only
- B) Per function execution
- C) Based on units (concurrent connections) and message count
- D) Flat monthly rate

**Answer: C**
SignalR charges based on units (supporting concurrent connections) and the number of messages sent.