# App Service for Static Web Apps - Exercise Walkthrough

## Exercise 1: Create a Static Web App

Let's begin by creating our first Static Web App. Since Static Web Apps deploy from Git repositories, we'll start by forking the course repository on GitHub.

### Fork the Repository

First, log into your GitHub account and navigate to the course repository. Click the Fork button to create your own copy. This gives you a repository where you can make changes that will trigger deployments to your Static Web App.

Once the fork is complete, add it as a remote to your local Git repository:

```bash
git remote add fork <your-fork-url>
```

### Create the Static Web App

Now we'll create a Resource Group and deploy our Static Web App. Let's start with the Resource Group:

```bash
az group create -n <resource-group> -l <location> --tags courselabs=azure
```

For the Static Web App creation, we'll use the `staticwebapp create` command. Notice that we need to specify:
- The GitHub repository source
- The branch to deploy from (main)
- The application location within the repository

```bash
az staticwebapp create -g <resource-group> --branch main \
  --app-location '/labs/appservice-static/html' \
  --login-with-github \
  -n <app-name> \
  --source <github-fork-url>
```

The `--login-with-github` flag enables interactive authentication. Azure will display a code, and your browser will open asking you to confirm the authorization. This allows Azure to create and manage the GitHub Action workflow file.

### Explore the Deployment

Open the Azure Portal and navigate to your Resource Group. Notice that unlike a traditional App Service deployment, there's only a single Static Web App resource - no App Service Plan is required.

Open the Static Web App resource. You'll see it has a public URL assigned. Browse to this URL to see your deployed static site.

Also notice the link to the deployment workflow. If you click through to GitHub, you'll see Azure has automatically created a GitHub Actions YAML file in your fork. This workflow runs automatically whenever you push changes to the main branch.

## Exercise 2: Push Content Changes

Let's see the continuous deployment in action by making a change to our static content.

### Modify the HTML

Open the `labs/appservice-static/html/index.html` file and make a visible change - perhaps update the heading text or add a new paragraph.

### Deploy the Changes

Now we'll use Git to deploy our changes:

```bash
# First, pull the workflow file that Azure created
git pull fork main

# Stage your changes
git add labs/appservice-static/html/index.html

# Commit with a descriptive message
git commit -m 'Update static web app content'

# Push to your fork
git push fork main
```

Switch to GitHub and open the Actions tab in your fork. You'll see a new workflow run has started automatically. You can drill into the workflow to see the detailed logs showing the build and deployment process.

Wait for the workflow to complete, then refresh your Static Web App URL in the browser. Your changes should now be visible. This is the power of continuous deployment - every push to your repository automatically updates your live site.

## Exercise 3: Using Web Apps for Static Content

Static Web Apps are excellent for their simplicity and Git-integrated workflow, but sometimes you need the additional control and management options that come with a traditional App Service. Let's see how to deploy the same static content to an App Service.

### Deploy with webapp up

Navigate to the directory containing your static HTML content:

```bash
cd labs/appservice-static/html
```

Now use the `webapp up` command to create and deploy in one step:

```bash
az webapp up -g <resource-group> --html --sku F1 -n <unique-app-name>
```

Watch the output - Azure creates an App Service Plan, creates a Web App, generates a ZIP file from your current directory, and deploys it. The `--html` flag tells Azure this is static content, and `--sku F1` specifies the Free tier.

### Explore the Deployment

Browse to the URL shown in the output. You'll see the same static content, but notice this time it was deployed from your local filesystem - no Git commit or push required.

Return to the Portal and refresh your Resource Group. Now you'll see additional resources: an App Service Plan and an App Service.

Open the Web App resource and explore the management options. You have access to the full range of App Service features - configuration settings, scaling options, deployment slots, and much more. Even though this is just static HTML, it's running on a full web server.

### Check the Runtime

Let's investigate what's actually serving this content. Use curl to examine the HTTP headers:

```bash
curl -IL <app-url>
```

Look at the `Server` header in the response. You'll see it's IIS, which means this is running on a Windows server using ASP.NET. This is the default runtime for static content in App Service.

## Exercise 4: Mixed Content with Node.js

Many real-world applications have both static content and dynamic endpoints that require backend processing. Let's deploy a Node.js application that demonstrates this pattern.

### Understand the Application

The application in the `node` folder has two components:
- A static HTML page at `public/index.html`
- A dynamic `/user` endpoint in `app.js` that displays authentication details

### Deploy the Node.js App

First, let's check what Node.js runtimes are available:

```bash
az webapp list-runtimes --os Windows
```

Find your existing App Service Plan name:

```bash
az appservice plan list -g <resource-group> -o table
```

Navigate to the node application folder:

```bash
cd ../node
```

Now deploy the application. We'll use the existing App Service Plan since it's already provisioned:

```bash
az webapp up -g <resource-group> \
  --runtime NODE:16LTS \
  --os-type Windows \
  --plan <plan-name> \
  -n <unique-app-name>
```

It's important to match the OS type with your existing plan. Since our plan is Windows-based, we specify Windows and the Windows Node runtime.

### Verify the Deployment

Check the Portal - you'll see a new App Service has been created, but it's using the same App Service Plan as your previous web app. This is an efficient use of resources.

Browse to the new app's URL. You should see the static HTML page load successfully. Now try the `/user` endpoint. You'll notice the authentication details show as `undefined` because we haven't configured an identity provider yet.

### Resource Efficiency

This is a good time to explore the resources in the Portal. Look at the App Service Plan - it shows multiple apps running on the same plan. Find the instance details for each app. Are they running on the same machine? This demonstrates how App Service Plans allow you to host multiple applications on shared infrastructure.

## Lab Challenge: Configure Authentication

Your final challenge is to configure authentication for the Node.js application. The code is already written to display authentication details - it just needs an identity provider configured.

Your task:
1. Open the Node.js Web App in the Portal
2. Navigate to the Authentication settings
3. Add an identity provider - the application expects Azure AD authentication
4. Configure the provider appropriately
5. Test by browsing to the app - you should be prompted to log in
6. After authentication, the `/user` endpoint should display your user details

This demonstrates how App Service integrates with Azure AD and other identity providers to add authentication to your applications without modifying code.

## Summary

In this lab, you've explored multiple approaches to hosting web content in Azure:

- **Static Web Apps** for streamlined, Git-integrated deployment of static content
- **App Service with static content** for more control and management options
- **App Service with Node.js** for mixed static and dynamic content with authentication

Each approach has its place, and understanding when to use each one is key to effective Azure development.
