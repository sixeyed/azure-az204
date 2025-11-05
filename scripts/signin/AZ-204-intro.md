# Azure Signin - AZ-204 Exam Introduction

Excellent work with Azure access methods! Understanding authentication and interaction approaches is foundational for the AZ-204 certification.

## What We'll Cover

**Azure account management** is fundamental. You need to understand the relationship between Azure accounts, tenants, and Subscriptions - one Microsoft account can have access to multiple Subscriptions, each Subscription is a logical container with its own billing and access management, and tenants represent Azure Active Directory instances. Authentication proves your identity, while authorization determines which resources you can access. The exam tests understanding of this hierarchy.

**Azure CLI proficiency** is critical throughout the exam. The CLI is the primary tool for creating App Services, managing Container Instances and AKS, configuring Azure Functions, setting up storage accounts and Cosmos DB, managing API Management, and configuring Key Vault. Being comfortable with `az` commands and their structure (`az [group] [subgroup] [command] [parameters]`) is crucial for exam success.

**Command structure and help system** should be mastered. Azure CLI follows consistent patterns like `az webapp create`, `az storage account create`, and `az functionapp create`. The integrated help with `-h` flags provides quick reference during the exam. Understanding this structure helps you discover and remember commands.

**Output formatting** enables different use cases. Table format (`-o table`) is for human reading with aligned columns. JSON format (default) is for programmatic parsing and detailed information. TSV format (`-o tsv`) is for simple scripting with tools like awk. Query format (`--query`) extracts specific values using JMESPath. The exam may test parsing CLI output for scripts.

**Cloud Shell capabilities** provide browser-based access. Pre-installed tools include Azure CLI, PowerShell, .NET SDK, Python, Git, kubectl, and more. Persistent storage maintains files and history across sessions. Automatic authentication eliminates the need for `az login`. The exam may present scenarios where Cloud Shell is the appropriate tool choice.

**Automation and repeatability** are key exam themes. The CLI enables scriptable operations for CI/CD pipelines, repeatable deployments with infrastructure as code, version-controlled resource definitions, and consistent environments across dev/test/prod. The exam tests understanding of when automation is appropriate versus manual Portal operations.

We'll cover **working across multiple Subscriptions** (using `az account set`), **authentication for automation** (service principals, managed identities), **integration with DevOps pipelines** (Azure Pipelines, GitHub Actions), **security best practices** (avoiding hardcoded credentials, using Key Vault), and **common scenarios** about choosing the right access method, scripting resource deployments, and troubleshooting authentication issues.

Master Azure access methods for the AZ-204!
