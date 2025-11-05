# Azure Functions RabbitMQ - Quickfire Questions

## Question 1
What is RabbitMQ?

- A) A database
- B) An open-source message broker that implements AMQP
- C) A storage service
- D) A web server

**Answer: B**
RabbitMQ is a popular open-source message broker that implements the Advanced Message Queuing Protocol (AMQP).

---

## Question 2
How do Azure Functions integrate with RabbitMQ?

- A) No integration available
- B) Through RabbitMQ trigger and output bindings (extension)
- C) Only through HTTP calls
- D) Manual polling only

**Answer: B**
Azure Functions support RabbitMQ through the RabbitMQ extension, providing triggers and output bindings.

---

## Question 3
What protocol does the RabbitMQ binding use?

- A) HTTP
- B) AMQP (Advanced Message Queuing Protocol)
- C) MQTT
- D) FTP

**Answer: B**
RabbitMQ bindings use AMQP 0.9.1 protocol for communication with RabbitMQ servers.

---

## Question 4
What is required to use RabbitMQ triggers in Azure Functions?

- A) RabbitMQ extension must be installed
- B) Connection string to RabbitMQ instance
- C) Queue name to monitor
- D) All of the above

**Answer: D**
You need the RabbitMQ extension, a connection string (host, credentials), and the queue name to monitor.

---

## Question 5
Can you host RabbitMQ on Azure?

- A) No, not supported
- B) Yes, on VMs, AKS, or third-party managed services
- C) Only on Azure Service Bus
- D) Only locally

**Answer: B**
RabbitMQ can run on Azure VMs, container services (ACI, AKS), or use third-party managed RabbitMQ services.

---

## Question 6
What is an exchange in RabbitMQ?

- A) A database table
- B) A routing component that receives messages and routes them to queues based on rules
- C) A storage account
- D) A monitoring tool

**Answer: B**
Exchanges receive messages from producers and route them to queues based on routing keys and binding rules.

---

## Question 7
What are the main exchange types in RabbitMQ?

- A) Direct, Fanout, Topic, Headers
- B) Queue and Stack
- C) FIFO and LIFO
- D) Public and Private

**Answer: A**
RabbitMQ supports Direct (routing key match), Fanout (broadcast), Topic (pattern match), and Headers (attribute match) exchanges.

---

## Question 8
How does RabbitMQ differ from Azure Service Bus?

- A) No difference
- B) RabbitMQ is open-source and self-managed; Service Bus is fully managed Azure service
- C) RabbitMQ is Azure-only
- D) Service Bus doesn't support queues

**Answer: B**
RabbitMQ is open-source and requires management; Azure Service Bus is a fully managed cloud service with similar features.

---

## Question 9
What is message acknowledgment in RabbitMQ?

- A) A greeting message
- B) Confirmation from consumer that message was successfully processed
- C) Message encryption
- D) Message routing

**Answer: B**
Acknowledgment confirms successful processing. Without acknowledgment, messages are redelivered ensuring at-least-once delivery.

---

## Question 10
Can RabbitMQ messages be persisted across server restarts?

- A) No, always in-memory only
- B) Yes, if queue and messages are marked as durable/persistent
- C) Only in paid versions
- D) Automatic for all messages

**Answer: B**
Queues must be declared as durable and messages published with persistent delivery mode to survive restarts.
