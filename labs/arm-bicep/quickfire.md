# Bicep Templates - Quickfire Questions

## Question 1
What is Bicep?


- A) Database language
- B) Muscle group
- C) Domain-specific language (DSL) for deploying Azure resources, alternative to ARM JSON
- D) Programming language

**Answer: C**
Bicep is a declarative language that transpiles to ARM JSON, providing simpler, cleaner syntax.
---
## Question 2
What are the advantages of Bicep over ARM JSON?


- A) No advantages
- B) Faster execution
- C) Simpler syntax, better tooling, type safety, modularity
- D) Only syntax

**Answer: C**
Bicep reduces boilerplate, provides IntelliSense, compile-time validation, and easier module reuse.
---
## Question 3
How does Bicep relate to ARM templates?


- A) Bicep transpiles to ARM JSON; fully compatible with ARM ecosystem
- B) No relation
- C) Completely different
- D) Bicep is deprecated

**Answer: A**
Bicep is a transparent abstraction over ARM. All ARM features available; deploys as ARM JSON.
---
## Question 4
What is the file extension for Bicep?


- A) .bicep
- B) .yaml
- C) .json
- D) .txt

**Answer: A**
Bicep files use .bicep extension, distinguishing them from .json ARM templates.
---
## Question 5
How do you deploy a Bicep file?


- A) Must convert to JSON manually first
- B) Only through portal
- C) Cannot deploy
- D) az deployment group create --template-file main.bicep (automatic transpilation)

**Answer: D**
Azure CLI and PowerShell automatically transpile Bicep to JSON during deployment.
---
## Question 6
What is a module in Bicep?


- A) Database module
- B) Hardware component
- C) Reusable Bicep file referenced from other Bicep files
- D) Network module

**Answer: C**
Modules enable composition and reuse: define once, use across multiple deployments.
---
## Question 7
How do you define a resource in Bicep?


- A) resource <symbolic-name> '<type>@<api-version>' = { properties }
- B) YAML block
- C) JSON object
- D) XML element

**Answer: A**
Example: `resource storage 'Microsoft.Storage/storageAccounts@2021-06-01' = { ... }`
---
## Question 8
Does Bicep support parameters?


- A) Yes, using param keyword with types
- B) Only outputs
- C) No parameters
- D) Only variables

**Answer: A**
`param location string = 'eastus'` defines typed parameters with optional default values.
---
## Question 9
What is Bicep decompilation?


- A) Not possible
- B) Breaking compiled code
- C) Removing deployment
- D) Converting ARM JSON templates to Bicep format

**Answer: D**
`az bicep decompile --file template.json` converts existing ARM JSON to Bicep.
---
## Question 10
What tooling support does Bicep have?


- A) VS Code extension with IntelliSense, validation, snippets
- B) No tooling
- C) Only command line
- D) Only portal

**Answer: A**
Bicep VS Code extension provides rich authoring experience: autocomplete, validation, visualization.