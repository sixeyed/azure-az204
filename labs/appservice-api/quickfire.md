# App Service API - Quickfire Questions

## Question 1
What is the primary benefit of using App Service for REST APIs?


- A) It offers managed infrastructure with built-in scaling, security, and deployment features
- B) It requires no configuration
- C) It provides automatic API documentation
- D) It only supports .NET applications

**Answer: A**
App Service provides a fully managed platform for hosting APIs with features like auto-scaling, SSL, deployment slots, and integrated authentication.
---
## Question 2
Which App Service feature allows you to test new API versions before directing production traffic to them?


- A) Deployment slots
- B) Traffic Manager
- C) Load Balancer
- D) API Gateway

**Answer: A**
Deployment slots allow you to deploy new versions to a staging slot, test them, and then swap with production with zero downtime.
---
## Question 3
How can you configure environment-specific settings in App Service without changing code?


- A) You cannot, settings must be in code
- B) Create different Docker images for each environment
- C) Hardcode them in the application
- D) Use App Settings and Connection Strings in the Azure Portal

**Answer: D**
App Settings and Connection Strings can be configured in the portal and override settings in your configuration files (like appsettings.json).
---
## Question 4
What is CORS and why is it important for APIs hosted in App Service?


- A) A security feature that prevents unauthorized database access
- B) A logging framework for APIs
- C) A method for compressing API responses
- D) Cross-Origin Resource Sharing - allows browsers to make requests to your API from different domains

**Answer: D**
CORS is a browser security feature. Configuring CORS in App Service allows web applications from different domains to call your API.
---
## Question 5
Which authentication option is built into App Service (Easy Auth)?


- A) No authentication is built-in
- B) Only custom JWT validation
- C) Azure AD, Microsoft Account, Facebook, Google, Twitter
- D) Only basic authentication

**Answer: C**
App Service Authentication (Easy Auth) supports multiple identity providers including Azure AD, Microsoft, Facebook, Google, and Twitter without code changes.
---
## Question 6
What is the recommended way to store API secrets like connection strings in App Service?


- A) In Azure Key Vault, referenced via App Settings
- B) In source code
- C) In environment variables on your local machine
- D) In appsettings.json committed to Git

**Answer: A**
Azure Key Vault is the best practice for storing secrets. App Service can reference Key Vault secrets using Key Vault references in App Settings.
---
## Question 7
How does App Service handle HTTP to HTTPS redirection?


- A) Can be enforced through the HTTPS Only setting in App Service configuration
- B) It must be configured manually in code
- C) Not supported, must use Application Gateway
- D) Only available in Premium tiers

**Answer: A**
App Service provides an "HTTPS Only" setting that automatically redirects all HTTP requests to HTTPS.
---
## Question 8
What is the purpose of the Always On setting in App Service?


- A) Enables HTTPS
- B) Keeps your app loaded even when there's no traffic
- C) Enables automatic scaling
- D) Provides 99.99% SLA

**Answer: B**
Always On prevents your app from being unloaded after periods of inactivity, reducing cold start times. It's not available in Free/Shared tiers.
---
## Question 9
Which HTTP methods are typically used in RESTful APIs?


- A) Only GET
- B) SEND and RECEIVE
- C) GET, POST, PUT, PATCH, DELETE
- D) Only GET and POST

**Answer: C**
RESTful APIs typically use GET (read), POST (create), PUT (full update), PATCH (partial update), and DELETE (remove).
---
## Question 10
What is the maximum request timeout for App Service in the default configuration?


- A) 30 seconds
- B) No timeout
- C) 230 seconds (approximately 4 minutes)
- D) 10 minutes

**Answer: C**
By default, Azure App Service has a request timeout of 230 seconds (~4 minutes). For longer operations, consider using async patterns or Azure Functions.