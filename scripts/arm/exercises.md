# ARM Templates - Exercises Script

## Exercise 1: Deploying a Storage Account

Let's start by creating a resource group for our ARM template deployments. Run this command:

```
az group create -n labs-arm --tags courselabs=azure --location eastus
```

I'm using eastus as the location, but you can use any region that works for you.

Now we're ready to deploy our first ARM template. We'll use the deployment group create command. Let me show you the help text first:

```
az deployment group create --help
```

You can see there are many options here. The key ones we need are the deployment name, the resource group, and the template file.

Let's deploy the storage account template. I'll supply the storage account name as a parameter:

```
az deployment group create --name storage-account -g labs-arm --template-file labs/arm/storage-account/azuredeploy.json --parameters storageAccountName=mystorageacct2024
```

Replace "mystorageacct2024" with your own unique storage account name - remember, it needs to be globally unique across all of Azure.

While this is deploying, switch over to the Azure Portal and navigate to your labs-arm resource group. You'll see the deployment in progress.

## Exercise 2: Checking Deployments

Once the deployment completes, let's list all deployments in this resource group:

```
az deployment group list -g labs-arm -o table
```

You can see our storage-account deployment listed with its provisioning state and timestamp.

Now here's something powerful - ARM deployments are repeatable. Let's see what happens if we run the exact same deployment again, but this time with the what-if flag:

```
az deployment group create --name storage-account -g labs-arm --template-file labs/arm/storage-account/azuredeploy.json --what-if --parameters storageAccountName=mystorageacct2024
```

Make sure you use the same storage account name you used before.

Look at the output - it shows the storage account with "no change". The what-if feature compares your template with the actual deployed resources and tells you what would change, without making any actual changes. This is incredibly useful for testing and validation.

## Exercise 3: Detecting Configuration Drift

One of the most valuable features of ARM templates is detecting configuration drift. Drift happens when someone manually changes a deployed resource, and those changes aren't reflected in your template.

Let's simulate this. We'll manually change the storage account SKU from Standard_LRS to Standard_GRS:

```
az storage account update -g labs-arm --sku Standard_GRS -n mystorageacct2024
```

Remember to use your storage account name.

Now let's run the what-if deployment again with the same parameters:

```
az deployment group create --name storage-account -g labs-arm --template-file labs/arm/storage-account/azuredeploy.json --what-if --parameters storageAccountName=mystorageacct2024
```

Look at the output now! It shows that the deployment would modify the SKU property, changing it back from Standard_GRS to Standard_LRS. This is drift detection in action - the template knows what the desired state should be, and it's showing you the difference.

This is extremely valuable for auditing your deployments and ensuring they haven't been manually changed outside of your infrastructure-as-code workflow.

## Exercise 4: Deploying a Linux VM

Now let's look at a more complex template - one that deploys a Linux virtual machine with all its associated resources: virtual network, subnet, public IP, network security group, and network interface.

Take a moment to examine the template at labs/arm/vm-simple-linux/azuredeploy.json. It's much longer than the storage account template, but it follows the same structure: parameters, variables, and resources.

Let's deploy this template. We'll use the parameters file that's included in the folder, but we'll override a couple of values:

```
az deployment group create --name vm-simple-linux -g labs-arm --template-file labs/arm/vm-simple-linux/azuredeploy.json --parameters @labs/arm/vm-simple-linux/azuredeploy.parameters.json adminPasswordOrKey='SecureP@ssw0rd123!' dnsLabelPrefix=myvm2024demo
```

Use your own strong password and a unique DNS prefix.

This deployment will take several minutes because it's creating multiple resources. You can watch the progress in the Portal.

## Exercise 5: Understanding Dynamic vs Static Values

Once the VM deployment completes, let's run the same command again with the what-if flag:

```
az deployment group create --name vm-simple-linux -g labs-arm --template-file labs/arm/vm-simple-linux/azuredeploy.json --what-if --parameters @labs/arm/vm-simple-linux/azuredeploy.parameters.json adminPasswordOrKey='SecureP@ssw0rd123!' dnsLabelPrefix=myvm2024demo
```

You might expect to see "no change" like we did with the storage account, but look at the output. It shows that the deployment wants to modify the IP address configuration.

Why is this happening? If you examine the template, you'll find that the network interface has its private IP allocation method set to "Dynamic". This means Azure assigns an IP address from the subnet range, but the template doesn't specify which one. The deployed NIC now has an actual IP address, but the template still just says "Dynamic" - so they don't match.

This makes the template non-idempotent. Dynamic values like this can cause problems when you're trying to maintain infrastructure as code.

## Next Steps

In the lab exercise, you'll fix this issue by modifying the template to use a static IP address. This will make the deployment truly repeatable and idempotent.

After completing the exercises, we'll look at how ARM templates relate to the AZ-204 certification exam.
