# APIM Mock APIs - Quickfire Questions

## Question 1
What is API mocking in APIM?

- A) Testing tool only
- B) Creating API responses without implementing backend logic
- C) Security feature
- D) Monitoring feature

**Answer: B**
Mock APIs return predefined responses, allowing frontend development and testing without backend implementation.

---

## Question 2
When should you use mock APIs?

- A) Production only
- B) During development, design-first approach, testing, demos
- C) Never
- D) Only for documentation

**Answer: B**
Mock APIs accelerate development, enable parallel frontend/backend work, and facilitate contract testing.

---

## Question 3
How do you create a mock response in APIM?

- A) Requires backend service
- B) Using mock-response policy to return static or dynamic content
- C) Not possible
- D) Only through code

**Answer: B**
The `mock-response` policy returns responses based on examples in API definition without calling backend.

---

## Question 4
Can mock responses be based on request parameters?

- A) No, always static
- B) Yes, using policy expressions to vary responses based on request
- C) Only random responses
- D) Requires database

**Answer: B**
Policy expressions can examine requests and return different mock responses based on headers, query params, etc.

---

## Question 5
What API definition formats support examples for mocking?

- A) No standards support
- B) OpenAPI (Swagger) with response examples
- C) Only custom format
- D) Plain text only

**Answer: B**
OpenAPI/Swagger specifications can include response examples that APIM uses for mock responses.

---

## Question 6
What is design-first API development?

- A) UI design priority
- B) Defining API contract (OpenAPI spec) before implementation
- C) Database design first
- D) Infrastructure first

**Answer: B**
Design-first defines API specification upfront, enabling mocking, stakeholder agreement, and parallel development.

---

## Question 7
Can you transition from mock to real backend seamlessly?

- A) Requires complete rebuild
- B) Yes, remove/modify mock-response policy to proxy to actual backend
- C) Not possible
- D) Only manually

**Answer: B**
Remove mock-response policy or add conditions to switch between mock and real backend without contract changes.

---

## Question 8
What status codes can mock responses return?

- A) Only 200
- B) Any HTTP status code (200, 201, 400, 404, 500, etc.)
- C) Only success codes
- D) Only error codes

**Answer: B**
Mock responses can simulate any HTTP status code and corresponding response bodies for comprehensive testing.

---

## Question 9
How do mock APIs help with API testing?

- A) They don't
- B) Provide consistent, controlled responses for automated testing
- C) Only manual testing
- D) Security testing only

**Answer: B**
Mocks enable predictable responses for automated tests, eliminating backend variability and dependencies.

---

## Question 10
Can multiple response examples be defined?

- A) Only one example per operation
- B) Yes, multiple examples for different scenarios (success, errors, edge cases)
- C) No examples
- D) Unlimited random examples

**Answer: B**
OpenAPI supports multiple examples per response status code, which can be used for different mock scenarios.
