# Packages with Spack

This exercise is about packaging code with Spack. We work with a simplified version of the code from the previous week's exercise and create packages for it.

At the end of the exercise you find a section with hints and remarks. Make sure to check this section.

Deadline: **Wednesday, December 4th, 2024, 09:00**

## Creation of a Spack Package

We want to package the [Spack example code on GitHub](https://github.com/Simulation-Software-Engineering/spack-exercise). It is an adapted version of the last week's exercise. The `deal.ii` dependency has been removed as compiling `deal.ii` from scratch takes too long. Additionally, several releases with different dependencies have been added. The code in the repository creates an executable that is called `spackexample`. It also creates a library  `libspackexamplelib` (what a name) which is needed to run `spackexample`.

The default name of your Spack package is `spack-exercise`. The Spack package should create the executable `spackexample` and the corresponding library `libspackexamplelib` mentioned above. Under normal circumstances you do not need to edit the CMake configuration for this exercise.

The [code repository](https://github.com/Simulation-Software-Engineering/spack-exercise) is slightly different from the previous repositories. It contains three releases of the code with increasing number of dependencies:

- `v0.1.0` has no special dependencies. The C++ standard library is automatically included.
- `v0.2.0` depends on Boost (at least version `1.65.1`)
- `v0.3.0` depends on Boost (at least version `1.65.1`) and `yaml-cpp` (at least version `0.7.0`)

**Note**: We require `yaml-cpp` in version `0.7.0`. This package will be automatically installed via Spack if you specify the dependency correctly in you package. You should **not** install `yaml-cpp` manually in this exercise.

Create a Spack package for all releases of the given code and make sure that the dependencies are specified appropriately. Make sure you also add yourself as maintainer to your package. Your final package should not contain any `FIXME` parts.

### Development/Packaging Environment

Please do all the development inside a Docker container. The Docker container is based on the image built from the recipe provided in the [exercise repository](https://github.com/Simulation-Software-Engineering/spack-exercise). You can find the recipe of the image inside the `docker/` directory. The image itself is based on Ubuntu 20.04 and has the Boost dependency preinstalled. Additionally, Spack has been set up in the recipe. Two editors `vim` and `nano` are preinstalled. If you want to install further software in your container you are free to do so.

**Note for MacOS users**: While building the Docker image, you may have to add the flag `--platform=linux/amd64`.

### Packaging Steps

- Create a fork of the [GitHub repository](https://github.com/Simulation-Software-Engineering/spack-exercise).
- Get acclimatized with the Docker container that you have just created:
    - Inside the container you are the user `spackbuilder`. This user is not root, but you can use `sudo` (without password) if you want to install something inside the container. However, you should not need superuser rights for this exercise.
    - In the home directory you will find a directory called `spack/` which contains a current Spack installation.
    - There is also a hidden directory `.spack/` in the home directory which contains some configuration files for Spack. The file `packages.yaml`, e.g., defines the preinstalled software like Boost or CMake such that Spack does not compile them from scratch. During this exercise, there should be no need to edit any of the files inside `.spack/`.
    - Spack's initialization procedure has been added to the `.bashrc` file so you can immediately start using Spack. Verify the Spack setup by running `spack spec yaml-cpp`. This command should concretize (i.e., resolve the dependencies of) `yaml-cpp`.

- Create the base package template via `spack create`. Make sure that all three released versions are added to the Spack package. If a version is missing, you can also add it manually later.

  **Note 1**: When specifying the URL to the software, you need to use the URL of the original repository name [`spack-exercise`](https://github.com/Simulation-Software-Engineering/spack-exercise). Sometimes the versions are not correctly detected from the original repository name. In case this happens, use the URL of one version, for example [v0.1.0](https://github.com/Simulation-Software-Engineering/spack-exercise/releases/tag/v0.1.0) of the original repository. Spack will then detect the respective version. To add more versions, change the URL accordingly. Packaging the code from your fork will fail because the releases are forked only partially. In your fork the archives, i.e., the `zip` and `tar.gz` files, will be missing.

  **Note 2**: Spack will open the created package file automatically in an editor. If you want to use a different editor or want to edit the package later, you can find the package file in `${HOME}/spack/var/spack/repos/builtin/packages/spack-exercise/package.py` (inside the container).

    - Verify that the class name of the package is `SpackExercise`.
    - Verify that all three releases are listed.
    - Go through the `FIXME` sections and fill them in accordingly, but leave out the `depends_on` part for the moment.
        - Add the course homepage `https://simulation-software-engineering.github.io/homepage/` as homepage.
        - Add your *GitHub* username as maintainer.
        - You do not have to specify  additional arguments to `CMake` such that the `cmake_args` function can be removed.
    - Check the output of `spack info spack-exercise` and make sure that it makes sense.
    - You already should be able to build/install the `0.1.0` version of our package with

      ```bash
      spack install spack-exercise@0.1.0
      ```

      Afterwards, you can check whether the package works as expected. You can load the package with

      ```bash
      spack load spack-exercise@0.1.0
      ```

      such that you can call `spackexample` afterwards:

      ```bash
      $ spackexample
      Let's fight with CMake, Docker, and some dependencies!
      ```

      If this looks fine, you unload the package.

      ```bash
      spack unload spack-exercise@0.1.0
      ```

- Add the dependencies for the `0.2.0` and `0.3.0` release of our code to the package (`depends_on`).
    - Make sure that only `0.3.0` depends on `yaml-cpp`.
    - Verify that you can install and use `spack-exercise@0.2.0` and `spack-exercise@0.3.0`. There is a `config.yml` file inside the `yamlParser` directory that you should be able to parse with `spack-exercise@0.3.0` with a command like

      ```bash
      spackexample <path_to_repo>/yamlParser/config.yml
      ```

    - Check the output of `spack info spack-exercise` and make sure that it makes sense. The additional dependencies (`yaml-cpp` and `Boost`) should appear in the output.
- If everything works as expected, copy the `package.py` file from the container into your fork of the GitHub repository and add the file to the repository.  You should find the file in `${HOME}/spack/var/spack/repos/builtin/packages/spack-exercise/`.
    - If there is a problem with the ownership of the file `package.py` on your host, you can change the owner of the file with `chown`.
    - **Note**: Do not delete the container before you have copied the `package.py`. Otherwise, the file will be lost and you have to start from the beginning.
- Submit your code via a pull request.
    - The pull request should be named `[USERNAME] Spack exercise`, e.g., `[desaiin] Spack exercise`. Please use the GitLab username here.
    - If you have extended the Docker recipe while doing the exercise, please also push the Dockerfile changes. Otherwise the only change should be an additional `package.py` file.

## Optional Tasks

If you work on any of the optional tasks, please mention this in your pull request.

- Add the main branch of the GitHub repository [as version to the Spack recipe](https://spack.readthedocs.io/en/latest/packaging_guide.html#git).
- Make the current dependencies (`Boost`, `yaml-cpp`) optional by defining suitable options in the `CMakeLists.txt` which are also picked up in the C++ code. Then add corresponding variants in the Spack recipe which allow to turn on/off these features.
- Create a Spack package for the Python code that you have packaged with pip. Checkout [Spack's documentation regarding the `PythonPackage`](https://spack.readthedocs.io/en/latest/build_systems/pythonpackage.html) class for recipes if you want to work on this.

## Remarks and Tips

- Under normal circumstances, the only packages Spack should compile are `yaml-cpp` and `spack-exercise`. All other dependencies are preinstalled and should be preconfigured.
    - If Spack tries to compile further packages, you could try to enforce reuse of preinstalled packages with `spack install --reuse PACKAGENAME`.
- You can open the recipe of your Spack package with `spack edit spack-exercise`. It uses the editor specified by the environment variable `EDITOR`.
- Inside the container the two editors `nano` and `vim` are preinstalled.
- You inspect your recipe with `spack info spack-exercise`.
- If you need an inspiration on how to write more complicated Spack recipes, you can check packages that are already shipped with Spack (`spack edit PACKAGENAME` or browse).
