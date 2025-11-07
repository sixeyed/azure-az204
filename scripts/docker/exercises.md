# Docker 101

## Reference

Docker is where you build all your application components and dependencies into a package called an image and use that to run instances of your apps called containers. The great thing about Docker containers is they're portable, so your app runs in the same way on Docker Desktop as it does on any other container runtime. The documentation covers everything from basic concepts to advanced topics like networking and volumes. Docker Desktop is the easiest way to run containers on your local machine, and the docker command line interface gives you complete control over building images and managing containers.

## Run a .NET web container

Let's start by running our first container. We'll use the Docker CLI, and just like the Azure CLI, it has built-in help functionality. The docker --help command shows all the available commands and options.

You'll see a comprehensive list of commands. The one we'll use most frequently is docker run, which starts a new container from an image.

Let's run a simple web server. We're executing docker run with several flags: -d to run in detached mode (background), -p to publish port 8081 on your local machine to port 80 in the container, and specifying the nginx:alpine image.

You'll see Docker pulling the image from Docker Hub if you don't already have it locally, and then a long random string appears - that's the unique ID of your new container.

Let me break down what this command does. We're running a container from the nginx:alpine image - this is a publicly available image that contains the Nginx web server installed on Alpine Linux, which is an extremely lightweight operating system of only a few megabytes.

The -d flag runs the container in detached mode, meaning it runs in the background and doesn't block your terminal. Without this flag, the container output would stream to your console.

The -p 8081:80 flag publishes a port. This tells Docker to listen on port 8081 on your local machine and forward any traffic to port 80 inside the container. This is how you access services running inside containers from your host machine.

Now open your browser and go to localhost port 8081. You should see the Nginx welcome page. Congratulations - you're running your first containerized web server!

---

## Runtime & SDK images

Now let's learn how to manage our running containers. Docker provides several commands for inspecting and controlling container lifecycle.

To list all running containers, use docker ps. This shows you a table of information for each running container.

You'll see your Nginx container listed with its container ID, the image it's running from, when it was created, its current status, the port mappings showing the published ports, and an automatically generated name Docker assigned to it.

To see the logs from a container, use the docker logs command followed by the container ID. You can use just the first few characters of the ID - Docker is smart enough to figure out which container you mean as long as the prefix is unique.

This shows you everything the container has written to stdout and stderr. For web servers, you'll typically see access logs, error logs, and startup messages.

---

## Build .NET apps in containers

Now it's your turn to practice. I want you to run another container - this time from Microsoft's ASP.NET sample application image.

First, you'll need to find the image name. Go to hub.docker.com and search for .NET or ASP.NET samples. You'll find Microsoft's official repository with various .NET images, including one for ASP.NET sample applications.

Once you've found the image name, run it in the background and publish port 8082 from your machine to port 80 in the container, similar to what we did with Nginx.

The image you're looking for is called mcr.microsoft.com/dotnet/samples:aspnetapp. The mcr.microsoft.com prefix indicates this is from Microsoft Container Registry. The command to run it uses the same flags as before: -d for detached mode and -p to map port 8082 to port 80.

Now browse to localhost port 8082 and you'll see the ASP.NET sample application running - a simple web page demonstrating that the .NET runtime is working correctly.

Here's a quick check: Is your Nginx container still running? Run docker ps again. You should see both containers running simultaneously on different ports. Each container is completely isolated and running its own web server. They don't interfere with each other despite both serving on port 80 internally - the port mapping keeps them separate.

---

## Lab

Microsoft publishes different variations of .NET images for different purposes: runtime images for running compiled apps, ASP.NET images that include the ASP.NET runtime for web apps, and SDK images that include everything needed for building applications.

You can run a container interactively, which gives you a shell session inside the container. This is similar to using SSH to connect to a virtual machine, but it's actually just running a shell process inside the container.

Let's explore the ASP.NET runtime image interactively. We're using the -it flags to make this interactive with a terminal. The --entrypoint sh flag tells Docker to run a shell instead of whatever default command the image specifies.

