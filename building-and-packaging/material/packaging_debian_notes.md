# Debian packages

## Learning goals

- How to make a CMake project installable.
- How to package a CMake project via `CPack`.
- How to create a Debian (`deb`) package of your program/library using CPack.
- How to check the resulting Debian package.

## Introduction

- Now:
    - Debian packages for C++ via `CMake`
    - HPC suitable packages for Python and C++
        - This requires a well-defined installation routine.
- Rough plan
    1. Extend CMake configuration from previous lecture to have an `install` target as well as proper prefix and installation layout (`/bin`, `/include`, `/lib`...)
    2. Extend CMake configuration to contain a CPack section (rather minimal) such that we can create a package (`tar.gz` file)
    3. Extend the CMake configuration to create a Debian package
    4. Check the Debian package with `lintian` and potentially improve the package

## 1. Preparing Project

- We will extend the code from the previous lecture.
    - [GitHub repository](https://github.com/Simulation-Software-Engineering/HelloWorld)
- Make sure two files are created (a library and en executable). This should be the case when starting with the code from last week's lecture.
- We add the following changes
    - Adding a version number to the project. This is not needed yet, but I am afraid of forgetting it later.
    - We mark the include files needed to use the `libsse` library, i.e., `sse/sse.hpp` publicly visible.
    - We define the target's include directory, i.e., where do we have to look for the dependency depending on the type of build (internally, top-level cmake project, external dependency)
    - We want to make sure that we have an `install` target for make that, at the same time, considers typical installation directories. That means `make install` should binaries in a `<prefix>/bin`, libraries in `<prefix>/lib` or `<prefix>/lib/helloworld`, include files in `<prefix>/include` etc. We include the predefined CMake macro `GNUInstallDirs` to get predefined variables like the installation directories.

Changes:

```diff
- project("HelloWorld")
+ project("HelloWorld" VERSION 0.1.0)
+ add_library(sse sse/sse.cpp)
+
+ set_target_properties(sse PROPERTIES PUBLIC_HEADER sse/sse.hpp)

+target_include_directories(sse
+    PRIVATE
+        # where the library itself will look for its internal headers
+        ${CMAKE_CURRENT_SOURCE_DIR}/helloworld
+    PUBLIC
+        # where top-level project will look for the library's public headers
+        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/helloworld>
+        # where external projects will look for the library's public headers
+        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/helloworld>
+)

+# Create install targets
+include(GNUInstallDirs)
+install(TARGETS helloworld sse
+  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
+  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
+  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
+  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/helloworld
+  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/helloworld
+  )
```

- Fire up a prepared containerf or testing. Container is beneficial as it allows us to mess around with the container's paths without messing up our own system. From the example repository I run

  ```bash
  sudo docker run --rm -it --name ubuntu-packaging --mount type=bind,source="$(pwd)",target=/mnt/cpack-example jaustar/debian-package-building-base
  ```

- Build the library and install it

  ```bash
  mkdir build && cd build
  cmake -DBUILD_SHARED_LIBS=ON ..
  make -j
  sudo make install
  ```

- Installs in `prefix=/usr/local`, i.e., it sets `CMAKE_INSTALL_PREFIX`.

  ```bash
  -- Install configuration: ""
  -- Installing: /usr/local/bin/helloworld
  -- Installing: /usr/local/lib/libsse.so
  -- Installing: /usr/local/include/helloworld/sse.hpp
  ```

  **Note** that we have an empty configuration here. It would make sense to build the project with a proper configuration (`Debug`, `Release`...) by setting `CMAKE_BUILD_TYPE`.
- Now we can run `helloworld` from anywhere on the system.
    - We might need to set `PATH="/usr/local/bin":"${PATH}"`. In my container it was not set.
- Tear down container

**Note**: At this point we have a package with reasonable installation routine. This is something we would need for (different) packaging solutions such as Debian packages and

## 2. Extend CMake configuration

In this step we add a CPack configuration such that we can actually create a package.

- We will add the configuration in another directory. Create `cmake/Packaging.cmake`
    - This allows to separate different parts of the CMake configuration.
- Additions to `CMakeLists.txt`

  ```diff
  + # Packaging section
  + # Adding other cmake modules
  + set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
  + # Include our packaging module
  + include(Packaging)
  ```

- Edit `cmake/Packaging.cmake` and add some properties.
    - `CPack` should be included at the end so it can ingest all preset variables
    - We can set version, e.g., but by default it will ingest the version number from the `project()` statement in `CMakeLists.txt`.
    - Full list of statements in [documentation](https://cmake.org/cmake/help/latest/module/CPack.html). Note, that the current statements are common properties of the packaging module.

  ```diff
  + set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
  +
  + set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "SSE hello world example project"
  +   CACHE STRING "Extended summary.")
  +
  + set(CPACK_PACKAGE_VENDOR "SSE Lecturers / Employer")
  +
  + set(CPACK_PACKAGE_CONTACT "firstname.lastname@example.com")
  + set(CPACK_PACKAGE_MAINTAINERS "SSE lecturers ${CPACK_PACKAGE_CONTACT}")
  +
  + set(CPACK_PACKAGE_HOMEPAGE_URL "https://simulation-software-engineering.github.io/homepage/")
  +
  + set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
  + set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
  + set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})
  +
  + include(CPack)
  ```

- Start up container again and then prepare project

  ```bash
  mkdir build && cd build
  cmake -DBUILD_SHARED_LIBS=ON ..
  ```

- This will create new files `CPackConfig.cmake` and `CPackSourceConfig.cmake`
- We can create a package, e.g., `tar.gz`

  ```bash
  cpack -G TGZ
  ```

  **NOTE** If this fails, this is due missing a `README.md` and `LICENSE` file. CPack expects these file to be present. They are important! Especially the license.

  `-G` is used to specify the package generator. We choose `TGZ` the generator for a compressed archive. We obtain the resulting file `HelloWorld-0.1.0-Linux.tar.gz`. The file name consists of the project name, version number and installation target.

- Inspect the package

  ```bash
  tar -xzf HelloWorld-0.1.0-Linux.tar.gz
  ```

  The unpacked package in directory `HelloWorld-0.1.0-Linux` has three subdirectories `bin/`, `lib/`, `include/`.

- We can also run `cpack -G DEB`, but it will complain

  ```bash
  $ cpack -G DEB
  CPack: Create package using DEB
  CPack: Install projects
  CPack: - Run preinstall target for: HelloWorld
  CPack: - Install project: HelloWorld []
  CPack: Create package
  -- CPACK_DEBIAN_PACKAGE_DEPENDS not set, the package will have no dependencies.
  CPack: - package: /mnt/cpack-example/build/HelloWorld-0.1.0-Linux.deb generated.
  ```

  The dependencies are missing for example.

## 3. Extend CPack configuration for Debian Package

- Setting up Debian package generator by adding lines to `cmake/Packaging.cmake`:

  ```diff
  + # Debian packaging section
  + set(CPACK_DEBIAN_FILE_NAME DEB-DEFAULT)
  + set(CPACK_DEBIAN_PACKAGE_SHLIBDEPS YES)
  ```

  `CPACK_DEBIAN_FILE_NAME` will set the package name to follow the standard package naming scheme (see slides) and `CPACK_DEBIAN_PACKAGE_SHLIBDEPS` set to `YES` will (try to) extract the dependencies automatically. We can also set dependencies manually (`CPACK_DEBIAN_PACKAGE_DEPENDS`).

- Afterwards there will be no more complaint as the dependency list will be generated

  ```bash
  $ cpack -G DEB
  CPack: Create package using DEB
  CPack: Install projects
  CPack: - Run preinstall target for: HelloWorld
  CPack: - Install project: HelloWorld []
  CPack: Create package
  CPackDeb: - Generating dependency list
  CPack: - package: /mnt/cpack-example/build/helloworld_0.1.0_amd64.deb generated.
  ```

  We see that the package name was set to "${helloworld}" as lowercase names seem to be preferred.

- We can install the package

  ```bash
  sudo apt install ./helloworld_0.1.0_amd64.deb
  ```

  Files are installed in `/usr` now instead of `/usr/local`. That is the default target for Debian packages using the generator!

## 4. Check Debian package

- The package already is usable. However, one might want to make sure that quality is good. If one wants to submit something to the actual repository of Ubuntu/Debian, then one has to follow the provided standards.
- If time permits we can checkout the contens of the package.
    - Inspect meta information

    ```bash
    dpkg --info helloworld_0.1.0_amd64.deb
    ```

    - Check full content

    ```bash
    dpkg-deb -R ./helloworld_0.1.0_amd64.deb ./helloworld-unpacked
    tree helloworld-unpacked
    ./helloworld-unpacked/
    ├── DEBIAN
    │   ├── control
    │   ├── md5sums
    │   ├── postinst
    │   └── postrm
    └── usr
        ├── bin
        │   └── helloworld
        ├── include
        │   └── sse
        │       └── sse.hpp
        └── lib
            ├── cmake
            │   ├── HelloWorldTargets-release.cmake
            │   └── HelloWorldTargets.cmake
            ├── libsse.so -> libsse.so.0.1.0
            └── libsse.so.0.1.0
    ```


- Check the package via `lintian`. (I need to do this on my host since I did not install lintian in the container).

  ```bash
  lintian helloworld_0.1.0_amd64.deb
  ```

- We observe quite some errors and warnings

  ```bash
  $ lintian helloworld_0.1.0_amd64.deb
  E: helloworld: changelog-file-missing-in-native-package
  E: helloworld: extended-description-is-empty
  E: helloworld: maintainer-name-missing firstname.lastname@example.com
  E: helloworld: no-copyright-file
  E: helloworld: package-must-activate-ldconfig-trigger usr/lib/libsse.so
  E: helloworld: unstripped-binary-or-object usr/bin/helloworld
  E: helloworld: unstripped-binary-or-object usr/lib/libsse.so
  W: helloworld: binary-without-manpage usr/bin/helloworld
  W: helloworld: maintscript-calls-ldconfig postinst
  W: helloworld: maintscript-calls-ldconfig postrm
  W: helloworld: package-name-doesnt-match-sonames libsse
  W: helloworld: shlib-without-versioned-soname usr/lib/libsse.so libsse.so
  ```

- Some things can be fixed easily by addin parameters to the CMake file

  ```diff
  + set(CPACK_PACKAGE_MAINTAINER "SSE lecturers")
  + set(CPACK_STRIP_FILES TRUE)
  ```

  `CPACK_PACKAGE_MAINTAINER` sets package maintainer and `CPACK_STRIP_FILES` make sure build files are stripped.

  Besides that one can add a changelog and a copyright file.
  `extended-description-is-empty` is requesting description of each component, i.e., the executable and the library. We do not provide information for each component at the moment.

- For some points it is harder to fix them
    - `package-must-activate-ldconfig-trigger`: Seems to be related how packages should be created and [CPack not respecting this yet](https://gitlab.kitware.com/cmake/cmake/-/issues/21834) (or I simply have an old version of CMake). CMake creates a maintainer script that calls `ldconfig` which should not be done anymore. Thus we get several error messages (1x ldconfig not called via trigger and 2x ldconfig called via maintainer script)
    - `shlib-without-versioned-soname`: No versioning of our library (e.g., `libsse.so -> libsse.so.0.1.0`) thus `shlib` cannot safely determine dependencies for software depending our library.
