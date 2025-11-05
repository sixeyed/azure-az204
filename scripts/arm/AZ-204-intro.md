# ARM Templates - AZ-204 Exam Introduction

Great work with ARM template deployments! Infrastructure as code is an important AZ-204 exam topic covering deployment automation and consistency.

## What We'll Cover

**Declarative vs imperative approaches** is fundamental. Imperative (Azure CLI commands) specifies step-by-step how to create resources - you control the order and must handle dependencies. Declarative (ARM templates) specifies what you want - Azure figures out the order and handles dependencies. The exam tests when to use each approach: CLI for quick one-off tasks, templates for repeatable production deployments.

**ARM template structure** must be understood. Parameters section defines inputs (environment-specific values like names and SKUs), Variables section contains reusable values calculated from parameters, Resources section declares what to deploy (the actual infrastructure), Outputs section returns values for use by other templates or scripts. The exam tests reading and understanding template structure.

**Idempotent operations** are critical. Templates should produce the same result when deployed multiple times - no duplicate resources, no errors. Azure checks if resources already exist and updates them to match the template rather than failing or creating duplicates. The exam tests understanding of idempotency and recognizing when templates aren't idempotent (like dynamic IP allocation).

**What-if operations** for deployment validation appear frequently. The `az deployment group what-if` command previews changes without applying them, showing what will be created, modified, or deleted. This helps catch mistakes before they affect production. The exam tests when to use what-if for validation.

**Configuration drift detection** uses what-if to identify when actual infrastructure differs from the template. If someone manually changes resources through Portal or CLI, what-if shows the discrepancy. The exam tests understanding of drift and how templates help maintain consistency.

**Deployment scopes** need to be known. Resource group (most common for application resources), Subscription (for policy and budget resources), Management group (for cross-subscription governance), Tenant (for tenant-wide resources). The exam focuses on resource group deployments for application scenarios.

We'll cover **parameter files for environment-specific values**, **linking templates for modular deployments**, **deployment modes** (incremental adds/updates vs complete removes unlisted resources), and **common scenarios** about troubleshooting template errors and organizing infrastructure code.

Master ARM templates for the AZ-204!
