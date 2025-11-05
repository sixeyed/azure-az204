# Azure Durable Functions: Human Interaction Pattern - Lab Exercises

## Conversational Narration Script

---

## Introduction to the Lab

Welcome to the hands-on portion of our Azure Durable Functions Human Interaction lab. In this session, we're going to build a complete two-factor authentication system using durable functions and SMS messaging. This is a realistic scenario you might implement in production applications, and it perfectly demonstrates how durable functions handle human-in-the-loop workflows.

Before we dive into the code, there's some setup we need to do with Twilio, which is the service we'll use to send SMS messages.

---

## Setting Up Twilio Account

First, you'll need to create a free Twilio account. Twilio has a generous free tier that's perfect for development and learning. Don't worry - you won't need to enter any payment details for this lab.

*[SHOW ON SCREEN: Twilio signup page]*

When you sign up, you will need to provide a real email address and your actual mobile phone number. Both of these get validated, so you can't use dummy data. But this is important - you'll be sending SMS messages to this number during testing, so make sure it's a number you have access to.

Once your account is created, navigate to the API keys and tokens section in your Twilio console. Here you'll find your account credentials. You'll need to note down two things: your Account SID and your Auth Token.

*[SHOW ON SCREEN: Twilio credentials page with SID and Auth Token visible]*

These are sensitive credentials, so keep them secure. We'll add them to our function configuration shortly, but never commit them to source control.

---

## Creating a Twilio Phone Number

Next, we need to get a phone number that will be used as the sender when your function sends SMS messages. In the Twilio console, look for the option to buy a number - there's a Jump To box at the top where you can type "buy a number".

When you search for available numbers, you'll see various capabilities listed. For this lab, we only need SMS capability, so you can untick voice and other options. This will give you more numbers to choose from.

*[SHOW ON SCREEN: Twilio number search with SMS capability selected]*

Pick any number you like. The purchase will use credits from your free tier allowance. Make a note of this number - you'll need it in your function configuration.

Great! Now we have everything we need from Twilio. Let's look at the function code.

---

## Understanding the Function Architecture

Before we run anything, let's understand what we're building. The code is organized into three main files, and each has a specific role in the workflow.

*[SHOW ON SCREEN: File structure of the 2FA folder]*

First, we have Authenticate dot C S. This is our HTTP trigger - the entry point to the workflow. It expects an HTTP POST request with the phone number as a URL parameter.

Second is SmsVerify dot C S - this is our orchestrator function. It coordinates the whole workflow, calling the Twilio activity to send the message, then starting a timer. The user has two minutes to respond before authentication fails.

Third is SmsChallenge dot C S - this is the activity function that does the actual work of calling Twilio. It generates a random four-digit code and sends it via SMS.

Notice how the orchestrator doesn't directly call Twilio. It calls the activity function, which maintains good separation of concerns. The orchestrator focuses on workflow logic, while the activity handles the integration details.

---

## Configuring Local Settings

Now let's get this running locally. First, we need our local development environment set up. Make sure Docker Desktop is running, then start the Azure Storage emulator called Azurite.

*[SHOW ON SCREEN: Docker command to run Azurite]*

This gives us the local storage our durable function needs for state management.

Next, we need to create our local settings file. This is where we'll put those Twilio credentials we noted earlier. Create a file called local dot settings dot json in the 2FA folder.

*[SHOW ON SCREEN: Creating local.settings.json file]*

The file needs several configuration values. The Azure Web Jobs Storage setting points to our local emulator. The Functions Worker Runtime is set to dotnet. Then we have our three Twilio settings: the Account SID, the Auth Token, and the phone number.

One important note about the phone number - you need to use E dot 164 formatting. This is the international standard format that starts with a plus sign, then the country code, then the number with no spaces or dashes. For example, if you have a US number like 555-123-4567, you'd format it as plus one five five five one two three four five six seven.

*[SHOW ON SCREEN: Example of E.164 formatting for different countries]*

A quick warning: do not commit this local settings file to GitHub. Twilio actively monitors public repositories for exposed credentials, and if they find yours, they'll revoke them and send you a not-so-friendly email. The file should already be in your git ignore, but it's worth double-checking.

---

## Running the Function Locally

Alright, let's run this function. Navigate to the 2FA folder in your terminal and run "func start".

*[SHOW ON SCREEN: Terminal running func start command]*

You'll see the Azure Functions runtime start up, and after a moment, it will list the available functions. You should see all three of our functions registered.

Now comes the fun part. We're going to trigger the authentication workflow. Open a new terminal window and use curl to make an HTTP POST request to the Authenticate function. Remember to use your own mobile number in E dot 164 format.

*[SHOW ON SCREEN: Curl command with phone number parameter]*

Hit enter, and watch your function logs. You should see messages indicating that the orchestrator started, and the SMS challenge activity is executing. It will log that it's sending a verification code to your phone number - though the number will be partially masked in the logs for privacy.

*[SHOW ON SCREEN: Function execution logs]*

More importantly, check your phone! You should receive an SMS message with a four-digit code. This is where the human interaction comes in - the function is now paused, waiting for you to respond.

---

## Responding to the Challenge

