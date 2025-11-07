# Automating VM Configuration

## Reference

All new Virtual Machines need additional configuration after creation, and manual setup simply doesn't scale. Azure provides multiple options to automate VM configuration during or after deployment. Extensions run scripts and install software after the VM is created. Applications are packaged software components you can attach during provisioning. Cloud-init provides industry-standard Linux configuration on first boot. Run commands let you execute scripts on-demand without persistent extensions. These automation capabilities are essential for consistent, repeatable infrastructure deployments.

## Explore VM Configuration in the Portal

Let's start by exploring the configuration options available when creating a VM.

We're opening the Azure Portal and searching for "Virtual machines". Click Create, then Azure virtual machine to start the creation wizard.

Fill in the basic details - choose a subscription, create a new resource group, give your VM a name. Select an image like Ubuntu or Windows to get started.

Now, click on the Advanced tab. This is where you'll see the configuration options we'll be working with in this lab, and they're really powerful for automation.

The first option is Extensions - these are add-ons that run after the VM is created. They can install software, configure settings, or perform any post-deployment tasks you need. Microsoft and third parties publish a wide variety of extensions.

Next is Applications - these are packaged software components you can attach to your VM. Think of them as pre-built solutions that you can deploy alongside your VM.

And for Linux VMs specifically, there's Cloud-init - this is a industry-standard tool for configuring Linux VMs on first boot. It's incredibly powerful and lets you script the entire initial setup of your system.

These all serve the same purpose: automating the configuration so you don't have to manually log in and set things up yourself. This is crucial for scaling your infrastructure and ensuring consistency.

Don't actually create this VM through the Portal - we'll do that from the CLI for better repeatability. Cancel out of the creation wizard.

## Linux with Custom Script Extension

Now let's create a Linux VM and use a custom script extension to install Nginx web server automatically.

First, we're creating a resource group using az group create. We'll use the name "labs-vm-config" with the "courselabs=azure" tag for tracking, and deploy to West Europe. The resource group is our logical container for all the resources we'll create in this lab.

Next, we're creating an Ubuntu VM using az vm create. We're specifying the location as West Europe, the resource group we just created, naming the VM "web01", using the Ubuntu LTS image for long-term support, specifying a VM size that you have quota for in your subscription, and setting a public IP address DNS name for easy access. Replace the placeholders with your own values - use a VM size you have access to like Standard_B2s or Standard_D2s_v3, and choose a unique DNS name that's available in the region.

The VM will be created with SSH access enabled by default. Azure generates SSH keys for you if you don't already have them. This takes a few minutes while Azure provisions the VM and all its supporting resources.

Now comes the interesting part - we'll add a custom script extension to install Nginx automatically. Custom scripts are specified in JSON format. The schema can be complex for advanced scenarios, but for a simple command, we just need the commandToExecute property.

Our JSON looks like this conceptually: we're setting commandToExecute to run apt-get update to refresh the package lists, followed by apt-get install nginx to install the web server. The -y flag automatically answers yes to prompts, which is essential for automation.

Now, the exact syntax differs between shells. In PowerShell, we need to escape the quotes by doubling them. We're creating a variable called json that contains the JSON with doubled quotes around the property names and values.

In Bash, we don't need to escape the quotes the same way. We're setting a variable json with the JSON containing the commandToExecute property and the apt-get commands.

Now we're adding the extension to the VM using az vm extension set. We specify the resource group "labs-vm-config", the VM name "web01", the extension name "customScript" which is the identifier for Linux custom scripts, the publisher "Microsoft.Azure.Extensions" who provides this extension, and the settings parameter containing our JSON variable.

The extension starts running on the VM immediately. You can watch the progress in the Portal - navigate to your VM and look at the Extensions and applications blade. You'll see the extension listed with its status, and you can watch it progress from Installing to Succeeded.

## Test the Web Server

When the extension completes, Nginx is installed and running on the VM. But if you try to browse to the VM's public IP address, you won't be able to access the web server. The connection will timeout.

Why? Because incoming traffic is blocked by the Network Security Group. Azure created an NSG automatically when we created the VM, but it only allows SSH traffic by default.

Let's examine the NSG to understand what's happening. First, we're listing the NSGs in the resource group using az network nsg list with table output for easy reading.

