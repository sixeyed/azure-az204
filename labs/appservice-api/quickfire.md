# App Service API - Quickfire Questions

## Question 1
What is the primary benefit of using App Service for REST APIs?

- A) It only supports .NET applications
- B) It provides automatic API documentation
- C) It offers managed infrastructure with built-in scaling, security, and deployment features
- D) It requires no configuration

**Answer: C**
App Service provides a fully managed platform for hosting APIs with features like auto-scaling, SSL, deployment slots, and integrated authentication.

---

## Question 2
Which App Service feature allows you to test new API versions before directing production traffic to them?

- A) API Gateway
- B) Deployment slots
- C) Traffic Manager
- D) Load Balancer

**Answer: B**
Deployment slots allow you to deploy new versions to a staging slot, test them, and then swap with production with zero downtime.

---

## Question 3
How can you configure environment-specific settings in App Service without changing code?

- A) Hardcode them in the application
- B) Use App Settings and Connection Strings in the Azure Portal
- C) Create different Docker images for each environment
- D) You cannot, settings must be in code

**Answer: B**
App Settings and Connection Strings can be configured in the portal and override settings in your configuration files (like appsettings.json).

---

## Question 4
What is CORS and why is it important for APIs hosted in App Service?

- A) A security feature that prevents unauthorized database access
- B) Cross-Origin Resource Sharing - allows browsers to make requests to your API from different domains
- C) A method for compressing API responses
- D) A logging framework for APIs

**Answer: B**
CORS is a browser security feature. Configuring CORS in App Service allows web applications from different domains to call your API.

---

## Question 5
Which authentication option is built into App Service (Easy Auth)?

- A) Only custom JWT validation
- B) Azure AD, Microsoft Account, Facebook, Google, Twitter
- C) Only basic authentication
- D) No authentication is built-in

**Answer: B**
App Service Authentication (Easy Auth) supports multiple identity providers including Azure AD, Microsoft, Facebook, Google, and Twitter without code changes.

---

## Question 6
What is the recommended way to store API secrets like connection strings in App Service?

- A) In source code
- B) In appsettings.json committed to Git
- C) In Azure Key Vault, referenced via App Settings
- D) In environment variables on your local machine

**Answer: C**
Azure Key Vault is the best practice for storing secrets. App Service can reference Key Vault secrets using Key Vault references in App Settings.

---

## Question 7
How does App Service handle HTTP to HTTPS redirection?

- A) It must be configured manually in code
- B) Can be enforced through the HTTPS Only setting in App Service configuration
- C) Not supported, must use Application Gateway
- D) Only available in Premium tiers

**Answer: B**
App Service provides an "HTTPS Only" setting that automatically redirects all HTTP requests to HTTPS.

---

## Question 8
What is the purpose of the Always On setting in App Service?

- A) Keeps your app loaded even when there's no traffic
- B) Enables automatic scaling
- C) Provides 99.99% SLA
- D) Enables HTTPS

**Answer: A**
Always On prevents your app from being unloaded after periods of inactivity, reducing cold start times. It's not available in Free/Shared tiers.

---

## Question 9
Which HTTP methods are typically used in RESTful APIs?

- A) Only GET and POST
- B) GET, POST, PUT, PATCH, DELETE
- C) Only GET
- D) SEND and RECEIVE

**Answer: B**
RESTful APIs typically use GET (read), POST (create), PUT (full update), PATCH (partial update), and DELETE (remove).

---

## Question 10
What is the maximum request timeout for App Service in the default configuration?

- A) 30 seconds
- B) 230 seconds (approximately 4 minutes)
- C) 10 minutes
- D) No timeout

**Answer: B**
By default, Azure App Service has a request timeout of 230 seconds (~4 minutes). For longer operations, consider using async patterns or Azure Functions.
