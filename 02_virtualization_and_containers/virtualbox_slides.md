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

<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/VirtualBox_2024_Logo.svg" width=20%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

---

## Introduction

- Hosted hypervisor created by Innotek GmbH (Weinstadt, Germany)
- Obtained by Sun Microsystems in 2008. Since 2010, owned by Oracle
- Open source (GPLv3)

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

## Virtual Hard Drive Formats

- Virtual hard drive as a file
- Multiple formats, for example:
    - **VDI**: "Virtual Disk Image", VirtualBox' native format
    - **VHD**: Format used by Microsoft
    - **VMDK**: VMWare's virtual disk format
    - Support for dynamic allocation

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

## Summary and Outlook

- VirtualBox is an open-source system for virtual machines
- Simple to set up and run
- Manual setup, but command-line interface exists
- Next step: Infrastructure as code
    - Consistency of the environment?
    - How to share a VM image with others?

    > "If you can't git diff a file format, it's broken."


---

## Further Reading

- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- [VirtualBox Manual: 4. Guest Additions](https://www.virtualbox.org/manual/ch04.html)
- [Overview of different disk formats](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)
