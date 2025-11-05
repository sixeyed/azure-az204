# Resource Groups - Introduction Script

## Opening

Welcome to this tutorial on Azure Resource Groups. Resource Groups are one of the fundamental building blocks of Azure, and understanding them is essential for managing your cloud resources effectively.

## What are Resource Groups?

Resource Groups, or RGs, are containers for all other Azure resources. Think of them as organizational folders that hold everything your application needs - virtual machines, SQL databases, Kubernetes clusters, storage accounts - they all live inside a Resource Group.

You typically create one Resource Group for each application, containing all the components that app requires. This logical grouping makes it much easier to manage your Azure resources as a cohesive unit.

## Key Benefits

There are several important benefits to using Resource Groups:

First, management permissions can be applied at the Resource Group level. This means you can grant a team access to everything they need for their application in one go, without having to set permissions on individual resources.

Second, Resource Groups make cleanup incredibly easy. When you delete a Resource Group, all the resources inside it are automatically deleted. This is perfect for development and testing scenarios where you want to quickly tear down an entire environment.

Third, they provide a way to organize your resources logically, which becomes increasingly important as your Azure footprint grows.

## Regions and Location

One important concept to understand is that Resource Groups themselves have a location - a specific Azure region. This region determines where the metadata about your Resource Group is stored.

Each region is a collection of nearby data centers. Typically, you'll put all the components for an application into the same region to minimize network latency between services. However, you might create additional deployments in other regions for high availability or to serve users in different geographic locations.

## Tags

Tags are simple key-value pairs that you can attach to Resource Groups and other resources. They're incredibly useful for organizing and managing resources at scale. For example, you might use an "environment" tag to identify resources in development, testing, or production environments, or a "cost-center" tag for billing purposes.

## What's Next

In this lab, we'll explore Resource Groups hands-on. We'll create them using both the Azure Portal and the Azure CLI, learn how to query and filter them, and practice managing them. By the end, you'll have a solid foundation in working with this essential Azure service.

Let's get started!
