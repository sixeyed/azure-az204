# ARM Templates - Introduction Script

## Opening

Welcome to this module on Azure Resource Manager templates, or ARM templates. In this lab, we'll explore the declarative approach to infrastructure deployment in Azure.

## What Are ARM Templates?

So far in this course, we've been using the Azure CLI to create and manage resources. This is what we call an imperative approach - you tell Azure exactly what to do, step by step. But there's a challenge with this approach: you need to add lots of checks to make sure you're not trying to create resources that already exist.

The alternative is the declarative approach. Instead of telling Azure HOW to do something, you describe WHAT you want the end result to be, and the tooling figures out whether it needs to create or update resources.

That's where ARM templates come in. ARM templates are JSON files that model the desired state of your Azure resources. They can live in source control alongside your application code, giving you version control and repeatability for your infrastructure.

## Understanding ARM Template Structure

Let's look at what an ARM template contains. Open the simple storage account template in your lab files. You'll see it has multiple blocks in the JSON:

First, we have **parameters** - these are values that can be changed for each deployment. Think of them as inputs to your template.

Next, we have **variables** - these set values that you'll use throughout the rest of the template. They help keep your template clean and maintainable.

Finally, we have **resources** - this is where you declare the actual Azure resources to create, using the variables and parameters you've defined.

## The Storage Account Resource

Let's examine the storage account resource definition. You'll see several key elements:

The **type** and **apiVersion** specify exactly what Azure resource we're defining. In this case, it's Microsoft.Storage/storageAccounts with a specific API version.

The **name** and **location** are read from parameters - this makes the template reusable. You can deploy the same template to different regions or with different names.

The **SKU** is read from a variable - we've set it to Standard_LRS.

And we have **properties** that define how the storage account should be configured. Notice we're setting supportsHttpsTrafficOnly to true, ensuring secure access.

When you share this template, anyone who deploys it will get exactly the same type of storage account: version 2, with Standard LRS redundancy, and HTTPS-only access. This consistency is one of the key benefits of the declarative approach.

## Desired State Deployment

Here's where ARM templates really shine. When you deploy an ARM template, Azure compares what you've described in the template with what currently exists in your subscription. It then makes only the changes necessary to reach that desired state.

This means ARM templates are idempotent - you can run the same deployment multiple times and get the same result, regardless of the current state.

## What's Next

In the exercises, we'll deploy ARM templates using the Azure CLI, explore the what-if feature to preview changes, and see how ARM templates help you identify and fix configuration drift.

Let's get started with the hands-on exercises.
