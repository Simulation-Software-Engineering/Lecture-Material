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

## Docstrings

-

```python
class ClassName:

    def funtion():
        return 0

    def awesome_function( input_parameter )

```

---

## Further Reading