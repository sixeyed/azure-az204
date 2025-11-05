# Azure Durable Functions: Human Interaction Pattern - Introduction

## Script Duration: 2-3 minutes

---

### Slide 1: Title - Human Interaction Pattern

Welcome to this session on Azure Durable Functions and the Human Interaction pattern. This is one of the most practical patterns you'll encounter when building real-world serverless applications.

---

### Slide 2: The Challenge - Workflows That Wait

Think about common business scenarios. A purchase order that needs manager approval. A password reset that requires verification. A support ticket that needs human review. These workflows all share something in common - they need to pause and wait for a person to take action.

Traditional approaches have problems. You could store sensitive data in a database while waiting, but that creates security risks. You could keep a service running continuously, but that's expensive and inefficient. This is where the Human Interaction pattern in Durable Functions really shines.

---

### Slide 3: How Durable Functions Solve This

Durable Functions give us an elegant solution. They can pause for extended periods - minutes, hours, even days - waiting for human input. And here's the key advantage: during that wait time, nothing is running. No compute resources being consumed. No sensitive data sitting in external storage. The function simply suspends, and resumes exactly where it left off when the human responds.

This makes it perfect for scenarios like two-factor authentication, approval workflows, or any process that requires human verification before continuing.

---

### Slide 4: Key Components - External Events and Timers

The Human Interaction pattern relies on two core concepts you need to understand. First, external events - these let you send information into a running orchestration. When a user enters their verification code, that's sent as an external event to wake up the waiting function.

Second, durable timers - because humans don't always respond promptly. You'll typically set a timeout, giving the user a window to respond. If they don't reply within that timeframe, the orchestration can handle it gracefully, perhaps by failing the authentication or escalating to another approval route.

---

### Slide 5: Real-World Example - Two-Factor Authentication

In today's lab, we're building a two-factor authentication system. Here's how it works: your function receives a phone number, sends an SMS with a verification code, then waits. The user has a limited time to respond with the correct code. If they respond correctly and within the time limit, they're authenticated. If not, authentication fails.

We'll use the Twilio service to send SMS messages, demonstrating how durable functions integrate with external services while managing the overall workflow logic.

---

### Slide 6: Why This Matters for AZ-204

For the AZ-204 exam, understanding the Human Interaction pattern is crucial. You need to know when to use external events versus other trigger types. You should understand how durable timers work and how to implement timeout logic. And importantly, you need to recognize scenarios where this pattern is the right architectural choice.

This pattern appears in exam questions about workflow orchestration, state management, and serverless design patterns. It's not just theoretical - it's a practical solution you'll use in production Azure applications.

---

### Slide 7: What You'll Learn Today

In this lab session, you'll set up a Twilio account for sending SMS messages. You'll build a durable function orchestration that sends verification codes and waits for user responses. You'll test it locally with the Azure Storage emulator, then deploy it to Azure. And you'll work with the HTTP endpoints that let you send events and check orchestration status.

By the end, you'll have hands-on experience with one of the most powerful patterns in the Azure Functions toolkit.

Let's get started!
