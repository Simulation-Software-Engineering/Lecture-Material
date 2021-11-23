# Let's fight with CMake, Docker, and some dependencies

In this exercise, we need to fight. Not everything always works smoothly. This is the only way to really learn how to juggle with dependencies using CMake. We build a program that uses standard or representative dependencies as often used in simulation software. We are not so much interested in the program itself, but in what steps are necessary to get it built.

To get an independent and reproducible environment as common ground, we use and, thus repeat, Docker.

Deadline: **Thursday, December 2nd, 2021, 9am**

## Overview

- Your overall goal is to open a pull request from a fork to [this repository](https://github.com/Simulation-Software-Engineering/cmake-exercise-test/) (TODO: update link) adding a `Dockerfile` and a `CMakeLists.txt`, besides minor changes in `main.cpp` uncommenting some code parts. Please name your pull request `<GitLab-USERNAME> Add building and container recipes`. With your pull request, building and running the docker container, one should be able to directly build the code skeleton within the container using CMake. As many of the currently commented-out dependencies as possible should be supported.

## First steps

- For and clone the repository, have a look at the `main.cpp` and the README.
- Then, build `main.cpp` manually (e.g. `g++ main.cpp -o main`) and run the program (`./main`).

## Tips / remarks

- **Docker**: As by now, you already know how to set up a basic Docker container, we do no longer provide detailed instructions. Please note the guidelines in the README. We recommend to build up the image incrementally. Start with a rather empty one, install dependencies manually in the interactive mode, and take notes of the commands your use. Once, you know what you want to do, add the commands to the Dockerfile and rebuild your image.
- **Dependencies**: Also add dependencies one by one: Uncomment the necessary part of `main.cpp`, install the dependency, write the CMake part, build and run. If everything works, go to the next dependency. Maybe start with the boost dependencies. `boost container` is a header-only dependency, `boost filesystem` needs to be linked.
- **CMake**:
    - Please follow good practice and create a `build` directory at the root level from which you call `cmake ..`. There is a hard-coded path `../yaml/config.yml` in `yaml/yaml.hpp`. If you use a non-standard location for your `build` directory, you have to adapt this path.
    - deal.II uses some fancy [CMake macros](https://www.dealii.org/current/users/cmake_user.html).
    - There is a CMake module to [find boost libraries](https://cmake.org/cmake/help/latest/module/FindBoost.html).
- **Bonus**: `yaml-cpp` is the optional bonus task. Do this one last. We want to use the newest version `0.7.0`, which is not available through Aptitude. To get it directly from GitHub, you can use `wget` (or `git clone`). Afterwards, build and install (`make install`) yourself. Do not forget to add the necessary instructions to your Dockerfile.
- **Functionality**: If you are interested in what the program actually does, have a look at the code and the links given in the README. But this is not our main focus here.
