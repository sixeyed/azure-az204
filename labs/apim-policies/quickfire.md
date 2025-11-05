# APIM Policies - Quickfire Questions

## Question 1
What are APIM policies?

- A) Security rules only
- B) XML-based statements that modify API behavior during request/response pipeline
- C) Billing policies
- D) Network policies

**Answer: B**
Policies are XML configurations that execute in sequence to transform, secure, throttle, and control APIs.

---

## Question 2
What are the policy execution sections?

- A) Only request
- B) Inbound, Backend, Outbound, On-Error
- C) Only response
- D) Single section

**Answer: B**
Inbound (before backend), Backend (before/after calling backend), Outbound (before response), On-Error (on exceptions).

---

## Question 3
What does the `set-header` policy do?

- A) Deletes headers only
- B) Adds, replaces, or deletes HTTP headers in requests or responses
- C) Only reads headers
- D) Encrypts headers

**Answer: B**
`set-header` modifies headers: adds new, updates existing, or removes headers from requests/responses.

---

## Question 4
What is the `rate-limit` policy?

- A) Performance optimization
- B) Restricts the number of API calls per time period per subscription
- C) Storage limit
- D) Network bandwidth limit

**Answer: B**
Rate limiting prevents API abuse by restricting calls per subscription (e.g., 100 calls per minute).

---

## Question 5
What is the difference between rate-limit and quota?

- A) No difference
- B) Rate-limit is short-term (per second/minute); quota is long-term (per week/month)
- C) Quota is faster
- D) Rate-limit is deprecated

**Answer: B**
Rate-limit controls burst traffic (short windows). Quota controls total volume over longer periods.

---

## Question 6
What does the `ip-filter` policy do?

- A) Encrypts IPs
- B) Allows or blocks requests from specific IP addresses or ranges
- C) Changes client IP
- D) Logs IP addresses

**Answer: B**
IP filtering whitelists or blacklists IP addresses/ranges for security and access control.

---

## Question 7
What are policy expressions?

- A) Regular expressions only
- B) C# code snippets embedded in policies for dynamic logic
- C) Math expressions
- D) Not supported

**Answer: B**
Policy expressions use C# syntax to access request/response context and execute custom logic dynamically.

---

## Question 8
What does the `json-to-xml` policy do?

- A) Converts JSON to XML format
- B) Validates JSON
- C) Compresses JSON
- D) Encrypts JSON

**Answer: A**
Transforms JSON request/response bodies to XML, useful for legacy backends expecting XML.

---

## Question 9
At what scopes can policies be applied?

- A) Only global
- B) Global, Product, API, Operation
- C) Only operation level
- D) Only API level

**Answer: B**
Policies inherit and can be defined at global (all APIs), product, API, or operation levels.

---

## Question 10
What is the `base` element in policies?

- A) Database base
- B) Placeholder where parent scope policies are executed in policy inheritance
- C) Base URL
- D) Not used

**Answer: B**
`<base />` determines where parent scope policies execute, controlling inheritance and execution order.
