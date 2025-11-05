# Distributed Apps on Azure Container Instances - AZ-204 Exam Introduction

Excellent work with the hands-on exercises. Now let's focus on what the AZ-204 exam expects you to know about multi-container deployments on ACI.

## What We'll Cover

The exam tests your understanding of **container groups** - how multiple containers scheduled on the same host share lifecycle, network, and storage resources. You need to know that containers in a group can communicate using localhost because they share the same network namespace. This is different from deploying separate container instances.

We'll dive into the **ACI YAML specification**, which is Azure's proprietary format for defining container groups. The exam loves to test whether you know which fields are required versus optional. For example, CPU and memory specifications are mandatory in ACI YAML, unlike Docker Compose where they default. You'll learn the proper structure for defining ports at both the container level and the IP address level - a common exam gotcha.

**Docker Compose integration** is another testable topic. You need to know the command sequence: `docker login azure`, then `docker context create aci`, then `docker context use`, and finally standard `docker compose` commands. The exam may ask about troubleshooting scenarios like "why can't I see my Azure containers?" which often relates to which Docker context is active. You'll also learn that the Docker ACI integration automatically creates sidecar containers for networking.

A critical exam concept is **container updates and lifecycle**. You cannot update configuration of running containers - any change to environment variables, resource limits, port mappings, or volumes requires recreating the container. ACI kills the old containers and starts new ones, which causes temporary downtime. Expect scenario questions about what happens when you redeploy with changed configuration.

**Storage integration** appears frequently on the exam. You need to understand the difference between Azure Blob Storage (accessed via connection strings and SDKs) and Azure Files (mounted as volumes in the filesystem). The exam tests whether you know that Blob Storage requires application code changes while Azure Files mounting is transparent to the application.

For security, you'll learn about **connection strings, Storage Account keys, and secure credential management**. The exam wants you to know that hardcoding credentials in YAML is not secure, and that Azure Key Vault or managed identities are the recommended approaches for production.

We'll cover **networking in container groups** - how containers share a single public IP, how to map ports for external access, and how inter-container communication uses localhost. And you'll learn about **Docker context management** for switching between local Docker and ACI.

Finally, we'll work through common exam scenarios like multi-container communication, persistent data, configuration updates, and secure credentials, along with the CLI commands you need to memorize.

Ready to master multi-container ACI deployments for the exam? Let's go!
