# Resource Groups - AZ-204 Exam Introduction

Great work with Resource Groups! While basic, this is foundational knowledge for all AZ-204 topics involving Azure resources.

## What We'll Cover

**Infrastructure as Code** deployment of Resource Groups programmatically with CLI (`az group create`), PowerShell (`New-AzResourceGroup`), ARM templates, or Bicep. The exam tests understanding of automated resource group creation as part of deployment pipelines.

**Resource Group scope in the hierarchy** needs to be understood. Management Group > Subscription > Resource Group > Resource. Each level provides a boundary for organizing resources and applying governance. Resource Groups are the most common scope for RBAC, policies, and cost allocation. The exam tests understanding of this hierarchy.

**Azure RBAC at Resource Group level** with permission inheritance means granting permissions at the RG level automatically applies to all resources within. Contributor role on RG grants Contributor to all resources. This simplifies permission management but requires understanding inheritance implications. The exam tests RBAC scope and inheritance patterns.

**Cost management using tags** enables allocation and tracking across projects, departments, or environments. Tags like `CostCenter=Marketing` or `Environment=Production` help attribute costs. Important: tags on Resource Groups **do not inherit** to resources - you must tag resources separately if needed. The exam tests understanding of tag inheritance (or lack thereof).

**CLI operations with `az group` commands** are essential. `create` (provision), `list` (view all), `show` (get details), `delete` (remove with all resources), `exists` (check if exists). Know command syntax and common parameters. The exam may test CLI usage scenarios.

**Cascading deletion behavior** means deleting a Resource Group deletes all contained resources automatically. This is convenient for cleanup but dangerous if you accidentally delete the wrong group. The exam tests understanding of deletion consequences.

**Resource locks** (CanNotDelete or ReadOnly) applied at Resource Group level prevent deletion or modification of all contained resources. Locks protect production resources from accidental changes. The exam tests when to use locks and their inheritance behavior.

**Limitations on moving resources** between groups include some services that don't support moves, and resources can't move across subscriptions easily. The exam tests understanding of move constraints.

We'll cover **organizational strategies** (separate RGs per environment vs per application), **JMESPath queries** for filtering, **lifecycle management**, **cost optimization**, and **common scenarios** about designing resource group strategies for multi-environment applications.

Master Resource Group fundamentals for the AZ-204!
