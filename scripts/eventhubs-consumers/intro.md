# Event Hubs Partitioned Consumers - Introduction

Welcome to this lab on Event Hubs Partitioned Consumers. In this session, we'll explore how to process a partitioned stream of events reliably using Azure Event Hubs.

## What You'll Learn

Event Hubs is Azure's big data streaming platform and event ingestion service. But consuming events at scale requires careful handling - especially when dealing with partitioned data streams.

In this lab, we'll focus on the partitioned consumer pattern, which is essential for building reliable, scalable event processing systems.

## The Challenge

When processing streams of events, you need to solve several problems:

First, you need to track your progress. If your consumer crashes or restarts, how does it know where it left off? You don't want to miss events, but you also don't want to process the same event multiple times.

Second, you need to scale. A single consumer might not be able to keep up with a high-volume event stream. You need multiple consumers working together, but they shouldn't duplicate work or miss events.

Third, you need high availability. If one consumer fails, the others should pick up its work automatically.

## The Solution

Microsoft has built this logic into the Event Hubs client libraries. The library handles:

- Recording the processed offset using blob storage as a simple state store
- Ensuring each consumer picks up where it left off in the stream
- Supporting multiple consumers running at scale
- Automatic failover when a consumer fails

## What We'll Build

In this lab, we'll work with a device logging scenario. We'll:

- Create an Event Hub namespace with the Standard SKU
- Set up an Event Hub with multiple partitions
- Configure consumer groups for different processing needs
- Use blob storage to track consumer progress
- Run multiple consumers and observe how they share the workload
- Enable Event Hub Capture to store all events automatically

We'll also see the competing consumer pattern in action - multiple consumers reading from the same stream, with the library managing partition ownership and failover.

## Key Concepts

Before we start, let's clarify some terminology:

**Partitions**: Event Hubs splits the event stream into multiple partitions. This allows parallel processing and increases throughput. The partition count is set when you create the Event Hub and cannot be changed later.

**Consumer Groups**: These are logical views of the event stream. Different consumer groups can process the same events at different speeds. For example, you might have one group for real-time processing and another for auditing.

**Checkpoints**: Consumers periodically record their position in the event stream by storing the offset in blob storage. This allows them to resume from where they left off after a restart.

**At-Least-Once Delivery**: The Event Hubs consumer pattern guarantees that every event will be processed at least once. However, events might be processed more than once if a consumer crashes between processing and checkpointing.

Let's get started and see these concepts in action.
