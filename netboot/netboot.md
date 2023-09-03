# NetBoot for G3/G4/G5

This is a software-only method to reinstall the operating system on most G3 and all G4/G5 models. That means you won't need a CD, USB, or FireWire to reinstall the OS on your PowerPC Mac; all you need is a virtual machine running on your modern Mac.

## Install Mac OS X 10.4 Server in UTM

UTM is a powerful graphical interface for QEMU that makes it easier to launch QEMU VMs without using the command line. You can get UTM for free from its project page:

https://github.com/utmapp/UTM

Or you can support the project by buying a paid version from the Mac App Store. Their functionalities are the same.

https://apps.apple.com/us/app/utm-virtual-machines/id1538878817?mt=12

Create a new VM in UTM with the following configuration:

- Choose “Emulation” in the first screen
- Choose “Other” in the Operating System screen
- Use the Mac OS X 10.4 Server Install DVD image as the boot image. You can find this DVD image on the [Internet Archive](https://archive.org) using the keyword `0Z691-5228-A`.
- Choose the `PowerPC` architecture and the `Mac99` system. Set the memory to 2GB and use one core. That is actually the maximum that this emulated system can support.
- For storage, you'll need at least 10GB. Having 20GB or more would be ideal if you want to try more NetBoot images later.

After the VM is created, you will need to modify two more settings before starting it.

- Network: Change the Network Mode to Bridged and bridge it to your LAN, so that your G3/G4/G5 can later find this VM.
- Network: Change Emulated Network Card to `sungem`

Start the VM and install Mac OS X 10.4 Server. The installation process is pretty straightforward. You can deselect extra languages and printer drivers to save some time and space.

After the installation is completed, it will restart to the installer on the DVD again. Shut down the VM and remove the DVD device so that you can start from the hard drive. It seems you might have to remove the device, rather than simply ejecting the image.

## Configuring NetBoot

Now you have a running Mac OS X 10.4 Server that can provide NetBoot to your PowerPC machines.

Let’s set up several images for NetBoot.

### NetBoot Image for Mac OS 9

For Mac OS 9, you can simply download the following installation package from Apple.

https://support.apple.com/kb/DL1192?locale=en_US

http://support.apple.com/downloads/DL1192/en_US/NetBoot9.dmg

In case that address becomes unreachable, here are its hash values. In the future, you will be able to find that file using search engines with those values.

|Hash Method|Value|
|---|---|
|MD5|3020b3968cb5448ad74da8ca3f11ff40|
|SHA1|3b1665c12b76c8c031bbb14bd8fed62f82643de8|

After you install that package, a new NetBoot image for OS 9 will become active in the Server app.

### NetBoot Image for Mac OS X

There are two types of NetBoot images for Mac OS X: Install and Live System. You can create an Install-type image from a disk image. A Live System image can be made from a system partition.

## Boot from Network

During start-up, hold down the `N` key, and your machine will locate the NetBoot server and boot from its default image.

You can also select which image to boot from by using the Startup Disk control panel in System Preferences.