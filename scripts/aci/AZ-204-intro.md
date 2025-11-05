# Azure Container Instances - AZ-204 Exam Introduction

Great work completing the hands-on exercises. Now let's shift focus to what you need to know about Azure Container Instances for the AZ-204 certification exam.

## Exam Coverage

ACI appears under the "Implement containerized solutions" domain and represents 5-10% of the exam content. While that might not sound like much, the questions are very specific and test your understanding of when to use ACI versus other services like App Service or AKS.

## What We'll Cover

First up is a critical exam topic: **knowing when to use ACI versus other compute options**. The exam loves scenario-based questions where you need to choose the right service. We'll cover the specific keywords to look for that point to ACI - words like "simple," "temporary," "task," or "single container" - versus scenarios that call for Kubernetes or App Service.

Next, we'll dive deep into **Azure CLI commands for creating and deploying containers**. The exam heavily tests CLI syntax, so you need to know commands like `az container create` with all its parameters - resource groups, images, ports, DNS names, CPU and memory allocation, OS types, and environment variables. We'll also cover the difference between regular environment variables and secure ones for sensitive data.

**Container networking** is another frequently tested topic. You'll learn about public versus private IP addresses, DNS name configuration, port exposure, and VNet integration. There's a common exam trick question about private ACI containers requiring dedicated subnets - we'll make sure you know that.

We'll explore **container groups** - how to deploy multiple containers together sharing lifecycle and network resources. This often appears in questions about sidecar patterns where you have a main application container alongside a logging or monitoring container.

**Restart policies** are tested on almost every exam - knowing when to use Always, OnFailure, or Never based on whether you're running a web service, a task that might fail, or a one-time batch job.

Storage is another key topic. The exam tests whether you know that **ACI only supports Azure Files for persistent volumes, not Azure Disk** - that's a classic exam gotcha. We'll cover how to mount Azure Files shares to your containers.

Finally, we'll look at **integration with Azure Container Registry** - pulling private images securely using credentials or managed identities, which is the more exam-friendly approach.

We'll wrap up with common exam scenarios and quick reference commands to help you memorize the syntax you'll need on test day.

Ready to master ACI for the AZ-204? Let's dive into the exam-focused content!
