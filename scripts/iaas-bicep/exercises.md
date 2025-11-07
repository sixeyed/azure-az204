# IaaS - Automating App Deployment

## Reference

The IaaS approach doesn't mean you have to manually log in to VMs and deploy applications. You can take advantage of automation with ARM templates or Bicep to model your infrastructure, and include deployment scripts that run automatically. Those scripts can install application dependencies, the application itself, and set up configuration files. This approach provides repeatable, reliable deployments that you can version control and integrate into CI/CD pipelines.

## Core resources

Bicep supports larger infrastructure requirements by letting you split the model across multiple files. You can share variable names between files, which lets you refer to resources defined in different Bicep files.

Let's start by examining how our Bicep templates are organized. Open the templates folder and you'll see we have a modular structure.

First, there's a variables file - it's actually just JSON, not Bicep. This file defines the names of all our resources in one place. This is a great pattern because if you need to change naming conventions, you only need to edit this one file.

Now let's look at the core Bicep file. Notice how it loads that JSON variables file using the loadJsonContent function. This is how we share resource names between different Bicep files.

There are a few interesting things to notice here. The location parameter has a default value that uses resourceGroup dot location. This means if we don't specify a location, it automatically uses whatever region our resource group is in. That's a nice touch for flexibility.

All the resource names come from the variables file - keeping the template clean and maintainable.

And notice how the subnet is defined. It's not nested inside the virtual network definition, even though it's a child resource. Instead, we use the parent property to specify the relationship. This keeps the file much more readable than deeply nested definitions.

Let's deploy these core networking resources. First, we'll create a resource group using the group create command with parameters for the name, location, and tags. We're placing it in the East US region and adding our courselabs equals azure tag.

Now we'll deploy the core Bicep template to that resource group. We're using the deployment group create command, specifying the resource group name, giving the deployment a name of "core", and pointing to our Bicep template file with the template-file parameter.

Watch the deployment progress. Bicep is compiling our template into ARM JSON behind the scenes, then Azure is deploying our virtual network, subnet, and network security group.

Once it's complete, let's verify what was created. We'll use the resource list command with the resource group parameter to see all resources. The table output format gives us a nice view.

You'll see the NSG and the virtual network listed here. Notice the subnet isn't shown - that's because it's a child resource of the virtual network, so it doesn't appear at the top level in resource lists. But it's there, nested inside the virtual network.

---

## SQL Server

Now let's look at the SQL Server Bicep template. This is our second modular file, and it demonstrates some important concepts.

Notice the SQL Server name parameter uses the uniqueString function. This generates a unique DNS-safe name based on the subscription ID and resource group name. The function is deterministic - it will always generate the same result for the same inputs - which guarantees we won't have naming conflicts across Azure while remaining predictable within our subscription.

The admin password parameter has the @secure decorator. This is critical - it tells ARM that this is sensitive data that shouldn't be logged or displayed in deployment history. You'll never see this value in the portal or in deployment outputs.

And here's something interesting - the SQL Server is created in the subnet that was defined in the core Bicep file. It references that resource using the existing keyword. This is how you reference resources across different Bicep files - you declare them as existing resources by their names.

Now, before we deploy, we need to talk about deployment modes. There are two modes: complete and incremental.

Complete mode means your template contains the full definition of all resources. Anything not in the template gets deleted. That's dangerous when we're working with multiple templates.

Let's see what would happen with complete mode. We'll use the what-if flag to simulate the deployment. This shows us what changes would be made without actually making them. We're providing the SQL admin password parameter as well.

Look at that - ARM says it would delete the virtual network because it's not in this template. That's not what we want at all.

So we'll use incremental mode instead. This adds our SQL resources to the existing deployment without touching resources that aren't mentioned in the template. This is almost always what you want when working with multiple Bicep files.

Perfect. Now let's check our resources again with the resource list command.

Great - all our core networking resources are still there, and now we have the SQL Server added.

The SQL Server has a virtual network rule configured. This is a firewall setting that allows access from resources in the same virtual network. Let's verify that's in place using the sql server vnet-rule list command with the resource group and server name parameters.

Perfect. Our database tier is ready.

---

## Windows Application VM

Now for the finale - the VM Bicep template. This is where it all comes together.

This template defines the Windows Server VM and all the resources it needs - the network interface card, the public IP address, and it references the virtual network from our core resources.

But here's the really powerful part - look at the custom script extension resource. This is configured to run a PowerShell script after the VM is created. Open the vm-setup script in the scripts folder, and you'll see it installs IIS, downloads the application, configures it, and sets up the database connection.

All of this happens automatically. We define it once in our Bicep template, and every deployment is identical. This is Infrastructure as Code at its finest - completely reproducible, completely automated deployments.

Let's run a what-if first to make sure we're not about to do anything unexpected. We're providing both the admin password for the VM and the SQL password as parameters.

Looks good - we're creating the VM, network interface, public IP, and the script extension. Nothing is being deleted.

Now let's deploy for real using the deployment group create command with incremental mode.

This will take a few minutes because we're creating the VM and then running the setup script. While we're waiting, think about what's happening. Azure is provisioning the VM, installing Windows Server, then automatically running our PowerShell script that installs IIS, deploys the .NET application, configures the database connection, and starts everything up.

All with a single command. This is the power of Infrastructure as Code.

Let's verify the VM is created using the vm list command with table output.

There it is. Now, the setup script writes log entries to a file on the VM. We can use a run-command to read that log file and verify everything worked. The run-command invoke feature lets us execute PowerShell commands on the VM without logging in via RDP.

Perfect. Everything ran successfully - IIS installed, application deployed, database configured. Now let's test the application. Get the FQDN from your VM output and browse to it with the /signup path.

And there it is - a fully functional web application, running on IIS, connected to SQL Server, all deployed completely automatically using Bicep templates and custom script extensions.

---

## Lab

There are a couple of issues with the VM Bicep file. The first is the warning you get when you deploy - it's not really an issue for us, but we should follow the best practice. Also we had to query the VM and manually build the URL to test. Update the Bicep file to address both of those issues then deploy it again. Does the setup script get run again?

---

## Cleanup

When you're finished with the lab, we're deleting the resource group to remove all resources and stop incurring charges. The delete command uses the -y flag to confirm without prompting, and the --no-wait flag to return immediately while the deletion continues in the background.
