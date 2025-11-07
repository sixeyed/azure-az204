# Kubernetes Nodes

## Reference

Nodes are the worker machines in Kubernetes clusters that run containerized applications, with each node containing the kubelet agent that manages Pods, a container runtime like Docker or containerd, and the kube-proxy that handles network routing. In Azure Kubernetes Service, nodes are Azure virtual machines that can be organized into node pools with different sizes and configurations to support different workload requirements. Understanding node capacity, resource allocation, and health monitoring is essential for operating production Kubernetes clusters effectively.

## Introduction

Alright, let's get hands-on with Kubernetes nodes. In this exercise, we'll be using kubectl to explore the nodes in our cluster. kubectl is your command-line interface to Kubernetes, and it's absolutely essential for working with AKS in Azure.

Make sure you have your terminal open and you're connected to your Kubernetes cluster. Let's dive in.

---

## Part 1: Getting Basic Node Information

The first thing we want to do is see what nodes are in our cluster. We'll use the kubectl get command for this.

We're typing kubectl get nodes and hitting enter. Great! So kubectl get nodes gives us a simple table view. You can see each node listed with some basic information: its name, status, the Kubernetes version it's running, and how long it's been running.

The status column is particularly important - you want to see "Ready" here, which means the node is healthy and able to accept pods. In a production AKS cluster, you might see multiple nodes here. Each one is a virtual machine running in Azure, ready to host your containerized applications.

---

## Part 2: Getting Detailed Node Information

Now, the get command is useful for a quick overview, but when you need more details, you'll want to use the describe command.

We're running kubectl describe nodes now. Wow, that's a lot of information! And this is exactly what you'll need when troubleshooting or planning capacity.

Let's break down what we're seeing here. At the top, you see labels - these are key-value pairs that help organize and identify nodes. You might see labels for the availability zone, instance type, and operating system.

Scrolling down, there's information about the node's capacity - the total CPU and memory available on this node. Just below that, you'll see allocatable resources - this is what's actually available for your pods after system components have reserved what they need.

Further down, you can see all the pods currently running on this node, along with their resource requests. This is really valuable when you're trying to figure out why a pod isn't being scheduled.

And at the bottom, there are events - these show you recent activities on this node, like pods being scheduled or removed.

---

## Part 3: Getting Help with kubectl

Before we go further, let me show you a really useful feature. kubectl has built-in help that you'll use constantly.

We're running kubectl --help. This shows you all the available kubectl commands. There are a lot of them, but you'll find yourself using just a handful most of the time.

You can also get help for specific commands. Let's try kubectl get --help. This shows you all the options and parameters for the get command. Notice the examples section at the bottom - these are really helpful when you're learning.

---

## Part 4: Learning About Kubernetes Resources

Here's another incredibly useful feature. If you want to learn what a Kubernetes resource actually is and what fields it has, you can use kubectl explain.

We're running kubectl explain node. Perfect! This gives you documentation right in your terminal. You can see the description of what a node is, what API version it uses, and what fields it contains.

You can drill down into specific fields too. For example, if you wanted to learn about the node's status field, you could run kubectl explain node.status. This is a great way to explore Kubernetes resources without leaving your terminal.

---

## Part 5: Querying and Formatting Output

Now let's talk about one of the most powerful features of kubectl - the ability to format output in different ways.

By default, kubectl get shows you a table, but you can request other formats. Let's try JSON. We're running kubectl get node with the node name, followed by -o json for output format.

There we go! Now we're seeing all the node information in JSON format. This is the raw data that Kubernetes stores about this node. You can see the metadata section with labels and annotations, the spec section with node configuration, and the status section with current state information.

This JSON format is really useful when you're scripting or when you need to extract specific pieces of information.

---

## Part 6: Using JSON Path for Precise Queries

Speaking of extracting specific information, let's use JSON Path. This is a query language that lets you pull out exactly the fields you need.

Let's say we just want to know how many CPU cores this node has. We can use JSON Path for that. We're running kubectl get node with the node name, then -o jsonpath equals, in quotes, the path '.status.capacity.cpu'.

Nice! It prints just the number of CPU cores. No extra formatting, no table - just the raw value. This is perfect for scripting or automation.

The JSON Path query starts with a dot, then navigates through the JSON structure. We went into status, then capacity, then cpu.

Now here's a question for you to think about: what happens if we run the same command but don't specify a node name?

Let's try it - kubectl get nodes plural with the same JSON Path. Interesting! When you query multiple nodes, JSON Path concatenates the results. So if you have three nodes with two cores each, you'd see something like: two two two, all run together. Keep this in mind when you're writing queries.

---

## Part 7: Lab Challenge

Alright, now it's time for you to put this knowledge into practice. Here's your challenge:

Every Kubernetes object can have labels - those key-value pairs we talked about earlier. Your task is to use kubectl to find the labels on your node. Specifically, you want to confirm the CPU architecture and operating system.

Take a moment to try this yourself. You have all the tools you need - the get command, the describe command, and JSON Path queries. Think about where labels are stored in the node object.

---

## Part 8: Lab Solution Walkthrough

Okay, let's work through this together. There are actually several ways to solve this challenge.

The simplest approach is to look at the labels directly. When we ran kubectl describe nodes earlier, the labels were right at the top of the output. See these labels here? They tell us quite a bit. There's usually a label for the architecture - like arm64 or amd64 - and labels for the operating system, like linux or windows.

Another approach is to use the get command with label output. We're running kubectl get nodes --show-labels. This shows the regular table, but with an additional column containing all the labels.

And if you wanted to use JSON Path to extract just the labels, you could run kubectl get node with the node name and -o jsonpath equals '.metadata.labels'. There you go! Multiple ways to solve the same problem. In Kubernetes, there's often more than one way to get the information you need.

---

## Conclusion

Excellent work! You've now learned how to inspect and query nodes using kubectl. These are fundamental skills that you'll use constantly when working with Kubernetes and Azure Kubernetes Service.

You've learned:
- How to list nodes with kubectl get
- How to see detailed information with kubectl describe
- How to get help and documentation with built-in commands
- How to format output and use JSON Path for queries
- How to find labels and other metadata

In the next lesson, we'll build on these skills as we start deploying applications to our cluster. See you there!
