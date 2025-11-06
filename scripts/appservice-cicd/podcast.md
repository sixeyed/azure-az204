# App Service CI/CD - Podcast Script

## Welcome and Introduction

Welcome to this episode on Azure App Service Continuous Integration and Continuous Deployment. Today we're exploring how to automate deployments to App Service using GitHub integration and deployment slots, implementing modern DevOps practices that are essential for professional cloud development.

Whether you're preparing for the Azure AZ-204 certification or building production deployment pipelines, understanding App Service CI/CD capabilities is critical. This episode covers GitHub integration, automated deployments, deployment slots, and zero-downtime production releases.

## Understanding CI/CD in App Service

Let's start with the fundamentals: what do we mean by continuous integration and continuous deployment in the context of Azure App Service?

Continuous Integration is the practice of automatically building and testing code whenever developers push changes to a shared repository. Every commit triggers an automated build process that verifies the code compiles and passes tests. This catches integration problems early, when they're easier to fix.

Continuous Deployment extends this further by automatically deploying successful builds to a target environment. When code passes all checks, it's automatically released to staging or production without manual intervention. This enables rapid iteration and ensures that what's in source control matches what's running in production.

Azure App Service provides built-in support for both practices through integration with Git repositories. When you connect App Service to a GitHub repository, Azure can automatically monitor for changes and deploy them. This eliminates manual deployment steps and ensures your application stays current with your latest code.

## Manual vs. Continuous Deployment

App Service supports two deployment integration modes, and understanding the distinction is important for both the exam and real-world scenarios.

**Manual integration** means Azure connects to your repository but doesn't automatically monitor for changes. When you push code to GitHub, nothing happens in Azure until you explicitly trigger a sync operation. You control when deployments occur by clicking the Sync button in the portal or running a CLI command. This gives you complete control but requires manual action for each deployment.

Manual integration works well for development environments where you want to control exactly when updates happen, or for situations where you're experimenting and don't want every commit to trigger a deployment.

**Continuous integration** means Azure actively monitors your repository for changes. When you push code to GitHub, Azure receives a webhook notification immediately. It automatically fetches the new code, builds the application, and deploys it. From commit to production, the process is entirely automated.

Continuous integration is ideal for production deployment pipelines where you want changes to flow automatically through your CI/CD process. Every commit that passes your tests gets deployed immediately, enabling rapid iteration and feedback.

The key difference is automation: manual requires clicking sync, continuous happens automatically on every push.

## Deployment Slots: Staging Environments

One of App Service's most powerful features for production deployments is deployment slots. Understanding slots is crucial for the AZ-204 exam and professional deployments.

A deployment slot is essentially a separate instance of your web app with its own hostname. When you create a slot named "staging", you get a URL like your-app-name-staging.azurewebsites.net running alongside your production app at your-app-name.azurewebsites.net.

Each slot can have its own configuration, its own deployment source, and its own application settings. You might configure the staging slot to deploy from the "staging" branch in GitHub while production deploys from "main". Staging might use test databases while production uses production databases.

The power of slots comes from swapping. After deploying new code to staging and thoroughly testing it, you can swap staging and production. The swap operation exchanges the content between slots, making what was in staging become production and vice versa. Critically, this happens with zero downtime.

Azure implements the swap intelligently. It warms up the instances being moved to production before making them live, ensuring they're ready to serve traffic. It performs a gradual switchover rather than an instant cutover. If you discover problems after swapping, you can swap back immediately, effectively rolling back to the previous version.

This swap capability enables several important deployment patterns: blue-green deployments where you validate the new version alongside the old before switching traffic, canary releases where you gradually shift traffic to the new version, and safe rollbacks if issues appear in production.

Importantly, deployment slots are only available in Standard tier and higher. The Basic and Free tiers don't support slots. This is a frequently tested detail on the AZ-204 exam.

## Walking Through GitHub Integration

Let's walk through the process of setting up continuous deployment from GitHub, understanding what happens at each step.

First, you need your own fork of the repository. This is essential because Azure needs to set up webhooks in the repository, which requires write access. You can't set up webhooks in someone else's repository. Forking creates a copy in your GitHub account where you have full permissions.

In Azure, you create an App Service Plan with Standard tier or higher if you want to use deployment slots later. You create a web app within that plan, specifying the runtime like .NET Core 6.0.

For repositories with multiple projects, you configure the PROJECT application setting to tell Azure which project to build. This is a relative path to the .csproj file within your repository. Azure's build system uses this to locate the correct project when multiple projects exist in the same repository.

Initially, when you browse to your app's URL, you see a default landing page. The app exists, but no code is deployed yet.

To configure manual deployment, you use the deployment source config command with the manual-integration flag. You provide your GitHub repository URL and specify which branch to deploy from. Azure can access public repositories without authentication for manual deployments.

