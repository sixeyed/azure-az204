# Durable Functions: Chained Functions

## Reference

Durable functions are an extension of Azure Functions that enable stateful workflows in a serverless environment. You can chain functions together if the output of one function can serve as the trigger to the next, but durable functions give you a much better way to model workflows with multiple steps. The orchestrator code calls all the other activities in sequence, managing inputs and outputs without needing additional triggers between steps.

## Timer Trigger with Orchestration

Before we start running anything, let's explore the code structure for our durable function. Understanding the architecture will make everything clearer as we work through the exercises.

**The Trigger Function**: Open up the file TimedOrchestratorStart.cs in the DurableChained folder. This is our entry point function. Notice it uses a standard TimerTrigger attribute - it runs on a schedule, just like any other timer-based function. But here's where it gets interesting: it also has a DurableClient parameter decorated with the DurableClient attribute.

This DurableClient is your gateway to starting orchestrations. In the function body, you'll see it creates an ApplicationStatus object with a timestamp, then calls StartNewAsync on the client to begin the orchestration. It passes "ChainedOrchestrator" as the orchestrator name and sends along that status object as the input.

Think of this as pressing the "start" button on your workflow. The timer fires, the trigger function runs, and it tells the durable functions runtime to begin executing the ChainedOrchestrator.

**The Orchestrator Function**: Now let's look at ChainedOrchestrator.cs. This is where the orchestration logic lives. The function has an OrchestrationTrigger parameter, which means it can only be invoked by the durable functions runtime - not directly by HTTP requests or other external triggers. This is important for maintaining the integrity of the orchestration.

Read through the orchestrator code. You'll see it calls three activities in sequence using CallActivityAsync. First, it calls "WriteBlob" and passes the application status. Then it takes the output from WriteBlob - which is the blob name - and passes it to "NotifySubscribers". Finally, it passes the same blob name to "WriteLog".

Notice how clean and sequential this is. You're looking at the entire workflow in one place. No separate functions with complex trigger chaining. No manual state management to track where you are in the process. Just straightforward sequential logic that reads like a script.

One important point about orchestrator functions: they get replayed. The framework saves checkpoints after each activity completes, and if the function needs to restart for any reason, it replays from the beginning but skips activities that already completed. This replay mechanism is why orchestrator code must be deterministic - you can't use DateTime.Now directly, generate random numbers, or make non-deterministic API calls in the orchestrator itself.

**The Activity Functions**: Now let's explore the three activity functions in the Activities folder. The WriteBlob activity is in Activities/WriteBlob.cs. This activity takes the application status, generates a blob name from the timestamp, and saves the status as JSON to blob storage. Notice it creates the blob binding programmatically using the Binder - this lets you specify the blob path dynamically at runtime rather than hardcoding it in an attribute. This activity returns the blob name, which the orchestrator will pass to the next activities.

The NotifySubscribers activity is in Activities/NotifySubscribers.cs. This function publishes a message to an Azure Service Bus queue named "HeartbeatCreated". It uses a ServiceBus attribute to bind to the queue. The message contains the blob name from the previous activity. Other systems could subscribe to this queue and react when heartbeat events occur - maybe sending notifications, triggering workflows, or updating dashboards.

The WriteLog activity is in Activities/WriteLog.cs. This activity writes an entity to Azure Table Storage for audit logging. It uses the Table attribute binding and creates a TableEntity with the timestamp and blob information. This gives you a queryable history of all heartbeat events that can be analyzed or reported on.

Each activity does one focused thing and does it well. They're simple, testable, and reusable. The orchestrator coordinates them into a meaningful workflow.

## Test the function locally

Let's get your environment ready for local testing.

**Create the Azure Service Bus Resources**: Durable functions need storage for orchestration state, and our activities need Service Bus for messaging. While we can use the Azure Storage Emulator locally, there's no Service Bus emulator, so we need to create real Azure resources.

First, create a Service Bus namespace. Choose a unique name and specify the Standard SKU since we need queue capabilities - the Basic SKU doesn't support all the features we'll use. The namespace is your Service Bus container. It provides a unique endpoint and contains all your queues and topics.

Next, create a queue named "HeartbeatCreated" within your namespace. This exact name matches what the NotifySubscribers activity expects in its binding.

Now get the connection string for your namespace using the authorization rule keys list command. Query for just the primary connection string in TSV format for easy copying.

Keep this connection string handy - you'll use it in the local configuration. Remember, connection strings contain credentials, so never commit them to source control in real projects.

**Start the Azure Storage Emulator**: Our function uses blob storage and table storage for the activities, and durable functions need storage for maintaining orchestration state. Let's use the Azurite emulator for local development.

