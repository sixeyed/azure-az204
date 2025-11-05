# IaaS with Bicep - Quickfire Questions

## Question 1
Why use Bicep for IaaS deployments?

- A) No benefits
- B) Declarative IaC with cleaner syntax than ARM JSON, version control, repeatability
- C) Only for documentation
- D) Required by Azure

**Answer: B**
Bicep simplifies infrastructure definitions, enabling consistent, version-controlled IaaS deployments.

---

## Question 2
How do you define a VM in Bicep?

- A) Manual creation
- B) Resource declaration with type 'Microsoft.Compute/virtualMachines@version'
- C) JSON only
- D) Not possible

**Answer: B**
Example: `resource vm 'Microsoft.Compute/virtualMachines@2023-03-01' = { properties: {...} }`

---

## Question 3
What dependencies must you define for VM deployment?

- A) None
- B) VNet, subnet, network interface, storage account/managed disk
- C) Only VNet
- D) Only disk

**Answer: B**
VMs require network interface (which needs subnet in VNet) and disk (managed or unmanaged).

---

## Question 4
How do you express dependencies in Bicep?

- A) Manual ordering
- B) Implicit via symbolic name references or explicit 'dependsOn'
- C) Not possible
- D) Time-based

**Answer: B**
Bicep infers dependencies from references; use dependsOn for explicit control.

---

## Question 5
Can you parameterize Bicep templates for reusability?

- A) No parameters
- B) Yes, using param keyword for inputs like VM size, location, name
- C) Hardcoded only
- D) Not recommended

**Answer: B**
Parameters enable deploying same template with different values per environment.

---

## Question 6
How do you deploy VMSS with Bicep?

- A) Not possible
- B) Define 'Microsoft.Compute/virtualMachineScaleSets' resource with scaling properties
- C) Manual only
- D) Requires JSON

**Answer: B**
VMSS resource type with capacity, upgrade policy, and VM profile configuration.

---

## Question 7
Can Bicep templates deploy load balancers and NSGs?

- A) VMs only
- B) Yes, all Azure resources including networking components
- C) Networking not supported
- D) Separate tools needed

**Answer: B**
Bicep supports all Azure resource types: networking, compute, storage, databases, etc.

---

## Question 8
What is a Bicep module for IaaS?

- A) Hardware component
- B) Reusable Bicep file defining common patterns (VM, networking) callable from main template
- C) Database module
- D) Not applicable

**Answer: B**
Modules promote reuse: create VM module, call from multiple templates with different parameters.

---

## Question 9
How do you manage secrets in Bicep templates?

- A) Hardcode in template
- B) Secure parameters, Key Vault references, avoid storing secrets in templates
- C) Plain text
- D) Not possible

**Answer: B**
Use @secure() decorator for sensitive parameters, reference Key Vault for existing secrets.

---

## Question 10
Can you validate Bicep before deployment?

- A) No validation
- B) Yes, using 'az deployment group validate' or Bicep CLI
- C) Only after deployment
- D) Manual review only

**Answer: B**
Validate syntax and some logic errors before actual deployment to catch issues early.
