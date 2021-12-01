---
type: slide
slideOptions:
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
  .reveal code {
    font-family: 'Source Code Pro';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# Packaging for High-Performance Computing and for you

---

## Learning goals

- What are the challenges when bringing (your) software to supercomputers?
- How to use Spack to install software.
- How to create a Spack package for your own software.

---

## Introduction 1/2

- Scientific software installation on supercomputers faces challenges:
    - Parallel architectures (MPI, OpenMP, HPX...)
    - Special hardware (accelerators, network...)
    - Greatly varying architectures (AMD, Intel, ARM...)
    - Missing dependencies (too new, too old...)
    - Admins will not/cannot install software for you

---

## Introduction 2/2

- Software should have best possible performance
    - Software needs to be **compiled** to get best performance (special libraries, compilers...)
    - Optimized compilation settings (best settings not always obvious)
    - Optimal settings depend on platform (supercomputers might be heterogenous, different generation of CPUs e.g.)

---

## Step by Step Plan

- **Goal**: Create a Spack package for HelloWorld code
- Steps:
    1. Install and configure Spack
    2. Learn how to use Spack for package management and installation
    3. Create a Spack package for our HelloWorld code
    4. Install HelloWorld code using our new package
- Code is on [GitHub](https://github.com/Simulation-Software-Engineering/HelloWorld)

---

## Spack

<img src="https://camo.githubusercontent.com/a01512f4480c4615a82f2b929789547a60d78e1f68d26be1a56e33d9258735d4/68747470733a2f2f63646e2e7261776769742e636f6d2f737061636b2f737061636b2f646576656c6f702f73686172652f737061636b2f6c6f676f2f737061636b2d6c6f676f2e737667" width=25%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

---

## Spack Introduction

- HPC-friendly package manager
    - Common scientific software included
    - No superuser rights needed
    - [Dependencies](https://spack.readthedocs.io/en/latest/getting_started.html#system-prerequisites) commonly available on Supercomputers
        - Python, git, curl...
- Deals with dependency resolution, compilation flags and **compilation**
- [Open-source project on GitHub](https://github.com/spack/spack)
- Valuable resources:
    - [Good starter guides](https://spack-tutorial.readthedocs.io/en/latest/)
    - [Extensive documentation](https://spack.readthedocs.io)
    - [Spack Slack](https://slack.spack.io/) for communication with community
- Heavily relies on concretizer [`clingo`](https://spack.readthedocs.io/en/latest/getting_started.html#bootstrapping-clingo)
    - Prefers to install newest version of packages

---

## Dependency Graph of FEniCS

<img src="https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/figs/spack/fenics-dependencies.png?raw=true" width=100%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

---

## Spack Installation

- Git repository of Python scripts

  ```bash
  git clone -b releases/v0.17 https://github.com/spack/spack.git
  ```

    - `v0.17` is currently the latest release
    - Update to newer versions using `git pull`/`git checkout -b`

- Add Spack to `PATH`

  ```bash
  . <spack_prefix>/share/spack/setup-env.sh
  ```

    - Add this command to `.bashrc` to make permanent
    - `SPACK_ROOT` points to local Spack directory

---

## Spack Configuration and Caches

- Spack heavily relies on `yaml` files
    - Take care of spaces when editing
- User configuration in `${HOME}/.spack`
- Several [other configuration scopes](https://spack.readthedocs.io/en/latest/configuration.html)
- If cache is out of date check `${HOME}/.spack/cache/`

---

## General Spack Usage

- Spack works with `spec`s (`spec`=specification)

  ```
  spack install petsc@3.16.1+mpi -shared~suite-sparse
  ```

  A spec may be more precise than just a package name.

- Loading and unloading of specs

  ```bash
  spack load petsc@3.16.1
  spack unload petsc@3.16.1
  ```

- [General syntax](https://spack.readthedocs.io/en/latest/command_index.html)

  ```bash
  spack COMMAND OPTION
  ```

---

## Common Spack Commands 1/2

- `spack find`:
    - Show packages in root environment
- `spack spec SPEC`:
    - Show packages that would be installed for specified package
- `spack install SPEC`:
    - Installs package
    - `--reuse` parameter will try to reuse installed packages
- `spack uninstall SPEC`:
    - Uninstalls package
- `spack load SPEC`:
    - Loads package into current environment
- `spack unload SPEC`:
    - Removes package from current environment

---

## Common Spack Commands 2/2

- `spack info PKG`:
    - Shows information about given package
- `spack remove SPEC`:
    - Removes a spec from current environment
- `spack gc`:
    - Garbage collection, removes all packages not needed in any environment
    - Will remove compile-time/link-time dependencies

---

## Spack Environments

- Spack organizes packages in [environments](https://spack.readthedocs.io/en/latest/environments.html)
- `spack find` shows packages in current environment
- By default one is in the "root" environment
    - The "root" environment contains all packages installed/known by Spack
- Environment has its own `view`
    - Only sees specs added to this environment
- Environments can be named for easier identification

---

## Common Spack Environments Commands

- `spack env list`:
    - List available environments
- `spack env create ENV`:
    - Create new environment with name `ENV`
- `spack env activate -p ENV`:
    - Activate environment `ENV` and prepend name to terminal
- `spack env deactivate`:
    - Deactivate a terminal (alternative: `despacktivate`)
- `spack env remove -p ENV`:
    - Remove environment `ENV`
- `spack add SPEC`:
    - Add `SPEC` to environment without installing
- `spack concretize`:
    - Concretize the specs of active environment

---

## Spack Demo 1

- Set up Spack
- Inspect environments
- Install a simple spec

---

## Spack Packaging

- By default packages reside in `${SPACK_ROOT}/var/spack/repos/builtin/packages/PACKAGENAME/`
- `package.py` inside `PACKAGENAME/` describes installation routine
- `spack edit PKG`:
    - Open given Spack package in editor
- `spack create URL`
    - Creates boilerplate package from template
    - `URL` points to some archive on can download

---

## Common Spack Package Properties

- `url`: Download URL of package
- `version(NUMBER, HASH)`: Version number and SHA256 hash

---

## Spack Demo 2

- Create package for our [CPack example](https://github.com/Simulation-Software-Engineering/HelloWorld)
    1. Create boilerplate package
    2. Add package details
    3. Verify package
    4. Model dependencies and add variants

---

## Package Managers for HPC 1/2

- Popular package managers for HPC
    - [Spack](https://spack.io/)
        - Originates from LLNL in US
    - [EasyBuild](https://github.com/easybuilders/easybuild)
        - Originates from Ghent University in Belgium


---


## Package Managers for HPC 2/2

- Package manager are a topic of great interest:

    - [European Environment for Scientific Software Installations (EESSI)](https://eessi.github.io/docs/)
        - European project
        - Focus on avoiding recompilation
    - [xSDK](https://xsdk.info/)

---

## Advanced Features

- Reproducible [builds](https://spack-tutorial.readthedocs.io/en/latest/tutorial_environments.html#building-in-environments) and [environments](https://spack-tutorial.readthedocs.io/en/latest/tutorial_environments.html)
- Own [mirrors and caches](https://spack-tutorial.readthedocs.io/en/latest/tutorial_binary_cache.html)
- [Container images](https://spack.readthedocs.io/en/latest/containers.html)
- [Chained installation](https://spack.readthedocs.io/en/latest/chain.html)
- [Stacks (build matrices)](https://spack-tutorial.readthedocs.io/en/latest/tutorial_stacks.html)
- [Software management (modules)](https://spack.readthedocs.io/en/latest/module_file_support.html)
- ...

---

## Further Reading

- [EasyBuild](https://github.com/easybuilders/easybuild)
- [EasyConfigs](https://github.com/easybuilders/easybuild-easyconfigs)
- [Spack](https://spack.io/)
- [Spack docs](https://spack.readthedocs.io/en/latest/)
- [Spack 101 tutorials](https://spack-tutorial.readthedocs.io/en/latest/)
- [archspec project](https://github.com/archspec/)

---

## Presentations

- [Spack's new Concretizer](https://archive.fosdem.org/2020/schedule/event/dependency_solving_not_just_sat/)
- [Build for your microarchitecture: experiences with Spack and archspec](https://archive.fosdem.org/2020/schedule/event/archspec/)
- [Binary packaging for HPC with Spack](https://archive.fosdem.org/2018/schedule/event/llnl_spack/)
- ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
- [Software Packages in HPC with Spack and EasyBuild](https://www.archer2.ac.uk/training/courses/200617-spack-easybuild/)