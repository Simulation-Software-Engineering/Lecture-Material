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

## Learning Goals of This Unit

- Understand the motivation of learning CMake.
- Work with CMake as a user of a project following good practices (using variables, specifying locations of dependencies).
- Develop simple CMake projects (executable vs. library, dependencies) and know how to learn more.

---

## What is CMake?

> A build system generator, for e.g. makefiles

---

## Why Not Directly Use Makefiles?

> CMake can do many more things, is more flexible, avoids complex patterns, and is, thus, more readable.
> But Make is also powerful and there are people loving it ... in the end, you need a certain understanding of both.

---

## Are There Alternatives?

> Yes, `autotools`, `scons`, ...

---

## Will You Explain and Discuss the Differences in Detail?

> No, but I claim that CMake is a standard tool for simulation software and sticking to standards has a value in itself. [Watch a video why](https://youtu.be/sBP17HQAQjk)

---

## At Least Some Reasons Why CMake is Great?

- CMake can generate files for many build systems: Make, ninja, VSCode project, Eclipse project, ...
- Many **GUIs** and **TUIs**: `ccmake`, `cmake-gui`, integration in probably nearly all IDEs, ...
- CMake is **cross-platform**: you can ideally use same CMake file in all OS (easy to distinguish platform-specific things).
- CMake build directory independent of project source directory (build multiple versions with different dependencies, different build types,  etc.)
- CMake respects choices in user environment (e.g. user defines cpp compiler through `CXX`).
- Wide language support

... does not all make it better than other solutions per-se.

---

## Who Develops CMake?

> KitWare (Scientific visualization, VTK, ParaView, ...), started around 2000 in need of a cross-platform build environment

---

## Demo 1/3

- "Hello World"
- Multiple files

---

## Basic Commands

- `cmake_minimum_required(VERSION "3.12")`
- `project("HelloWorld")`
- `add_executable(myexecutable main.cpp)`
    - Add executable using specified source files
    - Can use variables here: `"${SRC_FILES}"`
- `add_library(mylibrary "${SRC_FILES}")`
    - Add library using specified source files
- `file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS src/*.cpp)`
    - Collect list of files in variable `SRC_FILES` via wildcard
    - `CONFIGURE_DEPENDS` enables [population during building](https://cmake.org/cmake/help/latest/command/file.html#filesystem) (does not always work, sometimes discouraged)

---

## Demo 2/3

- Building libraries
- External dependencies

---

## External Dependencies

- `find_package(dependency REQUIRED MODULE/CONFIG)`
    - Find "cmake-ready" external package on system and make available
    - `MODULE` mode: Is there a `Finddependency.cmake` shipped with CMake or elsewhere?
    - `CONFIG` mode: Is there a `dependencyCongfig.cmake` installed or in `CMAKE_PREFIX_PATH`
        - Specific specific version with variable `Dependency_DIR`.
- `find_library(dependency REQUIRED)`
    - Find "not-cmake-ready" external package on system (standard system path or adjusted `LIBRARY_PATH`) and make available
- `target_link_libraries(myexecutable PRIVATE dependency)`
    - Links library `dependency` into target `myexecutable`
    - `PRIVATE`: symbols of `dependency` are not visible in `myexecutable`

---

## Demo 3/3

- Options and variables

---

## CMake Variables

- Use variables to talk to CMake (as user, do not change `CMakeLists.txt`)
    - Example: `cmake -DBUILD_SHARED_LIBS=ON ..`
    - [Already available CMake variables](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)
- `option(OPTION_NAME "Some description" ON)`
    - Define boolean option variable
    - Defaults to `ON`
    - Change via `cmake -DOPTION_NAME=OFF ..`
    - Use in CMake via `if(OPTION_NAME)`
- `target_compile_definitions(myexecutable PRIVATE NO_DEPENDENCY)`
    - Specify compile definition in target `myexecutable`
    - Use in code via `#ifndef NO_DEPENDENCY`

---

## Summary

- CMake generates build systems, e.g. a makefile with standard targets (`all`, `clean`).
- Define project, targets, dependencies in `CMakeLists.txt`
- Good practice: `mkdir build && cd build && cmake ..`
- Globs (e.g. `*.cpp`) can, but should not be handled directly in `CMakeLists.txt`, since populated during generation.
- Find dependencies with `find_package` (if cmake-ready) or `find_library` (if not)
- As a user, do not edit `CMakeLists.txt`, but work with variables, e.g. `cmake -DBUILD_SHARED_LIBS=ON ..`.

---

## Further Reading

- [Official CMake docs](https://cmake.org/cmake/help/latest/index.html)
- [Offical CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [Basic (unofficial) Cmake Tutorial for Linux Video](https://www.youtube.com/watch?v=mKZ-i-UfGgQ)
- [Advanced, but very good video tutorial](https://www.youtube.com/watch?v=bsXLMQ6WgIk)
- [An Introduction to Modern CMake](https://cliutils.gitlab.io/modern-cmake/)
- [Professional CMake](https://crascit.com/professional-cmake/), an up-to-date (non-public) book
- [CMake Cookbook](https://github.com/dev-cafe/cmake-cookbook)
