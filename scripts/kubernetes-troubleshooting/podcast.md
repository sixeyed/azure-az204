# Kubernetes Troubleshooting - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on Kubernetes Troubleshooting. Today we're diving into one of the most practical and essential skills you'll need as an Azure developer: diagnosing and resolving issues in containerized applications. If you're preparing for the Azure AZ-204 certification or working with Azure Kubernetes Service in production, troubleshooting is where theory meets reality. This is where you'll spend significant time, and mastering these skills will make you invaluable to your team and well-prepared for the exam.

## Why Troubleshooting Matters

Let's start by understanding why troubleshooting is such a critical skill in Kubernetes.

Kubernetes is incredibly powerful, but it's also complex. When you deploy an application, Kubernetes validates that your YAML syntax is correct and that the resource definitions are valid. But it doesn't guarantee your application will actually work. You can have perfectly valid Kubernetes manifests that produce a completely broken application.

Think of it like this: Kubernetes checks your spelling and grammar, but not whether your sentences make sense. Your Deployment might be syntactically correct, but if the selectors don't match the Pod labels, or if the image name has a typo, or if resource requests are too high, the application fails despite valid YAML.

And here's the challenge: Kubernetes components are loosely coupled. A mistake in one place can break everything, but the error messages don't always point directly to the root cause. You need to understand how the pieces fit together to diagnose where things went wrong.

For the AZ-204 exam, Microsoft expects you to demonstrate diagnostic and problem-solving skills. You won't just create configurations - you'll need to troubleshoot broken scenarios and identify solutions. These are practical skills the exam tests heavily.

## Common Points of Failure

Before we dive into troubleshooting techniques, let's understand where things typically go wrong in Kubernetes applications.

The first common failure point is the relationship between Deployments, ReplicaSets, and Pods. Deployments create ReplicaSets, which create Pods. These connections work through label selectors. If the Deployment selector doesn't match the Pod template labels, the Deployment can't manage the Pods. You'll have orphaned Pods that don't scale or update properly.

The second failure point is Services and their connection to Pods. Services route traffic based on selectors. If the Service selector doesn't match Pod labels, the Service has no endpoints and traffic fails. Port configuration is another common issue - if the Service targetPort doesn't match the container port, requests go to the wrong port on the Pod.

Third is container configuration. Image names must be exact - a single typo means Kubernetes can't pull the image. Container commands must be valid - a misspelled executable means the container can't start. Resource requests must be reasonable - requesting more resources than any node provides means Pods stay pending forever.

Fourth is health probe configuration. Liveness probes that check non-existent endpoints cause continuous restarts. Readiness probes with wrong ports or paths prevent Pods from receiving traffic even when the application is running fine.

The tricky part is that these components are loosely coupled. Kubernetes doesn't validate relationships between resources at creation time. You can create a Service that references Pods that don't exist yet, or a Deployment with selectors that will never match anything. Everything gets created successfully, but nothing works.

Understanding these common failure points helps you know where to look when diagnosing issues.

## The Troubleshooting Toolkit

Let's talk about the kubectl commands that form your troubleshooting toolkit. These are essential for the exam and for real-world problem-solving.

kubectl get provides high-level status information. Use it to see which resources exist and their current state. Is your Deployment created? Are Pods running? How many are ready? What's the Service status? This command gives you the big picture and helps you identify which resources need deeper investigation.

Pay attention to Pod status values. "Running" means at least one container is executing, but not necessarily that the application is working. "Pending" indicates scheduling issues or resource constraints. "ImagePullBackOff" means problems pulling the container image. "CrashLoopBackOff" means the container starts but then exits, and Kubernetes is backing off between restart attempts. Each status points to different categories of problems.

kubectl describe provides detailed information about resources, including events. Events are crucial - they show what Kubernetes has been trying to do and what errors it encountered. Pods stuck pending? Events tell you why - insufficient CPU, unsatisfiable constraints, or image pull failures. Container failing? Events show exit codes and error messages.

