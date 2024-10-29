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

- Name differences between virtualization and containers and name use cases for each.
- Create and modify virtual machines with VirtualBox and generate them with Vagrant.
- Create and manage Docker containers.
- Name containerization technologies beyond Docker and name their main differences.

---

## Virtualization and Containers for SSE

- Developing, testing and debugging software
    - Abstraction layer for different OS, configurations etc.
- Moving/Sharing software
    - Avoid compilation and/or setup complexity, OS dependency
- Manage complex workflows, ideally under version control
- Reproducible research
    - Make sure others are able to run your software (also in future).
    - Make sure others get the same results.

---

## Contents of this Chapter

- Virtual Machines (VMs)
    - VirtualBox: Popular hypervisor for running VMs
    - Vagrant: Popular management system for VMs (and more)
- Containers
    - Docker: Popular container framework (and more)
    - Singularity: Popular scientific container framework
