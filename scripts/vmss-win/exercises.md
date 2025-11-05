# Virtual Machine Scale Sets - Windows - Exercises

## Exercise 1: Create VMSS from Custom Image

### Verify Prerequisites

Let's start by verifying that we have our resource group and custom image ready from the previous lab. These are prerequisites for this exercise.

We're checking the resource group first using az group show with table output and the resource group name "labs-vmss-win".

This should show our resource group is ready with details about its location and provisioning state. Now let's check for the custom image using az image list with table output for the resource group "labs-vmss-win".

You should see the "app01-image" that we created in the VM images lab. This is the Windows Server image with IIS and our application pre-installed. If it's not there, you'll need to go back and complete the VM image lab first before continuing.

### Create the VMSS

Now we'll create our Virtual Machine Scale Set from the custom image. We need to specify several parameters to configure the scale set properly.

We're using az vmss create with the name "vmss-app01", resource group "labs-vmss-win", VM SKU set to Standard_D2s_v5 which provides adequate resources for Windows workloads, instance count set to 3 which creates three VM instances immediately, backend port 3389 for RDP access which we'll use for management, image set to "app01-image" which is our custom image, admin username and password for authentication, and location as West Europe to match where the image is stored.

This creates a scale set with three instances, using our custom image that has IIS and the application already installed. We're exposing port 3389 for RDP access so we can connect to individual instances if needed.

This command takes several minutes to complete. While it's creating, Azure is provisioning three VMs simultaneously from your image, creating a load balancer for traffic distribution, provisioning a public IP address for external access, and configuring all the networking components needed to support the scale set.

### Explore the Resources

Once creation is complete, let's check what VMs we have in the resource group. We're running az vm list with table output for the resource group "labs-vmss-win".

Notice there are no individual VMs listed. That's an important distinction - with VMSS, you manage instances through the scale set resource, not as separate VM resources. The instances exist, but they're not top-level VM resources in the resource group.

Now let's explore in the Portal. Opening the resource group shows several new resources including the VMSS resource itself, a load balancer for distributing traffic, a public IP address for external access, and various networking components like virtual networks and network interfaces.

Opening the VMSS resource and navigating to the Instances blade shows three instances, each with its own status. They might be in different states like Running, Creating, or Updating, and the instance numbers might not be sequential - we'll explain why this happens later when we talk about overprovisioning.

Click on one of the instances to see its details. Notice it has a private IP address assigned from the virtual network, but no public IP. Individual instances don't get public IPs in a scale set - so how do we access the application?

Back in the resource group, opening the public IP address resource shows it's associated with the load balancer. The load balancer is how we'll route traffic to our instances - it provides a single public endpoint that distributes requests across all healthy instances.

Try browsing to the public IP address in a web browser. Does the application respond? No, it doesn't work yet. Let's investigate why and fix it.

## Exercise 2: Configure Load Balancing

### Understanding the Load Balancer

The VMSS creation automatically set up a load balancer, which is a networking component that listens on the public IP and routes traffic to the VMSS instances based on configured rules.

But why doesn't it work out of the box? Because the default VMSS setup doesn't include load balancing rules. Without rules, the load balancer has no routing table and doesn't know where to send traffic. It's like having a switchboard with no directory.

Let's explore the load balancer in the Portal to understand what's missing.

First, select Backend pools in the load balancer menu. You'll see all three VMSS instances are registered and showing as running. So the load balancer knows about our VMs - the backend pool membership is correctly configured.

Next, select Health probes. This is how the load balancer checks if backend resources are ready to receive traffic - it periodically sends test requests to verify the instances are responsive. Right now there are no probes configured, which means the load balancer has no way to know if instances are healthy.

Finally, select Load balancing rules. There are none, which is exactly why our app doesn't work. The load balancer receives requests on its public IP but has no rules to forward them to the backend instances.

### Add a Load Balancing Rule

Let's add a rule to make our application accessible. Click to add a new load balancing rule and we'll configure it step by step.

Give it any name you like - something descriptive like "http-rule" works well.

For the frontend configuration, select the public IP address that was created with the scale set. This is what clients will connect to.

For the backend pool, select the VMSS backend pool that contains all our instances.

For both the frontend port and backend port, enter 80. This means clients connect on port 80 and traffic gets forwarded to port 80 on the instances.

You'll also need to create a health probe as part of this rule creation. Click to add a new health probe, and select HTTP as the probe type. This sends HTTP requests to verify the web server is responding. You can use the default path of slash which requests the root page.

Save the rule and wait for it to deploy. This takes a few seconds as Azure updates the load balancer configuration and starts running health probes.

### Test the Application

Load balancers only send traffic to healthy endpoints, which is why the health probe is essential. It continuously checks each instance every few seconds to ensure it's ready to handle requests.

Now browse to the public IP address again in your web browser. You should see the application responding with its HTML page showing the VM name.

If you refresh the page multiple times, do you see responses from different VMs? Depending on browser caching and the load balancer's algorithm, you might see the same instance repeatedly.

Let's use curl instead to make GET requests without caching interfering. We're running curl with your public IP address.

Repeat this command several times - hit the up arrow and enter repeatedly. You should see different VM names in the HTML response as the load balancer distributes requests across all three instances in a round-robin or similar pattern.

## Exercise 3: Manual Scaling

### Scale Up

Currently we have three instances running. Let's scale up to five instances to see how easy it is to add capacity.

We're using az vmss scale with the resource group "labs-vmss-win", scale set name "vmss-app01", and new-capacity parameter set to 5.

