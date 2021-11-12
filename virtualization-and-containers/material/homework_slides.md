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

# Homework

## (Virtualization / Containers)

---

## Details

- **Deadline**: Before exercise on 11 November 2021
- What to do?
    - Install VirtualBox and Vagrant
    - Install Docker on your machine or in a VM
- Please follow the manuals on the homepage
    - [VirtualBox](https://www.virtualbox.org/)
    - [Vagrant](https://www.vagrantup.com/)
    - [Docker Engine](https://docs.docker.com/engine/)


---

## VirtualBox and Vagrant

- Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/)
    - Verify that the installation was successful by creating the Vagrant example from the lecture:

        - Navigate to a directory of your choice

        ```bash
        vagrant init hashicorp/bionic64
        vagrant up
        ```

        - Go into the VM `vagrant ssh` and verify the content of the `/vagrant` directory.
        - Check in the VirtualBox manager that the VM is active.
        - Leave the SSH session (type `exit` and press `Enter` or use the shortcut `CTRL+D`)
        - Destroy the VM `vagrant destroy`

**Note**: Please install Vagrant from the homepage so that it is not too old.

---

## Install Docker

- Install [Docker Engine](https://docs.docker.com/engine/)
    - You can install it on your machine or in a VM
    - Check that your installation successful by running

    ```bash
    docker run hello-world
    ```

      You might have to prefix a `sudo` command. This depends on your Docker configuration.

    - You should see a message that starts with

    ```bash
    Hello from Docker!
    This message shows that your installation appears to be working correctly
    ```
