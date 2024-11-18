# Notes for CMake demo

Example code is in [`building-and-packaging/material/examples/cmake`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/03_building_and_packaging/examples/cmake). Example adapted from [Yanson Tech](https://www.youtube.com/watch?v=wl2Srog-j7I)

## CMake "Hello World"

- Look at and explain `CMakeLists.txt`.
- `cmake --help-command-list`, `cmake --help-command add_executable`
- `mkdir build && cd build && cmake ..`
- Standard to create `build` directory, don't call `cmake` in root directory.
    - In case of doubt, you can always just delete complete folder.
    - And you can have multiple build folders.
- Explain and look at files:
    - `Makefile`: lengthier than you think, many targets, search for `helloworld`
    - `CMakeCache.txt`: stores values of variables, used by GUIs for example
    - `cmake_install.cmake`: a file used by CPack internally, ignore it
    - `CMakeFiles`: even much more things that are not so important right now
- `make` and `./helloworld`
- `make clean`
- Makefiles are created by default, one can also create other things: `cmake --help`
- A bit more modern: From project root call:
    - `cmake -S. -Bbuild`
    - `cmake --build build` (independent of generator)

## Multiple files

- Again `sse.cpp` and `sse.hpp` in subfolder `sse`, same files
- Again adapt `main.cpp`:

```diff
#include <iostream>
+ #include "sse/sse.hpp"

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
- Run
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

## Building libraries

- `make clean`
- Let's turn the `sse` function into a library

```diff
+ file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS sse/*.cpp)
- file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
+ add_library(sse "${SRC_FILES}")
- add_executable(helloworld "${SRC_FILES}")
```

- Build static lib `libHelloWorld.a`, that's the default
- Build shared lib by `cmake -DBUILD_SHARED_LIBS=ON ..`, don't change in `CMakeLists.txt`, but stick to standards
- Define CMake variables with `-D`, we will come back to this later
- Now, let's use the library:

```diff
+ add_executable(helloworld main.cpp)
```

- ... gives an error, we also need to link

```diff
+ target_link_libraries(helloworld PRIVATE sse)
```

- `PRIVATE` means that the symbols of sse are not visible from the outside (imagine helloworld would be a library again)
- If `PUBLIC` and `helloworld` was library and used by `X`, we would also need to link `sse` in `X`.
- `cmake -DBUILD_SHARED_LIBS=ON ..` and `make` and `./helloworld`

## External dependencies

- preCICE should be used in every code :) .

`main.cpp`:

```diff
+ #include "precice/precice.hpp"
...
sse();
+ std::cout << precice::getVersionInformation() << std::endl;
```

- `make` ... does not find preCICE.

`CMakeLists.txt`:

```diff
find_package(precice REQUIRED CONFIG)
target_link_libraries(helloworld PRIVATE precice::precice)
```

- `cmake ..` and `make` and `./helloworld`
- `find_package` works if dependency is "cmake-ready"
    - There is a ["module" and a "config" mode](https://cmake.org/cmake/help/latest/command/find_package.html)
    - "module" mode
        - Is there a `Findprecice.cmake` module in CMake? Some are shipped with CMake. But this doesn't scale.
            - Find out which: `cmake --help-module-list | grep "Find"`
        - Is there a `Findprecice.cmake` module elsewhere? We could ship one with our helloworld program. But these modules often out-of-date.
    - "config" mode (here the case, the newer/better way of doing things)
        - Is there a `preciceCongfig.cmake`? A file installed by preCICE. Scales and up-to-date.
        - If not installed, one can extend `CMAKE_PREFIX_PATH`.
        - If a specific preCICE should be used, specify `preCICE_DIR` variable.
- `precice::precice` since in namespace
- If not "cmake-ready", but lib is in a discoverable location (standard system path or adjusted `LIBRARY_PATH`)

```cmake
find_library(precice REQUIRED)
target_link_libraries("${PROJECT_NAME}" PRIVATE precice)
```

## Options and variables

- For good software, a user should not need to touch `CMakeLists.txt`.
- Use variables to talk to CMake.
- Let's try to make preCICE an optional dependency of our code (not really everybody has preCICE installed, sadly).

`main.cpp`:

```c++
#ifndef NO_PRECICE
  std::cout << precice::getVersionInformation() << std::endl;
#endif
```

and around header (double negating is also the standard way to do things here).

`CMakeLists.txt`:

```cmake
option(ENABLE_PRECICE "Enable use of preCICE." ON)

if(ENABLE_PRECICE)
  message(STATUS "preCICE enabled")
  find_package(precice REQUIRED CONFIG)
  target_link_libraries(helloworld PRIVATE precice::precice)
else()
  message(STATUS "preCICE disabled")
  target_compile_definitions(helloworld PRIVATE NO_PRECICE)
endif()
```

- Build without preCICE `cmake -DENABLE_PRECICE=OFF ..` and `make` and `./helloworld`.
- Create different folder and build there with preCICE.
- Build in release mode `-DCMAKE_BUILD_TYPE=Release` and `make VERBOSE=1`.
