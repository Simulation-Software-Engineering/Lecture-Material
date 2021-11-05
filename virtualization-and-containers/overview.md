# Virtualization and Containers

| Duration | Format |
| --- | --- |
| 5 minutes | Slides |

- **Learning goals**
  - What is the difference between virtualization and containers?
  - When to use virtual machines and when containers.
  - How to work with virtual machines (VirtualBox) and how to manage these with Vagrant.
  - Building containers with Docker and Singularity.
  - Understand pros and cons of different container technologies.
  - Student can set up their own containers tailored to their requirements.

## Quiz (optional)

- Who is using containers or virtualization technologies?!
- Which tools do you use/know?

## General announcement

- This week focus on virtualization and containers. Exercise for this will be next week.
- VirtualBox (image) can also be used for exercises, especially for containers.

## Introduction to Virtualization

| Duration | Format |
| --- | --- |
| 10 minutes | Slides |

![A sketch of virtual machines](virtualmachine-sketch.png)

![A sketch of containers](container-sketch.png)

- What is virtualization and what is containerization?
  - What problems do they solve? Why do we need them?
- Virtual machines (VWs)
  - Emulating a complete computer.
  - Virtual machine brings the full software stack (kernel, libraries etc.)
  - Has a (type 1/2) hypervisor. Type 1 runs on bare metal while type 2 runs within an operating system. Distinction not always clear.
  - Might need/benefit from virtualization technologies (VT-X)
  - Great flexibility. Can run (normally) any operating system that runs on the virtualized platform.
  - Strict separation from host operating system. (Popular for safety critical tasks: c't banking os, Desinfec't, Remote laptops)
- Focus of lecture will be on Linux and Linux-based containers and VMs.
- Various virtualization and container technologies and tools to manage them. Sometimes separation is a bit vague/complicated and changed over time (lxc/lxd, Docker).
- We discuss tools and use cases that are (more) likely to be encountered in simulation software.

## VirtualBox (including practical examples)

| Duration | Format |
| --- | --- |
| 40 minutes | Slides + Demo |

- You can have root rights inside your virtual machine.
- What problems does it solve?
  - You want to run a different operating system within your current one. Example: I am on Linux, but want to use Microsoft Office and other stuff (without using WINE/Proton).
  - You want to run services in an encapsulated way. Want to run than one server on one physical machine. (Proxmox, KVM)
- Hypervisors create some overhead.
- Content of a VirtualBox Image
  - Show directory on drive:
    - `NAMEOFVM.vdi`: The virtual hard drive containing the guest os
    - `NAMEOFVM.vbox`: XML containing metadata and configuration information (RAM, network devices...)
    - `NAMEOFVM.vbox-prev`: Backup of previous settings
    - `Logs/`: Directory containing log files
    - `Snapshots/`: Snapshots of image
- Short question: What type of hypervisor is VirtualBox? Type 2


### VirtualBox demo

- Discuss configuration:
  - Virtual machine will reserve cores/threads of your CPU and main memory.
