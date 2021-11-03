# Virtualization and containers

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

## Introduction to virtualization

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

## VirtualBox

| Duration | Format |
| --- | --- |
| 35 minutes | Slides + Demo |

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
- Boot up some virtual machine.
- Show/install extensions to allow for
  - Some 3D rendering
  - Shared clipboard
  - In general: *Better integration* into host system
- Create a shared drive to exchange data instead of copy and pasting file content.
  - In case one cannot access it `sudo usermod -aG vboxsf $(whoami)`
  - You need to logout and in again afterwards for usergroups to be recognized
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

## Vagrant + demo

| Duration | Format |
| --- | --- |
| 25 minutes | Slides + Demo|

- Initially deveoped by Mitchell Hashimoto as side project
- Released in 2010
- Now developed by Hashimoto's company HashiCorp
  - HashiCorp develops a variety of open-source tools for DevOps and cloud computing. In general for large scale projects.
- Configure VMs (I think also containers nowadays) conveniently via text files
- Infrastructure as code (Git lecture: If you cannot use `diff`, it is the wrong format!)

### Vagrant practical example

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
- `vagrant suspend`Suspends VM
- `vagrant halt`Shuts VM down, keeping changes in the VM

- Exchanging files
  - Check output `default: Mounting shared folders...`
  - Default: Directory containing `Vagrantfile` is mounted as  `/vagrant`
  - Can configure more drives
  - Show example by creating file from Vagrant session

- Vagrant examples
  - Own stuff
    - [Own box online](https://app.vagrantup.com/ajaust/boxes/sse-first-steps/versions/0.1.0)
    - Create box with `vagrant init
  - preCICE
    - Comes with a GUI
    - Preconfigured

## Introduction to containers

| Duration | Format |
| --- | --- |
| 10 minutes | Slides |

- What are the differences between VMs and containers?
  - Containers
    - Low(er) overhead than virtual machines.
    - Container operates in "fenced off" part of the operating system (`cgroups`).
    - Container runs kernel of the host OS.
    - Operating system (OS) needs to be compatible with underlying OS. Cannot run different OS than host. (TODO: Verify this)
      - **Note**: Windows 10 can run Linux containers! (Due to Windows Subsystem for Linux?!)
- Shortly recap what we have learned about containers.
  - Fenced-off, relies on capabilities of OS etc.
- LXD/LXC and its container registry [Linux containers](https://linuxcontainers.org/)
- Short and incomplete overview over container technologies: Docker, Singularity, lxc/lxd, podman...

**Note**: Students not running Linux or without sufficient rights on their machine should be able to use a virtual machine to run Docker/Singularity on their machine if they could get that installed.


## Docker + Demos

| Duration | Format |
| --- | --- |
| 50 minutes | Slides + Demos|

- Quiz "What is Docker?"
  - Answer depends on when in time and  you ask.
    - Containerization framework, container management, company...

### Components

Source: [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)

- The most popular container framework one finds at the moment
- Short backstory:
  - Started as wrapper around lxc/lxd (Linux' native container format)
- Docker, Docker Engine, Docker Compose, Docker Hub? What is going on?
- Server-client layout
- Quite strong encapsulation from Host (**TODO**: Check for file exchange, networking etc.)
- Common commands:
  - TODO
- Explain text-based format (infrastructure as code)
- One can pre-build own images to reuse them later.
- Has a layer based build process (which is nice).
- Images can be shared via DockerHub
- Building an image can be pain in the neck as it depends on a fast internet connection.
- Installation issue/security risks: Docker user group is basically root
  - Rootless installation of Docker
- We focus on tools to create, run and interact with containers

### Demo: Run existing container

- Start VM with docker

  ```
  cd /media/jaustar/external-ssd/virtualmachines/vagrant/sse-docker-box/
  vagrant up
  ```

- Show containers on [DockerHub](https://hub.docker.com/)

- From tutorial `docker run -i -t ubuntu /bin/bash`
  - This pulls the latest `ubuntu` image `docker pull ubuntu`
  - Creates container `docker container create`
  - Creates read-write filesystem (last layer)
  - Creates network interface
  - Starts container and runs `/bin/bash`
  - `-i` means interactive
  - `-t` allocates pseudo-tty

- Changes inside the container are not persistent
  - `touch asdf`
  - leave container
  - enter container `docker run -i -t ubuntu /bin/bash`
  - File is gone
- When container is running, we see it when calling `docker ps`
- After quitting againg show `docker ps -a`

- `docker run -d -i -t --name test --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
  - Create detached container and bind mount
  - Will run cotnainer in detached mode, names it `test` and mounts current directory on Host to `/mnt/share`. Is based on `ubuntu` image.
  - Bind mount your source code for development for example
- Leave a container without closing it via `CTRL+P` followed by `CTRL+Q`


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
- `docker run -d -i -t --name testimage3 testimage /bin/bash` keeps container alive
- Show more complicated Dockerfile example (`dumux-precice`)
  - `~/container-recipes/docker/dumux-precice/ub2004/dumux-3.4-precice-2.2.1`
  - TODO: Add Dockerfile to `dumux-precice` repository
- When going into the container we are in the directory `/app` and the file `testfile` is present

- Copy files with `docker cp`
- `docker cp file-to-copy CONTAINERNAME:/app`
- `docker cp CONTAINERNAME:/app file-to-copy`
- This will fix preserve user and group id

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

- Go to `/media/jaustar/external-ssd/singularity/singularity-examples/build-image`
- Show file `singularity-example.def` content
- `sudo singularity build testimage singularity-example.def`
  - Point out that sudo is needed
- Creates image

## Concluding remarks

| Duration | Format |
| --- | --- |
| 5 minutes | Slides |

- Docker is popular for encapsulating environments for testing (CI/CD, DevOps) as we will see later.
- Singularity is a bit more "niche", but important in the computing/simulation business.
- For the exercise you should ideally have Docker, VirtualBox, Vagrant (maybe Singularity installed)

## Further reading

### Other

- Stackoverflow discussion between creator of Docker and Vagrant on Stackoverflow: ["Should I use Vagrant or Docker for creating an isolated environment?"](https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-for-creating-an-isolated-environment)

### References

- [Docker documentation](https://docs.docker.com/)
- [Singularity documentation](https://sylabs.io/docs/)

### Virtualization tools

- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

### Containers

- [Docker](https://www.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Singularity](https://sylabs.io/)
- [lxc/lxd](https://linuxcontainers.org/)
- [podman](https://podman.io/)
- [Linux containers](https://linuxcontainers.org/)
- Singularity paper: [Singularity: Scientific containers for mobility of compute](https://doi.org/10.1371/journal.pone.0177459)