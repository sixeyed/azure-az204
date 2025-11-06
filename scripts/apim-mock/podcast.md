# API Management: Mocking New APIs - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on mocking APIs with Azure API Management. Today we're exploring how APIM can help you design and publish mock APIs before the actual backend implementation is complete. Whether you're preparing for the Azure AZ-204 certification or working on real projects, understanding API mocking is valuable for enabling parallel development and reducing time to market.

## The API Design Challenge

When designing new APIs, you typically have a three-way discussion between the API architect who ensures the API follows best practices and patterns, the data owner who knows what data is available and how to access it, and the API consumer who knows what information they need to build their application.

This collaborative approach ensures that the API adheres to best practices, consumers get the information they need, and the data required is actually available from backend systems. But there's a problem: the time between API design and actual delivery can be quite long. Backend teams need time to implement data access, business logic, security, and all the other components of a production API.

This delay creates a bottleneck. Frontend teams can't start development until the backend is ready. Mobile app developers can't build features until they have a working API. Integration partners can't test their systems until the API exists.

## The Power of Mock APIs

This is where API mocking becomes invaluable. A mock API is a real API service that has all the operations agreed upon in the design phase, returns dummy data instead of real data, allows development teams to program against it immediately, and prevents delays while waiting for backend implementation.

The key insight is that for many development tasks, it doesn't matter whether the data is real or fake. If you're building a user interface to display a list of students, you can do most of your work with mock data. If you're writing code to parse API responses, mock responses work just as well as real ones. If you're testing error handling, mock 404 responses are just as useful as real ones.

API mocking enables parallel development. Frontend teams can work with the mock API while backend teams implement the actual data services. Integration partners can test their systems while you build yours. QA teams can write automated tests before features are complete.

## Azure API Management for Mocking

Azure API Management is perfect for creating mock APIs. APIM isn't just a gateway for existing APIs - it's also a design tool for new APIs. You can define API operations, create data schemas, specify responses, and publish a fully functional mock API, all without writing a single line of backend code.

The mocked-response policy in APIM automatically generates realistic dummy data based on your schema definitions. You define what your API responses should look like, and APIM generates sample data that matches those definitions. This provides a much richer experience than simple static responses.

## Designing a Mock API

Let me walk you through the process of creating a mock API from scratch.

First, you create a new API in your API Management service. You can create a manually defined HTTP API, which gives you full control over the design. You provide a name like "Student Management API" and a URL suffix that becomes part of the public URL path.

At this point, your API exists but has no operations. The next step is defining your data structures.

## Defining Data Schemas

APIs work with structured data, typically in JSON format. Before you can define operations, you need to define what your data looks like. APIM uses JSON Schema, which is the standard way to describe JSON structures.

You might create a basic Student definition with just an ID and a name, representing what you'd return when listing students. You might create a more detailed StudentDetail definition with first name, last name, company ID, and an array of courses with codes and completion dates. This richer structure is what you'd return when someone requests a specific student's details.

You can also create array definitions. Instead of sample JSON, you use a schema that specifies type as array and references your Student definition. This defines an array that contains Student objects.

These definitions serve two purposes. First, they document your API's data structures. Second, they enable APIM to generate realistic mock data automatically.

## Creating Mocked Operations

Now comes the fun part - adding mocked operations. Let's create a complete CRUD API with Create, Read, Update, and Delete operations.

For listing students, you create a GET operation at the URL path "/students". For the response, you specify a 200 OK status with the StudentArray definition. Then you add an inbound processing policy using the mocked-response policy, selecting the 200 response code. This tells APIM to automatically generate and return mock data.

When you test this operation, you get a mocked array of students with realistic-looking data generated from your schema. Each student has an ID and name, and the values look like real data, not just placeholders.

For creating a student, you create a POST operation at "/students". You specify the request payload using the StudentDetail definition - this is what clients will send. For the response, you add a 201 Created status with the StudentDetail definition - this simulates returning the created object, which is the standard REST pattern for POST operations. You add the mocked-response policy with the 201 status code.

