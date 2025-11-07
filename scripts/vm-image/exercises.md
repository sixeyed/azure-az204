# Building Custom VM Images

## Reference

Building custom VM images eliminates the need to configure software every time you create a new VM. Instead of adding deployment time with post-creation scripts, you can create your own VM image from a fully configured VM. The image serves as a template so any new VM created from it has your application and dependencies pre-installed and ready to go. Understanding image creation, generalization, and deployment is essential for efficient infrastructure management in Azure.

## Create a Base VM

Let's start by creating the foundation for our custom image - a base VM with our application deployed.

First, we'll create a Resource Group. Resource Groups are logical containers that help you organize and manage related Azure resources together. They provide a scope for permissions, billing, and lifecycle management.

We're running az group create with the name "labs-vm-image", adding our "courselabs=azure" tag for tracking, and placing it in the East US location. You can choose your preferred region, but remember that you'll need to use the same region consistently throughout this lab since images are region-specific.

Next, we need to find the right Windows Server image for our needs. Azure has many Windows images available, so let's query the available SKUs to see our options.

We're using az vm image list-skus with the location East US, publisher set to "MicrosoftWindowsServer", and offer set to "WindowsServer", displaying results in table format for easy reading. This shows us all the available Windows Server versions and editions published by Microsoft.

You'll see various options like 2019-datacenter, 2022-datacenter, and different variants like core editions or generation 2 images. We'll use Windows Server 2022 Datacenter for this lab because it's the latest long-term support version.

Now, let's create the VM. We're using az vm create with several important parameters. The location is East US, resource group is "labs-vm-image", and we're naming the VM "app01-base" - the "base" suffix reminds us this is our template VM that we'll image.

For the image parameter, we're using the full URN format: "MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest". This specifies the publisher, offer, SKU, and version. The "core" means it's Server Core without the full GUI, and "g2" indicates generation 2 which supports newer features like UEFI boot.

We're setting the size to Standard_D2s_v5 which provides 2 vCPUs and 8GB RAM, providing an admin username, specifying a unique public IP address DNS name for easy remote access, and creating a strong admin password that meets Azure's complexity requirements.

This will take a few minutes to complete. Azure is provisioning the VM, configuring Windows, and setting up all the supporting resources. Once it's ready, we'll connect via Remote Desktop.

---

## Prepare the VM for Imaging

Now we're connected to the VM through Remote Desktop. First, we'll install IIS Web Server and deploy our application.

In the PowerShell terminal on the VM, we're running Install-WindowsFeature to add the Web-Server role, the .NET Framework 4.5 ASP.NET support, and the Web-Asp-Net45 feature. These are the components needed to run ASP.NET applications on IIS.

Watch as the features are installed - you'll see progress bars and installation messages. This would normally happen every time you create a new VM, which is time-consuming and repetitive. But soon we'll bake this into our image, so new VMs will have these features pre-installed.

Next, we'll remove the default IIS welcome page and deploy our custom application. We're using Remove-Item with the force flag to delete the iisstart.htm file from the wwwroot directory.

Then we're using curl to download our ASP.NET page from the GitHub repository, saving it as default.aspx in the wwwroot directory. This becomes our application's entry point.

Let's test the application locally to make sure it works. We're running curl.exe pointing to localhost to make an HTTP request to the local web server.

You should see HTML output that includes the name of the VM - the application is dynamically reading the computer name and displaying it in the page. Perfect - our application is running and functional.

That's it for this application setup. When you build custom images for your own needs, you can configure whatever software and settings your application requires during this preparation phase.

Before we can create an image, we need to generalize the VM. This is a critical step that removes machine-specific information so the image can be used to create new VMs with their own unique identities. Without generalization, you'd have multiple VMs with the same computer name and security identifiers, which causes serious problems.

For Windows VMs, we use the Sysprep tool which is built into Windows. We're running the sysprep.exe executable from the Windows system32 directory.

In the Sysprep GUI window that opens, select "Enter System Out-of-Box Experience" which puts Windows into the same state it would be in when first starting a new computer. Check the "Generalize" checkbox - this is essential as it removes the machine-specific data. And choose "Shutdown" from the dropdown so the VM shuts down cleanly when Sysprep completes.

Click OK to start the process. Sysprep will generalize the system and then shut down the VM. You'll lose your Remote Desktop connection when this happens - this is expected and normal.

