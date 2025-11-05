# Docker 101 - Exercises Narration Script

## Exercise 1: Run Your First Container

Let's start by running our first container. We'll use the Docker CLI, and just like the Azure CLI, it has built-in help. Try running:

```
docker --help
```

You'll see all the available commands. The one we'll use most frequently is `docker run`, which starts a new container from an image.

Let's run a simple web server. Execute this command:

```
docker run -d -p 8081:80 nginx:alpine
```

You'll see Docker pulling the image from Docker Hub, and then a long random string will appear - that's the unique ID of your new container.

Let me break down what this command does:

- We're running a container from the `nginx:alpine` image. This is a publicly available image that contains the Nginx web server installed on Alpine Linux, which is a very lightweight operating system.

- The `-d` flag runs the container in detached mode, meaning it runs in the background.

- The `-p 8081:80` flag publishes a port. This tells Docker to listen on port 8081 on your local machine and forward any traffic to port 80 inside the container.

Now open your browser and go to http://localhost:8081. You should see the Nginx welcome page. Congratulations - you're running your first containerized web server!

## Managing Containers

Now let's learn how to manage our running containers. Docker provides several commands for this.

To list all running containers, use:

```
docker ps
```

You'll see your Nginx container listed with its ID, the image it's running from, when it was created, its status, and the port mappings.

To see the logs from a container, use the `docker logs` command followed by the container ID. You can use just the first few characters of the ID:

```
docker logs <container-id>
```

This shows you everything the container has written to stdout and stderr.

## Exercise 2: Running an ASP.NET Container

Now it's your turn. I want you to run another container - this time from Microsoft's ASP.NET sample app image.

First, you'll need to find the image name. Go to hub.docker.com and search for .NET. You'll find a page listing all of Microsoft's .NET images, including one for ASP.NET samples.

Once you've found the image name, run it in the background and publish port 8082 from your machine to port 80 in the container.

[pause for student work]

If you searched Docker Hub, you should have found the image `mcr.microsoft.com/dotnet/samples:aspnetapp`. The command to run it is:

```
docker run -d -p 8082:80 mcr.microsoft.com/dotnet/samples:aspnetapp
```

Now browse to http://localhost:8082 and you'll see the ASP.NET sample application.

Here's a quick check: Is your Nginx container still running? Run `docker ps` again. You should see both containers running simultaneously on different ports. Each container is isolated and running its own web server.

## Exercise 3: Exploring Runtime Images

Microsoft publishes different variations of .NET images: runtime images for running apps, ASP.NET images for web apps, and SDK images for building applications.

You can run a container interactively, which gives you a shell session inside the container. This is similar to using SSH to connect to a VM.

Let's explore the ASP.NET runtime image:

```
docker run -it --entrypoint sh mcr.microsoft.com/dotnet/aspnet:6.0
```

The `-it` flags make this interactive with a terminal. The `--entrypoint sh` tells Docker to run a shell instead of the default command.

Now you're inside the container. Let's see what's installed:

```
dotnet --list-runtimes
```

You'll see the .NET runtime and ASP.NET runtime are installed. Now check for SDKs:

```
dotnet --list-sdks
```

Nothing. This is a runtime image - you can run compiled applications, but you can't build them from source.

Type `exit` to leave the container and return to your terminal.

## Exercise 4: Using the SDK Image

Now let's try the SDK image. Your task is to run an interactive container from the .NET 6.0 SDK image and use it to create and run a new console application.

[pause for student work]

The command to run the SDK container is:

```
docker run -it --entrypoint sh mcr.microsoft.com/dotnet/sdk:6.0
```

Now you're in a container that has both the runtime and the SDK installed. Let's create a new console app:

```
dotnet new console -o labs-docker
cd labs-docker
dotnet run
```

You should see "Hello, World!" printed out. This is actually very similar to how Azure Cloud Shell works - those shell sessions run in containers behind the scenes.

Type `exit` to leave the container.

## Exercise 5: Building Your Own Docker Image

Building apps inside a container is useful for experimenting, but the real power of Docker comes from packaging your own images.

In the lab repository, there's a Dockerfile in the `src/simple-web` directory. A Dockerfile is a script that defines how to build a Docker image. This particular Dockerfile uses a multi-stage build: it uses the SDK image to compile the application, then copies the compiled output into an ASP.NET runtime image for running the app.

This is a best practice because it keeps your final image small - you don't need the SDK in production, just the runtime.

Let's build an image called `simple-web`:

```
docker build -t simple-web src/simple-web
```

The `-t` flag tags the image with a name. Docker will execute each step in the Dockerfile, and you'll see output from the dotnet build commands as it compiles the application.

Once the build completes, you have a new local Docker image. Now your task is to run a container from this image, publishing port 8083 from your machine to port 80 in the container.

[pause for student work]

The command is:

```
docker run -d -p 8083:80 simple-web
```

Browse to http://localhost:8083 and you'll see your simple web application.

## Making Changes

The application is quite basic, but you can improve it. Try editing the code in the `src/simple-web/src` folder - maybe change the welcome message or add some styling.

Then rebuild the image using the same `docker build` command. Docker will use cached layers where nothing has changed and only rebuild what's necessary.

Now try to test your changes by running:

```
docker run -d -p 8083:80 simple-web
```

Wait - this gives an error! Why? Because port 8083 is already in use by your first container. Each container needs its own port mapping, so you'd need to either stop the first container or use a different port like 8085.

## Lab Challenge: Environment Variables

Container images are static packages. They're essentially ZIP files containing your application, runtime, and OS tools. Wherever you run a container from an image, it behaves the same way because it starts from the same package.

But typically, you need different configuration between environments - development, staging, production. The simplest way to inject configuration is using environment variables.

The simple-web app uses a config setting to display the environment name on the homepage. Your challenge is to run a new container listening on port 8084 that displays the environment name "PROD" on the homepage.

[pause for student work]

The solution involves using the `-e` flag to set an environment variable:

```
docker run -d -p 8084:80 -e Environment=PROD simple-web
```

Browse to http://localhost:8084 and you should see "PROD" displayed as the environment name. This demonstrates how the same image can be configured differently for different environments.

## Cleanup

You probably have several containers running now. Containers are designed to be disposable - you can easily stop and remove them.

To remove all containers at once, run:

```
docker rm -f $(docker ps -aq)
```

This command lists all container IDs with `docker ps -aq` and pipes them to `docker rm -f` which forcibly removes them.

## Wrap Up

In this lab, you've learned the fundamentals of Docker:

- Running containers from pre-built images
- Managing containers with Docker CLI commands
- Understanding the difference between runtime and SDK images
- Building your own Docker images from Dockerfiles
- Configuring containers with environment variables

These skills form the foundation for deploying containerized applications to Azure, which we'll explore in upcoming labs.
