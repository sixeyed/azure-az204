# Virtual Machine Scale Sets - Windows - Introduction

## Opening

Welcome to this lab on Virtual Machine Scale Sets for Windows. In this session, we'll explore how to deploy and manage multiple VM instances using Azure's VMSS feature.

## What Are Virtual Machine Scale Sets?

When you need to run multiple instances of your application, you could create individual VMs - each with their own IP addresses and public IPs. But this approach becomes difficult to manage at scale.

Virtual Machine Scale Sets solve this problem by allowing you to manage multiple VM instances as a single resource. Instead of dealing with dozens of individual VMs, you can control them all through one VMSS resource.

## Lab Overview

In this lab, we'll be working with a Windows application that's already been captured as a custom VM image. We'll use this image to create a VMSS and explore the key features.

Here's what we'll cover:

First, we'll create a VMSS from a custom Windows VM image, deploying multiple instances automatically.

Second, we'll configure load balancing to distribute traffic across our VM instances, including health probes and routing rules.

Third, we'll explore scaling - both manual scaling where we control the instance count, and autoscaling where Azure adjusts capacity based on CPU metrics.

Finally, we'll test the health probe system to see how the load balancer handles unhealthy instances.

## Prerequisites

Before we begin, you should have completed the VM images lab. We'll be using a custom image called "app01-image" that contains a Windows application with IIS configured.

You should also have a resource group called "labs-vmss-win" with that image already in place.

## Portal Exploration

Let's start by looking at VMSS in the Azure Portal. When you search for Virtual Machine Scale Sets and begin creating one, you'll notice several important configuration options.

There are the usual VM settings - you select your image, choose a VM size, and configure disks.

You'll also see the orchestration mode setting. The most common option is "uniform" mode, where all instances are identical.

In the Scaling section, you can set the initial instance count. If you change the scaling policy to autoscaling, you'll see options for scale-out and scale-in thresholds.

## What's Next

Now that we understand what VMSS provides, let's move on to actually creating one from our custom image and getting our application running across multiple instances.
