---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
  code-block-font-size: \tiny
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

# Installation and Packaging with CMake and CPack

---

## Learning Goals of This Unit

- Add install targets to simple CMake projects.
- Package simple CMake projects with CPack.
- Create Debian (`deb`) packages of simple programs or libraries using CPack on Ubuntu.
- Check the resulting Debian packages.

---

## Introduction

- Why [Debian](https://www.debian.org/) package format?
    - It is common Debian, [Ubuntu](https://ubuntu.com/)...
    - Is the "natural" way to insall software on Debian, Ubuntu etc. (via `dpkg`/aptitude `apt`)
- Easy to share (`deb` file)
- Can be hosted and integrated in [official](https://launchpad.net/ubuntu) or third-party repositories

TODO: read more

---

## Step by Step Plan

- Start from CMake configuration of previous lecture
- **Goal**: Create Debian package of HelloWorld code for Ubuntu
- Steps:
    1. Add install target
    2. Add CPack configuration
    3. Extend CPack configuration to create Debian package
    4. Check Debian package with `lintian`

---

## Demo (1/4): Add Install Target to CMake Configuration

- `make install` should install (i.e. copy) `helloworld` and `libsse` in appropriate locations:

```bash
prefix/
  bin/
  lib/
  include/
```

---

## CMake Commands for Installation (1/2)

- `set_target_properties(mylibrary PROPERTIES PUBLIC_HEADER "header1.hpp;header2.hpp;...")`
    - Make headers publicly visible
- Where to find headers?

  ```cmake
  target_include_directories(mylibrary
      PRIVATE
          # where the library itself will look for its internal headers
          ${CMAKE_CURRENT_SOURCE_DIR}/includedir
      PUBLIC
          # where top-level project will look for the library's public headers
          $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/includedir>
          # where external projects will look for the library's public headers
          $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/includedir>
  )
  ```

---

## CMake Commands for Installation (2/2)

- Easiest way via CMake module `GNUInstallDirs` (predefines standard destinations and variables: `CMAKE_INSTALL_BINDIR`, `CMAKE_INSTALL_LIBDIR`,...)
- Which type of file has to go where?

  ```cmake
  include(GNUInstallDirs)
  install(TARGETS target1 target2 ...
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/includedir
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/
    )
  ```

---

## CPack

- CLI tool and [CMake module](https://cmake.org/cmake/help/latest/module/CPack.html)
- Go-to solution for packaging of C/C++ code
- Requires an `install()` target in CMake project
- Several [generators](https://cmake.org/cmake/help/latest/manual/cpack-generators.7.html): archive, DEB, RPM, ...

---

## Demo (2/4): Add CPack Configuration

- Add and configure CMake module `CPack` such that `make package` creates packages

---

## CPack Configuration (1/2)

- Set [common CPack variables](https://cmake.org/cmake/help/latest/module/CPack.html#variables-common-to-all-cpack-generators) via `CPACK_PACKAGE_<OPTION>`:

  ```cmake
  set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
  set(CPACK_PACKAGE_VENDOR "SSE Lecturers")
  set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "SSE CPack example"
  CACHE STRING "Extended summary.")
  set(CPACK_PACKAGE_HOMEPAGE_URL "https://simulation-software-engineering.github.io")
  ```

- Include CPack after variables/options are set

  ```cmake
  ...
  include(CPack)
  ```

---

## CPack Configuration (2/2)

- Generate package
    - `cmake ..` and `cpack -G "TGZ;DEB"` or
    - `make package`
- Set default
    - `set(CPACK_GENERATOR "TGZ;DEB")`

---

## Demo (3/4): Create Debian Package

- Extend `CPack` configuration to create a proper Debian package, which we then `apt install`

---

## Some CPack Options for Debian Packages

- Many settings are set from general package settings `CPACK_PACKAGE_<OPTION>`
- Use Debian file naming scheme
    - `set(CPACK_DEBIAN_FILE_NAME DEB-DEFAULT)`

- Extract shared library dependencies via `dpkg-shlibdeps`
    - `set(CPACK_DEBIAN_PACKAGE_SHLIBDEPS YES)`

- More options in [CPack documentation](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator)

---

## Debian Package Naming

`NAME_VERSION-REVISION_ARCHITECTURE.deb`

- Example ([PETSc package on Launchpad](https://launchpad.net/ubuntu/+source/petsc))

  ```text
  libpetsc-real3.12-dev_3.12.4+dfsg1-1_amd64.deb
  ```

- `NAME`: Package name (`libpetsc-real3.12-dev`)
- `VERSION`: Software version number (e.g. "PETSc 3.12.4" -> `3.12.4+dfsg1`)
- `REVISION`: Package version number (`1`)
- `ARCHITECTURE`: Target architecture (`amd64`)

---

## Demo (4/4): Check Debian Package

- Look into Debian package and check for mistakes with `lintian`

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
    - Debian installation and removal scripts (`preinst`, `postinst`, `prerm`, `postrm`)
    - Files of actual package (binaries, libraries, includes...)

---

## Check Debian Package with Lintian

- Static analysis tool for Debian packages: [lintian](https://lintian.debian.org/)

- Remove debugging symbols from executable
    - `set(CPACK_STRIP_FILES TRUE)`

---

## Summary

- Before packaging, create an install target: `install(TARGETS ...)`
- CMake module `GNUInstallDirs` provides standard locations
- CMake module `CPack` is the go-to solution for packaging of C/C++ code
- Provide meta information via `CPACK_PACKAGE_<OPTION>` variables
- Create Debian packages with `DEB` generator
- Check Debian packages with `lintian`

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

