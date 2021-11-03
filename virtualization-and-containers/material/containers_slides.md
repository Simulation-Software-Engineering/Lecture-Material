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

# Containers

---

## What is a Container?

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/virtualization-and-containers/material/figs/container-sketch.png" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">


- Container operates in "fenced off" part of the operating system (`namespaces`)
- Low(er) overhead than virtual machines
  - Runs on kernel (and libraries) of the host OS
  - Cheap to start and stop a container
- Available features depend on Host
  - Linux container on Windows or vice versa?
- Container can be isolated

---

## Common Use-Cases

- Microservices
- Reproducible environments for developing and testing (DevOps)
- Container hype strongly driven by [Docker](https://www.docker.com/)
- More and more in science
  - High-performance computing, "Bring Your Own Environment" (BYOE)
  - Reproducible research

---

## Container Solutions

- Plenty of different container formats
  - [lxc/lxd](https://linuxcontainers.org/), [Docker](https://www.docker.com/), [Singularity](https://sylabs.io/), [podman](https://podman.io/), [Sarus](https://user.cscs.ch/tools/containers/sarus/)...
- Different solutions with different strengths due to different use cases
  - (Super-)Userspace
  - Direct access to hardware (memory, storage, GPUs) vs. encapsulation
  - Generic or with integration in software ecosystem (e.g. schedulers)
- Effort to establish certain standards
  - [Open Container Initiative (OCI)](https://opencontainers.org/)

---

## Security

- Docker considers itself save

  > Applications are safer in containers and Docker provides the strongest default isolation capabilities in the industry

  - But so do most others
- Read the manual
- Are third-part containers trust worthy?
  - There have been cases [of malicious images](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)
- Containers isolation from Host depends on container framework
- Think about **what** you do, **before** you do it

---

## Summary

- Shares many similarities with VMs, but
  - Lightweight alternative to VMs
  - Stricter limitations than VMs
- Many different containers solutions
  - Standardization effort
  - Choose right container for your use case

**Note**: Do not (only) use containers for shipping your software. Not everyone can run/use them.

---

## Further Reading

- [Docker](https://www.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Singularity](https://sylabs.io/)
- [Sarus](https://user.cscs.ch/tools/containers/sarus/)
- [lxc/lxd](https://linuxcontainers.org/)
- [podman](https://podman.io/)
- [Open Container Initiative (OCI)](https://opencontainers.org/)
- [Singularity: Scientific containers for mobility of compute](https://doi.org/10.1371/journal.pone.0177459)
- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)