Start Azurite using Docker. We're running it in detached mode, exposing ports 10000 through 10002 for blob, queue, and table storage services respectively.

This gives you a fully functional local storage emulator running in a container. It's perfect for development and testing without incurring Azure costs.

Verify it's running by checking your Docker containers. You should see the azurite container with status "Up" and the three ports exposed.

**Configure Local Settings**: Now create your local configuration file. This file tells the function runtime how to connect to all the services it needs.

In the DurableChained folder, create a file named local.settings.json. This file needs several settings configured.

Set AzureWebJobsStorage to "UseDevelopmentStorage=true" to use Azurite for the function's internal storage needs - this is where durable functions maintains orchestration state, checkpoints, and work items.

Set FUNCTIONS_WORKER_RUNTIME to "dotnet" since we're using C# functions.

Set StorageConnectionString to "UseDevelopmentStorage=true" as well - this is what the WriteBlob and WriteLog activities use.

Set ServiceBusConnectionString to the actual connection string you got from Azure earlier.

Notice we're mixing local and cloud services. Blob and table storage use the local emulator, but Service Bus uses Azure. This hybrid approach is common in development - you use local emulators where available and cloud services where emulators don't exist.

**Start the Function**: Navigate to the DurableChained directory in your terminal and start the Azure Functions Core Tools using the func start command.

The Function runtime will initialize. You'll see it discovering functions, loading assemblies, and preparing the execution environment. Watch for messages showing that it found your timer trigger, orchestrator, and all three activities.

The timer trigger is configured to run on a schedule. Depending on the CRON expression, you might need to wait for it to fire, or you could modify the schedule temporarily to run more frequently during development.

**Observe the Orchestration**: When the timer fires, watch the console output carefully. You'll see a sequence of events unfold that demonstrates the orchestration in action.

First, you'll see "Executing TimedOrchestratorStart" followed by a message saying it's starting the orchestration. This is your timer trigger launching the workflow.

Next, you'll see "Executing WriteBlob". The activity runs, creates the blob, and logs the blob path - something like "heartbeat/20221114022400" with the current date and time.

Then you'll see "Executing NotifySubscribers" followed by confirmation that the message was published to Service Bus.

Finally, the WriteLog activity executes, though it might not produce visible console output.

When it's all done, you'll see "Orchestrator completed" and "Executed ChainedOrchestrator". The entire workflow has finished successfully.

All of this happens automatically, orchestrated by the durable functions framework. Each activity runs in sequence, receiving the output from the previous step, without any manual coordination code.

**Verify the Blob Storage**: Let's check that the WriteBlob activity actually created data in your local storage emulator. Use the Azure CLI to list tables in your local storage, using the emulator's connection string.

You should see a table named "heartbeats" created by the WriteLog activity. You'll also see tables with names like "DurableFunctionsHubHistory" and "DurableFunctionsHubInstances" - these are used by the durable functions framework to manage orchestration state, track instances, and coordinate activities.

The actual blob is harder to verify with CLI commands alone, but you could use Azure Storage Explorer to browse your local Azurite instance and navigate to the "heartbeat" container to see the JSON files.

**Check the Service Bus Queue**: Now let's verify the message arrived in Azure Service Bus. Navigate to the Azure Portal and find your Service Bus namespace. Select the "HeartbeatCreated" queue, then click on "Service Bus Explorer" in the left menu. This is a built-in tool for viewing and managing queue messages without writing any code.

Click "Peek from start" to view messages without removing them from the queue. This non-destructive peek lets you inspect messages while leaving them for other consumers.

You should see messages with JSON content showing the blob name. Each time the timer fires and the orchestration runs, a new message appears here.

This confirms your entire workflow is functioning end-to-end - the blob was created, the Service Bus message was published, and the table entry was written, all coordinated seamlessly by the orchestrator.

**Understanding the Flow**: Take a moment to appreciate what just happened. A single timer trigger started a workflow that coordinated three different activities across three different Azure services. The orchestrator managed the execution order, passed data between activities, and ensured everything ran in the correct sequence.

If any activity had failed, the orchestrator would have stopped there. The durable functions framework provides built-in retry logic and error handling that you can configure. You're getting enterprise-grade reliability in a serverless function without writing complex coordination code.

## Deploy to Azure

Once your function works locally, deploying to Azure is straightforward. Let's walk through the deployment process.

**Create the Azure Resources**: First, you need a function app and supporting resources in Azure. Create a resource group to hold all your resources. Use a descriptive name like "labs-functions-durable-chained" and add the courselabs tag.

