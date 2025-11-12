---
type: slide
slideOptions:
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

# Introduction to Packaging

---

## Learning Goals of Chapter

- Explain why software is packaged.
- Create a distributable package of a Python code, publish on PyPI, and install with pip.
- Understand the difference between static and dynamic libraries and common ways of installation on Linux.
- Build C++ software and handle dependencies with Make and CMake.
- Package C++ software with CPack and create Debian packages.
- Create Spack packages, e.g., for high-performance computing systems with restricted access rights.

---

## What is Packaging?

- Bare code is often hard to understand for everyone except the developer(s).
- Packaging is a workflow to convert a code into a standardized distributable software.
- A code can be standardized in various ways. For example, by ...
    - ... providing an installation recipe, for example, using CMake / make.
    - ... bundling it into an app or software with a user interface.
    - ... packaging it according to an existing standard.
- We discuss **packaging a code according to an existing standard**.

---

## Why Package Code? 1/2

- A code with many files typically has difficulties like
    - multiple dependencies and requirements of specific versions of dependencies.
    - intricate compilation / installation steps which are hard to get right.
    - missing or limited starting information / documentation, which means a high entry barrier.

---

## Why Package Code? 2/2

- Create a package to
    - benefit from a package index or package manager which is familiar to a broad audience.
    - benefit from automated handling of dependencies of package managers.
    - have ease of distribution and maintenance due to standardization.
    - increase overall usability and sustainability of your code.

---

## How to Package Code?

- First step is finding the right standard for your code.
- There are several options:
    - Linux package managers: apt, dpkg, yum, RPM, etc.
    - [CMake](https://cmake.org/)
    - [Spack](https://spack.io/)
    - [Conan](https://conan.io/)
    - [pip](https://pypi.org/project/pip/)
    - [Conda](https://docs.conda.io/en/latest/)
    - and many more ...

---

## Why Packaging a Python Code?

- Python is easy to understand and widely used in research software.
- Well established package managers and packaging tools already exist in the Python community.
- Many famous examples: [NumPy](https://pypi.org/project/numpy/), [SciPy](https://pypi.org/project/scipy/), [PyTorch](https://pypi.org/project/torch/).

---

## Key Takeaways

- Packaging or creating build recipe of a code is a standardized process.
- Many options in packaging / building tools.
- Most of these tools / methods are customized for use cases.
- In this lecture, we concentrate on packaging of Python code.
