# IaaS Bicep - Exercises Narration Script

## Exercise 1: Understanding the Bicep Structure

Let's start by examining how our Bicep templates are organized. Open the templates folder and you'll see we have a modular structure.

First, there's a variables file - it's actually just JSON, not Bicep. This file defines the names of all our resources in one place. This is a great pattern because if you need to change naming conventions, you only need to edit this one file.

Now let's look at the core Bicep file. Notice how it loads that JSON variables file using the `loadJsonContent` function. This is how we share resource names between different Bicep files.

There are a few interesting things to notice here:

The location parameter has a default value that uses `resourceGroup().location`. This means if we don't specify a location, it automatically uses whatever region our resource group is in. That's a nice touch for flexibility.

All the resource names come from the variables file - keeping the template clean and maintainable.

And notice how the subnet is defined. It's not nested inside the virtual network definition, even though it's a child resource. Instead, we use the `parent` property to specify the relationship. This keeps the file much more readable.

## Exercise 2: Deploying Core Resources

Let's deploy these core networking resources. First, we'll create a resource group.

```
az group create -n labs-iaas-bicep --tags courselabs=azure -l eastus
```

Now we'll deploy the core Bicep template to that resource group.

```
az deployment group create -g labs-iaas-bicep --name core --template-file labs/iaas-bicep/templates/core.bicep
```

Watch the deployment progress. Bicep is deploying our virtual network, subnet, and network security group.

Once it's complete, let's verify what was created.

```
az resource list -g labs-iaas-bicep -o table
```

You'll see the NSG and the virtual network listed here. Notice the subnet isn't shown - that's because it's a child resource of the virtual network, so it doesn't appear at the top level.

## Exercise 3: SQL Server Deployment

Now let's look at the SQL Server Bicep template. This is our second modular file, and it demonstrates some important concepts.

Notice the SQL Server name parameter uses the `uniqueString` function. This generates a unique DNS-safe name based on the subscription ID and resource group name. This guarantees we won't have naming conflicts.

The admin password parameter has the `@secure()` decorator. This is critical - it tells ARM that this is sensitive data that shouldn't be logged or displayed in deployment history.

And here's something interesting - the SQL Server is created in the subnet that was defined in the core Bicep file. It references that resource using the `existing` keyword. This is how you reference resources across different Bicep files.

Now, before we deploy, we need to talk about deployment modes. There are two modes: complete and incremental.

Complete mode means your template contains the full definition of all resources. Anything not in the template gets deleted. That's dangerous when we're working with multiple templates.

Let's see what would happen with complete mode. We'll use the `what-if` flag.

```
az deployment group create -g labs-iaas-bicep --name sql --template-file labs/iaas-bicep/templates/sql.bicep --mode complete --what-if --parameters sqlAdminPassword=SecurePassword123!
```

Look at that - ARM says it would delete the virtual network because it's not in this template. That's not what we want.

So we'll use incremental mode instead. This adds our SQL resources to the existing deployment.

```
az deployment group create -g labs-iaas-bicep --name sql --template-file labs/iaas-bicep/templates/sql.bicep --mode incremental --parameters sqlAdminPassword=SecurePassword123!
```

Perfect. Now let's check our resources again.

```
az resource list -g labs-iaas-bicep -o table
```

Great - all our core networking resources are still there, and now we have the SQL Server added.

The SQL Server has a virtual network rule configured. This is a firewall setting that allows access from resources in the same VNet. Let's verify that's in place.

```
az sql server vnet-rule list -g labs-iaas-bicep --server <your-sql-server-name>
```

Perfect. Our database tier is ready.

## Exercise 4: Windows VM and Application Deployment

Now for the finale - the VM Bicep template. This is where it all comes together.

This template defines the Windows Server VM and all the resources it needs - the network interface card, the public IP address, and it references the virtual network from our core resources.

But here's the really powerful part - look at the custom script extension resource. This is configured to run a PowerShell script after the VM is created. Open the vm-setup script in the scripts folder, and you'll see it installs IIS, downloads the application, configures it, and sets up the database connection.

All of this happens automatically. We define it once in our Bicep template, and every deployment is identical.

Let's run a what-if first to make sure we're not about to do anything unexpected.

```
az deployment group create --what-if -g labs-iaas-bicep --name vm --template-file labs/iaas-bicep/templates/vm.bicep --mode incremental --parameters adminPassword=SecureVMPassword123! sqlPassword=SecurePassword123!
```

Looks good. Now let's deploy for real.

```
az deployment group create -g labs-iaas-bicep --name vm --template-file labs/iaas-bicep/templates/vm.bicep --mode incremental --parameters adminPassword=SecureVMPassword123! sqlPassword=SecurePassword123!
```

This will take a few minutes because we're creating the VM and then running the setup script.

While we're waiting, think about what's happening. Azure is provisioning the VM, installing Windows Server, then automatically running our PowerShell script that installs IIS, deploys the .NET application, configures the database connection, and starts everything up.

All with a single command.

Let's verify the VM is created.

```
az vm list -g labs-iaas-bicep -o table
```

There it is. Now, the setup script writes log entries to a file on the VM. We can use a run-command to read that log file and verify everything worked.

```
az vm run-command invoke --command-id RunPowerShellScript -g labs-iaas-bicep --scripts "cat /vm-setup.log" -n <your-vm-name>
```

Perfect. Everything ran successfully. Now let's test the application. Get the FQDN from your VM output and browse to it.

```
http://<your-vm-fqdn>/signup
```

And there it is - a fully functional web application, running on IIS, connected to SQL Server, all deployed completely automatically.

## What We've Demonstrated

Let's review what we've accomplished:

We've deployed a complete application infrastructure using modular Bicep templates. We split the deployment across three files - core networking, SQL Server, and the application VM.

We used incremental deployment mode to safely add resources without affecting existing infrastructure.

We automated the entire application deployment process using VM custom script extensions.

And we ended up with a repeatable, reliable deployment process that we can run as many times as we need, always getting the same result.

This is the power of Infrastructure as Code with Azure Bicep and IaaS.
