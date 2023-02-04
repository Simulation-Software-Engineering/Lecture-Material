# Containers Demo

## Introduction to Containers

- What are the differences between VMs and containers?
    - Containers
        - Low(er) overhead than virtual machines.
        - Container operates in "fenced off" part of the operating system (`cgroups`).
        - Container runs kernel of the host OS -> Does **not** run its own OS in.
        - Operating system (OS) needs to be compatible with underlying OS. Cannot run different OS than host. (TODO: Verify this)
            - **Note**: Windows 10 can run Linux containers! (Due to Windows Subsystem for Linux?!)
        - A process for which (and its children) special rules apply.
- Shortly recap what we have learned about containers.
    - Fenced-off, relies on capabilities of OS etc.
- LXD/LXC and its container registry [Linux containers](https://linuxcontainers.org/)
- Short and incomplete overview over container technologies: Docker, Singularity, lxc/lxd, podman...

## Concluding Remarks and Discussion about Learning Goals

- Virtual machines are a good abstraction layer that are very flexible. They can run different OS, can be moved etc. VirtualBox is a popular VM solution (hypervisor).
- There are tools like Vagrant to manage them more conveniently than with the GUI or CLI.
- Containers are a light weight alternative to VMs. They are basically "special" processes that run more or less in an isolated manner. Therefore, they do not need to bring everything (kernel, libraries...) themselves, but rely on the functionalities of the Host. Example: Containers "run" on the same kernel as the Host. Cannot mix OSes (easily).
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
