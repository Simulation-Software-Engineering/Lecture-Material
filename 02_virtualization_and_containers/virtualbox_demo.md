# VirtualBox demo

## Introduction to Virtualization

![A sketch of virtual machines](./material/figs/virtualmachine-sketch.png)

![A sketch of containers](./material/figs/container-sketch.png)

- What is virtualization and what is containerization?
    - What problems do they solve? Why do we need them?
- Virtual machines (VWs)
    - Emulating a complete computer.
    - Virtual machine brings the full software stack (kernel, libraries etc.)
    - Has a (type 1/2) hypervisor. Type 1 runs on bare metal while type 2 runs within an operating system. Distinction not always clear.
    - Might need/benefit from virtualization technologies (VT-X)
    - Great flexibility. Can run (normally) any operating system that runs on the virtualized platform.
    - Strict separation from host operating system. (Popular for safety critical tasks: c't banking os, Desinfec't, Remote laptops)
- Focus of lecture will be on Linux and Linux-based containers and VMs.
- Various virtualization and container technologies and tools to manage them. Sometimes separation is a bit vague/complicated and changed over time (lxc/lxd, Docker).
- We discuss tools and use cases that are (more) likely to be encountered in simulation software.

## Introduction to VirtualBox

- You can have root rights inside your virtual machine.
- What problems does it solve?
    - You want to run a different operating system within your current one. Example: I am on Linux, but want to use Microsoft Office and other stuff (without using WINE/Proton).
    - You want to run services in an encapsulated way. Want to run than one server on one physical machine. (Proxmox, KVM)
- Hypervisors create some overhead.
- Content of a VirtualBox Image
    - Show directory on drive:
        - `NAMEOFVM.vdi`: The virtual hard drive containing the guest os
        - `NAMEOFVM.vbox`: XML containing metadata and configuration information (RAM, network devices...)
        - `NAMEOFVM.vbox-prev`: Backup of previous settings
        - `Logs/`: Directory containing log files
        - `Snapshots/`: Snapshots of image
- Short question: What type of hypervisor is VirtualBox? Type 2

## Demo

- Discuss configuration:
    - Virtual machine will reserve cores/threads of your CPU and main memory.
- Maybe go through installation process to show that it is the same as installing an OS on your normal computer.
- Create a new virtual machine and boot it up (nothing will happen).
- Boot up some configured virtual machine (Ubuntu).
- Creating a new virtual machine
    - Click on `new`
    - I use `expert mode` to set disk location, size and memory. Note, that one can change that also later on.
    - After clicking on `Create` a menu to create the `Virtual Hard Disk` opens.
        - One can choose between fixed size and dynamically allocated (i.e. the drive grows). I personally recommend avoiding dynamically allocated without upper limit.
    - Creates empty machine. Will not do much as we do not have any OS installed. VirtualBox will prompt to mount an image (iso).
    - Show system settings of VM.
    - Storage -> Controller (Mount drive here) and boot again. -> Installation will start up.
        - Normally should unmount image after installation.
    - Install "VirtualBox Guest Additions". Might have to download the image.
        - Devices `Insert Guest Additions CD image"

        ```bash
        sudo mkdir -p /media/cdrom
        sudo mount /dev/cdrom /media/cdrom
        cd /media/cdrom
        sudo apt-get install -y perl dkms build-essential linux-headers-generic linux-headers-$(uname -r)
        sudo su
        ./VBoxLinuxAdditions.run
        ```

        - Will enable clipboard sharing etc
        - Alternative on Ubuntu

        ```bash
        sudo apt install virtualbox-guest-dkms virtualbox-guest-x11 virtualbox-guest-utils
        ```

        - `virtualbox-guest-x11` can be dropped on headless system
    - VM will capture mouse pointer. Use `Right-CTRL` to "free" pointer again.
    - Create snapshots on image overview (Burger symbol on the right)
        - Load snapshots for different configuration stages
    - Configure network for ssh
        - Install `openssh-server`
        - Shutdown VM
        - In VirtualBox window -> File -> Host Network Manager -> Verify that network device is configured `vboxnet0`
        - In virtual machine's settings -> Network -> Adapter 2 -> Enable and set Host only adapter `vboxnet0`
        - Boot VM
        - Verify additional network device `enp0s8` and check for ip address. In my case `192.168.56.101`
        - On host machine `ssh vmuser@192.168.56.101`
- Show/install extensions to allow for
    - Some 3D rendering
    - Shared clipboard
    - In general: *Better integration* into host system
- Create a shared drive to exchange data instead of copy and pasting file content.
    - In case one cannot access it `sudo usermod -aG vboxsf $(whoami)`
    - You need to logout and in again afterwards for usergroups to be recognized.
    - I share `/media/jaustar/external-ssd/virtualmachines/shared-folder`
    - Add some file there and check that it appears Host and vice versa.
