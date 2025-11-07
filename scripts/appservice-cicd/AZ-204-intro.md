
Great job completing the hands-on exercises! Now let's focus on what you need to know about App Service deployments and deployment slots for the AZ-204 certification exam.

App Service deployment methods and slots are crucial topics for AZ-204. They appear in questions about implementing continuous deployment, achieving zero-downtime deployments, and managing application lifecycle. Expect both direct questions about commands and scenario-based questions about choosing the right approach.

First, we'll review the six deployment methods App Service supports: source control integration (GitHub, Azure Repos, Bitbucket), container-based deployment, ZIP deploy, FTP/FTPS, Azure Pipelines, and GitHub Actions. The exam tests your understanding of when to use each method and their tradeoffs.

Deployment slots is one of the most heavily tested topics. You must know that slots are only available in Standard, Premium, and Isolated tiers - Basic and Free don't support them. This is a common exam trick question. We'll cover slot-specific settings versus app-level settings, the concept of "sticky" settings that don't move during swaps, and the warm-up process that eliminates cold starts in production.

We'll dive deep into the Azure CLI commands you need to memorize. Creating deployment slots with `az webapp deployment slot create`, configuring deployment sources with `az webapp deployment source config`, swapping slots with `az webapp deployment slot swap`, and configuring slot-specific settings. Know these command syntaxes cold - the exam tests parameter names like `--slot` versus `--target-slot`.

Slot swap behavior appears on almost every exam. When you swap slots, most settings move with the slot, but slot-sticky settings like connection strings stay in place. The URLs swap so staging becomes production. The process is designed for zero downtime with automatic warm-up. You can also configure auto-swap to automatically swap slots after successful deployment, and swap-with-preview for multi-phase swapping with validation.

GitHub integration details are important: Azure requires a Personal Access Token with `workflow` and `admin:repo_hook` permissions, Azure creates webhooks in your repository to trigger deployments, and you need to understand manual versus continuous integration modes. Branch mapping lets different deployment targets map to different Git branches - main deploys to production, staging deploys to the staging slot.

We'll cover best practices the exam expects you to know: always test in staging before production, use Standard SKU or higher for slots, configure slot-specific connection strings to keep production data separate, prefer continuous deployment over manual for consistency, and configure health checks to ensure slots are ready before swapping.

Finally, we'll work through common exam scenarios: deploying with zero downtime (use deployment slots), preventing staging from connecting to production database after swap (use slot-specific connection strings), deploying automatically on GitHub push (continuous deployment with GitHub token), and why deployment slots aren't showing (Basic tier doesn't support them).

Ready to master App Service CI/CD for the exam? Let's go!
