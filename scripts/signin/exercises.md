# Azure Signin - Exercises

## Exploring the Azure Portal

Let's start by exploring the Azure Portal, which is the web-based interface for Azure.

**Step 1: Sign In**

Open your browser and navigate to portal.azure.com. Sign in with your Microsoft account. You'll be prompted to enter your email address and password through Microsoft's authentication flow.

**Step 2: Explore All Services**

Once you're signed in, click on "All services" in the left navigation menu. This view shows you everything available in Azure - the complete catalog of services. Take a moment to scroll through - there are hundreds of services available, organized by category such as Compute, Networking, Storage, Databases, and many more. Each category expands to show the specific services within it.

**Step 3: View Your Subscriptions**

In the All Services view, search for "Subscriptions" in the filter box and click on it when it appears. Here you'll see all the Azure Subscriptions you have access to. Each Subscription has a name that you or your organization set, a unique ID which is a GUID that Azure uses to identify the subscription internally, and shows its status which should typically be "Active" for subscriptions you can use.

For example, you might see a Subscription named "MY-SUBSCRIPTION" with an ID that looks like "12345678-1234-1234-1234-123456789abc". This ID is important for programmatic access and billing tracking.

**Step 4: Explore Virtual Machines**

Navigate to the Virtual Machines service by searching for it in the top search bar. Click the "Create" button to see what's involved in creating a new Windows VM. Notice all the configuration options you need to specify - there's quite a lot. You need to choose or create a resource group which organizes related resources together. You specify a virtual machine name for identification. You select the region and availability options which determine where your VM runs physically and how resilient it is. You choose an image which is the operating system and any pre-installed software. You configure the size which determines CPU cores and memory. You set the authentication method, choosing between password or SSH keys. You configure networking settings like virtual networks and public IP addresses. And there are many more options beyond these basics.

Don't actually create the VM - just explore the interface to understand what's required. Click through the tabs at the top - Basics, Disks, Networking, Management, Monitoring - to see the full scope of configuration.

**Step 5: Quickstart Center**

Return to the Azure Home page by clicking the Azure icon in the top left. Find the Quickstart Center tile or search for it. Browse to the reference architecture for Azure Web Apps. Notice how it shows common patterns and best practices for deploying web applications, including diagrams showing how different services connect together and explanations of why certain architectural decisions make sense.

**Key Takeaway**

The Portal is excellent for browsing services and exploring resources visually. It's great for learning, for ad-hoc investigations, and for one-off tasks. However, it doesn't provide a repeatable, automatable experience. Every time you need to create a resource, you have to click through the same screens. For professional development work and production deployments, we need the command line instead.

## Using the Azure CLI

The Azure CLI, accessed through the "az" command, is a powerful tool for managing Azure resources. Let's see why it's the recommended approach for developers.

**Step 1: Check CLI Version**

First, run the "az" command by itself in your terminal to see the integrated help system. You'll see a list of all available command groups - account, acr, ad, advisor, and many more. Each group contains commands for managing different Azure services.

Before we proceed, let's make sure you have the latest version. Run az upgrade to check for updates and upgrade your CLI if needed. This ensures you have access to the latest features and bug fixes.

**Step 2: Login to Azure**

Now authenticate with Azure using az login. This will open a browser window for you to sign in - it uses the same Microsoft authentication you used for the Portal. Complete the sign-in process by entering your credentials. After authenticating, the browser shows a success message, and you'll see your account information displayed in the terminal including your subscriptions.

**Step 3: List Your Accounts**

Let's use the command line to list all the accounts and Subscriptions you have access to with az account list. By default, this shows the output in JSON format, which is great for programmatic processing. You'll see information like the subscription name identifying the subscription, the subscription ID which is that GUID we saw earlier, the cloud name usually "AzureCloud" for the public Azure cloud but could be different for government or China clouds, your user credentials showing which account you're authenticated with, and the tenant ID identifying your Azure Active Directory tenant.

**Step 4: Explore Output Formats**

One of the powerful features of the Azure CLI is the ability to change output formats to suit different needs. Try these commands to see the same data in different ways.

Run az account list -o table. This displays the information in a clean, human-readable table format with columns nicely aligned. It's much easier to read at a glance than JSON.

Run az account list -o yaml. This shows the same data in YAML format, which some people find more readable than JSON, especially for nested data structures.

Run az account list -o tsv. This outputs tab-separated values, which is useful for scripting. You can easily parse this output with tools like awk or cut, or import it into spreadsheets.

**Key Advantages of the Azure CLI:**

The CLI is always up-to-date with the latest Azure features - often new features are available in the CLI before they appear in the Portal. There's an integrated help system - try running az vm -h for example to see help for virtual machine commands. The CLI can be used in scripts and CI/CD pipelines, enabling automation of your infrastructure. It's cross-platform, working on Windows, Linux, and macOS with the same commands. And it provides consistent, repeatable operations - run the same command, get the same result every time.