When you configure the deployment source, Azure fetches the code from GitHub, analyzes it to detect the project type, and builds it using the Oryx build system. Oryx is Azure's polyglot build tool that detects whether you're deploying .NET, Node.js, Python, Java, or other platforms, and automatically runs the appropriate build commands.

For a .NET application, Oryx runs dotnet restore to fetch dependencies, dotnet build to compile the code, and deploys the compiled assemblies. You can watch this entire process in real-time through the Deployment Center logs in the portal.

Once deployment completes, your application is live. When you test the API endpoint, it responds correctly, confirming that the build and deployment succeeded.

## Enabling Continuous Deployment

To enable continuous deployment, you need to provide Azure with authentication to GitHub. This requires a GitHub Personal Access Token with specific permissions.

The token needs "workflow" permission to allow Azure to create GitHub Actions if needed, and "admin:repo_hook" permission to let Azure create webhooks that notify it of repository changes. You generate this token in GitHub's developer settings, and it's critical to copy it immediately because you won't see it again.

You then reconfigure the deployment source, this time providing the token instead of using manual integration. Azure uses this token to authenticate to GitHub and set up a webhook in your repository.

When you push code to GitHub after continuous deployment is configured, GitHub sends a webhook notification to Azure. Azure receives this notification, fetches the updated code, builds it, and deploys it automatically. The entire process happens within minutes of pushing your commit.

You can see this in action in the Deployment Center. Each push to GitHub creates a new deployment entry showing the commit that was deployed, when it was deployed, and whether it succeeded or failed.

This automation is the essence of continuous deployment: code flows from developer machines to production automatically, reducing manual steps and enabling rapid iteration.

## Creating and Configuring Deployment Slots

When you're ready to add a staging environment, you create a deployment slot. The command is straightforward: specify the slot name like "staging", and Azure provisions a new slot.

Each slot needs its own configuration. If your production slot has a PROJECT application setting telling Azure which project to build, you need to set the same setting for the staging slot. Slots don't automatically inherit configuration from production; you configure them independently.

A common pattern is to map deployment slots to Git branches. Your production slot deploys from the "main" branch, while your staging slot deploys from a "staging" branch. This creates a clean workflow: developers merge to staging for testing, and promote to main for production releases.

You configure the staging slot's deployment source to use the staging branch. Now pushes to staging trigger deployments to the staging slot, while pushes to main trigger deployments to production. Each slot independently monitors its designated branch.

When you test both slots, they each respond correctly but deploy from different branches. This separation enables parallel development: you can test experimental features in staging without affecting production, and continue to deploy hotfixes to production without waiting for staging validation.

## The Slot Swap Operation

Let's understand what happens during a slot swap, because this is important for the exam and critical for production operations.

When you initiate a swap, Azure exchanges the content and most configuration between the two slots. What was running in staging moves to production, and what was in production moves to staging.

However, the URLs don't change. The staging URL still points to the staging slot, and the production URL still points to the production slot. What changes is the content behind those URLs. Users accessing the production URL now get the application that was just in staging.

Certain configuration settings can be marked as "slot-specific" or "slot-sticky". These settings don't swap; they remain with their slot. Connection strings are often configured as slot-specific because you want staging to always use test databases and production to always use production databases, regardless of which application code is deployed to which slot.

The swap process is designed for zero downtime. Azure warms up the instances being moved to production before exposing them to traffic. If your application has a health check endpoint, Azure pings it until it's ready. Only then does Azure route production traffic to the newly swapped content.

If problems are discovered after swapping, you can swap again to roll back. The previous production version is now in staging, so swapping back restores it to production. This provides a fast rollback mechanism if deployments cause issues.

## App Service CI/CD and the AZ-204 Exam

Now let's connect these concepts to the Azure AZ-204 Developer Associate certification exam, where CI/CD and deployment slots are significant topics.

### Deployment Methods

The exam tests your knowledge of different deployment methods and when to use each. Know these options:

Source control integration with GitHub, Azure Repos, or Bitbucket for Git-based deployments.

Container-based deployment from Azure Container Registry or Docker Hub for containerized applications.

ZIP deploy for uploading pre-packaged applications.

FTP/FTPS for legacy compatibility, though this is discouraged for new deployments.

Azure DevOps pipelines for full CI/CD orchestration with build and release stages.

GitHub Actions for modern CI/CD workflows tightly integrated with GitHub.

Exam questions often present requirements and ask which deployment method is most appropriate. Consider factors like automation level, security requirements, build complexity, and integration needs.

### Deployment Slots Requirements

This is a frequently tested detail: deployment slots are only available in Standard, Premium, and Isolated tier App Service Plans. Basic and Free tiers don't support slots.

