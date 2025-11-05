# Docker 101 - Introduction Narration Script

## Opening Hook

Welcome to Docker 101. In this lab, we're going to explore one of the most important technologies for deploying applications in the cloud: Docker containers.

## The Problem Statement

So let's start with a question: How would you run a .NET application on Azure?

Well, you could provision a virtual machine, connect to it, install .NET, download your application binaries, set up all the configuration, and then start the app. But this approach has some significant challenges.

First, it's hard to automate all those steps. Second, it's time-consuming to spin up a new instance. And third, it's difficult to keep multiple instances in sync. You're managing not just your application, but the entire infrastructure around it.

Now, you could use Azure App Service instead, which simplifies things. But there's still a lot to set up, and you end up with a different hosting environment than what you have running locally on your development machine. This can lead to the classic "it works on my machine" problem.

## Enter Docker

This is where Docker comes in.

With Docker, you build all your application components and dependencies into a package called an **image**. Then you use that image to run instances of your applications called **containers**.

Think of a Docker image as a blueprint - it's a static package that contains everything your application needs to run: your code, the runtime, system tools, libraries, and settings. Once you've built an image, you can run it anywhere that has Docker installed, and it will behave exactly the same way.

A container is a running instance of that image. It's lightweight, portable, and isolated from other containers and the host system.

## Key Benefits

The beauty of Docker is consistency. Whether you're running on your laptop, in a test environment, or in production on Azure, the container starts from exactly the same image. This eliminates environment-specific bugs and makes deployments much more reliable.

Docker also makes scaling easier. Need to handle more traffic? Just run more containers from the same image. No need to provision and configure new VMs from scratch.

## What We'll Cover

In this lab, we're going to start by running containers locally using Docker Desktop. We'll explore how to:

- Run pre-built container images from public registries
- Work with different types of .NET container images
- Build your own custom Docker images
- Package and run your own .NET applications in containers

Later, you'll see how these same containers can be deployed to Azure services like Azure Container Instances, Azure Container Apps, and Azure Kubernetes Service.

## Getting Started

Before we dive into the exercises, make sure you have Docker Desktop installed and running. You'll see the Docker whale icon in your taskbar. If you're on Windows and have used Docker Desktop before, make sure you're in Linux container mode, as that's what we'll be using for these exercises.

The main tool we'll be using is the `docker` command-line interface, which works similarly to the Azure CLI. It has built-in help, supports various subcommands, and gives you complete control over your container environment.

Alright, let's get started with our first container.