The CloudName field you see in the output indicates which Azure cloud environment you're connected to. Most users will see "AzureCloud", which is the public Azure cloud available worldwide. But you might see "AzureUSGovernment" for US government cloud, "AzureChinaCloud" for Azure in China, or other specialized clouds.

## The Azure Cloud Shell

Sometimes you need to use Azure tools but can't install the CLI locally. Maybe you're on a locked-down corporate machine, or you're traveling and using a borrowed computer. That's where the Azure Cloud Shell comes in.

**Step 1: Access Cloud Shell**

Navigate to shell.azure.com in your browser - this gives you access to Cloud Shell directly. You'll be prompted to choose between PowerShell and Bash for your terminal environment. Either works fine, but we'll use Bash for this exercise since it's more universally familiar.

**Step 2: First-Time Setup**

If this is your first time using Cloud Shell, you'll be prompted to create storage. Cloud Shell needs Azure Storage to persist your files and command history across sessions - without this, everything would be lost when you close the browser. Click through the setup process to create the storage. Azure will create a storage account and file share automatically for you. This costs a small amount, typically under a dollar per month.

**Step 3: You're Already Authenticated**

Notice that you're already signed in to Azure - there's no need to run az login. Try running az account list -o tsv right away. You'll see your Subscriptions listed in tab-separated format immediately. There was no "az login" required because you authenticated when you signed in to the Portal to access Cloud Shell. This is one of the major conveniences of Cloud Shell.

**Step 4: Explore Pre-installed Tools**

The Cloud Shell comes with many tools pre-installed, making it a complete development environment. Try these commands to see what's available.

Run dotnet --version to check the .NET SDK version. You'll see it's already installed, typically version 6 or 7.

Run python --version to see Python. Both Python 2 and Python 3 are typically available.

Run git --version to verify Git is installed for source control operations.

Run kubectl version to see Kubernetes command-line tools.

All of these tools are ready to use without any installation or configuration on your part. Microsoft maintains the Cloud Shell environment with commonly used tools, and they're regularly updated.

## Lab Exercise: Running C# in Cloud Shell

Here's a practical exercise to demonstrate what you can do with Cloud Shell - running C# code without any local development environment.

**Scenario:** You have a C# program file called Program.cs that you want to run in the cloud without setting up a local development environment. Maybe you're demonstrating code to someone, or testing something quickly without installing Visual Studio.

**Step 1: Create a New Console Project**

In the Cloud Shell terminal, create a new .NET console application using dotnet new console -n MyApp. This creates a new console project in a directory called "MyApp" with all the necessary files. Then change to that directory with cd MyApp. You now have a complete C# project structure.

**Step 2: Upload Your Code**

Click the "Upload/Download files" button in the Cloud Shell toolbar - it looks like a document with an up arrow. Select "Upload" and choose your Program.cs file from your local machine. Place it in the MyApp directory, replacing the existing Program.cs that was generated. This demonstrates that Cloud Shell can interact with your local filesystem for getting code and files into the cloud environment.

**Step 3: Run the Program**

Now run your application using dotnet run. The .NET SDK compiles your code and executes it right there in the cloud. You'll see the output of your program displayed in the terminal, just as if you were running it locally. This works with any valid C# console application.

**Key Takeaway**

The Cloud Shell provides a fully-configured development environment in your browser. It's perfect for quick tasks when you need to run commands or test code. It's great for demos and teaching when you want to show Azure concepts without local setup complexity. And it's invaluable when working from a computer where you can't install tools locally, like borrowed machines or locked-down corporate workstations.

## Reference

- [Azure documentation](https://docs.microsoft.com/azure/)

## Summary

You've now experienced all three methods of accessing Azure, each with its own strengths and use cases.

The Portal provides visual exploration - it's excellent for browsing services, learning what's available, and understanding resource relationships through its graphical interface. You can see metrics, logs, and resource configurations all in one place.

The CLI offers powerful, scriptable management - it's essential for automation, for defining infrastructure as code, and for repeatable, consistent operations. Commands can be version-controlled, shared with your team, and integrated into CI/CD pipelines.

The Cloud Shell delivers browser-based access with pre-installed tools - it removes the barrier of local installation and configuration, providing a consistent environment that's always available when you have a browser.

Each method has its place in your Azure toolkit. As you progress through this course, you'll primarily use the Azure CLI because it provides the repeatable, automatable approach that's essential for professional cloud development. However, you'll still use the Portal for exploring new services and checking on resources, and you might use Cloud Shell when you need quick access without local tools.

Understanding when to use each tool is part of becoming an effective Azure developer.
