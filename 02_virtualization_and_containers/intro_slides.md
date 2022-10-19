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

# Virtualization and Containers

---

## Learning Goals

- What is the difference between virtualization and containers?
- When and how to use virtual machines and/or containers.
- How to work with virtual machines (VirtualBox) and how to manage these with Vagrant.
- How to work with containers with Docker (and Singularity).
- You know how to set up own containers tailored to your requirements.

---

## Virtualization and Containers for SSE

- Developing, testing and debugging software
    - Abstraction layer for different OS, configurations etc.
    - Ensure software quality
- Moving/Sharing software
    - Avoid compilation and/or setup complexity, OS dependency
    - Work around target limitations (e.g. HPC)
- Manage complex workflows
    - Ideally under version control
    - (Potentially) Break down big software into smaller
- Reproducible research
    - Make sure others get the same results
    - Make sure others are able to run your software (also in future)
- Focus on established, open-source software

---

## Contents of this Chapter

- Virtual Machines
    - VirtualBox: Popular hypervisor for running VMs
    - Vagrant: Popular management system for VMs (and more)
- Containers
    - Docker: Popular container framework (and more)
    - Singularity: Popular scientific container framework

