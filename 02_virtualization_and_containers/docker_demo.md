# Docker Demo

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
- Start container (with name `tutorial`) `docker run --rm -i -t --name tutorial ubuntu    /bin/bash`
- Leave it `CTRL-P-Q` (all keys pressed at the same time)
- Show container running `docker ps`
- Reattach to container `docker container attach tutorial`
- After quitting again, show `docker ps -a`

## Restarting a stopped container

```shell
docker ps -a
docker container start tutorial
docker container attach tutorial
```

## Files in containers

- We can change files inside the container.
    - `docker run -i -t ubuntu /bin/bash`
    - `touch asdf`
    - leave container
    - enter container `docker run -i -t ubuntu /bin/bash`
    - File is not present because we implicitly created a new container based on the same image.

## Bind Mount

- `docker run -i -t --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
    - Create detached container and bind mount
    - Mounts current directory on Host to `/mnt/share`.
    - Bind mount your source code for development for example
    - I do not need `/bin/bash` because that is the default command for the `ubuntu` image.

## Demo: Building own example

- `cd dockerfile-example`
- Contains Dockerfile

```Dockerfile
FROM ubuntu:24.04

RUN apt-get update -y && apt install -y neofetch
WORKDIR /app
COPY testfile .
CMD ["neofetch"]
```

- `docker buildx build --tag testimage .`
- `docker run -i -t testimage /bin/bash`
- `docker run testimage` will run container and `CMD` will be executed
- Create file `touch testfile`, if not present.
- When going into the container we are in the directory `/app` and the file `testfile` is present.
- Copy files with `docker cp`. `touch file-to-copy`
- `docker cp file-to-copy CONTAINERNAME:/app`
- `docker cp CONTAINERNAME:/app file-to-copy`
- This will preserve user and group id
- `docker run -i -t -v $(pwd):/app testimage /bin/bash` starts container, creates volume `/app` and sets working directory to /app

