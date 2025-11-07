# App Service CI/CD

## Reference

Continuous Integration and Continuous Deployment are supported with two features of Azure App Service: deployments which can be triggered every time source code is changed and pushed to a Git repo, and deployment slots which let you deploy to a staging environment and test it before you send the new version to production.

## App Service Deployment from GitHub

First, we need to ensure you have your own fork of the lab repository. If you haven't done this yet, we're navigating to the GitHub repository and clicking the Fork button. This creates a copy in your own GitHub account that you have write access to - this is essential because Azure needs to connect to a repository where it can set up webhooks and read your code.

Once you have your fork, we're adding it as a remote to your local repository using git remote add with the name "fork" and your fork's URL. Make sure to replace the placeholder with your actual GitHub username.

Now let's create our Azure resources. We'll need a Resource Group and an App Service Plan to host our application.

We're creating the Resource Group named "labs-appservice-cicd" with our standard courselabs tag for tracking.

Now we're creating a Linux App Service Plan with 2 workers. Note that we're using the S1 SKU - Standard tier is required to get the deployment slot features we'll be using later in this lab. The Free and Basic tiers don't support slots, which are crucial for proper CI/CD workflows.

The plan is now ready to host our application with the redundancy and features we need.

We're creating the web app with .NET Core 6.0 runtime, specifying the resource group, the App Service Plan we just created, and a globally unique DNS name. Remember to replace the placeholder with your unique app name.

Now we're setting the project path so Azure knows which application to deploy. This is important because our repository contains multiple projects, and we need to tell Azure specifically which one to build and deploy. We're adding an application setting called "PROJECT" with the path to the Numbers API project file. This setting tells Azure's build system exactly where to find the project to compile.

If you browse to your App Service URL now, you'll see a waiting page. The app isn't deployed yet - we've created the hosting infrastructure, but we haven't actually put any code on it.

Let's create our first manual deployment. Since your GitHub repository is public, Azure can fetch it without authentication - this makes manual deployments straightforward. We're configuring the deployment source using the deployment source config command, specifying manual integration mode, the main branch as our source, and the repository URL. Make sure to add the .git suffix to your repository URL - this tells Azure it's a Git repository.

Opening the Azure Portal and navigating to your App Service, clicking on the Deployment Center tab, you'll see the Settings showing your GitHub configuration and the Logs showing the deployment status. This first deployment takes a few minutes as Azure fetches the code, builds the application using Oryx, and deploys it.

You can watch the progress in real-time as Azure clones your repository, detects that it's a .NET Core application, runs dotnet restore to fetch dependencies, runs dotnet build to compile the code, and finally deploys the compiled application.

Once deployment completes, we're testing your API using curl to call the "/rng" endpoint. You should receive a random number in the response. Calling it multiple times, you'll get different numbers each time, confirming the API is working correctly.

Now let's make a change to the application. We're navigating to the appsettings.json file in your GitHub fork at the path "src/rng/Numbers.Api/appsettings.json".

Editing the file directly on GitHub, we're changing the RngSettings to set minimum to 1000 and maximum to 10000. This will make the random number generator produce much larger numbers. Committing your changes with a descriptive message like "Change RNG range" helps you track what was changed and why.

Alternatively, you can make these changes locally. We're opening the file in your editor, making the same changes, using git add to stage the file, git commit to save the change with a message, and git push to send it to your fork. Both approaches work - it's about what fits your workflow better.

Checking the Deployment Center in the Portal, you'll notice there's no new deployment, even though the source repository has changed. This is because we're using manual integration - Azure doesn't automatically monitor for changes.

Clicking the Sync button triggers an update to pull the latest code from the repository. This is manual CI/CD - you control when deployments happen by clicking Sync.

Waiting for the deployment to complete, then testing again with curl to call the "/rng" endpoint, now you should see much larger random numbers, between 1000 and 10000. This confirms that your code change was deployed successfully.

## Configure CI/CD

Manual deployment works, but it's not automated. Let's switch to Continuous Integration so every push to GitHub triggers a deployment automatically.

First, we need to create a GitHub Personal Access Token. We're navigating to the GitHub tokens page at github.com/settings/tokens/new. You may need to sign in again if using multi-factor authentication.

We're entering a note like "Azure App Service CI/CD" to remember what this token is for, selecting the "workflow" permission which allows Azure to create GitHub Actions, and selecting "admin:repo_hook" which allows Azure to set up webhooks. Clicking Generate Token, we're copying it immediately - you won't see it again after leaving this page.

Your token will look something like "ghp_" followed by random characters.

Now we're deleting the manual deployment source to clear the configuration.

And replacing it with continuous deployment using the same deployment source config command, but this time we're providing your GitHub token with the git-token parameter. This authenticates Azure to set up webhooks and monitor your repository.

Note: Sometimes this command may appear to hang. If it doesn't return within a few minutes, cancel with Control-C and run the exact same command again - this is a known quirk of the CLI.

Checking the Deployment Center in the Settings tab, you'll now see your GitHub username, confirming the connection is authenticated. Azure has set up a webhook in your repository that will notify it of any changes.

Making another change to the appsettings.json file, perhaps changing the range again or adjusting another setting, we're committing and pushing to GitHub.

This time, watching the Deployment Center, within moments you should see a new deployment automatically triggered. No manual sync required! Azure received a notification from GitHub, pulled the latest code, built it, and deployed it automatically.

This is the power of continuous deployment - your changes flow from development to production with minimal manual intervention.

## Add a Staging Deployment Slot

Now let's add a staging deployment slot. This allows us to test changes before they go to production - you deploy to staging, verify everything works, then swap staging and production.

We're creating the staging slot using the deployment slot create command with the slot parameter set to "staging".

Now we're configuring the project path for the staging slot. Deployment slots have their own configuration, so we need to set the PROJECT setting for the staging slot separately using the same setting as production but with the --slot parameter.

Deployment slots typically match source code branches. This gives you a clean workflow - the main branch deploys to production, the staging branch deploys to staging.

We're creating a staging branch in GitHub by navigating to your fork, clicking the branches button, and creating a new branch called "staging".

Now we're configuring the staging slot to deploy from the staging branch using deployment source config with the --slot parameter. This links the staging slot to the staging branch.

Again, this might take a moment. Cancel and retry if it appears stuck - it's processing the webhook setup in the background.

In the Portal, navigating to Deployment slots, you can switch between your production and staging slots. Each has its own URL, its own configuration, and its own deployment source.

We're testing both endpoints using curl. The production slot is at your normal app URL, and the staging slot has "-staging" appended to the hostname.

Both should return random numbers, and since they're running the same code version right now, they'll have the same range. But soon we'll make them different to demonstrate the slot workflow.

---

## Lab

Now for your challenge: Update the app settings in the staging slot so the random number range is 50 to 500. Test your changes in the staging environment to verify they work correctly. Once you're satisfied the changes are good, swap the slots so production uses the new range.

Think about the workflow: How do you update configuration in a specific slot? The configuration blade has a slot selector at the top. How do you verify the changes are working? Test the staging URL directly. What command swaps the slots? Look for the swap operation in the Portal or check the CLI documentation. What happens to the URLs after swapping? The slots maintain their URLs, but their content swaps - staging becomes production and production becomes staging.

Take some time to work through this, and check the solution guide if you get stuck.

---

## Cleanup

When you're finished, we're deleting the Resource Group to avoid ongoing charges using the group delete command with the -y flag to skip confirmation.
