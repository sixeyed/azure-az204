# Azure Files Storage - Exercises Introduction

We've covered Azure Files as a fully managed file share service in the cloud using the industry-standard SMB protocol, providing network file shares accessible from Windows, Linux, and macOS - similar to corporate file shares but with cloud benefits. Now let's work with file shares hands-on.

## What You'll Do

You'll start by **creating a file share** within a storage account using `az storage share create`. Azure Files is a feature of Storage Accounts just like blob storage - both services share the same infrastructure. You'll create a share called "labs" with default settings for tier and quota that can be modified later.

Then you'll **work with files in the Portal** by adding directory structure and uploading files. This demonstrates a key difference from blob storage: file shares support true hierarchical directories, not just virtual ones simulated with forward slashes. You'll try accessing files via HTTP and discover file shares default to no public access and don't have easy options to make files publicly accessible - they're designed to work like network file shares using SMB/CIFS, not web storage.

You'll **mount the share locally** on your machine using platform-specific commands. For macOS: `open smb://` with credentials. For Linux: `mount -t cifs` with username and password. For Windows: `net use` to map a network drive. Once mounted, the share appears as a regular drive or directory. You'll edit files locally and see changes immediately reflected in the Portal, demonstrating real-time synchronization across clients.

Next comes **understanding key rotation** for security. Authentication uses storage account keys by default. You'll see how storage accounts have two keys (key1 and key2) - both provide full access and exist to support zero-downtime key rotation. You'll rotate key1 with `az storage account keys renew` and observe how existing mounts lose authentication. The clever rotation process: have clients use key1, rotate key2 (doesn't affect connections), update some clients to key2, rotate key1, update remaining clients.

You'll **mount the share in a Virtual Machine** using cloud-init automation. The mount-share.sh script installs cifs-utils, creates a mount point, and mounts the file share during VM provisioning. Once the VM starts, the share is automatically available without manual intervention. You can edit files from the VM and see changes everywhere instantly.

The lab challenge involves **increasing the share quota** to allow more data when the share is full, and **creating a premium file share** using FileStorage account kind (not general-purpose) which provides guaranteed IOPS and throughput for performance-sensitive workloads.

The key learning: Azure Files provides enterprise-grade shared storage working like traditional file servers but with cloud scale and reliability, accessible across platforms and environments with real-time synchronization.

Let's master Azure Files!
