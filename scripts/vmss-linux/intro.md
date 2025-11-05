# Virtual Machine Scale Sets - Linux: Introduction

## Opening

Welcome to this lab on Virtual Machine Scale Sets with Linux. In this session, we'll explore how to use cloud-init for automated deployment and configuration of applications on Linux-based VM Scale Sets.

## Context and Motivation

When working with VM Scale Sets, you have two main approaches for getting your application running on instances. The first approach is to use a custom image that contains your application pre-installed. This means instances can start work immediately when they come online with no additional setup required. However, this approach makes upgrades more complex because you need to build a new image every time you have a new release of your application.

The second approach, which we'll focus on in this lab, is to use a base VM image and script the deployment of your application. If your app can be deployed quickly to a base VM image, this approach offers more flexibility and simpler upgrade paths.

## What is cloud-init?

cloud-init is a powerful cross-platform system for configuring new machines. It allows you to automate all the usual steps for deploying pre-requisites, installing applications, and writing configuration files. Azure has excellent support for cloud-init on Linux VMs, making it an ideal choice for VM Scale Set deployments.

## Lab Objectives

In this lab, you'll learn how to:

1. Use cloud-init scripts as custom data when creating VMs and VM Scale Sets
2. Deploy and configure applications automatically as instances start
3. Create and configure load balancer rules for a new VM Scale Set
4. Update VM Scale Set models and manage instance upgrades
5. Understand the difference between model updates and instance updates

## What You'll Build

We'll start by creating a single VM with a cloud-init script to understand how the system works. Then we'll move to a full VM Scale Set running Nginx web servers, where each instance is automatically configured using cloud-init.

You'll see how to set up load balancing, how to update the VMSS model with new configurations, and how to manage the upgrade process for existing instances.

## Prerequisites

Before we begin, make sure you have:
- An active Azure subscription
- Azure CLI installed and configured
- Basic familiarity with Linux and shell commands
- Understanding of VM Scale Sets from previous labs

Let's get started by exploring how cloud-init works with a single VM.
