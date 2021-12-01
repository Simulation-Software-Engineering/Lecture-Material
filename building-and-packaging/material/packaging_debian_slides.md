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
</style>

# Creating Debian Packages from CMake

---

## Learning goals

- How to add an install target to a CMake project.
- How to package a CMake project via `CPack`.
- How to create a Debian (`deb`) package of your program/library using CPack.
- How to check the resulting Debian package.

---

## Introduction

- Why [Debian](https://www.debian.org/) package format?
    - It is common Debian, [Ubuntu](https://ubuntu.com/)...
    - Is the "natural" way to insall software on Debian, Ubuntu etc. (via `dpkg`/aptitude `apt`)
- Easy to share (`deb` file)
- Can be hosted and integrated in official or third-party repositories

---

## Step by Step Plan

- **Goal**: Create Debian package for HelloWorld code to be used on Ubuntu
- Steps:
    1. Extend CMake configuration from previous lecture to have `install` target
    2. Extend CMake configuration to contain a CPack section
    3. Extend the CMake configuration to create a Debian package
    4. Check the Debian package with `lintian` and potentially improve the package
- Code is on [GitHub](https://github.com/Simulation-Software-Engineering/HelloWorld)

---

## Adding Installation Target

- Add `install` target for `make`
- Should install files in appropriate location

  ```bash
  prefix/
    bin/
    lib/
    include/
    ...
  ```

---

## CPack

- CLI tool and [CMake module](https://cmake.org/cmake/help/latest/module/CPack.html)
- Go-to solution for packaging of C/C++ code
- Requires an `install()` routine in CMake project
- Several [generators](https://cmake.org/cmake/help/latest/manual/cpack-generators.7.html) for archive, DEB, RPM... type of packages

---

## CPack configuration

- Extend `CMakeLists.txt`  or create own module (`.cmake` file)
- Set [common CPack variables](https://cmake.org/cmake/help/latest/module/CPack.html#variables-common-to-all-cpack-generators) via `CPACK_PACKAGE_<OPTION>`

  ```cmake
  set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
  set(CPACK_PACKAGE_VENDOR "SSE Lecturers / Employer")
  ```

- Set target package variables, e.g., for [DEB generator](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator) via `CPACK_DEBIAN_<OPTION`>

  ```cmake
  set(CPACK_DEBIAN_FILE_NAME DEB-DEFAULT)
  set(CPACK_DEBIAN_PACKAGE_SHLIBDEPS YES)
  ...
  ```

- Generate package

  ```bash
  cmake -DCMAKE_OPTIONS ..
  cpack -G TGZ,DEB
  ```

---

## Demo 1: Preparing Project

1. Installation target
2. Packaging configuration (CPack, common settings)

**Warning:** We handle example as an seperate executable + library **for demonstration** only.

---

## Debian Package Format

- [Debian Package](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html) is special **archive**
    - Focus here on binary packages
- File ending `.deb`
- Used on Ubuntu (and other derivatives)
- Contents (some optional):
    - `control` file: Name, dependencies etc.
    - `md5sum` or similar: Checksums of bundled files
    - `conffile`: configuration file
    - Debian installation and removal scripts (`preinst`, `postinst`, `prerm`, a `postrm`)
    - Files of actual package (binaries, libraries, includes...)

---

## Debian Package Naming

> NAME_VERSION-REVISION_ARCHITECTURE.deb

- `NAME`: Package name
- `VERSION`: Software Version Number (e.g. "PETSc 3.16.1" -> `3.16.1`)
- `REVISION`: Package Version Number
- `ARCHITECTURE`: Target architectre (amd64, arm...)
- Example ([PETSc package on Launchpad](https://launchpad.net/ubuntu/+source/petsc))

  ```text
  libpetsc-real3.12-dev_3.12.4+dfsg1-1_amd64.deb
  ```

---

## Some CPack Options for Debian Packages

- Many settings are set from general settings
- `CPACK_DEBIAN_PACKAGE_NAME`: Package name, defaults to `CPACK_PACKAGE_NAME`
- `CPACK_DEBIAN_PACKAGE_VERSION`:
- `CPACK_DEBIAN_FILE_NAME`: Create package according to Debian package naming scheme. Recommended to set to `DEB-DEFAULT`
- `CPACK_DEBIAN_PACKAGE_SHLIBDEPS`: Extract shared library dependencies via `dpkg-shlibdeps`
- More options in [documentation](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator)

---

## Testing the package

- Ensure quality standards of package
    - Requirements higher for packages in official repositories
- Static analysis tool for Debian packages: [lintian](https://lintian.debian.org/)
    - `lintian` helps finding problems of package

---

## Demo 2: Debian Package

- Extend CPack configuration for Debian packaging
- Analyze Debian package

**Warning:** We handle example as an seperate executable + library **for demonstration** only.

---

## Advanced Topics

- Publishing Packages on [Launchpad](https://launchpad.net/)
- Usage of our library in other projects
    - Creation of `pc` file (`pkg-config`) from CMake
    - [Export targets](https://cmake.org/cmake/help/git-stage/guide/importing-exporting/index.html) to be included in other CMake projects

---

## Further Reading 1/2

- [Debian Package Basics](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html)
- [Debian Packaging Guide](https://wiki.debian.org/Packaging)
- [Ubuntu Packaging Guide](https://packaging.ubuntu.com/html/)
- [Launchpad](https://launchpad.net/)
- [lintian reports](https://lintian.debian.org/)
- [lintian man page](https://lintian.debian.org/)https://lintian.debian.org/

---

## Further Reading 2/2

- [CPack documentation](https://cmake.org/cmake/help/latest/module/CPack.html)
- [List of CPack generators](https://cmake.org/cmake/help/latest/manual/cpack-generators.7.html)
- [Debian CPack generator]([generators](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator))
- [Making a deb package with CMake/CPack and hosting it in a private APT repository](https://decovar.dev/blog/2021/09/23/cmake-cpack-package-deb-apt/)
- [GNU coding standard](https://www.gnu.org/prep/standards/html_node/Directory-Variables.html)