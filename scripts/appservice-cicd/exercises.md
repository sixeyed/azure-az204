# App Service CI/CD - Exercises Script

## Exercise 1: Setting Up GitHub Fork

First, we need to ensure you have your own fork of the lab repository. If you haven't done this yet:

Navigate to the GitHub repository and click the Fork button. This creates a copy in your own GitHub account that you have write access to.

Once you have your fork, add it as a remote to your local repository:

```
git remote add fork https://github.com/your-github-username/azure.git
```

Replace "your-github-username" with your actual GitHub username.

## Exercise 2: Create Azure Resources

Now let's create our Azure resources. We'll need a Resource Group and an App Service Plan.

Create the Resource Group:

```
az group create -n labs-appservice-cicd --tags courselabs=azure
```

Create a Linux App Service Plan with 2 workers. Note that we're using the S1 SKU - Standard tier is required to get the CI/CD features we'll be using:

```
az appservice plan create -g labs-appservice-cicd -n app-plan-01 --is-linux --sku S1 --number-of-workers 2
```

The plan is now ready to host our application.

## Exercise 3: Create Web App and Configure Deployment Path

Create the web app with .NET Core 6.0 runtime:

```
az webapp create -g labs-appservice-cicd --plan app-plan-01 --runtime dotnetcore:6.0 -n your-unique-app-name
```

Remember to replace "your-unique-app-name" with a globally unique DNS name.

Now set the project path so Azure knows which application to deploy:

```
az webapp config appsettings set --settings PROJECT='src/rng/Numbers.Api/Numbers.Api.csproj' -g labs-appservice-cicd -n your-unique-app-name
```

This tells Azure to deploy the Numbers API project from the repository.

## Exercise 4: Manual Deployment from GitHub

If you browse to your App Service URL now, you'll see a waiting page. The app isn't deployed yet.

Let's create our first manual deployment. Since your GitHub repository is public, Azure can fetch it without authentication:

```
az webapp deployment source config -g labs-appservice-cicd --manual-integration --branch main -n your-unique-app-name --repo-url https://github.com/your-github-username/azure.git
```

Make sure to add the .git suffix to your repository URL.

Open the Azure Portal and navigate to your App Service. Click on the Deployment Center tab. You'll see the Settings showing your GitHub configuration and the Logs showing the deployment status.

This first deployment takes a few minutes as Azure fetches the code, builds the application, and deploys it.

## Exercise 5: Test the Deployed API

Once deployment completes, test your API:

```
curl https://your-unique-app-name.azurewebsites.net/rng
```

You should receive a random number in the response. Call it multiple times and you'll get different numbers each time.

## Exercise 6: Make a Code Change

Now let's make a change to the application. Navigate to the appsettings.json file in your GitHub fork:

```
src/rng/Numbers.Api/appsettings.json
```

Edit the file directly on GitHub, changing the RngSettings:
- Set minimum to 1000
- Set maximum to 10000

Commit your changes with a descriptive message like "Change RNG range".

Alternatively, you can make these changes locally and push:

```
git add src/rng/Numbers.Api/appsettings.json
git commit -m 'Change RNG range'
git push fork main
```

## Exercise 7: Manual Sync

Check the Deployment Center in the Portal. You'll notice there's no new deployment, even though the source repository has changed. This is because we're using manual integration.

Click the Sync button to trigger an update to the latest code.

Wait for the deployment to complete, then test again:

```
curl https://your-unique-app-name.azurewebsites.net/rng
```

Now you should see much larger random numbers, between 1000 and 10000.

## Exercise 8: Configure Continuous Integration

Manual deployment works, but it's not automated. Let's switch to Continuous Integration so every push to GitHub triggers a deployment automatically.

First, create a GitHub Personal Access Token:
1. Navigate to https://github.com/settings/tokens/new
2. You may need to sign in again if using MFA
3. Enter a note like "Azure App Service CI/CD"
4. Select the "workflow" and "admin:repo_hook" permissions
5. Click Generate Token and copy it immediately - you won't see it again

Your token will look something like: ghp_followed-by-random-characters

Now delete the manual deployment source:

```
az webapp deployment source delete -g labs-appservice-cicd -n your-unique-app-name
```

And replace it with continuous deployment:

```
az webapp deployment source config -g labs-appservice-cicd --branch main -n your-unique-app-name --repo-url https://github.com/your-github-username/azure.git --git-token your-github-token
```

Note: Sometimes this command may appear to hang. If it doesn't return within a few minutes, cancel with Control-C and run the exact same command again.

Check the Deployment Center - in the Settings tab you'll now see your GitHub username, confirming the connection is authenticated.

## Exercise 9: Test Continuous Deployment

Make another change to the appsettings.json file, perhaps changing the range again. Commit and push to GitHub.

This time, watch the Deployment Center. Within moments, you should see a new deployment automatically triggered. No manual sync required!

## Exercise 10: Create Staging Slot

Now let's add a staging deployment slot. This allows us to test changes before they go to production.

Create the staging slot:

```
az webapp deployment slot create --slot staging -g labs-appservice-cicd -n your-unique-app-name
```

Configure the project path for the staging slot:

```
az webapp config appsettings set --slot staging --settings PROJECT='src/rng/Numbers.Api/Numbers.Api.csproj' -g labs-appservice-cicd -n your-unique-app-name
```

## Exercise 11: Configure Staging Branch

Deployment slots typically match source code branches. Create a staging branch in GitHub:

1. Navigate to your GitHub fork
2. Click the branches button
3. Create a new branch called "staging"

Now configure the staging slot to deploy from the staging branch:

```
az webapp deployment source config -g labs-appservice-cicd --branch staging --slot staging -n your-unique-app-name --repo-url https://github.com/your-github-username/azure.git --git-token your-github-token
```

Again, this might take a moment. Cancel and retry if it appears stuck.

## Exercise 12: Test Both Slots

In the Portal, navigate to Deployment slots. You can switch between your production and staging slots, each with its own URL.

Test both endpoints:

```
# Production slot:
curl https://your-unique-app-name.azurewebsites.net/rng

# Staging slot:
curl https://your-unique-app-name-staging.azurewebsites.net/rng
```

Both should return random numbers, and since they're running the same code version, they'll have the same range.

## Exercise 13: Lab Challenge

Now for your challenge:

Update the app settings in the staging slot so the random number range is 50 to 500. Test your changes in the staging environment. Once you're satisfied the changes work correctly, swap the slots so production uses the new range.

Think about:
- How do you update configuration in a specific slot?
- How do you verify the changes are working?
- What command swaps the slots?
- What happens to the URLs after swapping?

Take some time to work through this, and check the solution guide if you get stuck.

## Conclusion

You've now learned how to:
- Deploy App Service applications from GitHub
- Configure continuous deployment with automated builds
- Create and manage deployment slots
- Test changes in staging before promoting to production

These skills are essential for modern DevOps practices and are important for the AZ-204 certification exam.

## Cleanup

When you're finished, delete the Resource Group to avoid ongoing charges:

```
az group delete -y -n labs-appservice-cicd
```

Great work!
