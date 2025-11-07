# App Service for Web Apps

## Reference

IaaS options are great when you need access to the host machine, but they leave you with significant management overhead. Platform-as-a-Service takes care of that complexity for you, simplifying deployment and updates. Azure App Service is the PaaS option you'll use for most web applications, and in this lab you'll deploy an app by pushing source code from your local machine. Azure will compile and configure everything for you.

## Explore App Service

Let's start by exploring what App Service offers through the Azure Portal.

We're opening the Azure Portal and clicking on "Create a resource." In the search box, typing "Web App" and selecting it shows us one of the App Service types Azure offers.

Taking a moment to look at the creation form, notice that creating a web app requires a Resource Group to organize your resources, an App Service Plan which is the compute resources that will run your app, and publishing options where you can deploy from source code, Docker containers, or static web content. The runtime stack selection depends on whether you choose source code - you can select from various runtime stacks and operating systems, for example Java on Linux or .NET on Windows.

This gives you a lot of flexibility in how you deploy and run your applications.

Now, as usual, we won't actually create the resources from the Portal. Instead, we'll use the Azure CLI for better repeatability and automation. We're canceling out of this creation wizard.

## Create an App Service Plan

Let's switch to the command line. First, we'll create a Resource Group for this lab in the West Europe region with our courselabs tag to help us track resources from this course.

Before we can create a web app, we need an App Service Plan. Think of the App Service Plan as an abstraction of the infrastructure needed to run your applications. It defines the region where apps will run, the compute resources available, and the pricing tier that determines features and capacity.

Let's create an App Service Plan with the basic B1 SKU and two worker instances. The B1 SKU is a basic tier that's good for development and testing, providing a balance of features and cost. The two worker instances allow our app to run on multiple servers for some redundancy - if one instance fails, the other keeps serving requests.

Now, going back to the Portal and opening the labs-appservice resource group, you'll see the App Service Plan is the only resource. Opening it, notice the empty applications list. You can also see the scale up and scale out options, though these are limited by the SKU we selected - each tier has different scaling capabilities.

## Create an app for Git deployment

Before creating our web app, let's see what runtime environments are available. We're running the webapp list-runtimes command to display all supported platforms.

You'll see a comprehensive list of supported platforms. Under the Windows options, you'll find ASP.NET 4.8. This runtime is perfect for older .NET applications and is an excellent choice for migrating legacy applications to the cloud - provided you have the source code and don't need the low-level control you'd get with IaaS virtual machines.

Now let's create our web app. We'll configure it to use the ASP.NET 4.8 runtime and set it up for deployment from a local Git repository.

We're creating the web app with the resource group, App Service Plan, ASP.NET version 4.8 runtime, deployment from local git, and a globally unique name. The app name needs to be globally unique because it will become part of your public URL: https://your-app-name.azurewebsites.net.

Once the command completes, going back to the Portal and refreshing your resource group, now you'll see the web app listed as a separate resource with the type "App Service." Notice that you can navigate between the app and the plan - they're separate resources but linked together, similar to how virtual machines and disks are related.

Opening the web app resource, you'll see it has a public URL using the application name you specified. Also notice that HTTPS is provided automatically by the platform - no certificate management required. Azure provisions and manages the SSL certificate for you.

Clicking on the URL to browse to your application, you'll see a default landing page that says "Your web app is running and waiting for your content." Our app is live and accessible on the internet, but we haven't deployed any code yet.

## Deploy the web app

Deploying to App Service from a local Git repository is as simple as running git push, but we need to configure a few things first.

We need to tell Azure which branch to deploy from and where our application code is located within the repository. We do this using application settings with the webapp config appsettings set command. We're setting DEPLOYMENT_BRANCH to 'main' which tells Azure to use the main branch for deployment.

Next, we need to specify the path to our project file. We're setting PROJECT to point to the specific project file at 'src/WebForms/WebApp/WebApp.csproj'. This tells Azure exactly which project to build - important when you have multiple projects in the same repository.

Here's how the deployment works: the web app acts as a Git server. You'll add it as a remote repository and push your code. Whenever code is pushed, Azure automatically compiles it and configures the web app to run it.

First, we need to get the publishing credentials. We're using the deployment list-publishing-credentials command with a query to extract just the SCM URI, outputting as plain text.

This outputs a URL that contains your deployment username and password embedded directly in it. Notice that the credentials are in the URL format. This is convenient but not ideal for security - the username contains special characters like dollar signs, and the password is visible. For production scenarios, you'd want to use alternative authentication methods like service principals or managed identities, but this approach works fine for our lab.

Now we're adding this URL as a Git remote. We're using single quotes because the username contains a dollar sign which would be interpreted by the shell otherwise.

Verifying that the remote was saved correctly using git remote -v, you should see your new webapp remote listed along with any other remotes you have configured like origin.

Now for the exciting part - deploying the application. We're simply pushing your local repository to the webapp remote using git push webapp main.

Watching the output carefully, you'll see the usual Git messages about compressing and writing objects, but then you'll see much more. The remote Git server generates a deployment script automatically, detecting that you're pushing a .NET project. Then you'll see MSBuild output as your application is being compiled in real-time on Azure's build servers.

This is all happening automatically - Azure is detecting that you're pushing a .NET project, setting up the build environment, compiling it with MSBuild, and deploying the compiled binaries to your web app. No build pipelines to configure, no deployment packages to create manually.

When the git push completes, your application has been compiled and deployed.

## Check the build

Going back to your browser and refreshing the URL for your web app, instead of the landing page, you should now see a standard ASP.NET homepage. It's a simple application, but think about what we just accomplished - we deployed a compiled .NET application from source code with no virtual machines to manage, no build servers to configure, no deployment pipelines to set up. The entire process took just a few minutes.

Even though there's no VM where you can SSH in to diagnose issues, the Portal provides excellent tools to help you understand your runtime environment.

Opening the web app blade in the Portal and navigating to the Console option, this connects you to a terminal session running in the web app host - it's a Windows command prompt running in the container that hosts your application.

Let's explore the filesystem. Running "dir" shows you the root directory structure that was created by the deployment script - you can see folders for your application code, logs, and system files.

Now looking at the bin directory with "dir bin", here you'll find all the compiled assemblies for your application - the DLLs that Azure built from your source code.

Listing the environment variables with "set", you'll see numerous App Service-specific environment variables that your application can use. These include things like the website name, resource group, subscription ID, the region it's running in, and many platform-specific settings that applications can read to understand their environment.

---

## Lab

Now it's your turn. The web app we deployed is pretty basic. Your challenge is to make a change to the content of the home page, redeploy the application, and measure how long it takes for your update to appear.

This will help you understand the deployment workflow and timing for updates - from code change to live application.

Hint: You'll need to modify the source code in the WebForms project, commit the change using git add and git commit, and push again to the webapp remote with git push. Time the entire process from push to seeing your change live.

---

## Cleanup

When you're finished with the lab, we're cleaning up your resources to avoid unnecessary charges using the group delete command with the -y flag to skip the confirmation prompt.

This will delete the resource group and all resources within it - the App Service Plan, the Web App, and all their configurations.
