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

## Introduction

- [Debian](https://www.debian.org/) package format common
    - Debian, [Ubuntu](https://ubuntu.com/)... (lot os derivatives)
    - Native packaging format of popular Linux distributions
    - Support by native package manager (`dpkg`/aptitude `apt`)
- Easy to share (`deb` file)
- Can be hosted and integrated in official or third-party repositories

---

## Step by Step Plan

- **Goal**: Debian Package for Ubuntu
- Steps:
    1. Create installation routine
    2. Make project packagable
    3. Create Debian package
    4. Inspect Debian package

---

## Adding Installation Target

- Software must be installable
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
- Deals with package creation
- Depends strongly on `install()` routine of project
    - The install routine was missing in the previous example
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

## Demo: Project Extension

- Installation target
- Packaging configuration (CPack, common settings)

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

---

## Testing the package

- Ensure quality standards of package
    - Requirements higher for packages in official repositories
- Static analysis tool for Debian packages: [lintian](https://lintian.debian.org/)
    - Shows shortcomings of the Debian package

---

## Demo: Debian Package

- Extend CPack configuration for Debian packaging
- Analyze Debian package

---

## Advanced Topics

- Publishing Packages on [Launchpad](https://launchpad.net/)
- Debian package creation via [CPack](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator)
- Usage of our library in other projects
    - Creation of `pkg-config` file from CMake
    - Creation of `CMake` configuration generatio

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