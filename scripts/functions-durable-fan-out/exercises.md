# Azure Durable Functions: Fan-Out/Fan-In Pattern - Lab Exercises

**Duration:** 15-20 minutes
**Format:** Step-by-step walkthrough with conversational narration

---

## Introduction to the Lab

Welcome to the hands-on portion of our Azure Durable Functions lab! In this exercise, we're going to implement the fan-out/fan-in pattern to build a real-world quote engine. This is an improvement over a simpler Service Bus function implementation, because now we'll actually wait for all supplier responses and intelligently select the best quote.

Let's start by understanding what we're building, then we'll test it locally, and finally deploy it to Azure.

---

## Understanding the Code Structure

Before we run anything, let's take a quick tour of the code we'll be working with. You'll find everything in the QuoteEngine folder.

*[SHOW ON SCREEN: QuoteEngine folder structure]*

First, we have the HTTP Orchestrator Start function. This is our entry point. It uses an HTTP trigger, which means we can call it with a simple HTTP request. When we do that, it starts the durable orchestration and immediately returns a set of URLs that we can use to check on the status of our long-running function. This is really useful because we don't have to keep a connection open while waiting for results.

*[SHOW ON SCREEN: QuoteOrchestrator.cs file]*

Next, we have the Quote Orchestrator. This is where the magic happens. The orchestrator calls three different supplier quote activities asynchronously, which means they all run in parallel. Then it waits for all of them to complete using Task.WhenAll. This is incredibly efficient because the total duration is only as long as the slowest supplier call, not the sum of all three.

*[SHOW ON SCREEN: Activities folder with Supplier functions]*

And then we have our activity functions, one for each supplier. They're all similar, they generate a random quote price and return it in a response object. One of them has a deliberate delay built in, so we can see that the orchestrator patiently waits for even the slowest service to respond.

Once all the quotes are in, the orchestrator selects the one with the best price and returns that as the final result.

---

## Setting Up the Local Environment

Alright, let's get this running on your local machine first. Before we can test the function, we need a storage account, because durable functions persist their state in Azure Storage.

The good news is we don't need to create anything in Azure for local testing. We can use the Azure Storage emulator called Azurite.

*[SHOW ON SCREEN: Docker Desktop application]*

Make sure Docker Desktop is running on your machine. Then open a terminal and let's start Azurite.

*[SHOW ON SCREEN: Terminal window]*

Type or paste this command:

```
docker run -d -p 10000-10002:10000-10002 --name azurite mcr.microsoft.com/azure-storage/azurite
```

*[PAUSE for command execution]*

Perfect! Azurite is now running in the background, emulating Azure Storage on your local machine. This container exposes the storage endpoints on ports ten thousand through ten thousand and two.

---

## Creating the Local Configuration

Now we need to create a local settings file so our function knows how to connect to the storage emulator.

*[SHOW ON SCREEN: File explorer or VS Code]*

Navigate to your labs folder, then functions-durable, then fan-out, and into the QuoteEngine folder. We need to create a file called local.settings.json.

*[SHOW ON SCREEN: local.settings.json file being created]*

This file contains our local configuration. Let me explain what's in here. The IsEncrypted setting is false because we're working locally. Then we have our Values section with two important settings.

AzureWebJobsStorage is set to "UseDevelopmentStorage=true" which tells the function to use our local Azurite emulator instead of a real Azure Storage account. And FUNCTIONS_WORKER_RUNTIME is set to "dotnet" because this is a .NET function.

*[SHOW ON SCREEN: The complete JSON structure]*

Notice we're not putting any real connection strings or credentials in here. For local development, that simple placeholder is all we need.

---

## Running the Function Locally

Time to run our function! In your terminal, make sure you're in the QuoteEngine directory.

*[SHOW ON SCREEN: Terminal with current directory shown]*

Type:

```
func start
```

*[PAUSE for function startup]*

Great! The Azure Functions runtime is now starting up. You'll see it discover all the functions in our project. There's the HTTP Orchestrator Start function, the Quote Orchestrator, and all three supplier activity functions.

