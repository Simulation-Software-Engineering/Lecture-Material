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

---

## VirtualBox

- Created by Innotek (Weinstadt, Germany)
- 2008 obtained by Sun Microsystems in 2008. Since 2010, owned by Oracle
- Initially closed source product with special license for personal use and evaluation (PUEL)
- Now: Open Source edition which is free, open-source virtual machine solution (GPL2)

---

## Setting up VirtualBox

- Requires hardware virtualization support
    - `VT-x`, ` VT-d`, `AMD-V`, ...
    - Check virtualization settings in BIOS/UEFI if it does not work out of the box
- Sufficient space on hard drive

---

## Virtual Hard Drive Formats

- Main formats
  - **VDI**: "Virtual Disk Image", VirtualBox' native format
  - **VHD**: Format used by Microsoft
  - **VMDK**: VMWare's virtual disk format
  - Support dynamic allocation
- Further (partially) supported formats: HDD (Parallels format only version 2 supported), QCOW, QED

**Note**: If you use btrfs as filesystem, you should disable CoW for the VM's images. (I/O load)

Source: [https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)

---

## Content of a VirtualBox Image

- `NAMEOFVM.vdi`: The virtual hard drive containing the guest os
- `NAMEOFVM.vbox`: XML containing metadata and configuration information (RAM, network devices...)
- `Logs/`: Directory containing log files
- `Snapshots/`: Snapshots of image

---

## Guest Additions

- "Guest Additions": Software and drivers to improves guest's performance
    - Drivers etc.
- Might need additional packages
  - On Ubuntu:
  ```
  perl dkms build-essential linux-headers-generic linux-headers-$(uname -r)
  ```


---

## Demo

---

## Summary

- Open-source system for virtual machines
- Simple to set up and run
- Offer flexibility on OS choice
- Manual setup. How to manage several VMs efficiently?
- Consistency of the environment?
- Sharing image with others?

> "If you can't git diff a file format, it's broken."

---

## Further Reading

- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