When using kubectl describe pod, look for several key sections. The status section shows overall Pod state. The conditions section shows whether the Pod has been scheduled, containers are ready, and the Pod is ready. The containers section shows each container's state, restart count, and ready status. The events section at the bottom shows recent activities and errors.

kubectl logs shows output from containers. This is essential for application-level debugging. If your container is running but behaving incorrectly, logs reveal what's happening inside. For containers that are crashing, use the --previous flag to see logs from the crashed instance before it was restarted.

kubectl exec allows you to run commands inside containers. This is useful for debugging networking, checking file system contents, or testing configurations. You can exec into a running container and poke around to see what's actually happening.

kubectl port-forward creates a direct connection from your local machine to a Pod, bypassing Services. This helps isolate whether problems are in the application itself or in the networking configuration. If port-forward works but the Service doesn't, you know the issue is in the Service layer, not the application.

For the exam, know when to use each command and what information each provides. Questions often present scenarios where you need to identify the correct diagnostic approach.

## The Systematic Troubleshooting Approach

Let me walk you through a systematic methodology for troubleshooting Kubernetes applications. This approach keeps you from jumping to conclusions and helps ensure you find the actual root cause.

Start at the highest level and work down. Check your Deployment first. Does it exist? What does kubectl get deployment show for replicas - how many are desired, current, ready, and available? If these numbers don't match expectations, something's wrong with Deployment or ReplicaSet creation.

Next, check the ReplicaSet. Deployments create ReplicaSets, which create Pods. Use kubectl get replicaset to see if the ReplicaSet exists and has the correct number of replicas. If the ReplicaSet exists but has zero replicas, check the Deployment's replica count. If the ReplicaSet shows desired replicas but no current or ready Pods, there's a problem creating Pods.

Then check the Pods. Use kubectl get pods to see Pod status. Are they running? Pending? Crashing? Look at the ready count - if it shows 0/1, the container is running but failing readiness checks. Look at restart counts - high restart counts indicate liveness probe failures or application crashes.

For Pods with problems, use kubectl describe pod. This shows why Pods aren't scheduling, why containers aren't starting, or why probes are failing. Read the events section carefully - Kubernetes usually tells you what's wrong, you just need to know where to look.

If Pods are running but the application isn't accessible, move to Service troubleshooting. Use kubectl get service to verify the Service exists and has the right type. Use kubectl describe service to check endpoints - does the Service have any? No endpoints means either no Pods match the selector or matching Pods aren't passing readiness checks.

Check the Service selector and compare it to Pod labels. Use kubectl get pods --show-labels to see actual labels on Pods. Do they match the Service selector exactly? Even a small typo breaks the connection.

Verify port configuration. The Service targetPort must match the container port. Use kubectl describe pod or kubectl get pod with JSON/YAML output to see what ports containers are actually listening on.

This top-down, systematic approach prevents you from getting lost in details and helps you isolate the actual problem.

## Resource Requests and Limits

Resource management issues are common in Kubernetes and frequently tested on the AZ-204 exam. Let's understand how to diagnose and fix them.

When you create a Pod, you can specify resource requests and limits. Requests tell Kubernetes how much CPU and memory the container needs. Kubernetes uses requests to decide which node to schedule the Pod on. If no node has enough available capacity to meet the requests, the Pod stays in Pending status.

Limits define the maximum resources a container can use. If a container tries to use more CPU than its limit, it gets throttled. If it tries to use more memory than its limit, it gets killed with an Out Of Memory error.

When troubleshooting Pods stuck in Pending, use kubectl describe pod and look for events saying "Insufficient CPU" or "Insufficient memory". This means the Pod's resource requests are too high for any node in the cluster.

