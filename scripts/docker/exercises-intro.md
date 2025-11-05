# Docker - Exercises Introduction

We've covered Docker as a solution for consistent application deployment by packaging apps and dependencies into images. Now let's get hands-on with Docker fundamentals.

## What You'll Do

You'll start by **running pre-built containers** like nginx and ASP.NET samples to understand the container lifecycle. You'll see how `docker run` starts containers, `docker ps` lists running containers, `docker logs` shows output, and `docker stop` shuts them down. These are the core Docker CLI commands you'll use constantly.

Then you'll explore **runtime vs SDK images**. Runtime images contain only what's needed to run the app (small, optimized for production). SDK images contain development tools for building and debugging (large, used for development). You'll see the size difference and understand when to use each.

Next comes **building custom Docker images** using multi-stage Dockerfiles. You'll write a Dockerfile that compiles your application and packages it into an image. The multi-stage pattern uses build tools in intermediate stages but ships only the compiled app in the final image - this keeps production images small and secure.

You'll practice **configuring containers with environment variables** - passing runtime configuration without rebuilding images. The same image can behave differently in dev, staging, and prod just by changing environment variables. You'll also handle **port mappings** to expose containerized applications on your host machine, and troubleshoot port conflicts when multiple containers want the same port.

The key learning: containers make "it works on my machine" problems disappear. The exact same container that runs on your laptop runs identically in Azure.

Let's master Docker fundamentals!