Look at the response from your curl request. It's a JSON object with several URLs. These are the management endpoints for your orchestration instance. Each running orchestration gets its own unique instance ID, and these URLs let you interact with that specific instance.

*[SHOW ON SCREEN: JSON response highlighting sendEventPostUri]*

The one we need right now is called sendEventPostUri. This is how we send the external event that will resume our waiting orchestration. You'll see it has a placeholder for the event name. We need to replace that with "SmsChallengeResponse" - that's the specific event our orchestrator is waiting for.

Now construct a new curl command. It's an HTTP POST to that URL, with your verification code as the request body. The content type should be JSON, and you need to include all the query string parameters - the task hub, connection, and code parameters are all required.

*[SHOW ON SCREEN: Curl command to send event with verification code]*

I'll be honest, this curl command is a bit fiddly. You might need a few attempts to get the syntax exactly right. But remember, you have two minutes before the timer expires, so work carefully but don't panic.

Execute the command and watch the function logs. If your code matches what was sent in the SMS, you should see a message saying "Authorized! User responded correctly". If the code is wrong, you'll see an authentication failure message.

*[SHOW ON SCREEN: Successful authorization log message]*

You can also check the status by calling the status query get URI from the original response. This will show you the current state of the orchestration, and if authentication succeeded, the output will be true.

---

## What Happens on Timeout

Try running the workflow again, but this time, don't respond within the two-minute window. Just let it sit. Watch what happens in the logs.

*[SHOW ON SCREEN: Timeout message in logs]*

After two minutes, the durable timer expires, and the orchestration continues. Because no response was received, the authentication fails. This timeout mechanism is crucial for real-world applications - you can't have workflows waiting indefinitely for human input that might never come.

This combination of external events and durable timers is what makes the Human Interaction pattern so powerful and reliable.

---

## Deploying to Azure

Now let's deploy this to a real Azure environment. First, we'll create a resource group for our function app.

*[SHOW ON SCREEN: Azure CLI command to create resource group]*

Next, create a storage account. Remember, every Azure Function needs a storage account for its internal state management.

*[SHOW ON SCREEN: Azure CLI command to create storage account]*

Now create the function app itself. We're using the consumption plan, which means you only pay for execution time. The runtime is dotnet, and we're using Functions version four.

*[SHOW ON SCREEN: Azure CLI command to create function app]*

Before we can deploy our code, we need to add those Twilio credentials to the function app settings. You can do this through the portal or with the Azure CLI. You need to add three settings: TwilioAccountSid, TwilioAuthToken, and TwilioPhoneNumber.

*[SHOW ON SCREEN: Portal view of application settings]*

Use the same values you had in your local settings file. These settings are stored securely in Azure and are available to your function as environment variables.

Now we're ready to deploy. From the 2FA folder, run "func azure functionapp publish" followed by your function name.

*[SHOW ON SCREEN: Function deployment in progress]*

The deployment will package your code, upload it to Azure, and configure the function app. You'll see progress messages as each function is published.

---

## Testing in Azure

Once deployment completes, open the Azure Portal and navigate to your function app. Click on the Authenticate function to open its details.

*[SHOW ON SCREEN: Azure Portal function overview]*

You can test it right here in the portal using the Test slash Run feature. You'll need to switch the method to POST and add your phone number as a query parameter.

*[SHOW ON SCREEN: Portal test interface with phone number parameter]*

Click Run, and you should receive another SMS. But here's where the Azure Portal experience falls short. You'll get back the same JSON response with the URLs for sending events and checking status, but there's no built-in way in the portal to actually call those URLs. You still need to construct curl commands just like you did locally.

This is one of those areas where having a proper front-end application would make the user experience much smoother. The raw HTTP interface is functional, but it's definitely not user-friendly.

---

## Lab Challenge

Here's something to think about. In a real application, you wouldn't want your web frontend constantly polling the status endpoint to see if the user has been authenticated. That's inefficient and creates unnecessary load.

How could you redesign this architecture so the web application gets notified when authentication completes, rather than having to repeatedly check? Remember, orchestrators can call other activities at any point in the workflow. What Azure services might help here?

*[PAUSE FOR THOUGHT]*

One approach would be to add another activity function that posts a message to an Azure Queue when authentication succeeds or fails. Your web application could then listen to that queue and react immediately when a message arrives. No polling required, and the architecture scales beautifully.

---

## Cleanup

When you're finished experimenting, don't forget to clean up your resources. Stop the Azurite container if it's still running.

*[SHOW ON SCREEN: Docker command to remove Azurite]*

And delete your Azure resource group to avoid any charges.

*[SHOW ON SCREEN: Azure CLI delete resource group command]*

---

## Wrapping Up

Great work! You've successfully built and deployed a human interaction workflow using Azure Durable Functions. You've seen how external events let you send data into a running orchestration, how durable timers implement timeouts, and how these components work together to create reliable, serverless workflows that interact with users.

This pattern is incredibly versatile. Any time you need to pause a workflow for human input - approvals, verifications, decisions - the human interaction pattern is your solution. And because it's built on durable functions, you get all the benefits of serverless computing: automatic scaling, pay-per-execution pricing, and stateful orchestration without managing infrastructure.
