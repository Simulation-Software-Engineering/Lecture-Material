# Exercise: Virtualization and Containers

In this exercise, we work with the virtualization and container techniques that we have seen in the lecture. We set up a virtual machine manually first and then automatize the process using Vagrant. Afterwards, we build our own container using Docker.

Deadline: **Wednesday, November 13, 2024, 9:00**

## Prerequisites

- Some available space on your hard drive or a USB drive (about 10 GB should be enough).
- If you have a machine without Linux and or without root rights, a virtual box session with Linux installed is also fine.

### Preparatory tasks

- **Note**: All preparatory tasks need to be done before the exercise.
- What to do?
    - Install VirtualBox and Vagrant
    - Install Docker on your machine or in a VM
- Please follow the manuals on the homepage
    - [VirtualBox](https://www.virtualbox.org/)
    - [Vagrant](https://www.vagrantup.com/)
    - [Docker Engine](https://docs.docker.com/engine/)

#### VirtualBox and Vagrant

- Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/).
- Verify that the installation was successful by creating the Vagrant example from the lecture:
    - Navigate to a directory of your choice

        ```bash
        vagrant init bento/ubuntu-24.04
        vagrant up
        ```

    - Go into the VM `vagrant ssh` and verify the content of the `/vagrant` directory.
    - Check in the VirtualBox manager that the VM is active.
    - Leave the SSH session (type `exit` and press `Enter` or use the shortcut `CTRL+D`)
    - Destroy the VM `vagrant destroy`

#### Install Docker

- Install [Docker Engine](https://docs.docker.com/engine/)
    - You can install it on your machine or in a VM
    - Check that your installation successful by running

        ```bash
        docker run hello-world
        ```

    - You might have to prefix a `sudo` command. This depends on your Docker configuration.
    - You should see a message that starts with

        ```bash
        Hello from Docker!
        This message shows that your installation appears to be working correctly
        ```

## Before You Start

- **Important**: Whenever `USERNAME` is mentioned in a code block or similar, you have to replace this with your GitLab username.
- If you run into problems, check out the "Further Information" sections at the bottom of the tasks. These sections contain information about common pitfalls and link to the documentation of the used tools.

## Virtual Machines Using VirtualBox

We will install the minimal (server) version of Ubuntu 24.04 (codename Noble Numbat). This version does not include a graphical environment.

### Tasks (VirtualBox)

This exercise consists of the following main steps:

1. Download the "Ubuntu Server 24.04" installation image.
2. Create a new virtual machine in VirtualBox with (recommended, lower might work as well)
    - 6 GB virtual disk
    - 1024 MB of memory
    - 32 MB video memory
3. Install Ubuntu on the virtual machine with
    - user called `USERNAME` (if your GitLab name is `@musterm`, then `musterm`)
    - (host)name of the machine `USERNAMEvm` (e.g., `mustermvm`)
4. Install the software package `neofetch`.
5. Run `neofetch` in the terminal and take a screenshot
6. Upload the screenshot in a new issue on the SIM GitLab.

In the following subsections you will find additional instructions and explanations. This should help you, especially if you do not have much experience with software installation and Linux.

#### 1. Download the "Ubuntu Server 24.04"

See instruction in the introduction to this section.

#### 2. Creating the Virtual Machine

While the "Ubuntu Server 24.04" installation image is downloading, you can already prepare the virtual machine.

- Create a new VM in VirtualBox called "Ubuntu Server".
    - Assign RAM and virtual drive as stated in the introduction.
- After the creation, the virtual machine shows up in the "VirtualBox Manager". Open the settings of the VM and:
    - inspect the settings of the virtual machine and set the video memory to at least 32 MB.
    - in the same settings, you can also increase the number of CPU cores allocated (not necessary).

#### 2. Ubuntu installation process

This is a summary of the [Ubuntu Server installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-server).

- Start the virtual machine.
- VirtualBox will ask you for an installation medium. Add the installation image you just now downloaded (`.iso` file).
- The VM will boot from the Ubuntu image and will welcome you with a configuration program. Choose your preferred language and then choose "Start Ubuntu Server". It brings you to the installation routine. The starting process might take a short while.
- When the boot process has finished, you will be presented with Ubuntu's installation program. Go through it carefully.
    - Choose your preferred language and keyboard layout. Note that you cannot use your mouse in the menus, instead you have to use your keyboard.
    - For most settings you can accept the default values Ubuntu suggests (mirror, empty proxy, using entire disk with LVM group, storage configuration etc.)
    - After verifying that Ubuntu wants to use the virtual hard drive, confirm formatting of the virtual hard drive ("Confirm destructive action") when asked so.
- When setting up your user, please use your GitLab username, e.g. `musterm`, as username and choose the username + VM, e.g. `mustermvm`, as the server's name. The password you can choose freely, but it cannot be empty. If you do not feel creative, use `sse` as password.
- When you are asked about the SSH Setup, you can decide whether you want to activate the `Install OpenSSH Server` option (using spacebar) or not. If you want to test out the SSH connection to the VM (optional task), you can activate it now. If you do not activate it here, you can still install the OpenSSH server later.
- In the next window, skip all suggested "Featured Server Snaps" to keep the size of the image minimal. It suggests common software used on the Ubuntu Server edition, such as Docker, for example. However, we do not need it here. Confirming your choice will start the installation procedure.
- The installation procedure might take a while since it will also install security updates. You can already start reading on the subsequent sections.
- After the installation has finished confirm the reboot with "Reboot Now".

#### 3. Installation of neofetch

- After (re)booting you will be greeted by the Ubuntu login screen. If it looks like a mess press `CTRL-C` to clear the screen. You might have to wait for a moment and maybe switch in and out of the VM's window for it to be refreshed properly.
- Login using your username and password.
- We want to install [`neofetch`](https://github.com/dylanaraps/neofetch) which prints the system's information to the terminal and take a screenshot of this.
    - Install `neofetch` via `sudo apt update && sudo apt install -y neofetch`. This command will download and install `neofetch` using the package manager [`apt`](https://wiki.debian.org/Apt).

#### 4. Running neofetch and Taking a Screenshot (VirtualBox)

- Clear the terminal using `clear` (or `Ctrl-L`) and run neofetch via by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot via VirtualBox. At the top of the VirtualBox window you find the menu item `View`. There you find the option `Take Screenshot (Host+E)`. Save the screenshot as `neofetch-screenshot-USERNAME.png`.

Congratulations. You have successfully set up a virtual machine, installed Ubuntu and installed additional software. You are now done with this part of the exercise. If you do not want to play with the VM later nor do you want to do any of the optional assignments, you can power-off and delete the VM. Be sure that your screenshot displays the correct information though (correct username, correct hostname etc.) before deleting the VM.

#### 5. Upload the Screenshot to SIM GitLab

- Go to the SIM GitLab Repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-virtual-machines). You will find an example issue. Your issue should look similar in terms of title, labels etc.
- Open the issue.
    - As title choose "[`USERNAME`] Ubuntu Server Installation"
    - Attach the screenshot ("Attach a file") that you made in the previous step. By default, the screenshot is saved in the folder of your VM.
    - Add the `VirtualBox` label to the issue and create the issue.
    - Double-check that your issue looks as expected. You can compare your issue to the example issue in the GitLab Repository.

### Further Information (VirtualBox)

- If your mouse pointer gets caught, use the **right** `CTRL` (`STRG` on German keyboards) key on your keyboard to release it again.
- You can find more information on the installation procedure in the [Ubuntu Server documentation](https://ubuntu.com/server/docs).
- [Ubuntu Server download page](https://ubuntu.com/download/server)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)

## Virtual Machines Using Vagrant

In the previous section we set up a VM manually. This was quite tedious. Therefore, we want to automatize this process now by using [Vagrant](https://www.vagrantup.com/) and setting up our own Vagrant box. We will provision a box based on VirtualBox by using shell scripts and the included provisioning tools of Vagrant.

### Tasks (Vagrant)

This exercise consists of the following main steps:

1. Create a fork of the GitLab repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-virtual-machines)
2. Initialization of the VM
    - Name this virtual machine `USERNAME-ubuntu-server`.
    - Make sure that the virtual machine requests 1024 MB memory.
    - Create a shared/synced directory `/mnt/shared` inside the VM.
    - Test the new VM.
3. Extending the VMs configuration
    - Create a file called `testfile` that contains `USERNAME`. This file should be copied into the home directory of the `vagrant` user during the provisioning process.
    - Edit the `Vagrantfile` such that the `bootstrap.sh` script is run during provisioning. The script should:
        - add a new environment variable `ENV_TEST_VARIABLE` with the value `USERNAME`.
        - install `neofetch`.
4. Run `neofetch` in the terminal and take a screenshot.
5. Create a merge request containing your changes.

In the following subsections you will find additional instructions and explanations.

#### 1. Create a Fork (Vagrant)

Fork and clone the repository mentioned above. The repository initially contains a `README.md` and an empty file called `bootstrap.sh`. Please also create a new branch in your fork to work on the task.

#### 2. Initialization of the VM

- We want to start from scratch so initialize a new box using `vagrant init` inside this repository and add the resulting `Vagrantfile` to Git. Then adapt your `Vagrantfile` to incorporate the following settings:
    - Your virtual machine should be based on the [`bento/ubuntu-24.04` image](https://portal.cloud.hashicorp.com/vagrant/discover/bento/ubuntu-24.04). In case you need a different provider (e.g., `libvirt`), feel free to use another box, but state this in your submission.
    - The name of your VM should be `USERNAME-ubuntu-server`.
    - The VM must request [1024 MB of main memory](https://developer.hashicorp.com/vagrant/docs/providers/virtualbox/configuration).
    - We want a [new shared folder](https://developer.hashicorp.com/vagrant/docs/synced-folders/basic_usage) in our virtual machine. The directory where the `Vagrantfile` resides, i.e. `.`, should be mounted by default as `/mnt/shared/` in your virtual machine.
    - Run your box with `vagrant up` and make sure that everything works out as expected (`vagrant ssh`). If everything is fine, you can `exit` the VM. You do **not** have to stop/destroy the VM for the next step.

#### 3. Extending the VM Configuration

We want to provision (`config.vm.provision`) the box in several steps. You can run the provisioning on the running VM with [`vagrant provision`](https://developer.hashicorp.com/vagrant/docs/cli/provision) or `vagrant up --provision` to check every change you apply to the VM by the provisioning process.

- Create a new file with the name `testfile` and add it to the repository. The file must contain your `USERNAME` as text. Add the file to your box using the [file provisioner](https://developer.hashicorp.com/vagrant/docs/provisioning/file) and place it in the home directory of the `vagrant` user (`${HOME}`).
- Extend the file `bootstrap.sh` for provisioning your box. It should contain commands that you would usually use on the command line like in the VirtualBox task. The script must do the following:
    - Set the environment variable `ENV_TEST_VARIABLE` to have the value of your `USERNAME`. You can achieve this by adding `export ENV_TEST_VARIABLE=USERNAME` to the `.bashrc` file which resides in the home directory of `vagrant` user. You might need to `source` your `.bashrc` to access the variable.
    - Install `neofetch` as you did in the VirtualBox task.
    - **Note:** In the `bootstrap.sh` you do not have to prefix commands with `sudo` since the script is executed with superuser rights when Vagrant provisions the box.
    - The `booststrap.sh` script must be run by the [shell provisioner](https://developer.hashicorp.com/vagrant/docs/provisioning/shell).
- Rebuild your Vagrant box using the provisioning steps. Make sure that the software is installed, all files are present, and the environment variable is set.

#### 4. Running neofetch and Taking a Screenshot (Vagrant)

- Go into your running VM by using the `vagrant ssh` command.
- Clear the terminal using `clear` and run neofetch by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot and save it as `neofetch-screenshot-vagrant-USERNAME.png`.

#### 5. Creating a Merge Request (Vagrant)

- After checking your Vagrant box carefully, please open a merge request in the GitLab repository ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-virtual-machines):
    - As title, choose "[`USERNAME`] Vagrant Box Provisioning".
    - Make sure all files are up to date (`testfile`, `bootstrap.sh`, `Vagrantfile`). Do not add the hidden folder `.vagrant` to Git.
    - Attach the screenshot ("Attach a file") that you made in the previous step.
    - Add the label `Vagrant` label to the issue.
    - Double-check that all files are in the repository and up to date.
    - Double-check that the source (the new branch on your fork) and the target branch (`main` of original repo) of the merge request is correct.
    - If everything looks good, create the merge request.

### Further Information (Vagrant)

- You might want to add the option `--provision` to the `vagrant up` or use `vagrant provision` command if you want to reprovision a running box (without destroying it first). In case the box is not being built/rebuilt, please read the [documentation about provisioning](https://developer.hashicorp.com/vagrant/docs/provisioning).
- By default, Vagrant will store some larger files like the base images/boxes etc. in `${HOME}/.vagrant.d`. If Vagrant should use a different directory, you can set the environment variable `VAGRANT_HOME` to point to the alternative directory. This could look like

    ```bash
    export VAGRANT_HOME=/path/to/vagrant/.vagrant.d/
    ```

- You might want to add this line to your `.bashrc` to make this change persistent. Note that Vagrant will still create a hidden `.vagrant` directory in your working directory. However, the `.vagrant` directory normally does not need much space on your hard drive.
- [Vagrant Homepage](https://www.vagrantup.com/)
- [Vagrant Introduction](https://www.vagrantup.com/intro)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)

### Troubleshooting

If you are using Vagrant on Windows you might run into the following issue/error message:

```powershell
VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component ConsoleWrap, interface IConsole
```

The short version of the solution is given below. The detailed solution is described in this [Stack Overflow thread](https://stackoverflow.com/questions/37955942/vagrant-up-vboxmanage-exe-error-vt-x-is-not-available-verr-vmx-no-vmx-code).

- As admin, run the following command in a PowerShell:

    ```powershell
    bcdedit /set hypervisorlaunchtype off
    ```

- Restart your computer
- After the restart, run the following command as admin a PowerShell:

    ```powershell
    bcdedit /set hypervisorlaunchtype auto
    ```

## Containers Using Docker

Similarly to the previous task, we want to set up a Docker container for testing. It will contain similar functionality as the Vagrant box.

### Tasks (Docker)

This exercise consists of the following main steps:

1. Create a fork of the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-containers).
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

Fork and clone the repository mentioned above. The repository initially contains a `README.md` and an empty file called `Dockerfile`. Please also create a new branch in your fork to work on the task.

#### 2. Setting up the `Dockerfile`

- Currently, the [`Dockerfile`](https://docs.docker.com/reference/dockerfile/) is empty. Edit the file such that a container image with the following properties is built:
    - Your virtual machine should be based on the [`ubuntu:24.04` image](https://hub.docker.com/_/ubuntu).
    - Create a new file with the name `testfile` and add it to the repository. The file should contain your `USERNAME` as text. Add the file to your container and place it in directory `/testfiles`.
    - Set the environment variable `ENV_TEST_VARIABLE` to have the value of your `USERNAME`.
    - Make sure that the default command to be executed when running the container is `/bin/bash`.
    - Install `neofetch`.
    - **Note:** In the `Dockerfile` you do not have to prefix commands such as `apt` with `sudo` since the script is executed with superuser rights.
- Test your Docker container locally. Are all variables set and files available?
    - **Note:** If you rebuild your container often, you might end up with dangling containers. You can remove them (together with any unused images, containers, or objects) with [`docker [image|container|system] prune`)](https://docs.docker.com/engine/reference/commandline/system_prune/) depending on what you want to remove. To delete everything unused: `docker system prune`.

#### 3. Running neofetch and Taking a Screenshot (Docker)

- Go into your running container.
- Clear the terminal using `clear` and run neofetch by typing `neofetch` into the terminal and pressing `Enter`. It will show information about the Ubuntu version, available memory etc.
- Take a screenshot and save it as `neofetch-screenshot-docker-USERNAME.png`.

#### 4. Creating a Merge Request (Docker)

- Open a merge request in the GitHub Repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-containers).
    - As title choose "[`USERNAME`] Docker Container Recipe".
    - Make sure all files are up to date (`testfile`, `Dockerfile`).
    - Attach the screenshot ("Attach a file") that you made in the previous step.
    - Add the label `Docker` label to the merge request.
    - Double-check that all files are in the repository and up to date.
    - If everything looks good, create the merge request.

## Optional Tasks

Here are some ideas on how to extend your work after you have finished the main tasks. If you have more ideas, please explain them in your issue/pull request. You can also discuss them with us during the exercise.

Extensions to the VirtualBox task should be added to the existing VirtualBox issue in ["Exercise Virtual Machines"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/exercise-virtual-machines) by adding a new comment under the original screenshot. For all other extensions, please create a new merge request in the corresponding repository. Please use meaningful titles for new merge requests and prefix them with "[`USERNAME`]" as for the other merge requests.

### VirtualBox

- Set up the SSH server on your Ubuntu VM and connect to the Guest from the Host. Take a screenshot when connected to your Guest system and add it to the issue with a short explanation what you see.
- Install the Guest Additions and created a shared folder. Please also add a screenshot of that in the issue with a short explanation what you see.

### Vagrant

- Use Vagrant to set up a box with Docker.
- Publish a Vagrant box to Vagrant cloud. Please link to it in the issue.
    - Link the published repository in the issue
    - Please add all files (`Vagrantfile` etc.) that you have used to set up this box and shortly describe which commands you have used to do so.

### Docker

- Publish a [Docker base image](https://docs.docker.com/build/building/base-images/) to DockerHub.
    - Link the published DockerHub repository in the issue.
    - Please add all files (`Dockerfile` etc.) that you have used to set up this container and shortly describe which commands you have used to do so.

### Singularity

- Rebuild the Docker container as an [Apptainer container](https://apptainer.org/docs/user/latest/). Create a new merge request for this in the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/exercise-containers). Please choose the `Singularity` label when creating the merge request.
    - **Important:** only add the Singularity recipe to the merge request, and not the container file.
