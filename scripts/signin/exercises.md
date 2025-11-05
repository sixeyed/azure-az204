# Azure Signin - Exercises

## Exercise 1: Exploring the Azure Portal

Let's start by exploring the Azure Portal, which is the web-based interface for Azure.

**Step 1: Sign In**

Open your browser and navigate to portal.azure.com. Sign in with your Microsoft account. You'll be prompted to enter your email address and password.

**Step 2: Explore All Services**

Once you're signed in, click on "All services" in the left navigation menu. This view shows you everything available in Azure. Take a moment to scroll through - there are hundreds of services available, organized by category.

**Step 3: View Your Subscriptions**

In the All Services view, search for "Subscriptions" and click on it. Here you'll see all the Azure Subscriptions you have access to. Each Subscription has a name, a unique ID, and shows its status.

For example, you might see a Subscription named "MY-SUBSCRIPTION" with an ID that looks like "12345678-1234-1234-1234-123456789abc".

**Step 4: Explore Virtual Machines**

Navigate to the Virtual Machines service. Click the "Create" button to see what's involved in creating a new Windows VM. Notice all the configuration options you need to specify:
- Resource group
- Virtual machine name
- Region and availability options
- Image (operating system)
- Size (CPU and memory)
- Authentication method
- Networking settings
- And many more...

Don't actually create the VM - just explore the interface to understand what's required.

**Step 5: Quickstart Center**

Return to the Azure Home page and find the Quickstart Center. Browse to the reference architecture for Azure Web Apps. Notice how it shows common patterns and best practices for deploying web applications.

**Key Takeaway**

The Portal is excellent for browsing services and exploring resources. However, it doesn't provide a repeatable, automatable experience. For that, we need the command line.

## Exercise 2: Using the Azure CLI

The Azure CLI, accessed through the "az" command, is a powerful tool for managing Azure resources. Let's see why it's the recommended approach for developers.

**Step 1: Check CLI Version**

First, run the "az" command by itself to see the integrated help system. You'll see a list of all available command groups.

Before we proceed, let's make sure you have the latest version:

```
az upgrade
```

This will check for updates and upgrade your CLI if needed.

**Step 2: Login to Azure**

Now authenticate with Azure:

```
az login
```

This will open a browser window for you to sign in. After authenticating, you'll see your account information displayed in the terminal.

**Step 3: List Your Accounts**

Let's use the command line to list all the accounts and Subscriptions you have access to:

```
az account list
```

By default, this shows the output in JSON format. You'll see information like:
- Subscription name
- Subscription ID
- Cloud name (usually "AzureCloud")
- Your user credentials
- Tenant ID

**Step 4: Explore Output Formats**

One of the powerful features of the Azure CLI is the ability to change output formats. Try these commands:

```
az account list -o table
```

This displays the information in a clean, human-readable table format.

```
az account list -o yaml
```

This shows the same data in YAML format.

```
az account list -o tsv
```

This outputs tab-separated values, which is useful for scripting.

**Key Advantages of the Azure CLI:**
- Always up-to-date with the latest Azure features
- Integrated help system (try "az vm -h" for example)
- Can be used in scripts and CI/CD pipelines
- Cross-platform (Windows, Linux, macOS)
- Provides consistent, repeatable operations

The CloudName field you see in the output indicates which Azure cloud environment you're connected to. Most users will see "AzureCloud", which is the public Azure cloud.

## Exercise 3: The Azure Cloud Shell

Sometimes you need to use Azure tools but can't install the CLI locally. That's where the Azure Cloud Shell comes in.

**Step 1: Access Cloud Shell**

Navigate to shell.azure.com in your browser. You'll be prompted to choose between PowerShell and Bash for your terminal environment. Either works, but we'll use Bash for this exercise.

**Step 2: First-Time Setup**

If this is your first time using Cloud Shell, you'll be prompted to create storage. Cloud Shell uses Azure Storage to persist your files and command history across sessions. Click through the setup process to create the storage.

**Step 3: You're Already Authenticated**

Notice that you're already signed in to Azure. Try running:

```
az account list -o tsv
```

You'll see your Subscriptions listed in tab-separated format. There was no "az login" required because you authenticated when you signed in to the Portal.

**Step 4: Explore Pre-installed Tools**

The Cloud Shell comes with many tools pre-installed. Try these commands to see what's available:

```
dotnet --version
```

```
python --version
```

```
git --version
```

All of these tools are ready to use without any installation.

## Lab Exercise: Running C# in Cloud Shell

Here's a practical exercise to demonstrate what you can do with Cloud Shell.

**Scenario:** You have a C# program file called Program.cs that you want to run in the cloud without setting up a local development environment.

**Step 1: Create a New Console Project**

In the Cloud Shell, create a new .NET console application:

```
dotnet new console -n MyApp
cd MyApp
```

This creates a new console project in a directory called "MyApp".

**Step 2: Upload Your Code**

Click the "Upload/Download files" button in the Cloud Shell toolbar and upload your Program.cs file. Place it in the MyApp directory, replacing the existing Program.cs.

**Step 3: Run the Program**

Now run your application:

```
dotnet run
```

You'll see the output of your program displayed in the terminal.

**Key Takeaway**

The Cloud Shell provides a fully-configured development environment in your browser. It's perfect for quick tasks, demos, or working from a computer where you can't install tools locally.

## Summary

You've now experienced all three methods of accessing Azure:
- The Portal for visual exploration
- The CLI for powerful, scriptable management
- The Cloud Shell for browser-based access with pre-installed tools

Each method has its place in your Azure toolkit. As you progress through this course, you'll primarily use the Azure CLI because it provides the repeatable, automatable approach that's essential for professional cloud development.
