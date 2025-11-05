# Resource Groups - Exercises Narration Script

## Exercise 1: Creating a Resource Group in the Portal

Let's start by creating our first Resource Group using the Azure Portal.

I've already opened the Azure Portal and signed in. From the home page, I'll select "Create a Resource" from the Azure services section.

In the search box, I'll type "Resource Group" and select it from the results. Now I'll click "Create" to start the creation process.

For the resource group name, I'll use "labs-rg-1" - that's labs, hyphen, rg, hyphen, 1.

Next, I need to select a region. Notice how the list is organized into "Recommended" regions at the top, and "Others" below. I'll select a region close to my location to minimize latency. For this demonstration, I'm choosing East US.

Now let's add a tag. I'll click on "Next: Tags" and add a tag with the key "courselabs" and the value "azure". Tags like this help us organize and identify resources later.

I'll click "Review + create" and then "Create". Notice the notification that appears - Azure is creating the resource group. This happens quickly since a Resource Group is just a container. And there it is - the resource is ready.

Let me click "Go to resource" to explore the Resource Group. Here you can see all the properties, any resources that would be inside it, and management options like access control, policies, and more.

## Exercise 2: Creating a Resource Group with the Azure CLI

Now let's create a Resource Group using the Azure CLI. This is often faster and more convenient, especially when you're automating tasks.

First, let's explore the available commands. I'll type:

```
az group --help
```

This shows us all the subcommands available for managing Resource Groups - create, delete, list, show, and more.

Let's look at the create command specifically:

```
az group create --help
```

The help text shows us the required parameters. We need a name and a location. The location is referred to as the region in the portal, but in CLI commands, it's called "location" - that's important to remember.

Before we create our Resource Group, let's see what regions are available. The help text actually tells us how to do this:

```
az account list-locations -o table
```

This displays a nice table of all available Azure regions with their display names and actual location names. You can see regions all around the world.

Now let's create our second Resource Group. I'll call it "labs-rg-2" and put it in a different region from the first one. I'll use West US 2 for this example:

```
az group create -n labs-rg-2 -l westus2 --tags courselabs=azure
```

Notice that I'm using the short form of the parameters: "-n" for name and "-l" for location. I'm also adding the same tag we used before.

The command runs and waits until the Resource Group is created, then outputs the details in JSON format. You can see all the properties including the location, provisioning state, and our tags.

## Exercise 3: Managing Resource Groups

Now that we have multiple Resource Groups, let's learn how to manage them.

To list all Resource Groups in your subscription, use the list command:

```
az group list -o table
```

The "-o table" parameter formats the output as a table, which is much easier to read than JSON. You can see all our Resource Groups, their locations, and provisioning states.

Remember those tags we added? Let's use them to filter our results. Azure CLI supports JMESPath queries for filtering. Here's how we can find all Resource Groups with our courselabs tag:

```
az group list -o table --query "[?tags.courselabs=='azure']"
```

This query looks for Resource Groups where the tags object has a courselabs key with the value 'azure'. JMESPath is powerful for filtering and extracting specific data from JSON results.

## Exercise 4: Deleting Resource Groups

Finally, let's talk about deletion. The "group delete" command removes a Resource Group and all resources inside it. This is a powerful operation - you could have an entire application with databases, virtual machines, and storage accounts, and deleting the Resource Group will remove everything.

Because deletion is dangerous, Azure requires explicit confirmation and doesn't allow bulk deletion based on queries. Let's try something that won't work:

```
az group delete --query "[?tags.courselabs=='azure']"
```

As expected, this produces an error saying a group name is required. Azure forces us to delete Resource Groups one at a time to prevent accidental mass deletion.

To delete a specific Resource Group, we provide its name:

```
az group delete -n labs-rg-1
```

Notice that Azure asks for confirmation - I'll type 'y' and press Enter. The command waits until the Resource Group is fully deleted before returning. This ensures that all cleanup is complete.

We can verify the deletion by listing our Resource Groups again:

```
az group list -o table
```

And as you can see, "labs-rg-1" is no longer in the list.

## Conclusion

That covers the basics of working with Resource Groups! You've learned how to create them using both the Portal and CLI, how to list and filter them using tags and queries, and how to delete them safely. These skills form the foundation for managing all your Azure resources effectively.
