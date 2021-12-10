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
    font-family: 'Ubuntu Mono';
    color: orange;
  }
</style>

# Introduction to CMake

---

## Learning Goals of this Unit

- Students understand the motivation of learning CMake.
- Students know how to work with CMake as a user of a project following good practices (using variables, specifying locations of dependencies).
- Students can develop simple CMake projects (executable vs. library, dependencies, CTest) and know how to learn more.

---

## What is CMake?

> A build system generator, for e.g. makefiles

---

## Why not directly use makefiles?

> CMake can do many more things, is more flexible, avoids complex patterns, and is, thus, more readable.
> But Make is also powerful and there are people loving it ... in the end, you need a certain understanding of both.

---

## Are there alternatives?

> Yes, `autotools`, `scons`, ...

---

## Will you explain and discuss the differences in detail?

> No, but I claim that CMake is a standard tool for simulation software and sticking to standards has a value in itself. [Watch a video why](https://youtu.be/sBP17HQAQjk)

---

## At least some reasons why CMake is great?

- CMake can generate files for many build systems: Make, ninja, VSCode project, Eclipse project, ...
- Many **GUIs** and **TUIs**: `ccmake`, `cmake-gui`, integration in probably nearly all IDEs, ...
- CMake is **cross-platform**: you can ideally use same CMake file in all OS's (easy to distinguish platform-specific things)
- Build directory becomes independent of source directory (build multiple versions with different dependencies, different build types,  etc.)
- CMake respects choices in user environment (e.g. user defines cpp compiler through `CXX`)
- Wide language support

... does not all make it better than other solutions per-se.

---

## Who develops CMake?

> KitWare (Scientific visualization, VTK, ParaView, ...), started around 2000 in need of a cross-platform build environment

---

## Demo

- "Hello World"
- Multiple files
- CTest
- CPack
- Building libraries
- External dependencies
- Options and variables
- ccmake
- `CMakeLists.txt` of preCICE

---

## Summary

- CMake generates build systems, e.g. a makefile with standard targets (`all`, `clean`)
- Define project, targets, dependencies in `CMakeLists.txt`
- Good practice: `mkdir build && cd build && cmake ..`
- As a user, do not edit `CMakeLists.txt`, but work with variables, e.g. `cmake -DBUILD_SHARED_LIBS=ON ..`
- Globs (e.g. `*.cpp`) can, but should not be handled directly in `CMakeLists.txt`, since populated during generation
- Use CTest to add `test` target
- Find dependencies with `find_package` (if cmake-ready) or `find_library` (if not)

---

## Further Reading

- [Official CMake docs](https://cmake.org/cmake/help/latest/index.html)
- [Offical CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [Basic (unofficial) Cmake Tutorial for Linux Video](https://www.youtube.com/watch?v=mKZ-i-UfGgQ)
- [Advanced, but very good video tutorial](https://www.youtube.com/watch?v=bsXLMQ6WgIk)
- [An Introduction to Modern CMake](https://cliutils.gitlab.io/modern-cmake/)
- [Professional CMake](https://crascit.com/professional-cmake/), an up-to-date (non-public) book
- [CMake Cookbook](https://github.com/dev-cafe/cmake-cookbook)
