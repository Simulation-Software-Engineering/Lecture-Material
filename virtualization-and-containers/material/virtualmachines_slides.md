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

![A sketch of virtual machines](figs/virtualmachine-sketch.png)

- Environment that allows you to run any (supported) operating
- Virtual Machines are portable and flexible
- Strict separation from host operating system. (Popular for safety critical tasks: Desinfec't, Remote laptops)

---

## General information

- Big variety of solutions Kernel-based Virtual Machine (KVM)
- You can have root rights inside your virtual machine.
- VM will obtain exclusive access to some of your resources
- What problems does it solve?
    - You want to run a different operating system within your current one. Example: I am on Linux, but want to use Microsoft Office and other stuff (without using WINE/Proton).
    - You want to run services in an encapsulated way. Want to run than one server on one physical machine. (Proxmox, KVM)

---

## Common terms

- Host operating system (host OS)
    - The OS the hypervisor is installed on
- Guest operating system (guest OS)
    - The OS running inside the virtual machine
- Virtual machine (VM)
    - Environment the guest is running in

---

## Why is Virtualization Useful?

### For us

- Running multiple operating systems simultaneously
    - Test/develop software for other OS, debug problems on other OS...
- Easier software installations and testing
    - Offer preconfigured VM for users. Useful for trainings and teaching.
- Testing and disaster recovery
    - Create snapshots beforetesting. Copy VMs etc.

### Further benefits

- Infrastructure consolidation
    - Run many VMs on single host
- Seperate service from each other (security?!)

[VirtualBox Manual](https://www.virtualbox.org/manual/ch01.html)

---

## Types of Virtual Machines/ Hypervisors

- Sometimes distinction not clear, but in general:

### Type 1

- Runs directly on bare-metal hardware
- Examples: Microsoft Hyper-V, VMware ESXi, Proxmox Virtual Environment, Xen...

### Type 2

- Requires a running OS
- Examples: VirtualBox, VMWare Player, VMWare Workstation, Parallels (for Mac)...

---

## Summary

- Allows to run additional OS on your machine
- VM is encapsulated