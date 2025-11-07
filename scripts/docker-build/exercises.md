# Multi-Stage Builds

## Reference

Multi-stage builds use the standard Dockerfile syntax with multiple stages separated by FROM commands. They give you a repeatable build process with minimal dependencies, letting you use an SDK image for building and a runtime image for production. The multi-stage build documentation covers the pattern across different languages and frameworks. The docker build command works the same way for multi-stage builds, but BuildKit provides better performance by running stages in parallel and skipping stages that aren't needed.

## Multi-Stage Dockerfiles

### Setting Up

Before we start, we'll use the original Docker build engine so you can clearly see what's happening at each stage. Later, we'll switch to BuildKit for better performance.

Let's set an environment variable to disable BuildKit. On Linux or macOS, we're using the export command to set DOCKER_BUILDKIT to 0. On Windows with PowerShell, we're setting the environment variable using the dollar sign env syntax.

### Understanding the Simple Dockerfile

Let's examine the simple multi-stage Dockerfile in the labs directory. This Dockerfile demonstrates the core concepts of multi-stage builds in a simplified way.

The base stage uses Alpine Linux as a foundation and simulates adding some dependencies. Think of this as installing the runtime environment and libraries your application needs.

The build stage builds on the base stage and simulates an application build process. This represents compiling your code or preparing your application for deployment.

The test stage starts from the build output and simulates running automated tests. In a real scenario, this would run your unit tests, integration tests, or other quality checks.

The final stage starts fresh from the base image again and copies in only the build output from the build stage. This is the key insight - the final image doesn't include the test artifacts, build tools, or any intermediate files. It only contains what you explicitly copy into it.

### Building the Simple Image

Now let's build an image from this Dockerfile. We're tagging it as "simple" and pointing to the directory containing the Dockerfile.

Watch the output carefully. You'll see all four stages execute in sequence - base, build, test, and final. However, the magic is that the final app image only contains content explicitly copied from earlier stages.

Let's run a container to see what made it into the final image. When you run the container, notice the output. You'll see content from the base and build stages, but the additional content from the test stage isn't included. This is because we didn't copy anything from the test stage into the final stage. The test stage ran during the build, but its output was discarded.

---

## BuildKit and build targets

### Enabling BuildKit

BuildKit is Docker's modern build engine, introduced to replace the original builder. It's heavily optimized for multi-stage builds with two key advantages: it runs stages in parallel when possible, and it intelligently skips stages whose output isn't used in the final image.

Enable BuildKit by setting the environment variable. On Linux or macOS, we're exporting DOCKER_BUILDKIT=1. On Windows with PowerShell, we're setting the environment variable to 1.

### Building with BuildKit

Let's rebuild our simple Dockerfile using BuildKit. We're tagging this build as "simple:buildkit" to distinguish it from the previous build.

The output looks dramatically different! You'll see output from multiple stages appearing simultaneously because BuildKit executes independent stages in parallel. If you watch closely, you'll notice something interesting: the test stage is completely skipped.

Why does BuildKit skip the test stage? BuildKit is smart - it analyzes the Dockerfile dependency graph and realizes that nothing from the test stage is used in the final image. Since no subsequent stage depends on it, BuildKit doesn't bother executing it. This saves significant time on large builds with extensive test suites.

### Comparing Images

Let's verify the new image works correctly by running it. The output is identical to our original build - both images produce the same result.

Now let's compare the images to see if there are any differences. We're listing all images with the "simple" reference. Both images are exactly the same size, but they have different image IDs - they're distinct images stored separately even though they're functionally equivalent.

### Using Build Targets

BuildKit skipped the test stage automatically to save time, but what if we actually want to build up to the test stage? Maybe we want to run those tests in our CI/CD pipeline. We can use the target flag to specify which stage to build up to.

We're building to the test stage specifically, tagging the result as "simple:test". The --target parameter tells Docker to build all stages up to and including the named stage, then stop. This image is the output of the test stage, not the final stage.

Let's try running it. Nothing happens! That's because the test stage doesn't define a CMD instruction - it doesn't have a default command to execute.

But we can execute a command manually. We're running cat to display a file that was created in the build and test stages. Now you can see output from both stages, confirming that the test stage artifacts are present in this image.

---

## Simple Go application

### Understanding the whoami Dockerfile

Now let's look at a real-world example. The whoami Dockerfile builds an actual Go web application using the multi-stage pattern, demonstrating the significant benefits of this approach.

The builder stage starts from the official Go SDK image, which contains all the tools needed to compile Go applications. It installs OS packages needed for building, copies the Go module file and downloads dependencies separately (this enables Docker to cache the dependency layer), then copies the source code and compiles the application. The result is a compiled binary.

The final stage is dramatically different. It sets up a minimal container environment, then copies only the compiled binary from the builder stage. There's no SDK, no source code, no build tools - just the executable. This is the power of multi-stage builds for compiled languages.

### Building the Application

Let's build the whoami application. We're tagging it as "whoami" and pointing to the directory containing the Dockerfile.

With BuildKit enabled, you'll see output from both stages as Docker processes the build. The builder stage compiles the code, and the final stage packages just the binary.

### The Size Advantage

SDK images are typically massive because they contain the entire build toolset - compilers, debuggers, standard libraries, and development tools. You definitely don't want that bloat in your production images. Let's see the actual difference.

First, we're pulling the Go SDK image that we used as the builder stage. This is the golang:1.16.4-alpine image.

Now let's compare the sizes using docker image ls with filters to show just the whoami and golang images.

Look at that difference! The Go SDK image is over 300 megabytes, while our application image is under 10 megabytes. That's more than a 30x reduction! This translates directly to faster deployments, lower storage costs, reduced network bandwidth for image transfers, and a dramatically reduced attack surface since there are fewer components that could contain vulnerabilities.

### Running the Application

The whoami app is a simple web server that returns information about its environment. Let's run it with Docker's automatic port publishing feature.

We're running in detached mode, using the -P flag which tells Docker to publish all exposed ports to random host ports automatically. This is convenient for testing because Docker handles the port allocation.

The -P flag is useful, but we need to find out which port was assigned. The docker port command shows us the port mapping for the container.

Now we can test the application using curl. Replace the port placeholder with the actual port number from the previous command. The server responds with details about the environment and the incoming request - hostname, IP addresses, headers, and more.

---

## Lab

Here's your challenge to test your understanding. The whoami application needs special Linux capabilities to listen on standard HTTP ports like 80, even inside a container. These low-numbered ports are privileged.

However, the whoami app supports a -port argument that lets you configure which port it listens on. Your task is to configure the container to run the whoami app with a custom port using the -port flag.

Try using the -P flag for automatic port publishing - does it work with your custom port configuration? Figure out what you need to do to run a working container with your custom port. Think about how Docker knows which ports to expose and how you can configure that either in the Dockerfile or at runtime.

Give it a try, and check the hints file if you need guidance!

---

## Cleanup

When you're finished experimenting, clean up all containers. We're using a command that lists all container IDs (both running and stopped) and pipes them to docker rm -f to forcibly remove them all at once.

This is a quick way to clean up your Docker environment when you're done with a lab.
