# Azure Container Instances (ACI) - Quickfire Questions

## Question 1
What is Azure Container Instances (ACI)?


- A) A Kubernetes service
- B) A virtual machine service
- C) A serverless container platform for running containers without managing infrastructure
- D) A container registry

**Answer: C**
ACI provides the fastest and simplest way to run containers in Azure without managing VMs or orchestrators.
---
## Question 2
What are the key benefits of ACI?


- A) Requires Kubernetes knowledge
- B) Only supports Windows
- C) Fast startup, per-second billing, no infrastructure management
- D) Only low cost

**Answer: C**
ACI offers quick deployment (seconds), pay-per-second billing, and eliminates VM/cluster management.
---
## Question 3
What operating systems does ACI support?


- A) Only Windows
- B) Both Linux and Windows containers
- C) Only Linux
- D) Neither

**Answer: B**
ACI supports both Linux and Windows containers, though Windows containers have some limitations.
---
## Question 4
How is ACI billed?


- A) Monthly flat rate
- B) Per container
- C) Per request
- D) Per second for CPU and memory allocation

**Answer: D**
ACI charges per second based on allocated vCPUs and memory (GB), billed only while containers are running.
---
## Question 5
Can ACI pull images from private registries?


- A) Requires special permission
- B) No, only public Docker Hub
- C) Yes, from Azure Container Registry and other private registries with credentials
- D) Only from Microsoft registries

**Answer: C**
ACI can pull from Azure Container Registry (with managed identity) or other private registries using credentials.
---
## Question 6
What is a container group in ACI?


- A) A collection of containers that share host, network, and storage, similar to Kubernetes pod
- B) A monitoring group
- C) A billing group
- D) A security group

**Answer: A**
Container groups are collections of containers scheduled on the same host, sharing lifecycle, network, and volumes.
---
## Question 7
Can containers in a container group communicate?


- A) Only with load balancer
- B) No
- C) Yes, via localhost on different ports
- D) Only through internet

**Answer: C**
Containers in the same group can reach each other on localhost, similar to processes on the same machine.
---
## Question 8
What network options are available for ACI?


- A) No networking
- B) Public IP only
- C) Only private
- D) Public IP, Private (VNet integration), or no public IP

**Answer: D**
ACI can have a public IP, integrate with Azure VNet for private networking, or have no public IP.
---
## Question 9
Does ACI support persistent storage?


- A) No storage
- B) Only blob storage
- C) Yes, via Azure Files shares mounted as volumes
- D) Only temporary storage

**Answer: C**
ACI supports mounting Azure Files (SMB) shares for persistent storage across container restarts.
---
## Question 10
What is the maximum memory you can allocate to a single ACI container group?


- A) Unlimited
- B) 4 GB
- C) 16 GB (standard) or higher with specific SKUs
- D) 1 GB

**Answer: C**
Standard ACI supports up to 16 GB memory per container group. Specific SKUs may support more.