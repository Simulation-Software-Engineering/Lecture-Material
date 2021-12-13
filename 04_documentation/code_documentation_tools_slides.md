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
  .reveal code {
    font-family: 'Ubuntu Mono';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# Code Documentation Tools

---

## Learning Goals

- You know about common ways to generate code documentation.
- You know tools for Python and C++.
- You know common website generators for documentation.

---

## Introduction

- Tools that generate documentation from information supplied with source code
    - May also generate code from other sources

---

## Tools Overview

- Code documentation website generators
    - Doxygen, Sphinx (with autodoc extension),...
- General documentation website generators
    - MkDocs, Sphinx,...
- Publishing tools
    - Read the Docs, GitHub Pages

---

## Step by Step Plan

1. Document a Python code
2. Create a documentation website via Sphinx
3. Add code documenation to this websites
4. Publish the homepage via Read the Docs

The code is on GitHub

**TODO** Add GitHub link

---

## Docstrings

```python
"""Docstring explaining the script"""

class ClassName:
    """Docstring explaining the class"""

    def awesome_function(self, parameter ):
        """A docstring explaining the function"""
        return parameter

```

- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- `__doc__` property is derived from docstring
- May span multiple lines
- Docstrings are **not** comments

  ```python
  # This is a Python style comment
  ```

---

## Demo: Docstrings

- Inspect the code
- Add docstrings to do document sample code

---

## Sphinx

> Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
>
> From [project homepage](https://www.sphinx-doc.org/en/master/)

- Strongly connected to Python project
- Written in Python

  ```bash
  pip install sphinx
  ```

---

## Demo: Sphinx Setup

- Move to reStructuredText as markup language
- Create a new Sphinx configuration

---

## Code Documentation

- Sphinx + autodoc extension
- Format docstring in prescribed way

---

## Sphinx Docstring formatting

```python
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```

From: [Read the Docs Sphinx Docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

---

## Read the Docs

> Read the Docs simplifies software documentation by automating building, versioning, and hosting of your docs for you.

[Homepage](https://readthedocs.org/)

---

## Read the Docs configuration file

---

## Doxygen

> Doxygen is the de facto standard tool for generating documentation from annotated C++ sources, but it also supports other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors), Fortran, VHDL and to some extent D.
>
> From [project homepage](https://www.doxygen.nl)

---

## Doxygen Introduction

- Documentation (mainly) in code
- Place interface documentation in header (C++)
    - Does not clutter implementation

---

## Main Features

From [project homepage](https://www.doxygen.nl):

1. Create online (website/HTML) or offline (LaTeX, PDF...) code documentation
    - [DuMuX](https://dumux.org/docs/doxygen/master/), [preCICE API](https://precice.org/doxygen/master/classprecice_1_1SolverInterface.html)...
2. Extract code structure from undocumented code
3. Create project documentation
    - [Eigen](http://eigen.tuxfamily.org/dox/), [VTK](https://vtk.org/doc/nightly/html/index.html), [CGAL](https://doc.cgal.org/latest/Manual/index.html)

---

## Doxygen Information Flow

<img src="https://www.doxygen.nl/manual/infoflow.png" width=60%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

Source: [Getting started](https://www.doxygen.nl/manual/starting.html)

---

## Doxygen Configuration

- `Doxyfile` is main configuration tool
    -

---

## Doxygen Demo

---

## Further Reading