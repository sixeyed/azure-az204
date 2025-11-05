# Resource Groups - Exercises Introduction

We've covered Resource Groups as fundamental containers for organizing Azure resources with management, permission, and cleanup benefits. Now let's work with Resource Groups hands-on.

## What You'll Do

You'll start by **creating Resource Groups via Azure Portal** to see the visual interface. You'll select a region (where metadata is stored, not where resources must be deployed) and add tags (key-value pairs like environment=dev, project=webapp) for organization at scale.

Then you'll **create Resource Groups via Azure CLI** using `az group create` with name, location, and tags parameters. This is the automation approach - essential for infrastructure as code and repeatable deployments. You'll see how CLI enables scripting that Portal doesn't.

Before creating resources, you'll **list available Azure regions** with `az account list-locations`. Not all regions support all services, and choosing the right region affects latency, compliance, and cost. Understanding available regions is important for deployment planning.

You'll practice **managing Resource Groups by listing them** with `az group list`. Then you'll use **JMESPath queries** to filter results - showing only groups in specific regions or with specific tags. This demonstrates how to find resources programmatically in large environments.

An important lesson: **deletion requires explicit Resource Group names** - there's no bulk delete command for safety. You must specify exactly which group to delete. But when you do delete a group, **all contained resources are deleted** automatically. This cascading deletion is both powerful (easy cleanup) and dangerous (no undo).

You'll see **confirmation prompts** that require you to type "y" before deletion proceeds. This safeguard prevents accidental deletion of entire environments.

Let's master Resource Group management!
