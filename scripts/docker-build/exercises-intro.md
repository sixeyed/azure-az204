# Docker Multi-Stage Builds - Exercises Introduction

We've covered multi-stage builds as the pattern for creating optimized, production-ready images. Now let's see dramatic image size reductions in action.

## What You'll Do

You'll start by **building a simple multi-stage Dockerfile** with base, build, test, and final stages. You'll see how each stage uses a different FROM instruction, and how only explicitly copied content reaches the final image. Build tools stay in intermediate stages - they never make it to production.

Then you'll discover **BuildKit** - Docker's modern build engine with parallel stage execution and intelligent stage skipping. If you haven't modified a stage, BuildKit reuses cached results rather than rebuilding. This makes incremental builds incredibly fast.

You'll learn to use the **--target flag** to build specific stages. Want to run tests in CI/CD without shipping them in the final image? Build with `--target test` stage. This single Dockerfile serves both development and production needs.

The real magic happens with the **Go application example** showing dramatic size reduction. The SDK image with compilation tools is 300+ MB. The final runtime image? Under 10 MB! That's a 97% reduction. Smaller images mean faster pushes to Azure Container Registry, faster pulls when deploying to Azure Container Instances, and lower storage costs.

You'll also tackle a challenge around **configuring application arguments in multi-stage builds** - how do you pass runtime configuration to the final stage when build-time and runtime are separate phases? This teaches you important patterns for flexible, configurable containers.

Let's optimize Docker images with multi-stage builds!
