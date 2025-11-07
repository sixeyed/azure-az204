
Excellent work comparing static hosting approaches! This topic tests your understanding of when to use different Azure services for web hosting.

When to choose Static Web Apps versus App Service is a key exam decision. Choose Static Web Apps for: pure static content (HTML, CSS, JavaScript), SPAs (React, Angular, Vue), JAMstack applications, Git-integrated deployment (GitHub Actions or Azure DevOps automatic), staging from pull requests (automatic preview environments), no plan management (simpler resource model). The exam tests recognizing these scenarios.

When to choose App Service instead: need more deployment flexibility (FTP, ZIP, local Git), require full management features (slots, auto-scale, VNet integration), have mixed static/dynamic content in the same app, want to share infrastructure across multiple apps (plan sharing), need specific runtime configurations. The exam presents scenarios requiring these capabilities.

Static Web Apps architecture with Git-based deployment needs to be understood. Deployment happens through GitHub Actions or Azure DevOps pipelines defined in YAML workflow files. Azure automatically creates the workflow file when you create the Static Web App. The exam tests understanding of this automated workflow approach.

GitHub Actions for CI/CD is part of the deployment model. The workflow builds your site, deploys to Azure, and creates preview environments for pull requests. Know that Static Web Apps require repository write access and that changes to the workflow file affect deployment behavior.

App Service deployment with `az webapp up` provides rapid deployment. The `--html` flag indicates static content (no build step required), deployment uses ZIP deployment mechanism internally, and content is served by IIS on Windows by default. The exam tests when to use `webapp up` and its parameters.

Runtime stack configuration for App Service matters when mixing static and dynamic content. Static content typically uses Windows with IIS. Dynamic Node.js apps can use Windows or Linux. Plans are OS-specific (can't run both Windows and Linux apps on the same plan). The exam tests understanding of runtime compatibility and OS limitations.

Authentication with Easy Auth (App Service Authentication) enables authentication without code changes. Configure identity providers (Azure AD, Google, Facebook, Microsoft, Twitter) through Portal, protect endpoints with authentication requirements, and access user details in application code via headers. The exam tests when to use Easy Auth versus custom authentication code.

Resource management differences are important for cost and architecture decisions. Static Web Apps require only one resource (simpler management). App Service requires a plan (additional resource to manage). Multiple apps can share an App Service Plan for cost optimization but not Static Web Apps.

We'll cover deployment model comparison, cost implications, staging environment patterns, authentication integration, and common scenarios about choosing the right hosting service for different application types.

Master static web hosting options for the AZ-204!
