# Azure Functions RabbitMQ - Quickfire Questions

## Question 1
What is RabbitMQ?


- A) A database
- B) An open-source message broker that implements AMQP
- C) A web server
- D) A storage service

**Answer: B**
RabbitMQ is a popular open-source message broker that implements the Advanced Message Queuing Protocol (AMQP).
---
## Question 2
How do Azure Functions integrate with RabbitMQ?


- A) No integration available
- B) Only through HTTP calls
- C) Through RabbitMQ trigger and output bindings (extension)
- D) Manual polling only

**Answer: C**
Azure Functions support RabbitMQ through the RabbitMQ extension, providing triggers and output bindings.
---
## Question 3
What protocol does the RabbitMQ binding use?


- A) AMQP (Advanced Message Queuing Protocol)
- B) MQTT
- C) FTP
- D) HTTP

**Answer: A**
RabbitMQ bindings use AMQP 0.9.1 protocol for communication with RabbitMQ servers.
---
## Question 4
What is required to use RabbitMQ triggers in Azure Functions?


- A) Queue name to monitor
- B) RabbitMQ extension must be installed
- C) All of the above
- D) Connection string to RabbitMQ instance

**Answer: C**
You need the RabbitMQ extension, a connection string (host, credentials), and the queue name to monitor.
---
## Question 5
Can you host RabbitMQ on Azure?


- A) Yes, on VMs, AKS, or third-party managed services
- B) Only locally
- C) Only on Azure Service Bus
- D) No, not supported

**Answer: A**
RabbitMQ can run on Azure VMs, container services (ACI, AKS), or use third-party managed RabbitMQ services.
---
## Question 6
What is an exchange in RabbitMQ?


- A) A database table
- B) A monitoring tool
- C) A storage account
- D) A routing component that receives messages and routes them to queues based on rules

**Answer: D**
Exchanges receive messages from producers and route them to queues based on routing keys and binding rules.
---
## Question 7
What are the main exchange types in RabbitMQ?


- A) Queue and Stack
- B) FIFO and LIFO
- C) Direct, Fanout, Topic, Headers
- D) Public and Private

**Answer: C**
RabbitMQ supports Direct (routing key match), Fanout (broadcast), Topic (pattern match), and Headers (attribute match) exchanges.
---
## Question 8
How does RabbitMQ differ from Azure Service Bus?


- A) Service Bus doesn't support queues
- B) RabbitMQ is open-source and self-managed; Service Bus is fully managed Azure service
- C) No difference
- D) RabbitMQ is Azure-only

**Answer: B**
RabbitMQ is open-source and requires management; Azure Service Bus is a fully managed cloud service with similar features.
---
## Question 9
What is message acknowledgment in RabbitMQ?


- A) A greeting message
- B) Message encryption
- C) Message routing
- D) Confirmation from consumer that message was successfully processed

**Answer: D**
Acknowledgment confirms successful processing. Without acknowledgment, messages are redelivered ensuring at-least-once delivery.
---
## Question 10
Can RabbitMQ messages be persisted across server restarts?


- A) No, always in-memory only
- B) Only in paid versions
- C) Automatic for all messages
- D) Yes, if queue and messages are marked as durable/persistent

**Answer: D**
Queues must be declared as durable and messages published with persistent delivery mode to survive restarts.