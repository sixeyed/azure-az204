# Building Custom VM Images - Exercises Introduction

We've covered custom VM images as a solution to reduce deployment time and complexity - instead of installing applications after each VM creation, create an image from a fully configured VM so new VMs are ready immediately. Now let's build and deploy custom images.

## What You'll Do

You'll start by **creating a base VM** with your application deployed. You'll use `az vm image list-skus` to find Windows Server images, then create a VM using the full URN format like "MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest" specifying publisher, offer, SKU, and version with generation 2 supporting UEFI boot and newer features.

Then you'll **deploy the application** by connecting via Remote Desktop and installing IIS Web Server with PowerShell running `Install-WindowsFeature` for Web-Server role, .NET Framework ASP.NET support, and Web-Asp-Net45 feature. You'll deploy a custom ASP.NET page that displays the VM name dynamically, testing it locally before imaging.

Next comes **preparing the VM for imaging** - a critical step removing machine-specific information so the image can create new VMs with unique identities. You'll run Sysprep.exe selecting "Enter System Out-of-Box Experience", checking "Generalize" to remove machine-specific data, and choosing "Shutdown". Without generalization, multiple VMs would have the same computer name and security identifiers causing serious problems.

You'll **deallocate and generalize** from Azure's perspective using `az vm deallocate` to release compute resources and `az vm generalize` to mark the VM as sysprepped in Azure's metadata. Verification with `az vm show --show-details` confirms "VM deallocated" power state and no public IP.

You'll **create the image** using `az image create` specifying the source as your generalized VM and hyper-v-generation "V2" matching the source. This is surprisingly quick - just seconds - because Azure creates an image reference without copying the entire disk.

Then you'll **copy the image** to another resource group using `az image copy` for separation - images have different lifecycles than application resources. This creates a snapshot and copies gigabytes of data taking a few minutes.

Finally, you'll **deploy VMs from the image** using `az vm create` with `--image` pointing to your custom image and `--count 3` creating three identical VMs in one command. These VMs boot with IIS, .NET, and your application already installed - dramatically faster than standard deployment.

The key learning: Custom images bake configuration into reusable templates, Sysprep/generalization removes machine-specific data, and deployment from images is much faster than post-deployment configuration.

Let's build efficient VM templates!
