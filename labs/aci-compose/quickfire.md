# ACI with Docker Compose - Quickfire Questions

## Question 1
Can you deploy Docker Compose applications to Azure Container Instances?

- A) No, not supported
- B) Yes, using Docker Compose with Azure context or Azure CLI
- C) Only manually
- D) Only through portal

**Answer: B**
You can deploy Compose applications to ACI using `docker compose up` with Azure context or `az container create` with Compose file.

---

## Question 2
What is the benefit of using Compose with ACI?

- A) Lower cost only
- B) Easily transition multi-container apps from local development to cloud
- C) Better security
- D) No benefits

**Answer: B**
Docker Compose provides a consistent definition from development to cloud deployment, simplifying the transition.

---

## Question 3
What becomes of a multi-container Compose app when deployed to ACI?

- A) Multiple separate container instances
- B) A single ACI container group containing all services
- C) Nothing, it fails
- D) A Kubernetes cluster

**Answer: B**
The Compose services are deployed as containers within a single ACI container group.

---

## Question 4
Are all Docker Compose features supported in ACI?

- A) Yes, 100% compatible
- B) No, some features like build, depends_on behavior may differ
- C) Only networking features
- D) Only volume features

**Answer: B**
ACI supports core Compose features but not all (e.g., build must happen before deployment, some dependency ordering differences).

---

## Question 5
How do services defined in Compose communicate when deployed to ACI?

- A) They cannot
- B) Via localhost, as they're in the same container group
- C) Only through public internet
- D) Using VPN

**Answer: B**
Services in the same Compose deployment become containers in an ACI group, communicating via localhost.

---

## Question 6
What storage option works with ACI Compose deployments?

- A) No storage
- B) Azure Files volumes can be mounted
- C) Only local disk
- D) Only blob storage

**Answer: B**
Azure Files shares can be defined as volumes in Compose and mounted in ACI containers.

---

## Question 7
Can you specify resource limits in Compose for ACI deployment?

- A) No, always default
- B) Yes, using deploy.resources configuration in Compose file
- C) Only through portal after deployment
- D) Only with Kubernetes

**Answer: B**
Use the Compose `deploy.resources.limits` section to specify CPU and memory for ACI containers.

---

## Question 8
What happens to the network ports defined in Compose when deployed to ACI?

- A) Ignored
- B) Exposed through the container group's public IP
- C) Only internal
- D) Requires manual configuration

**Answer: B**
Ports defined in Compose are exposed on the container group's public IP address.

---

## Question 9
How do you provide secrets to ACI containers from Compose?

- A) Plaintext in Compose file
- B) Using environment variables or Azure Key Vault references
- C) Not possible
- D) Only through portal

**Answer: B**
Use environment variables in Compose or integrate with Azure Key Vault for secure secret management.

---

## Question 10
What command creates an ACI deployment from a Compose file using Azure CLI?

- A) az aci create-compose
- B) az container create with --file parameter pointing to Compose YAML
- C) docker aci deploy
- D) az compose up

**Answer: B**
`az container create --resource-group rg --file docker-compose.yml` deploys Compose applications to ACI.
