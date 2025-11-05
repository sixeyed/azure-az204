# Static Website Hosting on Azure Storage - Quickfire Questions

## Question 1
What Azure Storage feature enables static website hosting?

- A) Table Storage
- B) Blob Storage static website hosting
- C) Queue Storage
- D) File Storage

**Answer: B**
Blob Storage has a static website hosting feature that serves HTML, CSS, JavaScript, and media files.

---

## Question 2
What is the special container used for static website hosting?

- A) website
- B) $web
- C) static
- D) public

**Answer: B**
Static content must be uploaded to the $web container, which is automatically created when you enable the feature.

---

## Question 3
What HTTP/HTTPS endpoint is provided for static websites?

- A) Custom domain only
- B) https://<account-name>.z[zone].web.core.windows.net
- C) No HTTPS
- D) Same as blob endpoint

**Answer: B**
A dedicated web endpoint is provided, separate from the blob endpoint, with automatic HTTPS.

---

## Question 4
Can you use custom domains with static websites?

- A) No
- B) Yes, via CNAME mapping and Azure CDN for HTTPS on custom domain
- C) Only with Azure DNS
- D) Only HTTP, not HTTPS

**Answer: B**
Custom domains are supported. For HTTPS on custom domains, use Azure CDN or Azure Front Door.

---

## Question 5
What files can you specify for static website hosting?

- A) No configuration
- B) Index document (e.g., index.html) and optional error document (e.g., 404.html)
- C) Only index.html
- D) Only error pages

**Answer: B**
You configure an index document path (default page) and optional error document path for 404 errors.

---

## Question 6
Does static website hosting support server-side code?

- A) Yes, ASP.NET
- B) No, only static content (HTML, CSS, JS, images)
- C) Yes, PHP
- D) Yes, Node.js

**Answer: B**
Static website hosting serves static files only. For dynamic content, use Azure Functions, App Service, or client-side JavaScript APIs.

---

## Question 7
How can you add a CDN to your static website?

- A) Not possible
- B) Integrate Azure CDN for global distribution, caching, and custom domain HTTPS
- C) Only manual setup
- D) Requires third-party CDN

**Answer: B**
Azure CDN can be configured to cache static website content globally, improving performance and enabling custom domain HTTPS.

---

## Question 8
What is the cost model for static website hosting?

- A) Fixed monthly fee
- B) Based on storage used and data transfer (same as blob storage pricing)
- C) Per page view
- D) Free unlimited

**Answer: B**
You pay for blob storage capacity and outbound data transfer. No additional hosting fees.

---

## Question 9
Can you use Azure Storage static websites with SPAs (Single Page Applications)?

- A) No
- B) Yes, with fallback routing configured to index.html via CDN rewrite rules
- C) Only for simple HTML
- D) Requires App Service

**Answer: B**
SPAs work well with static hosting. Use CDN rewrite rules to route all paths to index.html for client-side routing.

---

## Question 10
How do you enable static website hosting?

- A) It's always enabled
- B) In Azure Portal under storage account > Static website, or via CLI/PowerShell
- C) Requires support ticket
- D) Only through ARM templates

**Answer: B**
Enable via Portal (Storage account > Data management > Static website), Azure CLI, PowerShell, or ARM templates.
