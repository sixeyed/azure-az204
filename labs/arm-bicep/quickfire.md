# Bicep Templates - Quickfire Questions

## Question 1
What is Bicep?

- A) Muscle group
- B) Domain-specific language (DSL) for deploying Azure resources, alternative to ARM JSON
- C) Database language
- D) Programming language

**Answer: B**
Bicep is a declarative language that transpiles to ARM JSON, providing simpler, cleaner syntax.

---

## Question 2
What are the advantages of Bicep over ARM JSON?

- A) No advantages
- B) Simpler syntax, better tooling, type safety, modularity
- C) Only syntax
- D) Faster execution

**Answer: B**
Bicep reduces boilerplate, provides IntelliSense, compile-time validation, and easier module reuse.

---

## Question 3
How does Bicep relate to ARM templates?

- A) Completely different
- B) Bicep transpiles to ARM JSON; fully compatible with ARM ecosystem
- C) Bicep is deprecated
- D) No relation

**Answer: B**
Bicep is a transparent abstraction over ARM. All ARM features available; deploys as ARM JSON.

---

## Question 4
What is the file extension for Bicep?

- A) .json
- B) .bicep
- C) .yaml
- D) .txt

**Answer: B**
Bicep files use .bicep extension, distinguishing them from .json ARM templates.

---

## Question 5
How do you deploy a Bicep file?

- A) Cannot deploy
- B) az deployment group create --template-file main.bicep (automatic transpilation)
- C) Must convert to JSON manually first
- D) Only through portal

**Answer: B**
Azure CLI and PowerShell automatically transpile Bicep to JSON during deployment.

---

## Question 6
What is a module in Bicep?

- A) Hardware component
- B) Reusable Bicep file referenced from other Bicep files
- C) Database module
- D) Network module

**Answer: B**
Modules enable composition and reuse: define once, use across multiple deployments.

---

## Question 7
How do you define a resource in Bicep?

- A) JSON object
- B) resource <symbolic-name> '<type>@<api-version>' = { properties }
- C) XML element
- D) YAML block

**Answer: B**
Example: `resource storage 'Microsoft.Storage/storageAccounts@2021-06-01' = { ... }`

---

## Question 8
Does Bicep support parameters?

- A) No parameters
- B) Yes, using param keyword with types
- C) Only variables
- D) Only outputs

**Answer: B**
`param location string = 'eastus'` defines typed parameters with optional default values.

---

## Question 9
What is Bicep decompilation?

- A) Breaking compiled code
- B) Converting ARM JSON templates to Bicep format
- C) Removing deployment
- D) Not possible

**Answer: B**
`az bicep decompile --file template.json` converts existing ARM JSON to Bicep.

---

## Question 10
What tooling support does Bicep have?

- A) No tooling
- B) VS Code extension with IntelliSense, validation, snippets
- C) Only command line
- D) Only portal

**Answer: B**
Bicep VS Code extension provides rich authoring experience: autocomplete, validation, visualization.
