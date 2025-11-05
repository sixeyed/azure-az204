# Azure Storage Accounts - Exercises Introduction

We've covered Azure Storage Accounts as a managed storage service providing highly available, secure, and scalable data storage with complete control over access and built-in redundancy options. Now let's work with storage accounts and blob storage hands-on.

## What You'll Do

You'll start by **exploring storage account options in the Portal** to understand configuration choices: globally unique naming with strict rules (3-24 characters, lowercase letters and numbers only), region selection affecting performance and pricing, performance levels (Standard with HDD or Premium with SSD), and redundancy levels (LRS for local, ZRS for zone-redundant, GRS for geo-redundant). Each option represents different trade-offs between cost, availability, and durability.

Then you'll **create a storage account with Azure CLI** using `az storage account create`, specifying the SKU which combines both performance and redundancy into a single value like Standard_ZRS or Premium_LRS. Understanding SKU naming is important: performance level underscore redundancy type.

You'll **work with blob storage** by uploading files through the Portal, learning that blob stands for Binary Large Objects - essentially file storage optimized for unstructured data. Containers organize blobs like folders, but storage is not hierarchical at the container level - no containers inside other containers, though you can simulate folder structure with forward slashes in blob names.

Next comes **understanding public versus private access** - a critical security concept. New blob containers default to private access as security-first approach. Even with the blob URL, anonymous access is denied without authentication. You'll configure blob-level access allowing public download with the URL but keeping container listings private, or container-level access making the entire container public like a web server directory.

You'll **explore storage for VM disks** by creating a premium storage account specifically for unmanaged disks, then creating a VM that uses this storage. VM disks are stored as page blobs in VHD format. While Azure uses managed disks by default today, unmanaged disks give you more control over storage configuration and let you manage VM disks alongside other data.

The lab challenge involves **configuring the storage account firewall** to allow access only from your IP address while blocking the VM's access, demonstrating defense in depth - multiple security layers rather than relying on a single control.

The key learning: Storage accounts provide flexible, secure storage with multiple redundancy options, configurable access control, and support for various workloads from files to VM disks.

Let's master Azure Storage!
