# Docker Compose - Exercises Narration Script

## Exercise 1: Understanding Multi-Container Apps

Let's start by understanding why we need Docker Compose in the first place.

We're going to run a simple web application - this is the front-end component for a random number generator.

```
docker run -d -p 8088:80 --name rng-web courselabs/rng-web:21.05
```

This command runs the container in detached mode on port 8088. Let's browse to localhost port 8088.

Click the button to get a random number... and after a few seconds, we see an error: "RNG service unavailable!"

This is a perfect example of why we need to understand distributed applications. The web front-end is only one piece of the puzzle.

Let's check the application logs to see what's happening:

```
docker logs rng-web
```

Looking at the logs, we can see the web application is trying to connect to a backend REST API at the address http://numbers-api/rng. But there's no such service running - we only started the web container.

We could start the API container with another docker run command, but we'd need to know the image name, the ports, and how to configure the network so the containers can communicate. This is where Docker Compose becomes invaluable.

## Exercise 2: Simple Compose Definition

Let's look at a simple Compose file first - this one just defines an Nginx container.

Open the file at labs/docker-compose/nginx/docker-compose.yml.

This is about as simple as a Compose file gets. It defines a single service named "web" that uses the nginx alpine image version 1.18 and publishes port 8082.

You might ask - why bother with a Compose file for just one container? Well, this file serves as documentation. Anyone looking at this file immediately knows which image version to use and which port the application listens on. It's executable documentation.

Let's run this application using the docker-compose CLI:

```
docker-compose -f labs/docker-compose/nginx/docker-compose.yml up
```

Notice that Compose shows us the logs in real-time. The container starts and we can browse to localhost port 8082 to verify it's working.

Use Control-C to exit. Notice that stopping the Compose command also stops the container. This is useful for development.

## Exercise 3: Multi-Container Apps in Compose

Now let's look at a more realistic example - the complete random number generator application with both the web front-end and the API backend.

Open the file at labs/docker-compose/rng/v1.yml.

In just 20 lines of YAML, we've defined a complete distributed application:
- Two services: one for the API and one for the web
- Each service specifies its container image and port mappings
- The web service includes an environment variable to configure logging
- Both services connect to the same container network
- The network itself is defined at the bottom

Let's run this application in detached mode:

```
docker-compose -f ./labs/docker-compose/rng/v1.yml up -d
```

Watch as Compose creates the network and both containers. Now we can use Compose commands to manage our application:

```
docker-compose -f ./labs/docker-compose/rng/v1.yml ps
```

This shows just the containers for this application. We can also view the logs:

```
docker-compose -f ./labs/docker-compose/rng/v1.yml logs
```

Remember, these are standard Docker containers. We can still use the regular Docker CLI to see them:

```
docker ps
```

Now let's browse to localhost port 8090 and try to get a random number.

Still not working! We need to debug this application.

## Exercise 4: Debugging with Compose

When a distributed application fails, we need to isolate the problem. The web app uses the API to get random numbers. There are only two possibilities:
- The API isn't working
- The web app can't connect to the API

Let's check if the API works independently. The Compose file shows it publishes port 8089. We can verify this with:

```
docker-compose -f ./labs/docker-compose/rng/v1.yml port rng-api 80
```

Let's test the API directly:

```
curl localhost:8089/rng
```

Good! We get a random number back. So the API is working correctly. The problem must be connectivity from the web app to the API.

Let's check the web container logs:

```
docker logs rng-rng-web-1
```

Looking at the logs, we can see the web app is trying to connect to the domain "numbers-api". Let's test if that domain is resolvable from within the web container:

```
docker exec rng-rng-web-1 nslookup numbers-api
```

There's the problem! DNS can't resolve "numbers-api" because that's not the name of our service. If we look back at the Compose file, the API service is named "rng-api", not "numbers-api".

In Docker Compose, the service name becomes the DNS name that other containers use for discovery. We have a mismatch.

## Exercise 5: Updating with Desired State

We could fix this by renaming the service in the Compose file, but there's a better way. The web application supports a configuration setting for the API URL.

Open the file at labs/docker-compose/rng/v2.yml.

This updated version adds an environment variable to the web service called "RngApi__Url" that points to "http://rng-api/rng" - using the correct service name.

The file also increases the logging level for the API by adding a "Logging__LogLevel__Default" environment variable.

Now here's where we see the desired-state approach in action. We don't need to stop and remove our containers and start over. We just update the spec and run up again:

```
docker-compose -f ./labs/docker-compose/rng/v2.yml up -d
```

Watch what happens. Compose compares the current state with the desired state. It sees that:
- The API container hasn't changed, so it leaves it running
- The web container has new environment variables, so it recreates that container

This is the power of desired-state deployment. Change your YAML, run up, and Compose figures out what needs to change.

Let's follow the logs:

```
docker-compose -f ./labs/docker-compose/rng/v2.yml logs -f
```

Now browse to localhost port 8090 and click to get a random number. Success! The application works, and we can see the API logs showing our requests.

Use Control-C to stop following the logs.

## Lab Challenge

Your challenge is to extend this application by adding an Nginx container as a reverse proxy.

You'll need to:
- Add a new network to the Compose file
- Define an Nginx service that connects to both the new network and the existing application network
- Deploy the updated spec

Then investigate: What IP addresses does the Nginx container have? Can the RNG web container access Nginx, even though it was created after the original containers?

This exercise will help you understand how Docker Compose manages networks and how containers can join multiple networks.

Take some time to work through this challenge. If you get stuck, there are hints available, and a complete solution in the lab materials.

## Summary

In these exercises, we've seen how Docker Compose:
- Simplifies multi-container application deployment
- Provides clear documentation of application architecture
- Enables desired-state updates where you change the YAML and Compose figures out what to update
- Helps debug distributed applications with logging and exec commands
- Manages networks so containers can communicate using service names

These skills are essential for container development and for the AZ-204 exam.
