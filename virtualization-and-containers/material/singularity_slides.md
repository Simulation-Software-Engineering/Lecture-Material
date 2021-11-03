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

# Singularity

<img src="https://sylabs.io/assets/svg/singularity-logo.svg" width=20%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

[https://sylabs.io/assets/svg/singularity-logo.svg](https://sylabs.io/assets/svg/singularity-logo.svg)

---

## Introduction

- Initiated at Lawrence Berkeley National Laboratory
- Now: Developed by [Sylabs](https://sylabs.io)
- Written in  Go
- Comes in [different flavors](https://sylabs.io/singularity/)
  - SingularityCE (Community edition, open source, BSD licensed)
  - SingularityPro (Enterprise)
  - Singularity Enterprise (More enterprise?)
  - SingularityDesktop (Mac, Beta)
  - [Sylabs Cloud](https://cloud.sylabs.io/library)
    - Image registry and remote builder
  - [Singularity Hub](https://singularityhub.github.io)
    - Open source registry
- Community edition open source (BSD license)

---

## Goals

- Verifiable reproducibility and security
  - Immutable images with encryption and verification support
- Integration over isolation by default
  - Access hardware (GPU, network...) and filesystems
- Simple and effective security model
  - Same user inside and outside container
- Mobility of Compute
  - Single file container for easy transport and sharing

---

## Typical Singularity Applications

- Bring Your Own Environment
- Reproducible research
- Software needs specific environment
  - Legacy code, commercial software, unmaintained research software
- "Hiding" complicated software stack
- Conservation of (complicated) workflows

---

## Notable Properties

- Only needs root when creating images
- User rights for running container
- Automatically mounts common directories
  - `${HOME}`, `${PWD}`, network etc.
- Allows to run "untrusted user to run untrusted containers"
  - Important for shared facilities (computing centers etc.)
- (Normally) Immutable containers
  - Set up environment and immutable data in container
- Support for typical HPC environments (schedulers, MPI, GPU...)

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
  - Pull a Singularity/Docker container to ${PWD}

---

## Demo: Run prebuilt containers

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
  - `%pre`, `%setup`... (see [Documentation](https://sylabs.io/guides/master/user-guide/definition_files.html#sections))

---

## Image Recipe Example

```Singularity
BootStrap: library
From: ubuntu:18.04

%post
    apt-get -y update
    apt-get -y install date cowsay lolcat

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    date | cowsay | lolcat

%labels
    Author Sylabs
```

[https://sylabs.io/guides/master/user-guide/quick_start.html#build-images-from-scratch](https://sylabs.io/guides/master/user-guide/quick_start.html#build-images-from-scratch)

---

## Demo: Build own containers

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
- Potential successor: [Sarus](https://user.cscs.ch/tools/containers/sarus/)

---

## Further Reading

- [Singularity User Guide](https://sylabs.io/guides/master/user-guide)
- [Singularity Cloud](https://cloud.sylabs.io/library)
- [Sarus](https://user.cscs.ch/tools/containers/sarus/)