This command is remarkably simple - you just specify the desired capacity and Azure handles everything else. It provisions new VMs from the image, adds them to the load balancer, and starts health probing them.

Let's check the Portal to watch it happen. Opening the VMSS and viewing the Instances blade shows new instances being created. You'll see their status change from Creating to Running as they provision.

These new instances get automatically added to the load balancer backend pool. When they become healthy according to our health probe - meaning the web server starts and responds to HTTP requests - they'll start receiving traffic from the load balancer.

Windows VMs take a few minutes to provision fully, so be patient. You might also see more than five instances temporarily during the creation process. Why is this?

Azure uses overprovisioning as a feature. It knows there's variation in VM startup time - some instances might fail to start, network issues might occur, or other problems could happen. So it creates more instances than you requested. When the desired count are online and healthy, it removes the extra ones that may still be starting up. This is why the instance numbers aren't always sequential - instance 0, 1, 2, 3, 5, 6 might exist, with 4 missing because it was removed during overprovisioning cleanup.

Once the new instances are healthy, try your curl command again several times. You should see the new instances appearing in the responses, sharing the request load with the original three instances.

## Exercise 4: Autoscaling

### Configure Autoscaling

So far we've been using manual scaling where we explicitly set the instance count. But VMSS also supports autoscaling, where Azure automatically adjusts capacity based on metrics like CPU usage, memory, network traffic, or custom metrics.

For VM-based autoscaling, the primary metric is typically CPU usage. When instances are working too hard and CPU is consistently high, the VMSS adds more instances. When there's not enough work and CPU is low, instances are removed to save money.

Let's configure autoscaling in the Portal. Opening the VMSS and navigating to the Scaling blade shows the current manual scaling configuration.

Switch from manual scaling to Custom autoscale mode to enable metric-based scaling.

Select "Scale based on a metric" to use performance metrics rather than a schedule.

Set the minimum instance count to 2, maximum to 3, and default to 2. This means the scale set will never go below 2 instances or above 3 instances regardless of load.

Now add a scale-out rule. This defines when to add instances. Set it to increase the instance count by 1 when average CPU usage is greater than 10 percent. We're using a low CPU threshold so we can see the scaling happen quickly during this lab without generating significant load.

Add a scale-in rule to define when to remove instances. Set it to decrease by 1 instance when average CPU is less than 8 percent. The lower threshold prevents flapping - instances rapidly scaling up and down.

Set the duration to 2 minutes for both rules. This is the time window over which CPU is averaged. Normally you'd use longer windows like 10-15 minutes to avoid reacting to temporary spikes, but we're using short windows for the lab.

We're using deliberately low CPU thresholds and short timescales so we can see the scaling behavior happen quickly during this lab without having to generate real load.

### Observe Scaling Behavior

Currently we have five instances running from our manual scale operation. What happens when we switch to autoscaling with a maximum of 3?

The autoscale engine evaluates the current state against the rules. We're above the maximum of 3 instances, so Azure will start removing instances to comply with the autoscale configuration.

After a few minutes, you should see two instances entering a deleting state in the Portal, bringing the count down to the maximum of 3 instances.

Those deleting instances are automatically removed from the load balancer backend pool before being deleted, so your application continues working during the scale-in operation. The health probe marks them as unhealthy once they stop responding, and traffic shifts to the remaining healthy instances.

After a few more minutes with low CPU activity across the instances, another instance will be removed, bringing us to the minimum of 2 instances. The scale-in rule triggered because average CPU is below 8 percent.

Notice which instances get removed when scaling in. Is it the most recent ones, or is there a different pattern? Azure typically removes the newest instances first, but the exact behavior depends on several factors including zone distribution and availability set configuration. This is an interesting consideration - what happens if a VM was handling a long-running request when it gets deleted? The load balancer and VMSS work together to drain connections gracefully before removing an instance, giving active connections time to complete.

## Exercise 5: Lab Challenge - Health Probes

Here's your challenge exercise to deepen your understanding of health probes and instance management.

Health probes are a powerful feature for managing failure scenarios automatically. You should test that your application works correctly when instances become unhealthy rather than being deleted.

The task is to connect to one of the VMSS instances using Remote Desktop and stop the IIS Windows Service manually. This will make that instance fail its health probe because it will stop responding to HTTP requests.

To connect, you'll need to configure NAT rules on the load balancer or use Azure Bastion. Look in the Portal for the connection options on the instance.

Once connected via RDP, open Services (services.msc), find the IIS service (called "World Wide Web Publishing Service"), and stop it.

Observe what happens over the next few minutes. Does the load balancer stop sending traffic to that instance? Can you see the probe status change in the Portal under the load balancer's backend pool?

The application should continue working on the remaining healthy instances, demonstrating the resilience that VMSS and load balancing provide. The unhealthy instance stays in the backend pool but marked as unhealthy, so it doesn't receive traffic. If you restart the IIS service, it should become healthy again and start receiving traffic.

Take some time to work through this challenge and explore how health probes enable automatic failure detection and traffic shifting.

## Cleanup

When you're finished exploring scale sets and load balancing, clean up the lab resources to avoid ongoing charges.

We're running az group delete with the -y flag to skip confirmation and the resource group name "labs-vmss-win".

This deletes the resource group and all resources within it. When the VMSS is deleted, all the VM instances are automatically deleted too, along with the load balancer, public IP, networking components, and everything else we created. The cleanup takes a few minutes to complete.

That concludes our Virtual Machine Scale Sets lab. You've learned how to create a VMSS from a custom image, configure load balancing with health probes for high availability, scale manually by changing instance count, configure autoscaling based on CPU metrics, and understand how health probes enable automatic failure handling.
