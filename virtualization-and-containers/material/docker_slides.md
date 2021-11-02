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
  - Images
    - Read-only template for creating a container
    - An image can be based on another image
  - Containers
    - Runnable instance of an image

---

## Docker Architecture

<img src="https://docs.docker.com/engine/images/architecture.svg" width=80%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

[https://docs.docker.com/engine/images/architecture.svg](https://docs.docker.com/engine/images/architecture.svg)

---

## Connection to Host

- Strong encapsulation
- Container communicates via daemon `dockerd`
- You cannot access Host filesystem by default
  - Several [mount options](https://docs.docker.com/storage) available

---

## Useful commands 1/2

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

**Note**: Commands take many extra options

---

## Useful commands 2/2

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
- Many commands have similar/same outcome

**Note**: Commands take many extra options

---

## Defining and Building own Images

- Define container in `Dockerfile`
  - Git friendly text file
- Start from base image
  - Find images on repository such as [DockerHub](https://hub.docker.com/)
- Extend image by additional layers
  - Layers are added separately -> Keep number of layers low
  - Layers are cached
  - Changed layer requires downstream layers to be recreated

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

## Demo

- Run an existing container
- Build own image and run it
- Run FEniCS container

---

## Advanced Topics

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
- Important building block for CI/CD pipelines (future lecture)

---

## Further Reading

- [Docker](https://www.docker.com/)
- [Docker documentation](https://docs.docker.com)
- [Docker Hub](https://hub.docker.com/)
- [Open Container Initiative (OCI)](https://opencontainers.org/)
- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)