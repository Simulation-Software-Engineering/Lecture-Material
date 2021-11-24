# Notes for CMake demo

Example code is in [`building-and-packaging/material/examples/cmake`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/building-and-packaging/examples/cmake). Example adapted from [Yanson Tech](https://www.youtube.com/watch?v=wl2Srog-j7I)

## CMake "Hello World"

- Look at and explain `CMakeLists.txt`.
- `mkdir build && cd build && cmake ..` 
- Standard to create `build` directory, don't call cmake in root directory.
  - In case of doubt, you can always just delete complete folder.
- Explain and look at files: 
    - `Makefile`: lengthier than you think, many targets
    - `CMakeCache.txt`: stores values of variables, used by GUIs for example
    - `cmake_install.cmake`: a file used by CPack internally, ignore it
- `make` and `./helloworld`
- `make clean`

## Multiple files

- Again `sse.cpp` and `sse.hpp` in subfolder `sse`, same files 
- Again adapt `main.cpp`:

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

- And adapt `CMakeLists.txt`:

```diff
+ add_executable(helloworld main.cpp sse/sse.cpp)
- add_executable(helloworld main.cpp)
```

- Generate and build again, this time with verbose output, `make VERBOSE=1`.
    - `cmake` does stuff again, checks build system.
    - How compiled, how linked, ...
- What if there are multiple source files in `sse` folder?

```diff
+ file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
+ add_executable(helloworld "${SRC_FILES}")
- add_executable(helloworld main.cpp sse.cpp)
```

- CMake variable values: `${}`, use quotations marks `"` to avoid problems with spaces.
- `GLOB_RECURSE`: filenames with wildcard characters, recurse -> also subdirectories
- Actually discouraged since wildcard populated while generating. You need to run `cmake` again when you add a file. See [cmake docs](https://cmake.org/cmake/help/latest/command/file.html#filesystem).
- `CONFIGURE_DEPENDS` partial remedy, but costly and no guarantee that all build systems support this.
- Alternatively, generate list outside of cmake (will come back to this later).

## CTest

- Let's add some dummy tests.

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
+ add_test("test1" "${CMAKE_CURRENT_BINARY_DIR}/helloworld")
+ add_test("test2" "${CMAKE_CURRENT_BINARY_DIR}/helloworld" "someparam")
```

- `include` includes a module, [some modules](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html) are builtin in CMake.
- Creates target `test`.
- `make test`, explain output.
- We will learn later (after Christmas) how to work with proper packages for testing (e.g. boost).

## CPack (maybe moved to next week if time short)

- We can also package code with CMake (or better: steer from CMake).

```diff
include(CPack)

install(TARGETS helloworld DESTINATION bin)
```

- Goes to `$CMAKE_INSTALL_PREFIX/bin`
- Run cmake and `make package`, creates `HelloWorld-0.1.1-Linux.tar.gz`
- We will see later (next week) how to package a `.deb`
- Set version number

```diff
+ project("HelloWorld" VERSION 2.3.0)
```

- `make package` again

## Building libraries

- Let's turn the `sse` function into a library

```diff
+ file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS sse/*.cpp)
- file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
+ add_library(sse "${SRC_FILES}")
- add_executable(main "${SRC_FILES}")
```

- Build static lib `libHelloWorld.a`, that's the default
- Build shared lib by `cmake -DBUILD_SHARED_LIBS=ON ..`, don't change in `CMakeLists.txt`, but stick to standards
- Define cmake variables with `-D`, we will come back to this later
- Now, let's use the library

```diff
+ add_executable(helloworld main.cpp)
```

- ... gives an error, we also need to link

```diff
+ target_link_libraries(helloworld PRIVATE sse)
```

- `PRIVATE` means that the symbols of sse are not visible from the outside (imagine helloworld would be a library again)
- If `PUBLIC` and `helloworld` was library and used by `X`, we would also need to link `sse` in `X`.

## External dependencies

- preCICE should be used in every code :) .

`main.cpp`:

```diff
+ #include "precice/SolverInterface.hpp"
...
sse();
+ std::cout << precice::getVersionInformation() << std::endl;
```

`CMakeLists.txt`:

```diff
find_package(precice REQUIRED CONFIG)
target_link_libraries("${PROJECT_NAME}" PRIVATE precice::precice)
```

- `find_package` works if dependency is "cmake-ready"
    - There is a ["module" and a "config" mode](https://cmake.org/cmake/help/latest/command/find_package.html)
    - "module" mode
        - Is there a `Findprecice.cmake` module in CMake? Some are shipped with CMake. But this doesn't scale.
        - Is there a `Findprecice.cmake` module elsewhere? We could ship one with our helloworld program. But these modules often out-of-date.
    - "config" mode (here the case, the newer/better way of doing things)
        - Is there a `preciceCongfig.cmake`? A file installed by preCICE. Scales and up-to-date.
        - If not installed, one can extend `CMAKE_PREFIX_PATH`. 
        - If a specific preCICE should be used, specify `preCICE_DIR` variable.
- `precice::precice` since in namespace
- If not "cmake-ready", but lib is in a discoverable location (standard system path or adjusted `LIBRARY_PATH`)

```cmake
find_library(precice REQUIRED CONFIG)
target_link_libraries("${PROJECT_NAME}" PRIVATE precice)
```

- As a third option, [one can also use pkg-config](https://cmake.org/cmake/help/latest/module/FindPkgConfig.html) (not shown here).


## Options and variables

- For good software, a user should not need to touch `CMakeLists.txt`.
- Use variables to talk to CMake.
- Let's try to make preCICE an optional dependency of our code (not really everybody has preCICE installed, sadly).

`CMakeLists.txt`:

```cmake
option(ENABLE_PRECICE "Enable use of preCICE." ON)

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
- Create different folder and build there with preCICE.
- Build in release mode `-DCMAKE_BUILD_TYPE=Release`
- This is a [standard CMake variable](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html).

## ccmake

`sudo apt-get install cmake-curses-gui`

- `ccmake ..`
- `c`, look add description of ENABLE_PRECICE`, disable it
- `t`, show all options, helpful to find out which variables exist
- `g`, generate `Makefile`

## Explain preCICE `CMakeLists.txt`

- On GitHub [here](https://github.com/precice/precice/blob/develop/CMakeLists.txt)
    - `sources.cmake` to include sources
    - TODO what else to show?
- Another real-world example: [deal.II](https://github.com/dealii/dealii/blob/master/CMakeLists.txt)
