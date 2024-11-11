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

## Learning goals of chapter

- Explain why software is packaged.
- Create Python packages, publish on PyPI, and install with pip.
- Understand the difference between static and dynamic libraries and common ways of installation on Linux.
- Build C++ software and handle dependencies with Make and CMake.
- Package C++ software with CPack and create Debian packages.
- Create Spack packages, e.g., for high-performance computing systems with restricted access rights.

---

## What is packaging?

- Bare code is often hard to understand for everyone except the developer(s).
- Packaging is a workflow to convert a code into a standardized distributable software.
- A code can be standardized in various ways. Some examples are
    - creating a compact form by following a standardization.
    - providing an installation recipe, for example, using CMake / make.
    - bundling code into an app or software with some UI.
- We discuss **creating a compact form by following a standardization**.

---

## Why should we package code? 1/2

- A bare code with many files typically has difficulties like
    - multiple dependencies and requirements of specific versions of dependencies.
    - intricate compilation / installation steps which are hard to get right.
    - missing or limited starting information / documentation, which means a high entry barrier.

---

## Why should we package code? 2/2

- Create a package to
    - benefit from a package index or package manager which is familiar for a broad audience.
    - benefit from automated handling of dependencies of package managers.
    - have ease of distribution and maintenance due to standardization.
    - increase overall usability and sustainability of your code.

---

## How to package code?

- First step is finding the right standard for your code.
- There are several options:
    - One of the many Linux package managers: apt, dpkg, yum, RPM and many more ...
    - [CMake](https://cmake.org/) <span>: building / installation / packaging tool mostly for C, C++ projects<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Spack](https://spack.io/) <span>: a package management tool mostly for supercomputing centers<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Conan](https://conan.io/) <span>: open-source package manager for C and C++ development<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [PyPI](https://pypi.org/) and [pip](https://pypi.org/project/pip/)
    - [Conda](https://docs.conda.io/en/latest/)

---

## Why do we look at packaging a Python code?

- Python is easy to understand and widely used in research software.
- A well established packaging workflow already exists in the Python community.
- Various examples of packaged codes already exist: [NumPy](https://pypi.org/project/numpy/), [SciPy](https://pypi.org/project/scipy/), [PyTorch](https://pypi.org/project/torch/) and more ...

---

## Key takeaways

- Packaging or creating build recipe of a code is a standardized process.
- Many options in packaging / building tools.
- Most of these tools / methods are customized for use cases.
- In this lecture we will concentrate on packaging of Python code.
