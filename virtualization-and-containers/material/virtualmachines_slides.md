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

- VM will obtain exclusive access to some of your resources
- What problems does it solve?
- Behaves (more or less) as native installation (root etc., system calls)

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

- **For us**
  - Running multiple operating systems simultaneously
      - Test/develop software for other OS, debug problems on other OS, Windows on Linux...
  - Easier software installations and testing
      - Offer preconfigured VM for users. Useful for trainings and teaching.
  - Testing and disaster recovery
      - Create snapshots beforetesting. Copy VMs etc.
- Further benefits
  - Infrastructure consolidation
      - Run many VMs on single host
  - Seperate service from each other (security?!)

[VirtualBox Manual](https://www.virtualbox.org/manual/ch01.html)

---

## Types of Virtual Machines/ Hypervisors

- Sometimes distinction not clear, but in general:

- **Type 1**
  - Runs directly on bare-metal hardware
  - Examples: [Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/), [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html), [Proxmox Virtual Environment](https://www.proxmox.com/en/proxmox-ve), [Xen](https://xenproject.org/)...
- **Type 2**
  - Requires a running OS
  - Examples: [VirtualBox](https://www.virtualbox.org/), [VMWare Workstation Player](https://www.vmware.com/products/workstation-player.html), [Parallels (for Mac)](https://www.parallels.com/eu/products/desktop/)...

---

## Short Note on Security

- Think about what you do
- Separation from Host, but VM also tightly embedded in Host
- Read the manual
  - Examples: GPU acceleration, networking, USB passthrough...

[VirtualBox Security Guide](https://www.virtualbox.org/manual/ch13.html)
---

## Summary

- Allows to run additional OSes on your machine
- Different types: 1 or 2
- VM is encapsulated environment