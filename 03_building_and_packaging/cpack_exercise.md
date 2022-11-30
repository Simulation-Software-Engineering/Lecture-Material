# Packaging with CPack

Let us try to package the code from the CMake exercise with CPack, such that we can give the (binary) software to somebody else.

Deadline: **Thursday, December 8th, 2022, 9:00**

## Overview

- The goal of the exercise is to open a pull request from a fork of [the CPack exercise repository](https://github.com/Simulation-Software-Engineering/cpack-exercise-wt2223). Please name your pull request `Add installation and packaging targets`. In the pull request description, please explain what we need to do to test your code. If you work on any of the optional tasks below, please document in the description as well.
- The current state of the code is basically a solution of the CMake exercise from last week. For demonstration purpose the code is now, however, artificially split into a library `cpackexamplelib` and an executable `cpackexample`.
- Your task is to develop a CMake/CPack configuration that allows generating a `.tar.gz` and a Debian `.deb` package of our code. To this end, follow the same four steps as in the lecture (details below).

## Getting Started

1. Fork and clone the repository.
2. Build the Docker image: `docker build -t IMAGENAME .` (might take a few minutes, continue reading already)
3. Take a look at the `CMakeLists.txt` file. It should look familiar.
4. Once the Docker image is ready, run it and mount the current directory:
    - `docker run --rm -it --mount type=bind,source="$(pwd)",target=/mnt/cpack-exercise IMAGENAME`
5. In the Docker container: build the code and run `cpackexample`.

## Tasks

The same four steps as in the lecture:

### 1. Add Install Target to CMake Configuration

- The executable `cpackexample` should be installed in a `<prefix>/bin/` directory, the library `libcpackexamplelib.a/so` should be installed in a `<prefix>/lib/` directory, and all header files (`fem.hpp`, `filesystem.hpp`, `flatset.hpp`, `yamlParser.hpp`) should be installed in a `<prefix>/include/cpackexamplelib` directory.
- Test whether `make install` works as expected.

### 2. Add CPack Configuration

- Write a seperate CMake module `cmake/CPackConfig.cmake` for the packaging process and include it in the `CMakeLists.txt` file. The created package should contain sufficient information about the package, at least: maintainer, contact, project description, vendor, and homepage (e.g. your fork on GitHub). Feel free to set more [additional options](https://cmake.org/cmake/help/latest/module/CPack.html).
- `make package` should (only) create a `tar.gz` and a `deb` package.
- Inspect that both packages contain the correct content:
    - To inspect the contents of a `.tar.gz.` file, you can unpack it using the tool `tar`:

      ```bash
      tar -xzf TARGZFILE
      ```

    - To inspect the contents of a  `.deb` file, you can unpack it using the tool `dpkg-deb`:

      ```bash
      dpkg-deb -R DEBFILE DIRECTORY_FOR_UNPACKED_DEBFILE
      ```

- Optional: Do the dependencies look correct? Modify the Dockerfile such that `libyaml-cpp` also properly appears as dependency.

### 3. Create Debian Package

- Extend the configuration for the generation of Debian packages. Make sure that the package file name is generated according to the Debian package naming scheme.
- Make sure that you can install the Debian package (`apt install ./DEBFILENAME`) and that you can run the executable `cpackexample`. The executable should now be located in `/usr/bin`.

### 4. Check Debian Package

- Inspect your Debian package with [lintian](https://manpages.ubuntu.com/manpages/trusty/man1/lintian.1.html): `lintian ./DEBFILENAME`. Check and save the output (report in pull request).
- Make sure that your compiled code [gets stripped](https://cmake.org/cmake/help/latest/module/CPack.html#variable:CPACK_STRIP_FILES).
- Optional: Create your package once with stripped and once with unstripped files. This should show a difference in file size, which you can check, for example, with `du -h FILENAME`.
- Optional: Fix more errors and warnings (not necessarily all). Add the initial and the final output of `lintian` to the pull request such that we can see what errors or warnings disappeared. Briefly describe in the pull request what you did to get rid of errors and warnings.

## Optional Bonus Task

Let us completely automatize the package creation using the Docker image. Simply running a container via `docker run` should automatically build and save the created packages at a predefined location. No further user interaction should be necessary. Once the container exits, the `tar.gz` and `deb` packages should be present on the host system. However, no `build` directory or other temporary files should be present on the host system, i.e., make sure the package is not created in the mounted drive. Please package `cpackexamplelib` as **shared** library when creating the packages.

Extend the Dockerfile accordingly. Please state the actual command that has to be used to run the container in the pull request.
