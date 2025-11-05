# App Service Static Web Apps - Quickfire Questions

## Question 1
What is Azure Static Web Apps designed for?

- A) Server-side applications with complex business logic
- B) Static content with optional serverless APIs
- C) Database-heavy applications
- D) Real-time streaming applications

**Answer: B**
Azure Static Web Apps is optimized for static site generators and SPAs (Single Page Applications) with optional Azure Functions for backend APIs.

---

## Question 2
Which frameworks are commonly used with Static Web Apps?

- A) React, Angular, Vue
- B) Hugo, Jekyll, Gatsby
- C) Blazor WebAssembly
- D) All of the above

**Answer: D**
Static Web Apps supports JavaScript frameworks (React, Angular, Vue), static site generators (Hugo, Jekyll, Gatsby), and Blazor WebAssembly.

---

## Question 3
What is automatically provided when you create a Static Web App from a GitHub repository?

- A) Database
- B) CI/CD pipeline via GitHub Actions
- C) Load balancer
- D) Virtual machine

**Answer: B**
Azure automatically creates a GitHub Actions workflow that builds and deploys your app whenever you push changes.

---

## Question 4
How are APIs implemented in Azure Static Web Apps?

- A) Using App Service
- B) Using Azure Functions
- C) Using Virtual Machines
- D) APIs are not supported

**Answer: B**
Static Web Apps uses Azure Functions for serverless API backends, automatically deployed with your static content.

---

## Question 5
What is the cost of the Free tier for Azure Static Web Apps?

- A) $5 per month
- B) $10 per month
- C) Free with limitations (100 GB bandwidth, 2 custom domains)
- D) Pay per request

**Answer: C**
The Free tier includes hosting for static content and APIs with 100 GB bandwidth per month and support for 2 custom domains.

---

## Question 6
Which feature allows you to preview pull requests before merging?

- A) Deployment slots
- B) Staging environments created automatically for each PR
- C) Traffic Manager
- D) Preview mode

**Answer: B**
Static Web Apps automatically creates a staging environment for each pull request, allowing you to preview changes before merging.

---

## Question 7
How does Static Web Apps handle authentication?

- A) No authentication support
- B) Built-in authentication with pre-configured providers
- C) Only custom authentication
- D) Only Azure AD

**Answer: B**
Static Web Apps provides built-in authentication with providers like GitHub, Azure AD, Twitter, and allows custom OpenID Connect providers.

---

## Question 8
What is the purpose of the `staticwebapp.config.json` file?

- A) Stores environment variables
- B) Configures routing, authentication, and other Static Web App settings
- C) Contains API definitions
- D) Defines database schema

**Answer: B**
The configuration file defines routes, authentication rules, navigation fallbacks, headers, and other app behavior.

---

## Question 9
Where should the API code be located in a Static Web Apps project?

- A) In the /api folder by default
- B) In the /functions folder
- C) In the /backend folder
- D) In the root directory

**Answer: A**
By default, Static Web Apps looks for Azure Functions code in the /api folder, though this can be configured.

---

## Question 10
What is the global distribution feature in Static Web Apps?

- A) Content is deployed to a single region only
- B) Content is automatically distributed across Azure's global CDN
- C) You must manually configure CDN
- D) Global distribution costs extra

**Answer: B**
Static Web Apps automatically distributes your content globally using Azure's CDN, ensuring low latency for users worldwide.