The solution depends on the situation. If the requests are realistic but the cluster is too small, you need to scale the cluster by adding nodes. In Azure Kubernetes Service, you can scale node pools manually or enable the cluster autoscaler. If the requests are unrealistic - perhaps someone specified 32 CPUs for a simple web app - you need to reduce the requests to reasonable values.

Understanding resource units is important. CPU is measured in cores or millicores. One full CPU core is written as "1" or "1000m". Half a core is "0.5" or "500m". A quarter core is "250m". Memory uses standard units - Mi for mebibytes, Gi for gibibytes.

For troubleshooting, if Pods won't schedule, check resource requests. If Pods are being killed, check if they're exceeding memory limits. If performance is poor, check if containers are hitting CPU limits.

## Image Pull Errors

Image pull errors are another common issue that's straightforward to diagnose but requires understanding of container registries.

When Kubernetes creates a Pod, it needs to pull container images from a registry. If the image can't be pulled, the Pod status shows ImagePullBackOff or ErrImagePull. This is Kubernetes backing off between retry attempts - it doesn't continuously hammer the registry, it increases the delay between tries.

Use kubectl describe pod to see the exact error message. Common causes include typos in the image name, the image tag doesn't exist, the image is in a private registry requiring authentication, or the registry is unreachable.

Verify the image name carefully. It needs to be exact - registry address, repository name, image name, and tag all must be correct. If no tag is specified, Kubernetes assumes "latest", which might not exist.

For private registries like Azure Container Registry, Pods need credentials to pull images. In AKS, you can integrate the cluster with ACR using managed identity or service principal. If integration isn't set up, you need to create an image pull secret and reference it in your Pod spec.

For troubleshooting, check the exact error message in Pod events. Verify the image name is correct. Try pulling the image manually with docker pull to confirm it exists and you have access. Check cluster authentication to the registry.

## Container Startup Failures

When containers fail to start, the troubleshooting approach depends on the failure mode.

If you see RunContainerError, the container runtime can't start the container. This usually indicates problems with the container command or arguments. Check the command and args fields in your Pod spec. If you've overridden the container's default command, make sure it's valid and the executable exists in the container image.

If the container starts but immediately exits, you'll see CrashLoopBackOff. The container is starting successfully but then terminating, and Kubernetes is restarting it with increasing delays. Use kubectl logs with the Pod name to see application output. If the container crashes before logs are written, use kubectl logs --previous to see logs from the previous instance.

Common causes include the application crashing due to missing configuration, the command completing normally when it should run indefinitely, or missing dependencies inside the container.

For troubleshooting, always check logs first. They usually reveal what's happening inside the container. Check that the container image is correct - perhaps you're using a different version than intended. Verify environment variables and configuration are correct. For applications that need configuration files or secrets, confirm they're mounted correctly.

## Health Probe Configuration

Health probes are critical for production reliability but commonly misconfigured. Understanding how to troubleshoot probe failures is essential for the exam.

Liveness probes determine whether a container should be restarted. If a liveness probe fails, Kubernetes kills the container and starts a new one. Watch for high restart counts - if a Pod shows 50 restarts, there's almost certainly a liveness probe issue.

Use kubectl describe pod to see probe configuration and recent probe results. Look for events about liveness probes failing. Then verify the probe configuration makes sense. Is it checking the correct port? Does the HTTP path actually exist? For exec probes, does the command return the right exit code?

A common mistake is configuring liveness probes that are too aggressive. If initialDelaySeconds is too short, probes start before the application is ready to respond, causing unnecessary restarts. If failureThreshold is too low, temporary issues cause restarts when the application might recover on its own.

Readiness probes determine whether a Pod should receive traffic. Failed readiness probes don't restart the container - they just remove the Pod from Service endpoints. If your Pod shows 0/1 in the Ready column, readiness probes are failing.

Again, kubectl describe pod shows probe configuration and failures. Verify the probe checks the right endpoint. For applications that need startup time, ensure initialDelaySeconds gives enough time for the application to become ready.

