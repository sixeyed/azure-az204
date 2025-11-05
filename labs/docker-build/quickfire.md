# Docker Multi-Stage Builds - Quickfire Questions

## Question 1
What is a multi-stage Docker build?


- A) Building in multiple regions
- B) Using multiple FROM statements in a Dockerfile to create intermediate stages and optimize final image
- C) Running builds in parallel
- D) Building multiple images

**Answer: B**
Multi-stage builds use multiple FROM statements, allowing you to build in one stage and copy artifacts to a smaller final stage.
---
## Question 2
What are the benefits of multi-stage builds?


- A) Automatic testing
- B) Faster builds only
- C) Better colors
- D) Smaller final images by excluding build tools and intermediate artifacts

**Answer: D**
Multi-stage builds reduce final image size by separating build-time dependencies from runtime dependencies.
---
## Question 3
What instruction copies files from one stage to another?


- A) MOVE --from=stage
- B) COPY --from=stage
- C) GET --from=stage
- D) TRANSFER --from=stage

**Answer: B**
`COPY --from=stagename /source /destination` copies files from a named or numbered build stage.
---
## Question 4
How do you name a build stage in a Dockerfile?


- A) STAGE name
- B) NAME stage
- C) FROM image AS name
- D) LABEL stage=name

**Answer: C**
`FROM node:18 AS build` creates a named stage called "build" that can be referenced later.
---
## Question 5
What is a common pattern for multi-stage builds with compiled languages?


- A) Documentation stage
- B) Single stage with all tools
- C) Build stage (with compiler/SDK) → Runtime stage (with minimal runtime only)
- D) Test stage only

**Answer: C**
Typical pattern: Build stage with full SDK compiles the app, runtime stage copies only the compiled output with minimal runtime.
---
## Question 6
Which base image is commonly used for minimal final stages?


- A) centos:latest
- B) alpine, distroless, or scratch
- C) windows:latest
- D) ubuntu:latest

**Answer: B**
Alpine Linux, Google's distroless images, or scratch (empty image) are used for minimal final images.
---
## Question 7
Can you build only a specific stage?


- A) Yes, using `docker build --target stagename`
- B) Only in Enterprise edition
- C) No, always builds all stages
- D) Only with special tools

**Answer: A**
`docker build --target build` builds only up to and including the specified stage, useful for testing build stages.
---
## Question 8
What is the scratch image?


- A) A damaged image
- B) An empty base image with no OS files, for ultra-minimal containers
- C) A test image
- D) A cache image

**Answer: B**
`FROM scratch` creates an empty image. Useful for compiled binaries that don't need an OS (like Go static binaries).
---
## Question 9
Do earlier stages affect the final image size if not referenced?


- A) No, only the final stage and referenced artifacts are in the final image
- B) Sometimes
- C) Only on Windows
- D) Yes, they're included in final image

**Answer: A**
Intermediate stages and their layers are not included in the final image unless explicitly copied.
---
## Question 10
What is layer caching in Docker builds?


- A) Docker reuses unchanged layers from previous builds to speed up builds
- B) RAM allocation
- C) Network caching
- D) A pricing tier

**Answer: A**
Docker caches each layer. If a layer hasn't changed, it's reused, significantly speeding up subsequent builds.