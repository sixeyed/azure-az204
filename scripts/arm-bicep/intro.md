# ARM Templates with Bicep - Introduction Narration Script

## Opening

Welcome to this lab on ARM Templates with Bicep. In this session, we'll explore how Bicep simplifies infrastructure as code for Azure deployments.

## What Are ARM Templates?

ARM templates represent an important evolution in cloud infrastructure management. The concepts behind them - infrastructure as code, parameterized deployments, and desired-state delivery - are fundamental to modern cloud architecture.

However, there's a challenge. The JSON format that ARM templates traditionally use can be difficult to work with, especially when you're dealing with larger applications that involve multiple resources. The syntax can become verbose and hard to maintain.

## Enter Bicep

This is where Bicep comes in. Bicep is the evolution of ARM templates - a new tool that uses a custom domain-specific language to define Azure resources in a simpler and more manageable way.

Let me show you an example. Here's how you define a Storage Account in Bicep:

[SHOW CODE ON SCREEN]

```
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-06-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: storageSku
  }
  kind: 'StorageV2'
  properties: {
    supportsHttpsTrafficOnly: httpsOnly
  }
}
```

Notice how clean this syntax is compared to JSON. The resource type specifies the API version it's using, but the rest of the template is much more readable.

## Key Advantages of Bicep

There are several advantages to using Bicep over traditional ARM JSON templates:

First, the syntax is cleaner. Field names and values don't need to be quoted, and there's less indentation noise.

Second, parameters and variables have simple, readable names like "location" and "storageSku" - no complex bracket notation required.

Third, and this is important, templates can include comments. This makes your infrastructure code self-documenting and easier for teams to maintain.

## Deployment Workflow

Here's the great news about Bicep: you don't need any additional tools to deploy Bicep files. The Azure CLI and PowerShell modules understand Bicep natively.

You can deploy Bicep files directly to Azure, or if you need to, you can generate ARM JSON files from your Bicep templates. This gives you flexibility in your deployment pipeline.

The output from deploying a Bicep template is exactly the same as deploying a JSON ARM template - Azure treats them identically under the hood.

## Bicep Tools

Bicep includes powerful tooling that bridges the gap between old and new. With the Bicep CLI, you can:

- Generate Bicep files from existing JSON ARM templates - useful for migrating legacy infrastructure code
- Compile Bicep files to JSON - helpful for pipelines that still expect JSON
- Use what-if analysis to preview changes before deployment

You can install the Bicep tools directly from the Azure CLI with a simple command. The tools integrate seamlessly with your existing Azure workflows.

## Why This Matters

Bicep is now the preferred way of using ARM. While JSON templates are still supported and many existing projects use them, Microsoft is investing heavily in Bicep as the future of Azure infrastructure as code.

For anyone working with Azure, especially those preparing for certifications or building production infrastructure, understanding Bicep is essential.

In the exercises that follow, we'll get hands-on experience with Bicep - deploying resources, converting JSON to Bicep, and evolving infrastructure specifications.

Let's get started.