A best practice is using different endpoints for liveness and readiness. Liveness should check basic health - can the application process respond at all? Readiness should check whether the application is ready to handle requests - are dependencies available, is initialization complete?

For troubleshooting, if containers keep restarting, suspect liveness probes. If Pods are running but not receiving traffic, suspect readiness probes. Use kubectl port-forward to directly test the probe endpoint and confirm it's working as expected.

## Service Networking Issues

Service networking problems are common and require understanding the relationships between Services, selectors, labels, and Pods.

When traffic doesn't reach your application through a Service, start by checking if the Service has endpoints. Use kubectl describe service and look for the Endpoints section. If it's empty, the Service isn't finding any Pods.

No endpoints usually means one of two things. Either the Service selector doesn't match any Pod labels, or matching Pods exist but aren't passing readiness probes.

Compare the Service selector to actual Pod labels. Use kubectl get service to see the selector, and kubectl get pods --show-labels to see labels. They must match exactly. Even differences in capitalization break the connection.

If labels match but endpoints are still empty, check Pod readiness. Use kubectl get pods to see the Ready column. If it shows 0/1, Pods aren't ready. Use kubectl describe pod to see why readiness probes are failing.

If endpoints exist but traffic still doesn't reach the application, check port configuration. The Service has a port it listens on and a targetPort where traffic gets forwarded. The targetPort must match the container port.

Use kubectl describe service to see port configuration. Use kubectl describe pod to see what ports containers expose. These must align for traffic to reach the application.

For NodePort Services, remember the port must be in the 30000-32767 range. Values outside this range are invalid. For LoadBalancer Services in AKS, external-ip might show "pending" while Azure provisions the Load Balancer. This is normal and can take a minute or two.

## Common Exam Scenarios

Let's walk through typical exam scenarios so you recognize these patterns and know how to respond.

Scenario one: A Pod is stuck in Pending status. What do you check? Use kubectl describe pod to see events. Look for messages about insufficient resources, unschedulable Pods, or image pull errors. If it's resource constraints, either reduce Pod requests or scale the cluster. If it's node selectors or taints, adjust those constraints or ensure nodes meet the requirements.

Scenario two: A Pod shows CrashLoopBackOff. What's your approach? Use kubectl logs to see application output. Use kubectl logs --previous if the container crashes before writing logs. Check that the container image is correct, environment variables are set properly, and any required configuration is mounted. Verify the container command is valid.

Scenario three: A Pod shows 0/1 Ready. What does this mean and how do you fix it? The container is running but failing readiness probes. Use kubectl describe pod to see probe configuration and failures. Verify the probe checks the correct port and path. Ensure the application is actually listening on the expected port. Check if the application needs more startup time by increasing initialDelaySeconds.

Scenario four: A Service exists but you can't access the application. How do you troubleshoot? Check if the Service has endpoints with kubectl describe service. No endpoints means either selector mismatch or readiness probe failures. Verify the selector matches Pod labels exactly. Check that Pods are ready. Verify port configuration - targetPort must match container port.

Scenario five: A Deployment shows 0/1 replicas ready. What could be wrong? This could be many things. Check the ReplicaSet to see if Pods are being created. If Pods exist, check their status. Are they pending, crashing, or failing probes? Work through the systematic troubleshooting steps based on what you find.

## Azure-Specific Troubleshooting

For the AZ-204 exam, understand these Azure-specific troubleshooting aspects.

Azure Monitor and Container Insights provide enhanced visibility into AKS clusters. You can view container logs in the Azure portal, not just through kubectl. You can see cluster-level metrics, node health, and container performance. Understand how to enable Container Insights and where to find this information in the portal.

For LoadBalancer Services that won't provision, Azure-specific issues might be involved. Check if you have quota for Load Balancers in your subscription. Verify the AKS service principal or managed identity has appropriate permissions to create Azure resources. Check subnet configuration if using internal Load Balancers.

