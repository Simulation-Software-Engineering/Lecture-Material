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

# VirtualBox

---

## What is a virtual machine?

- Big variety of solutions Kernel-based Virtual Machine (KVM)
- Short background story
    - Created by Innotek (Weinstadt, Germany! That is close to Stuttgart) and obtained by Sun Microsystems in 2008. Since 2010, owned by Oracle.
- Initially closed source product with special license for personal use and evaluation (PUEL). Now: Open Source edition which is free, open-source virtual machine solution (GPL2).
- Discuss some additional foundations of virtualization technologies.
- Virtual machines are based on virtual disks (VDI) which are virtual hard drives. Might be static or dynamic in size. Makes it possible to move virtual machines easily around.
- You can have root rights inside your virtual machine.
- VM will obtain exclusive access to some of your
- What problems does it solve?
    - You want to run a different operating system within your current one. Example: I am on Linux, but want to use Microsoft Office and other stuff (without using WINE/Proton).
    - You want to run services in an encapsulated way. Want to run than one server on one physical machine. (Proxmox, KVM)
- Short question: What type of hypervisor is VirtualBox? Type 2


---

## Setting up VirtualBox

- Requires hardware virtualization support
    - `VT-x`, ` VT-d`, `AMD-V`...
    - Check virtualization settings in BIOS/UEFI if it does not work out of the box.
- "Guest Additions": Software and drivers to improves guest's performance
    - To be installed on guest

---

## Virtual Hard Drive Formats

Supported formats:
- **VDI**: "Virtual Disk Image", VirtualBox' native format
- **VHD**: Format used by Microsoft
- **VMDK**: VMWare's virtual disk format

Further (partially) supported formats:
- HDD: Parallels format (only version 2 supported)
- QCOW
- QED

**Note**: If you use btrfs as filesystem, you should disable CoW for the VM's images. (I/O load)

Source: [https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/](https://www.parallels.com/blogs/ras/vdi-vs-vhd-vs-vmdk/)

---

## Further Reading

- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)