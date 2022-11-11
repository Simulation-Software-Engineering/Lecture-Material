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

- Environment that allows you to run any (supported) operating system (OS)
- Virtual Machines are portable and flexible

---

## Common Terms

- Host operating system (host OS)
    - The OS the hypervisor is installed on
- Guest operating system (guest OS)
    - The OS running inside the virtual machine
- Virtual machine (VM)
    - Environment the guest is running in

---

## Types of Virtual Machines / Hypervisors

- Sometimes distinction is not clear, but in general:
    - **Type 1**
        - Runs directly on bare-metal hardware
        - Examples: [Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/), [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html), [Xen](https://xenproject.org/)...
    - **Type 2**
        - Requires a running OS
        - Examples: [VirtualBox](https://www.virtualbox.org/), [VMWare Workstation Player](https://www.vmware.com/products/workstation-player.html), [Parallels (for Mac)](https://www.parallels.com/eu/products/desktop/), [Proxmox Virtual Environment](https://www.proxmox.com/en/proxmox-ve)...

---

## (Some) Features of Virtual Machines

- VM might obtain exclusive access to some of your resources.
- Behaves (more or less) as native installation (root etc., system calls).
- (Strict) isolation from host operating system
- Popular for
    - Safety critical tasks
    - Development and testing
    - Wherever one wants a portable solution

---

## Why is Virtualization Useful?

- Running multiple operating systems simultaneously
    - Test/develop software for other OS, debug problems on other OS, Windows on Linux, fill in forms of university (MS Office)
- Easier software installations and testing
    - Preconfigured VMs trainings and teaching
- Testing and disaster recovery
    - Create snapshots before testing, copy VMs etc.
- Infrastructure consolidation
    - Run many VMs on single host
- Separate services from each other (for security)
- Reproducible software environment for running and developing software

---

## Short Note on Security

- Does **not** solve all problems
- Separation from Host, but VM also tightly embedded in Host
- Virtual machine / Hypervisor might increase attack surface
- Additional layer of complexity
- Read the manual
    - Examples: GPU acceleration, networking, USB passthrough...
- Think about **what** you do and **before** you do it

---

## Summary

- Isolated environment that emulates a computer
- Different types of Hypervisors (bare-metal or running on OS)
- Run additional OSes on your machine
- VMs are portable
- Keep security in mind

**Note**: Do not (only) use VMs for shipping your software. Not everyone can run/use them.

---

### Further Reading

- [VirtualBox Manual: 1. First Steps](https://www.virtualbox.org/manual/ch01.html)
- [VirtualBox Manual: 13. Security Guide](https://www.virtualbox.org/manual/ch13.html)
- ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
