# Exercise: Virtualization and Containers

In this exercise we work the virtualization and container techniques that we have seen in the lecture. We set up a virtual machine manually first and then automatize the process using Vagrant. Afterwards we build our own container using Docker.

## Deadline

Please finish the the work before **18 November 2021 at 9:00**.

## Prerequisites

- Working installation of VirtualBox, Vagrant and Docker [as mentioned in the homework](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/virtualization-and-containers/material/homework_slides.md).
- SIM GitLab account.
- Some available space on your hard drive or a USB drive (about 8 GB should be enough).

## Before You Start

- **Important**: Whenever `USERNAME` is mentioned in a code block or similar, you have to replace this by your GitLab username. For example, if a task states that you shoud use "[`USERNAME`] Ubuntu Server Installation", then you have to actually use "[`jaustar`] Ubuntu Server Installation" in case `jaustar` is your username.
- If you are using a MacBook with ARM CPU and Parallels instead of VirtualBox, please mention this in the issues and pull requests that you create during this exercise. Ideally, use the `Parallels` label on GitLab for that.
- If you run into problems, check out the "Further Information" sections at the bottom of the tasks. These sections contain information about common pitfalls and link to the documentation of the used tools.

## Virtual Machines Using VirtualBox

We will install "Ubuntu Server 20.04", a lightweight version of Ubuntu without graphical user interface. However, the ISO image has still 1.2 GB so you might want to start the [download of the image called "Ubuntu Server 20.04.3 LTS"](https://ubuntu.com/download/server) before continuing reading. If you see the name "Focal Fossa" some places, this is the codename of the 20.04 release of Ubuntu.

### Tasks (VirtualBox)

This exercise consists of the following main steps:

1. Download the "Ubuntu Server 20.04" installation image.
2. Create a new virtual machine in VirtualBox with
    - 6 GB virtual disk
    - 2048 MB of memory
    - 32 MB video memory
3. Install Ubuntu on the virtual machine with
    - user called `USERNAME`, e.g., `jaustar`.
    - (host)name of the machine `USERNAMEvm`, e.g., `jaustarvm`.
4. Install the software package `neofetch`.
5. Run `neofetch` in the terminal and take a screenshot
6. Upload the screenshot in a new issue on the SIM GitLab.

In the following subsections you will find additional instructions and explanations. This should help you, especially if you do not have much experience with software installation and Linux.

#### 1. Download the "Ubuntu Server 20.04"

See instruction in the introduction to this section.

#### 2. Creating the Virtual Machine

While the "Ubuntu Server 20.04" installation image is downloading you can already prepare the virtual machine.

- Create a new VM in VirtualBox called "Ubuntu Server".
    - Assign 2048 MB of memory to it. If that is not possible on your machine, choose a larger or smaller amount of memory. Make sure the your virtual hard drive is large enough.
    - A maximum size 6 GB for the virtual hard drive should be enough for this exercise. If you choose "dynamic allocation" the actual image size should not grow beyond 4 GB during this exercise. If you are very limited on disk space you can also try a smaller disk size than 6 GB.
- After the creation the virtual machine shows up in the "VirtualBox Manager" open the settings of the VM and
    - Inspect the settings of the virtual machine and set the video memory to 32 MB.
    - When the Ubuntu installation image finished downloading, mount the `ubuntu-20.04.3-live-server-amd64.iso` to your virtual machine's cdrom drive (Storage -> Controller: IDE -> "Add optical drive").

#### 2. Ubuntu installation process

- Start the virtual machine.
- The VM will boot from the Ubuntu image and will welcome you with a configuration program. Choose your preferred language and then choose "Start Ubuntu Server". It brings you to the installation routine. The starting process might take a short while.
- When the boot process has finished, you will be presented with Ubuntu's installation program. Go through it carefully.
    - Choose your preferred language and keyboard layout. Note that you cannot use your mouse in the menus, instead you have to use your keyboard.
    - For most settings you can accept the default values Ubuntu suggests (mirror, empty proxy, using entire disk with LVM group, storage configuration etc.)
    - After verifying that Ubuntu wants to use the virtual hard drive, confirm formatting of the virtual hard drive ("Confirm destructive action") when asked so.
- When setting up your user, please use your GitLab username, e.g. `jaustar`, as username and choose the username + VM, e.g. `jaustarvm`, as the server's name. The password you can choose freely, but it cannot be empty. If you do not feel creative, use `vm` as password.
- When you are asked about the SSH Setup, you can decide whether you want to activate the `Install OpenSSH Server` option (using spacebar) or not. If you want to test out the SSH connection to the VM (optional task), you can activate it now. If you do not activate it here, you can still install the OpenSSH server later.
- In the next window, skip all suggested "Featured Server Snaps" to keep the size of the image minimal. It suggests common software used on the Ubuntu Server edition, such as Docker, for example. However, we do not need it here. Confirming your choice will start the installation procedure.
- The installation procedure might take a while since it will also install security updates. You can already start reading on the subsequent sections.
- After the installation has finished confirm the reboot with "Reboot Now".
    - Ubuntu should complain that it cannot unmount the cdrom drive. Check in the settings of your VM that VirtualBox has unmounted the `ubuntu-20.04.3-live-server-amd64.iso` image and confirm the reboot by pressing enter. If the image is still mounted, please shutdown the VM (Machine -> ACPI Shutdown), unmount the image manually and boot the VM again.

#### 3. Installation of neofetch

- After (re)booting you will be greeted by the Ubuntu login screen. If it looks like a mess press `CTRL-C` to clear the screen. You might have to wait for a moment and maybe switch in and out of the VM's window for it to be refreshed properly.
- Login using your username and password.
- We want to install [`neofetch`](https://github.com/dylanaraps/neofetch) which prints the system's information to the terminal and take a screenshot of this.
    - Install `neofetch` via `sudo apt update && sudo apt install -y neofetch`. This command will download and install `neofetch` using the package manager [`apt`](https://wiki.debian.org/Apt).

#### 4. Running neofetch and Taking a Screenshot (VirtualBox)

- Clear the terminal using `clear` and run neofetch via by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot via VirtualBox. At the top of the VirtualBox window you find the menu item `View`. There you find the option `Take Screenshot (Host+E)`. Save the screenshot as `neofetch-screenshot-USERNAME.png`.

Congratulations. You have successfully set up a virtual machine, installed Ubuntu and installed additional software. You are now done with this part of the exercise. If you do not want to play with the VM later nor do you want to do any of the optional assignments, you can poweroff and delete the VM. Be sure that your screenshot displays the correct information though (correct username, correct hostname etc.) before deleting the VM.

#### 5. Upload the Screenshot to SIM GitLab

- Go to the SIM GitLab Repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-virtual-machines). You will find an example issue. Your issue should look similar in terms of title, labels etc.
- Open the issue.
    - As title choose "[`USERNAME`] Ubuntu Server Installation"
    - Attach the screenshot ("Attach a file") that you made in the previous step. By default, the screenshot is saved in the folder of your VM.
    - If you did **not** assign 2048 MB of memory to the VM, please mention how much memory you assigned  instead.
    - Add the `VirtualBox` label to the issue and assign the issue to `jaustar`. Finally, create the issue.
    - Double-check that your issue looks as expected. You can compare your issue to the example issue in the GitLab Repository.

### Further Information (VirtualBox)

- If your mouse pointer gets caught, use the **right** `CTRL` (`STRG` on German keyboards) key on your keyboard to release it again.
- You can find more information on the installation procedure in the [Ubuntu Server documentation](https://ubuntu.com/server/docs).
- [Ubuntu Server download page](https://ubuntu.com/download/server)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- If you want to set up SSH forwarding to your VM, you can find instructions, for example, [on the codebot homepage](https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup). The instructions are for Ubuntu 18.04, but it also works for Ubuntu 20.04. Note that most of the steps are preconfigured in current VirtualBox releases, but it does not hurt to check whether the settings are set properly.


## Virtual Machines Using Vagrant

In the previous section we have set up a VM manually. This was quite tedious. Therefore, we want to automatize this process now by using [Vagrant](https://www.vagrantup.com/) and setting up our own Vagrant box. We will provision a box based on VirtualBox by using shell scripts and the included provisioning tools of Vagrant.

### Tasks (Vagrant)

This exercise consists of the following main steps:

1. Create a fork of the GitLab repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-virtual-machines)
2. Initialization of the VM
    - Name this virtual machine `USERNAME-ubuntu-server`.
    - Make sure that the virtual machine requests 1024 MB memory.
    - Create a shared/synced directory `/mnt/shared` inside the VM.
    - Test the new VM.
3. Extending the VMs configuration
    - Create a file called `testfile` that contains `USERNAME`. This file should be copied into the home directory of the `vagrant` user during the provisioning process.
    - Edit the `Vagrantfile` such that the `bootstrap.sh` script is run during provisioning. The script should
        - Add a new environment variable `ENV_TEST_VARIABLE` with the value `USERNAME`.
        - Install `neofetch`.
4. Run `neofetch` in the terminal and take a screenshot
5. Create a merge request containing your changes

In the following subsections you will find additional instructions and explanations.

#### 1. Create a Fork (Vagrant)

See the instructions in the task list above. The repository initially contains a `README.md` and an empty file called `bootstrap.sh`. Please also create a new branch in your fork to work on the task.

#### 2. Initialization of the VM

- We want to start from scratch so initialize a new box using `vagrant init` in inside this repository and add the resulting `Vagrantfile` to Git. Then adapt your `Vagrantfile` to incorporate the following settings:
    - Your virtual machine must be based on the [`ubuntu/focal64` image](https://app.vagrantup.com/ubuntu/boxes/focal64). See [official boxes of Vagrant](https://www.vagrantup.com/docs/boxes#official-boxes).
    - The name of your VM should be `USERNAME-ubuntu-server`.
    - The [box version](https://www.vagrantup.com/docs/boxes/versioning) of your box should be set `0.1.0`.
    - The VM must request [1024 MB of main memory](https://www.vagrantup.com/docs/providers/virtualbox/configuration).
    - We want a [new shared folder](https://www.vagrantup.com/docs/synced-folders/basic_usage) in our virtual machine. The directory where the `Vagrantfile` resides, i.e. `.`, should be mounted as `/mnt/shared/` in your container.
    - Run your box with `vagrant up` and make sure that everything works out as expected (`vagrant ssh`). If everything is fine, you can leave the VM. You do **not** have to stop/destroy the VM for the next step.

#### 3. Extending the VMs Configuration

We want to provision (`config.vm.provision`) the box in several steps. You can run the provisioning on the running VM with [`vagrant provision`](https://www.vagrantup.com/docs/cli/provision) or [`vagrant up --provision`](https://www.vagrantup.com/docs/cli/up#no-provision) to check every change you apply to the VM by the provisioning process.

- Create a new file with the name `testfile` and add it to the repository. The file must contain your `USERNAME` as text. Add the file to your box using the [file provisioner](https://www.vagrantup.com/docs/provisioning/file) and place it in the home directory of the `vagrant` user (`${HOME}`).
- Extend the file `bootstrap.sh` for provisioning your box. It should contain commands that you would usually use on the command line like in the VirtualBox task. The script must do the follwing:
    - Set the environment variable `ENV_TEST_VARIABLE` to have the value of your `USERNAME`. You can achieve this by adding `export ENV_TEST_VARIABLE=USERNAME` to the `.bashrc` file which resides in the home directory of `vagrant` user.
    - Install `neofetch` as you did in the VirtualBox task.
    - **Note:** In the `bootstrap.sh` you do not have to prefix commands with `sudo` since the script is executed with superuser rights when Vagrant provisions the box.

        The `booststrap.sh` script must be run by the [shell provisioner](https://www.vagrantup.com/docs/provisioning/shell).
- Rebuild your Vagrant box using the provisioning steps. Make sure that the software is installed, all files are present and the environment variable is set.

#### 4. Running neofetch and Taking a Screenshot (Vagrant)

- Go into your running VM by using the `vagrant ssh` command.
- Clear the terminal using `clear` and run neofetch via by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot and save it as `neofetch-screenshot-vagrant-USERNAME.png`.

#### 5. Creating a Merge Request (Vagrant)

- After checking your Vagrant box carefully, please open a merge request in the GitHub Repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-virtual-machines):
    - As title, choose "[`USERNAME`] Vagrant Box Provisioning".
    - Make sure all files are up to date (`testfile`, `bootstrap.sh`, `Vagrantfile`). Do not add the hidden folder `.vagrant` to Git.
    - Attach the screenshot ("Attach a file") that you made in the previous step.
    - Add the label `Vagrant` label to the issue and assign the issue to `jaustar`.
    - Double-check that all files are in the repository and up to date.
    - Double-check that the source (the new branch on your fork) and the target branch (`main` of original repo) of the merge request is correct.
    - If everything looks good, create the merge request.

### Further Information (Vagrant)

- You might want to add the option `--provision` to the `vagrant up` or use `vagrant provision` command if you want to reprovision a running box (without destroying it first). In case the box is not being build/rebuild, please read the [documentation about provisioning](https://www.vagrantup.com/docs/provisioning) carefully.
- By default, Vagrant will store some larger files like the base images/boxes etc.\ in `${HOME}/vagrant.d`. If Vagrant should use a different directory, you can set the environment variable `VAGRANT_HOME` to point the alternative directory. This could look like this:

  ```bash
  export VAGRANT_HOME=/media/jaustar/external-ssd/virtualmachines/vagrant/.vagrant.d/
  ```

    You might want to add this line to your `.bashrc` to make this change persistent. Note, that Vagrant will still create a hidden `.vagrant` directory in the your working directory. However, the `.vagrant` directory normally does not need much space on your hard drive.
- [Vagrant Homepage](https://www.vagrantup.com/)
- [Vagrant Introduction](https://www.vagrantup.com/intro)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- If you are using Vagrant on Windows you might run into the following issue/error message:

  ```powershell
  VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component ConsoleWrap, interface IConsole
  ```

    - The short version of the solution is given below. The detailed solution is described in this [Stack Overflow thread](https://stackoverflow.com/questions/37955942/vagrant-up-vboxmanage-exe-error-vt-x-is-not-available-verr-vmx-no-vmx-code).
        1. As admin, run the following command in a PowerShell:

        ```powershell
        bcdedit /set hypervisorlaunchtype off
        ```

        1. Restart your computer
        1. After the restart, run the following command as admin a PowerShell:

        ```powershell
        bcdedit /set hypervisorlaunchtype auto
        ```

## Containers Using Docker

Similar to the previous task we want to set up a Docker container for testing. It will contain similar functionality as the Vagrant box.

### Tasks (Docker)

This exercise consists of the following main steps:

1. Create a fork of the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-containers)
2. Setting up the `Dockerfile`
    - The name of this container will be `USERNAME-ubuntu`.
    - Create a file called `testfile` that contains `USERNAME`. This file should be copied to a directory called `/testfiles` inside the container.
    - Set the environment variable `ENV_TEST_VARIABLE` inside the container.
    - Define a default run command for the container.
    - Install `neofetch` inside the container
    - Test the new container
3. Run `neofetch` in a terminal inside the container and take a screenshot
4. Create a merge request containing your changes.

#### 1. Create a Fork (Docker)

See the instructions in the task list above. The repository initially contains a `README.md` and an empty file called `Dockerfile`. Please also create a new branch in your fork to work on the task.

#### 2. Setting up the `Dockerfile`

- Currently, the [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is empty. Edit the file such that an container image with the following properties is build:
    - Your virtual machine should be based on the [`ubuntu:20.04` image](https://hub.docker.com/_/ubuntu).
    - Create a new file with the name `testfile` and add it to the repository. The file should contain your `USERNAME` as text. Add the file to your container and place it in directory `/testfiles`.
    - Set the environment variable `ENV_TEST_VARIABLE` to have the value of your `USERNAME`.
    - Make sure that the default command to be executed when running the container is `/bin/bash`.
    - Install `neofetch`.
    - **Note:** In the `Dockerfile` you do not have to prefix commands such as `apt` with `sudo` since the script is executed with superuser rights.
- Test your Docker container locally. Are all variables set and files available?
    - **Note:** If you rebuild your container often, you might end up with dangling containers. You can remove them (and unused images, containers, or objects) with [`docker [image|container|system] prune`)](https://docs.docker.com/engine/reference/commandline/system_prune/) depending on what you want to remove.

#### 3. Running neofetch and Taking a Screenshot (Docker)

- Go into your running container.
- Clear the terminal using `clear` and run neofetch via by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot and save it as `neofetch-screenshot-docker-USERNAME.png`.

#### 4. Creating a Merge Request (Docker)

- Open a merge request in the GitHub Repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-containers).
    - As title choose "[`USERNAME`] Docker Container Recipe".
    - Make sure all files are up to date (`testfile`, `Dockerfile`).
    - Attach the screenshot ("Attach a file") that you made in the previous step.
    - Add the label `Docker` label to the merge request and assign the merge request to `jaustar`.
    - Double-check that all files are in the repository and up to date.
    - If everything looks good, create the merge request.

### Further Information (Docker)

- [Dockerfile documentation](https://docs.docker.com/engine/reference/builder/)
- [Docker](https://www.docker.com/)
- [Docker documentation](https://docs.docker.com)
- [DockerHub](https://hub.docker.com/)
- [DockerHub documentation](https://docs.docker.com/docker-hub/)


## Optional Tasks

Here are some ideas on how to extend your work after you have finished the main tasks. If you have more ideas, please explain them in your issue/pull request. You can also discuss them with us during the exercise.

Extensions to the VirtualBox task should be added to the existing VirtualBox issue in ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-virtual-machines) by adding a new comment under the original screenshot. For all other extensions, please create a new merge request in the corresponding repository. Please use a meaningful title for new merge requests and prefix it with "[`USERNAME`]" as for the other merge requests.

### VirtualBox

- Set up the SSH server on your Ubuntu VM and connect to the Guest from the Host. Take a screenshot when connected to your Guest system and add it to the issue with a short explanation what we see.
- Install the Guest Additions and created a shared folder. Please also add a screenshot of that in the issue with a short explanation what we see.

### Vagrant

- Use Vagrant to set up a box with Docker.
- Publish a Vagrant box to Vagrant cloud. Please link to it in the issue.
    - Link the published repository in the issue
    - Please add all files (`Vagrantfile` etc.) that you have used to set up this box and shortly describe which commands you have used to do so.

### Docker

- Publish a [Docker base image](https://docs.docker.com/develop/develop-images/baseimages/) to DockerHub.
    - Link the published DockerHub repository in the issue.
    - Please add all files (`Dockerfile` etc.) that you have used to set up this container and shortly describe which commands you have used to do so.

### Singularity

- Rebuild the Docker container as [Singularity container](https://sylabs.io/guides/master/user-guide/). Create a new merge request for this in the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-containers). Please choose the `Singularity` label when creating the merge request.
    - Please only add the Singularity recipe to the merge request, but not the container file.
