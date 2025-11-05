# Cosmos DB Table API - Introduction

Welcome to this lab on Cosmos DB Table API. In this session, we'll explore how Cosmos DB's Table API provides a modern, scalable replacement for Azure Table Storage.

## What is Cosmos DB Table API?

The Cosmos DB Table API is a straight replacement for Azure Table Storage. It's designed specifically to offer easy migration paths for older applications that were built with Table Storage. The beauty of this approach is that you can use Cosmos Table API without changing your existing applications - you can move to the modern storage option with all the scale and capabilities of Cosmos DB with minimal effort.

## Why Use Cosmos DB Table API?

If you have legacy applications using Azure Table Storage, the Table API gives you an upgrade path without rewriting code. You get all the benefits of Cosmos DB - global distribution, guaranteed low latency, multiple consistency models, and enterprise-grade SLA - while keeping your existing table storage code.

## Lab Overview

In today's lab, we'll explore the Table API hands-on. We'll run an application that writes to Table Storage, and then we'll switch it to using Cosmos DB with just a configuration change. This demonstrates the true power of the Table API - seamless migration with zero code changes.

## Key Concepts

Before we dive in, let's understand the structure. Unlike other Cosmos DB APIs that have hierarchies like Account, Database, and Container, the Table API has a simpler structure:
- Account level
- Table(s) directly under the account

There are no collections or containers in between. This matches the original Table Storage architecture, making migration even more straightforward.

## What You'll Learn

By the end of this lab, you'll know how to:
- Create a Cosmos DB account with Table API enabled
- Create tables using both the Portal and CLI
- Deploy an application that writes to Table Storage
- Switch the application to Cosmos DB with just a connection string change
- Query data using the Table API

Let's get started!
