# Debian packages and packaging for HPC

*Learning goals*

- How to automatize compilation of codes.
- How to easily add your code to package managers for
    - reproducibility
    - easier user compilation
- Reproducible builds/environments?

## Quiz (optional)

- Who is using containers or virtualization technologies?!
- Which tools do you use/know?

## General package creation / Debian packages

| Duration | Format |
| --- | --- |
| 15 minutes | Slides |

- `deb` packages are common in the Linux world
    - Used by Debian its derivatives (such as Ubuntu)
- **TODO** Figure out how to build Debian packages
- Can be used to package packages of all kind

## General package creation / Debian packages - Example

| Duration | Format |
| --- | --- |
| 5 minutes | Demo |


## Package managers for HPC (but also for you)

| Duration | Format |
| --- | --- |
| 20 minutes | Slides |

- Challenge:
    1. Software should be easy to install
    2. I want high performance on a super computer -> Compile software with platform dependent optimization (`-march=native`). Might have vendor-specific libraries (MPI, BLAS etc.) that are crucial for performance.
- This is a current topic of great interest: [European Environment for Scientific Software Installations (EESSI)](https://github.com/EESSI/)
- Common in HPC environments:
    - EasyBuild
    - Spack
- Both tools heavily rely on Python and are using `archspec`.
- Idea: Describe installation procedure in a package in order to automatize it.
- Tool (try to) will do dependency resolution, compilation and installation.
- EasyBuild
    - Originated from Ghent University, Belgium
    - Will create special environment variables that are prefixed with `EB`
- Spack
    - Originated from LLNL in the US
    - Can also be used to roll-out precompiled binaries
- European Environment for Scientific Software Installations (EESSI) tries to simplify the installation routine by providing precompiled packages with optimizations enabled.

## xSDK

- Standardization effort for scientific

## Exercise

| Duration | Format |
| --- | --- |
| XX minutes | Exercise |

1. TBD


## Further reading

### Other

### References

- [EasyBuild](https://github.com/easybuilders/easybuild)
- [EasyConfigs](https://github.com/easybuilders/easybuild-easyconfigs)
- [Spack](spack.io)
- [Spack docs](https://spack.readthedocs.io/en/latest/)
- [Spack 101 tutorials](https://spack-tutorial.readthedocs.io/en/latest/)
- [archspec project](https://github.com/archspec/)

### Talks

- Talks at FOSDEM
    - 2020: [Spack's new Concretizer](https://archive.fosdem.org/2020/schedule/event/dependency_solving_not_just_sat/)https://github.com/archspec/
    - 2020: [Build for your microarchitecture: experiences with Spack and archspec](https://archive.fosdem.org/2020/schedule/event/archspec/)
    - 2018: [Binary packaging for HPC with Spack](https://archive.fosdem.org/2018/schedule/event/llnl_spack/)
