
We've covered two approaches for hosting static content: Azure Static Web Apps (optimized for static sites) versus traditional App Service. Now let's deploy static content both ways and understand the differences.

First, you'll deploy using Azure Static Web Apps. You'll fork the course repository on GitHub (you need write access for automated workflows), then create a Static Web App with `az staticwebapp create`. Watch as Azure automatically creates a GitHub Actions workflow file in `.github/workflows` for continuous deployment. Make changes to your HTML, commit and push to your fork, and the GitHub Actions workflow automatically builds and deploys updates to your live site. This is Git-integrated deployment at its best!

Then you'll deploy the same static content to traditional App Service using `az webapp up --html`. This deploys from your local filesystem without Git integration. Examining HTTP headers reveals IIS serving the content on Windows - App Service defaults to Windows for static content.

Next comes something interesting: deploying a Node.js application with both static content and a dynamic `/user` endpoint to the existing App Service Plan. Multiple apps share the same infrastructure. The app runs on Windows Node runtime to match the plan's OS.

The lab challenge involves configuring Azure AD authentication through the Portal's Easy Auth settings. Once enabled, the `/user` endpoint can display authenticated user details without any code changes - App Service handles authentication, token validation, and session management automatically!

This demonstrates the flexibility of traditional App Service: you started with pure static content, then added a dynamic API with server-side logic, then enabled enterprise authentication - all sharing one infrastructure. Static Web Apps is simpler for pure static sites, but App Service provides more flexibility for mixed content.

Let's explore both static hosting approaches!