This simulates the complete create operation. A client can send a POST request with student data, and they receive a response as if the student was created in a real database.

For retrieving individual students, you create a GET operation with a template parameter in the URL path: "/students/{studentId}". The curly braces indicate a parameter that gets captured from the URL. You add two responses: 200 OK with the StudentDetail definition for successful retrieval, and 404 Not Found with no payload for when a student doesn't exist. You add the mocked-response policy with the 200 status code.

This allows retrieving individual student details by their ID. The URL might be "/students/1234", and the API returns detailed information about student 1234.

For deletion, you create a DELETE operation at "/students/{studentId}". You add responses for 204 No Content for successful deletion and 404 Not Found for when the student doesn't exist. The mocked-response policy returns 204.

The 204 No Content status code is the standard response for successful DELETE operations. It means the operation succeeded, but there's no content to return because the resource was deleted.

## Publishing the Mock API

Once your operations are defined, you need to make the API available to consumers. In APIM, you do this by adding the API to a product. Products are how you bundle APIs and control access.

You might add your API to the "Unlimited" product, which is a default product in APIM. Then you create a subscription for the product. This gives you a subscription key that clients will use to authenticate their requests.

Now your mock API is fully functional and accessible. Consumers can make requests, and they receive realistic mock responses based on your definitions.

## Testing with Command Line Tools

Let's test the mock API using curl, which is the standard command-line tool for testing REST APIs. If an API works with curl, it will work in any programming language.

To list all students, you make a GET request to your APIM URL at "/newapi/students", passing the subscription key in the "Ocp-Apim-Subscription-Key" header. The response shows a mocked array of student objects with realistic data.

To get a specific student, you make a GET request to "/newapi/students/1234", again with the subscription key header. The response shows a mocked StudentDetail with complete student information.

The responses demonstrate that APIM is generating realistic mock data based on your schema definitions, not just returning static responses.

## Testing with Postman

While curl is great for quick tests, Postman provides a more user-friendly interface for working with REST APIs. Postman is an application for testing, documenting, and sharing APIs.

You can import a collection file that represents the consumer's expectations for your API - what endpoints they expect to call and what responses they expect to receive. You configure variables for your base URL and API key, then run the requests.

Each operation should return the expected response code and body. If any operations fail, you need to review your API design in APIM to ensure it matches the consumer's expectations. This is the value of mock APIs - finding these mismatches early, before backend implementation begins.

## The Contract Testing Benefit

This testing with Postman demonstrates an important concept called contract testing. The Postman collection represents the contract - what the consumer expects from your API. By testing your mock API against this contract, you verify that your API design meets consumer needs.

If the backend team later implements the API differently, you can test the real API against the same contract. Any failures indicate that the implementation doesn't match the design, which is a problem you need to fix.

This approach prevents a common problem in API development: the backend team builds what they think the consumers need, only to discover later that consumers expected something different. Mock APIs let you validate the contract before implementation begins.

## Sharing API Specifications

One challenge with designing APIs in APIM is sharing the specification with other teams or external partners. APIM provides a solution through OpenAPI support.

OpenAPI, formerly known as Swagger, is the industry-standard format for describing REST APIs. APIM can export your API definition in OpenAPI format. This exported specification can be imported into tools like Postman, used to generate client libraries in various programming languages, and shared as documentation.

This makes your API design portable and enables tooling. Consumers don't need access to your APIM instance to understand your API - they just need the OpenAPI specification.

## Relevance to the AZ-204 Exam

Understanding API mocking with APIM is important for the Azure AZ-204 Developer Associate certification. Let me connect these concepts to specific exam objectives.

### Implementing API Management

The exam tests your knowledge of creating and configuring APIs in APIM, understanding the APIM service structure, working with products and subscriptions, and managing API access through subscription keys.

This lab covers all of these through hands-on work with a complete mock API.

### API Design and Operations

The exam expects you to understand how to define API operations using different HTTP methods, work with URL paths and template parameters, define request and response schemas, and use appropriate HTTP status codes.

Understanding when to use GET versus POST versus DELETE, knowing that 200 means success and 404 means not found and 201 means created - these are fundamental concepts the exam tests.

