
We've covered the design-first approach where mocking enables teams to publish fully functional APIs with dummy data before backend implementation. Now let's design and mock a complete API.

You'll manually create an HTTP API in your existing APIM instance - this time not importing from a backend, but designing from scratch. Then you'll define three data schemas using JSON Schema: Student (simple object with id, name, email), StudentDetail (extended object with additional fields), and StudentArray (collection using $ref to reference the Student schema). This demonstrates proper schema design with reusable components.

Next comes the core of mocking: implementing four CRUD operations. You'll create GET /students returning an array of mock students (200 OK), POST /students creating a new student (201 Created), GET /students/{studentId} returning a single student (200 OK or 404 Not Found for invalid IDs), and DELETE /students/{studentId} deleting a student (204 No Content). Each operation uses the mocked-response policy with appropriate HTTP status codes and dummy JSON data.

You'll add the API to a product because APIs must belong to at least one product to be accessible. Then you'll test with curl using the Ocp-Apim-Subscription-Key header - try without the key and get rejected (401 Unauthorized), then with a valid subscription key and see your mock responses.

Finally, you'll import a Postman collection to validate that your mock API matches consumer expectations. This simulates the real-world scenario where frontend teams build against your mock API while backend teams implement the actual data services. If the mock matches the contract, integration should be seamless when the real backend is ready.

Let's design and mock an API!
