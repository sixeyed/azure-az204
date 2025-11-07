
We've covered App Service as a fully managed PaaS offering that handles infrastructure while you focus on application code. Now let's deploy a real application to Azure.

You'll start by creating an App Service Plan (B1 SKU with 2 workers for redundancy). The plan is the compute unit - think of it as the servers that will run your apps. You'll check available runtimes to confirm ASP.NET 4.8 support, demonstrating how App Service handles legacy app migration without requiring VM management.

Then you'll create a web app configured for local Git deployment. This turns your Azure web app into a Git remote repository. You'll configure deployment settings using application settings like `DEPLOYMENT_BRANCH` (which branch to build) and `PROJECT` (which project file to compile in a multi-project repo).

The deployment is where it gets interesting: you'll get publishing credentials - these are special credentials embedded in the Git remote URL. After adding App Service as a Git remote, you simply push your code. Watch as Azure automatically detects it's a .NET project, runs MSBuild, compiles your code, and deploys the binaries. You didn't upload compiled DLLs - you pushed source code and Azure built it!

Next, you'll explore the runtime environment through the Portal Console, examining the filesystem structure to see where your DLLs live, how the directory structure is organized, and what environment variables are available. This demystifies the "magic" of PaaS deployment.

Finally, you'll make code changes and redeploy to measure update timing. You'll see how incremental deployments are fast because Azure only rebuilds and deploys what changed.

Let's deploy and explore App Service!
