# Code Documentation Tools Demo

## TODO

- Tag the important commits in [python-code-documentation repository](https://github.com/Simulation-Software-Engineering/python-code-documentation) and replace the tag **TODO**s.
    - This will be removed later when it is clear that the repository does not change anymore.

## 1. Docstrings

Goal: Add docstrings to the Python Code

### Steps

Initial state is in tag **TODO**

1. Explain Python code shortly. Emphasize that we have a class now so we show how to document a class. We also moved all code in one python file to avoid problems with module imports.
2. Add docstrings to class, solve, and auxiliary functions. Ideally add docstring only to one and then do fast-forward to tag **TODO** of repository.
3. Show `__doc__` attribute and `help` function of Python. Inside the directory containing the `diffusionsolver.py` we start python and print the content of the docstrings.

  ```bash
  python
  Python 3.8.10 (default, Sep 28 2021, 16:10:42)
  [GCC 9.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import diffusionsolver
  >>> print(diffusionsolver.__doc__)

  Solving the two-dimensional diffusion equation

  Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/

  >>> help(diffusionsolver)

      Some longer description is being generated

  >>>
  ```

## 2. Sphinx: Create website

We follow the [quickstart guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html) and the [tutorial](https://www.sphinx-doc.org/en/master/tutorial/index.html) of Sphinx here.

- Change back to the root of the repository
- Reformat the `README.md` into `README.rst`

    1. Rename the file

       ```bash
       git mv README.md README.rst
       ```

       We do this also for consistency with the new files that will be created.
    2. Redo headlines by underlining them
    3. Redo inline code samples with double backticks
    4. Reformat code block using `code-block` directive
- Set up documentation
    1. If not already installed, we install Sphinx via pip

       ```bash
       pip install -U sphinx
       ```

    2. Create documentation directory named `docs/`. This common/standard name for the directory containing documentation.

       ```bash
       mkdir docs && cd docs
       ```

    3. Create basic configuration

       ```bash
       sphinx-quickstart
       ```

       Example output:

       ```bash
       Welcome to the Sphinx 4.3.1 quickstart utility.

       Please enter values for the following settings (just press Enter to
       accept a default value, if one is given in brackets).

       Selected root path: .

       You have two options for placing the build directory for Sphinx output.
       Either, you use a directory "_build" within the root path, or you separate
       "source" and "build" directories within the root path.
       > Separate source and build directories (y/n) [n]: n

       The project name will occur in several places in the built documentation.
       > Project name: Diffusion Solver
       > Author name(s): Alexander Jaust
       > Project release []: 0.1

       If the documents are to be written in a language other than English,
       you can select a language here by its language code. Sphinx will then
       translate text that it generates into that language.

       For a list of supported codes, see
       https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
       > Project language [en]: en

       Creating file /home/jaustar/teaching/courses/simulation-software-engineering/preparation/documentation/python-code-documentation/docs/conf.py.
       Creating file /home/jaustar/teaching/courses/simulation-software-engineering/preparation/documentation/python-code-documentation/docs/index.rst.
       Creating file /home/jaustar/teaching/courses/simulation-software-engineering/preparation/documentation/python-code-documentation/docs/Makefile.
       Creating file /home/jaustar/teaching/courses/simulation-software-engineering/preparation/documentation/python-code-documentation/docs/make.bat.

       Finished: An initial directory structure has been created.

       You should now populate your master file /home/jaustar/teaching/courses/simulation-software-engineering/preparation/documentation/python-code-documentation/docs/index.rst and create other documentation
       source files. Use the Makefile to build the docs, like so:
          make builder
       where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
       ```

       This creates the certain file layout

       ```bash
       $ ls
       Makefile  _build  _static  _templates  conf.py  index.rst  make.bat
       ```

       The `conf.py` file is important to configure the documentation and contains most of the information.

       The `index.rst` file contains the main page of our homepage.

       The `Makefile` and `make.bat` are there to trigger building the website.

    4. Inspect website locally. Build the website

       ```bash
       make html
       ```

       and afterwards open `<prefix>/docs/build/html/index.html`. We can now also edit `index.rst` and rebuild to see the changes.

       Run make once without argument to show all the target options.

       ```bash
       make
       ```

    5. Add another subpage, e.g., "Tutorials".

       Add sub-directory `docs/tutorials/` with files `overview.rst` and `tutorial_case1.rst` (maybe `tutorial_case2.rst`).

       Add content to files:

       `tutorial_case1.rst`: Add headline, some text and two lower level headers.

       ```rst
       Tutorial 1
       ==========

       Tutorial description goes here.

       Step 1
       ------

       Description of step 1.

       Step 2
       ------

       Description of step 2.
       ```

       `overview.rst`: Add headline and a table of contents (TOC). It will be parsed from the `index.rst` such that the main header of the tutorial files will be present on the main page.

       ```rst
       Tutorial overview
       =================

       .. toctree::
          :maxdepth: 2
          :caption: tutorials:

          tutorial_case1.rst
          tutorial_case2.rst
       ```

       **Note** One must be careful with the indentation!
    6. We can include the `REAMDE.rst` into the `index.rst`

       ```diff
       +.. include:: ../README.rst
       ```

       **Note**: In the git repository this addition currently happens in the next step.

## 3. Sphinx: Code Documentation

- Include our source files to `conf.py`. To do so we uncomment the lines

  ```diff
  -#import os
  -#import sys
  -#sys.path.insert(0, os.path.abspath('.'))
  +import os
  +import sys
  +sys.path.insert(0, os.path.abspath('.'))
  ```

  and enable the autodoc extenstion

  ```diff
  -extensions = [
  +extensions = ['sphinx.ext.autodoc'
  ```

- Create autodoc template files

  ```bash
  sphinx-apidoc -o source ../src/

  Creating file source/solver.rst.
  Creating file source/modules.rst.
  ```

  We can inspect the generated files. The files do not contain the actual documentation, but rather a template. The actual documentation is generated once `sphinx` is invoked.
- Recreate website with `make html`. If there is an error message about "consistency" build the website again and/or comment out `from output` from the `diffusionsolver.py` file. Afterwards the error disappeared for me.
    - We now can check out "Index" or "Module Index" and will find some documentation.
- Add additional documentation to `diffusionsolver.py`. Example for `class DiffusionSolver` (should be added to constructor `__init__`)

  ```python
  """A class describing a finite-difference method for solving
  the heat equation if 2 space dimentions.

  :param h: Domain height, defaults to 10.
  :type h: `float`
  :param dx: Mesh width in x-direction, defaults to 0.1
  :type dx: `float`
  :param D: Diffusion constant, defaults to 4.
  :type D: `float`
  :param T_cold: Temperature of cold boundary, defaults to 300.
  :type T_cold: `float`
  :param T_hot: Temperature of cold boundary, defaults to 4.
  :type T_hot: `float`
  """
  ```

  Should follow the [typical Sphinx layout](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html):

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

  This is also on the slides, but may be good as reminder.

## 4. Publish the Website

- Add missing files in `docs/source` to git.
- Add Read the Docs configuration file by copying [the template from the RTD homepage](https://docs.readthedocs.io/en/stable/config-file/v2.html) and then editing it.

  ```yaml
  # .readthedocs.yaml
  # Read the Docs configuration file
  # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

  # Required
  version: 2

  # Set the version of Python and other tools you might need
  build:
    os: ubuntu-20.04
    tools:
      python: "3.9"

  # Build documentation in the docs/ directory with Sphinx
  sphinx:
    configuration: docs/conf.py

  # If using Sphinx, optionally build your docs in additional formats such as PDF
  formats:
  - pdf
  ```

- Follow instructions to [connect the accout from GitHub/sign up](https://readthedocs.org/accounts/signup/)
    - I am already connected.
- Import project -> Import manually (since project is not in my GitHub namespace)
    - Fill in information from [repository page](https://github.com/Simulation-Software-Engineering/python-code-documentation)
    - Name: "Python code documentation"
    - Repository URL: `https://github.com/Simulation-Software-Engineering/python-code-documentation`
    - Repository type `Git`
    - Default branch `main`
- On GitHub add Webhook. If it is not added automatically (permission issue) add it manually in the settings of the repository. Might need to add `https://` in front of the webhook URL (Example: `readthedocs.org/api/v2/webhook/python-code-documentation/185590/`)
- Resync webook
- This should automatically create the website. One can inspect it on Read the Docs. In our case on `https://python-code-documentation.readthedocs.io/en/latest/`
- Checkout the homepage:
    - Bottom right: Change between versions and types (PDF download)
    - Jump to GitHub and edit it there
    - Normally  with advertisements in docs.
- Delete the website after the lecture to not waste resources of Read the Docs