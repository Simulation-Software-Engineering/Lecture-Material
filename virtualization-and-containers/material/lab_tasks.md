# Working with Virtualization and Containers

In this exercise we will work the virtualization and container techniques that we have seen in the lecture. We will set up virtual machines manually and automatized and experiment a bit with containers.

## Prerequisites

- Installed and working VirtualBox, Vagrant and Docker.
- GitLab account.
- Some available space on your hard drive or a USB drive (about 8 GB to be safe).

## VirtualBox

In part of the

We will install "Ubuntu Server 20.04" a lightweight version of Ubuntu without graphical user interface. However, the ISO image has still 1.2 GB so you might want to start the [download of the image called "Ubuntu Server 20.04.3 LTS"](https://ubuntu.com/download/server) before continuing reading. If you see the name "Focal Fossa" some places, this is the codename of the 20.04 release of Ubuntu.


- Download the ISO image from the [Ubuntu homepage](https://ubuntu.com/download/server. Please choose the "20.04.3 LTS" image which is called "ubuntu-20.04.3-live-server-amd64.iso"
- While the image is being downloaded, you can start preparing the VM already. Create a new VM in VirtualBox called "Ubuntu Server" and assign 2048 MB of memory to it. If that is not possible on your machine, choose a larger or smaller amount of memory. Make sure the your virtual hard drive is large enough. 6 GB should be enough for this exercise. If you choose "dynamic allocation" the actual image size should not grow beyond 4 GB during this exercise.
- Mount the `ubuntu-20.04.3-live-server-amd64.iso` to your virtual machine's cdrom drive (Storage -> Controller: IDE), make sure the graphics card has at least 32 MB video memory and start the VM.
- The VM will boot from the Ubuntu image and will welcome you with the a configuration program. Choose your preferred language and then choose "Start Ubuntu Server". This will boot Ubuntu and bring you to the installation routine. The boot process might take a short while since Ubuntu will generate some files and run some checks.
- When the boot process has finished you will be presented with Ubuntu's installation program. Go through it carefully.
  - Choose your preferred language and keyboard layout. Note that you cannot use your mouse in the menus.
  - For most settings you can accept the default values Ubuntu suggests (mirror, empty proxy, using entire disk with LVM group, storage configuration etc.)
  - Confirm formatting of the virtual hard drive ("Confirm destructive action") if asked so.
- When setting up your user, please use your GitLab username, e.g. `jaustar`, as username and choose the username + VM, e.g. `jaustarvm`, as the server's name. The password you can choose freely. Note that the password cannot be empty. If you do not feel creative, use `vm` as password.
- When you are asked about the SSH Setup, please activate the `Install OpenSSH Server` option (using spacebar), do not import any SSH identiy and continue.
- In the next window you skip all succested "Featured Server Snaps" to keep the size of the image minimal. It suggests common software used on the Ubuntu Server edition, such as Docker, for example. However, we do not need it here. Confirming your choice will start the installation procedure.
- The installation procedure might take a while since it will also install security updates. You can already start reading on the subsequent sections.
- After the installation has finished confirm the reboot with `Reboot Now`.
  - Ubuntu should complain that it cannot unmount the cdrom drive. Check in the settings of your VM that VirtualBox has unmounted the `ubuntu-20.04.3-live-server-amd64.iso` image and confirm the reboot by pressing enter. If the image is still mounted, please shutdown the VM (Machine -> ACPI Shutdown), unmount the image manually and boot the VM again.
- After (re)booting you will be greeted by the Ubuntu login screen. If it looks like a mess press `CTRL-C` to clear the screen. You might have to wait for a moment and maybe switch in and out of the VM's window for it to be refreshed properly. Login using your username and password.
- We want to install [`neofetch`](https://github.com/dylanaraps/neofetch) which prints the system's information to the terminal and take a screenshot of this.
  - Install `neofetch` via `sudo apt update && sudo apt install neofetch`. This command will download and install `neofetch`.
  - Clear the terminal using `clear` and run neofetch via by typing`neofetch` into the terminal and pressing `Enter`.
  - Take a screenshot via VirtualBox. At the top of the VirtualBox window you find the menu item `View`. There you find the option `Take Screenshot (Host+E)`. Save the Screenshot as `neofetch-screenshot-USERNAME.png` (replace `USERNAME` by your username).
- Now we want to open an issue on the GitLab  Repository TODO and upload the screenshot to document your success.
  - Open a merge request in the GitHub Repository TODO.
    - As title choose "[`USERNAME`] Ubuntu Server Installation"
    - Attach the screenshot ('Attach a file`). By default, the screenshot is saved in the folder of your VM.
    - Add the `VirtualBox` Label to the issue and assign the issue to the lecturers `jaustar` and `uekermbn` and create the issue.
    - Double-check that your issue looks as expected. You will find an example issue in the GitLab Repository.

Congratulations. You have successfully set up a virtual machine, installed Ubuntu and installed additional software. You are now done with this part of the exercise. If you do not want to play with the VM later nor do you want to do any of the optional assignments, you can poweroff and delete the VM.

### Further notes

- If your mouse pointer gets caught, use the right `CTRL` button on your keyboard to relase it again.
- You can find more information on the installation procedure in the [Ubuntu Server documentation](https://ubuntu.com/server/docs).
- If you want to set up SSH forwarding to your VM, you can find instructions, for example, [on the codebot homepage](https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup). The instructions are for Ubuntu 18.04, but it also works for Ubuntu 20.04. Note that most of the steps are preconfigured in current VirtualBox releases, but it does not hurt to check whether the settings are set properly.


## Vagrant

In the previous section we have set up a VM manually. This was quite tedious. Therefore, we want to automatize this process now by using [Vagrant](https://www.vagrantup.com/).

- Setup your own Vagrant box


### Further notes

- By default, Vagrant will install all files in your home directory. If Vagrant should use a different directory, you can set the environment variable `VAGRANT_HOME` to point the alternative directory. This could look like this:

  ```
  export VAGRANT_HOME=/media/jaustar/external-ssd/virtualmachines/vagrant/.vagrant.d/
  ```

  You might want to add this line to your `.bashrc` to make this change persistent.

## Docker


## Optional extension

- Use Vagrant to set up a box with Docker
- Publish a Vagrant box to Vagrant cloud. Please link to it in the issue.
    - Link the published repository in the issue
    - Please add all files (`Vagrantfile` etc.) that you have used to set up this box.
- Create own [Docker base image ](https://docs.docker.com/develop/develop-images/baseimages/)

## Resources

- Vagrant docs
- VirtualBox docs
- [preCICE Vagrant box](https://github.com/precice/vm)

1. [ ] Build a VirtualBox VM managed by Vagrand
2. [ ] Build a Docker image containing some tooling for C++ and Python
  - Has to be able to run some non-common dependency?! Maybe install preCICE in there.
      - If preCICE, one could install it once from source and once as binary.
  - Automatically test this via some GitHub action.
     - Check for correct base image.
     - Build the image.
     - Check that code runs.
3. [ ] Install Singularity (optional?)
  - Compile by hand
     - Install Go
     - Compile Singularity
  - Install tooling as

- Use tags to run corrent runners?


## Optional tasks

- Set up the SSH server on your Ubuntu VM and connect to the Guest from the Host.
-

## Deadline

Please finish your work before 18 November 2021 at 9:00.