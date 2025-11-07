# Azure SignalR Service

## Reference

SignalR is a technology enabling two-way communication over the internet, providing a way for web applications to push updates to browsers. This supports asynchronous delivery to the front end, which is essential for modern real-time applications. SignalR is Microsoft's customization of WebSockets for .NET, originally designed as server technology you run within your own application. However, the challenge with self-hosted SignalR is that each server maintains its own isolated list of connected clients in memory, making horizontal scaling difficult. When you have multiple web servers, clients connected to different servers can't communicate with each other.

Azure SignalR Service solves this scaling challenge by moving SignalR into its own managed component. Your web application no longer deals with clients directly - instead, it sends update notifications to the SignalR Service, which acts as a central broadcast hub distributing messages to all connected clients regardless of which web server they came through. This architectural shift enables true horizontal scaling while maintaining real-time communication.

## Run a Local SignalR Website

Understanding the problem that Azure SignalR Service solves starts with seeing SignalR running locally.

**Run the Chat Application**: We have a basic chat application that uses SignalR to broadcast messages to connected clients. The code implementation details aren't the focus here - what matters is observing the behavior. We're running it using dotnet run with the --project parameter pointing to src/signalr/chat and --urls specifying http://localhost:5005/ as the listening address. This starts the chat server and makes it accessible locally.

**Test Real-Time Updates**: Open two browser windows to http://localhost:5005/ - the application prompts for a username and generates a random default suggestion. Exchange messages between the two browser windows and observe how both browsers update without any client-side refreshing. This is SignalR in action. When a new message gets posted, the server broadcasts it using SignalR's hub abstraction, and all connected clients receive it instantly.

**Test Server Failure**: Stop the server application with Ctrl-C or Cmd-C. Watch what happens in the browsers - the connection is lost immediately, and clients typically show a disconnected state or error. This demonstrates that SignalR maintains persistent connections between clients and server.

**Observe Message Loss**: Restart the application using the same command and reconnect the browsers by pressing F5. Notice that all previous messages are gone. The application doesn't have a persistence layer for storing data, and SignalR doesn't provide that functionality. SignalR is for real-time broadcasting, not data storage - it's a communication mechanism, not a database. This distinction is crucial for understanding its role in application architecture.

---

## Observing the Scaling Problem

Now let's see what happens when we try to scale horizontally by running multiple instances.

**Run Second Instance**: Run another copy of the website using a different port with dotnet run, changing the --urls parameter to http://localhost:5006/ so it doesn't conflict with the first instance. You now have two completely independent web servers running.

**Test Cross-Server Communication**: Open one browser window to localhost:5005 and another to localhost:5006. Try sending messages between them, with one user posting while watching the other browser.

**Observe the Problem**: Messages aren't shared between the two servers. Users see completely different conversations depending on which server instance they're connected to. Each SignalR server maintains its own isolated list of connections in memory - there's no communication between the two server processes. This is exactly the use case that Azure SignalR Service solves. We need a centralized hub for managing client connections across multiple web server instances. Without it, horizontal scaling breaks real-time communication.

---

## Create SignalR Service

Let's create an Azure SignalR Service instance to solve this scaling problem.

**Create Resource Group**: We're creating a resource group using az group create with -n set to "labs-signalr", -l for East US location, and --tags set to "courselabs=azure" for resource tracking.

**Create SignalR Service**: We're using az signalr create to establish the SignalR Service. The parameters include -g specifying the resource group, --sku set to Free_F1 for the free tier which is perfect for learning and testing, -l for location, and -n for a unique name. Remember that SignalR service names must be globally unique across Azure.

**Resource Provider Registration**: You might see a message indicating that the resource provider for SignalR Service is not registered in your subscription. The CLI will automatically register it for you, which takes a moment. SignalR is one of the less common Azure services, so it's often not enabled by default in new subscriptions.

**Explore Authentication Options**: Once created, browse to the SignalR Service in the Azure Portal. Navigate to the Keys blade on the left menu. Under Keys, you can see the connection string that uses an access key for authentication - this is the simpler approach for development. In the Connection strings section, you'll find a different format for using Managed Identities, which is the recommended approach for production since it doesn't require managing secrets.

---

## Connect Local Application to Azure SignalR

Let's connect our local application to the Azure SignalR Service to demonstrate how it solves the scaling problem.

**Get Connection String**: Copy the connection string for the access key from the Portal - click the copy button next to the connection string field. This contains the endpoint and authentication credentials.

**Run Multiple Instances with Azure SignalR**: We're running two instances of the application again, but this time passing configuration settings for Azure SignalR Service. For the first instance, use dotnet run with --project pointing to src/signalr/chat, --urls set to http://localhost:5005/, --Azure:SignalR:Enabled set to true to activate SignalR Service mode, and --Azure:SignalR:ConnectionString with your actual connection string in quotes.

**Run Second Instance**: In a separate terminal, run a second instance with identical parameters except change --urls to http://localhost:5006/ so it listens on a different port. Both instances use the exact same SignalR connection string, pointing to the same Azure service.

**Test Cross-Server Communication**: Open one browser window to localhost:5005 and another to localhost:5006. Now try exchanging messages between users on different server instances. Success! The messages are shared between both clients, even though they're connected to different server instances. The Azure SignalR Service is acting as the central hub, coordinating all connections and message broadcasts across both web servers.

**Test Persistence**: Try stopping one server and restarting it. Are the messages preserved after restart? No - remember, SignalR is for broadcasting real-time updates, not persistence. If you need to maintain message history or state, that's your application's responsibility, typically using a database or cache. SignalR handles the real-time communication channel but doesn't store data.

---

## Deploy to Azure App Service

Now let's deploy the chat application to Azure App Service to see it running entirely in the cloud.

