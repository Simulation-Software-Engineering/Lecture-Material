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

---

## Introduction

- Remember:
  > If you can't git diff a file format, it's broken.
- Infrastructure as code
  > Vagrant is a tool for building and managing virtual machine environments in a single workflow.
  [https://www.vagrantup.com/intro](https://www.vagrantup.com/intro)
- Initial release 2010 by Mitchell Hashimoto, now [HashiCorp](https://www.hashicorp.com/)
- HashiCorp develops open-source DevOps/Cloud tools like [Vagrant](https://www.vagrantup.com/), [TerraForm](https://www.terraform.io/)...

---

## What for?

- Developing software
  - Set up consistent development environment
  - Share environment with others
- Testing software, workflows...
  - Disposable environments
  - Consistent workflows
- More general
  - Easy way to setup virtual machine

---

## Advantages

- Strong focus on workflow consistency
- Avoid usage of (VirtualBox) CLI
- Store in Git-friendly format
- For us:
  - Management of VirtualBox VMs (testing, developing...)
  - Sharing of VMs (debugging, workshops...)

---

## Building Blocks

- Provisioners
  - Tool for configuring the boxes (install software on machine)
  - Examples: shell scripts, Chef, Puppet..
- Providers
  - "Backend" the box is based on
  - Examples: VirtualBox, Hyper-V, AWS, Docker...

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
  - Rebuild (partially) build image

---

## Structure of Vagrant Box

- File `Vagrantfile`
  - Contains configuration of VM
  - Ruby script
- Supplementary files, scripts etc. for configuring VM
  - Example: `bootstrap.sh`
- Files are usually text files (Git friendly)

---

## Setting up a Virtual Machine

- Install VirtualBox
- Install Vagrant (ideally from homepage so it is a recent release)
- Create `Vagrantfile` and specify image

  ```ruby
  Vagrant.configure("2") do |config|
    config.vm.box = "ajaust/sse-first-steps"
    config.vm.box_version = "0.1.0"
  end
  ```

- Alternative:

  ```
  vagrant init ajaust/sse-first-steps
  ```

- Start VM with `vagrant up`

---

## Exchanging Files

- Vagrant mounts shared folders
  - Check output when VM starts

  ```bash
  default: Mounting shared folders...
  ```

  - File can be changed from Guest or Host
- Default:
  - Directory containing `Vagrantfile` mounted to `/vagrant` in the Guest

---

## Demo: Premade Vagrant VM

---

## Vagrant Cloud

- Repository of premade boxes: [https://app.vagrantup.com/](https://app.vagrantup.com/)
- Pack box:

  ```bash
  vagrant package --base "NAMEOFVM" --output BOXNAME.box
  ```

  - `NAMEOFVM` is name as shown in VirtualBox
  - `BOXNAME` name to store box to
- [Publish own boxes](https://www.vagrantup.com/docs/providers/virtualbox/boxes) by uploading to [Vagrant Cloud](https://app.vagrantup.com/)

---

## Demo: Own box

- [Own box online](https://app.vagrantup.com/ajaust/boxes/sse-first-steps/versions/0.1.0)

---

## Demo: preCICE VM

- [https://github.com/precice/vm](https://github.com/precice/vm)
- [Premade box](https://app.vagrantup.com/precice/boxes/precice-vm)

---

## Summary

- Open-source tool
- Git-friendly way of configuring VMs
- Simple management of VMs
- Creates consistent workflows
- Flexible due to big variety of provisioners and providers
- Premade images can be used and shared

---

## Further Reading

- [Vagrant Homepage](https://www.vagrantup.com/)
- [Vagrant Introduction](https://www.vagrantup.com/intro)
- [VirtualBox Manual](https://www.virtualbox.org/manual/UserManual.html)
- ["Should I use Vagrant or Docker for creating an isolated environment?"](https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-for-creating-an-isolated-environment)
