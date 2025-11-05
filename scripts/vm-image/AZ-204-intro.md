# Building Custom VM Images - AZ-204 Exam Introduction

Excellent work with custom images! This topic supports AZ-204 exam objectives around Infrastructure as a Service solutions.

## What We'll Cover

**Image types and sources** must be understood. Marketplace Images are pre-built from Microsoft and partners with URNs like "MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest". Custom Images are created from generalized VMs as demonstrated in this lab. Managed Images are the modern approach stored as Azure resources. Shared Image Galleries provide enterprise-grade management with versioning, replication, and RBAC. The exam tests understanding of image types and when to use each.

**Generalization process** is frequently tested. For Windows: use Sysprep to generalize, then deallocate and mark as generalized in Azure. For Linux: use Azure Linux Agent (waagent) with deprovision command. Purpose: removes machine-specific information like computer name, user accounts, and security identifiers enabling multiple unique VMs from one image. The exam tests understanding of the complete generalization workflow.

**Image vs Snapshot** differences are critical. Snapshots are point-in-time copies of disks that are read-only and used to restore data or create new disks. Images are references to generalized VMs used to create new VMs including OS configuration. The exam tests knowing when to use images (creating VMs) vs snapshots (backup and recovery).

**CLI commands** appear in exam questions. Know `az vm create` for creating VMs, `az vm deallocate` for shutting down and deallocating, `az vm generalize` for marking VM as generalized, `az image create` for creating images from VMs, `az image list` for listing available images, and `az image copy` for copying to another location/resource group. Understand parameters: `-g` for resource group, `-n` for name, `-l` for location, `--image` for image reference, `--source` for source VM. The exam tests CLI command knowledge.

**Architecture patterns** guide service selection. Use Custom Images when you need consistent VM deployments, want to reduce deployment time, have complex installation requirements, or need to meet compliance with pre-configured baselines. Don't use when you need dynamic configuration per environment, application changes frequently, you can use containers (lighter weight, more portable), or you only need few VMs (overhead not worth it). The exam tests choosing appropriate approaches.

**Integration with other services** demonstrates broader understanding. Virtual Machine Scale Sets deploy auto-scaling fleets from custom images. Azure DevOps automates image creation in CI/CD pipelines using Packer. Azure Resource Manager references custom images in ARM templates for infrastructure as code. Shared Image Gallery replicates images across regions for global deployments. The exam tests integration scenarios.

**Best practices** for the exam include: Security (always generalize VMs before imaging to avoid leaking credentials), Lifecycle Management (store images in separate resource groups from application resources), Versioning (use image versions to track changes and enable rollback), Replication (use Shared Image Galleries for multi-region), and Automation (use Packer to automate image creation in DevOps pipelines). The exam tests best practice knowledge.

We'll cover **common exam scenarios** (deploying 100 identical web servers across regions, troubleshooting image creation errors after Sysprep, sharing images across subscriptions), **comparison with containers** (VMs for legacy applications vs containers for cloud-native), and **hands-on skills** (creating custom images, deploying VMs from images, troubleshooting failures).

Master custom VM images for the AZ-204!