*[SHOW ON SCREEN: Function list output with the HTTP endpoint URL]*

Look for the HTTP trigger URL in the output. You should see something like "HttpOrchestratorStart: [GET,POST]" followed by a localhost URL on port seven zero seven one. That's the endpoint we'll call to start our orchestration.

---

## Triggering the Orchestration

Now let's trigger the orchestration! Open a second terminal window so you can keep an eye on the function logs in the first one.

*[SHOW ON SCREEN: Second terminal window]*

In your new terminal, we'll use curl to call the HTTP trigger:

```
curl http://localhost:7071/api/HttpOrchestratorStart
```

*[PAUSE for execution]*

Excellent! Now look at your first terminal where the function is running.

*[SHOW ON SCREEN: Function terminal with orchestrator logs]*

You should see the orchestrator logs showing all three suppliers being called. Notice they all start executing at almost exactly the same time? That's the fan-out happening. Each supplier is calculating a quote in parallel. You'll see messages like "SUPPLIER-1 calculating price for quote ID" and then "SUPPLIER-1 calculated quote" with a random price.

The key thing to notice is that even though one supplier has a delay, the orchestrator waits for all of them before proceeding. That's the fan-in part of the pattern.

---

## Understanding the Status URLs

Now look at your curl terminal where you made the request.

*[SHOW ON SCREEN: JSON response with multiple URLs]*

You should see a JSON response full of URLs. Don't worry, you're not expected to memorize these! This is what an HTTP-triggered durable function returns: a set of management URLs.

The most important one is the statusQueryGetUri. This is the URL you can call to check on the progress of your orchestration. You'd typically use this in a web application to show progress to users, or to retrieve the final results once the function completes.

There's also a sendEventPostUri for sending external events to the running orchestration, and other URLs for terminating or managing the instance. This gives you complete control over your long-running functions.

---

## Checking the Orchestration Status

Let's use that status URL to see our results. Copy the statusQueryGetUri from your response, and make another curl request.

*[SHOW ON SCREEN: Terminal showing curl command with the status URL]*

*[NOTE: The actual URL will be unique to each execution]*

Paste in your specific URL and run it:

```
curl "http://localhost:7071/runtime/webhooks/durabletask/instances/<instance-id>?..."
```

*[PAUSE for execution]*

*[SHOW ON SCREEN: Status response JSON]*

Fantastic! The response shows you everything about your orchestration. You can see the runtime status is "Completed", which means all the suppliers have responded and the orchestrator has finished its work.

Look at the input section, it shows the quote request that was generated, with a quote ID, product code, and quantity.

And here's the important part: the output section. This contains the winning quote! You can see which supplier had the best price. In this example, it might be SUPPLIER-3 with a quote of two hundred fifty-six dollars. Your numbers will be different because the quotes are randomly generated.

You can also see timing information: when the orchestration was created and when it last updated. If you called this URL while the suppliers were still working, you'd see a runtime status of "Running" instead of "Completed".

---

## Deploying to Azure

Now that we've seen it working locally, let's deploy this to Azure! First, we need to create the Azure resources.

*[SHOW ON SCREEN: Terminal for Azure CLI commands]*

We'll start by creating a resource group:

```
az group create -n labs-functions-durable-fan-out --tags courselabs=azure -l eastus
```

*[PAUSE for execution]*

Next, we need a storage account. Remember, durable functions need storage to persist their state. Choose a unique name for your storage account.

*[SHOW ON SCREEN: Command with placeholder]*

```
az storage account create -g labs-functions-durable-fan-out --sku Standard_LRS -l eastus -n <your-storage-name>
```

Replace the placeholder with your unique storage account name. Storage account names must be globally unique and can only contain lowercase letters and numbers.

*[PAUSE for execution]*

Great! Now let's create the Function App itself:

```
az functionapp create -g labs-functions-durable-fan-out --runtime dotnet --functions-version 4 --consumption-plan-location eastus --storage-account <your-storage-name> -n <your-function-name>
```

