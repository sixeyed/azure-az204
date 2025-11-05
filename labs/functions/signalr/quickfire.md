# Azure Functions SignalR - Quickfire Questions

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
How do Azure Functions integrate with SignalR Service?

- A) They cannot integrate
- B) Using SignalR input and output bindings
- C) Only through custom code
- D) Only in Premium plan

**Answer: B**
Azure Functions have built-in SignalR bindings for negotiation (input) and sending messages (output).

---

## Question 4
What is the negotiate function in SignalR with Functions?

- A) A function that handles pricing
- B) An HTTP endpoint that provides connection info for SignalR clients
- C) A monitoring function
- D) An authentication function

**Answer: B**
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

- A) A billing group
- B) A logical collection of connections that can receive messages together
- C) A database table
- D) A subscription tier

**Answer: B**
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

- A) Free only
- B) Based on units (concurrent connections) and message count
- C) Per function execution
- D) Flat monthly rate

**Answer: B**
SignalR Service charges based on units (supporting concurrent connections) and the number of messages sent.

---

## Question 9
Can SignalR clients receive messages from Azure Functions?

- A) No, only send
- B) Yes, Functions can push messages to clients via output bindings
- C) Only in Enterprise tier
- D) Only through polling

**Answer: B**
Azure Functions can push real-time messages to SignalR clients using SignalR output bindings.

---

## Question 10
What authentication options are available for SignalR Service?

- A) None
- B) Access keys, Azure AD, managed identity
- C) Only password
- D) Only anonymous

**Answer: B**
SignalR Service supports authentication via access keys, Azure AD authentication, and managed identities for secure connections.
