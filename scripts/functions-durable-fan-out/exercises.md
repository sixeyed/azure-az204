# Azure Durable Functions: Fan-Out/Fan-In Pattern - Lab Exercises

## Introduction to the Lab

Welcome to the hands-on portion of our Azure Durable Functions lab. In this exercise, we're going to implement the fan-out/fan-in pattern to build a real-world quote engine. This is a significant improvement over a simpler Service Bus-based approach, because now we'll actually wait for all supplier responses and intelligently select the best quote.

Let's start by understanding what we're building, then we'll test it locally, and finally deploy it to Azure.

## Understanding the Code Structure

Before we run anything, let's take a quick tour of the code we'll be working with. You'll find everything in the QuoteEngine folder.

First, we have the HTTP Orchestrator Start function. This is our entry point that uses an HTTP trigger, which means we can call it with a simple HTTP request. When we do that, it starts the durable orchestration and immediately returns a set of URLs - status URLs that we can use to check on the progress of our long-running function. This is really useful because we don't have to keep an HTTP connection open while waiting for results.

Next, we have the Quote Orchestrator. This is where the fan-out/fan-in magic happens. The orchestrator calls three different supplier quote activities asynchronously using Task.WhenAll, which means they all run in parallel. Then it waits for all of them to complete. This is incredibly efficient because the total duration is only as long as the slowest supplier call, not the sum of all three.

And then we have our activity functions, one for each supplier. They're all similar in structure - they generate a random quote price and return it in a response object. One of them has a deliberate delay built in, so we can see that the orchestrator patiently waits for even the slowest service to respond.

Once all the quotes are in, the orchestrator selects the one with the best price and returns that as the final result. It's a simple but powerful pattern.

## Setting Up the Local Environment

Alright, let's get this running on your local machine first. Before we can test the function, we need a storage account, because durable functions persist their state in Azure Storage.

The good news is we don't need to create anything in Azure for local testing. We can use the Azure Storage emulator called Azurite.

Make sure Docker Desktop is running on your machine. Then open a terminal and start Azurite. We're running it in detached mode with the -d flag, exposing ports 10000 through 10002 for blob, queue, and table storage services. The --name flag gives the container a friendly name we can reference later.

Azurite is now running in the background, emulating Azure Storage on your local machine. This container exposes the storage endpoints that durable functions needs to maintain orchestration state.

## Creating the Local Configuration

Now we need to create a local settings file so our function knows how to connect to the storage emulator.

Navigate to your labs folder, then functions-durable, then fan-out, and into the QuoteEngine folder. We need to create a file called local.settings.json here.

This file contains our local configuration. The IsEncrypted setting is false because we're working locally - encryption is handled differently in production. Then we have our Values section with two important settings.

AzureWebJobsStorage is set to "UseDevelopmentStorage=true" which tells the function to use our local Azurite emulator instead of a real Azure Storage account. This magic connection string is recognized by the Azure SDK and automatically connects to localhost on the standard Azurite ports.

FUNCTIONS_WORKER_RUNTIME is set to "dotnet" because this is a .NET function. This tells the Functions runtime which language worker to use.

Notice we're not putting any real connection strings or credentials in here. For local development, that simple placeholder is all we need. This separation of configuration makes it easy to switch between local and cloud environments.

## Running the Function Locally

Time to run our function. In your terminal, make sure you're in the QuoteEngine directory.

Now start the Azure Functions Core Tools using func start. This command launches the local Functions runtime.

The runtime is starting up and discovering your functions. You'll see it find all the functions in our project - the HTTP Orchestrator Start function, the Quote Orchestrator, and all three supplier activity functions.

Look for the HTTP trigger URL in the output. You should see something like "HttpOrchestratorStart" followed by GET and POST methods, and a localhost URL on port 7071. That's the endpoint we'll call to start our orchestration.

## Triggering the Orchestration

Now let's trigger the orchestration. Open a second terminal window so you can keep an eye on the function logs in the first one.

In your new terminal, we'll use curl to call the HTTP trigger. We're making a GET request to localhost port 7071 at the api/HttpOrchestratorStart path.

Excellent! Now look at your first terminal where the function is running. You should see the orchestrator logs showing all three suppliers being called.

Notice they all start executing at almost exactly the same time? That's the fan-out happening - each supplier quote activity is running in parallel. You'll see messages like "SUPPLIER-1 calculating price for quote ID" followed by "SUPPLIER-1 calculated quote" with a random price amount.

The key thing to notice is that even though one supplier has a deliberate delay, the orchestrator waits patiently for all of them before proceeding. That's the fan-in part of the pattern - gathering all the parallel results before continuing.

## Understanding the Status URLs

Now look at your curl terminal where you made the request. You should see a JSON response containing multiple URLs. Don't worry about memorizing these - they're provided automatically by the durable functions framework.

This is what an HTTP-triggered durable function returns: a set of management URLs that let you interact with the running orchestration.

The most important one is the statusQueryGetUri. This is the URL you can call to check on the progress of your orchestration and retrieve results. You'd typically use this in a web application to show progress to users, or to poll for completion and get the final results.

There's also a sendEventPostUri for sending external events to the running orchestration - useful for approval workflows or human-in-the-loop scenarios. And other URLs for terminating the orchestration, purging history, or restarting it. This gives you complete programmatic control over your long-running functions.

## Checking the Orchestration Status

Let's use that status URL to see our results. Copy the statusQueryGetUri from your response - it will be unique to your specific orchestration instance.

Make another curl request using that URL. The URL will be something like localhost port 7071 with a path including the orchestration instance ID and some query parameters.