**Deploy Application**: Navigate to the source directory using cd src/signalr/chat, then use the webapp up command to create and deploy everything in one operation. We're using az webapp up with -g specifying the labs-signalr resource group, --os-type Linux for the operating system, --sku B1 for the Basic pricing tier, --runtime dotnetcore:6.0 to specify .NET 6, and -n with a unique app name.

**Understanding webapp up**: This single command does a lot of work - it creates an App Service Plan if one doesn't exist, creates a Web App with your specified name, packages your application code, and deploys it to Azure. Wait for the command to complete, which typically takes a few minutes.

---

## Configure Managed Identity Authentication

For production scenarios, we want to use Managed Identities instead of connection strings with embedded keys. This is more secure because there are no secrets to manage or rotate.

**Set Application Settings**: We're setting the SignalR connection string as an application setting using az webapp config appsettings set. Notice we're using a different connection string format this time - we're including only the endpoint with --settings including Azure__SignalR__Enabled set to 'true' and Azure__SignalR__ConnectionString with the endpoint URL followed by AuthType=azure.msi to specify Managed Identity authentication and Version=1.0. Double underscores in the setting names represent nested configuration in .NET applications.

**Test and Observe Failure**: Browse to the application URL shown in the previous command output. It loads the initial page, but if you try sending a message, it fails. Open the browser's developer tools by pressing F12 and check the Network tab - you'll see 500 errors. Check the Log stream in the Azure Portal by navigating to your Web App, finding Log stream in the Monitoring section, and you'll see errors indicating that no Managed Identity endpoint was found.

**Understanding the Problem**: The issue is that App Service applications are not created with a Managed Identity by default - it's an optional feature you need to explicitly enable. This security-by-default approach prevents inadvertent identity creation.

**Enable Managed Identity**: Let's fix that using az webapp identity assign with -g for the resource group and -n for the app name. This creates a system-assigned managed identity for the web app.

**Test Again and Observe Authorization Failure**: Try the application again by refreshing your browser. Still doesn't work. Check the logs again in the Log stream - they should tell you why. The error message now indicates authentication succeeded, but authorization failed.

**Understanding Authentication vs Authorization**: The web app can now authenticate to SignalR using the Managed Identity - it can prove who it is. But the identity isn't authorized to use the service - authentication and authorization are separate concerns. We've proven identity, but not granted permissions.

---

## Configure Role-Based Access

The Managed Identity needs to be authorized with a role assignment to actually access SignalR.

**Get SignalR Service ID**: First, we're getting the ID of the SignalR Service using az signalr show with -g for resource group, --query id to extract just the ID field, and -n for the service name. This resource ID defines the scope for the role assignment - it identifies exactly which SignalR service we're granting access to.

**Get Managed Identity Principal ID**: Next, we're getting the App Service's Managed Identity principal ID using az webapp identity show with --query principalId to extract the principal ID, -o tsv for tab-separated output without quotes, -g for the resource group, and -n for the app name. This unique identifier represents the managed identity we just created.

**Create Role Assignment**: Now we're creating a role assignment using az role assignment create. We're specifying --role 'SignalR App Server' which is a built-in Azure role that grants permissions to send messages and manage connections. The --assignee-object-id parameter takes the principal ID we just retrieved, and --scope takes the SignalR resource ID. This command essentially says "allow this web app's identity to act as an app server for this specific SignalR service."

**Verify in Portal**: You can verify this in the Portal by opening the SignalR Service, navigating to Access control (IAM) in the left menu, browsing to the Roles tab, selecting SignalR App Server from the list, and viewing the assignments. You should see your Web App listed there with its managed identity.

**Wait for Propagation**: The role assignment can take a few minutes to propagate through Azure's authorization system - it's not always instantaneous. But once it does propagate, the application will start working without requiring a restart. The application continuously attempts to connect, and once authorization succeeds, messages will flow normally.

---

## Lab

SignalR provides powerful debugging capabilities worth exploring for production troubleshooting.

**Configure Diagnostics**: In the Azure Portal, navigate to your SignalR Service and find the Diagnostic settings blade. Configure tracing for messages by enabling logs for various categories. This captures detailed information about SignalR operations.

**Use Live Trace**: Open the Live Trace tool from the left menu - this provides real-time visibility into SignalR traffic. Open the chat site in multiple browser windows and send messages between them while watching the Live Trace. Observe what the trace shows you about message flow - you'll see connections being established, messages being received by the hub, and broadcasts being sent to connected clients. This is incredibly useful for debugging production issues.

**Security Consideration**: Here's an important security question to consider - if someone obtained your SignalR connection details, whether the endpoint URL and a valid connection string or managed identity credentials, could they hack the site to broadcast messages to all users? What security boundaries does Azure SignalR Service provide? Think about the authentication model. SignalR authenticates app servers, but the app server is responsible for authenticating users. SignalR doesn't directly authenticate end users, so malicious actors with app server credentials could potentially broadcast messages. This highlights why managed identities and proper access control are so important - they limit the scope of compromise if credentials are exposed.

---

## Cleanup

When you're finished with the lab, proper cleanup prevents ongoing charges.

**Delete Resource Group**: We're using az group delete to remove all resources. The -y flag confirms without prompting, and --no-wait returns immediately without waiting for the deletion to complete. This removes everything we created - the SignalR Service, App Service Plan, Web App, and the resource group itself.

In these exercises, we've seen how Azure SignalR Service solves the scaling challenge for real-time communication, allowing multiple web server instances to share connections through a central hub. We've also learned how to implement secure authentication using Managed Identities with role-based access control, eliminating the need to manage connection strings with embedded secrets. These patterns apply broadly to building secure, scalable Azure applications beyond just SignalR scenarios.
