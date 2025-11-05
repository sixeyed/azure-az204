# Docker Multi-Stage Builds - Exercises Walkthrough

## Exercise 1: Simple Multi-Stage Build

### Setting Up

Before we start, we'll use the original Docker build engine so you can clearly see what's happening at each stage. Later, we'll switch to BuildKit for better performance.

Let's set an environment variable to disable BuildKit:

**On Linux or macOS:**
```bash
export DOCKER_BUILDKIT=0
```

**On Windows with PowerShell:**
```powershell
$env:DOCKER_BUILDKIT=0
```

### Understanding the Simple Dockerfile

Let's examine the simple multi-stage Dockerfile in the labs directory. This Dockerfile demonstrates the core concepts:

- The **base** stage uses Alpine Linux and simulates adding some dependencies
- The **build** stage builds on the base and simulates an application build
- The **test** stage starts from the build output and simulates automated testing
- The **final** stage starts fresh from base and copies in only the build output

### Building the Simple Image

Now let's build an image from this Dockerfile:

```bash
docker build -t simple ./labs/multi-stage/simple/
```

Watch the output carefully. You'll see all four stages execute in sequence. However, the magic is that the final app image only contains content explicitly copied from earlier stages.

Let's run a container to see what made it into the final image:

```bash
docker run simple
```

Notice the output. You'll see content from the base and build stages, but the additional content from the test stage isn't included. This is because we didn't copy anything from the test stage into the final stage.

## Exercise 2: BuildKit and Build Targets

### Enabling BuildKit

BuildKit is Docker's modern build engine. It's heavily optimized for multi-stage builds with two key advantages: it runs stages in parallel when possible, and it skips stages whose output isn't used.

Enable BuildKit by setting the environment variable:

**On Linux or macOS:**
```bash
export DOCKER_BUILDKIT=1
```

**On Windows with PowerShell:**
```powershell
$env:DOCKER_BUILDKIT=1
```

### Building with BuildKit

Let's rebuild our simple Dockerfile using BuildKit:

```bash
docker build -t simple:buildkit ./labs/multi-stage/simple/
```

The output looks different! You'll see output from multiple stages appearing simultaneously. If you watch closely, you'll notice something interesting: the test stage is completely skipped.

Why? BuildKit is smart. It analyzes the Dockerfile and realizes that nothing from the test stage is used in the final image, so it doesn't bother executing it. This saves time on large builds.

### Comparing Images

Let's verify the new image works:

```bash
docker run simple:buildkit
```

The output is identical to our original build. Now let's compare the images:

```bash
docker image ls simple
```

Both images are the same size, but they have different image IDs - they're distinct images even though they're functionally equivalent.

### Using Build Targets

BuildKit skipped the test stage automatically, but what if we actually want to build up to the test stage? Maybe we want to run those tests. We can use the target flag:

```bash
docker build -t simple:test --target test ./labs/multi-stage/simple/
```

The `--target` parameter tells Docker to build all stages up to and including the named stage. This image is the output of the test stage, not the final stage.

Let's try running it:

```bash
docker run simple:test
```

Nothing happens! That's because the test stage doesn't define a CMD instruction. But we can execute a command manually:

```bash
docker run simple:test cat /build.txt
```

Now you can see output from both the build stage and the test stage.

## Exercise 3: Real Go Application

### Understanding the whoami Dockerfile

Now let's look at a real-world example. The whoami Dockerfile builds an actual Go web application using the multi-stage pattern:

**Builder Stage:**
- Starts from the official Go SDK image
- Installs OS packages needed for building
- Copies the Go module file and downloads dependencies
- Copies source code and compiles the application

**Final Stage:**
- Sets up the container environment
- Copies only the compiled binary from the builder stage
- No SDK, no source code, no build tools - just the executable

### Building the Application

Let's build the whoami application:

```bash
docker build -t whoami ./labs/multi-stage/whoami/
```

With BuildKit enabled, you'll see all the stage output as Docker processes the build.

### The Size Advantage

SDK images are typically massive because they contain the entire build toolset. You definitely don't want that in your production images. Let's see the difference:

First, pull the Go SDK image:

```bash
docker pull golang:1.16.4-alpine
```

Now compare the sizes:

```bash
docker image ls -f reference=whoami -f reference=golang
```

Look at that difference! The Go SDK image is over 300 megabytes, while our application image is under 10 megabytes. That's a 30x reduction! This means faster deployments, lower storage costs, and reduced attack surface.

### Running the Application

The whoami app is a simple web server. Let's run it with Docker's automatic port publishing:

```bash
docker run -d -P --name whoami1 whoami
```

The `-P` flag tells Docker to publish all exposed ports to random host ports. Let's find which port was assigned:

```bash
docker port whoami1
```

Now we can test the application. Replace `<PORT>` with the port number from the previous command:

```bash
curl localhost:<PORT>
```

The server responds with details about the environment and the incoming request.

## Lab Challenge

Here's your challenge: The whoami application needs special Linux permissions to listen on standard HTTP ports like 80, even inside a container.

However, the whoami app supports a `-port` argument to configure which port it listens on. Your task is to:

1. Configure the container to run the whoami app with a custom port using the `-port` flag
2. Try using the `-P` flag for automatic port publishing - does it work?
3. Figure out what you need to do to run a working container with your custom port

Think about how Docker knows which ports to expose and how you can configure that in the Dockerfile or at runtime.

Give it a try, and check the hints file if you need guidance!

## Cleanup

When you're finished experimenting, clean up all containers:

```bash
docker rm -f $(docker ps -aq)
```

This removes all containers, whether they're running or stopped.

## Summary

In this session, you've learned:

- How multi-stage builds work with multiple FROM instructions
- The difference between the classic builder and BuildKit
- How to target specific build stages
- The dramatic size reduction possible with multi-stage builds
- How to build real applications with compiled languages

These techniques are essential for creating production-ready container images that are small, secure, and efficient.
