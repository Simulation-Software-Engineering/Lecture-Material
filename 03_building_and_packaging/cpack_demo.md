# Notes for Installation and Packaging with CMake and CPack Demo

Example code is in [`03_building_and_packaging/examples/cpack`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/03_building_and_packaging/examples/cpack).

- Show `main.cpp`, `sse/*`: same example as last week
- Goal of this lecture: How can we give this software to somebody else in a proper way? Remember lecture on packaging for Python; now C++ code
- Build and start Docker container:
    - `docker build -t "cpack_demo"`
    - `docker run -it cpack_demo`

## Add Install Target to CMake Configuration

- Show `CMakeLists.txt`
- First observations:
    - We still build a library (`add_library`) and then an executable (`add_executable`).
    - We do this **for demonstration only**. There is normally no need handle internal dependencies in such a complicated way.
    - Build the code: We still get an executable `helloworld` and a library `libsse.a`.
- Changes compared to previous version / last week:
    - Version number, not needed yet (but later), but good practice
    - `set_target_properties`: Mark include files needed for `libsse` library (`sse/sse.hpp`) as publicly visible.
        - Needed such that CMake knows which headers should be public and should be installed. By default CMake assumes headers are for internal use (within the current project) only.
    - `target_include_directories`: Where do we have to look for the dependency depending on the type of build (internally, top-level cmake project, external dependency).
        - If there was a `src` directory, for example, mention it here (or `sse` and then don't mention above and in `main.cpp`).
        - Classic strategy for headers to put them again in a folder named after the project (such that they don't get mixed up).
        - We do not use the last two here, but they would be used if we created a package config file.
        - `$<...>` notation: generator expressions, variables are evaluated during build system generation
    - Include CMake macro `GNUInstallDirs` to get predefined variables such as installation directories. Directories names and their purpose are defined in the [GNU coding standard](https://www.gnu.org/prep/standards/html_node/Directory-Variables.html).
    - Create install targets (where to install to)
- Build the library and install it (when installing or distributing a package always set a `CMAKE_BUILD_TYPE`)

  ```bash
  mkdir build && cd build
  cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release ..
  make -j
  sudo make install
  ```

- Installs in `/usr/local` which is the default value of `CMAKE_INSTALL_PREFIX` when using CMake.

  ```bash
  -- Install configuration: "Release"
  -- Installing: /usr/local/bin/helloworld
  -- Installing: /usr/local/lib/libsse.so
  -- Installing: /usr/local/include/helloworld/sse.hpp
  ```

- Run it: `helloworld`
- `which helloworld`
- Set the prefix: `cmake -DCMAKE_INSTALL_PREFIX="../installation" -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release ..`, install again, `tree` the folder.

## Add CPack Configuration

- Packaging happens in separate CMake module called `CPackConfig.cmake`. Include it in `CMakeLists.txt`:

  ```diff
  + # Adding other cmake modules (standard like this)
  + set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
  + # Include our packaging module (standard like this)
  + include(CPackConfig)
  ```

- Look at `cmake/CPackConfig.cmake`:
    - Basically only definition of meta information
    - `CPack` should be included at the end so it can ingest all preset variables
- `cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release ..`
    - Creates new files `CPackConfig.cmake` and `CPackSourceConfig.cmake`
    - Look at `CPackConfig.cmake`: things we added and much more (same name, same content)
- Create package, e.g., `tar.gz`: `cpack -G TGZ`
    - If this fails, this is due missing a `README.md` and `LICENSE` file. CPack expects these file to be present.
    - `-G` is used to specify the package generator. We choose `TGZ` the generator for a compressed archive.
    - We obtain the resulting file `HelloWorld-0.1.0-Linux.tar.gz`. The file name consists of the project name, version number and installation target.
- Inspect the package: `tar -xzf HelloWorld-0.1.0-Linux.tar.gz` and `tree`
- `make clean`
- Build Debian package: `cpack -G DEB` ... builds again (no need to run `make` first) and complains: no dependencies set
- `make clean` and `make package`: many things get created. Set default:

  ```diff
  + set(CPACK_GENERATOR "TGZ;DEB")
  ```

- `make clean` and `make package` again

## Create Debian Package

- Set up Debian package generator by adding lines to `cmake/CPackConfig.cmake`:

  ```diff
  + # Debian packaging section
  + set(CPACK_DEBIAN_FILE_NAME DEB-DEFAULT)
  + set(CPACK_DEBIAN_PACKAGE_SHLIBDEPS YES)
  include(CPack)
  ```

- `CPACK_DEBIAN_FILE_NAME` sets the package name to follow the standard package naming scheme (see slides)
- `CPACK_DEBIAN_PACKAGE_SHLIBDEPS` tries to extract dependencies automatically. We can also set dependencies manually (`CPACK_DEBIAN_PACKAGE_DEPENDS`).
- `cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release ..` and `cpack -G DEB` ... no complaints
- Different package name: `helloworld_0.1.0_amd64.deb`
- Install the package: `sudo apt install ./helloworld_0.1.0_amd64.deb`
- `helloworld` and `which helloworld`: now `/usr`, not `/usr/local`, since we use package manager.

## Check Debian Package

- Package is already usable. Still, one might want to check quality.
    - If one wants to submit something to the actual repository of Ubuntu/Debian, then one has to follow standards.
- Inspect meta information `dpkg --info helloworld_0.1.0_amd64.deb`
- Check full content:

  ```bash
  dpkg-deb -R ./helloworld_0.1.0_amd64.deb ./helloworld-unpacked
  tree helloworld-unpacked
  ```

- Look at `DEBIAN/control` file: dependencies, meta data
- Check package via `lintian`: `lintian helloworld_0.1.0_amd64.deb`
- Many errors and warning, some easy to fix:

  ```diff
  # strip really all Debug symbols
  + set(CPACK_STRIP_FILES TRUE)
  ```

- Others harder to fix:
    - `package-must-activate-ldconfig-trigger`: Seems to be related how packages should be created and [CPack not respecting this yet](https://gitlab.kitware.com/cmake/cmake/-/issues/21834). CMake creates a maintainer script that calls `ldconfig`, which should not be done anymore. Thus we get several error messages (1x ldconfig not called via trigger and 2x ldconfig called via maintainer script)
