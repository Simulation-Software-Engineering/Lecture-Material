# Virtual Machines Demo

## Introduction to Vagrant

- Initially developed by Mitchell Hashimoto as side project.
- Released in 2010.
- Now developed by Hashimoto's company HashiCorp.
    - HashiCorp develops a variety of open-source tools for DevOps and cloud computing. In general for large scale projects.
- Configure VMs (I think also containers nowadays) conveniently via text files
- Infrastructure as code (Git lecture: If you cannot use `diff`, it is the wrong format!)
- Standard user and all passwords are `vagrant`.

## Demo: Premade Vagrant VM

Tutorial case in `/media/jaustar/external-ssd/virtualmachines/vagrant/tutorial`

- `vagrant init hashicorp/bionic64` creates a base `Vagrantfile`.
- `vagrant up` Creates `Vagrantfile`. This file can be put in version control.
- Download and set up VM.
- Will also start VM
- Open VirtualBox to see a VM running. We can open the box there, but are prompted for login username and password.
- Note: The actual "box" is put under your home directory
- `vagrant ssh` Connect to running VM
- See different username/hostname
- Different Ubuntu (18.04)
- `vagrant destroy` Will destroy (delete) current VM
- Alternatives:
- `vagrant suspend` Suspends VM
- `vagrant halt` Shuts VM down, keeping changes in the VM
- `vagrant status` Shows status of currently running VMs

- Exchanging files
    - Check output `default: Mounting shared folders...`
    - Default: Directory containing `Vagrantfile` is mounted as    `/vagrant`
    - Can configure more drives
    - Show example by creating file from Vagrant session

## Demo: Own box

- [Own box online](https://app.vagrantup.com/ajaust/boxes/sse-first-steps/versions/0.1.0)
- Go to template `cd /media/jaustar/external-ssd/virtualmachines/vagrant/own-box-template`
- Open `Vagrantfile` and refer to name of VM

    ```ruby
    Vagrant.configure("2") do |config|
        config.vm.box = "ubuntu/focal64"
        config.vm.provision :shell, path: "bootstrap.sh"

        config.vm.provider "virtualbox" do |vb|
            vb.name = "sse-first-step"
        end
    end
    ```

- Open `bootstrap.sh` to show that it will do

    ```bash
    !/usr/bin/env bash

    apt-get update
    apt-get install -y neofetch vim
    echo "export TEST_ENV_VAR=\"Hello SSE\"" >> .bashrc
    ```

    - Installs software and sets `TEST_ENV_VAR`
- `vagrant up`: Create VM
    - Image should be prebuilt
- `vagrant ssh`
    - Call `neofetch`
    - `echo $TEST_ENV_VAR` to show that variable is actually set.
- `vagrant package --base "sse-first-step" --output sse-first-step.box`: Export VM
    - File has ben upladed already
- `sse-first-steps.box` can be uploaded to [Vagrant Cloud](https://app.vagrantup.com)
- Go to directory `using-own-box/`
    - Show `Vagrantfile` that is has my uploaded image as base image
    - Skip building box `vagrant up` as it takes too long, should be prebuilt
    - `vagrant box list` shoud show my box in overview.
    - **Note** My uploaded box is called `ajaust/sse-first-step`**s**
    - **Note** The box seems to be broken all of a sudden.

## Demo: preCICE VM

- Show repository:
    - [https://github.com/precice/vm](https://github.com/precice/vm)
- Run [Premade box](https://app.vagrantup.com/precice/boxes/precice-vm)
    - `cd /media/jaustar/external-ssd/virtualmachines/vagrant/precice`
    - Create box with `vagrant init` (Done before lecture as it takes to long)
    - Start box `vagrant up`
    - Comes with a GUI
    - Preconfigured
    - Destroy in the end `vagrant destroy` since it is large (?)
- If time allows, show preCICE example
    - [Tutorial](https://precice.org/installation-vm.html#how-to-use-this)
    - [Quickstart](https://precice.org/quickstart.html)
        - Open two terminals
        - Go to `/home/vagrant/Desktop/tutorials/quickstart`
        - In one terminal go to `cpp-solid` and build solver `cmake . && make`
            - Afterwards start simulation with `./run.sh`
        - In other terminal go to `fluid-openfoam`
            - Afterwards start simulation with `./run.sh`
        - Watch simulation running