*[SHOW ON SCREEN: Command with placeholders highlighted]*

Again, replace the placeholders with your storage account name and choose a unique name for your function app.

*[PAUSE for execution]*

Perfect! Your Function App is created. One of the great things about this example is that we don't have any external dependencies. We're not using Service Bus, Cosmos DB, or any other services. The function is completely self-contained, which makes deployment really simple.

---

## Publishing the Function

Now we'll publish our code to Azure using the Azure Functions Core Tools:

```
func azure functionapp publish <your-function-name>
```

*[PAUSE for deployment]*

*[SHOW ON SCREEN: Deployment progress output]*

The tools are packaging your function, uploading it to Azure, and setting everything up. This might take a minute or two.

*[SHOW ON SCREEN: Deployment success message with function URLs]*

Excellent! Look at the output. You should see the HTTP trigger URL, but this time it's a public Azure URL, not localhost. Copy that URL because we're going to test it.

---

## Testing in Azure

Let's verify that our function works in Azure just like it did locally. Use curl with your Azure function URL:

*[SHOW ON SCREEN: Terminal with curl command to Azure URL]*

```
curl https://<your-function-name>.azurewebsites.net/api/HttpOrchestratorStart
```

*[PAUSE for execution]*

You should get the same type of JSON response with status URLs, but this time they're all Azure URLs. Copy the statusQueryGetUri and call it to see your results.

*[SHOW ON SCREEN: Status query results]*

Perfect! The orchestration ran in Azure, called all three suppliers in parallel, and returned the best quote, just like it did locally.

---

## Monitoring in the Azure Portal

Now here's something really cool. Let's look at the monitoring capabilities in Azure.

*[SHOW ON SCREEN: Azure Portal, navigating to Function App]*

Go to the Azure Portal and navigate to your Function App. Find your HttpOrchestratorStart function and click on it. Now click on the Monitor tab.

*[SHOW ON SCREEN: Monitor tab with invocation history]*

You can see a complete history of every time your function was invoked. Click on one of the invocations to see detailed information.

*[SHOW ON SCREEN: Detailed invocation information]*

You can see the complete execution timeline, any logs that were written, and whether it succeeded or failed. For durable functions, you can even see the entire orchestration history, showing every activity that was called and when.

This monitoring is incredibly valuable for debugging and understanding what's happening in your functions.

---

## Lab Challenge

Before we wrap up, here's a challenge to think about. The fan-out pattern with durable functions is powerful, but consider these questions:

How would you on-board a new supplier with this pattern? You'd have to modify the orchestrator code to call another activity function. Compare that with an event-driven pub-sub pattern using separate functions and something like Service Bus. With pub-sub, you could just add a new subscriber without changing existing code.

Also, what if you wanted a timeout? Maybe you only want to wait five seconds for quotes, and you'll work with whatever responses you have by then. How would you implement that? Think about using Task.WhenAny with a timeout task, or using context.CreateTimer in your orchestrator.

These are the kinds of trade-offs you need to consider when choosing between patterns. Both approaches have their strengths, and understanding when to use each one is key to being an effective Azure developer.

---

## Cleanup

When you're done experimenting, don't forget to clean up your resources.

*[SHOW ON SCREEN: Terminal]*

Stop the local storage emulator:

```
docker rm -f azurite
```

And delete your Azure resource group:

```
az group delete -y --no-wait -n labs-functions-durable-fan-out
```

The no-wait flag means the command returns immediately without waiting for deletion to complete, which can take a few minutes.

---

## Summary

Great work! You've successfully implemented and deployed a fan-out/fan-in pattern using Azure Durable Functions. You learned how to coordinate multiple parallel activities, how to use HTTP triggers with durable orchestrations, and how to monitor your functions in Azure.

These skills are essential for building scalable, efficient cloud applications, and they're important topics for the AZ-204 certification exam.

Thanks for following along, and happy coding!

---

**[END OF EXERCISES]**
