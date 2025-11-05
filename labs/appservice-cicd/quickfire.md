# App Service CI/CD - Quickfire Questions

## Question 1
What is Continuous Integration (CI)?


- A) Integrating multiple Azure services
- B) Automatically deploying code to production
- C) Automatically building and testing code when changes are committed
- D) Continuously monitoring application performance

**Answer: C**
CI is the practice of automatically building and testing code whenever changes are pushed to the repository.
---
## Question 2
What is Continuous Deployment (CD)?


- A) Automatically deploying code to production after passing tests
- B) Creating deployment documentation
- C) Backing up data continuously
- D) Monitoring deployments

**Answer: A**
CD automatically deploys code changes to production (or staging) environments after passing automated tests.
---
## Question 3
What are deployment slots in App Service?


- A) API endpoints for deployments
- B) Time slots for scheduling deployments
- C) Separate live environments with their own hostnames running different versions of your app
- D) Storage locations for deployment packages

**Answer: C**
Deployment slots are live apps with their own hostnames. You can run different versions and swap them with zero downtime.
---
## Question 4
What is the primary benefit of using deployment slots for production deployments?


- A) Lower cost
- B) Better performance
- C) Automatic testing
- D) Zero-downtime deployment with ability to rollback

**Answer: D**
Deployment slots allow you to deploy to staging, test, then swap with production instantly. If issues arise, you can swap back.
---
## Question 5
Which App Service tier is required to use deployment slots?


- A) Standard (S1) or higher
- B) Any tier
- C) Free (F1)
- D) Basic (B1)

**Answer: A**
Deployment slots are only available in Standard (S1), Premium, and Isolated tiers.
---
## Question 6
What happens to app settings when you swap deployment slots?


- A) Settings cannot be configured differently per slot
- B) All settings move with the swap
- C) Settings marked as "deployment slot settings" stay with the slot and don't swap
- D) All settings are reset to default

**Answer: C**
You can mark settings as "slot settings" which will stay with that specific slot and not swap with the app.
---
## Question 7
Which CI/CD platform integrates natively with App Service?


- A) Azure DevOps
- B) Jenkins
- C) GitHub Actions
- D) All of the above

**Answer: D**
App Service supports GitHub Actions, Azure DevOps (Azure Pipelines), Bitbucket, Jenkins, and other CI/CD platforms.
---
## Question 8
What is warming up in the context of deployment slots?


- A) Pre-compiling code
- B) Making HTTP requests to the slot before swapping to initialize the app
- C) Gradual traffic routing
- D) Increasing server temperature

**Answer: B**
Slot warming sends HTTP requests to the app before swapping to ensure all instances are initialized and cached, preventing cold starts.
---
## Question 9
How can you route a percentage of production traffic to a staging slot for testing?


- A) Using Traffic Manager
- B) Not possible
- C) Using deployment slot traffic routing
- D) Using Application Gateway

**Answer: C**
App Service supports traffic routing where you can direct a percentage of traffic to a specific slot for A/B testing or canary deployments.
---
## Question 10
What is the purpose of auto-swap in deployment slots?


- A) Swaps slots on a schedule
- B) Randomly swaps slots for testing
- C) Prevents manual swapping
- D) Automatically swaps slots after successful deployment

**Answer: D**
Auto-swap automatically swaps a slot to production after a deployment completes, useful for automated CI/CD pipelines.