Now, back in your local terminal, we need to deallocate the VM from Azure's perspective. We're running az vm deallocate with the resource group "labs-vm-image" and VM name "app01-base".

This ensures Azure knows the VM is intentionally shut down and releases the compute resources. Without this step, Azure would think the VM crashed and might try to restart it.

Next, we're marking the VM as generalized in Azure's metadata using az vm generalize with the same resource group and VM name. This tells Azure that the VM has been sysprepped and is ready to be used as an image source.

Let's verify the VM is in the correct state. We're running az vm show with the --show-details flag to include runtime information, specifying the resource group and VM name.

Look for the power state in the output - it should show "VM deallocated" confirming the VM is shut down. Also notice there's no public IP address anymore - deallocated VMs release their dynamic public IPs.

---

## Create an Image from the VM

Now comes the easy part - creating the image resource. Because we used a generation 2 SKU for our source VM, we need to specify that in the image creation.

We're running az image create with the resource group "labs-vm-image", naming the image "app01-image", specifying the source as "app01-base" which is our generalized VM, and setting hyper-v-generation to "V2" to match the source VM's generation.

This command creates an image reference to the OS disk. It's surprisingly quick - just a few seconds - because Azure isn't copying the entire disk. Instead, it's creating a managed image resource that references the disk.

Let's verify the image was created successfully. We're running az image list with table output to see all images in our subscription.

You should see your "app01-image" listed with details about its location, provisioning state, and source. This image is now ready to be used as a template for creating new VMs.

---

In practice, you'll want to keep your images separate from your application resources. They have different lifecycles - you might delete and recreate application resources frequently for testing or updates, but you want to preserve your carefully crafted images.

Let's create a new Resource Group for our VM Scale Set that will use this image. We're running az group create with the name "labs-vmss-win" and location East US.

Now we'll copy the image to this new resource group. We're using az image copy with several parameters: source-type set to "image" since we're copying a managed image, source-resource-group pointing to "labs-vm-image" where our image currently lives, source-object-name set to "app01-image", target-location as East US, and target-resource-group as "labs-vmss-win".

This command creates a snapshot of the source disk and copies it to the target location. The progress starts slowly as it initializes, but speeds up quickly once the actual data transfer begins. This is copying gigabytes of data, so it takes a few minutes.

---

Now let's see the real benefit - deploying multiple VMs instantly with our application pre-installed. This is where all that preparation pays off.

We're running az vm create with the resource group "labs-vm-image", VM name "app-vm", image set to "app01-image" which is our custom image, size Standard_D2s_v5 to match what we used for the base VM, admin username, and here's the key part - the --count parameter set to 3 which creates three identical VMs in one command, location East US, and an admin password.

This creates three VMs simultaneously, all from our custom image. Watch the progress - notice how much faster this is than deploying VMs with a standard image and then configuring them. These VMs boot up with IIS already installed, the .NET features configured, and our application already deployed.

---

The VMs are created, but we can't access the web application yet because we need to configure the Network Security Group to allow HTTP traffic.

Let's use the Azure Portal for this since it provides a nice visual interface. Navigate to the resource group "labs-vm-image" and find the Network Security Group resource - it will have a name based on one of your VMs with "NSG" appended.

Click on "Inbound security rules" in the left menu, then click "Add" to create a new rule. We're configuring it to allow HTTP traffic from anywhere on port 80. Set the source to "Any", source port ranges to asterisk for all ports, destination to "Any", service to "HTTP" which automatically sets the destination port to 80, action to "Allow", priority to 1000 or any number lower than the deny-all rule, and give it a name like "AllowHTTP".

Click "Add" and wait for the rule to be created and applied to the NSG.

Now browse to the public IP address of any of your VMs. You'll see the application running, displaying the unique VM name in the HTML. Each VM has its own identity even though they were all created from the same image. Try browsing to the other VMs' IP addresses - each shows its own hostname, confirming they're all properly individualized.

## Lab

You can't access the app yet because the Network Security Group blocks traffic by default. Your task is to add a new NSG rule to allow HTTP traffic on port 80 and confirm you can reach each of the three VMs. You'll see the same application from each, but with different VM names displayed.

These three instances of the same application work independently, but it would be better to have a single DNS address and let Azure load-balance between them. Try creating a Traffic Manager Profile resource in the Portal and configure it to distribute traffic across all three VMs.

## Cleanup

Delete the lab resource group, but don't delete the labs-vmss-win resource group where you copied the image - we'll use that in a future lab.
