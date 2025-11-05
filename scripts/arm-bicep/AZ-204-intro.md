# ARM Templates with Bicep - AZ-204 Exam Introduction

Excellent work with Bicep! While the exam may not test Bicep syntax directly, understanding infrastructure as code concepts applies to both JSON and Bicep.

## What We'll Cover

**Infrastructure as code concepts** are fundamental regardless of format. Repeatability (deploy the same infrastructure multiple times consistently), Version control (track infrastructure changes in Git), Consistency (eliminate manual configuration differences), Documentation (templates serve as infrastructure documentation). The exam tests understanding of why infrastructure as code matters.

**ARM template structure** remains consistent between JSON and Bicep. Parameters define inputs, Variables hold reusable values, Resources declare infrastructure, Outputs return values. The syntax differs but the concepts are identical. The exam tests understanding of template structure regardless of format - knowing Bicep helps you understand ARM template questions.

**Deployment modes** are critical. Incremental mode (default) adds or updates resources matching the template, leaving other resources in the group untouched. Complete mode removes resources not in the template - dangerous if you forget to include existing resources! The exam heavily tests when to use each mode and the consequences of choosing wrong.

**Parameterization and reusability** enable using one template across environments. Parameters for environment-specific values (names, SKUs, sizes), Variables for calculated values, Conditional resources with if expressions, Loops for creating multiple similar resources. The exam tests designing templates that work across dev/test/prod environments.

**Resource dependencies** are handled differently in Bicep versus JSON. Bicep has implicit dependencies (automatically detects when resources reference each other), JSON requires explicit dependsOn arrays (manual dependency management). Understanding dependencies is important for exam questions about deployment order and troubleshooting circular dependencies.

**What-if analysis for validation** works identically with Bicep and JSON templates. `az deployment group what-if` previews changes, showing creates/updates/deletes. The exam tests when to use what-if and how to interpret results.

We'll cover **Bicep advantages** (cleaner syntax, better type safety, modules for reusability), **transpilation to ARM JSON** (Bicep compiles to JSON before deployment), **deployment validation**, **common scenarios** about troubleshooting templates, and **organizing infrastructure code** with modules and parameter files.

Master infrastructure as code for the AZ-204!
