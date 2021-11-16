
MlideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
  font-weight: bold;
      color: orange;
  }
  .reveal p {
      text-align: left;
  }
  .reveal section h1 {
      color: orange;
  }
  .reveal section h2 {
      color: orange;
  }
</style>

# Environment Variables, Paths and How to Find Them

---

## Introduction

---

## Some Standard Locations

- `/`
- `/usr/bin/`, `/bin`, `/sbin`, `/usr/local/bin`
- `/usr/lib`, `/usr/lib64`, `/usr/lib32`, `/usr/local/lib`
- `/etc/`
- `/share/`
- Structure mirrored under `/usr/local`

---

## Standard Paths and Environment Variables (general)

- `HOME` or `~`
- `PWD`
- `PATH`
- `CPATH`
- `LD_LIBRARY_PATH`
- `MANPATH`

---

## Standard Paths and Environment Variables (Python)

- `PYTHONPATH`

---

## Tools for Finding Libraries and Packages

- `ldconfig`
- `pkgconfig`
    - `pkg-conf`
    - `pkg-config`
