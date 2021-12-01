# Packages with CPack and Spack

This exercise is about packaging code with CPack and Spack. In this exercise we use adapted versions of the code from the previous week's exercise and create packages for it. The exercise is split into two parts: 1. CPack and 2. Spack. There are different GitHub repositories for the two subtasks.

At the end of the exercise you find a section with hints and remarks. Make sure to check this section.

Deadline: **Thursday, December 7th, 2021, 9:00**

## 1. CPack

**Attention/TODO**: Use [test repository](https://github.com/Simulation-Software-Engineering/cpack-exercise-test) for testing the exercise.

The ultimate goal is to have a CMake/CPack configuration that allows us to generate packages for different package formats. In this exercise we want to be able to create a `tar.gz` package and a Debian `deb` package. We want to package this [HelloWorld example from GitHub](https://github.com/Simulation-Software-Engineering/cpack-exercise). The example is based on the code from the previous week, but has relaxed requirements to `yaml-cpp`. This means you can use `libyaml-cpp-dev` from Ubuntu's package repository instead of compiling `yaml-cpp` yourself. In this exercise you should focus on the packaging aspect. Normally, there should be no need to adapt the compilation.

When setting up the package make sure that the executable `cpackexample` and also the library `cpackexamplelib` are build and installed in appropriate locations. You should also ensure that the header files for the library are installed properly. The package should contain enough information (at least maintainer, contact address, project description, vendor, version number, homepage). If you do not want to use your actual name/email address, please use your GitHub username and make up an email address). Running `make package` should automatically create `tar.gz` and `deb` package.

Additionally, for the Debian package, make sure that

- the executable is stripped, i.e., debug symbols should removed from the executable.
- the list of dependencies is generated automatically for the Debian package.
- the Debian package is generated with default file naming scheme.

Please use a suitable Docker container for this task. You should be able to reuse the Docker container from last week's exercise. The Docker container will be especially important if you want to work on the optional task

### Workflow (CPack)

- Create a fork of the [GitHub repository](https://github.com/Simulation-Software-Engineering/cpack-exercise).
- Adapt and create the files necessary to create packages via CPack.
- Also add your `Dockerfile` to the repository.
- Submit your code via a pull request. You can also open a (draft) pull request before you are incorporated all changes. In this case, do not forget to mark the pull request as ready to review when you are finished.
    - The pull request should be named `[USERNAME] CPack exercise`, e.g., `[jaustar] CPack exercise`.


## 2. Spack

**Attention/TODO**: Use [test repository](https://github.com/Simulation-Software-Engineering/spack-exercise) for pushing solutions. You will still have to build from the [public repository](https://github.com/Simulation-Software-Engineering/spack-exercise).

Now we want to package [another code](https://github.com/Simulation-Software-Engineering/spack-exercise) from Github. It is an adapted version of the previous week's exercise again. However, the `deal.ii` dependency has been removed as compiling `deal.ii` from scratch takes a very long time. Additionally, several releases with different depencies have been added.

The default name of your Spack package will be `spack-exercise` while the executable it produces is called `spackexample`. It also creates a library  `libspackexamplelib` (what a name) which is needed to run `spackexample`. Under normal circumstances you do not need to edit the CMake configuration for this exercise.

The [code repository](https://github.com/Simulation-Software-Engineering/spack-exercise) contains three releases:

- `v0.1.0` has no special dependencies. The C++ standard library is automatically included.
- `v0.2.0` depends on Boost (at least version `1.65.1`)
- `v0.3.0` depends on Boost (at least version `1.65.1`) and `yaml-cpp` (at least version `0.70.0`)

Create a Spack package for all releases the respect the dependencies appropriately. Make sure you also add yourself as maintainer to your package. Your final package should not contain any `FIXME` parts anymore.

### Workflow (Spack)

- Create a fork of the [GitHub repository](https://github.com/Simulation-Software-Engineering/spack-exercise).
- Adapt and create files as necessary to create the package via Spack.
- Please add a directory name `spack-exercise` inside the `spack` directory of the repository.
    - Inside the `spack-exercise` repository you should add the `package.py` of your Spack package.
- Please also add the `Dockerfile` you have used for the exercise if it has been adapted from the initial `Dockerfile` (see below). This `Dockerfile` should be in the root of the repository. Also add all other files you needed to create/edit to solve this task.
- Submit your code via a pull request. You can also open a (draft) pull request before you are incorporated all changes. In this case, do not forget to mark the pull request as ready to review when you are finished.
    - The pull request should be named `[USERNAME] Spack exercise`, e.g., `[jaustar] Spack exercise`.

It is strongly recommended to use work inside a Docker container. The directory `docker` includes a `Dockerfile` one may use as starting point for the exercise. It will come with Spack preinstalled (but **not** yet completely set up yet). Inside this container you are the `spackbuilder` user who does not have superuser rights. If you need superuser rights inside the container you can use the `sudo` command.

**Note**: You can also use the prebuilt Docker image as base for your Docker container. The image is available via [DockerHub](https://hub.docker.com/repository/docker/ajaust/spack-package-building-base) and is named `ajaust/spack-package-building-base`.

## Optional Tasks

If you work on any of the optional tasks, please mention this in your pull request.

### CPack

If you work on any of the optional tasks, please mention this in your pull request.

We want to automatize the package creation using a Docker container. Extend your Docker container image such that it automatically creates the Debian image without further user interaction. The Debian image should be copied to the directory `/mnt/package-build-dir` within the running container as `/mnt/package-build-dir` will be mounted at runtime of the container.

Ultimately, on will only run the following (or similar) command

```bash
docker run --rm -it --name cpack-packaging --mount type=bind,source="$(pwd)",target=/mnt/package-build-dir IMAGENAME
```

Please state the actual command to use in your pull request.

Running the container like this should trigger the preparation of the two packages. After the container is finished running, the files `PACKAGENAME.deb` and `PACKAGENAME.tar.gz` should be present on the host system but no `build` directory or similar, i.e., make sure the package is not created in the mounted drive. Please package `cpackexamplelib` as **shared** library when creating the packages.

### Spack

- Add the main branch of the GitHub repository [as version to the Spack recipe](https://spack.readthedocs.io/en/latest/packaging_guide.html#git).
- Make the current dependencies (`Boost`, `yaml-cpp`) optional by defining suitable options in the `CMakeLists.txt` which are also picked up in the C++ code. Then add corresponding variants in the Spack recipe.
- Create a Spack package for the Python code that you have packaged with pip. Checkout [Spack's documentation regaring the `PythonPackage`](https://spack.readthedocs.io/en/latest/build_systems/pythonpackage.html)  class for recipes if you want to work on this.

## Remarks and Tips

- If you need to specify a homepage, you can use the course homepage `https://simulation-software-engineering.github.io/homepage/`.
- All parts of the exercise should be ideally done on Docker container based on Ubuntu 20.04.
- If you are in a container and your libraries in `/usr/local/lib` are not found, you can extend the `LD_LIBRARY_PATH` accordingly.
- If you need an inspiration on how to write more complicated Spack recipes, you can check packages that are already shipped with spack (`spack edit PACKAGENAME` or browse).
- If you have `Boost` or `deal.ii` installed in the Docker container via `apt`, finding pre-installed packages using `spack external find` might fail. In this case you have to define the dependencies manually or run `spack external find` before installing the critical packages.
- Consider using the Docker image `ajaust/spack-package-building-base` as base for the Spack exercise which is available on [DockerHub](https://hub.docker.com/repository/docker/ajaust/spack-package-building-base).
- If you compile `Boost` via Spack this can take a short while. On our machines it took about 5 minutes. Normally, you should only have to compile it once.
- There is a `repo.yaml` file inside the `spack` directory. You can add [own Repositories](https://spack.readthedocs.io/en/latest/repositories.html) in Spack. However, you are not required to use this repository the exercise as this is meant for testing of your package.