Fantastic! The response shows you everything about your orchestration. The runtimeStatus field shows "Completed", which means all the suppliers have responded and the orchestrator has finished its work.

Look at the input section - it shows the quote request that was generated, with a quote ID, product code, and quantity.

And here's the important part: the output section. This contains the winning quote! You can see which supplier had the best price. In this example run, it might be SUPPLIER-3 with a quote of two hundred fifty-six dollars, or whatever random values your run generated.

You can also see timing information - when the orchestration was created and when it last updated. If you had called this URL while the suppliers were still calculating, you'd see a runtimeStatus of "Running" instead of "Completed", and the output would be null until completion.

## Deploying to Azure

Now that we've seen it working locally, let's deploy this to Azure. First, we need to create the Azure resources.

We'll start by creating a resource group called "labs-functions-durable-fan-out" in East US with the courselabs tag.

Next, we need a Storage Account. Remember, durable functions need storage to persist their orchestration state, checkpoints, and work items. Choose a unique name for your storage account - something like "durablestorage" plus your initials and a few random numbers.

We're using the Standard LRS SKU for locally redundant storage, which is cost-effective for development scenarios.

Now let's create the Function App itself. Again, choose a unique name for your function app. We're specifying the dotnet runtime, Functions version 4 for the latest features, the consumption plan for serverless pay-per-execution billing, and linking it to our storage account.

The Function App is now created. One of the great things about this example is that we don't have any external dependencies like Service Bus or Cosmos DB. The function is completely self-contained, using only the storage account that's already required for durable functions. This makes deployment really simple.

## Publishing the Function

Now we'll publish our code to Azure using the Azure Functions Core Tools. From the QuoteEngine directory, run func azure functionapp publish with your function app name.

The tools are packaging your function code, uploading it to Azure, and setting everything up. This might take a minute or two as it zips your files, uploads them, syncs triggers, and prepares the remote environment.

Look at the output when it completes. You should see the HTTP trigger URL listed, but this time it's a public Azure URL on the azurewebsites.net domain, not localhost. This is your production endpoint.

Copy that URL because we're going to test it.

## Testing in Azure

Let's verify that our function works in Azure just like it did locally. Use curl with your Azure function URL. You're making a request to your-function-name.azurewebsites.net at the api/HttpOrchestratorStart path.

You should get the same type of JSON response with status URLs, but this time they're all Azure URLs instead of localhost. The pattern is exactly the same - the function returns management URLs for checking status and controlling the orchestration.

Copy the statusQueryGetUri from the response and call it with curl to see your results.

Perfect! The orchestration ran in Azure, called all three suppliers in parallel, and returned the best quote, just like it did locally. The same code, the same behavior, but now running in the cloud.

## Monitoring in the Azure Portal

Now here's something really cool - let's look at the monitoring capabilities in Azure.

Go to the Azure Portal and navigate to your Function App. Find your HttpOrchestratorStart function in the functions list and click on it. Now click on the Monitor tab.

You can see a complete history of every time your function was invoked. Each invocation is listed with its timestamp, duration, and status. Click on one of the invocations to see detailed information.

You can see the complete execution timeline showing when the function started, what parameters it received, and what it returned. Any logs that were written appear here. For durable functions, you can even see the entire orchestration history, showing every activity that was called and when.

This monitoring is incredibly valuable for debugging and understanding what's happening in your functions. Application Insights integration provides even deeper telemetry if you enable it.

## Lab Challenge

Before we wrap up, here's a challenge to think about. The fan-out pattern with durable functions is powerful, but consider these trade-offs.

How would you onboard a new supplier with this pattern? You'd have to modify the orchestrator code to call another activity function. Compare that with an event-driven pub-sub pattern using separate functions and something like Service Bus or Event Grid. With pub-sub, you could just add a new subscriber function without changing existing code. There's no central orchestrator to update.

Also, what if you wanted a timeout? Maybe you only want to wait five seconds for quotes, and you'll work with whatever responses you have by then. How would you implement that? Think about using Task.WhenAny combined with a timeout task, or using context.CreateTimer in your orchestrator to implement deadline-based logic.

These are the kinds of trade-offs you need to consider when choosing between patterns. Durable functions give you centralized control and guaranteed completion, but they require code changes for new participants. Event-driven patterns are more decoupled and flexible, but they give up some control and predictability. Both approaches have their place, and understanding when to use each one is key to being an effective Azure developer.

## Cleanup

When you're done experimenting, don't forget to clean up your resources to avoid unnecessary charges.

Stop the local storage emulator by removing the azurite Docker container using docker rm with the -f flag.

Delete your Azure resource group using az group delete with the -y flag to skip confirmation and --no-wait to return immediately without waiting for completion.

The no-wait flag means the command returns immediately while Azure deletes resources in the background. This can take a few minutes, but you don't need to wait.

## Summary

Great work! You've successfully implemented and deployed a fan-out/fan-in pattern using Azure Durable Functions. You learned how to coordinate multiple parallel activities, wait for all of them to complete, and aggregate their results. You saw how to use HTTP triggers with durable orchestrations to provide status URLs for long-running operations. And you experienced the monitoring capabilities available in Azure for debugging and understanding function behavior.

These skills are essential for building scalable, efficient cloud applications. The fan-out/fan-in pattern is perfect for scenarios where you need to gather results from multiple sources before proceeding - supplier quotes, credit checks, parallel data processing, or any scenario where you need to fork execution, do work in parallel, and then join the results.

The pattern appears in many real-world scenarios, and it's an important topic for the AZ-204 certification exam. Understanding when to use fan-out/fan-in versus other patterns like event-driven pub-sub is a key architectural skill.

Thanks for following along, and excellent work completing this hands-on lab!
