# Virtual Machines - Web Server - AZ-204 Exam Introduction

Great work with web server deployment! This content supports multiple AZ-204 exam objectives around compute, networking, and security.

## What We'll Cover

**Resource lifecycle management** is tested on the exam. VMs have dependencies on multiple resources including NICs, PIPs, NSGs, and disks. Resources can be managed independently or as a group. Deleting a VM doesn't automatically delete all associated resources unless configured. PIPs can exist independently and be reassigned. This knowledge is crucial for exam questions about resource management and cost optimization - understanding which resources persist and continue costing money.

**Networking in Azure** is a major exam topic. Public IP Addresses: understand difference between dynamic (released when VM is deallocated) and static allocation (retained regardless of VM state). DNS Names: Azure provides FQDN support for PIPs in format "name.region.cloudapp.azure.com" remaining constant even when IP changes. Network Security Groups act as virtual firewalls with rule-based access control. Inbound rules control what traffic can reach resources with priority-based evaluation (lower numbers processed first). The exam tests networking configuration and troubleshooting.

**Infrastructure as Code** concepts apply beyond this interactive lab. The exam expects understanding of how to script VM deployments using Azure CLI, the parameters needed for programmatic VM creation, and how to query and manage resources using CLI commands. These same concepts apply to ARM templates, Bicep, and SDKs - all tested on the exam.

**Exam question patterns** include scenario-based questions like: "You deploy a VM but cannot access the web application" (Answer involves checking NSG rules); "You need to ensure a VM's public IP doesn't change" (Answer involves setting PIP to static allocation); "You want to stop paying for a VM but retain its configuration" (Answer: Deallocate the VM, not just stop it). Resource management questions test understanding of correct operation order, which resources are automatic vs manual, and how to associate or disassociate resources.

**Comparison with other compute options** helps choose the right service. When to use VMs: need full OS control, running legacy applications, specific OS or software requirements, lift-and-shift scenarios. When NOT to use VMs: simple HTTP-triggered workloads (use Azure Functions), containerized applications (use Container Instances or AKS), don't need OS-level access (use App Service). The exam tests ability to choose appropriate compute services.

**Practical exam tips**: Know the CLI commands (exam includes CLI questions - practice commands for creating, managing, and querying VMs). Understand defaults (know what resources are created by default and what's optional). Security first (always consider NSG rules and access control). Cost optimization (understand billing implications of running, stopped, and deallocated VMs). Networking (be comfortable with public vs private IPs, static vs dynamic allocation, and DNS). The exam tests these fundamentals across scenarios.

We'll cover **hands-on practice value** (performance-based questions where you create/modify VM configurations, troubleshoot networking, write CLI commands), **related topics** (VM Scale Sets for automatic scaling, Availability Sets and Zones, ARM templates, managed disks, VM extensions, Azure Monitor integration), and **key takeaways** about VMs representing foundational IaaS with concepts applying across all Azure services.

Master VM web server deployment for the AZ-204!
