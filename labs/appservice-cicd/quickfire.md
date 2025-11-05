# App Service CI/CD - Quickfire Questions

## Question 1
What is Continuous Integration (CI)?

- A) Automatically deploying code to production
- B) Automatically building and testing code when changes are committed
- C) Continuously monitoring application performance
- D) Integrating multiple Azure services

**Answer: B**
CI is the practice of automatically building and testing code whenever changes are pushed to the repository.

---

## Question 2
What is Continuous Deployment (CD)?

- A) Backing up data continuously
- B) Automatically deploying code to production after passing tests
- C) Monitoring deployments
- D) Creating deployment documentation

**Answer: B**
CD automatically deploys code changes to production (or staging) environments after passing automated tests.

---

## Question 3
What are deployment slots in App Service?

- A) Time slots for scheduling deployments
- B) Separate live environments with their own hostnames running different versions of your app
- C) Storage locations for deployment packages
- D) API endpoints for deployments

**Answer: B**
Deployment slots are live apps with their own hostnames. You can run different versions and swap them with zero downtime.

---

## Question 4
What is the primary benefit of using deployment slots for production deployments?

- A) Lower cost
- B) Better performance
- C) Zero-downtime deployment with ability to rollback
- D) Automatic testing

**Answer: C**
Deployment slots allow you to deploy to staging, test, then swap with production instantly. If issues arise, you can swap back.

---

## Question 5
Which App Service tier is required to use deployment slots?

- A) Free (F1)
- B) Basic (B1)
- C) Standard (S1) or higher
- D) Any tier

**Answer: C**
Deployment slots are only available in Standard (S1), Premium, and Isolated tiers.

---

## Question 6
What happens to app settings when you swap deployment slots?

- A) All settings move with the swap
- B) Settings marked as "deployment slot settings" stay with the slot and don't swap
- C) All settings are reset to default
- D) Settings cannot be configured differently per slot

**Answer: B**
You can mark settings as "slot settings" which will stay with that specific slot and not swap with the app.

---

## Question 7
Which CI/CD platform integrates natively with App Service?

- A) GitHub Actions
- B) Azure DevOps
- C) Jenkins
- D) All of the above

**Answer: D**
App Service supports GitHub Actions, Azure DevOps (Azure Pipelines), Bitbucket, Jenkins, and other CI/CD platforms.

---

## Question 8
What is warming up in the context of deployment slots?

- A) Increasing server temperature
- B) Making HTTP requests to the slot before swapping to initialize the app
- C) Gradual traffic routing
- D) Pre-compiling code

**Answer: B**
Slot warming sends HTTP requests to the app before swapping to ensure all instances are initialized and cached, preventing cold starts.

---

## Question 9
How can you route a percentage of production traffic to a staging slot for testing?

- A) Using Traffic Manager
- B) Using deployment slot traffic routing
- C) Using Application Gateway
- D) Not possible

**Answer: B**
App Service supports traffic routing where you can direct a percentage of traffic to a specific slot for A/B testing or canary deployments.

---

## Question 10
What is the purpose of auto-swap in deployment slots?

- A) Automatically swaps slots after successful deployment
- B) Swaps slots on a schedule
- C) Randomly swaps slots for testing
- D) Prevents manual swapping

**Answer: A**
Auto-swap automatically swaps a slot to production after a deployment completes, useful for automated CI/CD pipelines.
