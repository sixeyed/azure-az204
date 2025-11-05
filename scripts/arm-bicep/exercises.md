# ARM Templates with Bicep - Exercises Narration Script

## Exercise 1: Deploying Your First Bicep Template

Let's start by deploying a simple Bicep template. We'll create a storage account using a pre-built Bicep file.

First, we need to create a resource group. I'll call this resource group "labs-arm-bicep" and place it in the West Europe region.

[SHOW COMMAND ON SCREEN]

```
az group create -n labs-arm-bicep --tags courselabs=azure --location westeurope
```

Now we have our resource group ready. Next, we'll deploy the storage account using the Bicep file located in the storage-account folder.

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/storage-account/main.bicep
```

Notice what happens here. The CLI prompts us for parameter values because the template has required parameters without default values. We need to provide a unique storage account name.

Alternatively, we can supply the parameters directly in the command line like this:

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/storage-account/main.bicep --parameters storageAccountName=<your-unique-name>
```

The output from this deployment command is exactly the same whether we're deploying JSON or Bicep templates. Azure processes them identically.

## Exercise 2: Using What-If Analysis

One powerful feature available with both ARM and Bicep is the what-if capability. This lets you preview changes before actually applying them.

Let's run the same deployment again, but this time with a different SKU parameter and the what-if flag:

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/storage-account/main.bicep --what-if --parameters storageSku=Standard_GRS storageAccountName=<your-unique-name>
```

Watch the output carefully. It shows you exactly what would change if you applied this deployment. This is invaluable for avoiding surprises in production environments.

## Exercise 3: Installing and Using Bicep Tools

Now let's explore the Bicep tooling. We can install the Bicep CLI directly from the Azure CLI:

[SHOW COMMAND ON SCREEN]

```
az bicep install
```

Once installed, we can access the Bicep commands:

[SHOW COMMAND ON SCREEN]

```
az bicep --help
```

The Bicep tools give us the ability to convert between JSON and Bicep formats. This is particularly useful when working with legacy ARM templates or when you need to migrate existing infrastructure code.

## Exercise 4: Decompiling JSON to Bicep

We have a complex ARM template for a Linux virtual machine that's written in JSON. All the resources - the VM itself, the network interface, the disk - are defined in JSON format.

Let's convert this to Bicep using the decompile command:

[SHOW COMMAND ON SCREEN]

```
az bicep decompile -f labs/arm-bicep/vm-simple-linux/azuredeploy.json
```

This generates a new file called azuredeploy.bicep in the same directory. Open this file and notice several things:

First, there are parameters defined for the VM name, password, and other configuration options.

Second, every resource the VM needs is modeled - the virtual network, the network interface, the disk, and the VM itself.

Third, resources reference each other by name, not by complex resource ID strings. This makes the relationships much clearer.

Let's validate that the generated Bicep file works correctly using a what-if deployment:

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/vm-simple-linux/azuredeploy.bicep --what-if --parameters adminUsername=linuxuser adminPasswordOrKey=<your-strong-password>
```

You'll see output showing all the resources that would be created. You might also see some warnings about the generated template - these are common when decompiling from JSON.

## Exercise 5: Editing and Deploying Bicep Templates

Now let's make some improvements. The generated Bicep file might have warnings we should fix, and we want to customize the network interface to use a specific static IP address.

We'll edit the Bicep file to:
- Fix any warnings from the decompilation process
- Update the network interface to use the static IP address 10.1.0.103

[SHOW EDITED FILE ON SCREEN]

Once we've made these changes, we can deploy the template:

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/vm-simple-linux/azuredeploy-updated.bicep --parameters adminUsername=linuxuser adminPasswordOrKey=<your-strong-password>
```

Notice how much easier it is to navigate and edit the Bicep file compared to the original JSON template. This is one of Bicep's major advantages - maintainability.

## Exercise 6: Evolving Infrastructure Specifications

Bicep templates typically describe all the resources in a resource group. Let's look at how we can evolve our infrastructure over time.

The default deployment mode for ARM is incremental, which means:
- New resources in the template get added
- Existing resources that match are left as they are
- Extra resources in the resource group not described in the template remain untouched

We have a new Bicep template that adds a SQL Server and database to our existing Linux VM deployment. The template includes both the original VM resources and the new SQL resources.

Let's preview what this deployment would do using what-if:

[SHOW COMMAND ON SCREEN]

```
az deployment group create -g labs-arm-bicep --template-file labs/arm-bicep/vm-and-sql-db/main.bicep --parameters adminUsername=linuxuser adminPasswordOrKey=<your-strong-password> sqlAdminPassword=<your-strong-password> --what-if
```

Watch the output. You'll see it plans to add three new resources - the SQL Server, the database, and related components - while making no changes to the existing VM infrastructure. This is incremental deployment in action.

## Understanding Incremental Deployment

This incremental deployment model is powerful. It means you can safely evolve your infrastructure specifications over time. You don't have to redeploy everything from scratch - you just update your template with the new resources and Azure figures out what needs to change.

This makes Bicep ideal for continuous infrastructure development, where your requirements grow and change over time.

## Conclusion

We've covered the core workflows with Bicep:
- Deploying templates
- Using what-if analysis
- Converting between JSON and Bicep
- Editing Bicep files
- Evolving infrastructure incrementally

In the lab exercise, you'll get to practice parameterizing Bicep templates to make them more flexible and reusable.
