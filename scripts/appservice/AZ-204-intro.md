
Great job deploying to App Service! This is one of the most heavily tested topics on the AZ-204 covering multiple exam domains.

App Service Plans as compute units is fundamental. One plan can host multiple apps that share the compute resources (CPU, memory, instances). The plan defines region (can't move apps across regions without recreating), SKU/pricing tier (determines features and performance), and scaling capabilities. The exam tests understanding of when to use shared plans (cost savings) versus separate plans (isolation, different scaling needs).

Pricing tiers must be memorized. Free/Shared for dev/test (no SLA, limited CPU minutes, custom domains in Shared only). Basic for dedicated compute (manual scaling up to 3 instances, no deployment slots). Standard with auto-scale and staging slots (up to 10 instances). Premium with enhanced performance (up to 30 instances, VNet integration, always-on). Isolated with dedicated VNet (maximum isolation and scale). The exam tests which tier to choose based on requirements.

Deployment methods and their use cases appear frequently. Local Git (push code, Azure builds it), GitHub/Azure Repos/Bitbucket (continuous deployment with webhooks), Containers (Docker images), FTP (manual file transfer, not recommended), ZIP deploy (package and upload), DevOps pipelines (full CI/CD). Know when to use each method and their tradeoffs.

Application settings override configuration files, acting as environment variables available to your code. Connection strings have special handling with type prefixes (SQLServer, SQLAzure, Custom, etc.). Configuration precedence: Application Settings > appsettings.json > web.config. Know how to configure slot-specific settings that don't swap during deployment slot swaps.

Deployment slots enable zero-downtime deployments. Deploy to staging, test thoroughly, swap to production. Each slot is a live app with its own hostname. Swapping is instant - just DNS changes. Some settings are slot-specific (stick with the slot) while others swap with the app. The exam heavily tests slot behavior and configuration.

Diagnostic logging types need to be understood. Application logging (your code's output), Web server logging (IIS logs), Detailed error messages (full error pages), Failed request tracing (detailed diagnostics for failed requests), Deployment logging (deployment process logs). Know what each captures and where to configure it.

Scaling strategies are critical. Scale up changes SKU (more CPU/memory, requires restart). Scale out adds instances (more capacity, no restart, requires Standard or higher for auto-scale). Auto-scaling based on metrics (CPU, memory, HTTP queue) or schedules (time-based rules). The exam tests when to scale up versus out and how to configure auto-scale rules.

We'll cover built-in authentication (Easy Auth), custom domains and SSL, virtual applications and directories, and common scenarios about deployment troubleshooting, performance optimization, and cost management.

Master App Service for the AZ-204!
