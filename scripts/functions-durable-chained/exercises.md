# Azure Durable Functions - Chained Pattern Exercises Walkthrough

## Understanding the Code Structure

Before we start running anything, let's explore the code structure for our durable function. Understanding the architecture will make everything clearer as we work through the exercises.

### The Trigger Function

Open up the file TimedOrchestratorStart.cs in the DurableChained folder. This is our entry point.

Notice it uses a standard TimerTrigger - it runs on a schedule, just like any other timer-based function. But here's where it gets interesting: it also has a DurableClient parameter decorated with the DurableClient attribute.

This DurableClient is your gateway to starting orchestrations. In the function body, you'll see it creates an ApplicationStatus object with a timestamp, then calls StartNewAsync on the client to begin the orchestration. It passes "ChainedOrchestrator" as the orchestrator name and sends along that status object.

Think of this as pressing the "start" button on your workflow. The timer fires, the function runs, and it tells the durable functions runtime to begin executing the ChainedOrchestrator.

### The Orchestrator Function

Now let's look at ChainedOrchestrator.cs. This is where the magic happens.

The function has an OrchestrationTrigger parameter, which means it can only be invoked by the durable functions runtime - not directly by HTTP requests or other triggers.

Read through the orchestrator code. You'll see it calls three activities in sequence using CallActivityAsync. First, it calls "WriteBlob" and passes the application status. Then it takes the output from WriteBlob - which is the blob name - and passes it to "NotifySubscribers". Finally, it passes the same information to "WriteLog".

Notice how clean this is. You're looking at the entire workflow in one place. No separate functions with complex triggers. No manual state management. Just straightforward sequential logic.

One important point: orchestrator functions get replayed. The framework saves checkpoints after each activity completes, and if the function needs to restart, it replays from the beginning but skips activities that already completed. This is why orchestrator code must be deterministic - it can't use DateTime.Now directly, generate random numbers, or make non-deterministic API calls.

### The Activity Functions

Now let's explore the three activity functions in the Activities folder.

**WriteBlob Activity**: Open Activities/WriteBlob.cs. This activity takes the application status, generates a blob name from the timestamp, and saves the status as JSON to blob storage. Notice it creates the blob binding programmatically using the Binder - this lets you specify the blob path dynamically at runtime rather than hardcoding it. This activity returns the blob name, which the orchestrator will pass to the next activities.

**NotifySubscribers Activity**: Look at Activities/NotifySubscribers.cs. This function publishes a message to an Azure Service Bus queue named "HeartbeatCreated". It uses a ServiceBus attribute to bind to the queue. The message contains the blob name from the previous activity. Other systems could subscribe to this queue and react when heartbeat events occur.

**WriteLog Activity**: Finally, check out Activities/WriteLog.cs. This activity writes an entity to Azure Table Storage for audit logging. It uses the Table attribute binding and creates a TableEntity with the timestamp and blob information. This gives you a queryable history of all heartbeat events.

Each activity does one thing and does it well. They're simple, testable, and reusable.

---

## Exercise 1: Set Up Your Development Environment

Let's get your environment ready for local testing.

### Create the Azure Service Bus Resources

Durable functions need storage, and our activities need Service Bus. While we can use the Azure Storage Emulator for local development, there's no Service Bus emulator, so we need to create real Azure resources.

**Create a Service Bus Namespace**: Run the Azure CLI command to create a namespace. Choose a unique name and specify the Standard SKU since we need queues.

*[SHOW ON SCREEN: az servicebus namespace create command]*

The namespace is your Service Bus container. It provides a unique endpoint for your messaging operations.

**Create the Queue**: Within your namespace, create a queue named "HeartbeatCreated". This exact name matches what the NotifySubscribers activity expects.

*[SHOW ON SCREEN: az servicebus queue create command]*

**Get the Connection String**: Retrieve the connection string for your namespace. You'll need this for the local configuration.

