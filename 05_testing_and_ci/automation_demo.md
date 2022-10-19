# Demo: Automation

## Build Docker Container

**Note**: This is done at the end of the automation chapter.

Goal: Configure a Docker container useful for our tests. This should show...

- why we did introduce Docker before.
- a common use case of Docker.
- how to make even tinier containers than before. We use Alpine Linux here.

Steps:

- Plan: Set up a Docker container that contains
    - `python`, this should include `unittest`
    - `pip` to install packages:
        - [`black`](https://github.com/psf/black)
    - **Note**: The `pytest` package is needed later, but we will *not* install it here. The package will be our example to show that we can install extra software within the CI.
- Open the `Dockerfile` in the `examples/automation` directory
    - Image is build on top of [Alpine Linux](https://www.alpinelinux.org). Alpine is optimized to produce tiny build to be used in containers.
    - We fix the version of the base image to make sure to not run into compatibility problems.
    - We need to install Python etc. ourselves:
        - `python3`, `pip` and Python libraries/packages (`black`)
        - `pip` should be installed and used from a non-root user. Therefore, we create a user called `testuser` and change to this user
    - Password-less sudo is enabled for the user in case it would be needed to install other packages.

- Build the image locally and tag it according to my Docker Hub account name (`ajaust`)

  ```bash
  sudo docker build -t ajaust/automation-lecture .
  ```

- Inspect the image list `sudo docker image list` to point out that the container is reasonably small. During the preparation it was about 72 MB large/small. This about the size of the size of the pure Ubuntu base container:

  ```text
  ubuntu                          20.04        ba6acccedd29   3 months ago   72.8MB
  ajaust/automation-lecture       latest       a0dec678c941   5 hours ago    71.2MB
  ```

- Push image to Docker Hub such that we can use it in CI pipelines

  ```bash
  sudo docker push ajaust/automation-lecture
  ```

- Now the image can be used as `ajaust/automation-lecture` or `ajaust/automation-lecture:latest`. I did not version the uploaded container.

- Run `black` shortly locally and explain what it does.

  ```bash
  black --check .
  ```

    - It is a style checker that checks whether the Python files are formatted according to a certain standard.
    - `black --check .` will chececify dependencik files without modifying them.
    - `black` uses a lot of smileys

