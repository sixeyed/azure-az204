# Static Websites with Azure Storage Blobs - Introduction

## Opening

Welcome to this lab on hosting static websites with Azure Storage Blobs. In this session, we'll explore how Azure Storage can serve as a powerful platform for hosting static web content without the need to manage traditional web servers.

## What are Static Websites on Azure Storage?

Azure Storage Blobs provide a cost-effective and scalable solution for hosting static web content. You can upload HTML files, JavaScript, CSS, images, and other static assets as blobs, and configure the blob container for public web access. This gives you a fast, globally accessible website without the overhead of managing web servers, patching operating systems, or dealing with server infrastructure.

## Key Benefits

The main advantages of using Azure Storage for static websites include:

- **Serverless Architecture** - No web server to manage, update, or scale
- **Cost Effective** - Pay only for the storage you use
- **High Availability** - Built-in redundancy options keep your site accessible
- **Scalability** - Handle traffic spikes automatically
- **Global Reach** - Combine with CDN for worldwide content delivery

## What We'll Cover

In this lab, you'll learn how to:

1. **Deploy a static website** to Azure Storage by configuring a storage account with static website hosting
2. **Upload web content** to the special dollar-web container
3. **Configure geo-replication** using read-access geo-redundant storage for high availability
4. **Set up Azure CDN** to distribute content globally and improve performance for users worldwide
5. **Manage content updates** and understand how caching works with CDN

## Use Cases

Static website hosting on Azure Storage is ideal for:

- Marketing and promotional sites
- Documentation portals
- Single Page Applications (SPAs)
- Personal blogs and portfolios
- Event landing pages
- Any content that doesn't require server-side processing

## What You'll Need

To complete this lab, you'll need:

- An active Azure subscription
- Azure CLI installed and configured
- Basic knowledge of Azure Storage accounts
- Familiarity with HTML and web concepts

Let's get started by deploying our first static website on Azure Storage.
