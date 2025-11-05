# ARM Templates with Bicep - Exercises Narration Script

## Exercise 1: Deploying Your First Bicep Template

Let's start by deploying a simple Bicep template. We'll create a storage account using a pre-built Bicep file.

First, we need to create a resource group. We're calling this resource group "labs-arm-bicep" and placing it in the West Europe region with our standard courselabs tag for tracking.

Now we have our resource group ready. Next, we'll deploy the storage account using the Bicep file located in the storage-account folder. We're using the deployment group create command to deploy to our resource group, specifying the template file path to the main.bicep file.

Notice what happens here. The CLI prompts us for parameter values because the template has required parameters without default values. We need to provide a unique storage account name. This interactive prompting ensures you don't accidentally deploy resources without proper configuration.

Alternatively, we can supply the parameters directly in the command line. We're using the same deployment command but adding the --parameters flag with the storage account name value. This is more suitable for automation since it doesn't require interactive input.

The output from this deployment command is exactly the same whether we're deploying JSON or Bicep templates. Azure processes them identically because Bicep is transpiled to ARM JSON before deployment.

## Exercise 2: Using What-If Analysis

One powerful feature available with both ARM and Bicep is the what-if capability. This lets you preview changes before actually applying them.

Let's run the same deployment again, but this time with a different SKU parameter and the what-if flag. We're deploying the same template but changing the storage SKU to Standard GRS for geo-redundant storage, and adding the --what-if flag.

Watching the output carefully, it shows you exactly what would change if you applied this deployment. You'll see it comparing your template to the existing resources and highlighting the differences. This is invaluable for avoiding surprises in production environments - you can see exactly what will change before making any actual modifications.

## Exercise 3: Installing and Using Bicep Tools

Now let's explore the Bicep tooling. We can install the Bicep CLI directly from the Azure CLI using the bicep install command. This downloads and configures the Bicep compiler on your machine.

Once installed, we can access the Bicep commands using the bicep help command to see all available operations.

The Bicep tools give us the ability to convert between JSON and Bicep formats. This is particularly useful when working with legacy ARM templates that were written in JSON, or when you need to migrate existing infrastructure code to the more readable Bicep syntax.

## Exercise 4: Decompiling JSON to Bicep

We have a complex ARM template for a Linux virtual machine that's written in JSON. All the resources - the VM itself, the network interface, the virtual network, the public IP, the disk - are defined in JSON format which can be verbose and hard to read.

Let's convert this to Bicep using the decompile command. We're using bicep decompile with the file parameter pointing to the azuredeploy.json template.

This generates a new file called azuredeploy.bicep in the same directory. Opening this file, notice several things that make it easier to work with.

First, there are parameters defined for the VM name, password, and other configuration options - these are clearly declared at the top of the file.

Second, every resource the VM needs is modeled - the virtual network, the network interface, the disk, and the VM itself - but they're much more readable than the JSON equivalents.

Third, resources reference each other by name, not by complex resource ID strings. Instead of concatenating strings to build resource IDs, you can simply reference the network interface by its symbolic name. This makes the relationships much clearer and reduces errors.

Let's validate that the generated Bicep file works correctly using a what-if deployment. We're running the deployment with the what-if flag, providing parameters for the admin username and password.

You'll see output showing all the resources that would be created - the virtual network, subnet, public IP, network interface, and the VM. You might also see some warnings about the generated template - these are common when decompiling from JSON because the decompiler has to make assumptions about how the template was structured.

## Exercise 5: Editing and Deploying Bicep Templates

Now let's make some improvements. The generated Bicep file might have warnings we should fix, and we want to customize the network interface to use a specific static IP address instead of dynamic allocation.

We'll edit the Bicep file to fix any warnings from the decompilation process and update the network interface configuration. We're finding the network interface resource definition and changing the private IP allocation method from Dynamic to Static, then specifying the exact IP address we want - 10.1.0.103 in this case.

Once we've made these changes, we can deploy the template using the deployment group create command with our updated Bicep file, providing the admin username and password parameters.

Notice how much easier it is to navigate and edit the Bicep file compared to the original JSON template. This is one of Bicep's major advantages - maintainability. You can quickly find and modify resources without getting lost in nested JSON objects and string concatenations.

## Exercise 6: Evolving Infrastructure Specifications

Bicep templates typically describe all the resources in a resource group. Let's look at how we can evolve our infrastructure over time.

The default deployment mode for ARM is incremental, which means new resources in the template get added, existing resources that match the template are left as they are, and extra resources in the resource group not described in the template remain untouched. This is different from complete mode which would delete anything not in the template.

We have a new Bicep template that adds a SQL Server and database to our existing Linux VM deployment. The template includes both the original VM resources and the new SQL resources all in one file.

Let's preview what this deployment would do using what-if. We're deploying the combined template with parameters for both the VM and the SQL server, using the --what-if flag to see the changes.

Watching the output, you'll see it plans to add three new resources - the SQL Server, the database, and related components - while making no changes to the existing VM infrastructure. The VM resources match what's already deployed, so they're ignored. This is incremental deployment in action.

## Understanding Incremental Deployment

This incremental deployment model is powerful. It means you can safely evolve your infrastructure specifications over time. You don't have to redeploy everything from scratch when adding new components - you just update your template with the new resources and Azure figures out what needs to change.

This makes Bicep ideal for continuous infrastructure development, where your requirements grow and change over time. You maintain one template that represents your complete infrastructure, and each deployment brings the actual resources in sync with your desired state.

## Conclusion

We've covered the core workflows with Bicep: deploying templates with parameters, using what-if analysis to preview changes safely, converting between JSON and Bicep formats for migration, editing Bicep files with a more maintainable syntax, and evolving infrastructure incrementally without disruption.

In the lab exercise, you'll get to practice parameterizing Bicep templates to make them more flexible and reusable across different environments.
