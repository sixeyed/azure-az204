# VM Configuration Automation - Exercises

## Exercise 1: Exploring Configuration Options

Let's start by exploring the configuration options available when creating a VM.

Open the Azure Portal and search for "Virtual machines". Click Create, then Azure virtual machine.

Fill in the basic details - choose a subscription, create a new resource group, give your VM a name. Select an image like Ubuntu or Windows.

Now, click on the Advanced tab. This is where you'll see the configuration options we'll be working with:

**Extensions** - these are add-ons that run after the VM is created
**Applications** - these are packaged software components you can attach
**Cloud-init** - for Linux VMs, this configures the VM on first boot

These all serve the same purpose: automating the configuration so you don't have to do it manually.

Don't actually create this VM - we'll do that from the CLI. Cancel out of the creation wizard.

## Exercise 2: Linux VM with Custom Script Extension

Now let's create a Linux VM and use a custom script extension to install Nginx web server.

First, create a resource group. We'll use the name "labs-vm-config" and deploy to West Europe:

```
az group create -n labs-vm-config --tags courselabs=azure -l westeurope
```

Next, create an Ubuntu VM. Replace the placeholders with your own values - use a VM size you have access to, and choose a unique DNS name:

```
az vm create -l westeurope -g labs-vm-config -n web01 --image UbuntuLTS --size YOUR_VM_SIZE --public-ip-address-dns-name YOUR_DNS_NAME
```

The VM will be created with SSH access. Now we'll add a custom script extension to install Nginx.

Custom scripts are specified in JSON. The schema can be complex, but for a simple command, we just need the commandToExecute property.

Our JSON looks like this:

```
{ "commandToExecute": "apt-get -y update && apt-get install -y nginx" }
```

This updates the package list and installs Nginx.

In PowerShell, we need to escape the quotes:

```
$json='{ ""commandToExecute"": ""apt-get -y update && apt-get install -y nginx"" }'
```

In Bash, we don't:

```
json='{ "commandToExecute": "apt-get -y update && apt-get install -y nginx" }'
```

Now add the extension to the VM:

```
az vm extension set -g labs-vm-config --vm-name web01 --name customScript --publisher Microsoft.Azure.Extensions --settings "$json"
```

The extension will run on the VM. You can watch the progress in the Portal - navigate to your VM and look at the Extensions + applications blade.

## Exercise 3: Configuring Network Access

When the extension completes, Nginx is installed and running. But if you try to browse to the VM's public IP address, you won't be able to access it.

Why? Because incoming traffic is blocked by the Network Security Group.

Let's examine the NSG. First, list the NSGs in the resource group:

```
az network nsg list -g labs-vm-config -o table
```

You'll see an NSG with a name like "web01NSG". Now list the rules:

```
az network nsg rule list -g labs-vm-config --include-default -o table --nsg-name web01NSG
```

Look at the default rules. There's a rule called "DenyAllInBound" with priority 65500. This blocks all incoming traffic from the Internet.

To allow HTTP traffic, we need to add a rule with a higher priority - remember, lower numbers mean higher priority.

Create a new rule to allow port 80:

```
az network nsg rule create -g labs-vm-config --nsg-name web01NSG -n http --priority 100 --source-address-prefixes Internet --destination-port-ranges 80 --access Allow
```

Now when the rule is created, browse to your VM's DNS name. You should see the default Nginx welcome page.

## Exercise 4: Windows VM with Run Command

Windows VMs also support custom script extensions, but there's an easier option for running scripts: the run-command feature.

Let's create a Windows 11 VM:

```
az vm create -l westeurope -g labs-vm-config -n dev01 --image YOUR_WINDOWS_11_IMAGE --size Standard_D4s_v5 --admin-username labs --public-ip-address-dns-name YOUR_UNIQUE_DNS_NAME --admin-password YOUR_STRONG_PASSWORD
```

Use a VM size you have access to, and make sure to use a strong password that meets Azure's complexity requirements.

When the VM is created, we can run a PowerShell script on it. The script is in the labs folder and it installs development tools using Chocolatey.

Run the command:

```
az vm run-command invoke --command-id RunPowerShellScript -g labs-vm-config --name dev01 --scripts @labs/vm-config/setup.ps1
```

The output isn't very user-friendly, but you should see a message indicating that Chocolatey installed packages successfully.

You can connect to the VM with RDP to verify the tools are installed.

## Lab Exercise

Here's a challenge for you. We've created two VMs - web01 (Linux) and dev01 (Windows). They're in the same resource group.

Are they connected on a private network? Can they reach each other?

Use run commands on both VMs to:
1. Print the IP addresses
2. Test network connectivity between them

Hint: You can use built-in run commands - you don't need to write scripts. Look for commands like RunShellScript and RunPowerShellScript.

Try this yourself before checking the solution.

## Cleanup

When you're done, delete the resource group to remove all resources:

```
az group delete -y --no-wait -n labs-vm-config
```

This removes everything: the VMs, disks, network interfaces, NSGs, and public IP addresses.
