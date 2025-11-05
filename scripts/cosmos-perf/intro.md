# Cosmos DB Performance Provisioning - Introduction

## Opening

Welcome to this lab on Cosmos DB Performance Provisioning. In this session, we'll explore one of the most important aspects of using Azure Cosmos DB effectively - understanding and managing Request Units to control both performance and cost.

## What is Cosmos DB Pricing?

Cosmos DB charges you for two main things: storage and compute.

Storage is straightforward - it's a flat rate based on the amount of data you store, and this rate is the same regardless of your performance level.

Compute, however, is where things get interesting. Cosmos DB measures compute in terms of Request Units, or RUs. You pay for all access operations - reads, writes, deletes, updates, and queries.

## Provisioning Models

You have two main options for how you pay for these Request Units:

First, there's the serverless model. With serverless, you pay only for the RUs you actually consume. This is great for development, testing, or applications with unpredictable workloads.

Second, there's the provisioned model. Here, you pay for a fixed level of RUs per second, whether you use them all or not. This can be more cost-effective for consistent, high-volume workloads.

## Why This Matters

Cost is often cited as a concern when considering Cosmos DB. But here's the truth - if you plan appropriately and understand how RUs work, Cosmos DB can actually be very cost-effective. The key is knowing how to test and measure your RU consumption.

## What You'll Learn

In this lab, you'll learn how to:

- Create a Cosmos DB account and database with fixed performance levels
- Understand how Request Units are calculated
- Measure RU consumption for different types of queries
- See how data modeling choices dramatically affect RU usage
- Use techniques like point reads to minimize costs
- Apply index policies to optimize performance and cost

## The Lab Scenario

We'll be working with a shop database containing product information. You'll create containers with different configurations, load data in different formats, and run queries to see exactly how many Request Units each operation consumes.

By the end of this lab, you'll have practical experience measuring RU consumption and making informed decisions about how to structure your Cosmos DB solutions for optimal cost and performance.

Let's get started.
