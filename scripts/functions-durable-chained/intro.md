# Azure Durable Functions - Chained Pattern Introduction

## Welcome

Welcome to the Azure Durable Functions lab, where we'll explore the chained pattern. In this session, you'll learn how to orchestrate multiple functions into a sequential workflow using Azure's powerful durable functions framework.

## The Challenge with Regular Functions

Let's start by understanding the problem we're solving. Imagine you need to build a workflow with multiple steps that must run in a specific order. Perhaps you're processing an order: validate payment, update inventory, send confirmation email, and log the transaction.

With regular Azure Functions, you could chain these together by having each function trigger the next. Function one writes to a blob, which triggers function two. Function two writes to a queue, which triggers function three. This works, but it has some serious limitations.

First, you can't guarantee the exact running order when dealing with distributed triggers. Second, passing data between functions becomes complicated - you need intermediate storage. Third, there's no single place to see the overall workflow status. And finally, error handling and retry logic gets messy when spread across multiple independent functions.

## Enter Durable Functions

This is where Azure Durable Functions come in. Durable Functions let you write stateful workflows in a serverless environment. The key word here is stateful - the framework automatically manages state between function calls, so you don't have to worry about it.

With the chained pattern, you write an orchestrator function that calls multiple activity functions in sequence. The orchestrator controls the workflow, manages data flow, and handles the execution order. Each activity is just a simple function that does one thing well.

## The Chained Pattern Explained

The chained pattern is one of the most common durable function patterns. Think of it as a pipeline where the output of one step becomes the input to the next step.

Here's how it works: A trigger starts the orchestrator. The orchestrator then calls Activity A and waits for its result. When Activity A completes, the orchestrator takes that output and passes it to Activity B. When Activity B finishes, its output goes to Activity C. Each step runs only after the previous one completes successfully.

The beauty is that this entire workflow is defined in code, in one place. You can see the logic, understand the flow, and manage it as a single unit.

## Key Concepts

Let's break down the components:

**The Orchestrator Function**: This is the conductor of your workflow. It defines what activities run and in what order. The orchestrator function uses special APIs to call activities and manage their execution. Importantly, the orchestrator code must be deterministic - it needs to produce the same result when replayed.

**Activity Functions**: These are the workers that do the actual tasks. Each activity is a standard function that performs one specific operation. Activities can read from databases, call external APIs, process data - anything a regular function can do. They use the ActivityTrigger binding, which means they can only be called by an orchestrator.

**The Durable Client**: This is what starts the orchestration. Any function with a DurableClient binding can start an orchestrator instance. In our lab, we use a timer trigger that periodically starts the orchestration workflow.

**State Management**: The durable functions framework automatically saves the orchestrator's progress. If something fails or Azure needs to move your function, the framework restores the state and continues from where it left off. You get this reliability without writing any state management code.

## Real-World Use Cases

The chained pattern is perfect for many scenarios:

**Data processing pipelines**: Extract data from a source, transform it, validate it, and load it into a destination. Each step depends on the previous one completing successfully.

**Order processing**: Validate payment, reserve inventory, create shipping labels, send notifications - these must happen in sequence.

**System initialization**: Start a service, wait for it to be healthy, configure it, run tests, promote to production. The chain ensures each step completes before moving forward.

**Batch operations**: Process a set of items where each item goes through multiple transformation stages in order.

## How This Fits AZ-204 Exam Preparation

For the AZ-204 exam, you need to understand several key aspects of durable functions:

You should know the different durable function patterns - chained, fan-out/fan-in, async HTTP APIs, monitoring, and human interaction. Understand when to use each pattern.

You need to understand orchestrator constraints - why orchestrator code must be deterministic, why you can't use random numbers or current time directly, and why you can't make direct HTTP calls from the orchestrator.

Know the bindings - DurableClient for starting orchestrations, OrchestrationTrigger for the orchestrator function, and ActivityTrigger for activity functions.

Understand how durable functions maintain state and provide reliability without you managing storage directly.

And finally, know how to configure and deploy durable functions, including the required storage account and function app settings.

## What You'll Build Today

In this lab, you'll build a health monitoring system using the chained pattern. The workflow starts with a timer trigger that runs periodically. The orchestrator then coordinates three activities:

First, it calls WriteBlob to save a heartbeat timestamp to Azure Blob Storage. The blob name contains the timestamp, giving us a historical record.

Next, it calls NotifySubscribers to publish a message to an Azure Service Bus queue, alerting other systems that a heartbeat occurred.

Finally, it calls WriteLog to record the event in Azure Table Storage for long-term auditing and analysis.

Each activity receives the output from the previous activity, and the orchestrator manages the entire flow. You'll see how simple it is to coordinate multiple Azure services in a reliable, sequential workflow.

## Development Approach

You'll start by testing locally using the Azure Storage Emulator for blob and table storage, combined with a real Azure Service Bus for queue messaging. This gives you a fast development cycle without deploying to Azure.

Once everything works locally, you'll deploy the durable function to Azure and see it running in a production environment. You'll explore the Functions portal to see how orchestrators and activities are displayed, and learn how to monitor and debug running workflows.

## Let's Get Started

By the end of this lab, you'll have hands-on experience building a real durable function with the chained pattern. You'll understand how to structure orchestrators and activities, how to pass data between steps, and how to test and deploy these powerful serverless workflows.

Let's dive in and build something great!
