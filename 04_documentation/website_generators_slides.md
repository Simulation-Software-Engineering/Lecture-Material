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

# Documentation Website Generators

---

## Learning Goals

- Know about common tools to generate and host software documentation.
- Generate basic software documentation of Python codes with Sphinx and host on Read the Docs.

---

## Recap

- Documentation should be easy to write
    - Lower hurdle to actually document software
- Tools should enhance presentation of documentation
    - Formatting, searching, ...
- Documentation should be accessible
    - Host website
- Different types of documentation
    - Code (functions, API etc.)
    - Everything else (tutorials, project description, contribution guides, ...)
- [Docs as Code](https://www.writethedocs.org/guide/docs-as-code/), [DocOps](https://www.writethedocs.org/guide/doc-ops/)

---

## Brief Overview of Tools

- General documentation site generators
    - [MkDocs](https://www.mkdocs.org) (md), [Sphinx](https://www.sphinx-doc.org/en/master/) (rst), [Jekill](https://jekyllrb.com/), ...
- Code documentation site generators
    - [Doxygen](https://www.doxygen.nl) (C++, C...), Sphinx with [autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) (Python), ...
- Publishing tools
    - [Read the Docs](https://readthedocs.org/), [GitHub Pages](https://pages.github.com/), ...

- Examples:
    - [SSE homepage](https://simulation-software-engineering.github.io/homepage/): MkDocs + [material theme](https://squidfunk.github.io/mkdocs-material/) + GitHub Pages
    - [preCICE docs](https://precice.org/): Jekill + [Jekyll Doc Theme](https://idratherbewriting.com/documentation-theme-jekyll) + GitHub Pages
    - Diffusion solver demo: Sphinx + autodoc ext. + Read the Docs

---

## Step by Step Plan

1. Document Python code: docstrings
2. Create (general) documentation website: Sphinx
3. Add code documentation to this websites: autodoc extension
4. (Homework) Publish the homepage: Read the Docs

---

## Demo: Docstrings

---

## Docstrings

```python
"""Docstring about script/module"""

class ClassName:
    """Docstring about class"""

    def awesome_function(self, parameter ):
        """Docstring about function"""
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

## Sphinx

> Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.

From [Sphinx homepage](https://www.sphinx-doc.org/en/master/)

- Strongly connected to Python project
- Written in Python, also configured in Python (`conf.py`)
- [Sphinx on PyPI](https://pypi.org/project/Sphinx/)
- Generates documentation from reStructuredText files
- Many [extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html) available ([code documentation](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html), [md support](https://www.sphinx-doc.org/en/master/usage/markdown.html), ...)
- Read the Docs has Sphinx integration

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

---

## Code Documentation

- Sphinx + autodoc extension, activate in `conf.py`

  ```python
  extensions = ['sphinx.ext.autodoc']
  ```

- By default, style needs to follow [Sphinx' standard](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
- To change to `numpydoc`, use e.g. [numpydoc extension](https://numpydoc.readthedocs.io/en/latest/index.html) (or [napoleon extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html))

  ```python
  extensions = ['sphinx.ext.autodoc', 'numpydoc']
  ```

---

## Demo: Code Documentation

---

## Read the Docs

> Read the Docs simplifies software documentation by automating building, versioning, and hosting of your docs for you.

From [project homepage](https://readthedocs.org/)

- Itself [open source](https://github.com/readthedocs)
- GitHub integration (Hooks) for automatic deployment
- Supports
    - Sphinx and MkDocs
    - Versioned documentation
    - Downloadable documentation formats

---

## Optional Homework: Publishing on Read the Docs

- Copy the demo example into a new repository under your namespace
- Create Read the Docs [configuration file](https://docs.readthedocs.io/en/stable/config-file/v2.html)
- [Sign up at Read the Docs and connect with GitHub account](https://readthedocs.org/accounts/signup/)
- Import GitHub project on Read the Docs
- Add Read the Docs webhook in GitHub settings

[Read the Docs tutorial](https://docs.readthedocs.io/en/stable/tutorial/index.html)

---

## Further Reading

- [Sphinx homepage](https://www.sphinx-doc.org/en/master/)
- [Sphinx tutorial](https://www.sphinx-doc.org/en/master/tutorial/index.html)
- [Sphinx autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [py-RSE: Packaging with Sphinx](https://merely-useful.tech/py-rse/packaging.html#packaging-sphinx)
- [Doxygen](https://www.doxygen.nl/)
- [MkDocs](https://www.mkdocs.org)
- [Read the Docs](https://readthedocs.org/)
- [GitHub Pages](https://pages.github.com/)
