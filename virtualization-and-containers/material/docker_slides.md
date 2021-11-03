---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
  font-weight: bold;
    color: orange;
  }
  .reveal p {
    text-align: left;
  }
  .reveal section h1 {
    color: orange;
  }
  .reveal section h2 {
    color: orange;
  }
</style>

# Docker

<img src="https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png" width=20%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

[https://www.docker.com/company/newsroom/media-resources](https://www.docker.com/company/newsroom/media-resources)

---

## What is Docker? 1/2

- Docker, Inc.
  - Company promoting Docker
- Docker Desktop
  > Developer productivity tools and a local Kubernetes environment.
- Docker Engine
  > Docker Engine is an open source containerization technology for building and containerizing your applications.

---

## What is Docker? 2/2

- Docker Hub
  > Cloud-based application registry and development team collaboration services.
- Docker Compose
  > Compose is a tool for defining and running multi-container Docker applications.
- According to documentation
  > Docker is an open platform for developing, shipping, and running applications.
- We use definition from documentation.

---

## Typical Docker Applications

- Applications as Microservices
- Containers for consistent development environment
- Containers for consistent testing environment
- Portable format for sharing applications
- Avoid tedious installation procedures by providing Docker container ([FEniCS](https://fenicsproject.org/download/), [GitLab](https://docs.gitlab.com/ee/install/docker.html)...)

---

## Building Blocks 1/2

- Docker daemon `dockerd`
  - Controlling instance of containers and reacts to API requests
  - Server process
- Docker client
  - User interface/tools to interact with, create, manage containers etc. via daemon
- Docker registries
  - Registries that manage Docker images to be used

---

## Building Blocks 2/2

- Docker objects
  - **Images**
    - Read-only template for creating a container
    - An image can be based on another image
  - **Containers**
    - Runnable instance of an image

---

## Docker Architecture

<img src="https://docs.docker.com/engine/images/architecture.svg" width=80%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

[https://docs.docker.com/engine/images/architecture.svg](https://docs.docker.com/engine/images/architecture.svg)

---

## Connection to Host

- Container communicates via daemon `dockerd` (runs as   root)
- Strong isolation (`namespaces` and `cgroups`)
  - You cannot access Host filesystem by default
  - Several [mount options](https://docs.docker.com/storage) available

---

## Requirements

- Root rights for installation
- `dockerd` runs as root -> Interaction needs root rights
  - Prefix commands with `sudo`
  - Be member of group `docker` (=makes you root), expected by some applications (e.g. `act`)
  - [Attack surface?!](https://docs.docker.com/engine/security/#docker-daemon-attack-surface)
    - [Isolate user namespace](https://docs.docker.com/engine/security/userns-remap/)
    - Use trustworthy containers
- Alternatives:
  - [Rootless mode](https://docs.docker.com/engine/security/rootless/)
  - Run Docker in a VM
- Check [security notes](https://docs.docker.com/engine/security/)

---

## Useful Commands 1/2

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

---

## Useful Commands 2/2

- `docker container start/stop NAME`
  - Start/stop container
- `docker container attach NAME`
  - Attach to running container
- `docker build`
  - Creates an image from a given Dockerfile
- `docker cp`
  - Copy files in/out of container
- `docker image history IMAGE`
  - Show layers of image (including commands)
- `docker system prune`
  - Remove all unused objects (images, containers...)
- Many commands have similar/same outcome

---

## Demo: Running prebuilt images


---

## Defining and Building own Images 1/2

- Define container in `Dockerfile`
  - Git-friendly text file
- Start from base image
  - Find images on repository such as [DockerHub](https://hub.docker.com/)
- Extend image by additional layers
  - Layers are added separately -> Keep number of layers low
  - Layers are cached
  - Changed layer requires downstream layers to be recreated
- Container (layers) have commit hashes

---

## Defining and Building own Images 2/2

- `FROM`: Defines base image
- `RUN`: Defines commands to execute
- `WORKDIR`: Defines working directory for following commands
- `COPY`: Copy for from source to destination
- `ADD`: Add for from source to destination (powerful and confusing)
- `CMD`: Command to run under `docker run`
- `ENV`: Sets environment variable
- `ARG`: Environment variable for **only** build process

---

## Dockerfile Example

```Dockerfile
FROM ubuntu:18.04

RUN apt update -y && apt install -y neofetch
WORKDIR /app
COPY testfile .
CMD ["echo", "hello"]
```

---

## Demo: Building own image

---

## Publish own Images

- Publication on registry (e.g. [DockerHub](https://hub.docker.com/))
- `docker build -t ACCOUNT/REPOSITORY[:TAG] .`
  - Creates image
- `docker push ACCOUNT/REPOSITORY[:TAG]`
  - Push image to registry (default DockerHub)
  - Needs account and must be logged in via `docker login`

---

## Demo: Run FEniCS container

---

## Advanced Topics

- User ID mapping
- [Multistage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
  - Build image by combining layers created from different base images
- [Different mount typs](https://docs.docker.com/storage)
  - Volumes, bind mount, tmpfs mount
- [Persisting data](https://docs.docker.com/get-started/05_persisting_data/)
- [Multi-container apps](https://docs.docker.com/get-started/07_multi_container/)
- And many more. Check out the [Docker documentation](https://docs.docker.com)

---

## Summary and Outlook

- Lightweight virtualization technique
- Run application in isolated environment
- Run application in consistent environment
- Share environments and applications with containers
- Plenty of options and feature-rich CLI
- Important building block for CI/CD pipelines (future lectures)

---

## Further Reading

- [Docker](https://www.docker.com/)
- [Docker documentation](https://docs.docker.com)
- [DockerHub](https://hub.docker.com/)
- [DockerHub documentation](https://docs.docker.com/docker-hub/)
- [Open Container Initiative (OCI)](https://opencontainers.org/)
- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)