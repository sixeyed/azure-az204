# IaaS with Bicep - Quickfire Questions

## Question 1
Why use Bicep for IaaS deployments?


- A) Declarative IaC with cleaner syntax than ARM JSON, version control, repeatability
- B) Required by Azure
- C) No benefits
- D) Only for documentation

**Answer: A**
Bicep simplifies infrastructure definitions, enabling consistent, version-controlled IaaS deployments.
---
## Question 2
How do you define a VM in Bicep?


- A) JSON only
- B) Manual creation
- C) Resource declaration with type 'Microsoft.Compute/virtualMachines@version'
- D) Not possible

**Answer: C**
Example: `resource vm 'Microsoft.Compute/virtualMachines@2023-03-01' = { properties: {...} }`
---
## Question 3
What dependencies must you define for VM deployment?


- A) Only VNet
- B) VNet, subnet, network interface, storage account/managed disk
- C) Only disk
- D) None

**Answer: B**
VMs require network interface (which needs subnet in VNet) and disk (managed or unmanaged).
---
## Question 4
How do you express dependencies in Bicep?


- A) Not possible
- B) Implicit via symbolic name references or explicit 'dependsOn'
- C) Time-based
- D) Manual ordering

**Answer: B**
Bicep infers dependencies from references; use dependsOn for explicit control.
---
## Question 5
Can you parameterize Bicep templates for reusability?


- A) Not recommended
- B) Hardcoded only
- C) No parameters
- D) Yes, using param keyword for inputs like VM size, location, name

**Answer: D**
Parameters enable deploying same template with different values per environment.
---
## Question 6
How do you deploy VMSS with Bicep?


- A) Not possible
- B) Manual only
- C) Define 'Microsoft.Compute/virtualMachineScaleSets' resource with scaling properties
- D) Requires JSON

**Answer: C**
VMSS resource type with capacity, upgrade policy, and VM profile configuration.
---
## Question 7
Can Bicep templates deploy load balancers and NSGs?


- A) Separate tools needed
- B) VMs only
- C) Networking not supported
- D) Yes, all Azure resources including networking components

**Answer: D**
Bicep supports all Azure resource types: networking, compute, storage, databases, etc.
---
## Question 8
What is a Bicep module for IaaS?


- A) Not applicable
- B) Hardware component
- C) Reusable Bicep file defining common patterns (VM, networking) callable from main template
- D) Database module

**Answer: C**
Modules promote reuse: create VM module, call from multiple templates with different parameters.
---
## Question 9
How do you manage secrets in Bicep templates?


- A) Not possible
- B) Secure parameters, Key Vault references, avoid storing secrets in templates
- C) Plain text
- D) Hardcode in template

**Answer: B**
Use @secure() decorator for sensitive parameters, reference Key Vault for existing secrets.
---
## Question 10
Can you validate Bicep before deployment?


- A) Manual review only
- B) Yes, using 'az deployment group validate' or Bicep CLI
- C) Only after deployment
- D) No validation

**Answer: B**
Validate syntax and some logic errors before actual deployment to catch issues early.