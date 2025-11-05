# Azure Functions HTTP - Quickfire Questions

## Question 1
What is Azure Functions?

- A) A virtual machine service
- B) A serverless compute service that runs code in response to events
- C) A database service
- D) A storage service

**Answer: B**
Azure Functions is a serverless compute platform that executes code in response to triggers without requiring server management.

---

## Question 2
What are the primary hosting plans for Azure Functions?

- A) Consumption Plan, Premium Plan, Dedicated (App Service) Plan
- B) Only Consumption Plan
- C) Free Plan and Enterprise Plan
- D) Basic and Standard Plans

**Answer: A**
Functions can run on Consumption (pay-per-execution), Premium (pre-warmed instances), or Dedicated (App Service Plan) hosting.

---

## Question 3
What is the default timeout for Azure Functions on the Consumption plan?

- A) 30 seconds
- B) 5 minutes (configurable up to 10 minutes)
- C) 30 minutes
- D) No timeout

**Answer: B**
The default is 5 minutes, configurable up to 10 minutes on Consumption plan. Premium and Dedicated plans can have longer timeouts.

---

## Question 4
Which authorization level provides the most security for HTTP triggered functions?

- A) Anonymous
- B) Function
- C) Admin
- D) System

**Answer: B** (or C for admin operations)
Authorization levels: Anonymous (no key), Function (function-specific key), Admin (master key). Function level is secure for regular APIs.

---

## Question 5
How are Azure Function apps scaled in the Consumption plan?

- A) Manually only
- B) Automatically based on incoming event load
- C) Using auto-scale rules
- D) They don't scale

**Answer: B**
The Consumption plan automatically scales by allocating additional compute resources based on the number of incoming events.

---

## Question 6
What is a cold start in Azure Functions?

- A) Starting a function in a cold region
- B) The delay when a function instance is created after being idle
- C) A function error
- D) Restarting a function app

**Answer: B**
Cold start is the latency incurred when creating a new function instance after a period of inactivity. Premium plans reduce this with pre-warmed workers.

---

## Question 7
Which HTTP methods are commonly used with Azure Functions HTTP triggers?

- A) Only GET
- B) GET and POST only
- C) GET, POST, PUT, PATCH, DELETE, and more
- D) Only POST

**Answer: C**
HTTP triggered functions support all standard HTTP methods and can be configured to respond to specific methods.

---

## Question 8
How can you return JSON from an HTTP triggered function in C#?

- A) Convert to string manually
- B) Return an object, Functions serializes it automatically
- C) Use a custom serializer
- D) JSON is not supported

**Answer: B**
Azure Functions automatically serializes return objects to JSON for HTTP responses.

---

## Question 9
What is the purpose of function.json in Azure Functions?

- A) Stores application code
- B) Defines bindings, triggers, and function configuration
- C) Contains deployment settings
- D) Logs function execution

**Answer: B**
function.json defines the function's triggers, input/output bindings, and configuration (for non-.NET languages or out-of-process).

---

## Question 10
How can you access query parameters in an HTTP triggered function?

- A) From the HttpRequest object's Query collection
- B) They are not accessible
- C) Only through configuration
- D) Using environment variables

**Answer: A**
Query parameters are accessed through the HttpRequest.Query collection in C# or req.query in JavaScript/Python.
