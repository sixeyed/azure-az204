# VM Configuration Automation - Exercises Introduction

We've covered automating VM configuration to eliminate manual, time-consuming, error-prone setup tasks that don't scale - Azure provides options to configure VMs during deployment or after creation. Now let's automate VM setup hands-on.

## What You'll Do

You'll start by **exploring configuration options in the Portal** under the Advanced tab during VM creation: Extensions are add-ons running after VM creation that can install software or configure settings; Applications are packaged software components attachable to VMs; Cloud-init is an industry-standard Linux tool for configuring VMs on first boot. All serve the same purpose: automating configuration for scaling and consistency.

Then you'll **use custom script extension** to install Nginx automatically. You'll create a Linux VM, then add the extension using `az vm extension set` with JSON specifying commandToExecute running `apt-get update && apt-get install nginx -y`. The extension runs on the VM immediately, automatically installing and configuring the web server.

Next comes **configuring network access** by examining NSG rules with `az network nsg rule list`. You'll discover the default "DenyAllInBound" rule at priority 65500 blocking all incoming traffic from the Internet. You'll create a new rule with `az network nsg rule create` at priority 100 (lower numbers take precedence) allowing HTTP traffic on port 80 from the Internet, enabling web access to your Nginx server.

You'll **use run commands on Windows** with the `az vm run-command invoke` feature executing PowerShell scripts on-demand without installing extensions. You'll create a Windows 11 VM and run a setup script that installs development tools using Chocolatey package manager, demonstrating an easier alternative for on-demand script execution.

The lab challenge involves **testing network connectivity** between VMs using run commands to print IP addresses and test connectivity, discovering whether VMs in the same resource group are automatically networked together or if Azure networking works differently.

The key learning: Custom script extensions automate post-deployment configuration, cloud-init handles Linux provisioning, run commands execute on-demand scripts, and NSG rules with priority control network access following default-deny security principles.

Let's master VM configuration automation!
