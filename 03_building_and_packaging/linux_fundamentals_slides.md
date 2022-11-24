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
  .reveal code {
    font-family: 'Ubuntu Mono';
    color: orange;
  }
</style>


# Some Fundamentals of Linux Systems

---

## Introduction

- Common functionality should not be redone.
    - Examples: [C++ Standard Library](https://en.cppreference.com/w/cpp), [Python Standard Library](https://docs.python.org/3/library/), [PETSc](https://petsc.org/), [FEniCS](https://fenicsproject.org/)...
- For reusing software we need to know
    - ... where the software is located.
    - ... how to compile and link with/against.

---

## Learning Goals of This Unit

- Explain the difference between static and shared linking.
- Have an overview over common file system structure on Linux.
- Know about commonly used environment variables, how to interact with them, and how to use them.

---

## Static and Shared Linking

- Static
    - Self-contained (no external dependency)
    - Larger library/executable
    - Libraries: `libName.a`
- Shared
    - Has runtime dependencies
    - Executables can share library in memory
    - Libraries: `libName.so`

---

## Demo Static and Shared Linking

---

## Filesystem Hierarchy Standard

- Defines filesystem layout and location of common files on Linux
    <img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/03_building_and_packaging/figs/filesystem_hierarchy_structure/fig.png" width=100%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">
- [Official homepage of FHS](https://refspecs.linuxfoundation.org/fhs.shtml)

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
  echo $VARIABLE
  printenv VARIABLE
  ```

- Setting variable for a single command (bash)

  ```bash
  VARIABLE=VALUE ./COMMAND
  ```

- Setting **environment** variable

  ```bash
  export ENV_VARIABLE=VALUE
  ```

---

## Manipulating Environment Variables 2/2

- Adding additional values by colon (`:`) separated list

  Example:

  ```bash
  PATH=/home/uekermbn/bin:${PATH}
  ```

- Extra paths of user often set in `${HOME}/.bashrc`, `${HOME}/.bash_exports`,...

---

## Demo Environment Variables

---

## Some Environment Variables (C++)

- `LD_<NAME>`: Library loader related variable
    - `LD_LIBRARY_PATH`: Library paths for runtime
- `LIBRARY_PATH`: Library path for compilation (linker)
- `CPATH`, `C_INCLUDE_PATH`, `CPLUS_INCLUDE_PATH`: Include file path
- Names can vary between OS, software

---

## Paths and Environment Variables (Python)

- System-wide and user-specific
    <img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/03_building_and_packaging/figs/filesystem_paths_python/fig.png" width=75%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">
- `PYTHONPATH`: Environment variable for non-standard installation of modules/packages
    - Points to `prefix/lib/pythonX.Y/site-packages`

---

## Further Reading

- [Homepage of the FHS](https://refspecs.linuxfoundation.org/fhs.shtml)
- [Wikipedia entry of FHS](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
- [Set and list environment variables in Linux](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)
- [Ubuntu help on environment variables](https://help.ubuntu.com/community/EnvironmentVariables)
- [CPP environment variables (GCC)](https://gcc.gnu.org/onlinedocs/cpp/Environment-Variables.html)
- [Matt Godbolt “What Has My Compiler Done for Me Lately? Unbolting the Compiler's Lid”](https://www.youtube.com/watch?v=bSkpMdDe4g4)
- [Matt Godbolt “The Bits Between the Bits: How We Get to main()”](https://www.youtube.com/watch?v=dOfucXtyEsU)
- [Linux Directories Explained in 100 Seconds](https://www.youtube.com/watch?v=42iQKuQodW4)