*[SHOW ON SCREEN: az servicebus namespace authorization-rule keys list command]*

Keep this connection string handy - you'll use it in the next step. Remember, this connection string contains credentials, so never commit it to source control.

### Start the Azure Storage Emulator

Our function uses blob storage and table storage for the activities, and durable functions need storage for orchestration state. Let's use the Azurite emulator for local development.

**Start Azurite with Docker**: Run the Docker command to start Azurite. It exposes ports 10000 through 10002 for blob, queue, and table storage services.

*[SHOW ON SCREEN: docker run command for azurite]*

This gives you a fully functional local storage emulator. It's perfect for development and testing without Azure costs.

**Verify It's Running**: Check that the Azurite container is running with docker ps. You should see it listening on the three ports.

### Configure Local Settings

Now create your local configuration file. This file tells the function runtime how to connect to all the services.

**Create local.settings.json**: In the DurableChained folder, create a file named local.settings.json.

The file needs several settings:

- **AzureWebJobsStorage**: Set this to "UseDevelopmentStorage=true" to use Azurite for the function's internal storage needs
- **FUNCTIONS_WORKER_RUNTIME**: Set this to "dotnet" since we're using C#
- **StorageConnectionString**: Also set to "UseDevelopmentStorage=true" for the WriteBlob and WriteLog activities
- **ServiceBusConnectionString**: Paste in the actual connection string you got from Azure

*[SHOW ON SCREEN: The local.settings.json structure with placeholder for Service Bus]*

Notice we're mixing local and cloud services. Blob and table use the emulator, but Service Bus uses Azure. This hybrid approach is common in development.

---

## Exercise 2: Test the Function Locally

Time to see your durable function in action.

### Start the Function

Navigate to the DurableChained directory in your terminal and run the Azure Functions Core Tools.

*[SHOW ON SCREEN: func start command]*

The Function runtime will start up. You'll see it discovering functions, loading assemblies, and initializing. Watch for messages showing that it found your timer trigger, orchestrator, and all three activities.

The timer trigger is configured to run every few minutes, so you might need to wait a bit for it to fire. Or, if you want to test immediately, you could modify the timer schedule in the code to run more frequently during development.

### Observe the Orchestration

When the timer fires, watch the console output carefully. You'll see a sequence of events unfold.

**Orchestrator Starts**: First, you'll see a line saying "Executing TimedOrchestratorStart" followed by "Starting orchestration for: save-handler". This is your timer trigger starting the orchestrator.

**Activity Execution**: Next, you'll see "Executing WriteBlob". The activity runs, creates the blob, and logs "Created blob" with the path. Look for the blob path - it will be something like "heartbeat/20221114022400" with the current timestamp.

**Second Activity**: Then you'll see "Executing NotifySubscribers" followed by "Published heartbeat message". This means the message successfully went to the Service Bus queue.

**Third Activity**: Finally, you'll see the WriteLog activity execute, though it might not produce visible output.

**Completion**: Look for "Orchestrator completed" and "Executed ChainedOrchestrator". This tells you the entire workflow finished successfully.

All of this happens automatically, orchestrated by the durable functions framework. Each activity runs in sequence, receiving the output from the previous step.

### Verify the Blob Storage

Let's check that the WriteBlob activity actually created a blob in your local storage emulator.

**List Tables**: Use the Azure CLI to list tables in your local storage. You'll need to use the emulator's connection string.

*[SHOW ON SCREEN: az storage table list command with emulator connection string]*

You should see a table named "heartbeats" created by the WriteLog activity. You'll also see tables with names like "DurableFunctionsHubHistory" - these are used by the durable functions framework to manage orchestration state.

The blob itself is a bit harder to verify with just CLI commands, but you could use Azure Storage Explorer to browse your local Azurite instance and navigate to the "heartbeat" container.

### Check the Service Bus Queue

Now let's verify the message arrived in Azure Service Bus.