Create a Storage Account for the function app's internal operations. Choose a unique name and use the Standard LRS SKU for cost-effective local redundancy. This storage account is used by Azure Functions for triggers, bindings, and orchestration state.

Create the Function App itself. Specify the dotnet runtime, Functions version 4 for the latest features, and the consumption plan for serverless billing where you only pay for execution time.

The function app is now running in Azure as an empty shell - we need to deploy our code to it.

**Configure the Dependencies**: Your function needs access to Service Bus and a storage account for the activities. If you created these earlier for local testing, you can reuse them. Otherwise, create them now.

For Service Bus, you already have a namespace and queue from local testing. Get the connection string if you don't have it saved - use the same authorization rule keys list command.

For output storage, you can use the same storage account as the function app itself, or create a separate one for cleaner separation of concerns. Get its connection string using the storage account show-connection-string command.

Set these as application settings on the function app. We're configuring ServiceBusConnectionString and StorageConnectionString as environment variables that your function code reads at runtime.

These settings are stored securely in Azure and never appear in your source code. This separation of configuration from code is a key principle of cloud-native applications.

**Deploy the Function Code**: Now for the deployment. From the DurableChained directory, use the Azure Functions Core Tools to publish your code. Specify your function app name.

The CLI packages your code, uploads it to Azure, and triggers a deployment. You'll see progress messages as it syncs files, restores NuGet packages, and initializes the function app.

This process installs your functions, their dependencies, and configuration in the Azure environment. The deployment typically takes a minute or two.

**Verify the Deployment**: Let's make sure everything deployed correctly and is working in Azure. Navigate to your function app in the Azure Portal. Click on "Functions" in the left menu to see the list of functions.

Here's an interesting observation: do you see all your functions, or only some of them? You should see the TimedOrchestratorStart function because it has an external trigger that the portal recognizes. But the orchestrator and activity functions might not appear in this list because they use internal triggers - OrchestrationTrigger and ActivityTrigger. The portal primarily shows functions that can be invoked externally.

Don't worry - they're all there and working, even if not all are visible in the portal's function list.

Wait a few minutes for the timer to fire, then check the "Monitor" section or Application Insights to see execution logs. You should see the orchestrator running and the activities completing successfully.

Verify the output by checking your Service Bus queue in the portal - new messages should appear as the timer fires. Check the storage account - you should see blobs being created in the heartbeat container and entries in the heartbeats table.

Your durable function is now running in production, executing the chained workflow on schedule.

## Lab

Here's a challenge to deepen your understanding of how durable functions work.

**The Question**: In the Azure Portal, functions can be disabled, which prevents their triggers from firing. Can you disable one of the activity functions? What would happen if you could?

**Exploring the Portal**: Go to your function app in the portal and look at the Functions list. Try to find the activity functions - WriteBlob, NotifySubscribers, or WriteLog.

You might notice they don't appear in the same way as the timer trigger, or they might not appear at all. This is because activities use the ActivityTrigger binding, which is internal to the durable functions framework.

**Understanding the Implication**: Think about the architecture. The orchestrator calls activities using the CallActivityAsync method. These aren't HTTP endpoints or queue-based triggers - they're function-to-function calls managed internally by the durable functions runtime.

If you could disable an activity, what would happen? The orchestrator would try to call it, and the call would fail. The orchestrator would handle this as an exception. Depending on your retry policies, it might retry the activity, or it might fail the entire orchestration.

**The Real Answer**: Activity functions can't be disabled independently through the portal because they're not triggered by external events. They're invoked directly by the orchestrator through the durable functions framework. The only way to prevent an activity from running is to either not call it from the orchestrator code, or to disable the function that starts the orchestration.

This design makes sense when you think about workflows as atomic units. An orchestrator manages a workflow as a single logical operation. Disabling part of the workflow would leave it in an inconsistent state - you'd have orchestrations that start but can't complete.

**What You Can Disable**: You CAN disable the TimedOrchestratorStart function. This would prevent new orchestrations from starting, but it wouldn't affect any in-progress orchestrations - they would continue to completion.

Try it if you'd like - go to the timer trigger function in the portal, click "Disable", and watch what happens. No new heartbeats are created. Enable it again, and the workflow resumes on the next timer schedule.

## Cleanup

Before we finish, let's clean up your Azure resources to avoid unnecessary charges.

Stop the storage emulator by removing the Azurite Docker container using docker rm with the force flag.

Delete the entire resource group containing your function app and associated resources. Use the --no-wait flag to return immediately without waiting for deletion to complete in the background.

If you created the Service Bus namespace specifically for this lab, you can delete that resource group too. If you're using it for other labs or projects, keep it running.

Resource cleanup is important - even small resources can accumulate charges over time.
