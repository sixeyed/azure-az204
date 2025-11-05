# Resource Groups - Exercises Narration

## Exercise 1: Creating a Resource Group in the Portal

Let's start by creating our first Resource Group using the Azure Portal.

I've already opened the Azure Portal and signed in. From the home page, I'll select "Create a Resource" from the Azure services section.

In the search box, I'm typing "Resource Group" and selecting it from the results. Now I'll click "Create" to start the creation process.

For the resource group name, I'm using "labs-rg-1" - that's labs, hyphen, rg, hyphen, 1. This naming convention helps identify it as a lab resource group.

Next, I need to select a region. Notice how the list is organized into "Recommended" regions at the top, and "Others" below. Azure recommends regions based on your location and subscription settings. I'll select a region close to my location to minimize latency. For this demonstration, I'm choosing East US.

Now let's add a tag. I'm clicking on "Next: Tags" and adding a tag with the key "courselabs" and the value "azure". Tags like this help us organize and identify resources later. You can use tags to track costs, identify environments like production versus development, or mark resources that belong to specific projects.

I'll click "Review + create" and then "Create". Notice the notification that appears - Azure is creating the resource group. This happens quickly since a Resource Group is just a container - there's no actual infrastructure being provisioned yet. And there it is - the resource is ready.

Let me click "Go to resource" to explore the Resource Group. Here you can see all the properties, any resources that would be inside it, and management options like access control, policies, cost analysis, and more. This is your central hub for managing everything within this resource group.

---

## Exercise 2: Creating a Resource Group with the Azure CLI

Now let's create a Resource Group using the Azure CLI. This is often faster and more convenient, especially when you're automating tasks or working with infrastructure as code.

First, let's explore the available commands. I'm running az group --help. This shows us all the subcommands available for managing Resource Groups - create, delete, list, show, update, and more. Each of these commands has its own options and parameters.

Let's look at the create command specifically using az group create --help. The help text shows us the required parameters. We need a name and a location. The location is referred to as the region in the portal, but in CLI commands, it's called "location" - that's important to remember to avoid confusion.

Before we create our Resource Group, let's see what regions are available. The help text actually tells us how to do this. We're running az account list-locations with the -o table flag for table output.

This displays a nice table of all available Azure regions with their display names and actual location names. You can see regions all around the world - from East US to West Europe to Australia East and beyond. The display name is human-friendly, but the location name is what you use in CLI commands.

Now let's create our second Resource Group. I'll call it "labs-rg-2" and put it in a different region from the first one. I'll use West US 2 for this example. We're running az group create with -n for name set to labs-rg-2, -l for location set to westus2, and --tags set to courselabs equals azure.

Notice that I'm using the short form of the parameters: "-n" for name and "-l" for location. The Azure CLI supports both short and long parameter names for convenience. I'm also adding the same tag we used before - this consistency makes it easier to find and manage related resources.

The command runs and waits until the Resource Group is created, then outputs the details in JSON format. You can see all the properties including the location, provisioning state which shows "Succeeded", our tags, and the unique resource ID. This JSON output is useful for scripting and automation.

---

## Exercise 3: Managing Resource Groups

Now that we have multiple Resource Groups, let's learn how to manage them.

To list all Resource Groups in your subscription, we're using the list command with az group list and -o table for table formatting.

The "-o table" parameter formats the output as a table, which is much easier to read than JSON for human consumption. You can see all our Resource Groups, their locations, and provisioning states. This gives you a quick overview of all the containers in your subscription.

Remember those tags we added? Let's use them to filter our results. Azure CLI supports JMESPath queries for filtering JSON results. Here's how we can find all Resource Groups with our courselabs tag.

We're running az group list with -o table and --query parameter set to a JMESPath expression. The query "[?tags.courselabs=='azure']" looks for Resource Groups where the tags object has a courselabs key with the value 'azure'. The question mark indicates a filter, and we're checking the tags.courselabs property.

JMESPath is powerful for filtering and extracting specific data from JSON results. You can use it to create complex queries that filter, transform, and project exactly the data you need.

---

## Exercise 4: Deleting Resource Groups

Finally, let's talk about deletion. The "group delete" command removes a Resource Group and all resources inside it. This is a powerful operation - you could have an entire application with databases, virtual machines, storage accounts, and networking components, and deleting the Resource Group will remove everything in one operation.

Because deletion is dangerous, Azure requires explicit confirmation and doesn't allow bulk deletion based on queries. Let's try something that won't work to understand the safety mechanisms.

We're trying az group delete with a query parameter. As expected, this produces an error saying a group name is required. Azure forces us to delete Resource Groups one at a time to prevent accidental mass deletion. You can't accidentally delete multiple resource groups with a single command - this is by design.

To delete a specific Resource Group, we provide its name using az group delete with -n set to labs-rg-1.

Notice that Azure asks for confirmation - "Are you sure you want to perform this operation?". I'll type 'y' and press Enter. The command waits until the Resource Group is fully deleted before returning. This ensures that all cleanup is complete - all resources have been removed, all dependencies have been cleared, and everything is cleaned up properly.

We can verify the deletion by listing our Resource Groups again using az group list with -o table.

And as you can see, "labs-rg-1" is no longer in the list. Only labs-rg-2 remains. The deletion was successful.

---

## Conclusion

That covers the basics of working with Resource Groups! You've learned how to create them using both the Portal and CLI, how to list and filter them using tags and queries, and how to delete them safely. These skills form the foundation for managing all your Azure resources effectively.

Resource Groups are the fundamental organizational unit in Azure. Understanding how to manage them well will make your entire Azure experience more efficient and organized.
