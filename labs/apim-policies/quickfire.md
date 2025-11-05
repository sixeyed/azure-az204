# APIM Policies - Quickfire Questions

## Question 1
What are APIM policies?


- A) XML-based statements that modify API behavior during request/response pipeline
- B) Billing policies
- C) Security rules only
- D) Network policies

**Answer: A**
Policies are XML configurations that execute in sequence to transform, secure, throttle, and control APIs.
---
## Question 2
What are the policy execution sections?


- A) Single section
- B) Inbound, Backend, Outbound, On-Error
- C) Only request
- D) Only response

**Answer: B**
Inbound (before backend), Backend (before/after calling backend), Outbound (before response), On-Error (on exceptions).
---
## Question 3
What does the `set-header` policy do?


- A) Adds, replaces, or deletes HTTP headers in requests or responses
- B) Encrypts headers
- C) Only reads headers
- D) Deletes headers only

**Answer: A**
`set-header` modifies headers: adds new, updates existing, or removes headers from requests/responses.
---
## Question 4
What is the `rate-limit` policy?


- A) Storage limit
- B) Network bandwidth limit
- C) Performance optimization
- D) Restricts the number of API calls per time period per subscription

**Answer: D**
Rate limiting prevents API abuse by restricting calls per subscription (e.g., 100 calls per minute).
---
## Question 5
What is the difference between rate-limit and quota?


- A) Rate-limit is deprecated
- B) Quota is faster
- C) No difference
- D) Rate-limit is short-term (per second/minute); quota is long-term (per week/month)

**Answer: D**
Rate-limit controls burst traffic (short windows). Quota controls total volume over longer periods.
---
## Question 6
What does the `ip-filter` policy do?


- A) Encrypts IPs
- B) Logs IP addresses
- C) Changes client IP
- D) Allows or blocks requests from specific IP addresses or ranges

**Answer: D**
IP filtering whitelists or blacklists IP addresses/ranges for security and access control.
---
## Question 7
What are policy expressions?


- A) Math expressions
- B) Regular expressions only
- C) C# code snippets embedded in policies for dynamic logic
- D) Not supported

**Answer: C**
Policy expressions use C# syntax to access request/response context and execute custom logic dynamically.
---
## Question 8
What does the `json-to-xml` policy do?


- A) Validates JSON
- B) Converts JSON to XML format
- C) Compresses JSON
- D) Encrypts JSON

**Answer: B**
Transforms JSON request/response bodies to XML, useful for legacy backends expecting XML.
---
## Question 9
At what scopes can policies be applied?


- A) Global, Product, API, Operation
- B) Only operation level
- C) Only global
- D) Only API level

**Answer: A**
Policies inherit and can be defined at global (all APIs), product, API, or operation levels.
---
## Question 10
What is the `base` element in policies?


- A) Placeholder where parent scope policies are executed in policy inheritance
- B) Not used
- C) Base URL
- D) Database base

**Answer: A**
`<base />` determines where parent scope policies execute, controlling inheritance and execution order.