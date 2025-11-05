# API Management: Mocking New APIs - Exercise Walkthrough

## Prerequisites

Before we begin, make sure you have an existing API Management service from the previous API Management lab. We'll browse to it in the Azure Portal to start creating our new API.

## Exercise 1: Create a New API

Let's start by creating a new API in our API Management service.

In the Azure Portal, navigate to your API Management resource. We'll create a manually defined HTTP API:

- Select "manually defined HTTP API"
- For the name, you can use something like "Student Management API"
- For the URL, enter any base URL you prefer
- For the APIM URL suffix, use "newapi"

This creates the foundation for our API.

## Exercise 2: Define API Objects

Now, let's define the data structures our API will work with. Navigate to the Definitions tab.

### Student Definition

First, we'll create a definition called "Student" using this sample JSON:

```json
{
    "StudentId": 2315125,
    "FullName" : "Test One"
}
```

This represents a basic student object with an ID and full name.

### StudentDetail Definition

Next, create a definition called "StudentDetail" for more detailed student information:

```json
{
    "StudentId": 2315125,
    "CompanyId": 124121,
    "FirstName" : "Test",
    "LastName" : "Two",
    "Courses" : [
        {
            "CourseCode": "AZDEVACAD",
            "Completed" : "22-11"
        },
        {
            "CourseCode": "K8SFUN",
            "Completed" : "21-01"
        }
    ]
}
```

This includes additional fields like company affiliation and course history.

### StudentArray Definition

Finally, create an array definition called "StudentArray" using this payload:

```json
{
    "type": "array",
    "items": {
        "$ref": "#/definitions/Student"
    }
}
```

This defines an array that contains Student objects, which we'll use for list operations.

## Exercise 3: Add Mocked Operations

Now for the core of our lab - adding mocked operations. We'll create four operations that represent a complete CRUD API.

### Operation 1: List Students

Create a GET operation at the URL path "/students":

- HTTP Method: GET
- URL: /students
- Response: 200 OK
- Response type: application/json with StudentArray definition

Add an inbound processing policy using the "mocked-response" policy and select the 200 response code.

When you test this operation, you should get a mocked array of students.

### Operation 2: Create Student

Create a POST operation at "/students":

- HTTP Method: POST
- URL: /students
- Request payload: application/json with StudentDetail definition
- Response: 201 Created
- Response type: application/json with StudentDetail definition

Add the mocked-response policy with the 201 response code.

This simulates creating a new student and returning the created object.

### Operation 3: Get Student

Create a GET operation with a template parameter:

- HTTP Method: GET
- URL: /students/{studentId}
- Template parameter: studentId
- Response 1: 200 OK with StudentDetail definition
- Response 2: 404 Not Found with no payload

Add the mocked-response policy with the 200 response code.

This allows retrieving individual student details by their ID.

### Operation 4: Delete Student

Create a DELETE operation:

- HTTP Method: DELETE
- URL: /students/{studentId}
- Template parameter: studentId
- Response 1: 204 No Content with no payload
- Response 2: 404 Not Found with no payload

Add the mocked-response policy with the 204 response code.

This simulates deleting a student.

Test each operation in the portal to verify you get the correct mocked responses with the appropriate data types.

## Exercise 4: Publish the API

Now let's make our mock API available to consumers.

Add the new API to the "Unlimited" product, then create a subscription for the product. This gives you a subscription key that clients will use to authenticate.

## Exercise 5: Test with curl

Let's test our API from the command line using curl. curl is the standard tool for testing REST APIs - if it works with curl, it will work in any programming language.

Try these commands (replace YOUR-APIM-NAME and YOUR-SUBSCRIPTION-KEY with your actual values):

```bash
# List all students
curl "https://YOUR-APIM-NAME.azure-api.net/newapi/students" \
  -H "Ocp-Apim-Subscription-Key: YOUR-SUBSCRIPTION-KEY"

# Get a specific student
curl "https://YOUR-APIM-NAME.azure-api.net/newapi/students/1234" \
  -H "Ocp-Apim-Subscription-Key: YOUR-SUBSCRIPTION-KEY"
```

You should see the mocked responses with appropriate data structures.

## Exercise 6: Test with Postman

While curl is great for testing, Postman provides a more user-friendly interface for working with REST APIs. You can either install Postman locally or use the web version at web.postman.co.

Import the collection file from "labs/apim-mock/students.postman_collection.json". This collection represents the consumer's expectations for our API.

Navigate to the collection's Variables tab and set:

- baseUrl: Your full API URL (e.g., https://YOUR-APIM-NAME.azure-api.net/newapi)
- apiKey: Your subscription key

Save the collection and try all the operations. Each operation should return the expected response code and response body.

If any operations fail, you'll need to review your API design in APIM to ensure it matches the consumer's expectations.

## Lab Challenge

Here's a question to consider: We've manually created this API spec in the APIM designer, which is easy to do but not easy to share. How could you distribute the API specification to API consumers?

Think about industry-standard formats for API specifications and how APIM can export or expose them.

## Wrap Up

Great work! You've successfully:

- Designed a new API in Azure API Management
- Created data definitions for your API objects
- Implemented mocked operations for all CRUD operations
- Published the API with subscription-based access
- Tested the API using both curl and Postman

This mock API can now be shared with development teams, allowing them to build integrations immediately while the backend implementation is being developed.

Remember, don't delete this API Management instance yet - we'll use it in upcoming labs!