Exam questions often present scenarios requiring zero-downtime deployments or staging environments, and the correct answer involves deployment slots. But you must choose an appropriate tier that supports them.

Know that slots consume resources from your App Service Plan. If your plan has two instances and you create a staging slot, you now have four total instances running: two for production and two for staging. This affects capacity planning and cost.

### Slot Swap Behavior

Understanding what happens during a slot swap is crucial for exam questions. Know these key points:

Most application settings and configuration swap with the content, allowing the new version to use production configuration.

Slot-specific settings don't swap; they remain with their slot. This is critical for connection strings and API keys that differ between environments.

The swap operation warms up instances before exposing them to traffic, eliminating cold starts.

URLs remain constant; only the content behind them changes.

You can configure auto-swap to automatically swap after successful deployments to staging, fully automating the production release process.

Swap with preview is a multi-phase operation that lets you validate the swap before completing it, providing an extra safety check.

### CLI Commands for the Exam

Be familiar with these Azure CLI commands:

Creating deployment slots uses "az webapp deployment slot create" with the slot parameter.

Configuring deployment sources uses "az webapp deployment source config" with repository URL, branch, and optionally the Git token for continuous integration.

Swapping slots uses "az webapp deployment slot swap" with source and target slot parameters.

Setting slot-specific application settings uses "az webapp config appsettings set" with the slot-settings parameter to mark them as slot-sticky.

You don't need to memorize exact syntax, but you should recognize correct commands and understand their parameters.

### Common Exam Scenarios

Based on actual exam questions, expect these scenarios:

"You need to deploy a web application with zero downtime and the ability to roll back quickly if issues occur."

Solution: Use deployment slots with staging and production, deploy to staging, test thoroughly, then swap to production. If issues arise, swap back.

"After swapping deployment slots, your application in production is connecting to the test database instead of the production database."

Solution: The connection string is not configured as slot-specific. Mark it as slot-sticky so it doesn't swap with the content.

"You need to automatically deploy when code is pushed to GitHub."

Solution: Configure continuous deployment with GitHub token authentication to enable webhook-triggered deployments.

"Your App Service is on Basic tier, but you don't see the option to create deployment slots."

Solution: Upgrade to Standard tier or higher, which is required for deployment slot support.

"You want to test changes in a staging environment before users see them."

Solution: Create a staging deployment slot, deploy changes there, validate, then swap to production.

### GitHub Integration Details

For the exam, understand GitHub-specific requirements:

A Personal Access Token is required with "workflow" and "admin:repo_hook" permissions for continuous deployment.

Azure creates webhooks in your repository that notify it of push events.

Manual integration doesn't require a token for public repositories but requires clicking sync for each deployment.

Different slots can deploy from different branches, enabling branch-based deployment workflows.

Webhook creation can sometimes fail or timeout; retrying the command often resolves this, which is a known quirk to be aware of.

## Key Takeaways

Let me summarize the critical points about App Service CI/CD:

First, App Service supports both manual and continuous deployment integration with Git repositories, with continuous deployment providing automatic deployment on every push.

Second, deployment slots enable staging environments and zero-downtime deployments through swapping, but require Standard tier or higher.

Third, GitHub integration requires Personal Access Tokens with specific permissions for continuous deployment and webhook creation.

Fourth, slot swaps exchange content between slots while keeping URLs constant, and slot-specific settings don't swap.

Fifth, Azure's Oryx build system automatically detects project types and builds applications without requiring build pipeline configuration.

Finally, deployment workflows can map branches to slots, enabling clean separation between staging and production release processes.

## Final Thoughts

Azure App Service CI/CD capabilities enable modern DevOps practices with minimal configuration. The combination of GitHub integration, automated builds, and deployment slots provides a complete solution for continuous delivery with testing stages and zero-downtime releases.

For the AZ-204 exam, CI/CD and deployment slots represent a significant topic because they demonstrate understanding of professional deployment practices, infrastructure requirements, and operational considerations.

The hands-on experience with these features is invaluable. Actually setting up GitHub integration, watching automated deployments, creating slots, and performing swaps provides practical knowledge that reading alone cannot deliver.

As you continue your AZ-204 preparation, think about CI/CD in the context of complete DevOps pipelines. How do you integrate testing into deployment workflows? How do you handle database schema changes alongside application deployments? How do you implement progressive rollouts with partial traffic shifting? How do you monitor deployments to detect issues quickly?

These broader questions demonstrate the systems thinking that the AZ-204 certification validates. It's not just about configuring deployment sources; it's about designing reliable, automated delivery pipelines that enable rapid innovation while maintaining production stability.

Thanks for listening to this episode on App Service CI/CD. I hope this gives you both the conceptual understanding and practical knowledge for the AZ-204 exam and for implementing professional deployment pipelines in Azure. Good luck with your studies!
