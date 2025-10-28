---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
  slideNumber: true
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

# Virtual machines with VirtualBox

<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/VirtualBox_2024_Logo.svg" width=20%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

---

## What is a Virtual Machine?

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/02_virtualization_and_containers/figs/virtualmachine-sketch.png" width=40%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- A computer inside your computer, with its own OS and resources
- Virtual Machines are portable and flexible

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

## Types of Hypervisors

- **Type 1**
    - Runs directly on bare-metal hardware, like the host OS
    - Examples: [Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/), [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html), [Xen](https://xenproject.org/), [KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine), ...
- **Type 2**
    - Negotiates resources shared with a host OS
    - Examples: [VirtualBox](https://www.virtualbox.org/), [VMWare Workstation Player](https://www.vmware.com/products/workstation-player.html), [Parallels](https://www.parallels.com/eu/products/desktop/)...

---

## VirtualBox

- Hosted hypervisor created by Innotek GmbH (Weinstadt, Germany)
- Obtained by Sun Microsystems in 2008. Since 2010, owned by Oracle
- Free software (GPLv3)

---

## Requirements

- Linux, macOS, Windows
- Reasonably new hardware with virtualization support
    - Check virtualization settings in your BIOS/UEFI
- Sufficient space on hard drive
    - VM uses a virtual hard drive, i.e., a file on your drive
- Some video memory
- Exact requirements depend on VM: CPU cores, RAM, ...

---

## Note on CPU architectures

- VirtualBox runs both on x86 and ARM
- ARM hosts need ARM VMs (no emulation)
- Linux support limited/recent (e.g., Ubuntu 25.10)
- Emulation alternative (very slow): [UTM](https://mac.getutm.app/)

---

## Content of a VirtualBox Image Directory

- `VM.vdi`: The virtual hard drive containing the Guest OS
- `VM.vbox`: XML containing metadata and configuration information (RAM, network devices...)
- `VM.vbox-prev`: Backup of previous settings
- `Logs/`: Directory containing log files
- `Snapshots/`: Snapshots of image

---

## Guest Additions

- Software and drivers to improves Guest's performance
    - Better video support, shared clipboard, ...
- Might need additional packages. On Ubuntu 24.04 (guest):

    ```bash
    sudo apt install virtualbox-guest-utils virtualbox-guest-x11
    ```

---

## Demo

Details available in [`virtualbox_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/virtualbox_demo.md)

---

## Further Reading

- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- [VirtualBox Manual: 1. First Steps](https://www.virtualbox.org/manual/ch01.html)
- [VirtualBox Manual: 4. Guest Additions](https://www.virtualbox.org/manual/ch04.html)
- [VirtualBox Manual: 13. Security Guide](https://www.virtualbox.org/manual/ch13.html)
- [Overview of different disk formats](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)
