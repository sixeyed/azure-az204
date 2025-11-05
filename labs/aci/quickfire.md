# Azure Container Instances (ACI) - Quickfire Questions

## Question 1
What is Azure Container Instances (ACI)?

- A) A virtual machine service
- B) A serverless container platform for running containers without managing infrastructure
- C) A container registry
- D) A Kubernetes service

**Answer: B**
ACI provides the fastest and simplest way to run containers in Azure without managing VMs or orchestrators.

---

## Question 2
What are the key benefits of ACI?

- A) Only low cost
- B) Fast startup, per-second billing, no infrastructure management
- C) Only supports Windows
- D) Requires Kubernetes knowledge

**Answer: B**
ACI offers quick deployment (seconds), pay-per-second billing, and eliminates VM/cluster management.

---

## Question 3
What operating systems does ACI support?

- A) Only Linux
- B) Both Linux and Windows containers
- C) Only Windows
- D) Neither

**Answer: B**
ACI supports both Linux and Windows containers, though Windows containers have some limitations.

---

## Question 4
How is ACI billed?

- A) Monthly flat rate
- B) Per second for CPU and memory allocation
- C) Per container
- D) Per request

**Answer: B**
ACI charges per second based on allocated vCPUs and memory (GB), billed only while containers are running.

---

## Question 5
Can ACI pull images from private registries?

- A) No, only public Docker Hub
- B) Yes, from Azure Container Registry and other private registries with credentials
- C) Only from Microsoft registries
- D) Requires special permission

**Answer: B**
ACI can pull from Azure Container Registry (with managed identity) or other private registries using credentials.

---

## Question 6
What is a container group in ACI?

- A) A monitoring group
- B) A collection of containers that share host, network, and storage, similar to Kubernetes pod
- C) A billing group
- D) A security group

**Answer: B**
Container groups are collections of containers scheduled on the same host, sharing lifecycle, network, and volumes.

---

## Question 7
Can containers in a container group communicate?

- A) No
- B) Yes, via localhost on different ports
- C) Only through internet
- D) Only with load balancer

**Answer: B**
Containers in the same group can reach each other on localhost, similar to processes on the same machine.

---

## Question 8
What network options are available for ACI?

- A) Public IP only
- B) Public IP, Private (VNet integration), or no public IP
- C) Only private
- D) No networking

**Answer: B**
ACI can have a public IP, integrate with Azure VNet for private networking, or have no public IP.

---

## Question 9
Does ACI support persistent storage?

- A) No storage
- B) Yes, via Azure Files shares mounted as volumes
- C) Only temporary storage
- D) Only blob storage

**Answer: B**
ACI supports mounting Azure Files (SMB) shares for persistent storage across container restarts.

---

## Question 10
What is the maximum memory you can allocate to a single ACI container group?

- A) 1 GB
- B) 4 GB
- C) 16 GB (standard) or higher with specific SKUs
- D) Unlimited

**Answer: C**
Standard ACI supports up to 16 GB memory per container group. Specific SKUs may support more.
