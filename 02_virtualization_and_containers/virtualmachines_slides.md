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

# Virtual Machines

---

## What is a Virtual Machine?

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/02_virtualization_and_containers/figs/virtualmachine-sketch.png" width=40%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- A computer inside your computer, with its own OS and resources
- Virtual Machines are portable and flexible

---

## Common Terms

- Host operating system
    - The OS the hypervisor is installed on
- Guest operating system
    - The OS running inside the virtual machine
- Virtual machine (VM)
    - Environment the guest is running in

---

## Types of Hypervisors

- **Type 1**
  - Runs directly on bare-metal hardware, like the host OS
  - Examples: [Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/), [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html), [Xen](https://xenproject.org/), [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine), ...
- **Type 2**
  - Negotiates resources shared with a host OS
  - Examples: [VirtualBox](https://www.virtualbox.org/), [VMWare Workstation Player](https://www.vmware.com/products/workstation-player.html), [Parallels](https://www.parallels.com/eu/products/desktop/)...

---

## (Some) Features of Virtual Machines

- Exclusive access to some of your resources
- Behaves like a native installation
- Isolation from host operating system
- Popular for
    - Safety critical tasks
    - Development and testing
    - Wherever one wants a portable solution

---

## Why is Virtualization Useful?

- Running multiple operating systems simultaneously
    - Test/develop/debug software for other OS
- Easier software installations and testing
    - Preconfigured VMs for teaching (see [preCICE Demo VM](https://precice.org/installation-vm.html))
- Testing and disaster recovery
    - Create snapshots before testing, copy VMs etc.
- Separate services from each other for security (see [Qubes OS](https://www.qubes-os.org/intro/))
- Reproducibility

---

## Summary

- Isolated environment that emulates a computer
- Different types of Hypervisors (bare-metal or running on OS)
- Run additional OSes on your machine
- VMs are portable, reproducible, easy to manage, and provide isolation

---

### Further Reading

- [VirtualBox Manual: 1. First Steps](https://www.virtualbox.org/manual/ch01.html)
- [VirtualBox Manual: 13. Security Guide](https://www.virtualbox.org/manual/ch13.html)
- ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
  (Kenneth Hoste, FOSDEM 2018)
