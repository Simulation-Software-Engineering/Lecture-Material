# Notes for Documentation Website Generators Demo

Example code is in [`04_documentation/examples/sphinx`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/04_documentation/examples/sphinx).

- Look at Python code. Same as in packaging exercise, but now refactored into different functions. Run code.

## Docstrings

- Look into `src/solver/diffusionsolver.py`
    - We are using [numpydoc](https://numpydoc.readthedocs.io/en/latest/) as syntax (there is also Google style and Sphinx standard).
    - Explain notation of docstring
    - Short and long description
- Run `python` to start interpreter
    - `import diffusionsolver`
    - `print(diffusionsolver.__doc__)`, but actually private, not the way how to work with docstrings
    - `help(diffusionsolver)`
    - `help(diffusionsolver.SolveDiffusion2D)`

## Sphinx Setup

- `cd docs`; there is already a `tutorials` subfolder; will explain later
- `sphinx-quickstart`
    - You only have to do this once
    - Separate source and build directories (y/n) [n]: n
        - ... of the documentation obviously. Both will go into `docs`.
    - Project name: Diffusion Solver
    - Author name(s): Benjamin Uekermann
    - Project release []: 0.1.0
        - Can distinguish releases
    - Project language [en]: en
- Inspect structure: `tree .`
    - `conf.py`: configure documentation, contains most information
    - `index.rst`: main page
    - `Makefile` and `make.bat`: to build the website
    - more private folders for Sphinx, all empty still
- Build website
    - `make` gives all target options
    - `make html`
    - `tree .`, `_build` is now filled
    - Open and inspect `_build/html/index.html`
- Add tutorials
    - Look at files in `tutorials` subfolder
    - Table of contents in `overview.rst`
    - Add in `index.rst` after `toctree` with indentation of 3 spaces:

    ```diff
    + tutorials/overview
    ```

    - Rebuild and inspect changes: `make html`
- Add `README.rst`:

    ```diff
    +.. include:: ../README.rst
    ```

- Look at `conf.py` and change theme to `classic`

## Code Documentation

- Edit `conf.py`
    - Add `'sphinx.ext.autodoc', 'numpydoc'` to extensions
    - Include source files, at the top add:

    ```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../src'))
    ```

- Create autodoc template files:

  ```bash
  sphinx-apidoc -o source ../src/
  ```

    - Inspect: The files do not contain the actual documentation, but rather a template. The actual documentation is generated once `sphinx` is invoked.
- `make html` and check `Index`
