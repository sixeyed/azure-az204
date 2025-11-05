# Azure Resource Manager (ARM) Templates - Quickfire Questions

## Question 1
What is an ARM template?

- A) Physical template
- B) JSON file defining infrastructure and configuration for Azure resources
- C) Word document
- D) Excel spreadsheet

**Answer: B**
ARM templates are JSON files implementing Infrastructure as Code for declarative Azure deployments.

---

## Question 2
What is Infrastructure as Code (IaC)?

- A) Programming only
- B) Managing infrastructure through code/configuration files instead of manual processes
- C) Database code
- D) Application code

**Answer: B**
IaC enables version-controlled, repeatable, automated infrastructure deployments.

---

## Question 3
What are the main sections of an ARM template?

- A) Only resources
- B) Parameters, variables, resources, outputs
- C) Only parameters
- D) One section

**Answer: B**
Parameters (inputs), variables (reusable values), resources (what to deploy), outputs (return values).

---

## Question 4
What is the purpose of parameters in ARM templates?

- A) Hard-coded values
- B) Input values specified during deployment for customization
- C) Outputs only
- D) Not used

**Answer: B**
Parameters make templates reusable by accepting different values per deployment (environment, size, location).

---

## Question 5
What deployment modes exist for ARM templates?

- A) Only one mode
- B) Incremental and Complete
- C) Fast and Slow
- D) Public and Private

**Answer: B**
Incremental: add/update resources, keep others. Complete: add/update specified, delete others in resource group.

---

## Question 6
What is the recommended deployment mode?

- A) Complete
- B) Incremental (safer, preserves existing resources)
- C) No preference
- D) Random

**Answer: B**
Incremental is safer, avoiding accidental deletions. Complete mode useful for clean deployments.

---

## Question 7
What is template linking?

- A) Hyperlinks in templates
- B) Referencing other templates for modular, reusable deployments
- C) Network linking
- D) Database linking

**Answer: B**
Linked templates break large deployments into smaller, manageable modules that can be reused.

---

## Question 8
What format does ARM templates use?

- A) YAML
- B) JSON
- C) XML
- D) Plain text

**Answer: B**
ARM templates are JSON documents, though Bicep provides an alternative DSL that transpiles to JSON.

---

## Question 9
Can you validate templates before deployment?

- A) No validation
- B) Yes, using `az deployment group validate` or portal validation
- C) Only after deployment
- D) Manual check only

**Answer: B**
Template validation checks syntax and some logical errors before actual deployment.

---

## Question 10
What is template idempotency?

- A) Uniqueness
- B) Running same template multiple times produces same result without unintended changes
- C) Template size
- D) Deployment speed

**Answer: B**
Idempotent templates can be re-run safely; Azure creates/updates as needed without duplicating resources.
