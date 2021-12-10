# Singularity Demo

- Back story
    - Created at Lawrence Berkeley National Laboratory but now developed by SyLabs
    - Based on Go
- Container solution with high-performance computing in mind
    - "Mobility of compute", "Bring your own environment"
        - Mobility of your compute environment
        - Normally immutable images
    - Integration in scheduling systems
    - Runs in *user-space* (no root privilege escalation)
    - Direct network and (some) hardware access (GPUs, accelerators)
    - Mounts common/important directories
    - Show text-based file format. Is similar to Docker
        - Building is without layers (hit or miss)
        - Images can be based on Docker images. This is nice to prebuild parts of the image as Docker image since Singularity's format is not layer based. This means you have to rebuilt from scratch if it fails.
    - Small runtime penalty.
- Nowadays available on many HPC platforms
- Common commands

## Demo: Run prebuilt containers

- `singularity pull library://lolcow`
    - Obtain existing container image and store it as `lolcow_latest.sif`
- `singularity pull lolcow_docker.sif docker://sylabsio/lolcow`
    - Pulls docker image, converts it and stores it as lolcow_docker.sif
- `singularity shell lolcow_latest.sif`
    - Run shell in container
    - `whoami` will show same user as I am on the computer
- `singularity exec lolcow_latest.sif cowsay moo`
    - Run command in container
- Show the mounted filesystems and hardware access.
- Show that we cannot run things as root.
- Note that images are executable by default

## Demo: Build own containers

- Recipe `singularity-example.def`

    ```Singularity
    BootStrap: library
    From: ubuntu:16.04

    %post
            apt-get -y update
            apt-get -y install fortune cowsay lolcat

    %environment
            export LC_ALL=C
            export PATH=/usr/games:$PATH

    %runscript
            fortune | cowsay | lolcat
    ```

- Go to `/media/jaustar/external-ssd/singularity/singularity-examples/build-image`
- Show file `singularity-example.def` content
- `sudo singularity build testimage singularity-example.def`
    - Point out that sudo is needed
- Creates image which is identical to the prebuilt image
