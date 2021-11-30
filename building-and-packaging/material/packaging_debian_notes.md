# Debian packages

*Learning goals*

- How to create a Debian (`deb`) package of your program/library.


## General package creation / Debian packages

| Duration | Format |
| --- | --- |
| 20 minutes | Slides |

- `deb` packages are common in the Linux world
    - Used by Debian its derivatives (such as Ubuntu)
- **TODO** Figure out how to build Debian packages
- Can be used to package packages of all kind


- [Ubuntu Packaging Tutorial](https://packaging.ubuntu.com/html/packaging-new-software.html)


- Create package with some problems
    - Missing changelog
    - Missing maintainer name (`CPACK_PACKAGE_MAINTAINER`)
    - Unstripped binaries and libraries (`CPACK_STRIP_FILES TRUE`)
- apt list | grep helloworld
- Files from debian package installed in `/usr` instead of `/usr/local`
- So name missing
    - Do I need to fix that?


- `lintian` errors

  ```bash
  E: helloworld: package-must-activate-ldconfig-trigger usr/lib/libsse.so
  W: helloworld: maintscript-calls-ldconfig postinst
  W: helloworld: maintscript-calls-ldconfig postrm
  ```

  Seems to be related how packages should be created and [CPack not respecting this yet](https://gitlab.kitware.com/cmake/cmake/-/issues/21834) (or I simply have an old version of CMake). CMake creates a maintainer script that calls `ldconfig` which should not be done anymore. Thus we get several error messages (1x ldconfig not called via trigger and 2x ldconfig called via maintainer script)

  - `extended-description-is-empty`: Yes, as we do not document each component (`libsee.so` and `helloworld`)

## General package creation / Debian packages - Example

| Duration | Format |
| --- | --- |
| 5 minutes | Demo |

