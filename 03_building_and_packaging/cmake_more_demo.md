# Notes for More CMake Demo

## Walk Through preCICE `CMakeLists.txt`

- [`CMakeLists.txt` on GitHub](https://github.com/precice/precice/blob/develop/CMakeLists.txt)
- First look around:
    - `CMakeLists.txt`: lengthy
    - `tree cmake`
    - If software should be usable (for everybody everywhere), building and packaging is a project by itself
- In `modules`: some `FindX.cmake`, partially third-party, partially developed by preCICE devs
- In `CMakeLists.txt`: `sources.cmake` included (around line 510)
    - No glob, but generated externally (some python script)
    - Look at `src/sources.cmake`
- Look at `CPackConfig.cmake`
- `cmake ..` and read through output

## CMake Curses Interface

- There are many tools around CMake, `ccmake` is also developed by KitWare
- Separate package on Ubuntu: `sudo apt-get install cmake-curses-gui`
- Delete previous build folder and start from scratch
- `ccmake ..`
- `[c]` if not yet configured before
- Change variable with `[enter]`, e.g. `CMAKE_BUILD_TYPE`
- Look at short description of options at the bottom
- `[t]` to show also CMake options, helpful to find out which variables exist
- `[c]` to configure again (because we changed something)
- `[g]` to generate `Makefile` and exit
