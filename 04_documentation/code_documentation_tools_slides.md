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
- You know how to publish your homepage.

---

## Introduction

- Software projects need documentation
- Different types of documentation and locations
    - Code (functions, API etc.)
    - Everything else (tutorials, project description, contribution guides...)
- [Docs as Code](https://www.writethedocs.org/guide/docs-as-code/), [DocOps](https://www.writethedocs.org/guide/doc-ops/)

---

## Documentation (Tool) Requirements

- Documentation should be easy to write
    - Lower hurdle to actually document software
- Tools should enhance presentation of documentation
    - Formatting, searching...
- Documentation should be accessible
    - Host website

---

## Short Tools Overview

- General documentation website generators
    - [MkDocs](https://www.mkdocs.org) (md), [Sphinx](https://www.sphinx-doc.org/en/master/) (rst),...
- Code documentation website generators
    - [Doxygen](https://www.doxygen.nl) (C++, C...), Sphinx with [autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) (Python),...
- Publishing tools
    - [Read the Docs](https://readthedocs.org/), [GitHub Pages](https://pages.github.com/)...
- Example: [SSE homepage](https://simulation-software-engineering.github.io/homepage/)
    - MkDocs + [MkDocs material theme](https://squidfunk.github.io/mkdocs-material/) + GitHub Pages

---

## Step by Step Plan

1. Document Python code
2. Create (general) documentation website
3. Add code documentation to this websites
4. Publish the homepage via Read the Docs

The code is on [GitHub](https://github.com/Simulation-Software-Engineering/python-code-documentation)

---

## Docstrings

```python
"""Docstring explaining the script/module"""

class ClassName:
    """Docstring explaining the class"""

    def awesome_function(self, parameter ):
        """A docstring explaining the function"""
        return parameter
```

- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- `__doc__` property is derived from docstring
- May span multiple lines
- Docstrings are not normal comments

  ```python
  # This is a Python style comment
  ```

---

## Demo: Docstrings

- Inspect the code
- Add docstrings to document sample code
- Checkout the help directive

---

## Sphinx

> Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
>
> From [project homepage](https://www.sphinx-doc.org/en/master/)

---

## Sphinx Introduction

- Strongly connected to Python project
- Written in Python, also configured in Python (`conf.py`)
- Generates documentation from reStructuredText files
- Many [extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html) available ([code documentation](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html), [Markdown support](https://www.sphinx-doc.org/en/master/usage/markdown.html)...)
- Read the Docs integration

---

## Important Sphinx Commands

- Create new project

  ```bash
  sphinx-quickstart
  ```

- Build documentation

  ```bash
  sphinx-build [OPTIONS] SOURCEDIR OUTPUTDIR [FILENAMES...]
  ```

  or if `sphinx-quickstart` was used

  ```bash
  make html
  ```

  Supports several targets (HTML, LaTeX, man...)

---

## Demo: Sphinx Setup

- Move to reStructuredText as markup language
- Create Sphinx configuration

---

## Code Documentation

- Sphinx + autodoc extension, activate in `conf.py`

  ```python
  extensions = ['sphinx.ext.autodoc']
  ```

- Format docstring according to Sphinx' standard

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
>
> From [project homepage](https://readthedocs.org/)

---

## Read the Docs Introduction

- Financed by (ethical) advertisements and sponsors
- Itself [open source](https://github.com/readthedocs)
- GitHub integration (Hooks) for automatic deployment
- Supports
    - Sphinx and MkDocs
    - Versioned documentation
    - Downloadable documentation formats

---

## Demo: Publishing on Read the Docs

- Create Read the Docs configuration file
- Connect GitHub repository with Read the Docs
- Study the generated documentation website

---

## Other Tools

---

## MkDocs

> MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
>
> From [project homepage](https://www.mkdocs.org/)

---

## MkDocs Introduction

- Written in Python and configured via YAML (`mkdocs.yml`)
- Generates documentation from Markdown files
- Many [plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) available (e.g. [API/code documentation](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins#api-documentation-building))
- Read the Docs integration

---

## Important MkDocs commands

- Create new project

  ```bash
  mkdocs new [OPTIONS] PROJECT_DIRECTORY
  ```

- Build documentation

  ```bash
  mkdocs build [OPTIONS]
  ```

- Build and serve website

  ```bash
  mkdocs serve [OPTIONS]
  ```

- Deploy to GitHub Pages

  ```bash
  mkdocs gh-deploy [OPTIONS]
  ```

---

## Doxygen

> Doxygen is the de facto standard tool for generating documentation from annotated C++ sources, but it also supports other popular programming languages such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors), Fortran, VHDL and to some extent D.
>
> From [project homepage](https://www.doxygen.nl)

---

## Doxygen Introduction

From [project homepage](https://www.doxygen.nl):

1. Create online (website/HTML) or offline (LaTeX, PDF...) code documentation
    - [DuMuX](https://dumux.org/docs/doxygen/master/), [preCICE API](https://precice.org/doxygen/master/classprecice_1_1SolverInterface.html)...
2. Extract code structure from undocumented code
3. Create project documentation
    - [Eigen](http://eigen.tuxfamily.org/dox/), [VTK](https://vtk.org/doc/nightly/html/index.html), [CGAL](https://doc.cgal.org/latest/Manual/index.html)
- Configuration stored in `Doxyfile`
    - May use [`Doxywizard` GUI](https://www.doxygen.nl/manual/doxywizard_usage.html)

---

## Doxygen Information Flow

<img src="https://www.doxygen.nl/manual/infoflow.png" width=60%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

Source: [Getting started](https://www.doxygen.nl/manual/starting.html)


---

## Important Doxygen Commands

- Create Doxygen configuration

  ```bash
  doxygen -g <config_file>
  ```

- Create documentation

  ```bash
  doxygen <config-file>
  ```

---

## Doxygen Documentation Blocks

```c++
/*! A test class */

class Afterdoc_Test
{
  public:
    /** An enum type.
     *  The documentation block cannot be put after the enum!
     */
    enum EnumType
    {
      int EVal1,     /**< enum value 1 */
      int EVal2      /**< enum value 2 */
    };
    void member();   //!< a member function.

  protected:
    int value;       /*!< an integer value */
};
```

- Different comment styles `/**...*/`, `/*!...*/`, `///`, `//!`...
- More information in and also this example in [documentation](https://www.doxygen.nl/manual/docblocks.html)

---

## Further Reading

- [Sphinx homepage](https://www.sphinx-doc.org/en/master/)
- [Sphinx extensions overview](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
- [Sphinx autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [Read the Docs on Sphinx Docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
- [py-RSE: Packaging with Sphinx](https://merely-useful.tech/py-rse/packaging.html#packaging-sphinx)
- [Doxygen](https://www.doxygen.nl/)
- [MkDocs](https://www.mkdocs.org)
- [Read the Docs](https://readthedocs.org/)
- [GitHub Pages](https://pages.github.com/)
