# Azure SignalR Service - Hands-On Exercises

In these exercises, we'll work through a complete SignalR implementation, starting with a local application and progressing to a fully managed Azure deployment.

## Exercise 1: Running SignalR Locally

Let's begin by running a basic chat application that uses SignalR to broadcast messages to connected clients. We'll start with the application running on a single server to understand how SignalR works.

We'll use the .NET 6 SDK to run the application. Execute this command to start the chat server on port five thousand and five:

```
dotnet run --project src/signalr/chat --urls=http://localhost:5005/
```

Now, open two browser windows to localhost port five thousand and five. The application will prompt for a username and generate a random default. Try exchanging messages between the two browser windows. Notice how both browsers update without any client-side refreshing - this is SignalR in action. When a new message gets posted, the server broadcasts it to all connected clients using SignalR.

Here's an interesting test: stop the server application with Control-C or Command-C. What happens in the browser? The connection is lost, of course.

Now restart the application using the same command. You can reconnect the browser by pressing F5 to refresh. But notice something important - all previous messages are gone. The application doesn't have a persistence layer for storing data, and SignalR doesn't provide that functionality. SignalR is for real-time broadcasting, not data storage.

## Exercise 2: Observing the Scaling Problem

Now let's see what happens when we try to scale horizontally. Run a second copy of the website using a different port - five thousand and six:

```
dotnet run --project src/signalr/chat --urls=http://localhost:5006/
```

Open one browser to localhost port five thousand and five, and another browser to localhost port five thousand and six. Try sending messages between them.

Notice the problem? Messages aren't shared between the two servers. Users see completely different conversations depending on which server instance they're connected to. Each SignalR server maintains its own isolated list of connections. This is exactly the use case that Azure SignalR Service solves - we need a centralized hub for managing client connections across multiple web server instances.

## Exercise 3: Creating Azure SignalR Service

Let's create an Azure SignalR Service instance using the Azure CLI. First, we'll create a resource group:

```
az group create -n labs-signalr -l eastus --tags courselabs=azure
```

Now create the SignalR Service. We'll use the Free tier for this lab:

```
az signalr create -g labs-signalr --sku Free_F1 -l eastus -n <placeholder-signalr-name>
```

You might see a message indicating that the resource provider for SignalR Service is not registered in your subscription. The CLI will automatically register it for you. SignalR is one of the less common Azure services, so it's often not enabled by default.

Once created, browse to the SignalR Service in the Azure Portal. Under Keys, you can see the connection string that uses an access key for authentication. In the Connection strings section, you'll find a different format for using Managed Identities.

## Exercise 4: Connecting Local Application to Azure SignalR

Let's connect our local application to the Azure SignalR Service. First, copy the connection string for the access key from the Portal.

Now run two instances of your application again, but this time pass in configuration settings for Azure SignalR Service:

```
dotnet run --project src/signalr/chat --urls=http://localhost:5005/ --Azure:SignalR:Enabled=true --Azure:SignalR:ConnectionString='<placeholder-connection-string>'
```

In a separate terminal:

```
dotnet run --project src/signalr/chat --urls=http://localhost:5006/ --Azure:SignalR:Enabled=true --Azure:SignalR:ConnectionString='<placeholder-connection-string>'
```

Open one browser to each server - localhost five thousand and five and localhost five thousand and six. Now try exchanging messages. Success! The messages are shared between both clients, even though they're connected to different server instances. The Azure SignalR Service is acting as the central hub.

Try stopping one server and restarting it. Are the messages preserved? No - remember, SignalR is for broadcasting, not persistence. If you need to maintain state, that's your application's responsibility.

## Exercise 5: Deploying to Azure App Service

Now let's deploy the chat application to Azure App Service. Navigate to the source directory and use the webapp up command:

```
cd src/signalr/chat

az webapp up -g labs-signalr --os-type Linux --sku B1 --runtime dotnetcore:6.0 -n <placeholder-app-name>
```

This creates an App Service and deploys the application code in a single command.

## Exercise 6: Configuring Managed Identity Authentication

For production scenarios, we want to use Managed Identities instead of connection strings with embedded keys. Let's configure that now.

Set the SignalR connection string as an application setting, but this time using the Managed Identity format - notice we only include the endpoint, not an access key:

```
az webapp config appsettings set --settings Azure__SignalR__Enabled='true' Azure__SignalR__ConnectionString='Endpoint=https://<placeholder-signalr-name>.service.signalr.net;AuthType=azure.msi;Version=1.0;' -g labs-signalr -n <placeholder-app-name>
```

Browse to the application. It loads, but if you try sending a message, it fails. Open the browser's developer tools and you'll see five hundred errors. Check the Log stream in the Azure Portal for your Web App, and you'll see errors indicating that no Managed Identity endpoint was found.

The problem is that App Service applications are not created with a Managed Identity by default. Let's fix that:

```
az webapp identity assign -g labs-signalr -n <placeholder-app-name>
```

Try the application again. Still doesn't work. Check the logs again - they should tell you why.

The web app can now authenticate to SignalR using the Managed Identity, but the identity isn't authorized to use the service. Authentication and authorization are separate concerns.

## Exercise 7: Configuring Role-Based Access

The Managed Identity needs to be authorized with a role assignment. First, get the ID of the SignalR Service - this defines the scope for the role:

```
az signalr show -g labs-signalr --query id -n <placeholder-signalr-name>
```

Next, get the App Service's Managed Identity principal ID:

```
az webapp identity show --query principalId -o tsv -g labs-signalr -n <placeholder-app-name>
```

Now create a role assignment, giving the App Service's identity the SignalR App Server role:

```
az role assignment create --role 'SignalR App Server' --assignee-object-id <placeholder-principal-id> --scope "<placeholder-signalr-id>"
```

You can verify this in the Portal. Open the SignalR Service, navigate to Access control (IAM), browse to Roles, select SignalR App Server, and view the assignments. You should see your Web App listed.

The role assignment can take a few minutes to propagate through Azure's authorization system, but once it does, the application will start working without requiring a restart.

## Exercise 8: Lab Challenge

For the lab challenge, explore SignalR's debugging capabilities. In the Azure Portal, configure tracing for messages and open the Live Trace tool. Open the chat site in multiple browser windows and send messages between them. Observe what the trace shows you about message flow.

Here's a security question to consider: if someone obtained your SignalR connection details, could they hack the site to broadcast messages to all users? What security boundaries does Azure SignalR Service provide?

## Cleanup

When you're finished, delete the resource group to remove all resources:

```
az group delete -y --no-wait -n labs-signalr
```

In these exercises, we've seen how Azure SignalR Service solves the scaling challenge for real-time communication, and how to implement secure authentication using Managed Identities with role-based access control.