### APIM Policies

A crucial concept tested in the exam is policy management. The mocked-response policy is one of many policies available in APIM. Understanding inbound processing policies, knowing when and why to use mock responses, and being able to apply policies to operations are all exam topics.

### REST API Principles

The AZ-204 exam assumes foundational knowledge of REST APIs. Resource-based URL design like "/students" and "/students/{id}", appropriate use of HTTP methods, status code meanings, and JSON as the standard data format are all prerequisites.

### Common Exam Scenarios

Let me share typical scenarios you might encounter on the exam.

"A development team needs to test their application against an API that hasn't been implemented yet. Which APIM policy should you use?" The answer is the mocked-response policy, which allows you to return predefined responses without calling a backend service.

"How do you control access to APIs in Azure API Management?" The answer is that APIs are added to products, and consumers subscribe to products to receive subscription keys for authentication.

"What format does APIM use for defining API request and response schemas?" The answer is JSON Schema definitions, which can reference other definitions using the ref syntax.

"Which HTTP header is used to authenticate requests to an APIM-hosted API?" The answer is the "Ocp-Apim-Subscription-Key" header, which contains the subscription key for authentication.

## Real-World Applications

Beyond the exam, API mocking teaches skills you'll use in production scenarios.

### Enabling Parallel Development

In real projects, frontend and backend teams often work simultaneously. Mock APIs allow frontend teams to start development immediately without waiting for backend implementation, reducing overall project timelines. Mobile developers can build features, web developers can create interfaces, and integration partners can test their systems, all in parallel.

### API-First Design

Modern development favors designing APIs before implementing them. This ensures clear contracts between services, agreement on data structures and operations, better collaboration between teams, and reduced integration issues.

When everyone agrees on the API design upfront, and that design is validated with a working mock API, implementation becomes much smoother. Backend teams know exactly what to build. Frontend teams know exactly what to expect.

### Contract Testing

Mock APIs serve as the source of truth for API contracts. Teams can validate that implementations match specifications, test error scenarios like 404 responses, verify data structures and types, and ensure consistent behavior.

This reduces bugs and integration issues because problems are caught early when they're cheaper to fix.

## Key Takeaways

Let me summarize the essential points about mocking APIs with Azure API Management.

Mock APIs enable parallel development by allowing consumers to work with realistic API responses before backend implementation is complete. APIM makes creating mock APIs easy through manual API definition, JSON Schema for data structures, the mocked-response policy for generating realistic data, and products and subscriptions for access control.

The development workflow follows this pattern: design the API collaboratively with architects, data owners, and consumers, define data schemas using JSON Schema, create operations with mocked responses, publish the API through products, share the OpenAPI specification with consumers, and let teams work in parallel while backend is implemented.

For the AZ-204 exam, understand how to create APIs in APIM, define operations with different HTTP methods and status codes, use JSON Schema for request and response definitions, apply the mocked-response policy, manage products and subscriptions, and share APIs using OpenAPI specifications.

REST API principles tested on the exam include resource-based URL design, appropriate HTTP methods, meaningful status codes, and JSON for data exchange.

## Final Thoughts

API mocking with Azure API Management is a powerful technique for modern API development. It breaks the dependency between API design and implementation, enabling teams to work in parallel and validate contracts early.

For the AZ-204 exam, understanding mock APIs is part of the broader API Management domain, which represents 20 to 25 percent of the exam. The exam tests both theoretical knowledge and practical skills, so hands-on practice is essential.

As you prepare, create mock APIs yourself. Define schemas, create operations, test with curl and Postman, and export OpenAPI specifications. This practical experience will help you understand the concepts deeply and recognize correct answers on the exam.

Remember that the exam focuses on practical skills. Understanding how to actually implement these solutions is more important than memorizing facts. Practice, experiment, and build real mock APIs to solidify your knowledge.

Thanks for listening to this episode on mocking APIs with Azure API Management. I hope this gives you a clear understanding of how to use APIM for API-first development and how these concepts relate to the AZ-204 certification. Good luck with your studies!
