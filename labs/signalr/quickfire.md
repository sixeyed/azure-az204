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

- A) HTTP only
- B) WebSockets with fallbacks (Server-Sent Events, Long Polling)
- C) FTP
- D) SMTP

**Answer: B**
SignalR prefers WebSockets but automatically falls back to Server-Sent Events or Long Polling if WebSockets aren't available.

---

## Question 3
What are common use cases for SignalR?

- A) Batch processing only
- B) Real-time dashboards, chat apps, live notifications, collaborative apps
- C) Static websites
- D) File storage

**Answer: B**
SignalR excels at scenarios requiring instant updates: dashboards, chat, gaming, IoT, live collaboration.

---

## Question 4
What are the SignalR service modes?

- A) Only one mode
- B) Default, Serverless, Classic
- C) Fast and Slow
- D) Public and Private

**Answer: B**
Default (app server manages connections), Serverless (Azure Functions only), Classic (backward compatibility).

---

## Question 5
What is the difference between Default and Serverless mode?

- A) No difference
- B) Default uses app server for logic; Serverless uses only Azure Functions
- C) Serverless is always cheaper
- D) Default doesn't work

**Answer: B**
Default mode: app server handles hub logic. Serverless mode: Azure Functions handle all logic without app server.

---

## Question 6
What is a SignalR hub?

- A) A hardware device
- B) High-level pipeline enabling server and client to call methods on each other
- C) A storage container
- D) A monitoring dashboard

**Answer: B**
Hubs provide the abstraction for bi-directional RPC-style communication between server and clients.

---

## Question 7
How can you scale SignalR across multiple servers?

- A) Cannot scale
- B) Azure SignalR Service acts as backplane, managing connections across multiple app servers
- C) Manual configuration only
- D) Requires load balancer only

**Answer: B**
SignalR Service manages all client connections and message routing, allowing your app servers to scale out seamlessly.

---

## Question 8
What authentication options does SignalR support?

- A) None
- B) Access keys, Azure AD, custom JWT validation
- C) Only passwords
- D) Only anonymous

**Answer: B**
SignalR supports access key authentication, Azure AD authentication, and custom JWT token validation.

---

## Question 9
Can SignalR work with Azure Functions?

- A) No integration
- B) Yes, using SignalR bindings for serverless real-time apps
- C) Only with App Service
- D) Requires VMs

**Answer: B**
Azure Functions have SignalR input/output bindings enabling serverless real-time applications.

---

## Question 10
What is the pricing model for SignalR Service?

- A) Free only
- B) Based on units (concurrent connections) and message count
- C) Per function execution
- D) Flat monthly rate

**Answer: B**
SignalR charges based on units (supporting concurrent connections) and the number of messages sent.
