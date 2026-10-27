# Exercise: Containers

In this exercise, we build our own containers using Docker and Apptainer.

Deadline: **Wednesday, November 4, 2026, 9:00**

## Prerequisites

These steps take significant time, so it would be good to prepare them before the exercise session:

1. Install [Docker Engine](https://docs.docker.com/engine/)
2. Install [Apptainer](https://apptainer.org/)

If you have a machine without Linux and or without root rights, a virtual box session with Linux installed is also fine.

Use the demo from the lecture to test your installation.

## Part 1: Docker

This exercise consists of the following main steps:

1. Create a fork of the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2627/exercise-containers).
2. Setting up the `Dockerfile`
    - Base your image on Ubuntu 26.04
    - Install `fastfetch` inside the container
    - Create a file called `testfile` that contains `USERNAME` (your GitLab-SIM username). Using a `COPY`, copy this file to a directory called `/testfiles` inside the container.
    - Set the environment variable `ENV_TEST_VARIABLE` inside the container.
    - Define a default run command for the container.
    - Test the new container
3. Manually run `fastfetch` or `neofetch` in a terminal inside the container at runtime and take a screenshot
4. Create a merge request containing your changes.

### 1. Create a Fork

Fork and clone the repository mentioned above. The repository initially contains a `README.md` and an empty file called `Dockerfile`. Please also create a new branch in your fork to work on the task.

### 2. Setting up the `Dockerfile`

- Currently, the [`Dockerfile`](https://docs.docker.com/reference/dockerfile/) is empty. Edit the file such that a container image with the following properties is built:
    - Your virtual machine should be based on the [`alpine:latest` image](https://hub.docker.com/_/alpine).
        - Alternatively, you can use the (larger) [`ubuntu:26.04` image](https://hub.docker.com/_/ubuntu).
    - Install `fastfetch` (Alpine) or `neofetch` (Ubuntu).
    - **Note:** In the `Dockerfile` you do not have to prefix commands such as `apt` with `sudo` since the script is executed with superuser rights.
    - Create a new file with the name `testfile` and add it to the repository. The file should contain your `USERNAME` as text. Add the file to your container and place it in the directory `/testfiles` using `COPY`.
    - Set the environment variable `ENV_TEST_VARIABLE` to have the value of your `USERNAME`.
    - Make sure that the default command to be executed when running the container is `/bin/bash`.
- Test your Docker container locally. Are all variables set and files available?
    - **Note:** If you rebuild your container often, you might end up with dangling containers. You can remove them (together with any unused images, containers, or objects) with [`docker [image|container|system] prune`)](https://docs.docker.com/engine/reference/commandline/system_prune/) depending on what you want to remove. To delete everything unused: `docker system prune`.

Hints for installing `fastfetch` on Alpine:

- Update the cache with `apk update`
- Install fastfetch with `apk add fastfetch`
- Run fastfetch with `fastfetch`

To install `fastfetch` on Ubuntu, do `apt update` and `apt install fastfetch`.

### 3. Running neofetch and Taking a Screenshot

- Go into your running container.
- Clear the terminal using `clear` and run fastfetch/neofetch as before.
- Take a screenshot and save it as `screenshot-docker-USERNAME.png`.

### 4. Creating a Merge Request

- Open a merge request in the GitLab Repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2627/exercise-containers).
    - As title, choose "[`USERNAME`] Docker Container Recipe".
    - Make sure all files are up to date (`testfile`, `Dockerfile`).
    - Attach the screenshot ("Attach a file") that you made in the previous step.
    - Add the label `Docker` label to the merge request.
    - Double-check that all files are in the repository and up to date.
    - If everything looks good, create the merge request.

## Part 2: Singularity/Apptainer

Rebuild the above Docker container as an [Apptainer container](https://apptainer.org/docs/user/latest/). Create a new merge request for this in the GitLab repository ["Exercise Containers"](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2627/exercise-containers). Please choose the `Apptainer` label when creating the merge request.

**Important:** only add the Apptainer recipe to the merge request, and not the container image file.
