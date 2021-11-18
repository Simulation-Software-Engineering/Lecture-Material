
MlideOptions:
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


# System paths and libraries

## Environment Variables, Paths, Libraries and How to Find Them

---

## Introduction

- Common functionality should not be redone the whole time
    - Examples: C++ standard library, Python NumPy
- Software needs to be findable
- We had this for Python already

---

## Shared libraries

- Code/functionality shared between executables
    - Often needed functionality shared by many applications stored at one place
    - Examples: `libc.so`

---

## Filesystem Hierarchy Standard (FHS)

- Defines filesystem layout and location of common files on Linux
- `/`: Primary root
- `/bin`, `/lib`, `/include`, `/var`, `/etc`, `/home`...
    - First hierarchy level containing essential tools and configuration of the OS
- `/usr/` with subdirectories `/usr/lib`, `/usr/lib64`, `/usr/lib32`,
    - Second hierarchy level containing shareable user data (read-only)
- `/usr/local`
    - Third level hierachy level containing local data specific to host
- There are many additional directories
- Similar structure mirrored under `usr` and `/usr/local`
- [Official homepage of FHS](https://refspecs.linuxfoundation.org/fhs.shtml)

---

## Standard Paths and Environment Variables (general)

- `HOME` or `~`
- `PWD`
- `PATH`
- `CPATH`
- `LD_LIBRARY_PATH`
- `MANPATH`
- System paths often set from `/etc/profile` and `/etc/bashrc` or `/etc/bash.bashrc`
- Extra paths set by user often by `${HOME}/.bashrc`, `${HOME}/.bash_exports`, `${HOME}/.bash_profile`
- Show content of paths via

  ```bash
  echo $VARIABLENAME
  printenv VARIABLENAME
  ```

  e.g.

  ```bash
  echo $PATH
  printenv PATH
  ```

---

## Manipulating Environment Variables

- Setting variable for a single command

  ```bash
  ENVVARIABLE=VALUE ./COMMAND
  ```

- Adding additional values by colon (`:`) separated list

  ```bash
  PATH=ADDITONALPATH:${PATH}
  ```

  ```
  PATH=/home/jaustar/bin:${PATH}
  ```

---

## Important Paths and Environment Variables (General)

---

## Important Paths and Environment Variables (C++)

---

## Standard Paths and Environment Variables (Python)

- `PYTHONPATH`

---

## Tools for Finding Libraries and Packages

- `ldconfig`
- `pkgconfig`
    - `pkg-conf`
    - `pkg-config`

---

## ldconfig

- Generate links and cache to libraries
- Can be used to inform system about new libraries at non-standard location
    - Useful for your own codes/environments
    - Usually automatically run by system's package manager (`apt`, `yum` etc.)

---

## pkgconfig

---