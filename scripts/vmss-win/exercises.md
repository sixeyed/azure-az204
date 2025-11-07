# Virtual Machine Scale Sets - Windows

## Reference

You can create multiple VMs from the same image and have multiple instances of your application running, but they're all separate VMs with their own IP addresses and public IPs. When you need multiple VM instances running the same workload, you can use a Virtual Machine Scale Set which lets you manage several VMs from a single resource. The Azure documentation provides comprehensive coverage of VMSS features from basic configuration to advanced topics like availability zones and rolling upgrades, while the Azure CLI gives you complete control through the az vmss commands. In this lab we'll use an existing application image and create a VMSS for a Windows application, exploring load balancing, scaling, and autoscaling capabilities.

## Portal

Start by exploring in the Portal - create a new resource and search for VMSS. Select to create the Virtual Machine Scale Set and look through the options.

**VM Configuration**: There's the usual VM settings - image, size and disks. These settings define what each instance in the scale set will look like.

**Orchestration Mode**: You can choose an Orchestration mode - uniform is the most common where all instances are identical. Uniform mode is what we'll use in this lab because it's the standard approach for running multiple instances of the same application.

**Scaling Options**: Under the Scaling section you select the number of VM instances in the scale set. This is the instance count which determines how many VMs run simultaneously. Change the scaling policy to Autoscaling and you'll see scale-out and scale-in thresholds and instance counts. These rules determine when Azure adds or removes instances based on metrics like CPU usage. This automatic scaling capability is one of the key benefits of using VMSS instead of managing individual VMs.

Don't create the VMSS through the portal - we'll use the CLI for better control and understanding of exactly what's being created.

---

## Create a VMSS from a Custom Image

You should have your RG called "labs-vmss-win" created with an image ready to go from the VM images exercises.

**Verify Prerequisites**: Let's start by verifying that we have our resource group and custom image ready. We're checking the resource group first using az group show with table output and the resource group name "labs-vmss-win". This should show our resource group is ready with details about its location and provisioning state. Now let's check for the custom image using az image list with table output for the resource group "labs-vmss-win". You should see the "app01-image" that we created in the VM images lab. This is the Windows Server image with IIS and our application pre-installed. If it's not there, you'll need to go back and complete the VM image lab first before continuing.

**Create the Scale Set**: Now we'll create our Virtual Machine Scale Set from the custom image. We're using az vmss create with the name "vmss-app01", resource group "labs-vmss-win", VM SKU set to Standard_D2s_v5 which provides adequate resources for Windows workloads, instance count set to 3 which creates three VM instances immediately, backend port 3389 for RDP access which we'll use for management, image set to "app01-image" which is our custom image, admin username and password for authentication, and location as West Europe to match where the image is stored. This creates a scale set with three instances using our custom image that has IIS and the application already installed. We're exposing port 3389 for RDP access so we can connect to individual instances if needed.

**Resource Creation Time**: This command takes several minutes to complete. While it's creating, Azure is provisioning three VMs simultaneously from your image, creating a load balancer for traffic distribution, provisioning a public IP address for external access, and configuring all the networking components needed to support the scale set.

**Check VM List**: Once creation is complete, let's check what VMs we have in the resource group using az vm list with table output. Notice there are no individual VMs listed. That's an important distinction - with VMSS, you manage instances through the scale set resource, not as separate VM resources. The instances exist, but they're not top-level VM resources in the resource group.

**Explore in Portal**: Now let's explore in the Portal. Opening the resource group shows several new resources including the VMSS resource itself, a load balancer for distributing traffic, a public IP address for external access, and various networking components like virtual networks and network interfaces. Opening the VMSS resource and navigating to the Instances blade shows three instances, each with its own status. They might be in different states like Running, Creating, or Updating, and the instance numbers might not be sequential - we'll explain why this happens later when we talk about overprovisioning.

**Instance Details**: Click on one of the instances to see its details. Notice it has a private IP address assigned from the virtual network, but no public IP. Individual instances don't get public IPs in a scale set - so how do we access the application? Back in the resource group, opening the public IP address resource shows it's associated with the load balancer. The load balancer is how we'll route traffic to our instances - it provides a single public endpoint that distributes requests across all healthy instances.

**Initial Test**: Try browsing to the public IP address in a web browser. Does the application respond? No, it doesn't work yet. Let's investigate why and fix it.

---

## Load Balancer Configuration

Creating the VMSS also sets up the load balancer, which is a networking component.

**Understanding the Problem**: The VMSS creation automatically set up a load balancer which listens on the public IP and routes traffic to the VMSS instances based on configured rules. But why doesn't it work out of the box? Because the default VMSS setup doesn't include load balancing rules. Without rules, the load balancer has no routing table and doesn't know where to send traffic. It's like having a switchboard with no directory.

**Check Backend Pools**: Let's explore the load balancer in the Portal. First, select Backend pools in the load balancer menu. You'll see all three VMSS instances are registered and showing as running. So the load balancer knows about our VMs - the backend pool membership is correctly configured.

**Check Health Probes**: Next, select Health probes. This is how the load balancer checks if backend resources are ready to receive traffic - it periodically sends test requests to verify the instances are responsive. Right now there are no probes configured, which means the load balancer has no way to know if instances are healthy.

**Check Rules**: Finally, select Load balancing rules. There are none, which is exactly why our app doesn't work. The load balancer receives requests on its public IP but has no rules to forward them to the backend instances.

**Add a Rule**: Let's add a rule to make our application accessible. Click to add a new load balancing rule and give it any name you like. Select the public IP address for the frontend, the VMSS backend pool for the backend, and enter 80 for both the frontend port and backend port. This means clients connect on port 80 and traffic gets forwarded to port 80 on the instances. You'll also need to add a health probe - choose the HTTP type which sends HTTP requests to verify the web server is responding. Save the rule and wait for it to deploy.

