# IaaS with Bicep Automation - AZ-204 Exam Introduction

Excellent work automating IaaS! This combines infrastructure as code concepts with IaaS resource management for the AZ-204.

## What We'll Cover

**Complete vs incremental deployment modes** is critical and frequently tested. Incremental (default) adds/updates resources matching the template, leaves other resources alone (safe for adding to existing groups). Complete deletes resources not in the template (dangerous - can accidentally remove resources if you forget to include them in the template). The exam tests understanding when to use each mode and the consequences of choosing wrong.

**Using existing keyword** to reference resources across Bicep files enables modular design. `resource vnet 'Microsoft.Network/virtualNetworks@2021-02-01' existing = { name: vnetName }` creates a reference to an existing resource without trying to create it. This allows one module to reference resources created by another module. The exam tests understanding of resource references and modular template design.

**The @secure decorator** marks parameters containing sensitive data (passwords, connection strings, API keys). Bicep ensures these values aren't logged or displayed. In ARM JSON, this is SecureString type. The exam tests proper handling of sensitive parameters.

**Custom script extensions for VM automation** execute scripts on VMs after deployment. Use for: installing software, configuring applications, deploying code, running setup scripts. Extensions download scripts from storage accounts or URLs, execute with appropriate permissions, and report success/failure. The exam tests when to use custom script extensions versus other approaches like Desired State Configuration or Azure Automation.

**Modular template design** with separate files for concerns (networking, database, compute) makes templates maintainable and reusable. Use modules with parameters to customize behavior. The exam tests understanding of modular design benefits and how to structure templates for reuse across environments.

**Resource dependencies and references** must be handled correctly. Bicep infers dependencies automatically when you reference resource properties. The exam tests understanding of dependency chains and what happens when dependencies aren't satisfied.

**Security with secure parameters and Key Vault** protects sensitive data. Never hardcode passwords in templates. Use Key Vault references in production. The exam tests security best practices for credential management in IaaS deployments.

We'll cover **what-if validation workflow**, **parameter files for environments**, **troubleshooting deployment failures**, **lifecycle management**, and **scenarios** about migrating from manual IaaS deployments to fully automated infrastructure as code.

Master IaaS automation for the AZ-204!
