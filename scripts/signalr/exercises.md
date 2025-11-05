# Azure SignalR Service - Hands-On Exercises

In these exercises, we'll work through a complete SignalR implementation, starting with a local application and progressing to a fully managed Azure deployment.

## Exercise 1: Running SignalR Locally

Let's begin by running a basic chat application that uses SignalR to broadcast messages to connected clients. We'll start with the application running on a single server to understand how SignalR works at its core.

We'll use the .NET 6 SDK to run the application. We're executing the dotnet run command with the --project parameter pointing to src/signalr/chat, and the --urls parameter set to http://localhost:5005/ to specify which port the application listens on. This starts the chat server and makes it accessible on localhost port five thousand and five.

Now, open two browser windows to localhost port five thousand and five. The application will prompt for a username and generate a random default suggestion. Try exchanging messages between the two browser windows. Notice how both browsers update without any client-side refreshing - this is SignalR in action, using WebSockets to push updates from server to client in real-time. When a new message gets posted, the server broadcasts it to all connected clients using SignalR's hub abstraction.

Here's an interesting test: stop the server application with Control-C on Windows and Linux or Command-C on Mac. What happens in the browser? The connection is lost immediately, and clients typically show a disconnected state or error.

Now restart the application using the same dotnet run command. You can reconnect the browser by pressing F5 to refresh. But notice something important - all previous messages are gone. The application doesn't have a persistence layer for storing data, and SignalR doesn't provide that functionality either. SignalR is for real-time broadcasting, not data storage - it's a communication mechanism, not a database.

## Exercise 2: Observing the Scaling Problem

Now let's see what happens when we try to scale horizontally by running multiple instances. Run a second copy of the website using a different port - we're using the same dotnet run command but changing the --urls parameter to http://localhost:5006/ so it doesn't conflict with the first instance.

Open one browser window to localhost port five thousand and five, and another browser window to localhost port five thousand and six. Try sending messages between them, having one user post a message while watching the other browser.

Notice the problem? Messages aren't shared between the two servers. Users see completely different conversations depending on which server instance they're connected to. Each SignalR server maintains its own isolated list of connections in memory - there's no communication between the two server processes. This is exactly the use case that Azure SignalR Service solves - we need a centralized hub for managing client connections across multiple web server instances. Without it, horizontal scaling breaks the real-time communication.

## Exercise 3: Creating Azure SignalR Service

Let's create an Azure SignalR Service instance using the Azure CLI to solve this scaling problem. First, we'll create a resource group using az group create with -n set to "labs-signalr", -l for East US location, and --tags set to "courselabs=azure" for resource tracking.

Now create the SignalR Service using az signalr create. We're specifying the resource group with -g, using --sku Free_F1 for the free tier which is perfect for learning and testing, setting the location with -l, and providing a unique name with -n. Remember that SignalR service names must be globally unique.

You might see a message indicating that the resource provider for SignalR Service is not registered in your subscription. The CLI will automatically register it for you, which takes a moment. SignalR is one of the less common Azure services, so it's often not enabled by default in new subscriptions.

Once created, browse to the SignalR Service in the Azure Portal. Navigate to the Keys blade on the left menu. Under Keys, you can see the connection string that uses an access key for authentication - this is the simpler approach for development. In the Connection strings section, you'll find a different format for using Managed Identities, which is the recommended approach for production since it doesn't require managing secrets.

## Exercise 4: Connecting Local Application to Azure SignalR

Let's connect our local application to the Azure SignalR Service to demonstrate how it solves the scaling problem. First, copy the connection string for the access key from the Portal - click the copy button next to the connection string field.

Now run two instances of your application again, but this time pass in configuration settings for Azure SignalR Service. For the first instance, we're using dotnet run with --project pointing to src/signalr/chat, --urls set to http://localhost:5005/, --Azure:SignalR:Enabled set to true to activate SignalR Service mode, and --Azure:SignalR:ConnectionString with your actual connection string in quotes.

In a separate terminal, run a second instance with the same parameters except change --urls to http://localhost:5006/ so it listens on a different port. Both instances use the exact same SignalR connection string, pointing to the same Azure service.

Open one browser window to localhost five thousand and five and another to localhost five thousand and six. Now try exchanging messages between users on different server instances. Success! The messages are shared between both clients, even though they're connected to different server instances. The Azure SignalR Service is acting as the central hub, coordinating all connections and message broadcasts across both web servers.

Try stopping one server and restarting it. Are the messages preserved after restart? No - remember, SignalR is for broadcasting real-time updates, not persistence. If you need to maintain message history or state, that's your application's responsibility, typically using a database or cache. SignalR handles the real-time communication channel, but doesn't store data.

## Exercise 5: Deploying to Azure App Service

