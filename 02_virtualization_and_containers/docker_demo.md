# Docker quiz

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

## Demo: Run existing container

- Start VM with docker

    ```
    cd /media/jaustar/external-ssd/virtualmachines/vagrant/sse-docker-box/
    vagrant up
    ```

- Show containers on [DockerHub](https://hub.docker.com/)

## Some Management Commands

- Show running containers `docker container ls`
- Show all containers `docker container ls -a`
- Show images `docker images`
- Potentially remove some image/container `docker image rm NAME` or `docker container rm NAME/ID`

## Tutorial Case

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

## Files in containers

- We can change files inside the container.
    - `docker run -i -t ubuntu /bin/bash`
    - `touch asdf`
    - leave container
    - enter container `docker run -i -t ubuntu /bin/bash`
    - File is not present because we implicitly created a new container based on the same image.

## Detached Containers

- `docker run -d -i -t --name test --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
    - Create detached container and bind mount
    - Will run cotnainer in detached mode, names it `test` and mounts current directory on Host to `/mnt/share`. Is based on `ubuntu` image.
    - Bind mount your source code for development for example
    - I do not need `/bin/bash` because that is the default command for the `ubuntu` image.

## Restarting a stopped container with arbitrary command

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

## Demo: Building own example

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

## Demo: DuMuX Dockerfile

- Show more complicated Dockerfile example (`dumux-precice`)?
    - `~/container-recipes/docker/dumux-precice/ub2004/dumux-3.4-precice-2.2.1`. Also in branch of [`dumux-precice` repository](https://git.iws.uni-stuttgart.de/dumux-appl/dumux-precice/-/blob/add-docker-images/docker/dumux-3.4-precice-2.2.1.dockerfile)+
    - Uses most/all commands on slides

## Demo: FEniCS example

`docker run -ti -p 127.0.0.1:8000:8000 -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current`

- `-v` creates a volume in the container and mounts the current directory on Host to path `/home/fenics/shared` inside the container
- `-w` sets the working directory to /home/fenics/shared
- Volume allows for persistent data
