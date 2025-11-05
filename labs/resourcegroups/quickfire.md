# Azure Resource Groups - Quickfire Questions

## Question 1
What is an Azure Resource Group?


- A) Logical container for grouping related Azure resources
- B) Network group
- C) Security group
- D) User group

**Answer: A**
Resource groups organize resources sharing lifecycle, permissions, and management scope.
---
## Question 2
Can a resource belong to multiple resource groups?


- A) Up to 5 groups
- B) Yes, multiple groups
- C) Depends on resource type
- D) No, each resource belongs to exactly one resource group

**Answer: D**
Resources exist in only one resource group, though they can reference resources in other groups.
---
## Question 3
What happens when you delete a resource group?


- A) Resources moved to default group
- B) Nothing happens
- C) Only group metadata deleted
- D) All resources within the group are deleted

**Answer: D**
Deleting a resource group permanently deletes all contained resources - use with caution.
---
## Question 4
Can resources in a resource group be in different regions?


- A) No, same region only
- B) Requires special configuration
- C) Only adjacent regions
- D) Yes, resources can be in any region

**Answer: D**
Resource group location stores metadata; resources can be deployed to any Azure region.
---
## Question 5
What is the purpose of resource group location?


- A) Stores metadata about the resource group
- B) No purpose
- C) Sets billing region
- D) Determines resource location

**Answer: A**
Resource group location only affects where management metadata is stored, not where resources are deployed.
---
## Question 6
Can you move resources between resource groups?


- A) Only same region
- B) Yes, most resources support move operations (with some exceptions)
- C) Only within same subscription
- D) Never

**Answer: B**
Most resources can move between groups or subscriptions, though some restrictions apply (check documentation).
---
## Question 7
What permissions model applies to resource groups?


- A) Public access
- B) No permissions
- C) Only owner access
- D) Azure RBAC (Role-Based Access Control)

**Answer: D**
RBAC roles assigned at resource group level inherit to contained resources.
---
## Question 8
What is a resource lock?


- A) Prevents accidental deletion or modification of resources
- B) Billing lock
- C) Network lock
- D) Security encryption

**Answer: A**
Locks (ReadOnly or CanNotDelete) prevent changes even by authorized users, protecting critical resources.
---
## Question 9
What lock types exist?


- A) Public and Private
- B) Only one type
- C) Delete and Modify
- D) CanNotDelete and ReadOnly

**Answer: D**
CanNotDelete: allows reads/updates, prevents deletion. ReadOnly: allows reads only, prevents updates/deletions.
---
## Question 10
Can you apply tags to resource groups?


- A) Only to resources
- B) Only one tag
- C) No tagging
- D) Yes, for organization, cost tracking, automation

**Answer: D**
Tags (key-value pairs) categorize resources for management, billing, and automation. Note: tags don't automatically inherit to resources.