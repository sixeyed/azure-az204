# Docker Compose - Exercises Introduction

We've covered Docker Compose as both a YAML specification for describing multi-container applications and a tool for managing them with desired-state approach. Now let's orchestrate multiple containers together.

## What You'll Do

You'll start with **a broken multi-container app** - a random number generator with web frontend and API backend. When you run it, the frontend can't connect to the API. Why? This is a common container networking issue that teaches you how to debug connectivity problems.

You'll use **docker logs** to see application output and **nslookup** to test DNS resolution between containers. You'll discover that containers on the same Compose network can reach each other using service names as hostnames. Once you fix the configuration with the right DNS name, everything works!

Then you'll practice **desired-state updates**. Change the Compose file (add environment variables, adjust port mappings), run `docker-compose up` again, and watch as Compose intelligently determines which containers need recreation and which can stay running. This is infrastructure as code in action - declare what you want, Compose figures out how to get there.

You'll explore **service discovery through DNS names** - how containers automatically get hostnames matching their service names in Compose. You'll see **aggregated logs** from all containers with `docker-compose logs`, making it easy to debug distributed applications.

The **challenge** involves **adding containers to multiple networks** using an nginx reverse proxy. You'll create a network topology where the proxy sits between clients and backend services, demonstrating how Compose handles complex networking scenarios.

The key learning: patterns you learn with Docker Compose apply directly to Azure Container Instances (multi-container groups) and AKS deployments.

Let's orchestrate multi-container applications!
