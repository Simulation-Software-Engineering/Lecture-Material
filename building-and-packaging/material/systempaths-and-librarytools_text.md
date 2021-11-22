# Git -- the standard version control system


## Environment Variables, Paths and How to Find Them

| Duration | Format | Material |
| --- | --- | --- |
| 20 minutes | Lecture | [`systempaths-and-librarytools_slides.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/systempaths-and-librarytools_slides.md) |

## Static vs/ Shared Libraries/Executables

- Whether shared or static is preferable depends on use case.
    - Shared approach makes modes more lightweight and allows for sharing of library in memory. Additionaly, it allows updating shared libraries to patch bugs, for example.
    - Static makes code self-contained. It is easier to move to other computers at the cost of larger files.
- Some programming languages, e.g., Go prefers static binaries by default.

### Demo

- Show example from `examples/shared-and-static-c++/`
    - Simple hello world program
- Run `ldd` on `main-static` and `main-shared`
- Run `ls -lah` to show different executable sizes
- `main-static` could be copied over to

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

## Filesystem Hierarchy Standard (FHS)

- Where are files stored by default?
    - **Linux**: This is defined in the Filesystem Hierarchy Standard.
- Defines filesystem layout
- `/`: Primary root
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
- `/usr/`: Second hierarchy level containing shareable user data (read-only)
    - `/usr/bin/`, `/usr/sbin/`: Non-essential binaries to be used by user
    - `/usr/lib/`
    - `/usr/include/`
    - `/usr/local`: Third level hierachy level containing local data specific to host
- ...and more directories. Details and meaning can be found in the reference (see below).
- **Important** for us/our software normally
    - `/usr/bin/`
    - `/usr/lib/`
    - `/usr/include/`
- **Note*: Some parts of the structure should be reproduced/respected by own software/libraries. In the installation prefix one should create structure like `prefix/bin`, `prefix/lib`, `prefix/include`... Exact structure depends on own software. Does it have binaries, does it have includes etc.

### Demo (Filesystem Hierarchy Standard)

- If time permits, show file structre in a terminal.

## Standard Paths and Environment Variables (general)

- (Environment) Variable can be used in scripts
    - See examples earler where we used `${HOME}`.
- Environment variable also exist on Windows. They hide somewhere in the advanced system setting.

### Demo (Environment variables)

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

## Environment variables

- Variables of local scope (to one process)
- Environment variables (set with `export` or `setenv`) have (more) global scope as they are inherited by child processes.
- System's environment variables often set from `/etc/profile` and `/etc/bashrc` or `/etc/bash.bashrc` as they are typically sourced by the user's shell.
    - Processes started via GUI etc. are also connected to some process attached to a shell and thus inherit environment variables.
- Extra paths of user often set in `${HOME}/.bashrc`, `${HOME}/.bash_exports`, `${HOME}/.bash_profile`...
    - Some file that needs to be sourced when a shell is opened.
- Some important variables for **C++** on Linux
    - Mainly about finding includes, libraries and setting compilation flags
    - `CC`, `CXX`, `CPP` etc. compilers
    - `CFLAGS`, `CXXFLAGS`, `CPPFLAGS` etc. compiler flags
    - `LD_<NAME>` are (library) loader variables. Commonly used `LD_LIBRARY_PATH` which points to shared libraries.
    - `CPATH`, `C_INCLUDE_PATH`, `CPLUS_INCLUDE_PATH` include file paths
    - There are more variables. Their name and meaning also depend on the toolchains used (GCC, LLVM etc.)
- Some important variables for **Python** on Linux
    - System-wide scripts in `/usr`
    - Filesystem is mirrored in `${HOME}/.local/` for local (user-space) installations. That applies to Python code installed with `setup.py` or via `pip`, for example.
    - Python does some versioning of modules/packages by the directory structure as for libraries they use `prefix/lib/pythonX.Y` where `X` is the major and `Y` the minor version of Python.
    - `PYTHONPATH` can be set for packages that are not installed in non-standard locations. This allows to `import` packages.
    - `PATH` as for all executables.
- **Note**: Lower case names = local variables or non-constant values


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

- Variables may have more than one value. In this case different values are seperated by a colon `:`

## Interlude

- It is important/helpful to know where libraries and binaries live.
    - This is especially true for languages that compilation.
    - Helps with debugging problems (library not found, wrong executable called...)
- Finding all libraries and approriate options to link against them is tedious -> Helper tools:
    - `ldconfig`
    - `pkg-config`


## ldconfig

- Manages list of installed shared libraries.
- Can and should be used instead of `LD_LIBRARY_PATH`.
- However:
    - Needs root rights `sudo`
    - Not straight forward if one has same library in many versions (different version number, different compiler options) etc. Thus, this environment variable (and others) are commonly used in scientific computing.

## pkg-config

- At least two implementations
    - `pkgconfig`
    - `pkgconf`
  but should work the same.
- Can be used to obtain compilation and linking flags for a library.
- System-wide files stored system-dependent: `/usr/lib/pkgconfig/`, `/usr/lib/x86_64-linux-gnu/pkgconfig/`,...

### pkg-config file

Fields:

- Name: Name. Can deviate from `pc` file name.
- Description: Description
- URL: URL of project
- Version: Version of package. Use semantic versioning MAJOR.MINOR.PATCH. Everything but numbers can create unexpected results
- Requires: List of dependencies. Versions can be specified using >, <, =,  <= or >=.
- Requires.private: Private list of dependencies.
- Conflicts: Conflicting packages. Packages can be specified with version number and also several times to create version ranges
- Cflags: Compiler flags for the software package or its dependencies that do not support pkg-config.
- Libs: Link flags for this package and dependencies that do not support pkg-config.
- Libs.private: Link flags for private dependencies that do not support pkg-config.
- Dependencies that support pkg-config should be added to Requires and Requires.private

One can define local variable to be used in the file. In the example on the slides, `prefix`, `exec_prefix`, `includedir`, and `libdir` are local variables that can be used be dereferencing them `${variablename}`.

### Demo: Ubuntu

- Show pkg-config files in `/usr/lib/x86_64-linux-gnu/pkgconfig/`, for example.

### Demo: PETSc

- Code in `examples/pkg-config/`
    - Creates executable printing the PETSc version and also initialized and destroys PETSc.
    - `petsc-systempath`: Compiles using hand set options. Need to set include manually. `-lpetsc` is found as it is installed in a system's path that is known to `ldconfig`.
    - `petsc-pkg-config`: Compiles by obtaining compile options from  `pkg-config`
- This might be too confusing?!
- My machine has PETSc installed from the Ubuntu package repository (via `apt`)

  ```bash
  > pkg-config --libs PETSc
  -L/usr/lib/petscdir/petsc3.12/x86_64-linux-gnu-real/lib -lpetsc_real
  > pkg-config --modversion PETSc
  3.12.4
  ```

- Compile code twice.
    1. Compile usind preinstalled PETSc library

       ```
       > module purge
       > make all
       > ./petsc-systempath
       Using PETSc version: 3.12.4
       > ./petsc-pkg-config
       Using PETSc version: 3.12.4
       > make clean
       > module load PETSc/3.16.1-opt-sse-lecture
       > make
       > ./petsc-systempath
       Using PETSc version: 3.12.4
       > ./petsc-pkg-config
       Using PETSc version: 3.16.1
       ```

       If there is time, check output of

       ```bash
       ldd petsc-systempath | grep petsc
       ldd petsc-pkg-config | grep petsc
       ```

       to see that the executable are indeed linked to different libraries.

- Can also load `module load PETSc/3.16.1-opt-sse-lecture` which sets rather minimal environment variables, but still allows compilation using pkg-config. Does not set `LIBRARY_PATH` so new PETSc is not found during compile time.
    - Compilation of `petsc-systempath` still use old PETSc version because it does not find the newer version.

## Further reading

### References

- [Official homepage of the Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/fhs.shtml)
- [Wikipedia entry of the Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
- [How to on working with environment and shell variables](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)
- [Ubuntu help on environment variables](https://help.ubuntu.com/community/EnvironmentVariables)
- [Wikipedia on pkg-config](https://en.wikipedia.org/wiki/Pkg-config)
- [pkg-config project homepage](https://www.freedesktop.org/wiki/Software/pkg-config/)
- [Guide to pkg-config](https://people.freedesktop.org/~dbn/pkg-config-guide.html)
- [CPP environment variables (GCC)](https://gcc.gnu.org/onlinedocs/cpp/Environment-Variables.html)
- ["using ldconfig and ld.so.conf versus LD_LIBRARY_PATH" on Stack Overflow](https://unix.stackexchange.com/questions/425251/using-ldconfig-and-ld-so-conf-versus-ld-library-path)

### Talks and videos

- [Matt Godbolt “What Has My Compiler Done for Me Lately? Unbolting the Compiler's Lid”](https://www.youtube.com/watch?v=bSkpMdDe4g4)
- [Matt Godbolt “The Bits Between the Bits: How We Get to main()”](https://www.youtube.com/watch?v=dOfucXtyEsU)
- [Linux Directories Explained in 100 Seconds](https://www.youtube.com/watch?v=42iQKuQodW4)