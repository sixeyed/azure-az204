# Azure Storage Accounts - Introduction

## Opening

Welcome to this lab on Azure Storage Accounts. In this session, we'll explore one of the fundamental building blocks of Azure - managed storage services that provide highly available, secure, and scalable data storage.

## What are Storage Accounts?

Azure Storage Accounts are a managed storage service that allows you to store data in the cloud. You have complete control over who can access your data - you can make it publicly accessible, restrict it to specific users, or limit access to other Azure services.

One of the key benefits of Storage Accounts is built-in redundancy. Your data is automatically replicated across multiple locations to ensure high availability and durability. And you're not locked into a single configuration - you can choose different performance levels based on your specific needs and budget.

## What We'll Cover

In this lab, we'll explore the basics of Azure Storage Accounts. You'll learn how to create storage accounts, understand different redundancy options, and work with blob storage to upload both small and large files.

By the end of this session, you'll have hands-on experience with:
- Creating storage accounts using the Azure CLI
- Understanding performance and redundancy levels
- Working with blob containers
- Managing public and private access to your data
- Storing VM disks in storage accounts

## Redundancy Options

Before we dive into the exercises, let's talk about data redundancy. Azure offers several levels of replication:

**Locally Redundant Storage** - or LRS - replicates your data within a single datacenter. This is the most cost-effective option and protects against hardware failures.

**Zone Redundant Storage** - or ZRS - replicates your data across multiple datacenters within a single region. This provides better availability than LRS.

**Geo-Redundant Storage** - or GRS - replicates your data across different regions entirely. This gives you the highest level of protection, but comes at a higher cost.

The key takeaway? Your data becomes more secure with wider replication, but you'll pay more for that additional protection.

## Getting Started

Let's get started with our hands-on exercises. We'll begin by exploring the options available when creating a Storage Account, then move on to creating one ourselves using the Azure CLI.
