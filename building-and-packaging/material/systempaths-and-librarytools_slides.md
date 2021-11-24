---
SlideOptions:
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
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>


# System Paths, Libraries, and How to Use Them

---

## Introduction

- Common functionality should not be redone the whole time
    - Examples: [C++ Standard Library](https://en.cppreference.com/w/cpp), [Python Standard Library](https://docs.python.org/3/library/), [PETSc](https://petsc.org/), [FEniCS](https://fenicsproject.org/)...
- For reusing software we need to know
    - where the software is located
    - how to compile and link with/against

---

## Static and shared libraries

- Static
    - Libraries: `libName.a`
    - Self-contained code/libraries
    - Larger library/executable
- Shared
    - Libraries: `libName.so`
    - Shared code must be installed and accessible
    - Executables can share library in memory

---

## Filesystem Hierarchy Standard

- Defines filesystem layout and location of common files on Linux

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/add-overview-systempaths-librarytools/building-and-packaging/material/figs/filesystem_hierarchy_structure/fig.png" width=100%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- [Official homepage of FHS](https://refspecs.linuxfoundation.org/fhs.shtml)

**TODO** Set image link to the GitHub main branch before merging.

---

## Some Environment Variables

- `HOME` or `~`: User's home directory
- `PWD`: Current working directory
- `PATH`: Locations of executables on system
- `LC_<NAME>`: [Locales](https://wiki.archlinux.org/title/locale)
- `LANG`: Systems' language
- System variables often set from `/etc/profile` and `/etc/bashrc` or `/etc/bash.bashrc`

---

## Manipulating Environment Variables 1/2

- Show content of variables via

  ```bash
  echo $VARIABLENAME
  printenv VARIABLENAME
  ```

- Setting variable for a single command (bash)

  ```bash
  ENVVARIABLE=VALUE ./COMMAND
  ```

- Setting **environment** variable

  ```bash
  export ENVVARIABLE=VALUE
  ```

---

## Manipulating Environment Variables 2/2

- Adding additional values by colon (`:`) separated list

  Example:

  ```bash
  PATH=/home/jaustar/bin:${PATH}
  ```

- Extra paths of user often set in `${HOME}/.bashrc`, `${HOME}/.bash_exports`,...

---

## Some Environment Variables (C++)

- `LD_<NAME>`: Library loader related variable
    - `LD_LIBRARY_PATH`: Library paths for runtime
- `LIBRARY_PATH`: Library path for compilation (linker)
- `CPATH`, `C_INCLUDE_PATH`, `CPLUS_INCLUDE_PATH`: Include file path
- Names can vary beween OS, software
- Variables should be manipulated carefully

---

## Paths and Environment Variables (Python)

- System-wide:

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/add-overview-systempaths-librarytools/building-and-packaging/material/figs/filesystem_paths_python/fig.png" width=100%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- User-specific

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/add-overview-systempaths-librarytools/building-and-packaging/material/figs/filesystem_paths_python/fig-user-level.png" width=100%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- `PYTHONPATH`: Environment variable for non-standard installation of modules/packages
    - Points to `prefix/lib/pythonX.Y/site-packages`

**TODO** Set image link to the GitHub main branch before merging.
---

## Working with Libraries

- How to find libraries?
    - Paths?
- How to incorporate libraries when compiling?
    - Compileflags?

---

## Tools for Finding Libraries and Packages

- [ldconfig](https://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html)
    - Managing paths of library loader
- [pkg-config]((https://www.freedesktop.org/wiki/Software/pkg-config/))
    - Manage package information such as
        - Version
        - Metadata
        - Compile and link flags


---

## ldconfig

- Generates links and cache of libraries and their locations
- Can be used to inform system about new libraries at non-standard location
    - Useful for your own codes/environments
    - Usually automatically run by system's package manager (`apt`, `yum` etc.)
- `LD_LIBRARY_PATH` commonly used, but use with care

---

## ldconfig - Usage

- Configuration tool for library loader
- Tell `ldconfig` about library in non-standard location

  ```bash
  sudo ldconfig PATHTOLIBRARY
  ```

    - `PATHTOLIBRARY` points to directory containing `NAME.so` file

- Note: One can bake search paths in executables (rpath)

---

## pkg-config

- Collects metadata of installed software
- Different implementations
    - `pkgconf`, `pkg-config`...
- Provides information about packages
    - Package location
    - Compile options
    - Link options

---

## `pc` File Layout

```pkg-config
# Comment
local_variable=value
another_variable=${value}/lib

Name: ...
Description:
URL: ...
Version: ...
Requires: ...
Requires.private: ...
Conflict: ...
Cflags: ...
Libs: ...
Libs.private: ...
```

- Options can be left out if not needed

---

## pc File of PETSc

```pkgconfig
prefix=/home/jaustar/software/petsc/3.16.1-opt
exec_prefix=${prefix}
includedir=${prefix}/include
libdir=${prefix}/lib
ccompiler=mpicc
cflags_extra=-fPIC -Wall -Wwrite-strings -Wno-strict-aliasing -Wno-unknown-pragmas -fstack-protector -fvisibility=hidden -O3
cflags_dep=-MMD -MP
ldflag_rpath=-Wl,-rpath,
cxxcompiler=mpicxx
cxxflags_extra=-Wall -Wwrite-strings -Wno-strict-aliasing -Wno-unknown-pragmas -fstack-protector -fvisibility=hidden -O3  -fPIC -std=gnu++17
fcompiler=mpif90
fflags_extra=-fPIC -Wall -ffree-line-length-0 -Wno-unused-dummy-argument -O3

Name: PETSc
Description: Library to solve ODEs and algebraic equations
Version: 3.16.1
Cflags:   -I${includedir}
Libs: -L${libdir} -lpetsc
Libs.private: -L/usr/lib/x86_64-linux-gnu/openmpi/lib -L/usr/lib/gcc/x86_64-linux-gnu/9 -llapack -lblas -lm -lX11 -lstdc++ -ldl -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi -lgfortran -lm -lgfortran -lm -lgcc_s -lquadmath -lpthread -lquadmath -lstdc++ -ldl
```

---

## pc File Location

- Common options
    - `--modversion`: Module/package version
    - `--libs`: Link flags
    - `--cflags`: compilation flags
- Often stored in `prefix/lib`, but no guarantee
- System-wide files stored system-dependent
- `PKG_CONFIG_PATH`: (Extended) Search path for pkg-config files
    - Must point to directory containting `pc` file

---

## Using pkg-config

- On command line

  ```bash
  gcc `pkg-config --cflags --libs LIBRARYNAME` SOURCEFILE
  ```

- In Makefile: As above or

  ```makefile
  CFLAGS+=$(shell pkg-config --cflags --libs LIBRARYNAME)
  gcc $(CFLAGS) SOURCEFILE
  ```

---

## Summary and Outlook

- Meaning of environment variables and how to work with them
- Filesystem Hierarchy Standard
- Common tools to work with libraries
    - ldconfig
    - pkg-config
- Use build system (generators) ([autotools](https://airs.com/ian/configure/), [CMake](https://cmake.org/), ...) to set variables and create pc files