**Open the Portal**: Navigate to the Azure Portal and find your Service Bus namespace.

**Access Service Bus Explorer**: In your namespace, select the "HeartbeatCreated" queue, then click on "Service Bus Explorer" in the left menu. This is a built-in tool for viewing and managing queue messages.

**Peek at Messages**: Click "Peek from start". This shows messages without removing them from the queue.

You should see messages with JSON content showing the blob name, something like `{"BlobName": "heartbeat/20221114022400"}`. Each time the timer fires and the orchestration runs, a new message appears here.

This confirms your entire workflow is functioning - the blob was created, the message was published, and the table entry was written, all coordinated by the orchestrator.

### Understanding the Flow

Take a moment to appreciate what just happened. A single timer trigger started a workflow that coordinated three different activities across three different Azure services. The orchestrator managed the execution order, passed data between activities, and ensured everything ran in sequence.

If any activity had failed, the orchestrator would have stopped there, and the durable functions framework would have retry logic available. You're getting enterprise-grade reliability in a serverless function.

---

## Exercise 3: Deploy to Azure

Once your function works locally, deploying to Azure is straightforward. Let's walk through the deployment process.

### Create the Azure Resources

First, you need a function app and supporting resources in Azure.

**Create a Resource Group**: Start with a resource group to hold all your resources. Use a descriptive name and add the courselabs tag for easy identification.

*[SHOW ON SCREEN: az group create command]*

**Create a Storage Account**: The function app needs a storage account for its internal operations. Choose a unique name and use the Standard LRS SKU for cost-effective local redundancy.

*[SHOW ON SCREEN: az storage account create command]*

**Create the Function App**: Now create the function app itself. Specify the dotnet runtime, Functions version 4, and the consumption plan for serverless billing.

*[SHOW ON SCREEN: az functionapp create command]*

The function app is now running in Azure, but it's empty - we need to deploy our code.

### Configure the Dependencies

Your function needs access to the Service Bus and an output storage account. If you created these earlier for local testing, you can reuse them. Otherwise, create them now.

**Service Bus Configuration**: You already have a namespace and queue from local testing. Get the connection string if you don't have it saved.

**Output Storage Account**: You can use the same storage account as the function app, or create a separate one for cleaner separation. Get its connection string.

**Set Application Settings**: Use the Azure CLI to configure the function app with these connection strings. Set ServiceBusConnectionString and StorageConnectionString as application settings.

*[SHOW ON SCREEN: az functionapp config appsettings set command with placeholder values]*

These settings become environment variables that your function code reads at runtime. They're stored securely in Azure and never appear in your source code.

### Deploy the Function Code

Now for the exciting part - deploying your code to Azure.

**Publish with func CLI**: From the DurableChained directory, use the Azure Functions Core Tools to publish. Specify your function app name.

*[SHOW ON SCREEN: func azure functionapp publish command]*

The CLI packages your code, uploads it to Azure, and triggers a deployment. You'll see progress messages as it syncs files and initializes the function app.

This process installs your functions, their dependencies, and configuration in the Azure environment.

### Verify the Deployment

Let's make sure everything deployed correctly.

**Open the Portal**: Navigate to your function app in the Azure Portal.

**Check the Functions List**: Click on "Functions" in the left menu. Here's an interesting observation: do you see all your functions, or only some of them?

You should see the TimedOrchestratorStart function because it has an external trigger - the timer. But the orchestrator and activities might not appear in this list because they use internal triggers. The portal primarily shows functions that can be invoked externally.

Don't worry - they're all there and working, even if not all are visible in the portal.

**Monitor Executions**: Wait a few minutes for the timer to fire. Then check the "Monitor" section or "Application Insights" to see execution logs. You should see the orchestrator running and the activities completing successfully.

**Verify the Output**: Check your Service Bus queue in the portal - new messages should appear. Check the storage account - you should see blobs being created in the heartbeat container and entries in the heartbeats table.

