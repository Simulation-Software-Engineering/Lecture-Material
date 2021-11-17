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

- Understanding why a majority of code is packaged
- Being able to determine the type of packaging required for the code
- Modifying code and packaging it according to a standardization
- Uploading code to a remote package managing platform and testing the installation procedure

---

## Lets start with a survey

- https://app.sli.do/event/joel1av7
- **ID: 665367**

## What is packaging?

- Standalone code is easy for the developer to understand but quite hard for everyone else to use.
- Packaging is a workflow to convert a code into a standardized distributable software.
- Broadly code can be made standard in various ways:
    - Packaging according to a standardized approach
    - Providing an installation recipe, for example, using CMake / make (`make install`)
    - Bundling code into an app or software with some UI
- In this first lecture we will look at **packaging according to a standardized approach**.

---

## Why should we package code? 1/2

- Codes with many files and a variety of functionalities have several difficulties:
    - Difficult to understand and use for users who are not developers of the code
    - Having multiple dependencies and requirements of specific versions of dependencies
    - Intricate building / installation steps

---

## Why should we package code? 2/2

- Packaging is basically *standardization* of a raw code.
- Main reasons for packaging:
    - Increase usability and sustainability
    - Ease of distribution and maintenance
    - Avoiding lengthy documentation effort by following a standard
    - Versioning

---

## Building and packaging tools

- First step is finding the right type of building or packaging standard fits best for your code.
- There are several (overlapping) options:
    - One of the many Linux package managers: apt, dpkg, yum, RPM Package Manager and many more ...
    - [CMake](https://cmake.org/) <span>: building / installation / packaging tool mostly for C, C++ projects<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Spack](https://spack.io/) <span>: a package management tool mostly for supercomputing centers<!-- .element: class="fragment" data-fragment-index="1" --></span>
    - [Conan](https://conan.io/) <span>: open-source package manager for C and C++ development<!-- .element: class="fragment" data-fragment-index="1" --></span>

<span>
We concentrate on Python code package managers in this lecture:

- [PyPI](https://pypi.org/) and [pip](https://pypi.org/project/pip/)
- [Conda](https://docs.conda.io/en/latest/)

<!-- .element: class="fragment" data-fragment-index="2" --></span>

<span>
There are many more tools out there!
<!-- .element: class="fragment" data-fragment-index="3" --></span>

---

## Why do we particularly look at packaging of Python codes?

- Python is widely used in research software and particularly in simulation software.
- A finetuned packaging workflow is already well established in the community.
- Various examples of packaged codes already exist: [NumPy](https://pypi.org/project/numpy/), [PyMOR](https://pypi.org/project/pymor/), [fenicsprecice](https://pypi.org/project/fenicsprecice/) and more ...

---

## Key takeaways

- Packaging or creating build recipe for your code is generally a good idea.
- There are several tools / methods to do this.
- Most of these tools / methods are customized for specific languages.
- We will concentrate on packaging of Python code.