Now let's deploy the chat application to Azure App Service to see it running entirely in the cloud. Navigate to the source directory using cd src/signalr/chat, then use the webapp up command to create and deploy everything in one operation. We're using az webapp up with -g to specify the labs-signalr resource group, --os-type Linux for the operating system, --sku B1 for the Basic pricing tier, --runtime dotnetcore:6.0 to specify .NET 6, and -n with a unique app name.

This single command does a lot - it creates an App Service Plan if one doesn't exist, creates a Web App with your specified name, packages your application code, and deploys it to Azure. Wait for the command to complete, which typically takes a few minutes.

## Exercise 6: Configuring Managed Identity Authentication

For production scenarios, we want to use Managed Identities instead of connection strings with embedded keys. This is more secure because there are no secrets to manage or rotate. Let's configure that now.

Set the SignalR connection string as an application setting using az webapp config appsettings set. Notice we're using a different connection string format this time - we're including only the endpoint with --settings Azure__SignalR__Enabled set to 'true' and Azure__SignalR__ConnectionString including the endpoint URL followed by parameters AuthType=azure.msi to specify Managed Identity authentication and Version=1.0. Double underscores in the setting names represent nested configuration in .NET applications.

Browse to the application URL shown in the previous command output. It loads the initial page, but if you try sending a message, it fails. Open the browser's developer tools - press F12 in most browsers - and you'll see five hundred errors in the network tab. Check the Log stream in the Azure Portal by navigating to your Web App, finding Log stream in the Monitoring section, and you'll see errors indicating that no Managed Identity endpoint was found.

The problem is that App Service applications are not created with a Managed Identity by default - it's an optional feature you need to enable. Let's fix that using az webapp identity assign with -g for the resource group and -n for the app name. This creates a system-assigned managed identity for the web app.

Try the application again by refreshing your browser. Still doesn't work. Check the logs again in the Log stream - they should tell you why. The error message now indicates authentication succeeded, but authorization failed.

The web app can now authenticate to SignalR using the Managed Identity - it can prove who it is. But the identity isn't authorized to use the service - authentication and authorization are separate concerns. We've proven identity, but not granted permissions.

## Exercise 7: Configuring Role-Based Access

The Managed Identity needs to be authorized with a role assignment to actually access SignalR. First, get the ID of the SignalR Service using az signalr show with -g for resource group, --query id to extract just the ID field, and -n for the service name. This resource ID defines the scope for the role assignment - it identifies exactly which SignalR service we're granting access to.

Next, get the App Service's Managed Identity principal ID using az webapp identity show with --query principalId to extract the principal ID, -o tsv for tab-separated output without quotes, -g for the resource group, and -n for the app name. This unique identifier represents the managed identity we just created.

Now create a role assignment using az role assignment create. We're specifying --role 'SignalR App Server' which is a built-in Azure role that grants permissions to send messages and manage connections. The --assignee-object-id parameter takes the principal ID we just retrieved, and --scope takes the SignalR resource ID. This command essentially says "allow this web app's identity to act as an app server for this specific SignalR service."

You can verify this in the Portal by opening the SignalR Service, navigating to Access control (IAM) in the left menu, browsing to the Roles tab, selecting SignalR App Server from the list, and viewing the assignments. You should see your Web App listed there with its managed identity.

The role assignment can take a few minutes to propagate through Azure's authorization system - it's not always instantaneous. But once it does propagate, the application will start working without requiring a restart. The application continuously attempts to connect, and once authorization succeeds, messages will flow normally.

## Exercise 8: Lab Challenge

For the lab challenge, explore SignalR's debugging capabilities. In the Azure Portal, navigate to your SignalR Service and find the Diagnostic settings blade. Configure tracing for messages by enabling logs for various categories. Then open the Live Trace tool from the left menu - this provides real-time visibility into SignalR traffic.

Open the chat site in multiple browser windows and send messages between them while watching the Live Trace. Observe what the trace shows you about message flow - you'll see connections being established, messages being received by the hub, and broadcasts being sent to connected clients. This is incredibly useful for debugging production issues.

Here's a security question to consider: if someone obtained your SignalR connection details - the endpoint URL and a valid connection string or managed identity credentials - could they hack the site to broadcast messages to all users? What security boundaries does Azure SignalR Service provide? Think about the authentication model - SignalR authenticates app servers, but the app server is responsible for authenticating users. SignalR doesn't directly authenticate end users, so malicious actors with app server credentials could potentially broadcast messages. This highlights why managed identities and proper access control are so important.

## Cleanup

When you're finished with the lab, delete the resource group to remove all resources using az group delete. The -y flag confirms without prompting, and --no-wait returns immediately without waiting for the deletion to complete. This removes everything we created - the SignalR Service, App Service Plan, Web App, and the resource group itself.

In these exercises, we've seen how Azure SignalR Service solves the scaling challenge for real-time communication, allowing multiple web server instances to share connections. We've also learned how to implement secure authentication using Managed Identities with role-based access control, eliminating the need to manage connection strings with embedded secrets. These patterns apply broadly to building secure, scalable Azure applications.
