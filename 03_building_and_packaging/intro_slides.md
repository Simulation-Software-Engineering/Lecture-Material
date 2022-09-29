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

- What is code packaging and which technologies are available to package code
- What are the various ways in which a Python code can be packaged
- How is the Python Package Index (PyPI) used to distribute Python packages

---

## Lets start with a survey

- https://app.sli.do/event/joel1av7
- **ID: 665367**

---

## What is packaging?

- Bare code is often hard to understand for everyone except the developer.
- Packaging is a workflow to convert a code into a standardized distributable software.
- Broadly code can be standardized in various ways. Some examples are
    - creating a package according to some standardization.
    - providing an installation recipe, for example, using CMake / make (`make install`).
    - bundling code into an app or software with some UI.
- In this first lecture you will learn about **creating a package according to some standardization**.

---

## Why should we package code? 1/2

- A bare code with many files typically has difficulties like
    - multiple dependencies and requirements of specific versions of dependencies.
    - intricate compilation / installation steps which are hard to get right.
    - missing or limited starting information / documentation which means a high entry barrier.

---

## Why should we package code? 2/2

- Create a package of bare code to
    - benefit from a package index or package manager which is familiar for a broad audience.
    - benefit from automated handling of dependencies of package managers.
    - have ease of distribution and maintenance due to standardization.

---

## How to package code?

- First step is finding the right type of packaging standard that fits best for your code.
- There are several (overlapping) options:
    - One of the many Linux package managers: apt, dpkg, yum, RPM Package Manager and many more ...
    - [CMake](https://cmake.org/) <span>: building / installation / packaging tool mostly for C, C++ projects<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Spack](https://spack.io/) <span>: a package management tool mostly for supercomputing centers<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Conan](https://conan.io/) <span>: open-source package manager for C and C++ development<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [PyPI](https://pypi.org/) and [pip](https://pypi.org/project/pip/)
    - [Conda](https://docs.conda.io/en/latest/)

---

## Why do we particularly look at packaging a Python code?

- Python is easy to understand and widely used in research software.
- A finetuned packaging workflow is already well established in the Python community.
- Various examples of packaged codes already exist: [NumPy](https://pypi.org/project/numpy/), [PyMOR](https://pypi.org/project/pymor/), [fenicsprecice](https://pypi.org/project/fenicsprecice/) and more ...

---

## Key takeaways

- Packaging or creating build recipe of a code is a standardized process.
- Many options in packaging / building tools.
- Most of these tools / methods are customized for use cases.
- In this lecture we will concentrate on packaging of Python code.
