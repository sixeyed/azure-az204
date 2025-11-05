# Azure Functions SignalR - Quickfire Questions

## Question 1
What is Azure SignalR Service?


- A) A database service
- B) A monitoring service
- C) A messaging queue
- D) A managed service for real-time web functionality using WebSockets

**Answer: D**
Azure SignalR Service enables real-time bi-directional communication between servers and clients using WebSockets and fallback protocols.
---
## Question 2
What protocol does SignalR primarily use?


- A) FTP
- B) SMTP
- C) WebSockets with fallbacks (Server-Sent Events, Long Polling)
- D) HTTP only

**Answer: C**
SignalR prefers WebSockets but automatically falls back to Server-Sent Events or Long Polling if WebSockets aren't available.
---
## Question 3
How do Azure Functions integrate with SignalR Service?


- A) Only in Premium plan
- B) They cannot integrate
- C) Using SignalR input and output bindings
- D) Only through custom code

**Answer: C**
Azure Functions have built-in SignalR bindings for negotiation (input) and sending messages (output).
---
## Question 4
What is the negotiate function in SignalR with Functions?


- A) A monitoring function
- B) An authentication function
- C) An HTTP endpoint that provides connection info for SignalR clients
- D) A function that handles pricing

**Answer: C**
The negotiate function returns connection information (URL, access token) that clients use to connect to SignalR Service.
---
## Question 5
How can you send messages to specific users in SignalR?


- A) You cannot target specific users
- B) Using User IDs in SignalR output binding
- C) Only by broadcasting to all
- D) Using email addresses

**Answer: B**
SignalR supports sending to specific users via userId, to groups via groupName, or broadcasting to all connections.
---
## Question 6
What is a SignalR group?


- A) A logical collection of connections that can receive messages together
- B) A database table
- C) A subscription tier
- D) A billing group

**Answer: A**
Groups allow you to send messages to multiple connections simultaneously, useful for chat rooms or topic-based notifications.
---
## Question 7
How do clients typically connect to Azure SignalR Service with Functions?


- A) Direct connection to SignalR Service
- B) Call negotiate function, then connect to SignalR with returned connection info
- C) Through a VPN
- D) Using FTP

**Answer: B**
Clients first call the negotiate endpoint to get connection information, then use that to establish a SignalR connection.
---
## Question 8
What is the pricing model for Azure SignalR Service?


- A) Flat monthly rate
- B) Based on units (concurrent connections) and message count
- C) Free only
- D) Per function execution

**Answer: B**
SignalR Service charges based on units (supporting concurrent connections) and the number of messages sent.
---
## Question 9
Can SignalR clients receive messages from Azure Functions?


- A) Only through polling
- B) No, only send
- C) Only in Enterprise tier
- D) Yes, Functions can push messages to clients via output bindings

**Answer: D**
Azure Functions can push real-time messages to SignalR clients using SignalR output bindings.
---
## Question 10
What authentication options are available for SignalR Service?


- A) None
- B) Only password
- C) Access keys, Azure AD, managed identity
- D) Only anonymous

**Answer: C**
SignalR Service supports authentication via access keys, Azure AD authentication, and managed identities for secure connections.