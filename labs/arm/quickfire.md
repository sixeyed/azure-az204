# Azure Resource Manager (ARM) Templates - Quickfire Questions

## Question 1
What is an ARM template?


- A) Physical template
- B) Word document
- C) Excel spreadsheet
- D) JSON file defining infrastructure and configuration for Azure resources

**Answer: D**
ARM templates are JSON files implementing Infrastructure as Code for declarative Azure deployments.
---
## Question 2
What is Infrastructure as Code (IaC)?


- A) Managing infrastructure through code/configuration files instead of manual processes
- B) Application code
- C) Database code
- D) Programming only

**Answer: A**
IaC enables version-controlled, repeatable, automated infrastructure deployments.
---
## Question 3
What are the main sections of an ARM template?


- A) Only parameters
- B) One section
- C) Only resources
- D) Parameters, variables, resources, outputs

**Answer: D**
Parameters (inputs), variables (reusable values), resources (what to deploy), outputs (return values).
---
## Question 4
What is the purpose of parameters in ARM templates?


- A) Input values specified during deployment for customization
- B) Hard-coded values
- C) Not used
- D) Outputs only

**Answer: A**
Parameters make templates reusable by accepting different values per deployment (environment, size, location).
---
## Question 5
What deployment modes exist for ARM templates?


- A) Public and Private
- B) Incremental and Complete
- C) Fast and Slow
- D) Only one mode

**Answer: B**
Incremental: add/update resources, keep others. Complete: add/update specified, delete others in resource group.
---
## Question 6
What is the recommended deployment mode?


- A) Incremental (safer, preserves existing resources)
- B) Complete
- C) No preference
- D) Random

**Answer: A**
Incremental is safer, avoiding accidental deletions. Complete mode useful for clean deployments.
---
## Question 7
What is template linking?


- A) Database linking
- B) Network linking
- C) Hyperlinks in templates
- D) Referencing other templates for modular, reusable deployments

**Answer: D**
Linked templates break large deployments into smaller, manageable modules that can be reused.
---
## Question 8
What format does ARM templates use?


- A) JSON
- B) Plain text
- C) XML
- D) YAML

**Answer: A**
ARM templates are JSON documents, though Bicep provides an alternative DSL that transpiles to JSON.
---
## Question 9
Can you validate templates before deployment?


- A) Manual check only
- B) Only after deployment
- C) Yes, using `az deployment group validate` or portal validation
- D) No validation

**Answer: C**
Template validation checks syntax and some logical errors before actual deployment.
---
## Question 10
What is template idempotency?


- A) Template size
- B) Running same template multiple times produces same result without unintended changes
- C) Deployment speed
- D) Uniqueness

**Answer: B**
Idempotent templates can be re-run safely; Azure creates/updates as needed without duplicating resources.