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

# Virtual machines

---

## What is a virtual machine?

![A sketch of virtual machines](virtualmachine-sketch.png)

- Emulating a complete computer.
- Has a (type 1/2) hypervisor. Type 1 runs on bare metal while type 2 runs within an operating system. Distinction not always clear.
- Might need/benefit from virtualization technologies (VT-X)
- Great flexibility. Can run (normally) any operating system that runs on the virtualized platform.
- Strict separation from host operating system. (Popular for safety critical tasks: c't banking os, Desinfec't, Remote laptops)

---

## Why is Virtualization Useful?

- Running multiple operating systems simultaneously
- Easier software installations
- Testing and disaster recovery
- Infrastructure consolidation

[VirtualBox Manual](https://www.virtualbox.org/manual/ch01.html)

---

## Types of Virtual Machines/ Hypervisors

- Sometimes distinction not clear, but in general:

### Type 1

- Runs directly on bare-metal hardware

### Type 2

- Requires a running OS to

---

## Common terms

- Host operating system (host OS)
    - The OS the hypervisor is installed on
- Guest operating system (guest OS)
    - The OS running inside the virtual machine
- Virtual machine (VM)
