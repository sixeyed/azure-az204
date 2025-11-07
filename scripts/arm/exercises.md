# Azure Resource Manager JSON templates

## Reference

The Azure CLI is a great tool for exploring and automating deployments, but it's an imperative approach. If you use it in scripts, you'll need to add lots of checks to make sure you're not trying to create resources which already exist. The alternative is the declarative approach where you describe what you want the end result to be, and the tooling works out if it needs to create or update resources. Azure Resource Manager templates provide this declarative model, defining desired state rather than deployment steps. Templates can live in source control, be reviewed through standard code review processes, and provide repeatable infrastructure deployment.

## Deploying a Storage Account

Let's start by creating a resource group for our ARM template deployments. We're naming it "labs-arm" with our standard courselabs tag, deploying to East US - though you can use any region that works for you.

Now we're ready to deploy our first ARM template. We'll use the deployment group create command. Let me show you the help text first to understand the available options.

You can see there are many options here. The key ones we need are the deployment name which helps us identify this deployment later, the resource group where resources will be deployed, and the template file which contains our infrastructure definition.

Let's deploy the storage account template. We're supplying the storage account name as a parameter using the --parameters flag. Remember to replace the placeholder with your own unique storage account name - it needs to be globally unique across all of Azure and can only contain lowercase letters and numbers.

While this is deploying, switching over to the Azure Portal and navigating to your labs-arm resource group, you'll see the deployment in progress. You can watch it happening in real-time.

---

## Checking Deployments

Once the deployment completes, let's list all deployments in this resource group using the deployment group list command with table output for easier reading.

You can see our storage-account deployment listed with its provisioning state showing "Succeeded" and a timestamp showing when it completed.

Now here's something powerful - ARM deployments are idempotent and repeatable. Let's see what happens if we run the exact same deployment again, but this time with the what-if flag. We're using the same deployment name, same resource group, same template file, and the same storage account name parameter, but adding --what-if.

Make sure you use the same storage account name you used before.

Looking at the output, it shows the storage account with "no change". The what-if feature compares your template with the actual deployed resources and tells you what would change, without making any actual changes. This is incredibly useful for testing and validation - you can verify your templates before applying them.

---

## Detecting Configuration Drift

One of the most valuable features of ARM templates is detecting configuration drift. Drift happens when someone manually changes a deployed resource, and those changes aren't reflected in your template. This is a common problem in cloud environments.

Let's simulate this. We'll manually change the storage account SKU from Standard LRS to Standard GRS using the storage account update command. This simulates someone making a manual change in the portal or via the CLI.

Remember to use your storage account name.

Now let's run the what-if deployment again with the same parameters - we haven't changed the template, so it still specifies Standard LRS.

Looking at the output now, it shows that the deployment would modify the SKU property, changing it back from Standard GRS to Standard LRS. This is drift detection in action - the template knows what the desired state should be, and it's showing you the difference between actual and desired.

This is extremely valuable for auditing your deployments and ensuring they haven't been manually changed outside of your infrastructure-as-code workflow. You can run what-if periodically to check for drift.

---

## Deploying a Linux VM

Now let's look at a more complex template - one that deploys a Linux virtual machine with all its associated resources: virtual network, subnet, public IP, network security group, network interface, and the VM itself.

Taking a moment to examine the template at the path to azuredeploy.json, you'll see it's much longer than the storage account template, but it follows the same structure: parameters section defining inputs, variables section for computed values, and resources section describing everything to create.

Let's deploy this template. We'll use the parameters file that's included in the folder for most values, but we'll override a couple of values on the command line. We're using the @ symbol to reference the parameters file, then overriding the admin password and DNS prefix with specific values.

Use your own strong password and a unique DNS prefix.

This deployment will take several minutes because it's creating multiple resources - the networking infrastructure, storage, and the virtual machine itself. You can watch the progress in the Portal as each resource is created.

---

## Understanding Dynamic vs Static Values

Once the VM deployment completes, let's run the same command again with the what-if flag to see if it's truly idempotent.

You might expect to see "no change" like we did with the storage account, but looking at the output, it shows that the deployment wants to modify the IP address configuration. Why is this happening?

If you examine the template, you'll find that the network interface has its private IP allocation method set to "Dynamic". This means Azure assigns an IP address from the subnet range, but the template doesn't specify which one. The deployed network interface now has an actual IP address assigned like 10.1.0.4, but the template still just says "Dynamic" - so they don't match exactly.

This makes the template non-idempotent. Dynamic values like this can cause problems when you're trying to maintain infrastructure as code because every what-if shows changes even though nothing is actually wrong.

---

## Lab

In the lab exercise, you'll fix this issue by modifying the template to use a static IP address. This will make the deployment truly repeatable and idempotent - you'll be able to run it multiple times and get "no change" in what-if.

---

## Cleanup

You can delete an ARM deployment with the CLI, but that only deletes the deployment metadata, not the actual resources. To clean up for real we need to delete the Resource Groups.
