# Docker Compose - Exercises Narration Script

## Exercise 1: Understanding Multi-Container Apps

Let's start by understanding why we need Docker Compose in the first place.

We're going to run a simple web application - this is the front-end component for a random number generator. We're running the container in detached mode on port 8088 with a specific name so we can reference it easily.

Browse to localhost port 8088. The web page loads, showing a button that says "Get a random number". Click the button to request a number. After a few seconds, instead of getting a result, we see an error message: "RNG service unavailable!"

This is a perfect example of why we need to understand distributed applications. The web front-end is only one piece of the puzzle - it's trying to call a backend REST API service that doesn't exist yet.

Let's check the application logs to see what's happening. Looking at the logs, we can see the web application is trying to connect to a backend REST API at the address "numbers-api" on port 80. But there's no such service running - we only started the web container.

We could start the API container with another docker run command, but we'd need to know the exact image name, configure the ports correctly, and set up the networking so the containers can communicate using DNS names. This is where Docker Compose becomes invaluable - it handles all of this configuration declaratively.

## Exercise 2: Simple Compose Definition

Let's look at a simple Compose file first to understand the basic structure. Open the file at labs/docker-compose/nginx/docker-compose.yml.

This is about as simple as a Compose file gets. It defines a single service named "web" that uses the nginx alpine image version 1.18 and publishes port 8082 to the host.

You might ask - why bother with a Compose file for just one container? Well, this file serves as documentation. Anyone looking at this file immediately knows which image version to use, which port the application listens on, and how to start it. It's executable documentation that captures the operational knowledge of running this application.

Let's run this application using the docker-compose CLI. We're using the -f flag to specify the file path since it's not in the current directory, followed by the up command to start the application.

Notice that Compose shows us the logs in real-time by default. The container starts up and we can browse to localhost port 8082 to verify it's working.

Use Control-C to exit. Notice that stopping the Compose command also stops the container automatically. This is useful for development workflows where you want to see logs as you work.

## Exercise 3: Multi-Container Apps in Compose

Now let's look at a more realistic example - the complete random number generator application with both the web front-end and the API backend.

Open the file at labs/docker-compose/rng/v1.yml.

In just 20 lines of YAML, we've defined a complete distributed application. There are two services: "rng-api" for the backend API and "rng-web" for the front-end. Each service specifies its container image and port mappings. The web service includes an environment variable to configure logging levels. Both services connect to the same container network called "app-net", enabling them to communicate. The network itself is defined at the bottom of the file.

This declarative approach is powerful - you describe what you want, not the steps to achieve it.

Let's run this application in detached mode using the -d flag. Watch as Compose creates the network first, then both containers. The order of operations is intelligent - Compose ensures dependencies are satisfied.

Now we can use Compose commands to manage our application. The ps command shows just the containers for this application, not all Docker containers on your machine. This scoping is one of Compose's advantages.

We can also view the logs for all services together. Compose interleaves the log output and prefixes each line with the service name, making it easy to track what's happening across your distributed application.

Remember, these are standard Docker containers under the hood. We can still use the regular Docker CLI to see them with docker ps. The container names include the project name prefix, which Compose derives from the directory name.

Now let's browse to localhost port 8090 and try to get a random number. Click the button... and it still doesn't work! We need to debug this application.

## Exercise 4: Debugging with Compose

When a distributed application fails, we need to isolate the problem systematically. The web app uses the API to get random numbers. There are only two possibilities: either the API isn't working correctly, or the web app can't connect to the API.

Let's check if the API works independently. The Compose file shows it publishes port 8089. We can verify the exact port mapping using docker-compose port command, specifying the service name "rng-api" and the internal port 80.

Now let's test the API directly using curl to access localhost port 8089 with the /rng endpoint.

Good! We get a random number back. So the API is working correctly. The problem must be connectivity from the web app to the API.

Let's check the web container logs. Looking at the logs, we can see the web app is trying to connect to the domain "numbers-api". Let's test if that domain is resolvable from within the web container.

We're using docker exec to run the nslookup command inside the web container, checking if "numbers-api" can be resolved. The DNS lookup fails - the name can't be resolved.

There's the problem! If we look back at the Compose file, the API service is named "rng-api", not "numbers-api". In Docker Compose, the service name becomes the DNS name that other containers use for service discovery. We have a mismatch between what the web app expects and what the service is actually named.

## Exercise 5: Updating with Desired State

We could fix this by renaming the service in the Compose file to match what the web app expects, but there's a better way. The web application supports a configuration setting for the API URL.

Open the file at labs/docker-compose/rng/v2.yml.

This updated version adds an environment variable to the web service called "RngApi__Url" that points to "http://rng-api/rng" - using the correct service name from our Compose file. Notice the double-underscore convention - this is how .NET configuration handles hierarchical settings.

The file also increases the logging level for the API by adding a "Logging__LogLevel__Default" environment variable set to Information for more detailed logging.

Now here's where we see the desired-state approach in action. We don't need to stop and remove our containers and start over from scratch. We just update the specification file and run up again with the new file.

Watch what happens. Compose compares the current state with the desired state defined in the file. It sees that the API container configuration hasn't changed, so it leaves it running untouched. But the web container has new environment variables, so Compose gracefully stops the old container and creates a new one with the updated configuration.

This is the power of desired-state deployment. You change your YAML specification, run up, and Compose figures out what needs to change. It's declarative infrastructure - you describe the end state, not the steps to get there.

Let's follow the logs using the -f flag to stream them in real-time.

Now browse to localhost port 8090 and click to get a random number. Success! The application works, and we can see the API logs showing our requests coming in with detailed information now that logging is set to Information level.

Use Control-C to stop following the logs. The containers continue running in the background.

## Lab Challenge

Your challenge is to extend this application by adding an Nginx container as a reverse proxy.

You'll need to add a new network to the Compose file called something like "proxy-net". Define an Nginx service that connects to both the new proxy network and the existing app-net network. This demonstrates an important Compose feature - containers can connect to multiple networks simultaneously.

Then deploy the updated specification using docker-compose up -d.

After deployment, investigate these questions: What IP addresses does the Nginx container have? Use docker inspect to look at the network configuration. Can the RNG web container access Nginx, even though Nginx was created after the original containers? Test this using docker exec to ping or curl from one container to another.

This exercise will help you understand how Docker Compose manages networks dynamically and how containers can join multiple networks for different communication patterns.

Take some time to work through this challenge. If you get stuck, there are hints available in the hints file, and a complete solution in the lab solution materials.

## Summary

In these exercises, we've seen how Docker Compose simplifies multi-container application deployment. Instead of running multiple docker run commands with complex networking configuration, you write one declarative YAML file that describes your entire application stack.

Compose provides clear documentation of application architecture - anyone can read the docker-compose.yml file and understand how the application is structured, which services it includes, how they communicate, and what configuration they need.

The desired-state update model is powerful - you change the YAML specification and Compose figures out what needs to update. It intelligently leaves unchanged services running while recreating only the services that need updates.

Compose helps debug distributed applications with features like viewing logs across all services simultaneously, executing commands inside containers with docker exec, and inspecting network configuration to understand connectivity.

It manages networks automatically so containers can communicate using service names as DNS hostnames. You don't need to know IP addresses or manage DNS yourself - Compose handles service discovery.

These skills are essential for container development and testing. While you might use Kubernetes or Azure Container Apps in production, Docker Compose is invaluable for local development and for understanding how containerized distributed applications work.

For the AZ-204 exam, understanding multi-container coordination and service-to-service communication is important background knowledge that applies across different container platforms.
