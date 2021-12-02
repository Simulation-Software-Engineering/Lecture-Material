# Packaging with CPack

This exercise is about packaging code with CPack. We work with a simplified version of the code from the previous week's exercise and create packages for it.

At the end of the exercise you find a section with hints and remarks. Make sure to check this section.

Deadline: **Thursday, December 9th, 2021, 9:00**

## CPack and Packaging for Debian

The ultimate goal is to have a CMake/CPack configuration that allows us to generate packages for different package formats. In this exercise we want to be able to create a `tar.gz` package and a Debian `deb` package.


### Code to Package

We want to package this [CPack example code from GitHub](https://github.com/Simulation-Software-Engineering/cpack-exercise). It is based on the exercise code from last week and has the same dependencies (`Boost`, `deal.ii` and `yaml-cpp`). However, the compilation procedure has been set up already. Moreover, the `yaml-cpp` dependency is milder than last week since version `0.6.0` is new enough to compile the HelloWorld code. Therefore it is sufficient to install `libyaml-cpp-dev` from Ubuntu's package manager (`apt`) instead of compiling `yaml-cpp` yourself.

The `CMakeLists.txt` should look familiar. It has two targets

1. `cpackexample`: This target creates an executable with same name.
2. `cpackexamplelib`: This target creates a library (called `libcpackexamplelib.so` or `libcpackexamplelib.a`).

The executable will take one command line argument to specify a `yaml` file to be parsed. This allows to parse the file `config.yml` inside the `yamlParser/` directory even if the executable is not located within the repository anymore. In last week's exercise the path to `config.yaml` was hard coded. In this exercise you can call the program as

```bash
cpackexample <path_to_repo>/yamlParser/config.yml
```

If you start the program without the additional argument, the program will not try to parse anything.

### Development/Packaging Environment

Please work inside a Docker container when packaging the code. The image should be based on *Ubuntu 20.04* such that you have a consistent work environment. Such a container was also used when the exercise was prepared.

The code has (almost) the same dependencies as last week, Therefore, you can reuse your container most parts from the previous week's exercise's container, but install `libyaml-cpp-dev` via `apt` instead of compiling `yaml-cpp` manually.

The code in the repository should compile immediately. It is *not* part of the task to fix the compilation process. If you have problems compiling the code before changing, get in touch with us during the exercise or open a (draft) pull request and ask for help there. If you open a pull request, make sure to add the Dockerfile you have used so we can reproduce the problem.

### Packaging Steps

- Create a fork of the GitHub repository [CPack exercise](https://github.com/Simulation-Software-Engineering/cpack-exercise).
- Set up a `Dockerfile` to create a your packaging environment as described above. Add this file to the repository.
- Add the packaging procedure to the CMake configuration. You can do this step by step to make sure that the individual steps work.
    1. Add an appropriate installation routine to the project. The executable `cpackexample` should be installed in a `<prefix>/bin/` directory, the library `libcpackexamplelib.a/so` should be installed in a `<prefix>/lib/` directory and all header files (`fem.hpp`, `filesystem.hpp`, `flatset.hpp`, `yamlParser.hpp`) should be installed in a `<prefix>/include/cpackexamplelib` directory. This is also a good time to test whether `make install` works as expected.
    2. Add a packaging routine via `CPack`. Please write a seperate CMake module called `MyPackagingModule.cmake` for the packaging process and put it into a directory called `cmake/`. Make sure that the new file is added to Git. Don't forget to include this module in the `CMakeLists.txt` and double check that you can actually create packages with your configuration file.

       The created package should contain sufficient information about the package, at least: maintainer, contact address, project description, vendor, version number, homepage. Feel free to set [additional options](https://cmake.org/cmake/help/latest/module/CPack.html). If you set additional options, please mention in the pull request which options you set and why. You can create a `.tar.gz.` and a `deb` package already and verify that they contain the correct contents.
    3. Make sure that your compiled code [gets stripped](https://cmake.org/cmake/help/latest/module/CPack.html#variable:CPACK_STRIP_FILES) by default. Also ensure that executing `make package` creates (only) a `tar.gz` and a `deb` package.

       Optional: Create your package once with stripped and once with unstripped files. This should show a difference in the file size between the stripped and unstripped file. You can check the file size, for example, with `du -h FILENAME`.
    4. Extend the configuration for the generation of Debian packages. Make sure that the package file name is generated according to the Debian package naming scheme. Additionally, you should ensure that the dependencies of the Debian package are set appropriately.
    5. Make sure that you can install your `deb` package (`apt install ./DEBFILENAME`) and that you can run the executable `cpackexample`.
- Submit your code via a pull request. You can also open a (draft) pull request before you have incorporated all changes. This allows you to ask question if something is unclear. If you opened a draft pull request, do not forget to mark the pull request as ready to review when you are finished.
    - The pull request should be named `[USERNAME] CPack exercise`, e.g., `[ajaust] CPack exercise`.
    - Make sure that all files (`CMakeLists.txt`, `MyPackagingModule.cmake`, `Dockerfile`) are added to the repository and up-to-date.

## Optional Tasks

If you work on any of the optional tasks, please mention this in your pull request.

1. Inspect your Debian package with [lintian](https://manpages.ubuntu.com/manpages/trusty/man1/lintian.1.html). Check and save the output of `lintian`. Fix (some of) the errors. Please add the initial output of `lintian` and the final output such that one can see what errors/warnings disappeared. Shortly describe in the pull request what you did to get rid of errors.
2. We can automatize the package creation using a Docker container. The idea is that one starts the container via `docker run` which will then automatically build and save the created packages at a predefined location. No further user interaction should be necessary.

   Extend your Docker container image such that it automatically creates the Debian image without further user interaction. The Debian image should be copied to the directory `/mnt/package-build-dir` within the running container as `/mnt/package-build-dir` will be mounted at runtime of the container.

   Ultimately, one has to only run the following (or similar) command

   ```bash
   docker run --rm -it --mount type=bind,source="$(pwd)",target=/mnt/package-build-dir IMAGENAME
   ```

   Please state the actual command that has to be used with your container your pull request.

   Running the container like this should trigger the preparation of the two packages. After the container is finished running, the `tar.gz` and `deb` packages should be present on the host system. However, no `build` directory or other temporary files should be present on the host system, i.e., make sure the package is not created in the mounted drive. Please package `cpackexamplelib` as **shared** library when creating the packages.

## Remarks and Tips

- If you need to specify a homepage, you can use the course homepage `https://simulation-software-engineering.github.io/homepage/`.
- (Almost) All parts of the exercise should be ideally done inside a Docker container based on Ubuntu 20.04.
- If you are in a container and your libraries in `/usr/local/lib` are not found, you can add the path to environment variable `LD_LIBRARY_PATH` accordingly.
- For editing your fork inside a container you can mount the directory as bind mount when starting the container. Add `--mount type=bind,source=/path/to/repository/directory,target=/container/target/dir` to the command line when starting the container. Replace the paths with the paths you want to use.

  Example:
  Assuming you are in the repository's directory and want to mount it to the path `/mnt/package-build-dir` inside the container you could use a command looking similar to the following:

  ```bash
  docker run --rm -it --name CONTAINERNAME --mount type=bind,source="$(pwd)",target=/mnt/package-build-dir IMAGENAME
  ```

  Just make sure to use the correct image name (`IMAGENAME`).
- If you want to inspect the contents of a `.tar.gz.` file  you can unpack it using the tool `tar`. The unpacking command would look like this

  ```bash
  tar xzf TARGZFILE
  ```

- If you want to inspect the contents of a  `deb` file, you can unpack it using the tool `dpkg-deb`. The unpacking command would look like this

  ```bash
  dpkg-deb -R DEBFILE DIRECTORY_FOR_UNPACKED_DEBFILE
  ```
