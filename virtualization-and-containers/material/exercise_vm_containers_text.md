# Working with Virtualization and Containers

**This exercise sheet is work in progress**

In this exercise we will work the virtualization and container techniques that we have seen in the lecture. We will set up virtual machines manually first and then automatize the process. Afterwards we will build out own containers.

## Prerequisites

- Installed and working VirtualBox, Vagrant and Docker.
- GitLab account.
- Some available space on your hard drive or a USB drive (about 8 GB to be safe).

## Before You Start

- Whenever `USERNAME` is mentioned in a code block or similar, you have to replace this by your GitLab username. For example, if a task states that you shoud use "[`USERNAME`] Ubuntu Server Installation", then you have to actually use "[`jaustar`] Ubuntu Server Installation" in case `jaustar` is the username.
## Virtual Machines Using VirtualBox

In part of the

We will install "Ubuntu Server 20.04" a lightweight version of Ubuntu without graphical user interface. However, the ISO image has still 1.2 GB so you might want to start the [download of the image called "Ubuntu Server 20.04.3 LTS"](https://ubuntu.com/download/server) before continuing reading. If you see the name "Focal Fossa" some places, this is the codename of the 20.04 release of Ubuntu.

### Tasks (VirtualBox)

- Download the ISO image from the [Ubuntu homepage](https://ubuntu.com/download/server. Please choose the "20.04.3 LTS" image which is called "ubuntu-20.04.3-live-server-amd64.iso"
- While the image is being downloaded, you can start preparing the VM already. Create a new VM in VirtualBox called "Ubuntu Server" and assign 2048 MB of memory to it. If that is not possible on your machine, choose a larger or smaller amount of memory. Make sure the your virtual hard drive is large enough. 6 GB should be enough for this exercise. If you choose "dynamic allocation" the actual image size should not grow beyond 4 GB during this exercise. So it you are very limited on disk space you could also try a smaller disk size than 6 GB.
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
  - Install `neofetch` via `sudo apt update && sudo apt install -y neofetch`. This command will download and install `neofetch`.
  - Clear the terminal using `clear` and run neofetch via by typing`neofetch` into the terminal and pressing `Enter`.
  - Take a screenshot via VirtualBox. At the top of the VirtualBox window you find the menu item `View`. There you find the option `Take Screenshot (Host+E)`. Save the Screenshot as `neofetch-screenshot-USERNAME.png` (replace `USERNAME` by your username).
- Now we want to open an issue on the GitLab  Repository [TODO: "Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/sse-test-group/exercise-virtual-machines) and upload the screenshot to document your success.
  - Open an issue in the GitHub Repository TODO.
    - As title choose "[`USERNAME`] Ubuntu Server Installation"
    - Attach the screenshot ('Attach a file`). By default, the screenshot is saved in the folder of your VM.
    - Add the `VirtualBox` Label to the issue and assign the issue to the lecturers `jaustar` and `uekermbn` and create the issue.
    - Double-check that your issue looks as expected. You will find an example issue in the GitLab Repository.

Congratulations. You have successfully set up a virtual machine, installed Ubuntu and installed additional software. You are now done with this part of the exercise. If you do not want to play with the VM later nor do you want to do any of the optional assignments, you can poweroff and delete the VM.

### Further Information

- If your mouse pointer gets caught, use the right `CTRL` button on your keyboard to relase it again.
- You can find more information on the installation procedure in the [Ubuntu Server documentation](https://ubuntu.com/server/docs).
- [Ubuntu Server download page](https://ubuntu.com/download/server)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- If you want to set up SSH forwarding to your VM, you can find instructions, for example, [on the codebot homepage](https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup). The instructions are for Ubuntu 18.04, but it also works for Ubuntu 20.04. Note that most of the steps are preconfigured in current VirtualBox releases, but it does not hurt to check whether the settings are set properly.


## Virtual Machines Using Vagrant

In the previous section we have set up a VM manually. This was quite tedious. Therefore, we want to automatize this process now by using [Vagrant](https://www.vagrantup.com/) and setting up our own Vagrant box. We will provision a box based on VirtualBox by using shell scripts and the included provisioning tools of Vagrant.

### Tasks (Vagrant)

- Fork the repository TODO from GitLab and create a branch to work on the fork. It will contain a `README.md` and a file called `bootstrap.sh`.
- We want to start from scratch so initialize a new box using `vagrant init` in a suitable directory. Then adapt your `Vagrantfile` of the box.
  - Your virtual machine should be based on the [`ubuntu/focal64` image](https://www.vagrantup.com/docs/boxes#official-boxes).
  - The name of your VM should be `USERNAME-ubuntu-server`. Replace `USERNAME` with your GitLab username, e.g., `jaustar-ubuntu-server`.
  - The [box version](https://www.vagrantup.com/docs/boxes/versioning) should be `0.1.0`.
  - Run your box with `vagrant up` and make sure that everything works out as expected (`vagrant ssh`). If everything is fine, you can leave the VM and stop it.
  - The VM must request [384 MB of memory](https://www.vagrantup.com/docs/providers/virtualbox/configuration)..
- In the next step we want to provision your virtual machines. That means we want to install additional software and set some additional variables
  - We want to provision (`config.vm.provision`) the box in several steps.
    - Create a new file in the directory where the Vagrantfile resides with the name `testfile` and add it to the repository. The file should contain your GitLab username as text. Add the file to your box using the [file provisioner](https://www.vagrantup.com/docs/provisioning/file) and place it in the home directory of the `vagrant` user.
    - We want an [additional shared folder](https://www.vagrantup.com/docs/synced-folders/basic_usage), besides `/vagrant`, in our virtual machine. The directory where the `Vagrantfile` resides, i.e. '.', should mounted as `/mnt/shared/` in your container.
    - Extend the file called `bootstrap.sh` for provisioning your box. In this script you should do the following:
      - Set the environment variable `ENV_TEST_USERNAME` to have the value of your GitLab username.
      - Install `neofetch`.
      - **Note:** In the `bootstrap.sh` you do not have to prefix commands with `sudo` since the script is executed with superuser rights when Vagrant provisions the box.

      This script should be run by the [shell provisioner](https://www.vagrantup.com/docs/provisioning/shell).
- Open a merge request in the GitHub Repository [TODO: "Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/sse-test-group/exercise-virtual-machines).
  - As title choose "[`USERNAME`] Vagrant Box Provisioning"
  - Make sure all files are up to date (`testfile`, `bootstrap.sh`, `Vagrantfile`)
    - Add the label `Vagrant` label to the issue and assign the issue to the lecturers `jaustar` and `uekermbn`.
  - Double-check that all files are in the repository and up to date. Check everything carefully since a CI pipeline will try to build your Vagrant recipe.
  - If everything looks good, create the issue..
- Check whether the CI pipeline could verify your submission. This may take some time due to the number of concurrent submission being limited. If read the error message carefully and fix your submission by creating a new commit.


### Further Information (Vagrant)

- You might want to add the option `--provision` to the `vagrant up` command if you want to rebuild a box. In case the box is not being build/rebuild, please read the [documentation about provisioning](https://www.vagrantup.com/docs/provisioning) carefully.
- By default, Vagrant will install all files in your home directory. If Vagrant should use a different directory, you can set the environment variable `VAGRANT_HOME` to point the alternative directory. This could look like this:

  ```bash
  export VAGRANT_HOME=/media/jaustar/external-ssd/virtualmachines/vagrant/.vagrant.d/
  ```

  You might want to add this line to your `.bashrc` to make this change persistent.
- [Vagrant Homepage](https://www.vagrantup.com/)
- [Vagrant Introduction](https://www.vagrantup.com/intro)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)

## Containers Using Docker

Similar to the previous task we want to set up a Docker container for testing. I should basically contain the same functionality as the Vagrant box.

### Tasks (Docker)

- Fork the repository TODO from GitLab and create a branch to work on the fork. It will contain a `README.md` and a file called `Dockerfile`.
- We start from scratch. Thus the [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is empty. Edit it to contain the following features
  - Your virtual machine should be based on the [`ubuntu:20.04` image](https://hub.docker.com/_/ubuntu).
  - Create a new file with the name `testfile` and add it to the repository. The file should contain your GitLab username as text. Add the file to your container and place it in directory `/testfiles`.
  - Set the environment variable `ENV_TEST_USERNAME` to have the value of your GitLab username.
  - Make sure that the default command to be executed when running the container is `/bin/bash`.
  - Install `neofetch`.
  - **Note:** In the `Dockerfile` you do not have to prefix commands with `sudo` since the script is executed with superuser rights.
- Open a merge request in the GitHub Repository [TODO: "Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/sse-test-group/exercise-containers).
  - As title choose "[`USERNAME`] Docker Container Recipe"
  - Make sure all files are up to date (`testfile`, `Dockerfile`)
    - Add the label `Docker` label to the issue and assign the issue to the lecturers `jaustar` and `uekermbn`.
  - Double-check that all files are in the repository and up to date. Check everything carefully since a CI pipeline will try to build your Docker recipe.
  - If everything looks good, create the issue..
- Check whether the CI pipeline could verify your submission. This may take some time due to the number of concurrent submission being limited. If read the error message carefully and fix your submission by creating a new commit.


### Further Information (Docker)

- [Dockerfile documentation](https://docs.docker.com/engine/reference/builder/)
- [Docker](https://www.docker.com/)
- [Docker documentation](https://docs.docker.com)
- [DockerHub](https://hub.docker.com/)
- [DockerHub documentation](https://docs.docker.com/docker-hub/)


## Optional Tasks

Here are some ideas on how to extend your work. If you have more ideas, please explain them in your issue/pull request.

### VirtualBox

- Set up the SSH server on your Ubuntu VM and connect to the Guest from the Host. Take a screenshot when connected to your Guest system and add it to the issue.
- Install the Guest Additions

### Vagrant

- Use Vagrant to set up a box with Docker
- Publish a Vagrant box to Vagrant cloud. Please link to it in the issue.
  - Link the published repository in the issue
  - Please add all files (`Vagrantfile` etc.) that you have used to set up this box.

### Docker

- Publish a [Docker base image](https://docs.docker.com/develop/develop-images/baseimages/) to DockerHub.
  - Link the published DockerHub repository in the issue.
  - Please add all files (`Dockerfile` etc.) that you have used to set up this container.

### Singularity

- Rebuild the Docker container as Singularity container. Create a new merge request for this in the GitLab repository [TODO: "Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/sse-test-group/exercise-containers). Please choose the `Singularity` label when creating the merge request.

## Deadline

Please finish the mandatory parts of the work before **18 November 2021 at 9:00**.
