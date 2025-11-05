# Docker Compose - Introduction Narration Script

## Opening

Welcome to this lesson on Docker Compose. In this session, we'll explore how Docker Compose helps you define and manage multi-container applications using a simple YAML specification.

## What is Docker Compose?

Docker Compose is two things: first, it's a specification for describing distributed applications that run in containers. Second, it's a command-line tool that takes those specifications and runs them in Docker.

The key concept here is the desired-state approach. If you've worked with Azure Resource Manager templates or Bicep, you'll recognize this pattern. Instead of imperatively telling Docker what to do step-by-step, you declare what you want your application to look like, and Compose makes it happen.

## Why Use Docker Compose?

You might be wondering - why not just use docker run commands? Well, there are several compelling reasons.

First, Compose files act as living documentation for your application. Instead of sharing a list of docker run commands with complex parameters, you have a clear YAML file that shows the entire application architecture.

Second, it simplifies multi-container applications. Modern distributed applications often have multiple components - a web front-end, an API backend, a database, maybe a cache. Managing all these with individual docker run commands becomes tedious and error-prone.

Third, it provides consistent deployment. The same Compose file works on your development machine, on a colleague's laptop, and in testing environments. Everyone gets the same application configuration.

## The Compose Specification

Docker Compose files are written in YAML format. A typical Compose file defines several key elements:

- Services: These are the containers that make up your application
- Networks: These connect your containers so they can communicate
- Volumes: These provide persistent storage for your containers
- Environment variables: These configure your application components

## CLI Tools

There are actually two versions of the Docker Compose CLI you might encounter.

The original tool is called docker-compose with a hyphen. It's a separate binary that you install alongside Docker.

The newer versions of Docker include Compose functionality built right in. You use it with docker compose - notice the space instead of the hyphen.

The commands are identical between the two versions - just swap the hyphen for a space. You can use whichever version you have available.

## When to Use Docker Compose

Docker Compose is particularly well-suited for:

- Development environments where you need to run multiple services locally
- Testing multi-container applications
- Defining application architecture that will later be deployed to orchestrators like Kubernetes or Azure Container Instances
- Small production deployments where you don't need full orchestration

Even for simple single-container applications, Compose can be valuable as executable documentation of your application configuration.

## Looking Ahead

In the exercises that follow, we'll start simple with a single Nginx container in Compose, then move on to a multi-container distributed application. We'll see how to debug connectivity issues, update running applications, and manage the entire lifecycle of a containerized application.

Docker Compose is a fundamental skill for working with containers, and it's an important topic for the AZ-204 certification exam. Let's dive in and see it in action.
