# API Management: Mocking New APIs - Exercise Walkthrough

## Prerequisites

Before we begin, make sure you have an existing API Management service from the previous API Management lab. We'll browse to it in the Azure Portal to start creating our new API.

## Create a New API

Let's start by creating a new API in our API Management service.

**Navigate to APIM**: In the Azure Portal, we're navigating to your API Management resource. This is where all your APIs are centrally managed.

**Create the API**: We're creating a manually defined HTTP API. This gives us full control over the API design without needing a backend service yet. For the name, you can use something like "Student Management API" or any descriptive name. For the URL, enter any base URL you prefer - this doesn't matter much for mocking. For the APIM URL suffix, we're using "newapi" - this becomes part of the public URL path.

This creates the foundation for our API, and now we can define what operations it supports.

## Define API Objects

Now, let's define the data structures our API will work with. We're navigating to the Definitions tab where we can model our data schemas.

**Student Definition**: First, we'll create a definition called "Student" using a sample JSON structure. The JSON has a StudentId set to 2315125 and a FullName of "Test One". This represents a basic student object with an ID and full name - a simple structure for listing students.

**StudentDetail Definition**: Next, we're creating a definition called "StudentDetail" for more detailed student information. This JSON includes StudentId, CompanyId for their employer or organization, FirstName and LastName split out separately, and a Courses array containing course history. Each course has a CourseCode like "AZDEVACAD" and a Completed date like "22-11". This richer structure is what we'd return when someone requests a specific student's details.

**StudentArray Definition**: Finally, we're creating an array definition called "StudentArray". Instead of using sample JSON, we're using a schema definition with type set to "array" and items referencing our Student definition. This defines an array that contains Student objects, which we'll use for list operations. The reference syntax links to the Student definition we created earlier.

## Add Mocked Operations

Now for the core of our lab - adding mocked operations. We'll create four operations that represent a complete CRUD API - Create, Read, Update, and Delete.

**Operation 1: List Students**: We're creating a GET operation at the URL path "/students". This represents listing all students. For the response, we're adding a 200 OK status with response type application/json using the StudentArray definition. Now we're adding an inbound processing policy using the "mocked-response" policy and selecting the 200 response code. This tells APIM to automatically generate and return mock data based on our StudentArray definition.

When you test this operation in the portal, you should get a mocked array of students with realistic-looking data generated from our schema.

**Operation 2: Create Student**: We're creating a POST operation at "/students". This simulates creating a new student. For the request payload, we're specifying application/json with the StudentDetail definition - this is what clients will send. For the response, we're adding a 201 Created status with response type application/json using the StudentDetail definition - this simulates returning the created object. We're adding the mocked-response policy with the 201 response code.

This simulates creating a new student and returning the created object, which is the standard REST pattern for POST operations.

**Operation 3: Get Student**: We're creating a GET operation with a template parameter in the URL. The path is "/students/{studentId}" with a template parameter called "studentId". This captures the ID from the URL. We're adding two responses: Response 1 is 200 OK with StudentDetail definition for successful retrieval, and Response 2 is 404 Not Found with no payload for when a student doesn't exist. We're adding the mocked-response policy with the 200 response code.

This allows retrieving individual student details by their ID, which is a fundamental REST operation.

**Operation 4: Delete Student**: We're creating a DELETE operation at "/students/{studentId}" with the same template parameter. We're adding two responses: Response 1 is 204 No Content with no payload for successful deletion, and Response 2 is 404 Not Found with no payload for when the student doesn't exist. We're adding the mocked-response policy with the 204 response code.

This simulates deleting a student, using 204 No Content which is the standard response for successful DELETE operations.

**Test the Operations**: We're testing each operation in the portal to verify you get the correct mocked responses with the appropriate data types and status codes.

## Publish the API

Now let's make our mock API available to consumers.

**Add to Product**: We're adding the new API to the "Unlimited" product. Products in APIM are how you bundle APIs and control access. Then we're creating a subscription for the product. This gives you a subscription key that clients will use to authenticate their requests.

## Test with curl

Let's test our API from the command line using curl. curl is the standard tool for testing REST APIs - if it works with curl, it will work in any programming language.

**List All Students**: We're running curl to make a GET request to your APIM URL at /newapi/students, passing the subscription key in the Ocp-Apim-Subscription-Key header. You should see the mocked response with an array of student objects.

**Get a Specific Student**: We're running curl to get /newapi/students/1234, again with the subscription key header. You should see a mocked StudentDetail response with complete student information.

The responses demonstrate that APIM is generating realistic mock data based on your schema definitions.

## Test with Postman

While curl is great for testing, Postman provides a more user-friendly interface for working with REST APIs. You can either install Postman locally or use the web version at web.postman.co.

**Import the Collection**: We're importing the collection file from "labs/apim-mock/students.postman_collection.json". This collection represents the consumer's expectations for our API - what endpoints they expect to call and what responses they expect to receive.

**Configure Variables**: We're navigating to the collection's Variables tab and setting baseUrl to your full API URL like https://YOUR-APIM-NAME.azure-api.net/newapi, and apiKey to your subscription key.

**Run the Requests**: We're saving the collection and trying all the operations. Each operation should return the expected response code and response body. If any operations fail, you'll need to review your API design in APIM to ensure it matches the consumer's expectations - this is the value of mock APIs, finding these mismatches early.

## Lab Challenge

Here's a question to consider: We've manually created this API spec in the APIM designer, which is easy to do but not easy to share with other teams or external partners. How could you distribute the API specification to API consumers so they can generate client libraries or test their integrations?

Think about industry-standard formats for API specifications - APIM supports exporting APIs in OpenAPI (Swagger) format, which can be imported into tools like Postman, used to generate client libraries in various languages, and shared as documentation. Explore the export options in APIM to see how you can share your API definition.

## Reference

- [Mock API responses in APIM](https://docs.microsoft.com/azure/api-management/mock-api-responses)
- [API definitions and schemas](https://docs.microsoft.com/azure/api-management/api-management-howto-add-operations)
- [APIM products](https://docs.microsoft.com/azure/api-management/api-management-howto-add-products)

## Wrap Up

Great work! You've successfully designed a new API in Azure API Management, created data definitions for your API objects, implemented mocked operations for all CRUD operations, published the API with subscription-based access, and tested the API using both curl and Postman.

This mock API can now be shared with development teams, allowing them to build integrations immediately while the backend implementation is being developed. This parallel development approach can significantly reduce time to market.

Remember, don't delete this API Management instance yet - we'll use it in upcoming labs to explore policies, versioning, and other advanced features!
