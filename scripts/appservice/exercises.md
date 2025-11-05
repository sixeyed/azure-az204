# App Service for Web Apps - Exercises

## Exercise 1: Exploring App Service in the Portal

Let's start by exploring what App Service offers through the Azure Portal.

Open the Azure Portal and click on "Create a resource." In the search box, type "Web App" and select it. This is one of the App Service types Azure offers.

Take a moment to look at the creation form. Notice that creating a web app requires:
- A Resource Group to organize your resources
- An App Service Plan, which is the compute resources that will run your app
- Publishing options: you can deploy from source code, Docker containers, or static web content
- Runtime stack selection: depending on whether you choose source code, you can select from various runtime stacks and operating systems - for example, Java on Linux or .NET on Windows

This gives you a lot of flexibility in how you deploy and run your applications.

Now, as usual, we won't actually create the resources from the Portal. Instead, we'll use the Azure CLI for better repeatability and automation. Go ahead and cancel out of this creation wizard.

## Exercise 2: Creating an App Service Plan

Let's switch to the command line. First, we'll create a Resource Group for this lab.

Run this command:
```bash
az group create -n labs-appservice -l westeurope --tags courselabs=azure
```

This creates our resource group in the West Europe region with a tag to help us track resources from this course.

Before we can create a web app, we need an App Service Plan. Think of the App Service Plan as an abstraction of the infrastructure needed to run your applications. It defines the region, compute resources, and pricing tier.

Let's create an App Service Plan with the basic B1 SKU and two worker instances:

```bash
az appservice plan create -g labs-appservice -n app-service-01 --sku B1 --number-of-workers 2
```

The B1 SKU is a basic tier that's good for development and testing. The two worker instances will allow our app to run on multiple servers for some redundancy.

Now, go back to the Portal and open the labs-appservice resource group. You'll see the App Service Plan is the only resource. Open it and notice the empty applications list. You can also see the scale up and scale out options, though these are limited by the SKU we selected.

## Exercise 3: Checking Available Runtimes

Before creating our web app, let's see what runtime environments are available. Run this command:

```bash
az webapp list-runtimes
```

You'll see a comprehensive list of supported platforms. Under the Windows options, you'll find ASP.NET 4.8. This runtime is perfect for older .NET applications and is an excellent choice for migrating legacy applications to the cloud - provided you have the source code and don't need the low-level control you'd get with IaaS.

## Exercise 4: Creating a Web App for Git Deployment

Now let's create our web app. We'll configure it to use the ASP.NET 4.8 runtime and set it up for deployment from a local Git repository.

Run this command, replacing the placeholder with a globally unique DNS name:

```bash
az webapp create -g labs-appservice --plan app-service-01 --runtime 'ASPNET:V4.8' --deployment-local-git --name <YOUR-APP-NAME>
```

The app name needs to be globally unique because it will become part of your public URL: https://your-app-name.azurewebsites.net

Once the command completes, go back to the Portal and refresh your resource group. Now you'll see the web app listed as a separate resource with the type "App Service." Notice that you can navigate between the app and the plan - they're separate resources but linked together.

Open the web app resource. You'll see it has a public URL using the application name you specified. Also notice that HTTPS is provided automatically by the platform - no certificate management required.

Click on the URL to browse to your application. You'll see a default landing page that says "Your web app is running and waiting for your content." Our app is live, but we haven't deployed any code yet.

## Exercise 5: Configuring Deployment Settings

Deploying to App Service from a local Git repository is as simple as running git push, but we need to configure a few things first.

We need to tell Azure which branch to deploy from and where our application code is located within the repository. We do this using application settings:

```bash
az webapp config appsettings set --settings DEPLOYMENT_BRANCH='main' -g labs-appservice -n <YOUR-APP-NAME>
```

This tells Azure to use the main branch for deployment.

Next, we need to specify the path to our project file:

```bash
az webapp config appsettings set --settings PROJECT='src/WebForms/WebApp/WebApp.csproj' -g labs-appservice -n <YOUR-APP-NAME>
```

This points Azure to the specific project file it should build and deploy.

## Exercise 6: Setting Up Git Remote

Here's how the deployment works: the web app acts as a Git server. You'll add it as a remote repository and push your code. Whenever code is pushed, Azure automatically compiles it and configures the web app to run it.

First, we need to get the publishing credentials. Run this command:

```bash
az webapp deployment list-publishing-credentials --query scmUri -g labs-appservice -o tsv -n <YOUR-APP-NAME>
```

This will output a URL that looks something like:
```
https://<USERNAME>:<PASSWORD>@<YOUR-APP-NAME>.scm.azurewebsites.net/<YOUR-APP-NAME>.git
```

Notice that the credentials are embedded directly in the URL. This is convenient but not ideal for security. For production scenarios, you'd want to use alternative authentication methods, but this approach works fine for our lab.

Now add this URL as a Git remote. Make sure to use single quotes because the username contains a dollar sign:

```bash
git remote add webapp '<GIT-REMOTE-URL>'
```

Verify that the remote was saved correctly:

```bash
git remote -v
```

You should see your new webapp remote listed along with any other remotes you have configured.

## Exercise 7: Deploying the Application

Now for the exciting part - deploying the application. Simply push your local repository to the webapp remote:

```bash
git push webapp main
```

Watch the output carefully. You'll see the usual Git messages about compressing and writing objects, but then you'll see much more. The remote Git server generates a deployment script automatically, and you'll see MSBuild output as your .NET application is being compiled in real-time.

This is all happening automatically - Azure is detecting that you're pushing a .NET project, compiling it, and deploying the binaries to your web app.

When the git push completes, your application has been compiled and deployed.

## Exercise 8: Verifying the Deployment

Go back to your browser and refresh the URL for your web app. Instead of the landing page, you should now see a standard ASP.NET homepage. It's a simple application, but think about what we just accomplished - we deployed a compiled .NET application from source code with no virtual machines, no build servers, no deployment pipelines. The entire process took just a few minutes.

## Exercise 9: Exploring the Runtime Environment

Even though there's no VM where you can SSH in to diagnose issues, the Portal provides excellent tools to help you understand your runtime environment.

Open the web app blade in the Portal and navigate to the Console option. This connects you to a terminal session running in the web app host.

Let's explore the filesystem. Run these commands:

```cmd
dir
```

You'll see the root directory structure that was created by the deployment script.

Now look at the bin directory:

```cmd
dir bin
```

Here you'll find all the compiled assemblies for your application.

List the environment variables:

```cmd
set
```

You'll see numerous App Service-specific environment variables that your application can use. These include things like the website name, resource group, subscription ID, and many platform-specific settings.

## Lab Challenge

Now it's your turn. The web app we deployed is pretty basic. Your challenge is to:

1. Make a change to the content of the home page
2. Redeploy the application
3. Measure how long it takes for your update to appear

This will help you understand the deployment workflow and timing for updates.

Hint: You'll need to modify the source code, commit the change, and push again to the webapp remote.

## Cleanup

When you're finished with the lab, clean up your resources to avoid unnecessary charges:

```bash
az group delete -y -n labs-appservice
```

This will delete the resource group and all resources within it.

## Summary

In this lab, you've learned how to:
- Create an App Service Plan to host web applications
- Deploy a web app from source code using Git
- Configure application settings
- Explore the runtime environment
- Update and redeploy an application

App Service is a powerful platform that handles all the infrastructure complexity, letting you focus on building and deploying your applications.
