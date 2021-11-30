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

- Debian package format common
    - Debian, Ubuntu... (lot os derivatives)
- Goal: Debian Package for Ubuntu
    - Create installation routing
    - Make project packagable
    - Create Debian package
    - Inspect Debian package

---

## Adding Installation Target

- Add target `install` for `make`
- Should install files in `prefix/<bin/include/lib...>`
-

## CPack

- CLI tool and CMake module
- Deals with package creation
- Depends strongly on `install()` routine of project
    - The install routine was missing in the previous example

---

## CPack configuration

- Create separate CMake file (in `cmake/`)
    - Not necessary, but helps with managements

---

## Options

- `CPACK_PACKAGE_<OPTION>`

---

## Demo: Project Extension

- Installation target
- Packaging configuration (CPack, common settings)


---

## Debian Package Format

- "Package" is special **archive**
- File ending `.deb`
- Contents:
    - `control` dictionary
    -
    -
    -

---

## Debian Package Naming

> NAME_VERSION-REVISION_ARCHITECTURE.deb

- `NAME`:
- `VERSION`: Software Version Number (e.g. "PETSc 3.16.1" -> `3.16.1`)
- `REVISION`: Package Version Number
- `ARCHITECTURE`: Target architectre (amd64, arm...)

---

## Debian-specific Options

- `CPACK_DEBIAN_FILE_NAME`: Follow Debian nomenclature (`deb`-file)

---

## Package creation (Debian)

- Stuff

  ```bash
  cmake -DCMAKE_BUILD_TYPE=Release -DSOME_OPTION_VALUE ..
  make / cmake build --target
  cpack -G DEB
  ```

---

## Testing the package

- `lintian`
- Shows shortcomings of the Debian package

---

## Demo: Debian Package

- Extend CPack configuration
- Test Debian package

---

## Advanced Topics

- Publishing Packages on [Launchpad](https://launchpad.net/)
- Debian package creation via [CPack](https://cmake.org/cmake/help/latest/cpack_gen/deb.html#cpack_gen:CPack%20DEB%20Generator)
- Usage of our library in other projects
    - Creation of `pkg-config` file from CMake
    - Creation of `CMake` configuration generatio

---

## Further Reading

- [Debian Package Basics](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html)
- [Debian Packaging Guide](https://wiki.debian.org/Packaging)
- [Ubuntu Packaging Guide](https://packaging.ubuntu.com/html/)
- [Making a deb package with CMake/CPack and hosting it in a private APT repository](https://decovar.dev/blog/2021/09/23/cmake-cpack-package-deb-apt/)
- [Launchpad](https://launchpad.net/)
- [CPack documentation](https://cmake.org/cmake/help/latest/module/CPack.html)