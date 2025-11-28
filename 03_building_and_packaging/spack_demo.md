# Packaging for High-Performance Computing Demo Notes

It is recommended to do this demo in a fresh Docker container. To understand how Spack itself is installed, follow Step 1 in a fresh Ubuntu Noble container (`docker run --rm -it ubuntu:noble`).

To make things simpler from Step 2 onwards, create a container from the [spack/ubuntu-noble](https://hub.docker.com/r/spack/ubuntu-noble) image, so that Spack is preinstalled. Install a text editor (for e.g. vim) before running a Spack command.

## 1. Spack Setup/Installation

- This demo (and Spack) needs Python, Git, a C/C++ compiler, patch, make, tar, and a few more tools. Basically `build-essential`, `git`, and `python` on Ubuntu Noble.

- Get the Spack repository

  ```bash
  git clone -b v1.1.0 --depth=2 https://github.com/spack/spack.git
  ```

- Initializing Spack with

  ```bash
  . <spack_prefix>/share/spack/setup-env.sh
  ```

  will set `SPACK_ROOT` and also add `spack` to `PATH`. Note that the  `.` operator will run the commands in the supplied script as if we would type the commands supplied by the script in the shell ourselves. In bash the `.` operator is equivalent to `source`. However, `source` is not specified in POSIX and thus using `.` is likely to work on more platforms.

- Finish Spack setup

  ```bash
  spack compiler find
  ```

  This will find preinstalled compilers which is important. Without any compiler Spack is most likely useless as most packages need to be compiled.

  The command

  ```bash
  spack compilers
  ```

  prints the list of compilers that Spack has added.

- Find external packages

  ```bash
  spack external find
  ```

  This command tries to find preinstalled software packages which are also in Spack's package database. This way we do not have to recompile everything from scratch.

  Found packages (including version, configuration etc.) are stored in `~/.spack/packages.yaml`. There one can add further packages manually. Look at contents of this file.

- Concretize a spec to trigger bootstrap process

  ```bash
  spack spec zlib
  ```

  This will try to concretize the package and its dependencies. `clingo`, Spack's concretizer, is needed for this. Running `spack spec` for the first time triggers a bootstrapping process that installs `clingo`.

## 2. Package Installation/Management with Spack

- Inspect package properties

  ```bash
  spack info zlib
  ```

- Install the package

  ```bash
  spack install --reuse zlib
  ```

  This installs the package `zlib` by downloading and compiling it. `--reuse` tells spack to reuse already existing packages if possible.

- List installed packages

  ```bash
  spack find
  ```

  Checks the root environment and should show `zlib` being available now. Only `zlib` should be shown even if preinstalled software was found by `spack external find`. These external packages have not been added to the root environment of Spack **explicitly** yet and thus do not show up yet.

## 3. Spack Package Creation

- Create base package (boilerplate)

  ```bash
  spack create https://github.com/Simulation-Software-Engineering/HelloWorld/archive/refs/tags/v0.3.0.tar.gz
  ```

  Spack will fetch the archive and try to deduce some basic settings. It will also check for other releases and asks whether to add checksums. We want all checksums.

- Spack immediately drops you in a boilerplate package file

  ```Python
  class Helloworld(CMakePackage):
      """FIXME: Put a proper description of your package here."""

      # FIXME: Add a proper url for your package's homepage here.
      homepage = "https://www.example.com"
      url      = "https://github.com/Simulation-Software-Engineering/HelloWorld/archive/refs/tags/v0.3.0.tar.gz"

      # FIXME: Add a list of GitHub accounts to
      # notify when the package is updated.
      # maintainers = ['github_user1', 'github_user2']

      version('0.3.0', sha256='5e95bf1904ebfbd5c28b064bff098a3bb654bf7c407f2031295e3588d6d9e8fa')
      version('0.2.0', sha256='a77499bbfd0b8f4d7070b06c491e062fa608fdd7e939d6c37796bdafdbbaa35a')
      version('0.1.0', sha256='2e99e2ff2b955b9d17645367a0a7eeb485162d9336cdbf0034b9d95d464f3157')

      # FIXME: Add dependencies if required.
      # depends_on('foo')

      def cmake_args(self):
          # FIXME: Add arguments other than
          # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
          # FIXME: If not needed delete this function
          args = []
          return args
  ```

  At least the `FIXME` statements should be fixed before releasing the package. The Spack package recipe is written in Python so we can also do common Python magic here.

- Spack has deduced a good amount of information already.
    - We work with CMake
    - There are 3 releases of the software
    - The URL to download the package
    - The name of the package we work with `class Helloworld`. This is also the name of the software now within Spack.
- We want to fix/extend the package with some standard information.
    - Package description
    - Set URL to SSE homepage
    - Add GitHub username as maintainer
    - Remove the `cmake_args` part as there are only standard CMake arguments.

- Concretize the package

  ```bash
  spack spec helloworld
  ```

  `cmake` is an implicit dependency as we need it for building our package.

- If the same Docker container as in step 2 is used, make sure to uninstall `zlib` before installing `helloworld`.

- Make sure Spack finds external packages that `HelloWorld` needs

  ```bash
  spack external find
  ```

- Install package

  ```bash
  spack install helloworld
  ```

  and show package being available now via

  ```bash
  spack find
  ```

- Load installed package, run, and unload

  ```bash
  spack load helloworld
  helloworld
  spack unload helloworld
  ```

- Install different version

  ```bash
  spack install helloworld@0.2.0
  ```

  This will concretize (internally, i.e., no output on terminal) and then build the software.

- If one wants to edit the package later, there are two options

  ```bash
  spack edit helloworld
  ```

  or open `package.py` file in `.spack/package_repos/fncqgg4/repos/spack_repo/builtin/packages/helloworld/package.py`.

- Add the `main` branch as a version

  ```diff
  + git = "https://github.com/Simulation-Software-Engineering/HelloWorld.git"
  +
  + version("main", branch="main")
  ```

  This can also be used for `develop` branches etc. It is useful if the development state is required, or if one develops software using Spack.

- Add artificial dependencies

  ```diff
  + depends_on("python@3:", when="@0.3.0:")
  + depends_on("zlib@:1.2")
  ```

  This states that the package depends on Python version `3.0.0` or newer if we use `helloworld` of version `0.3.0` or newer. The software also requires at most `zlib` in version `1.2.10`

- Show new dependencies

  ```bash
  spack spec helloworld
  spack spec helloworld@0.2.0
  spack info helloworld
  ```

  The Python dependency will only show up for version `0.3.0`.

- Add an artificial variant

  ```diff
  - depends_on("python@3:", when="@0.3.0:")
  + variant("python", default=True, description="Enable Python support")
  + depends_on("python@3:", when="@0.3.0:+python")
  ```

  and check its existence

  ```bash
  spack info helloworld
  ```

  where Python now shows up as variant with its description. Python dependency is removed by doing

  ```bash
  spack info helloworld -python
  ```

## Further material

### References

- [Spack](https://spack.io/)
- [Spack docs](https://spack.readthedocs.io/en/latest/)
- [Spack 101 tutorials](https://spack-tutorial.readthedocs.io/en/latest/)
- [EasyBuild](https://github.com/easybuilders/easybuild)
- [EasyConfigs](https://github.com/easybuilders/easybuild-easyconfigs)
- [archspec project](https://github.com/archspec/)

### Interesting Talks On This Topic

FOSDEM talks:

- 2020: [Spack's new Concretizer](https://archive.fosdem.org/2020/schedule/event/dependency_solving_not_just_sat/)
- 2020: [Build for your microarchitecture: experiences with Spack and archspec](https://archive.fosdem.org/2020/schedule/event/archspec/)
- 2018: [Binary packaging for HPC with Spack](https://archive.fosdem.org/2018/schedule/event/llnl_spack/)
- 2018: ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