You'll see an NSG with a name like "web01NSG" - Azure automatically created this with the same base name as your VM. Now let's list the rules using az network nsg rule list. We're specifying the resource group, including the default rules with the --include-default flag, using table output, and providing the NSG name.

Look at the default rules in the output. There's a rule called "DenyAllInBound" with priority 65500. This blocks all incoming traffic from the Internet. Lower priority numbers take precedence, so rules with priority 100, 200, etc. will be evaluated before this deny rule.

To allow HTTP traffic, we need to add a rule with a higher priority - remember, lower numbers mean higher priority, so a rule with priority 100 will be checked before priority 65500.

We're creating a new rule using az network nsg rule create. The resource group is "labs-vm-config", the NSG name is "web01NSG", we're naming the rule "http" for clarity, setting priority to 100 to ensure it's evaluated early, specifying source address prefixes as "Internet" to allow traffic from anywhere, setting destination port ranges to 80 for HTTP, and setting access to Allow.

Now when the rule is created and applied, browse to your VM's DNS name or public IP address. You should see the default Nginx welcome page displaying in your browser. The custom script extension successfully installed and started Nginx, and now we've opened the network path to access it.

## Windows with VM Extension

Windows VMs also support custom script extensions, but there's an easier option for running scripts on Windows: the run-command feature. This lets you execute PowerShell scripts on-demand without installing an extension.

Let's create a Windows 11 VM to explore this. We're using az vm create with location West Europe, resource group "labs-vm-config", VM name "dev01", and here's the important part - the image parameter. You'll need to specify a Windows 11 image URN. Use a format like "MicrosoftWindowsDesktop:windows-11:win11-22h2-pro:latest" or check available images first.

We're also setting the size to Standard_D4s_v5 or another size that supports Windows 11, providing an admin username, setting a public IP address DNS name that's unique, and creating an admin password. Make sure to use a strong password that meets Azure's complexity requirements - at least 12 characters with uppercase, lowercase, numbers, and special characters.

Use a VM size you have access to, and make sure your password is strong enough - Azure will reject weak passwords. The VM creation takes several minutes, especially for Windows desktop operating systems which are larger than server editions.

When the VM is created, we can run a PowerShell script on it using the run-command feature. There's a script in the labs folder called setup.ps1 that installs development tools using Chocolatey, a popular Windows package manager.

We're running az vm run-command invoke with the command-id set to "RunPowerShellScript" which tells Azure we're executing PowerShell, specifying the resource group and VM name, and using the --scripts parameter with the @ symbol to read the script from the file at labs/vm-config/setup.ps1.

The command executes on the remote VM and returns the output. The output isn't very user-friendly - it's wrapped in JSON with lots of metadata - but you should see a message indicating that Chocolatey installed packages successfully. Look for messages about installing Git, Visual Studio Code, or other tools depending on what's in the setup script.

You can connect to the VM with Remote Desktop Protocol to verify the tools are actually installed and working. The RDP connection will show you the Windows desktop with all the development tools ready to use.

## Lab

Here's a challenge for you. We've created two VMs in this lab - web01 running Linux and dev01 running Windows. They're both in the same resource group called "labs-vm-config".

Are they connected on a private network? Can they reach each other using their private IP addresses?

Your task is to use run commands on both VMs to print their IP addresses and test network connectivity between them. For the Linux VM, you can use commands like "hostname -I" to get the IP address and "ping" to test connectivity. For the Windows VM, PowerShell commands like "Get-NetIPAddress" and "Test-Connection" will work.

Hint: You don't need to write script files for this. You can use the built-in run commands - look for RunShellScript for Linux and RunPowerShellScript for Windows. The --scripts parameter accepts inline scripts, not just file references.

Try this yourself before checking the solution. Think about what you expect to happen - are VMs in the same resource group automatically networked together, or does networking work differently in Azure?

## Cleanup

When you're done experimenting, remember to delete the resource group to remove all resources and stop incurring charges.

We're running az group delete with the resource group name "labs-vm-config", the -y flag to skip the confirmation prompt, and --no-wait to run asynchronously.

This removes everything we created: both VMs, their disks, network interfaces, NSGs, public IP addresses, and the virtual network. The --no-wait flag means the command returns immediately while the deletion continues in the background, which is useful when cleaning up large environments.
