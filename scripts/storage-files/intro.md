# Azure Files Storage - Introduction

## Opening

Welcome to this lab on Azure Files Storage. In this session, we'll explore one of Azure's managed file sharing solutions that allows you to create cloud-based file shares accessible via the industry-standard SMB protocol.

## What is Azure Files?

Azure Files is a fully managed file share service in the cloud. It provides shared storage that can be mounted into your filesystem, making it easy to share files between multiple applications, virtual machines, or on-premises systems.

Think of Azure Files as a network file share, similar to what you might use in a corporate environment, but hosted in Azure with all the benefits of cloud infrastructure including scalability, redundancy, and global availability.

## Key Features

Let's look at the main features of Azure Files:

First, it uses the standard SMB protocol - Server Message Block - which is the same protocol used by Windows file shares. This means your applications can access Azure Files without any special code changes.

Second, Azure Files is highly available and durable. Your data is replicated within Azure to protect against hardware failures.

Third, it's fully managed. You don't need to worry about maintaining file servers, applying patches, or managing hardware.

And fourth, it integrates seamlessly with both cloud and on-premises environments. You can mount Azure file shares from Windows, Linux, and macOS machines.

## Common Use Cases

Azure Files is ideal for several scenarios:

Lift and shift migrations - when you're moving legacy applications that expect file shares to the cloud.

Shared storage for applications - when multiple VMs or containers need access to the same files.

Storing configuration files - that need to be accessible across multiple instances.

And for development and debugging - when you need shared access to logs, metrics, or diagnostic data.

## How it Works

Azure Files is a feature of Azure Storage Accounts. When you create a storage account, you can create one or more file shares within it. Each share has a quota that defines its maximum capacity.

To access a file share, clients use the storage account name and key for authentication. You can mount the share using standard operating system commands, and once mounted, it appears as a regular drive or directory on your system.

## Lab Overview

In today's lab, we'll walk through the complete Azure Files experience. We'll start by creating a storage account and file share. Then we'll upload files and explore different ways to access them.

We'll mount the share on our local machine and see how changes sync in real-time. We'll also look at security considerations, including how to rotate storage account keys.

Finally, we'll mount the same share in an Azure Virtual Machine using cloud-init, demonstrating how you can automate file share mounting during VM provisioning.

By the end of this lab, you'll understand how to create, configure, and use Azure Files for your applications.

Let's get started.
