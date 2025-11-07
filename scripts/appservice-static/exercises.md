# App Service for Static Web Apps

## Reference

Azure offers multiple approaches for hosting web content, and understanding when to use each one is crucial for effective cloud development. Static Web Apps is a specialized service optimized for hosting static content and Single Page Applications with automatic CI/CD integration through GitHub Actions. The service provides global content distribution, automatic SSL certificates, and simplified deployment workflows that eliminate the need for App Service Plans. The documentation covers everything from basic static hosting to advanced scenarios with serverless API backends. For comparison, traditional App Service provides more control and management options but with additional complexity. The command line interface gives you tools for both approaches through the az staticwebapp and az webapp commands, which we'll be using throughout these exercises.

## Create a Static Web App

Static Web Apps deploy directly from Git repositories, so we'll start by setting up your own copy of the course materials in GitHub.

**Fork the Course Repository**: We're opening GitHub and navigating to the course repository to create a fork. Forking creates your own copy under your GitHub account, which is essential because the Static Web App needs write access to create the deployment workflow file. After clicking the Fork button and confirming, you'll have your own copy of all the course materials that you can modify freely.

**Add the Fork as a Remote**: We're adding your fork as a remote in your local Git repository using git remote add. This allows you to push changes from your local machine to your fork, which will trigger automated deployments to your Static Web App. You'll need the URL of your fork, which should be something like "https://github.com/your-username/azure".

**Create the Resource Group**: We're creating a resource group called "labs-appservice-static" with our standard courselabs tag for tracking resources.

**Deploy the Static Web App**: We're using the staticwebapp create command to deploy. This command requires several parameters - the GitHub repository URL pointing to your fork, the branch to deploy from which is main, and the application location within the repository which points to "/labs/appservice-static/html". We're using the login-with-github flag which triggers interactive authentication - Azure displays a code and opens your browser where you enter that code to authorize access. This authorization allows Azure to create and manage the GitHub Actions workflow file automatically.

**Explore the Deployment**: Opening the Azure Portal and navigating to your resource group, notice there's only a single Static Web App resource - no App Service Plan is required. This simpler resource model is one of the key advantages of Static Web Apps for appropriate scenarios. Opening the Static Web App resource shows you have a public URL assigned automatically. Browsing to this URL displays your deployed static site.

**Examine the GitHub Workflow**: The Static Web App resource includes a link to the deployment workflow in GitHub. Following this link shows a YAML file that Azure created automatically in your fork at ".github/workflows". This GitHub Actions workflow runs every time you push to the main branch, providing continuous deployment without any manual configuration. The workflow uses a specialized Azure action that handles building and deploying your static content.

---

## Push Content Changes

Let's see continuous deployment in action by making changes to our static content and watching them deploy automatically.

**Modify the HTML Content**: We're opening the file at "labs/appservice-static/html/index.html" in your local repository and making a visible change - perhaps updating a heading, adding content, or changing styles. This change will demonstrate the automatic deployment workflow.

**Sync the Workflow File**: Before pushing your changes, we need to pull from the fork to get the workflow file that Azure created. We're using git pull fork main to synchronize your local repository with the workflow file.

**Commit and Push Changes**: We're staging your HTML changes with git add, creating a commit with a descriptive message like "Update static web app content", and pushing to your fork with git push fork main. This push triggers the GitHub Actions workflow automatically.

**Monitor the Deployment**: Opening GitHub and navigating to the Actions tab in your fork shows a new workflow run that started automatically when you pushed. Drilling into the workflow displays detailed logs showing the build and deployment process. The workflow checks out your code, builds the static content, and deploys it to your Static Web App - all without manual intervention.

**Verify the Changes**: Waiting for the workflow to complete, then refreshing your Static Web App URL in the browser shows your changes are now live. This is continuous deployment at work - every push to your repository automatically updates your live site within minutes, with no manual steps or deployment commands required.

---

## Using Web Apps for Static Content

While Static Web Apps are excellent for their simplicity and Git-integrated workflow, traditional App Service provides additional control and management options that some scenarios require.

**Navigate to the Content Directory**: We're changing to the directory containing the static HTML content at "labs/appservice-static/html" so we can deploy from this location.

