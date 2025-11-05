# Azure Resource Groups - Quickfire Questions

## Question 1
What is an Azure Resource Group?

- A) User group
- B) Logical container for grouping related Azure resources
- C) Security group
- D) Network group

**Answer: B**
Resource groups organize resources sharing lifecycle, permissions, and management scope.

---

## Question 2
Can a resource belong to multiple resource groups?

- A) Yes, multiple groups
- B) No, each resource belongs to exactly one resource group
- C) Up to 5 groups
- D) Depends on resource type

**Answer: B**
Resources exist in only one resource group, though they can reference resources in other groups.

---

## Question 3
What happens when you delete a resource group?

- A) Only group metadata deleted
- B) All resources within the group are deleted
- C) Resources moved to default group
- D) Nothing happens

**Answer: B**
Deleting a resource group permanently deletes all contained resources - use with caution.

---

## Question 4
Can resources in a resource group be in different regions?

- A) No, same region only
- B) Yes, resources can be in any region
- C) Only adjacent regions
- D) Requires special configuration

**Answer: B**
Resource group location stores metadata; resources can be deployed to any Azure region.

---

## Question 5
What is the purpose of resource group location?

- A) Determines resource location
- B) Stores metadata about the resource group
- C) Sets billing region
- D) No purpose

**Answer: B**
Resource group location only affects where management metadata is stored, not where resources are deployed.

---

## Question 6
Can you move resources between resource groups?

- A) Never
- B) Yes, most resources support move operations (with some exceptions)
- C) Only within same subscription
- D) Only same region

**Answer: B**
Most resources can move between groups or subscriptions, though some restrictions apply (check documentation).

---

## Question 7
What permissions model applies to resource groups?

- A) No permissions
- B) Azure RBAC (Role-Based Access Control)
- C) Only owner access
- D) Public access

**Answer: B**
RBAC roles assigned at resource group level inherit to contained resources.

---

## Question 8
What is a resource lock?

- A) Security encryption
- B) Prevents accidental deletion or modification of resources
- C) Network lock
- D) Billing lock

**Answer: B**
Locks (ReadOnly or CanNotDelete) prevent changes even by authorized users, protecting critical resources.

---

## Question 9
What lock types exist?

- A) Only one type
- B) CanNotDelete and ReadOnly
- C) Delete and Modify
- D) Public and Private

**Answer: B**
CanNotDelete: allows reads/updates, prevents deletion. ReadOnly: allows reads only, prevents updates/deletions.

---

## Question 10
Can you apply tags to resource groups?

- A) No tagging
- B) Yes, for organization, cost tracking, automation
- C) Only to resources
- D) Only one tag

**Answer: B**
Tags (key-value pairs) categorize resources for management, billing, and automation. Note: tags don't automatically inherit to resources.
