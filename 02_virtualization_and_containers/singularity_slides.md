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

# Singularity / Apptainer

---

## Introduction

- Initiated in 2015 at Lawrence Berkeley National Laboratory
- Two open source projects, fork in 2021:
    - [Apptainer](https://apptainer.org/) (The Linux Foundation)
    - SingularityCE (Sylabs)
- More [related enterprise products by Sylabs](https://sylabs.io/products/)

---

## Image registries

- [Sylabs Cloud](https://cloud.sylabs.io/library)
    - Image registry and remote builder
- [Singularity Hub](https://singularityhub.github.io)
   - Older open source registry

---

## Goals

- Verifiable reproducibility and security
    - Immutable images with encryption and verification support
- Integration over isolation by default
    - Access hardware (GPU, network...) and filesystems
- Simple and effective security model
    - Same user inside and outside container
- "Mobility of Compute"
    - Single file container for easy transport and sharing

---

## Differences to Docker

- User rights enough for running container
- Automatically mounts [common directories](https://apptainer.org/docs/user/latest/bind_paths_and_mounts.html#system-defined-bind-paths)
    - `${HOME}`, `${PWD}`, network etc.
- Allows "untrusted user to run untrusted containers"
    - Important for shared facilities (computing centers etc.)
- (Normally) Immutable containers
    - Set up environment and immutable data in container
- Support for typical HPC environments (schedulers, MPI, GPU...)

---

## Typical Singularity Applications

- Bring Your Own Environment
- Reproducible research
- Software needs specific environment
    - Legacy code, commercial software, unmaintained research software
- "Hiding" complicated software stack
- Conservation of (complicated) workflows

---

## Useful Commands

- `singularity exec`
    - Execute a command within container
- `singularity run`
    - Launch a runscript within container
- `singularity shell`
    - Run a Bourne shell within container
- `singularity build`
    - Build a new Singularity container
    - Use `--sandbox` for mutable container
- `singularity pull`
    - Pull a Singularity image (`.sif` file)

---

## Demo: Run prebuilt containers

Details available in [`singularity_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/singularity_demo.md)

---

## Defining and Building own Images

- Build instructions in text file
    - Git friendly
- Start from base images
    - Several bootstrap strategies (container sources)
    - Images can be based on Docker images
- Extra steps
    - `%post`: Steps after OS installation
    - `%environment`: Set environment variables (`PATH` etc.)
    - `%runscript`: Container behavior under `singularity run`
    - `%labels`: Extra information
    - `%pre`, `%setup`... (see [Documentation](https://apptainer.org/docs/user/latest/definition_files.html))

---

## Image Recipe Example

```Singularity
BootStrap: docker
From: ubuntu:22.04

%post
   apt-get -y update
   apt-get -y install cowsay lolcat

%environment
   export LC_ALL=C
   export PATH=/usr/games:$PATH

%runscript
   date | cowsay | lolcat
```

https://apptainer.org/docs/user/latest/quick_start.html

---

## Demo: Build own containers

Details available in [`singularity_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/singularity_demo.md)

---

## Advanced topics

- Run container as service (called `instance`)
- Parallel computing
    - Using correct MPI, network drivers
    - MPI: hybrid model, bind model
- Mounting additional directories
- Signing, sharing and sandbox containers
- Performance vs. Portability
    - Compile content with `arch=generic` or `arch=TARGET`?

---

## Summary

- Special container format for scientific computing
- Immutable containers in a single file
- Prefers integration over isolation
- Other solutions: [Sarus](https://user.cscs.ch/tools/containers/sarus/), [Charliecloud](https://hpc.github.io/charliecloud/)

---

## Further Reading

- [Apptainer user guide](https://apptainer.org/docs/user/latest/index.html)
- [Singularity User Guide](https://docs.sylabs.io/guides/main/user-guide/)
- [Singularity Cloud](https://cloud.sylabs.io/library)
