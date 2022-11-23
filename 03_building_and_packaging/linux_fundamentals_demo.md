# Notes for Some Fundamentals of Linux Systems Demo

## Static and Shared Linking

Example code is in [`building-and-packaging/material/examples/shared-and-static-c++`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/03_building_and_packaging/examples/shared-and-static-c++).

- This example is based on the C++ standard library to emphasize the difference between static and shared libraries.
- Show `main.cpp`, which uses standard lib
- Compile code:
    - Shared: `g++ main.cpp -o main-shared`
    - Static: `g++ -static main.cpp -o main-static`
- Run codes to show that they produce the same output:
    - `./main-static`
    - `./main-shared`
- Run `ldd` on `main-shared` and `main-static`.
    - There will several libraries linked to `main-shared`.
    - When using `ldd` on `main-static`, we get the message `not a dynamic executable`.
- Run `ls -lah` to show different executable sizes:

  ```bash
  $ ls -lah
  total 2.4M
  17K main-shared
  2.3M main-static
  ```

- `main-static` could be copied over to other systems, containers etc. where the standard library is not preinstalled.

## Filesystem Hierarchy Standard (FHS)

- `/`: primary root
- `/home`: contains user's home directories
- `/bin`: executables important for the system/OS
- `/sbin`: executables important for the system/OS to be executed by the super user
- `/usr/`: second hierarchy level containing things not required by the OS:
    - `/usr/lib/`
    - `/usr/bin/`, `/usr/sbin/`
    - `/usr/include/`
    - `/usr/local`: third level hierarchy level containing packages built manually
- ...and more directories. Details and meaning can be found on [homepage of FHS](https://refspecs.linuxfoundation.org/fhs.shtml).

## Environment Variables

Example code is in [`building-and-packaging/material/examples/environment-variables`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/03_building_and_packaging/examples/environment-variables).

- If necessary build Docker image: `docker build -t "demo_variables" .`
- Start docker container to have fresh system: `docker run -it demo_variables`
- Show file structure:
    - `ls`
    - `ls usr`
    - `ls usr/local`
- Show all environment variables: `env`
- Show script `print_my_environment_variable.sh`
- Use script:
    - `./print_my_environment_variable.sh` -> empty
    - `MY_ENV_VARIABLE="Hi students" ./print_my_environment_variable.sh` -> good
    - `echo $MY_ENV_VARIABLE` -> empty (dereference variable)
    - `./print_my_environment_variable.sh` -> empty
    - `MY_ENV_VARIABLE="Hi students"` and `echo $MY_ENV_VARIABLE` -> good
    - `./print_my_environment_variable.sh` -> empty
    - `export MY_ENV_VARIABLE="Hi students"` (share with child process)
    - `./print_my_environment_variable.sh` -> good
