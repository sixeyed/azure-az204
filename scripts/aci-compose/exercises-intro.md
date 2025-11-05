# Distributed Apps on Azure Container Instances - Exercises Introduction

Now that you understand the basics of ACI, let's explore something more advanced - running distributed applications with multiple containers working together.

## What's Ahead

In these exercises, you'll deploy multi-container applications to Azure Container Instances using two different approaches.

First, you'll use **Azure's native YAML specification**. You'll deploy a random number application consisting of two containers - an API and a web frontend - that communicate with each other in the same container group. You'll see how containers in a group share network space and can talk to each other using localhost. Then you'll learn an important lesson about container lifecycle: when you need to update configuration like environment variables, ACI recreates the containers rather than modifying them in place. You'll watch this happen by increasing the logging level and observing the old containers being killed and new ones starting.

Next comes **Docker Compose integration with ACI**. If you're already familiar with Docker Compose, this is going to feel really natural. You'll authenticate the Docker CLI to Azure, create an ACI context, and then use standard `docker compose up` commands to deploy to Azure. It's the exact same workflow you use locally, but running in the cloud. You'll also discover that Docker ACI integration adds some automatic sidecars to help with networking.

Finally, you'll explore **ACI's integration with Azure Storage**. You'll see two different approaches: using Blob Storage as a data store through connection strings, and mounting Azure Files shares as volumes in the container filesystem. You'll deploy a container that writes data to what looks like local storage, but it's actually writing to Azure Files that persists beyond the container lifecycle.

The challenge exercise has you exploring whether multiple instances can share the same file share and how you might load-balance traffic between them - important questions when thinking about ACI's limitations for production workloads.

Let's see how to build distributed container applications on ACI!