- Maybe go through installation process to show that it is the same as installing an OS on your normal computer.
- Create a new virtual machine and boot it up (nothing will happen).
- Boot up some configured virtual machine (Ubuntu).
- Creating a new virtual machine
  - Click on `new`
  - I use `expert mode` to set disk location, size and memory. Note, that one can change that also later on.
  - After clicking on `Create` a menu to create the `Virtual Hard Disk` opens.
    - One can choose between fixed size and dynamically allocated (i.e. the drive grows). I personally recommend avoiding dynamically allocated without upper limit.
  - Creates empty machine. Will not do much as we do not have any OS installed. VirtualBox will prompt to mount an image (iso).
  - Show system settings of VM.
  - Storage -> Controller (Mount drive here) and boot again. -> Installation will start up.
    - Normally should unmount image after installation.
  - Install "VirtualBox Guest Additions". Might have to download the image.
    - Devices `Insert Guest Additions CD image"

    ```bash
    sudo mkdir -p /media/cdrom
    sudo mount /dev/cdrom /media/cdrom
    cd /media/cdrom
    sudo apt-get install -y perl dkms build-essential linux-headers-generic linux-headers-$(uname -r)
    sudo su
    ./VBoxLinuxAdditions.run
    ```

    - Will enable clipboard sharing etc
    - Alternative on Ubuntu

    ```bash
    sudo apt install virtualbox-guest-dkms virtualbox-guest-x11 virtualbox-guest-utils
    ```

    - `virtualbox-guest-x11` can be dropped on headless system
  - VM will capture mouse pointer. Use `Right-CTRL` to "free" pointer again.
  - Create snapshots on image overview (Burger symbol on the right)
    - Load snapshots for different configuration stages
  - Configure network for ssh
    - Install `openssh-server`
    - Shutdown VM
    - In VirtualBox window -> File -> Host Network Manager -> Verify that network device is configured `vboxnet0`
    - In virtual machine's settings -> Network -> Adapter 2 -> Enable and set Host only adapter `vboxnet0`
    - Boot VM
    - Verify additional network device `enp0s8` and check for ip address. In my case `192.168.56.101`
    - On host machine `ssh vmuser@192.168.56.101`
- Show/install extensions to allow for
  - Some 3D rendering
  - Shared clipboard
  - In general: *Better integration* into host system
- Create a shared drive to exchange data instead of copy and pasting file content.
  - In case one cannot access it `sudo usermod -aG vboxsf $(whoami)`
  - You need to logout and in again afterwards for usergroups to be recognized.
  - I share `/media/jaustar/external-ssd/virtualmachines/shared-folder`
  - Add some file there and check that it appears Host and vice versa.

## Vagrant (including practical examples)

| Duration | Format |
| --- | --- |
| 25 minutes | Slides + Demo|

- Initially deveoped by Mitchell Hashimoto as side project
- Released in 2010
- Now developed by Hashimoto's company HashiCorp
  - HashiCorp develops a variety of open-source tools for DevOps and cloud computing. In general for large scale projects.
- Configure VMs (I think also containers nowadays) conveniently via text files
- Infrastructure as code (Git lecture: If you cannot use `diff`, it is the wrong format!)
- Standard user and all passwords are `vagrant`

### Demo: Premade Vagrant VM

Tutorial case in `/media/jaustar/external-ssd/virtualmachines/vagrant/tutorial`

- `vagrant init hashicorp/bionic64` Initialize repository
- `vagrant up` Creates `Vagrantfile`. This file can be put in version control.
- Download and set up VM.
- Will also start VM
- Open VirtualBox to see a VM running. We can open the box there, but are prompted for login username and password.
- Note: The actual "box" is put under your home directory
- `vagrant ssh` Connect to running VM
- See different username/hostname
- Different Ubuntu (18.04)
- `vagrant destroy` Will destroy (delete) current VM
- Alternatives:
- `vagrant suspend` Suspends VM
- `vagrant halt` Shuts VM down, keeping changes in the VM
- `vagrant status` Shows status of currently running VMs

- Exchanging files
  - Check output `default: Mounting shared folders...`
  - Default: Directory containing `Vagrantfile` is mounted as  `/vagrant`
  - Can configure more drives
  - Show example by creating file from Vagrant session

### Demo: Own box

- [Own box online](https://app.vagrantup.com/ajaust/boxes/sse-first-steps/versions/0.1.0)
- Go to template `cd /media/jaustar/external-ssd/virtualmachines/vagrant/own-box-template`
- Open `Vagrantfile` and refer to name of VM

  ```ruby
  Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.provision :shell, path: "bootstrap.sh"

    config.vm.provider "virtualbox" do |vb|
      vb.name = "sse-first-step"
    end
  end
  ```

- Open `bootstrap.sh` to show that it will do

  ```bash
  !/usr/bin/env bash

  apt-get update
  apt-get install -y neofetch vim
  echo "export TEST_ENV_VAR=\"Hello SSE\"" >> .bashrc
  ```

  - Installs software and sets `TEST_ENV_VAR`
- `vagrant up`: Create VM
  - Image should be prebuilt
- `vagrant ssh`
  - Call `neofetch`
  - `echo $TEST_ENV_VAR` to show that variable is actually set.
- `vagrant package --base "sse-first-step" --output sse-first-step.box`: Export VM
  - File has ben upladed already
- `sse-first-steps.box` can be uploaded to [Vagrant Cloud](https://app.vagrantup.com)
- Go to directory `using-own-box/`
  - Show `Vagrantfile` that is has my uploaded image as base image
  - Skip building box `vagrant up` as it takes too long, should be prebuilt
  - `vagrant box list` shoud show my box in overview.
  - **Note** My uploaded box is called `ajaust/sse-first-step`**s**
  - **Note** The box seems to be broken all of a sudden.

### Demo: preCICE VM

- Show repository:
  - [https://github.com/precice/vm](https://github.com/precice/vm)
- Run [Premade box](https://app.vagrantup.com/precice/boxes/precice-vm)
  - `cd /media/jaustar/external-ssd/virtualmachines/vagrant/precice`
  - Create box with `vagrant init` (Done before lecture as it takes to long)
  - Start box `vagrant up`
  - Comes with a GUI
  - Preconfigured
  - Destroy in the end `vagrant destroy` since it is large (?)
- If time allows, show preCICE example
  - [Tutorial](https://precice.org/installation-vm.html#how-to-use-this)
  - [Quickstart](https://precice.org/quickstart.html)
    - Open two terminals
    - Go to `/home/vagrant/Desktop/tutorials/quickstart`
    - In one terminal go to `cpp-solid` and build solver `cmake . && make`
      - Afterwards start simulation with `./run.sh`
    - In other terminal go to `fluid-openfoam`
      - Afterwards start simulation with `./run.sh`
    - Watch simulation running

## Introduction to Containers

| Duration | Format |
| --- | --- |
| 10 minutes | Slides |

- What are the differences between VMs and containers?
  - Containers
    - Low(er) overhead than virtual machines.
    - Container operates in "fenced off" part of the operating system (`cgroups`).
    - Container runs kernel of the host OS -> Does **not** run its own OS in.
    - Operating system (OS) needs to be compatible with underlying OS. Cannot run different OS than host. (TODO: Verify this)
      - **Note**: Windows 10 can run Linux containers! (Due to Windows Subsystem for Linux?!)
    - A process for which (and its childs) special rules apply.
- Shortly recap what we have learned about containers.
  - Fenced-off, relies on capabilities of OS etc.
- LXD/LXC and its container registry [Linux containers](https://linuxcontainers.org/)
- Short and incomplete overview over container technologies: Docker, Singularity, lxc/lxd, podman...


**Note**: Students not running Linux or without sufficient rights on their machine should be able to use a virtual machine to run Docker/Singularity on their machine if they could get that installed.

## Docker Quiz

| Duration | Format |
| --- | --- |
| 5 minutes | Quiz |

- Quiz "What is Docker?"
  - Start slido quiz
  - Answer depends on when in time and  you ask.
    - Containerization framework, container management, company...

## Docker (including practical examples)

| Duration | Format |
| --- | --- |
| 60 minutes | Slides + Demos|

- [`act`](https://github.com/nektos/act) is a tool to debug/run GitHub actions locally
- The most popular container framework one finds at the moment
- Short backstory:
  - Started as wrapper around lxc/lxd (Linux' native container format)
- Docker, Docker Engine, Docker Compose, Docker Hub? What is going on?
- Server-client layout
- Quite strong encapsulation from Host (**TODO**: Check for file exchange, networking etc.)
- **Generally useful commands** (see slides as well)
  - `docker run OPTIONS`
    - Run a container
  - `docker image ls`
    - List locally available images
  - `docker pull NAME:TAG`
    - Pulls an image from registry, `TAG` optional
  - `docker container create IMAGE`
    - Create container from image
  - `docker container ls`
    - List running containers
    - Add `-a` to see all containers
  - `docker container start/stop NAME`
    - Start/stop container
  - `docker container attach NAME`
    - Attach to running container
  - `docker build`
    - Creates an image from a given Dockerfile
  - `docker cp`
    - Copy files in/out of container
  - `docker image history IMAGE`
    - Show layers of image (including commands)Vagrant
  - `docker system prune`
    - Remove all unused objects (images, containers...)
- **Note**
- Explain text-based format (infrastructure as code)
- One can pre-build own images to reuse them later.
- Has a layer based build process (which is nice). We do not have to rebuild from scratch, if build fails.
- Images can be shared via DockerHub or other registries
- Building an image can be pain in the neck as it depends on a fast internet connection.
- Installation issue/security risks: Docker user group is basically root
  - Rootless installation of Docker
  - Namespces
  - Docker considers itself quite safe
- We focus on tools to create, run and interact with containers

Source: [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)

### Demo: Run existing container

- Start VM with docker

  ```
  cd /media/jaustar/external-ssd/virtualmachines/vagrant/sse-docker-box/
  vagrant up
  ```

- Show containers on [DockerHub](https://hub.docker.com/)

#### Some Management Commands

- Show running containers `docker container ls`
- Show all containers `docker container ls -a`
- Show images `docker images`
- Potentially remove some image/container `docker image rm NAME` or `docker container rm NAME/ID`

#### Tutorial Case

- From tutorial `docker run -i -t ubuntu /bin/bash`
  - This pulls the latest `ubuntu` image `docker pull ubuntu`
  - Creates container `docker container create`
  - Creates read-write filesystem (last layer)
  - Creates network interface
  - Starts container and runs `/bin/bash`
  - `-i` means interactive
  - `-t` allocates pseudo-tty

- When container is running, we see it when calling `docker ps`
- Start container (with name `tutoral`) `docker run -i -t --name tutorial ubuntu  /bin/bash`
- Leave it `CTRL-P` + `CTRL-Q` (do not let go of `CTRL` while doing this)
- Show container running `docker ps`
- Reattach to container `docker container attach tutorial`
- After quitting againg show `docker ps -a`

#### Files in containers

- We can change files inside the container.
  - `docker run -i -t ubuntu /bin/bash`
  - `touch asdf`
  - leave container
  - enter container `docker run -i -t ubuntu /bin/bash`
  - File is not present because we implicitly created a new container based on the same image.

#### Detached Containers

- `docker run -d -i -t --name test --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
  - Create detached container and bind mount
  - Will run cotnainer in detached mode, names it `test` and mounts current directory on Host to `/mnt/share`. Is based on `ubuntu` image.
  - Bind mount your source code for development for example

