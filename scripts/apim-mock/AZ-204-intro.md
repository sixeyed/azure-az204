
Excellent work mocking an API! While mocking itself isn't heavily tested, this lab covers several AZ-204 exam concepts. Let's focus on what you need to know.

The mocked-response policy is important for design-first development. This policy returns predefined responses without calling any backend service. Know that it goes in the inbound section (it must execute before the backend section to bypass the backend call). The exam may present scenarios where backends aren't ready yet and ask how to provide an API to consumers - mocked-response is your answer.

Products and subscriptions control API access and are heavily tested. APIs must belong to at least one product to be accessible via the gateway (unpublished APIs can't be called). Products require subscriptions (with subscription keys) unless you explicitly disable this requirement. Clients authenticate with the Ocp-Apim-Subscription-Key header (or as a query parameter). The exam tests understanding of this access control hierarchy.

JSON Schema for request/response definitions helps APIM validate and document APIs. Know the basic structure: properties define object fields with types (string, integer, boolean, object, array), required arrays list mandatory fields, and $ref syntax references other schemas for reusability. While you won't write complex schemas on the exam, you should recognize valid syntax and understand how schema validation works.

REST principles appear in API design questions. Resource-based URLs (nouns not verbs: /students not /getStudents), correct HTTP methods (GET for reading, POST for creating, PUT/PATCH for updating, DELETE for removing), proper status codes (200 OK, 201 Created, 204 No Content, 404 Not Found, 401 Unauthorized, 403 Forbidden), and idempotency (GET/PUT/DELETE should be idempotent, POST is not). The exam tests whether you know the right method and status code for different operations.

Policy scope and inheritance is critical. Policies can be defined at four levels: Operation (most specific), API, Product, and Global (least specific). The `<base />` tag in policy XML controls whether parent policies execute. Without `<base />` in inbound, API/Product/Global inbound policies don't run. Know that mocked-response typically goes at the operation level because you want different mock responses for different endpoints.

We'll also cover API design best practices, schema validation policies, common exam scenarios about providing APIs before backend implementation, and troubleshooting authentication issues.

Master API design patterns for the AZ-204!
