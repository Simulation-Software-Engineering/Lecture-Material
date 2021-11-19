# Make and CMake

> 60 mins in total

## Make

> 15 mins

### "Hello World" starting point

Show `hello-world.cpp` and build by hand `g++ -o HelloWorld main.cpp`

```cpp
#include <iostream>

int main(int argc, char *argv[])
{
  std::cout << "Hello World!" << std::endl;
  return 0;
}
```

### What is Make?

- A build manager
- The / a go-to solution for small projects (e.g., latex document, processing data, ...)
- A buidling block for cmake
- Nice non-expert introduction in [py-RSE book, chapter 9](https://merely-useful.tech/py-rse/automate.html)
- [GNU Make](https://www.gnu.org/software/make/): standard implementation of Make for Linux and macOS

### How does it work?

- When you create / change a file, the OS updates timestamp of file.
- Make compares timestamps to see which files are older / newer than others.
- In `Makefile`:
    - Rules which file(s) depend on which other file(s)
    - Rules how to update out-of-date files
- When you run `make`, Make updates out-of-date files including transitive dependencies in right order.

### Single rule example

```makefile
HelloWorld : main.cpp
	g++ -o HelloWorld main.cpp
```

- Explain that `HelloWorld` depends on `main.cpp` and rule to update
- Three cases:
    - no `HelloWorld`: run update
    - `HelloWorld` older than `main.cpp`: run update
    - `HelloWorld` newer than `main.cpp`: do nothing

- Run make twice
- `ll` to show timestamp

- Requires actual tabs, spaces not allowed. Show error message.

> Makefile:2: *** missing separator (did you mean TAB instead of 8 spaces?).  Stop.

### Multiple rules example and phony targets

- Add `sse.hpp` and `sse.cpp` in subfolder `sse`

`sse.cpp`:

```cpp
#include "sse.hpp"
#include <iostream>

void sse()
{
  std::cout << "SSE is great!" << std::endl;
}
```

`sse.hpp`:

```cpp
#pragma once

void sse();
```

`main.cpp`:

```diff
#include <iostream>
+ #include "sse.hpp"

int main()
{
  std::cout << "Hello World!" << std::endl;
+ sse();
  return 0;
}
```

`Makefile`:

```makefile
sse.o : sse/sse.hpp sse/sse.cpp
	g++ -c sse/sse.cpp

HelloWorld : main.cpp sse/sse.hpp
	g++ -o HelloWorld sse.o main.cpp sse.o
```

- Run `make`, only builds `sse.o`
- By default, first target is built
- `make HelloWorld` to build specific target
- phony target (doesn't correspond to file, no update rule)

```diff
+ all : HelloWorld sse.o
```

- Why does Make not just build directly build all targets? We could want to do different things with different targets.
- Add `clean` target, has no dependency

```diff
+ clean :
+ 	rm HelloWorld sse.o
```

- Run `make clean`
- `mkdir clean` and `make clean` confuses Make

```
+ .PHONY : all clean
```

### Advanced Make

- There is more:
    - Variables
    - Rules
    - Wildcards
- ... but becomes quickly very hard to read
- Not covered because cmake does this for us.
- But nicely documented in [py-RSE chapter 9](https://merely-useful.tech/py-rse/automate.html).


## CMake

*35 mins* ... might be tough

### Introduction


What is cmake?

> A build system generator, for e.g. makefiles

Why not directly use makefiles?

> CMake can do many more things, is more flexible, avoids complex patterns, and is, thus, more readable

Are there alternatives?

> Yes, `scons`, `autotools`, ...

Will you explain and discuss the differences in detail?

> No, but I claim that CMake is the most standard tool and sticking to standards has a value in itself. [Watch a video why](https://youtu.be/sBP17HQAQjk)

Can you give some reasons why CMake is great?

> Of course:

- CMake can generate many build systems: make, ninja, VSCode project, Eclipse project, ...
- Many GUIs and TUIs: ccmake, cmake-gui, integration in probably nearly all IDEs, ...
- CMake is *"cross-platform"*: you can ideally use same cmake file in all OS's (easy to distinguish platform-specific things)
- Build directory becomes independent of source directory (build multiple versions with different dependencies etc.)
- CMake respects choices in user environment (e.g. user defines cpp compiler through CXX)

### CMake "Hello World"

Example adapted from [Yanson Tech](https://www.youtube.com/watch?v=wl2Srog-j7I)
Go back to original `main.cpp`

`CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION "3.12")

project("HelloWorld")

add_executable("${PROJECT_NAME}" main.cpp)
```

- CMake variable values: `${}`, use quotations to avoid problems with spaces
- `mkdir build && cd build && cmake ..` ... explain files (TODO), look at makefile
    - `CMakeCache.txt`
- `make` and `./HelloWorld`

### Multiple files

- Add again `sse.cpp` and `sse.hpp` in subfolder `sse` and adapt `main.cpp`

`CMakeLists.txt`:

```diff
+ add_executable("${PROJECT_NAME}" main.cpp sse/sse.cpp)
- add_executable("${PROJECT_NAME}" main.cpp)
```

- Generate and build again, this time both with verbose output TODO

- What if there are multiple source files in `sse` folder?

`CMakeLists.txt`:

```diff
+ file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
+ add_executable("${PROJECT_NAME}" "${SRC_FILES}")
- add_executable("${PROJECT_NAME}" main.cpp sse.cpp)
```

- `GLOB_RECURSE`: filenames with wildcard characters, recurse -> also subdirectories
- Actually discouraged since wildcard populated while generating. You need to run `cmake` again when you add a file. See [cmake docs](https://cmake.org/cmake/help/latest/command/file.html#filesystem).
- `CONFIGURE_DEPENDS` partial remedy, but costly and no guarantee that all build systems support this

### CTest

- Let's add some dummy tests

`main.cpp`:

```diff
+  if (argc > 1)
+  {
+    return 1;
+  }
```

`CMakeLists.txt`:

```diff
+ include(CTest)
+
+ add_test("test1" "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}")
+ add_test("test2" "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}" "someparam")
```

- `include` includes a module, some module are builtin in CMake
- Creates target `test`
- `make test`, explain output
- We will learn later (after Christmas) how to work with proper packages for testing (e.g. boost)

### CPack

- We can also package code with cmake (or better: steer from cmake)

`CMakeLists.txt`:

```diff
include(CPack)

install(TARGETS "${PROJECT_NAME}" DESTINATION bin)
```

- Goes to `$CMAKE_INSTALL_PREFIX/bin`
- Run cmake and `make package`, creates `HelloWorld-0.1.1-Linux.tar.gz`
- We will see later (next week) how to package a `.deb`
- Set version number

```diff
+ SET(CPACK_PACKAGE_VERSION_MAJOR "1")
+ SET(CPACK_PACKAGE_VERSION_MINOR "2")
+ SET(CPACK_PACKAGE_VERSION_PATCH "3")
include(CPack)
```

- Variables must be set before `include(CPack)`
- `make package` again

### Building libraries

- Let's turn the `sse` function into a library

```diff
+ file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS sse/*.cpp)
- file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
+ add_library(sse "${SRC_FILES}")
- add_executable("${PROJECT_NAME}" "${SRC_FILES}")
```

- Build static lib `libHelloWorld.a`, that's the default
- Build shared lib by `cmake -DBUILD_SHARED_LIBS=ON ..`, don't change in `CMakeLists.txt`, but stick to standards
- Define cmake variables with `-D`, we will come back to this later
- Now, let's use the library

```diff
+ add_executable("${PROJECT_NAME}" main.cpp)
```

- ... gives an error, we also need to link

```diff
+ target_link_libraries("${PROJECT_NAME}" PUBLIC sse)
```

TODO: explain PRIVATE (only build), PUBLIC (both), INTERFACE (only linking)

### External Dependencies

- preCICE should be used in every code :)

`main.cpp`:

```diff
+ #include "precice/SolverInterface.hpp"
...
+ sse();
+ std::cout << precice::getVersionInformation() << std::endl;
```

`CMakeLists.txt`:

```diff
find_package(precice REQUIRED CONFIG)
target_link_libraries("${PROJECT_NAME}" PRIVATE precice::precice)
```

- `find_package` works if dependency is "cmake-ready"
- Alternative option if lib is in a discoverable location (standard system path or adjusted `LD_LIBRARY_PATH`)

```cmake
find_library(precice REQUIRED CONFIG)
target_link_libraries("${PROJECT_NAME}" PRIVATE precice)
```

- TODO: external dependencies via pkg-config?
    - @fsimonis: Is `find_package` already using pkg-config? Or is there a real third option?
    - include(..), pkg-config.search_modules ... link ... cmake searches in pkg-config

### Options and variables

- For good software, a user should not need to touch `CMakeLists.txt`
- Use variables to talk to cmake
- Let's try to make preCICE an optional dependency of our code (not really everybody has preCICE installed, sadly)

`CMakeLists.txt`:

```cmake
if (ENABLE_PRECICE)
  message(STATUS "preCICE enabled")
  find_library(precice REQUIRED CONFIG)
  target_link_libraries("${PROJECT_NAME}" PRIVATE precice)
else()
  message(STATUS "preCICE disabled")
  target_compile_definitions("HelloWorld" PRIVATE NO_PRECICE)
endif()
```

`main.cpp`:

```c++
#ifndef NO_PRECICE
  std::cout << precice::getVersionInformation() << std::endl;
#endif
```

- Build without preCICE `cmake -DENABLE_PRECICE=OFF ..`
- Create different folder and build there with preCICE

TODO: variables, which ones are import? how to pass? change compiler etc

`CXX ?= g++`

TODO: More reading on this:

- https://cmake.org/cmake/help/latest/module/FindPkgConfig.html#command:pkg_check_modules
- https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html
- https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html


### ccmake

`sudo apt-get install cmake-curses-gui`

- `ccmake ..`
- `c`, look add description of ENABLE_PRECICE`, disable it
- `t`, show all options, helpful to find out which variables exist
- `g`, generate `Makefile`

TODO: watch some tutorial, learn more

## Explain preCICE `CMakeLists.txt`

> 10 mins

- `sources.cmake` to include sources

## Exercise

TODO

> 90 mins

- Skeleton: main file, 2-3 other source files, each one with one dependency (e.g. Eigen (a bit difficult), deal.II, boost, mpi (?),..., boost-dev (header only) -> `boost_container_flat_set` example?)
- Other header are initially commented out in main file.
- Write docker file and build container, based on Ubuntu 20:04 (we only give high-level instructions this time)
- Students write basic `CMakeLists.txt`.
- Add dependencies step by step. (in code, in `CMakeLists.txt`, in docker recipe (we provide package names)
- Make dependencies all optional
- Use CTest (we already provide test stubs)
- Open PR with docker recipe, `CMakeLists.txt, and modified code

## Further material

- [Cmake Tutorial Video](https://www.youtube.com/watch?v=mKZ-i-UfGgQ)
- https://cliutils.gitlab.io/modern-cmake/
- https://github.com/dev-cafe/cmake-cookbook
