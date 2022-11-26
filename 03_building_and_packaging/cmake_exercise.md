# Let's Fight With CMake, Docker, and Some Dependencies

In this exercise, we need to fight. Not everything always works smoothly. This is the only way to really learn how to juggle with dependencies using CMake. We build a program that uses common, representative dependencies as often used in simulation software. We are not so much interested in the program itself, but in what steps are necessary to build the program.

To get an independent and reproducible environment as common ground, we use and, thus repeat, Docker.

Deadline: **Thursday, December 1st, 2022, 9:00**

## Overview

- The goal of the exercise is to open a pull request from a fork of [the CMake exercise repository](https://github.com/Simulation-Software-Engineering/cmake-exercise-wt2223). Please name your pull request `Add building and container recipes` and assign yourself. In the pull request description, please explain what we need to do to test your code.
- Your should add a `Dockerfile` and a `CMakeLists.txt`, besides some minor changes in `main.cpp` like commenting in some code parts. It should be possible to create an executable container from your pull request. Inside the container, one should be able to directly build the C++ code (`main.cpp`) using CMake. Use as many of the currently commented-out additional files, which induce additional dependencies.

## First Steps

1. Fork and clone the repository, have a look at the `main.cpp` and the `README.md`.
2. Build `main.cpp` manually (e.g. `g++ main.cpp -o main`) and run the executable (`./main`).
3. Build a Docker image, run a container (in interactive mode), and repeat steps 1 and 2 within the container.

## Repository Structure

The bare `main.cpp` uses several additions, which are located in the following subdirectories, each containing a `cpp` and a `hpp` file with the same name.

- `flatset` adds a function to create and modify a flat set using [Boost Container](https://www.boost.org/doc/libs/1_80_0/doc/html/container.html) and outputs the set. This example is adapted from a [cppsecrets blog post](http://cppsecrets.com/article.php?id=2834).
- `filesystem` adds a function to inspect and output the current directory using [Boost Filesystem](https://www.boost.org/doc/libs/1_75_0/libs/filesystem/doc/index.htm). This example is adapted from [tutorial 4](https://www.boost.org/doc/libs/1_80_0/libs/filesystem/example/tut4.cpp) of Boost Filesystem.
- `fem` defines a class to solve the Poisson problem with the finite-element method (FEM) using [deal.II](https://www.dealii.org/). Output is written to a file `solution.vtk`, which can be visualized with, for example, [Paraview](https://www.paraview.org/). This example is adapted from the [tutorial step 3](https://dealii.org/current/doxygen/deal.II/step_3.html) of deal.II.
- `yamlParser` adds a function to parse a simple yaml file using [yaml-cpp](https://github.com/jbeder/yaml-cpp) and to output the value of the key `version`. The folder also contains an example file `config.yml`.

Further resources:

- `inittimezone`: A bash script that comes handy when inheriting from Ubuntu Docker images. More information on what to do with it below.

## CMake

Please choose a meaningful project name. As target name, use `main`. We recommend to follow best practice and create a `build` directory at the root level from which `cmake ..` is called.

## Docker Setup

The code and all dependencies should run in a Docker container based on the `ubuntu:22.04` image. As by now, you already know how to set up a basic Docker container, we do no longer provide detailed instructions. We recommend to build the Dockerfile incrementally. Start with a rather empty one and install dependencies manually in the interactive mode. Take notes of the commands you use, so you can integrate them into the Dockerfile afterwards and rebuild your image.

To prevent the image from asking the timezone in some dialog, use ...

```docker
COPY inittimezone /usr/local/bin/inittimezone
RUN inittimezone
```

... **before** you install new packages. Otherwise the Docker image creation will be stuck at a point that requires user interaction while it is not possible to interact with the process. You might need make `inittimezone` executable first: `chmod +x inittimezone`.

Some standard packages available on Aptitude might come handy:

- `build-essential`
- `cmake`
- `git`
- `wget`
- `vim`

## Dependencies

Add dependencies one by one: Comment in the parts of `main.cpp` that are connected to a specific dependency. Then, install the dependency and extend the `CMakeLists.txt`. Verify that you can build and run the executable. If everything works, go on and include the next dependency.

- Maybe start with the boost dependencies. Boost Container is a header-only dependency, Boost Filesystem needs to be linked. Both are available in `libboost-all-dev`. There is a CMake module to [find boost libraries](https://cmake.org/cmake/help/latest/module/FindBoost.html).
- deal.II is available in `libdeal.ii-dev`. deal.II uses some fancy [CMake macros](https://www.dealii.org/current/users/cmake_user.html).
- yaml-cpp is an optional bonus task. For some arbitrary reason, we are not happy with the latest release of the software (which would be available through Aptitude), but we want to use the current `master` branch [directly from GitHub](https://github.com/jbeder/yaml-cpp). Get it via `git clone`, and build and install (`make install`) it yourself. Do not forget to add the necessary instructions to the Dockerfile. Sometimes containers behave weirdly: If libraries in `/usr/local/lib` are not found by CMake, please add the path to the environment variable `LD_LIBRARY_PATH`.
