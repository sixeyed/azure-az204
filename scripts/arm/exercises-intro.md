# ARM Templates - Exercises Introduction

We've covered the declarative approach to infrastructure deployment as an alternative to imperative Azure CLI commands. Now let's deploy infrastructure using ARM templates.

## What You'll Do

You'll start by **deploying a storage account using an ARM template** via Azure CLI. This demonstrates the declarative approach - you describe what you want (a storage account with specific properties), and Azure figures out how to create it. You'll explore the **what-if feature** to preview changes before deployment, seeing exactly what Azure will create, modify, or delete.

Then comes a key learning moment: **configuration drift detection**. You'll manually change a deployed resource through the Portal (simulating when someone makes ad-hoc changes outside your infrastructure code). Then you'll run what-if again to see how ARM templates identify the discrepancy between your template's desired state and the actual deployed state. This shows how templates help maintain infrastructure consistency.

Next, you'll **deploy a complex Linux VM template** with multiple associated resources - virtual network, storage account, public IP, network interface, and the VM itself. This demonstrates how ARM templates handle resource dependencies automatically. All related resources are defined in one file and deployed together.

You'll encounter an **idempotency issue with dynamic IP allocation**. When you deploy the template multiple times, Azure tries to allocate a new IP each time because "dynamic" means it can change. The fix involves **using static IP addresses** in your template. This teaches you about making templates truly idempotent - running them multiple times produces the same result without creating new resources.

Let's deploy infrastructure as code with ARM templates!
