
We've covered the concepts of continuous integration and deployment with App Service. Now let's see it in action with hands-on exercises deploying a real application from GitHub.

You'll start by setting up your own GitHub fork of the lab repository - this is essential because Azure needs write access to set up webhooks and monitor your code. You'll add your fork as a remote to your local repository.

Then you'll create the Azure infrastructure - a resource group and an App Service Plan with Standard tier (required for deployment slots). You'll see why the Free and Basic tiers don't support the slot features crucial for proper CI/CD workflows.

Next, you'll create the web app and configure the deployment path. The lab repository contains multiple projects, so you'll set the PROJECT application setting to tell Azure's build system exactly which project to compile. Then you'll deploy manually from GitHub using the `--manual-integration` flag, watching in the Portal as Azure fetches your code, detects it's .NET Core, runs restore and build, and deploys the application. You'll test the random number API to confirm it's working.

After making a code change to adjust the random number range, you'll learn an important lesson: manual integration doesn't automatically deploy changes. You need to click the Sync button in the Deployment Center to pull updates. This is manual CI/CD - you control when deployments happen.

To enable true continuous integration, you'll create a GitHub Personal Access Token with workflow and webhook permissions, delete the manual deployment source, and configure continuous deployment. Now every push to GitHub automatically triggers a deployment - no manual sync required!

Finally, you'll create a staging deployment slot linked to a staging branch. This lets you test changes before they go to production. The lab challenge has you updating configuration in staging, testing it, and then swapping slots to promote the tested changes to production with zero downtime.

Let's build a complete CI/CD pipeline with App Service!
