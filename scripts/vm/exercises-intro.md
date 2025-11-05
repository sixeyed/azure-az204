# Virtual Machines - Exercises Introduction

We've covered Azure Virtual Machines as isolated compute environments running full operating systems with complete administrative permissions - supporting both Linux and Windows with preconfigured images and various compute sizes. Now let's provision and manage VMs hands-on.

## What You'll Do

You'll start by **exploring VMs in the Portal** to understand all configuration options: image selection browsing Ubuntu, Red Hat, Windows Server, SQL Server pre-configured variants; size selection seeing how costs scale with CPU cores and memory from a few dollars to hundreds per day; authentication options comparing SSH keys (more secure) vs passwords for Linux, username/password for Windows; and inbound port rules identifying which ports to open (port 22 for SSH on Linux, 3389 for RDP on Windows).

You'll observe **required dependencies** - all resources must belong to a resource group providing organization and lifecycle management; virtual networks for network infrastructure; network security groups (NSGs) acting as distributed firewalls; and public IP addresses for internet connectivity.

Then you'll **find valid VM sizes** for your subscription and region using `az vm list-sizes` with JMESPath queries filtering by cores and memory constraints. Availability varies by region and subscription type - Enterprise subscriptions might have access to sizes that free-tier subscriptions don't.

You'll **create a Linux VM** using `az vm create` specifying location, resource group, VM name, image (UbuntuLTS alias), and size. Creating takes a few minutes as Azure provisions all components: virtual network, network interface, public IP, NSG, and managed disk - all created automatically with sensible defaults.

Next, you'll **connect to the VM via SSH** using the public IP address retrieved with `az vm show --show-details`. You'll connect without specifying username or password because Azure generated SSH key pairs during creation and configured the VM with the public key. SSH automatically finds the private key in your .ssh directory for secure, convenient authentication.

You'll **explore the environment** running commands like top, uname -a, and curl to understand the Linux system, kernel information, and verify internet connectivity from the VM.

The lab challenge involves **investigating disk configuration** with `az` commands to understand disk size, performance tier, IOPS, and exploring the important concept of which resources persist after VM deletion for cost management.

The key learning: VMs provide full control over operating systems with supporting resources like VNets, NICs, PIPs, and NSGs. Understanding resource dependencies and lifecycles is critical for infrastructure management.

Let's master Azure Virtual Machines!
