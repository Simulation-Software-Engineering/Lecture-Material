# Containers Demo

## Introduction to Containers

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

## Docker quiz

- Quiz "What is Docker?"
    - Start slido quiz
    - Answer depends on when in time and    you ask.
        - Containerization framework, container management, company...

## Introduction to Docker and some practical examples

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
    - `docker logs ID/NAME`
        - Shows log files of container
- Explain text-based format (infrastructure as code)
- One can pre-build own images to reuse them later.
- Has a layer based build process (which is nice). We do not have to rebuild from scratch, if build fails.
- Images can be shared via DockerHub or other registries
- Building an image can be pain in the neck as it depends on a fast internet connection.
- Installation issue/security risks: Docker user group is basically root
    - Rootless installation of Docker
    - Namespaces
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

### Some Management Commands

- Show running containers `docker container ls`
- Show all containers `docker container ls -a`
- Show images `docker images`
- Potentially remove some image/container `docker image rm NAME` or `docker container rm NAME/ID`

### Tutorial Case

- From tutorial `docker run -i -t ubuntu /bin/bash`
    - This pulls the latest `ubuntu` image `docker pull ubuntu`
    - Creates container `docker container create`
    - Creates read-write filesystem (last layer)
    - Creates network interface
    - Starts container and runs `/bin/bash`
    - `-i` means interactive
    - `-t` allocates pseudo-tty
- Note that the container will still be there `docker container list -a` vs. `docker container list -a`
- We can make sure that the container is removed after exiting by the `--rm` options, i.e., `docker run --rm -i -t ubuntu /bin/bash`

- When container is running, we see it when calling `docker ps`
- Start container (with name `tutoral`) `docker run --rm -i -t --name tutorial ubuntu    /bin/bash`
- Leave it `CTRL-P` + `CTRL-Q` (do not let go of `CTRL` while doing this)
- Show container running `docker ps`
- Reattach to container `docker container attach tutorial`
- After quitting againg show `docker ps -a`

### Files in containers

- We can change files inside the container.
    - `docker run -i -t ubuntu /bin/bash`
    - `touch asdf`
    - leave container
    - enter container `docker run -i -t ubuntu /bin/bash`
    - File is not present because we implicitly created a new container based on the same image.

### Detached Containers

- `docker run -d -i -t --name test --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
    - Create detached container and bind mount
    - Will run cotnainer in detached mode, names it `test` and mounts current directory on Host to `/mnt/share`. Is based on `ubuntu` image.
    - Bind mount your source code for development for example
    - I do not need `/bin/bash` because that is the default command for the `ubuntu` image.

### Restarting a stopped container with arbitrary command

- This is currently not possible. The default command or entrypoint is part of the runnable container. One has to create a new container from the stopped container to start it with another command
- See also GitHub issues
    - [docker exec into a stopped container](https://github.com/moby/moby/issues/18078). There is also a workaround mentioned in this issue

        ```basg
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

### Demo: DuMuX Dockerfile

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

### Demo: Build own containers

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
