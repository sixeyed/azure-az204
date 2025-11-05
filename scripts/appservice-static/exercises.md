# App Service for Static Web Apps - Exercise Walkthrough

## Exercise 1: Create a Static Web App

Let's begin by creating our first Static Web App. Since Static Web Apps deploy from Git repositories, we'll start by forking the course repository on GitHub.

### Fork the Repository

First, we're logging into your GitHub account and navigating to the course repository. Clicking the Fork button creates your own copy. This gives you a repository where you can make changes that will trigger deployments to your Static Web App - you need write access for the automated deployment workflow to work.

Once the fork is complete, we're adding it as a remote to your local Git repository using git remote add with your fork's URL. This allows you to push changes from your local machine.

### Create the Static Web App

Now we'll create a Resource Group and deploy our Static Web App. Let's start with the Resource Group in your chosen location with our standard courselabs tag.

For the Static Web App creation, we're using the staticwebapp create command. Notice that we need to specify the GitHub repository source, the branch to deploy from which is main, and the application location within the repository which points to our HTML files.

We're using the --login-with-github flag which enables interactive authentication. Azure will display a code, and your browser will open asking you to confirm the authorization. This allows Azure to create and manage the GitHub Action workflow file in your repository automatically.

### Explore the Deployment

Opening the Azure Portal and navigating to your Resource Group, notice that unlike a traditional App Service deployment, there's only a single Static Web App resource - no App Service Plan is required. This is one of the advantages of Static Web Apps - simpler resource management and lower costs.

Opening the Static Web App resource, you'll see it has a public URL assigned. Browsing to this URL shows your deployed static site.

Also notice the link to the deployment workflow. Clicking through to GitHub, you'll see Azure has automatically created a GitHub Actions YAML file in your fork at ".github/workflows". This workflow runs automatically whenever you push changes to the main branch - it's continuous deployment out of the box.

## Exercise 2: Push Content Changes

Let's see the continuous deployment in action by making a change to our static content.

### Modify the HTML

We're opening the file at "labs/appservice-static/html/index.html" and making a visible change - perhaps updating the heading text or adding a new paragraph. This change will demonstrate the deployment workflow.

### Deploy the Changes

Now we'll use Git to deploy our changes. First, we're pulling from the fork to get the workflow file that Azure created. Then we're staging your HTML changes using git add, committing with a descriptive message like "Update static web app content", and pushing to your fork.

Switching to GitHub and opening the Actions tab in your fork, you'll see a new workflow run has started automatically. You can drill into the workflow to see the detailed logs showing the build and deployment process - it's using a specialized GitHub Action for Azure Static Web Apps.

Waiting for the workflow to complete, then refreshing your Static Web App URL in the browser, your changes should now be visible. This is the power of continuous deployment - every push to your repository automatically updates your live site without any manual steps.

## Exercise 3: Using Web Apps for Static Content

Static Web Apps are excellent for their simplicity and Git-integrated workflow, but sometimes you need the additional control and management options that come with a traditional App Service. Let's see how to deploy the same static content to an App Service.

### Deploy with webapp up

We're navigating to the directory containing your static HTML content at "labs/appservice-static/html".

Now we're using the webapp up command to create and deploy in one step. We're specifying the resource group, using the --html flag which tells Azure this is static content, using the F1 Free SKU to keep costs minimal, and providing a unique app name.

Watching the output, Azure creates an App Service Plan, creates a Web App, generates a ZIP file from your current directory, and deploys it. All in a single command.

### Explore the Deployment

Browsing to the URL shown in the output, you'll see the same static content, but notice this time it was deployed from your local filesystem - no Git commit or push required. This is useful for quick testing or when you don't want to commit changes yet.

Returning to the Portal and refreshing your Resource Group, now you'll see additional resources: an App Service Plan and an App Service.

Opening the Web App resource and exploring the management options, you have access to the full range of App Service features - configuration settings, scaling options, deployment slots, custom domains, SSL certificates, and much more. Even though this is just static HTML, it's running on a full web server with all the enterprise features.

### Check the Runtime

Let's investigate what's actually serving this content. We're using curl with the -IL flags to examine the HTTP headers without downloading the content.

Looking at the "Server" header in the response, you'll see it's IIS, which means this is running on a Windows server using ASP.NET. This is the default runtime for static content in App Service - Azure chose Windows and IIS automatically when you used the --html flag.

## Exercise 4: Mixed Content with Node.js

Many real-world applications have both static content and dynamic endpoints that require backend processing. Let's deploy a Node.js application that demonstrates this pattern.

### Understand the Application

The application in the "node" folder has two components working together: a static HTML page at "public/index.html" for the user interface, and a dynamic "/user" endpoint in "app.js" that displays authentication details from the server.

### Deploy the Node.js App

First, let's check what Node.js runtimes are available on Windows using the list-runtimes command with the os filter.

We need to find your existing App Service Plan name using the appservice plan list command with table output for easy reading.

Now we're navigating to the node application folder at the relative path from where you are.

We're deploying the application using webapp up. We'll use the existing App Service Plan since it's already provisioned - this is more efficient than creating a new plan. We're specifying the Node 16 LTS runtime, Windows as the operating system to match our existing plan, the plan name, and a unique app name.

It's important to match the OS type with your existing plan. Since our plan is Windows-based from the previous exercise, we specify Windows and the Windows Node runtime. Mixing OS types on the same plan won't work.

### Verify the Deployment

Checking the Portal, you'll see a new App Service has been created, but it's using the same App Service Plan as your previous web app. This is an efficient use of resources - both apps share the underlying infrastructure but remain isolated.

Browsing to the new app's URL, you should see the static HTML page load successfully. Now trying the "/user" endpoint, you'll notice the authentication details show as "undefined" because we haven't configured an identity provider yet. The page renders, but the dynamic content is empty.

### Resource Efficiency

This is a good time to explore the resources in the Portal. Looking at the App Service Plan, it shows multiple apps running on the same plan. Finding the instance details for each app, you can see whether they're running on the same machine or different machines within the plan. This demonstrates how App Service Plans allow you to host multiple applications on shared infrastructure, optimizing costs while maintaining isolation.

## Lab Challenge: Configure Authentication

Your final challenge is to configure authentication for the Node.js application. The code is already written to display authentication details - it just needs an identity provider configured.

Your task has several steps: Opening the Node.js Web App in the Portal, navigating to the Authentication settings, adding an identity provider where the application expects Azure AD authentication, configuring the provider appropriately with the right permissions and settings, testing by browsing to the app where you should be prompted to log in, and verifying that after authentication, the "/user" endpoint displays your user details including your name and email.

This demonstrates how App Service integrates with Azure AD and other identity providers to add authentication to your applications without modifying code - it's all handled by the platform through a feature called Easy Auth.

## Summary

In this lab, you've explored multiple approaches to hosting web content in Azure.

**Static Web Apps** provide streamlined, Git-integrated deployment of static content with automatic CI/CD through GitHub Actions, global distribution, and a simple pricing model. They're perfect for SPAs and static sites.

**App Service with static content** gives you more control and management options - you get deployment slots, scaling controls, VNet integration, and all the enterprise features, but at a higher complexity and cost.

**App Service with Node.js** supports mixed static and dynamic content with authentication, allowing you to build full applications with both frontend and backend in a single hosting environment.

Each approach has its place, and understanding when to use each one is key to effective Azure development.