Now you're inside the container. It's like being logged into a Linux system. Let's see what's installed. We're running dotnet --list-runtimes to see which .NET runtimes are available.

You'll see the .NET runtime and ASP.NET runtime are installed - these are what you need to run compiled .NET applications. Now check for SDKs using dotnet --list-sdks.

Nothing appears! This is a runtime image - you can run compiled applications that have already been built, but you can't build applications from source code. The SDK and build tools aren't included to keep the image size smaller.

Type exit to leave the container and return to your terminal.

---

## Cleanup

Now let's try the SDK image. Your task is to run an interactive container from the .NET 6.0 SDK image and use it to create and run a new console application.

The command to run the SDK container uses the same format as before: docker run -it --entrypoint sh, but this time specifying the mcr.microsoft.com/dotnet/sdk:6.0 image.

Now you're in a container that has both the runtime and the SDK installed. Let's create a new console application. We're using dotnet new console to create a new console app in a directory called labs-docker, then changing into that directory and running the application with dotnet run.

You should see "Hello, World!" printed out. We just created and ran a .NET application entirely inside a container! This is actually very similar to how Azure Cloud Shell works - those shell sessions run in containers behind the scenes, providing you with a consistent environment regardless of what's on your local machine.

Type exit to leave the container. Notice that when the container stops, everything you did inside it is gone - the application you created no longer exists. Containers are ephemeral by default.


Building apps inside a running container is useful for experimenting, but the real power of Docker comes from packaging your own images that can be deployed consistently anywhere.

In the lab repository, there's a Dockerfile in the src/simple-web directory. A Dockerfile is a script that defines how to build a Docker image - it's like a recipe that tells Docker how to assemble your application and its dependencies into a runnable package.

This particular Dockerfile uses a multi-stage build: it uses the SDK image to compile the application, then copies the compiled output into an ASP.NET runtime image for running the app. This is a best practice because it keeps your final image small - you don't need the SDK and source code in production, just the runtime and the compiled application.

Let's build an image called simple-web. We're using the -t flag to tag the image with a name, and specifying the src/simple-web directory which contains both the Dockerfile and the application source code.

Docker will execute each step in the Dockerfile sequentially. You'll see output from the dotnet build commands as it compiles the application, and then see the final image being assembled.

Once the build completes, you have a new local Docker image. Now your task is to run a container from this image, publishing port 8083 from your machine to port 80 in the container.

The command is docker run -d -p 8083:80 simple-web.

Browse to localhost port 8083 and you'll see your simple web application running - a basic ASP.NET application with some diagnostic information.


The application is quite basic, but you can improve it. Try editing the code in the src/simple-web/src folder - maybe change the welcome message, adjust the styling, or add new features.

Then rebuild the image using the same docker build command. Docker will use cached layers where nothing has changed and only rebuild the layers affected by your code changes. This makes rebuilds faster.

Now try to test your changes by running docker run -d -p 8083:80 simple-web again.

Wait - this gives an error! The error message says the port is already in use. Why? Because port 8083 is already bound to your first container which is still running. Each container needs its own unique port mapping on the host machine, so you'd need to either stop the first container using docker rm -f with the container ID, or use a different port like 8085 for the new container.


Container images are static packages. They're essentially ZIP files containing your application, runtime, and OS tools. Wherever you run a container from an image, it behaves the same way because it starts from the same immutable package.

But typically, you need different configuration between environments - development might point to a local database, staging to a test database, and production to a production database. The simplest way to inject environment-specific configuration is using environment variables.

The simple-web app uses a configuration setting to display the environment name on the homepage. Your challenge is to run a new container listening on port 8084 that displays the environment name "PROD" on the homepage.

Think about how you might pass configuration into a container. There's a Docker flag that lets you set environment variables.

The solution involves using the -e flag to set an environment variable when running the container. We're running docker run -d -p 8084:80 -e Environment=PROD simple-web.

Browse to localhost port 8084 and you should see "PROD" displayed as the environment name. This demonstrates how the same image can be configured differently for different environments using environment variables. The application reads the Environment variable and displays it, allowing you to run identical images in development, staging, and production with just different environment variables.

