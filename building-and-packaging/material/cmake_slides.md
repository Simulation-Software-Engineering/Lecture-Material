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

TODO

- Students understand the basic functionality of makefiles (timestamps, dependencies, update rules).
- Students can read simple makefiles and know where to look for additional material for complex makefiles.
- Students can write simple makefiles for small projects.

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

## Can you give some reasons why CMake is great?

> Of course:

- CMake can generate files for many build systems: make, ninja, VSCode project, Eclipse project, ...
- Many GUIs and TUIs: ccmake, cmake-gui, integration in probably nearly all IDEs, ...
- CMake is *"cross-platform"*: you can ideally use same cmake file in all OS's (easy to distinguish platform-specific things)
- Build directory becomes independent of source directory (build multiple versions with different dependencies, different build type,  etc.)
- CMake respects choices in user environment (e.g. user defines cpp compiler through CXX)
- Wide language support

... does not all make it better than other solutions per-se.

---

## Who develops CMake?

> KitWare (Scientific visualization, VTK, ParaView, ...), started around 2000 in need of a cross-platform build environment

---


## Demo



---

## Summary

TODO

---

## Further Reading

TODO: have a look at all first

- [Official CMake docs](https://cmake.org/cmake/help/latest/index.html)
- [Offical CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [Cmake Tutorial Video](https://www.youtube.com/watch?v=mKZ-i-UfGgQ)
- [Advanced, but very good video tutorial](https://www.youtube.com/watch?v=bsXLMQ6WgIk)
- https://cliutils.gitlab.io/modern-cmake/
- [Up-to-date (non-public) book](https://crascit.com/professional-cmake/)
- https://github.com/dev-cafe/cmake-cookbook


