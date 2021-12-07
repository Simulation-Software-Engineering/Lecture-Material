# Packages with Spack

This exercise is about packaging code with Spack. We work with a simplified version of the code from the previous week's exercise and create packages for it.

At the end of the exercise you find a section with hints and remarks. Make sure to check this section.

Deadline: **Thursday, December 16th, 2021, 9:00**

## Spack

**Attention/TODO**: Use [test repository](https://github.com/Simulation-Software-Engineering/spack-exercise) for pushing solutions. You will still have to build from the [public repository](https://github.com/Simulation-Software-Engineering/spack-exercise).

Now we want to package [another code](https://github.com/Simulation-Software-Engineering/spack-exercise) from Github. It is an adapted version of the previous week's exercise again. However, the `deal.ii` dependency has been removed as compiling `deal.ii` from scratch takes a very long time. Additionally, several releases with different depencies have been added.

The default name of your Spack package will be `spack-exercise` while the executable it produces is called `spackexample`. It also creates a library  `libspackexamplelib` (what a name) which is needed to run `spackexample`. Under normal circumstances you do not need to edit the CMake configuration for this exercise.

The [code repository](https://github.com/Simulation-Software-Engineering/spack-exercise) contains three releases:

- `v0.1.0` has no special dependencies. The C++ standard library is automatically included.
- `v0.2.0` depends on Boost (at least version `1.65.1`)
- `v0.3.0` depends on Boost (at least version `1.65.1`) and `yaml-cpp` (at least version `0.7.0`)

Create a Spack package for all releases the respect the dependencies appropriately. Make sure you also add yourself as maintainer to your package. Your final package should not contain any `FIXME` parts anymore.

### Packaging Steps

- Create a fork of the [GitHub repository](https://github.com/Simulation-Software-Engineering/spack-exercise).
- Adapt and create files as necessary to create the package via Spack.
- Please add a directory named `spack-exercise` inside the `spack` directory of the repository.
    - Inside the `spack-exercise` repository you should add the `package.py` of your Spack package.
- Please also add the `Dockerfile` you have used for the exercise if it has been adapted from the initial `Dockerfile` (see below). This `Dockerfile` should be in the root of the repository. Also add all other files you needed to create/edit to solve this task.
- Submit your code via a pull request. You can also open a (draft) pull request before you are incorporated all changes. In this case, do not forget to mark the pull request as ready to review when you are finished.
    - The pull request should be named `[USERNAME] Spack exercise`, e.g., `[jaustar] Spack exercise`. Please use the GitLab username here.

It is strongly recommended to work inside a Docker container. The directory `docker` includes a `Dockerfile` one may use as starting point for the exercise. It will come with Spack preinstalled (but **not** yet completely set up). Inside this container, you are the `spackbuilder` user who does not have superuser rights. If you need superuser rights inside the container you can use the `sudo` command.

**Note**: You can also use the prebuilt Docker image as base for your Docker container. The image is available via [DockerHub](https://hub.docker.com/repository/docker/ajaust/spack-package-building-base) and is named `ajaust/spack-package-building-base`.

## Optional Tasks

If you work on any of the optional tasks, please mention this in your pull request.

- Add the main branch of the GitHub repository [as version to the Spack recipe](https://spack.readthedocs.io/en/latest/packaging_guide.html#git).
- Make the current dependencies (`Boost`, `yaml-cpp`) optional by defining suitable options in the `CMakeLists.txt` which are also picked up in the C++ code. Then add corresponding variants in the Spack recipe.
- Create a Spack package for the Python code that you have packaged with pip. Checkout [Spack's documentation regaring the `PythonPackage`](https://spack.readthedocs.io/en/latest/build_systems/pythonpackage.html)  class for recipes if you want to work on this.

## Remarks and Tips

- If you need to specify a homepage, you can use the course homepage `https://simulation-software-engineering.github.io/homepage/`.
- All parts of the exercise should be ideally done on Docker container based on Ubuntu 20.04.
- If you are in a container and your libraries in `/usr/local/lib` are not found, you can extend the `LD_LIBRARY_PATH` accordingly.
- If you need an inspiration on how to write more complicated Spack recipes, you can check packages that are already shipped with spack (`spack edit PACKAGENAME` or browse).
- Consider using the Docker image `ajaust/spack-package-building-base` as base for the Spack exercise which is available on [DockerHub](https://hub.docker.com/repository/docker/ajaust/spack-package-building-base).
- If you compile `Boost` via Spack this can take a short while. On our machines it took about 5 minutes. Normally, you should only have to compile it once.
- There is a `repo.yaml` file inside the `spack` directory. You can add [own Repositories](https://spack.readthedocs.io/en/latest/repositories.html) in Spack. However, you are not required to use this repository the exercise as this is meant for testing of your package.
