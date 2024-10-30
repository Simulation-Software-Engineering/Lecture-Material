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

# Vagrant

<img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Vagrant.png" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

---

## Introduction

- Infrastructure as code

    > Vagrant is a tool for building and managing virtual machine environments in a single workflow.
    > <small>https://developer.hashicorp.com/vagrant/intro</small>

- Initial release 2010 by Mitchell Hashimoto, now [HashiCorp](https://www.hashicorp.com/)
- HashiCorp develops DevOps tools such as [Vagrant](https://www.vagrantup.com/) and [TerraForm](https://www.terraform.io/)

---

## Building Blocks

- Provisioners
    - Tool for configuring the boxes (install software on machine)
    - Examples: shell scripts, Ansible, Chef, Puppet..
- Providers
    - "Backend" on which the box is based
    - Examples: VirtualBox, Hyper-V, libvirt, AWS, Docker...

---

## What for?

- Developing software
    - Set up consistent development environment
    - Share environment with others
- Testing software, workflows...
    - Disposable environments
    - Consistent workflows
- More general
    - Simple way to setup virtual machine
- Reproducible environment

---

## Advantages

- Strong focus on workflow consistency
- (Re)use existing images
- Automatize VM creation and configuration
    - Easier than with VirtualBox CLI and shell scripts
- Store in Git-friendly format
- For us:
    - Management of VirtualBox VMs (testing, developing...)
    - Sharing of VMs (debugging, workshops...)

---

## Some Useful Commands 1/2

- `vagrant init USERNAME/BOXNAME or URL`
    - Initializes repository in current directory
    - Creates `Vagrantfile` -> Text file (Git friendly)
- `vagrant up`
    - Create VM and start it
    - VM is stored in `${HOME}/.vagrant.d/boxes` (overruled by `VAGRANT_HOME`)
- `vagrant ssh`
    - Connect to VM via ssh
- `vagrant destroy`
    - Stops the virtual machine and removes its disk

---

## Some Useful Commands 2/2

- `vagrant box list`
    - Show available boxes
- `vagrant box remove NAMEOFBOX`
    - Remove a box completely
- `vagrant suspend`
    - Suspends machine (sleep)
- `vagrant halt`
    - Shuts down machine keeping changes
- `vagrant reload --provision` or `vagrant provision`
    - Rebuild (partially) built image

---

## Demo: Premade Vagrant VM

Details available in [`vagrant_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/vagrant_demo.md)

---

## Structure of Vagrant Box

- File `Vagrantfile`
    - Contains configuration of VM
- Supplementary files, scripts etc. for configuring VM
    - Example: `bootstrap.sh`
- Files are usually text files (Git friendly)

---

## Setting up a Virtual Machine

- Install VirtualBox and Vagrant
- Create `Vagrantfile` and specify image

    ```ruby
    Vagrant.configure("2") do |config|
        config.vm.box = "bento/ubuntu-24.04"
        config.vm.box_version = "202407.23.0"
    end
    ```

- Alternative (creates the corresponding `Vagrantfile`):

    ```bash
    vagrant init bento/ubuntu-24.04
    ```

- Start VM with `vagrant up`

---

## Exchanging Files

- Vagrant mounts shared folders
    - Check output when VM starts

    ```bash
    default: Mounting shared folders...
    ```

    - Files can be exchanged between Guest and Host (bidirectional)
- Default:
    - Directory containing `Vagrantfile` mounted to `/vagrant`
    - Natural use case: Build your code in a VM

---

## Vagrant Cloud

- Repository of premade boxes: [HashiCorp Cloud](https://portal.cloud.hashicorp.com/vagrant/discover)
- Package a box:

    ```bash
    vagrant package --base "NAMEOFVM" --output BOXNAME.box
    ```

    - `NAMEOFVM` is name as shown in VirtualBox
    - `BOXNAME` name to store box to
- [Publish own boxes](https://developer.hashicorp.com/vagrant/docs/providers/virtualbox/boxes)

---

## Demo: Own box

- `bento/ubuntu-24.04`:
    - [HashiCorp Cloud](https://portal.cloud.hashicorp.com/vagrant/discover/bento/ubuntu-24.04)
    - [GitHub](https://github.com/chef/bento)
- `precice/precice-vm`:
    - [HashiCorp Cloud](https://portal.cloud.hashicorp.com/vagrant/discover/precice/precice-vm)
    - [GitHub](https://github.com/precice/vm)
    - [User Documentation](https://precice.org/installation-vm.html)

---

## Summary

- Git-friendly way of configuring VMs
- Simple management of VMs
- Creates consistent workflows
- Flexible due to big variety of provisioners and providers
- Premade images can be used and shared

---

## Further Reading

- [Vagrant Homepage](https://www.vagrantup.com/)
- [Vagrant Introduction](https://developer.hashicorp.com/vagrant/intro)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- StackOverflow: ["Should I use Vagrant or Docker for creating an isolated environment?"](https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-for-creating-an-isolated-environment)
    with answers by both Vagrant and Docker creators (!)
