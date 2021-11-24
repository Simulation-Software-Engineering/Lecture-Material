# Git -- the standard version control system


## Environment Variables, Paths and How to Find Them

| Duration | Format | Material |
| --- | --- | --- |
| 20 minutes | Lecture | [`systempaths-and-librarytools_slides.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/systempaths-and-librarytools_slides.md) |

## Filesystem Hierarchy Standard (FHS)

- Defines filesystem layout
- `/home` contains user's home directories
- `/etc` contains system-wide configuration
- `/bin` directories refer to executables
- `/boot` contains bootloader files
- `/usr/bin/`
    - `/usr/lib/`
    - `/usr/include/`
- **Impoortant** for us/our software normally
    - `/usr/bin/`
    - `/usr/lib/`
    - `/usr/include/`



## Standard Paths and Environment Variables (general)

### Demo

- Boot up a VM (sse-docker-box)
- Run the command `env` in a terminal. It will show all set environment variables and their value
- Note that some values/environment variables are not standard since it sources my own `.bashrc`.
    - `EDITOR=vim`
    - `CODIPACKDIR=/opt/CoDiPack`
    - `_JAVA_OPTIONS=-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true`


Example output:

```bash
> env
SHELL=/bin/bash
HISTSIZE=5000
LC_ADDRESS=C.UTF-8
LC_NAME=C.UTF-8
SSH_AUTH_SOCK=/tmp/ssh-Fn5gmLhJcmgC/agent.1645
LC_MONETARY=C.UTF-8
SSH_AGENT_PID=1646
DISTCC_HOSTS=deepthought/5,lzo,cpp
EDITOR=vim
PWD=/home/vagrant
LOGNAME=vagrant
XDG_SESSION_TYPE=tty
MOTD_SHOWN=pam
HOME=/home/vagrant
LC_PAPER=C.UTF-8
LANG=C.UTF-8
SSH_CONNECTION=10.0.2.2 52046 10.0.2.15 22
XDG_SESSION_CLASS=user
TERM=xterm-256color
LC_IDENTIFICATION=C.UTF-8
USER=vagrant
SHLVL=1
LC_TELEPHONE=C.UTF-8
LC_MEASUREMENT=C.UTF-8
XDG_SESSION_ID=3
XDG_RUNTIME_DIR=/run/user/1000
PS1=\u\[\033[1;34m\]@\h\[\033[0m\]:\[\033[0;32m\]\w\[\033[0;32m\]$(__git_ps1)\n└─(\[\033[1;32m\]\t, $(ls -1 | wc -l | sed 's: ::g') files, $(ls -sh | head -n1 | sed 's/total //')b\[\033[1;37m\]\[\033[0;32m\])\342\224\200>\[\033[0m\]
SSH_CLIENT=10.0.2.2 52046 22
LC_TIME=C.UTF-8
OMP_NUM_THREADS=1
VAGRANT_HOME=/media/jaustar/external-ssd/virtualmachines/vagrant/.vagrant.d/
CODIPACKDIR=/opt/CoDiPack
LC_COLLATE=C
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/home/vagrant/bin:/home/vagrant/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/vagrant/bin/ubuntu-focal
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
SSH_TTY=/dev/pts/0
_JAVA_OPTIONS=-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
LC_NUMERIC=en_US.UTF-8
_=/usr/bin/env
```

## Shared libraries

- Show example
- Run `ldd` on some code that uses shared libraries.
    - Create simple C++ code that links against the standard library? "Hello world?"
    - Maybe use an example from BU.

## Environment variables


### Demo (Environment Variables)

- Use script that uses the environment variable in `lecture-material/building-and-packaging/material/scripts` called `print_my_environment_variable.sh`
    - The script checks whether the environment variable `MY_ENV_VARIABLE` is checked. If the variable exists, the script will print the variable's value to the screen. Otherwise, the script states that the variable does not exist.
- Show script
    1. Show what happens if variable is empty

       ```bash
       ./print_my_environment_variable.sh
       ```

    2. Set the variables value just for the one command

       ```bash
       MY_ENV_VARIABLE="Hi students" ./print_my_environment_variable.sh
       ```

    3. Show that the variable is indeed empty again

       ```bash
       ./print_my_environment_variable.sh
       ```

    4. Permanently set the value for the terminal

       ```bash
       export MY_ENV_VARIABLE="Hi students"
       ./print_my_environment_variable.sh
       ```

## Further reading


### References

- [Official homepage of the Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/fhs.shtml)
- [Wikipedia entry of the Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)


### Talks

- [Matt Godbolt “What Has My Compiler Done for Me Lately? Unbolting the Compiler's Lid”](https://www.youtube.com/watch?v=bSkpMdDe4g4`)
- [Matt Godbolt “The Bits Between the Bits: How We Get to main()” ](https://www.youtube.com/watch?v=dOfucXtyEsU)