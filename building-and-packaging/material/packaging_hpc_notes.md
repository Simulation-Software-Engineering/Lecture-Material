# Packaging for High-Performance Computing (Notes)

## Spack Package Creation

- Finish Spack setup

  ```
  spack compiler find
  spack external find
  ```

  This will find preinstalled compilers and further software. This way we do not have to recompile everything from scratch.

  **Note** `spack external find` is an experimental feature and might fail. System packages [can be defined manually](https://spack.readthedocs.io/en/latest/getting_started.html#system-packages).

- Install a simple example package

  ```bash
  spack spec zlib
  ```

  This will trigger the bootstrap process of Spack. It installs `clingo`, the dependency resolver.

  ```bash
  spack install --reuse zlib
  ```

  Will now install the package `zlib` by downloading and compiling it. `--reuse` tells it to reuse package that exist already if possible

  ```bash
  spack find
  ```

  will show `zlib` being available now and only `zlib` as the preinstalled software has not been used/added to the root environment of Spack yet.

- Create base package (boilerplate)

  ```bash
  spack create https://github.com/Simulation-Software-Engineering/HelloWorld/archive/refs/tags/v0.3.0.tar.gz
  ```

  Spack will fetch the archive and try to deduce some basic settings. It will also check for other releases and asks whether to add checksums. We wann all checksums.

- Afterwards Spack drops us in the boilerplate package.

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

  At least the `FIXME` statements should be fixed before relasing the package. The Spack package recipe is written in Python so we can also do common Python magic here.

- Spack has deduced a good number of information already.
    - We work with CMake
    - There are 3 releases of the software
    - The URL to download packages
    - The name of the Package we work with `class Helloworld`. This is also the name of the software now within Spack.
- We want to fix/extend the package with some standard information
    - Package description
    - Set URL to SSE homepage
    - Add our GitHub username as maintainer
    - Remove the `cmake_args` part as we only have a standard CMake arguments. Here could give extra/special arguments specific to the software package.
- Concretize our package

  ```bash
  $ spack spec helloworld
  Input spec
  --------------------------------
  helloworld

  Concretized
  --------------------------------
  helloworld@0.3.0%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-ubuntu20.04-skylake
    ^cmake@3.16.3%gcc@9.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release patches=1c540040c7e203dd8e27aa20345ecb07fe06570d56410a24a266ae570b1c4c39,bf695e3febb222da2ed94b3beea600650e4318975da90e4a71d6f31a6d5d8c3d arch=linux-ubuntu20.04-skylake
  ```

  We see that `cmake` is an implicit dependency as we need it for building our package.

- Install package

  ```bash
  spack install helloworld
  ```

- Load installed package, run code and unload

  ```bash
  spack load helloworld
  helloworld
  spack unload helloworld
  ```

- Install different version of code

  ```bash
  spack install helloworld@0.2.0
  ```

  This will concretize (internally, i.e. no output on terminal) and then build the software.

- Add `main` branch and thus GitHub repository

  ```diff
  + git      = "https://github.com/Simulation-Software-Engineering/HelloWorld.git"
  +
  + version('main', branch='main')
  ```

- If one wants to edit the package later, there are two options

  ```bash
  spack edit helloworld
  ```

  or open `package.py` file in `${HOME}/var/spack/repos/builtin/packages/helloworld/`

- Add artifical dependencies

  ```diff
  + depends_on('python@3:', when='@0.3.0:')
  + depends_on('zlib@:1.2')
  ```

  Means that the package depends on Python `3.0.0` or newer and newer if we use `helloworld` of version `0.3.0` or newer. The software also requires at most `zlib` in version `1.2.10`

    - Show new dependencies

      ```bash
      spack spec helloworld
      spack spec helloworld@0.2.0
      ```

      The Python dependency will only show up for the newest version of our software package.

- Add an artificial variant

  ```diff
  + variant('python', default=True, description='Enable Python support')
  - depends_on('python@3:', when='@0.3.0:')
  + depends_on('python@3:', when='+python')
  ```

  and check its existence

  ```bash
  spack info helloworld
  ```

  where Python now shows up as variant with its description. We can deactivate Python by specifying

  ```bash
  spack info helloworld -python
  ```

  `~` can be (often) used instaed of `-`. There are [examples in the documentation](https://spack.readthedocs.io/en/latest/basic_usage.html#variants).

## Further reading

### References

- [EasyBuild](https://github.com/easybuilders/easybuild)
- [EasyConfigs](https://github.com/easybuilders/easybuild-easyconfigs)
- [Spack](https://spack.io/)
- [Spack docs](https://spack.readthedocs.io/en/latest/)
- [Spack 101 tutorials](https://spack-tutorial.readthedocs.io/en/latest/)
- [archspec project](https://github.com/archspec/)

### Talks

- Talks at FOSDEM
    - 2020: [Spack's new Concretizer](https://archive.fosdem.org/2020/schedule/event/dependency_solving_not_just_sat/)
    - 2020: [Build for your microarchitecture: experiences with Spack and archspec](https://archive.fosdem.org/2020/schedule/event/archspec/)
    - 2018: [Binary packaging for HPC with Spack](https://archive.fosdem.org/2018/schedule/event/llnl_spack/)
    - 2018: ["How To Make Package Managers Cry"](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)