For image pull errors from Azure Container Registry, ensure AKS integration is properly configured. You can attach ACR to AKS, giving the cluster automatic pull access. If not attached, you need image pull secrets or other authentication mechanisms.

Azure Policy can enforce requirements on AKS clusters. If Pods won't start or Services won't create, check if Azure Policy is blocking them for non-compliance.

Network security groups and virtual network configuration can affect connectivity. If you can create LoadBalancer Services but can't reach them externally, check NSG rules on the subnet.

## Key Exam Takeaways

Let me summarize what you absolutely must know about Kubernetes troubleshooting for the AZ-204 exam.

Number one: Know the systematic troubleshooting approach. Start with high-level resources like Deployments, work down to ReplicaSets and Pods, then check Services. This methodology helps you isolate issues efficiently.

Number two: Master the kubectl diagnostic commands. Know when to use get, describe, logs, and exec. Understand what information each provides and how to interpret the output.

Number three: Understand Pod status values and what they indicate. Pending means scheduling issues. ImagePullBackOff means image problems. CrashLoopBackOff means startup failures. Each status points to different troubleshooting paths.

Number four: Know how to diagnose resource constraint issues. Pods pending with "Insufficient CPU" or "Insufficient memory" need either reduced requests or more cluster capacity.

Number five: Understand health probe configuration and troubleshooting. Liveness probe failures cause restarts. Readiness probe failures prevent traffic routing. Know how to verify probe configurations make sense.

Number six: Know how to troubleshoot Service networking. Check endpoints to see if Services are finding Pods. Verify selectors match labels. Confirm port configuration aligns.

Number seven: Understand the relationship between Deployments, ReplicaSets, and Pods through label selectors. Mismatched selectors break the management chain.

Number eight: Be familiar with Azure-specific troubleshooting using Container Insights, Azure Monitor, and Azure portal diagnostics.

## Practical Preparation

To prepare effectively for troubleshooting questions on the exam, I recommend several things.

Set up an AKS cluster and intentionally break things. Create Deployments with wrong selectors, Services with mismatched ports, Pods with bad image names. Practice diagnosing and fixing each issue. This hands-on experience builds intuition you can't get from reading.

Work through the troubleshooting lab we've discussed, but don't just follow the solution. When you encounter each issue, stop and try to diagnose it yourself. What commands would you use? What are you looking for? Then check the solution to see if your approach was correct.

Practice reading kubectl describe output. What sections matter most? What events indicate which problems? The more familiar you are with normal output, the easier it is to spot anomalies.

Time yourself troubleshooting scenarios. The exam has time limits. Being efficient with commands and knowing where to look for information helps you answer questions quickly.

Most importantly, understand the why behind each issue. Don't just memorize that ImagePullBackOff means image problems - understand why Kubernetes can't pull images, what fixes apply to different causes, and how to prevent the issue. Deep understanding helps with complex exam scenarios.

## Final Thoughts

Kubernetes troubleshooting is a practical skill that the AZ-204 exam tests heavily. You won't just create configurations - you'll diagnose broken scenarios, identify root causes, and determine correct solutions.

Master the diagnostic commands and systematic approach we've covered. Understand common failure patterns and how to recognize them. Practice hands-on troubleshooting until it becomes second nature.

The exam rewards methodical thinking over guessing. When presented with troubleshooting scenarios, work through the diagnostic steps systematically. Check high-level resources first, narrow down to specific components, gather information before acting. This approach leads to correct answers.

Remember that troubleshooting is an essential skill for production Kubernetes work, not just exam preparation. The time you invest learning these techniques pays dividends throughout your career.

Thanks for listening to this episode on Kubernetes Troubleshooting. I hope this gives you the systematic approach and practical skills you need for both the AZ-204 exam and for building reliable applications in Azure Kubernetes Service. Good luck with your studies!