**Test the Application**: Load balancers only send traffic to healthy endpoints, which is why the health probe is essential. It continuously checks each instance every few seconds to ensure it's ready to handle requests. Now browse to the public IP address again. You should see the application responding with its HTML page showing the VM name. If you refresh the page multiple times, you might see the same instance repeatedly depending on browser caching and the load balancer's algorithm.

**Test with curl**: Let's use curl instead to make GET requests without caching interfering. Repeat the curl command several times and you should see different VM names in the HTML response as the load balancer distributes requests across all three instances.

---

## Scaling VMSS

There's lots of caching in the browser stack, so command-line testing shows load balancing more clearly.

**Scale Up**: Currently we have three instances running. Let's scale up to five instances to see how easy it is to add capacity. We're using az vmss scale with the resource group "labs-vmss-win", scale set name "vmss-app01", and new-capacity parameter set to 5. This command is remarkably simple - you just specify the desired capacity and Azure handles everything else. It provisions new VMs from the image, adds them to the load balancer, and starts health probing them.

**Watch the Portal**: Let's check the Portal to watch it happen. Opening the VMSS and viewing the Instances blade shows new instances being created. You'll see their status change from Creating to Running as they provision. These new instances get automatically added to the load balancer backend pool. When they become healthy according to our health probe - meaning the web server starts and responds to HTTP requests - they'll start receiving traffic from the load balancer.

**Overprovisioning**: Windows VMs take a few minutes to provision fully, so be patient. You might also see more than five instances temporarily during the creation process. Azure uses overprovisioning as a feature. It knows there's variation in VM startup time - some instances might fail to start, network issues might occur, or other problems could happen. So it creates more instances than you requested. When the desired count are online and healthy, it removes the extra ones that may still be starting up. This is why the instance numbers aren't always sequential - instance 0, 1, 2, 3, 5, 6 might exist, with 4 missing because it was removed during overprovisioning cleanup.

**Test Load Distribution**: Once the new instances are healthy, try your curl command again several times. You should see the new instances appearing in the responses, sharing the request load with the original three instances.

**Configure Autoscaling**: So far we've been using manual scaling where we explicitly set the instance count. But VMSS also supports autoscaling where Azure automatically adjusts capacity based on metrics like CPU usage. For VM-based autoscaling, the primary metric is typically CPU usage. When instances are working too hard and CPU is consistently high, the VMSS adds more instances. When there's not enough work and CPU is low, instances are removed to save money.

**Portal Configuration**: Let's configure autoscaling in the Portal. Opening the VMSS and navigating to the Scaling blade shows the current manual scaling configuration. Switch from manual scaling to Custom autoscale mode to enable metric-based scaling. Select "Scale based on a metric" to use performance metrics rather than a schedule. Set the minimum instance count to 2, maximum to 3, and default to 2. This means the scale set will never go below 2 instances or above 3 instances regardless of load.

**Scale-Out Rule**: Now add a scale-out rule. This defines when to add instances. Set it to increase the instance count by 1 when average CPU usage is greater than 10 percent. We're using a low CPU threshold so we can see the scaling happen quickly during this lab without generating significant load.

**Scale-In Rule**: Add a scale-in rule to define when to remove instances. Set it to decrease by 1 instance when average CPU is less than 8 percent. The lower threshold prevents flapping - instances rapidly scaling up and down. Set the duration to 2 minutes for both rules. This is the time window over which CPU is averaged. Normally you'd use longer windows like 10-15 minutes to avoid reacting to temporary spikes, but we're using short windows for the lab. We're using deliberately low CPU thresholds and short timescales so we can see the scaling behavior happen quickly.

**Observe Scaling**: Currently we have five instances running from our manual scale operation. What happens when we switch to autoscaling with a maximum of 3? The autoscale engine evaluates the current state against the rules. We're above the maximum of 3 instances, so Azure will start removing instances to comply with the autoscale configuration. After a few minutes, you should see two instances entering a deleting state, bringing the count down to the maximum of 3. Those deleting instances are automatically removed from the load balancer backend pool before being deleted, so your application continues working. After a few more minutes with low CPU activity, another instance will be removed, bringing us to the minimum of 2.

**Scaling Patterns**: Notice which instances get removed when scaling in. Is it the most recent ones, or is there a different pattern? Azure typically removes the newest instances first. What happens if a VM was handling a long-running request when it gets deleted? The load balancer and VMSS work together to drain connections gracefully before removing an instance.

---

## Lab

Health probes in the load balancer are a powerful feature for managing lots of failure scenarios. You should test that your application works correctly if instances are unhealthy. With the VMSS you can connect to an instance with Remote Desktop and take the web server offline by stopping the IIS Windows Service. Try that and see if the load balancer works as expected. Can you see the probe status in the portal?

The task is to connect to one of the VMSS instances using Remote Desktop and stop the IIS Windows Service manually. To connect, you'll need to configure NAT rules on the load balancer or use Azure Bastion. Once connected via RDP, open Services, find the IIS service, and stop it. Observe what happens over the next few minutes. The application should continue working on the remaining healthy instances, demonstrating the resilience that VMSS and load balancing provide.

---

## Cleanup

Delete the lab RG, which will delete the VMSS - when the VMSS is deleted it deletes all the VMs.

We're running az group delete with the yes flag to skip confirmation and the resource group name "labs-vmss-win". This deletes the resource group and all resources within it. When the VMSS is deleted, all the VM instances are automatically deleted too, along with the load balancer, public IP, networking components, and everything else we created.