#### Restarting a stopped container with arbitrary command

- This is currently not possible. The default command or entrypoint is part of the runnable container. One has to create a new container from the stopped container to start it with another command
- See also GitHub issues
  - [docker exec into a stopped container](https://github.com/moby/moby/issues/18078). There is also a workaround mentioned in this issue

    ```
    docker commit $STOPPED_CONTAINER user/test_image
    docker run -ti --entrypoint=sh user/test_image
    ```

    Also interesting quote

    > The main reason why is because containers are supposed to be immutable. You cannot exec into a stopped container because it has be be running first.

  - [`docker exec` in stopped containers](https://github.com/moby/moby/issues/30361)
- See some workaround on [StackOverflow](https://stackoverflow.com/questions/32353055/how-to-start-a-stopped-docker-container-with-a-different-command)
  - Find container id `docker container list -a`
  - Commit stopped container to save its modifed state into a new image `docker commit CONTAINERID USER/IMAGENAME`
  - Start new container with differnt entry point `docker run -ti --entrypoint=sh USER/IMAGENAME` if an entrypoint is specified in the previews image or `docker run -ti USER/IMAGENAME /bin/sh`
  - For details on the difference between entry points (`ENTRYPOINT`) and the default for executing a container (`CMD`) check the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

### Demo: Building own example

- `cd dockerfile-example`
- Contains Dockerfile

  ```Dockerfile
  FROM ubuntu:18.04

  RUN apt update -y && apt install -y neofetch
  WORKDIR /app
  COPY testfile .
  CMD ["echo", "hello"]
  ```

- `docker build --tag testimage .`
- `docker run -i -t testimage /bin/bash`
- `docker run testimage` will run container and `CMD` will be executed
- `docker run -d -i -t --name testimage testimage` will immediately terminate since the container `CMD` is executed.
- `docker run -d -i -t --name testimage testimage /bin/bash` keeps container alive since the terminal session is running inside.
- Create file `touch testfile`, if not present.
- `docker run -i -t --name testimage -v $(pwd):/app -w /app testimage /bin/bash` starts container, creates volume `/app` and sets working directory to /app
- When going into the container we are in the directory `/app` and the file `testfile` is present.
- Copy files with `docker cp`. `touch file-to-copy`
- `docker cp file-to-copy CONTAINERNAME:/app`
- `docker cp CONTAINERNAME:/app file-to-copy`
- This will fix preserve user and group id
- Show more complicated Dockerfile example (`dumux-precice`)?
  - `~/container-recipes/docker/dumux-precice/ub2004/dumux-3.4-precice-2.2.1`. Also in branch of [`dumux-precice` repository](https://git.iws.uni-stuttgart.de/dumux-appl/dumux-precice/-/blob/add-docker-images/docker/dumux-3.4-precice-2.2.1.dockerfile)+
  - Uses most/all commands on slides

### Demo: FEniCS example

`docker run -ti -p 127.0.0.1:8000:8000 -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current`

- `-v` creates a volume in the container and mounts the current directory on Host to path `/home/fenics/shared` inside the container
- `-w` sets the working directory to /home/fenics/shared
- Volume allows for persistent data

## Singularity + Demos

| Duration | Format |
| --- | --- |
| 20 minutes | Slides + Demos|

- Back story
  - Created at Lawrence Berkeley National Laboratory but now developed by SyLabs
  - Based on Go
- Container solution with high-performance computing in mind
  - "Mobility of compute", "Bring your own environment"
    - Mobility of your compute environment
    - Normally immutable images
  - Integration in scheduling systems
  - Runs in *user-space* (no root privilege escalation)
  - Direct network and (some) hardware access (GPUs, accelerators)
  - Mounts common/important directories
  - Show text-based file format. Is similar to Docker
    - Building is without layers (hit or miss)
    - Images can be based on Docker images. This is nice to prebuild parts of the image as Docker image since Singularity's format is not layer based. This means you have to rebuilt from scratch if it fails.
  - Small runtime penalty.
- Nowadays available on many HPC platforms
- Common commands

### Demo: Run prebuilt containers

- `singularity pull library://lolcow`
  - Obtain existing container image and store it as `lolcow_latest.sif`
- `singularity pull lolcow_docker.sif docker://sylabsio/lolcow`
  - Pulls docker image, converts it and stores it as lolcow_docker.sif
- `singularity shell lolcow_latest.sif`
  - Run shell in container
  - `whoami` will show same user as I am on the computer
- `singularity exec lolcow_latest.sif cowsay moo`
  - Run command in container
- Show the mounted filesystems and hardware access.
- Show that we cannot run things as root.
- Note that images are executable by default

#### Demo: Build own containers

- Recipe `singularity-example.def`

  ```Singularity
  BootStrap: library
  From: ubuntu:16.04

  %post
      apt-get -y update
      apt-get -y install fortune cowsay lolcat

  %environment
      export LC_ALL=C
      export PATH=/usr/games:$PATH

  %runscript
      fortune | cowsay | lolcat
  ```

- Go to `/media/jaustar/external-ssd/singularity/singularity-examples/build-image`
- Show file `singularity-example.def` content
- `sudo singularity build testimage singularity-example.def`
  - Point out that sudo is needed
- Creates image which is identical to the prebuilt image

## Concluding Remarks and Discussion about Learning Goals

| Duration | Format |
| --- | --- |
| 5 minutes | Slides |

- Virtual machines are a good abstraction layer that are very flexible. They can run different OS, can be moved etc. VirtualBox is a popular VM solution (hypervisor.)
- There are tools like Vagrant to manage them more conveniently than with the GUI or CLI.
- Containers are a light weight alternative to VMs. They are basically "special" processes that run more or less isolated. Therefore, they do not need to bring everything (kernel, libraries...) themselves, but rely on the functionalities of the Host. Example: Containers "run" on the same kernel as the Host. Cannot mix OSes (easily).
- Docker is popular for container framework encapsulating environments and applications. We will use it also more for testing (CI/CD, DevOps). This will come in future lectures.
- Singularity is a bit more "niche", but important in the computing/simulation business as it focuses on self-contained applications that can easily run on different platforms instead of isolation compared to Docker.
- For the exercise you should ideally have Docker, VirtualBox, Vagrant (maybe Singularity installed).
- Show slides from the intro with learning goals again.
  - Can you answer the questions now?

## Further Reading

### References

- [Docker documentation](https://docs.docker.com/)
- [Singularity documentation](https://sylabs.io/docs/)

### Virtualization tools

- [VirtualBox](https://www.virtualbox.org/)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- [Overview of different disk formats](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)
- [Ubuntu 18.04 virtual machine setup](https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup)
- [Vagrant](https://www.vagrantup.com/)

### Containers

- [Docker](https://www.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Singularity](https://sylabs.io/)
- [Sarus](https://user.cscs.ch/tools/containers/sarus/)
- [lxc/lxd](https://linuxcontainers.org/)
- [podman](https://podman.io/)
- [Linux containers](https://linuxcontainers.org/)
- Singularity paper: [Singularity: Scientific containers for mobility of compute](https://doi.org/10.1371/journal.pone.0177459)

### Other

- ["Should I use Vagrant or Docker for creating an isolated environment?"](https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-for-creating-an-isolated-environment)
- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)
- ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
- [Open Container Initiative (OCI)](https://opencontainers.org/)