We've covered how nodes are the worker machines in your Kubernetes cluster that run your containerized workloads. Now let's explore how to examine and work with nodes using Kubectl.

We'll start by working with nodes, using the get and describe commands to find information about nodes in your cluster. You'll see basic information like node names and status with get, and much more detailed information about capacity, allocatable resources, and conditions with describe.

Next, we'll explore getting help from Kubectl itself. You'll learn to use the built-in help system to list all commands or get details about specific commands. You'll also use kubectl explain to learn about Kubernetes resources directly from the command line, which is invaluable when you need quick reference information.

Then we'll dive into querying and formatting, exploring how Kubectl can print information in different formats including JSON and YAML. You'll work with JSON Path, a query language that lets you print specific fields from Kubernetes objects, perfect for extracting just the information you need like CPU capacity or memory allocatable. You'll spend a lot of time with Kubectl, so getting familiar with these features early will make you much more productive.

The lab challenge asks you to find labels for your nodes, which will confirm the CPU architecture and operating system. Labels are key-value pairs used to record additional information about objects, and they're fundamental to how Kubernetes organizes and selects resources. The key learning is that understanding how to examine nodes and use Kubectl effectively is essential for managing your cluster and troubleshooting issues when they arise.
