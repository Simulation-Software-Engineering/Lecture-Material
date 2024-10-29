# Singularity Demo

## Demo: Run prebuilt containers

- `apptainer pull docker://precice/precice`
    - Obtain existing Docker image, convert it, and store it as `precice_latest.sif`
- `apptainer shell precice_latest.sif`
    - Run shell in container
    - `whoami` will show same user as I am on the computer
- `apptainer exec precice_latest.sif precice-tools --version`
    - Run command in container
- Show the mounted filesystems and hardware access.
- Show that we cannot run things as root.
- Note that images are executable by default: `./precice-latest.sif`

## Demo: Build own containers

- Recipe `lolcow.def`

    ```Singularity
    BootStrap: docker
    From: ubuntu:22.04

    %post
    apt-get -y update
    apt-get -y install cowsay lolcat

    %environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

    %runscript
    date | cowsay | lolcat
    ```

- Show file `lolcow.def` content
- `apptainer build testimage lolcow.def`
- Creates image which is identical to the prebuilt image
