# IaaS with Bicep Automation - Exercises Introduction

We've covered automating IaaS deployments using Bicep Infrastructure as Code, combining full control with complete automation. Now let's implement a fully automated IaaS environment.

## What You'll Do

You'll **examine modular Bicep structure** split across multiple files - networking.bicep for VNet and subnet, database.bicep for SQL Server, and vm.bicep for Windows VMs. Each file focuses on one concern, making the code more maintainable. The files use **JSON variables and loadJsonContent** to share configuration across modules.

You'll **deploy core networking resources** (VNet, subnet, NSG) first. Then you'll practice **incremental vs complete deployment modes** with what-if validation. Incremental mode (default) adds or updates resources matching the template, leaving others untouched. Complete mode removes resources not in the template - dangerous if you forget to include existing resources! You'll see what-if show the difference before making changes.

Next comes **SQL Server deployment** with secure parameters (@secure decorator) for admin password. The what-if validation shows exactly what will be created before you commit.

The exciting part is the **Windows VM with custom script extension**. Instead of manually connecting via RDP and installing IIS, the custom script extension **automatically installs IIS, deploys your application, and configures everything** without human intervention. You define the entire setup process in the Bicep template.

You'll use **run-command to verify setup logs** remotely, checking that the custom script executed successfully. Then you'll **test the fully automated deployment** - from empty resource group to working application, all defined in code with zero manual steps.

The key learning: custom script extensions turn IaaS into infrastructure as code. The same automation benefits you get from PaaS, but with full control over the OS and configuration.

Let's automate IaaS deployments!
