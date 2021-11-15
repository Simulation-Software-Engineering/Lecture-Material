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

# Introduction to packaging

---

## Learning goals of chapter

- Understanding the necessity to somehow package code written in a crude way
- Being able to determine the type of packaging required for the code
- Modifying code and packaging it according to a standardization
- Uploading code to a remote package managing platform and testing the installation

---

## What is packaging?

- Raw code is easy for the developer to understand but quite hard for everyone else to use
- Packaging is a workflow to convert a code into a usable and distributable library
- Packaging can be done in various forms:
  - Using a standardized approach for a particular package manager
  - Providing an installation recipe, for example, using CMake
  - Bundling code into an app or software with some UI
- In this lecture we will look at **using a standardized approach for a particular package manager**

---

## Why should we think about packaging code?

- Small and simple codes written for single applications perhaps do not need packaging
- Codes with many files and a variety of functionalities have several difficulties:
  - Such codes are difficult to use for users who are not developers of the code
  - These codes may have multiple dependencies and also multiple users
  - Users may find it hard to understand and debug the code when errors are observed during the compilation process

---

## More reasons to pursue code packaging

- Writing extensive documentation is one solution, but it needs a lot of effort and it not sustainable
- Packaging is basically *standardization* of a raw code
- Main reasons for packaging:
  - Increase usability
  - Increase sustainability
  - Ease of distribution
  - Avoiding extensive documentation by following a standard
  - Version control

---

## Various ways to package code

- First step in packaging is to find a tool / package manager which fits best for the code
- There are several options:
  - [CMake](https://cmake.org/) <span>: mostly for C, C++ projects<!-- .element: class="fragment" data-fragment-index="1" --></span>
  - [Spack](https://spack.io/) <span>: a package management tool mostly for supercomputing centers<!-- .element: class="fragment" data-fragment-index="1" --></span>
  - [Conan](https://conan.io/) <span>: open-source package manager for C and C++ development<!-- .element: class="fragment" data-fragment-index="1" --></span>
<span>
- We concentrate on Python code package managers in this lecture:
  - Packaging Python codes:
    - [PyPI](https://pypi.org/) and [pip](https://pypi.org/project/pip/)
    - [Conda](https://docs.conda.io/en/latest/)
    <!-- .element: class="fragment" data-fragment-index="2" --></span>

---

## Why do we particularly look at packaging of Python codes?

- Python is widely used in research software and particularly in simulation software
- A finetuned packaging workflow with PyPI and `pip` is already well established in the community
- Various examples of packaged codes already exist: [NumPy](https://pypi.org/project/numpy/), [PyMOR](https://pypi.org/project/pymor/), [fenicsprecice](https://pypi.org/project/fenicsprecice/) and more ...

---

## Questions?
