# Distributed Apps on Azure Container Instances - Introduction

Welcome to this lab on Distributed Apps on Azure Container Instances.

## Overview

Azure Container Instances, or ACI, is the simplest container platform available on Azure. It allows you to run containers without having to manage virtual machines or adopt a higher-level orchestration service. While you can run single containers, ACI also supports running multiple containers in a group to host distributed applications.

## What You'll Learn

In this lab, we'll explore two different approaches to modeling and deploying distributed applications on ACI:

First, we'll use Azure's native YAML specification with the Azure CLI. This gives you access to all ACI-specific features and configuration options.

Second, we'll use the standard Docker Compose specification with the Docker CLI. This is particularly useful when you want to use familiar Docker tooling and don't need ACI-specific configurations.

## Integration with Azure Services

ACI doesn't exist in isolation - it integrates seamlessly with other Azure services. We'll demonstrate this integration by connecting our containerized applications to Azure Storage services, including Blob Storage and Azure Files.

You'll see how containers running in ACI can:
- Use Azure Blob Storage as a persistent data store
- Mount Azure Files shares as part of the container filesystem
- Access Azure services using connection strings and authentication

## Key Concepts

Throughout this lab, we'll cover several important concepts:

**Container Groups**: ACI organizes multiple containers into groups that share the same network space, making it easy to build distributed applications where containers communicate over localhost.

**Resource Specification**: Unlike Docker Desktop, ACI requires you to specify CPU and memory requirements upfront so Azure can provision the appropriate compute resources.

**Deployment Models**: You'll see the differences and similarities between ACI's YAML format and the Docker Compose format, and understand when to use each approach.

**Container Updates**: We'll explore how ACI handles configuration changes and what happens under the hood when you update a running container.

Let's get started and see how easy it is to run distributed applications on Azure Container Instances.
