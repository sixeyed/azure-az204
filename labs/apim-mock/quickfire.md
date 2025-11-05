# APIM Mock APIs - Quickfire Questions

## Question 1
What is API mocking in APIM?


- A) Creating API responses without implementing backend logic
- B) Monitoring feature
- C) Security feature
- D) Testing tool only

**Answer: A**
Mock APIs return predefined responses, allowing frontend development and testing without backend implementation.
---
## Question 2
When should you use mock APIs?


- A) During development, design-first approach, testing, demos
- B) Production only
- C) Never
- D) Only for documentation

**Answer: A**
Mock APIs accelerate development, enable parallel frontend/backend work, and facilitate contract testing.
---
## Question 3
How do you create a mock response in APIM?


- A) Only through code
- B) Using mock-response policy to return static or dynamic content
- C) Requires backend service
- D) Not possible

**Answer: B**
The `mock-response` policy returns responses based on examples in API definition without calling backend.
---
## Question 4
Can mock responses be based on request parameters?


- A) Yes, using policy expressions to vary responses based on request
- B) Requires database
- C) No, always static
- D) Only random responses

**Answer: A**
Policy expressions can examine requests and return different mock responses based on headers, query params, etc.
---
## Question 5
What API definition formats support examples for mocking?


- A) Plain text only
- B) No standards support
- C) OpenAPI (Swagger) with response examples
- D) Only custom format

**Answer: C**
OpenAPI/Swagger specifications can include response examples that APIM uses for mock responses.
---
## Question 6
What is design-first API development?


- A) Infrastructure first
- B) Database design first
- C) Defining API contract (OpenAPI spec) before implementation
- D) UI design priority

**Answer: C**
Design-first defines API specification upfront, enabling mocking, stakeholder agreement, and parallel development.
---
## Question 7
Can you transition from mock to real backend seamlessly?


- A) Only manually
- B) Requires complete rebuild
- C) Not possible
- D) Yes, remove/modify mock-response policy to proxy to actual backend

**Answer: D**
Remove mock-response policy or add conditions to switch between mock and real backend without contract changes.
---
## Question 8
What status codes can mock responses return?


- A) Only 200
- B) Only error codes
- C) Only success codes
- D) Any HTTP status code (200, 201, 400, 404, 500, etc.)

**Answer: D**
Mock responses can simulate any HTTP status code and corresponding response bodies for comprehensive testing.
---
## Question 9
How do mock APIs help with API testing?


- A) Security testing only
- B) Provide consistent, controlled responses for automated testing
- C) Only manual testing
- D) They don't

**Answer: B**
Mocks enable predictable responses for automated tests, eliminating backend variability and dependencies.
---
## Question 10
Can multiple response examples be defined?


- A) No examples
- B) Only one example per operation
- C) Yes, multiple examples for different scenarios (success, errors, edge cases)
- D) Unlimited random examples

**Answer: C**
OpenAPI supports multiple examples per response status code, which can be used for different mock scenarios.