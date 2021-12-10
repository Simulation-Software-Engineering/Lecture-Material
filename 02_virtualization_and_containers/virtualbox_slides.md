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

# VirtualBox

<img src="https://www.virtualbox.org/graphics/vbox_logo2_gradient.png" width=15%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

[https://www.virtualbox.org/graphics/vbox_logo2_gradient.png](https://www.virtualbox.org/graphics/vbox_logo2_gradient.png)

---

## Introduction

- Virtualization solution created by Innotek GmbH (Weinstadt, Germany)
- 2008 obtained by Sun Microsystems in 2008. Since 2010, owned by Oracle
- Initially closed source product with special license for personal use and evaluation (PUEL)
- Now: Open Source edition (GPL2)

---

## Requirements

- Reasonably new operating system (Windows, Mac OS, Linux, Oracle Solaris)
- Reasonably new hardware (SSE2 and virtualization support)
    - VT-x, VT-d, AMD-V, ...
    - Check virtualization settings in BIOS/UEFI if it does not work out of the box
- Sufficient space on hard drive
    - VM uses a virtual hard drive, i.e., a file on your drive
- Some video memory (recommend >=64MB)
- Exact requirements depend on VM

---

## Virtual Hard Drive Formats

- Main formats
    - **VDI**: "Virtual Disk Image", VirtualBox' native format
    - **VHD**: Format used by Microsoft
    - **VMDK**: VMWare's virtual disk format
    - Support dynamic allocation
- Further (partially) supported formats: HDD (Parallels format), QCOW, QED

**Note**: If you use btrfs as filesystem, you should disable CoW for the VM's images. (I/O load)

---

## Content of VirtualBox Image's Directory

- `NAMEOFVM.vdi`: The virtual hard drive containing the Guest os
- `NAMEOFVM.vbox`: XML containing metadata and configuration information (RAM, network devices...)
- `NAMEOFVM.vbox-prev`: Backup of previous settings
- `Logs/`: Directory containing log files
- `Snapshots/`: Snapshots of image

---

## Guest Additions

- Software and drivers to improves Guest's performance
    - Better video support, shared clipboard, mouse pointer integration...
- Might need additional packages
    - On Ubuntu 20.04

    ```bash
    sudo apt install virtualbox-guest-dkms virtualbox-guest-x11 virtualbox-guest-utils
    ```

    - `virtualbox-guest-x11` can be dropped on headless system
    - On Ubuntu for building packages manually

    ```bash
    perl dkms build-essential linux-headers-generic linux-headers-$(uname -r)
    ```

    - Then run installation script of Guest Additions
- Screen black after/during installation -> Increase video memory to >=64 MB


---

## Demo

Details available in [`virtualbox_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/virtualbox_demo.md)

---

## Summary and Outlook

- VirtualBox is open-source system for virtual machines
- Simple to set up and run
- Offers flexibility on OS choice
- Manual setup, but also CLI interface exists
- Next steps
    - How to manage several VMs efficiently?

    > "If you can't git diff a file format, it's broken."

    - Consistency of the environment?
    - Sharing image with others?


---

## Further Reading

- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- [VirtualBox Manual: 4. Guest Additions](https://www.virtualbox.org/manual/ch04.html)
- [Overview of different disk formats](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)
- [Ubuntu 18.04 virtual machine setup](https://codebots.com/docs/ubuntu-18-04-virtual-machine-setup)
