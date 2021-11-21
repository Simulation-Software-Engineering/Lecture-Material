# Git -- the standard version control system


## Environment Variables, Paths and How to Find Them

| Duration | Format | Material |
| --- | --- | --- |
| 20 minutes | Lecture | [`systempaths-and-librarytools_slides.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/systempaths-and-librarytools_slides.md) |

## Filesystem Hierarchy Standard (FHS)

- Defines filesystem layout
- `/home` contains user's home directories
- `/etc` contains system-wide configuration
    - "et cetera" (Bell lab manual), "editable text confiuration"
- `/bin` directories refer to executables important for the system/OS
- `/sbin` directories refer to executables important for the system/OS to be executed by the super user
- `/boot`: Contains files to boot the system such as bootloader files or the kernel
- `/opt`: Optional software
- `/tmp`: Temporary files. Wiped at reboot
- `/dev`: Device files, interact with devices as if they were files
- `/var`: Variable files that change during the OS running
- `/proc`: Virtual filesystem keeping track of processes.
- `/usr/`
    - `/usr/bin/`, `/usr/sbin/`: Non-essential binaries to be used by user
    - `/usr/lib/`
    - `/usr/include/`
    - `/usr/local`
        - More or less same structure again
        - FIles
- ...and more directories. Details and meaning can be found in the reference (see below).
- **Important** for us/our software normally
    - `/usr/bin/`
    - `/usr/lib/`
    - `/usr/include/`
## Standard Paths and Environment Variables (general)

### Demo

- Boot up a VM (sse-docker-box)
- Run the command `env` or `printenv` in a terminal. It will show all set environment variables and their value
    - `printenv` can also print the value of a certain variable `printenv USER` (can be used instead of `echo $USER`)
    - `env` has extra features for setting environment variables
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


### Example

```
$ ls -lah
total 2.4M
drwxrwxr-x 2 jaustar jaustar 4.0K Nov 19 19:00 .
drwxrwxr-x 4 jaustar jaustar 4.0K Nov 19 18:43 ..
-rw-rw-r-- 1 jaustar jaustar  162 Nov 19 15:34 CMakeLists.txt
-rw-rw-r-- 1 jaustar jaustar  151 Nov 19 18:52 Makefile
-rwxrwxr-x 1 jaustar jaustar  17K Nov 19 18:52 main-shared
-rwxrwxr-x 1 jaustar jaustar 2.3M Nov 19 18:52 main-static
-rw-rw-r-- 1 jaustar jaustar   95 Nov 19 18:50 main.cpp
```

## Environment variables


### Demo (Environment Variables)

- Use script that uses the environment variable in `lecture-material/building-and-packaging/material/scripts` called `print_my_environment_variable.sh`
    - The script checks whether the environment variable `MY_ENV_VARIABLE` is checked. If the variable exists, the script will print the variable's value to the screen. Otherwise, the script states that the variable does not exist.
- Show script
    1. Show what happens if variable is empty

       ```bash
       $ ./print_my_environment_variable.sh
       The environment variable MY_ENV_VARIABLE is empty (zero length)
       ```

    2. Set the variables value just for the one command. This is probably a feature tied to using **bash**.

       ```bash
       $ MY_ENV_VARIABLE="Hi students" ./print_my_environment_variable.sh
       The environment variable MY_ENV_VARIABLE is set to
         Hi students
       ```

    3. Show that the variable is indeed empty again

       ```bash
       $ ./print_my_environment_variable.sh
       The environment variable MY_ENV_VARIABLE is empty (zero length)
       ```

    4. We can set the variable in the terminal, but without export it is not shared with child processes

       ```bash
       $ MY_ENV_VARIABLE="Hi students"
       $ echo $MY_ENV_VARIABLE
       test
       $ ./print_my_environment_variable.sh
       The environment variable MY_ENV_VARIABLE is empty (zero length)
       ```

    5. Permanently set the value for the terminal

       ```bash
       $ export MY_ENV_VARIABLE="Hi students"
       $ ./print_my_environment_variable.sh
       The environment variable MY_ENV_VARIABLE is set to
         Hi students
       ```


## Interlude

- It is important/helpful to know where libraries and binaries live.
    - This is especially true for languages that compilation.
    - Helps with debugging problems (library not found, wrong executable called...)
- Finding all libraries and approriate options to link against them is tedious -> Helper tools:
    - `ldconfig`
    - `pkg-config`


## ldconfig

## pkg-config

At least two implementations
- `pkgconfig`
- `pkgconf`



### Example: Own pkg-config application


### Example: PETSc (?)

- This might be too confusing
- My machine has PETSc installed from the Ubuntu package repository (via `apt`)

  ```bash
  > pkg-config --libs PETSc
  -L/usr/lib/petscdir/petsc3.12/x86_64-linux-gnu-real/lib -lpetsc_real
  > pkg-config --modversion PETSc
  3.12.4
  ```

## Further reading


### References

- [Official homepage of the Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/fhs.shtml)
- [Wikipedia entry of the Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
- [How to on working with environment and shell variables](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)
- [Ubuntu help on environment variables](https://help.ubuntu.com/community/EnvironmentVariables)
- [Wikipedia on pkg-config](https://en.wikipedia.org/wiki/Pkg-config)
- [pkg-config project homepage](https://www.freedesktop.org/wiki/Software/pkg-config/)
- [Guide to pkg-config](https://people.freedesktop.org/~dbn/pkg-config-guide.html)

### Talks and videos

- [Matt Godbolt “What Has My Compiler Done for Me Lately? Unbolting the Compiler's Lid”](https://www.youtube.com/watch?v=bSkpMdDe4g4`)
- [Matt Godbolt “The Bits Between the Bits: How We Get to main()” ](https://www.youtube.com/watch?v=dOfucXtyEsU)
- [ Linux Directories Explained in 100 Seconds ](https://www.youtube.com/watch?v=42iQKuQodW4)