Your durable function is now running in production, executing the chained workflow on a schedule.

---

## Exercise 4: Lab Challenge - Understanding Activity Triggers

Here's a challenge to deepen your understanding of how durable functions work.

### The Question

In the Azure Portal, functions can be disabled, which prevents their triggers from firing. Can you disable one of the activity triggers? What would happen if you could?

### Exploring the Portal

Go to your function app in the portal and look at the Functions list. Try to find the activity functions - WriteBlob, NotifySubscribers, or WriteLog.

You might notice they don't appear in the same way as the timer trigger. This is because activities use the ActivityTrigger binding, which is internal to the durable functions framework.

### Understanding the Implication

Think about the architecture. The orchestrator calls activities using the CallActivityAsync method. These aren't HTTP endpoints or queue-based triggers - they're function-to-function calls managed by the durable functions runtime.

If you could disable an activity, the orchestrator would try to call it, and the call would fail. The orchestrator would handle this as an exception. Depending on your retry policies, it might retry, or it might fail the entire orchestration.

### The Real Answer

Activity functions can't be disabled independently because they're not triggered by external events. They're invoked directly by the orchestrator through the durable functions framework. The only way to prevent an activity from running is to not call it from the orchestrator or to disable the function that starts the orchestration.

This design makes sense when you think about it - an orchestrator manages a workflow as a single unit. Disabling part of the workflow would leave it in an inconsistent state.

### What You Can Disable

You CAN disable the TimedOrchestratorStart function. This would prevent new orchestrations from starting, but it wouldn't affect any in-progress orchestrations - they would continue to completion.

Try it - go to the timer trigger function, click "Disable", and watch what happens. No new heartbeats are created. Enable it again, and the workflow resumes.

---

## Key Takeaways from the Exercises

Let's recap what you've learned through these hands-on exercises.

**Durable functions orchestrate stateful workflows** in serverless environments. You write clear, sequential code and the framework handles state, reliability, and scaling.

**The chained pattern coordinates multiple activities** that must run in order. Each activity receives the output from the previous one, creating a pipeline of operations.

**Development is flexible** - you can test locally with emulators and then deploy to Azure with minimal changes. The same code runs in both environments.

**Activities use special triggers** - ActivityTrigger for activities and OrchestrationTrigger for orchestrators. These aren't external triggers like HTTP or queues; they're internal to the durable functions framework.

**Orchestrators must be deterministic** because they get replayed during execution. Avoid non-deterministic operations in orchestrator code.

**Monitoring and debugging** work through standard Azure Functions tools - Application Insights, logs, and the portal. But remember that not all functions appear in the portal's function list.

**The pattern is powerful** - you coordinated blob storage, Service Bus, and table storage in a single workflow without writing any coordination code. The orchestrator did it all.

---

## Cleanup

Before we finish, let's clean up your Azure resources to avoid unnecessary charges.

**Stop the Storage Emulator**: Remove the Azurite Docker container since you don't need it running anymore.

*[SHOW ON SCREEN: docker rm command]*

**Delete the Resource Group**: Remove the entire resource group containing your function app and associated resources. Use the --no-wait flag to return immediately without waiting for deletion to complete.

*[SHOW ON SCREEN: az group delete command]*

**Keep or Remove Service Bus**: If you created the Service Bus namespace specifically for this lab, you can delete that resource group too. If you're using it for other labs, keep it.

---

## Excellent Work!

You've successfully built, tested, and deployed a durable function using the chained pattern. You understand how orchestrators coordinate activities, how to pass data between steps, and how to work with the durable functions framework.

These skills are essential for building complex serverless workflows in Azure. You're now prepared to tackle real-world scenarios that require reliable, sequential processing across multiple services.

Keep exploring the other durable function patterns - fan-out/fan-in, async HTTP APIs, and monitoring patterns each solve different workflow challenges. But the fundamentals you learned here apply to all of them.

Great job!