**Deploy with webapp up**: We're using the webapp up command with the html flag which tells Azure this is static content. We're specifying the resource group, using the F1 Free SKU to minimize costs, and providing a unique app name. Watching the command execute, Azure creates an App Service Plan, creates a Web App, generates a ZIP file from your current directory, and deploys it - all in a single operation.

**Compare the Resource Model**: Browsing to the URL shown in the output displays the same static content, but this time it was deployed from your local filesystem without requiring a Git commit or push. This is useful for rapid testing or when you don't want to commit changes yet. Opening the Portal and refreshing your resource group now shows additional resources - an App Service Plan and an App Service. This is a more complex resource model than Static Web Apps, but it comes with additional capabilities.

**Explore Management Options**: Opening the Web App resource in the Portal shows the full range of App Service management features. Even though this is just static HTML, you have access to deployment slots, scaling options, custom domains, SSL certificates, networking features, and comprehensive monitoring. These enterprise features aren't available in Static Web Apps, which is why traditional App Service remains relevant for certain scenarios.

**Examine the Runtime**: We're using curl with the -IL flags to examine the HTTP response headers without downloading content. Looking at the "Server" header reveals this is IIS, indicating the site runs on a Windows server using ASP.NET. This is the default runtime Azure selected when you used the html flag - it chose Windows and IIS automatically to serve your static content.

---

## Using Node.js for Mixed Content

Many real-world applications combine static content with dynamic endpoints that require backend processing. Let's explore this pattern using a Node.js application.

**Understand the Application**: The application in the "node" folder demonstrates a common pattern - it serves static HTML from the "public" directory for the user interface, and provides a dynamic "/user" endpoint in "app.js" that displays authentication information. This represents applications that have some static assets but also need server-side logic for certain features.

**Check Available Runtimes**: Before deploying, we're checking what Node.js runtimes are available on Windows using az webapp list-runtimes with the os filter. This shows the runtime options compatible with our existing App Service Plan.

**Find the Existing Plan**: We're listing App Service Plans in the resource group using az appservice plan list with table output for easy reading. We want to reuse the existing plan rather than creating a new one, which is more efficient.

**Navigate to the Application**: We're changing directories to the node folder where the application code lives.

**Deploy the Node.js Application**: We're using webapp up with several important parameters. We're specifying the existing App Service Plan name to reuse infrastructure, the Node 16 LTS runtime, Windows as the operating system to match the existing plan, and a unique app name. It's critical that the OS type matches your existing plan - since the plan was created with Windows, we must use Windows and specify a Windows-compatible runtime. Mixing OS types on the same plan doesn't work.

**Verify Multiple Apps on One Plan**: Checking the Portal shows a new App Service has been created, but both web apps share the same App Service Plan. This demonstrates efficient resource utilization - both applications run on the same underlying infrastructure but remain isolated from each other. This is a key cost optimization pattern in App Service.

**Test the Application**: Browsing to the new app's URL displays the static HTML page successfully. Trying the "/user" endpoint shows the page renders but the authentication details display as "undefined". The dynamic endpoint works but doesn't have the authentication context it needs because we haven't configured an identity provider yet.

**Explore Instance Details**: Looking at the App Service Plan in the Portal shows both apps listed. You can explore whether they're running on the same physical machine or different machines within the plan - App Service manages this placement automatically based on resource availability and load.

---

## Lab

Your final challenge is to configure authentication for the Node.js application so the "/user" endpoint can display actual user information.

**The Scenario**: The application code is already written to access authentication details from the request context - it just needs an identity provider configured at the platform level. This is a common pattern in App Service where the platform handles authentication without requiring application code changes.

**Your Task**: Open the Node.js Web App in the Portal and navigate to the Authentication settings under the Settings section. Add an identity provider - the application is designed to work with Azure AD authentication. Configure the provider with appropriate settings, including whether to allow unauthenticated access to the static content while requiring authentication for the user endpoint. Test by browsing to the application where you should be prompted to log in. After authenticating, verify that the "/user" endpoint displays your user details including your name and email address.

**The Pattern**: This demonstrates App Service's Easy Auth feature, which adds authentication to applications entirely through platform configuration. The platform intercepts requests, handles the authentication flow with the identity provider, and injects authentication details into the request context where your application code can access them. No code changes or authentication libraries are required in your application.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for completion. The deletion happens in the background, which is useful when cleaning up resource groups with multiple resources. This cleanup is important because Azure resources continue to incur charges until they're deleted.
