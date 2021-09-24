# Packaging and package managers

Learning goals:

* Comprehending the necessity to package code
* Using package managers to package code and upload to a remote managing platform
* TODO

## Introduction to packaging

Duration: 20 mins
Format: slides

* Why do we need to *package* our code? Is it worth the effort?
  * Codes written for personal use perhaps do not need packaging --> you are the only user and you yourself know how to compile the code and how to debug the compilation process if errors occur
  * Codes with many files and a range of functionality are hard to compile --> such codes may involve multiple compilation commands and also several dependencies
  * Making such codes user friendly and viable for distribution is the essence of packaging

* How do we package code?
  * Packaging a code involves restructing the files to a specific pre-defined file format. This file format depends on which package manager we use.
  * Try packaging a basic code. [Example from python.org](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) and [example from py-rse](https://merely-useful.tech/py-rse/packaging.html).

## Using a package manager

Duration 15 mins
Format: slides

* How is a packaged code used?
  * Several package managers are available. Lets look at a package manager for Python codes: [PyPI](https://pypi.org/)
  * A packaged code can be installed using special installers, for example [pip](https://pypi.org/project/pip/) which is an installer for Python packages on PyPI and is itself a Python package! pip is itself [open source](https://github.com/pypa/pip).
  * A packaged code needs to be uploaded to a remote location of the package manager. It is from this location that the installer can fetch the code files and install it.

  * 

## Exercise: Prepare a raw code for packaging and upload it to TestPyPI

Duration: 60 mins
Format: group work (~2-3 students in one group)
Prerequisites: everybody needs a terminal or an IDE with which they can edit a Python code, a GitHub account, read access to the repo they will work on
Material: TODO: create a repo with raw Python code, master branch is protected, a basic README with exercise instructions and maybe some tips

Lets convert a raw Python code into a properly packaged code which is uploaded to a package manager. There are many such examples out there but doing the whole workflow yourself once is important to get the hang of the process. Our intention is not to provide a brand new exercise but to take the concepts of packaging and package management and put them into context of simulation software engineering. Every group is expected to have an uploaded version of the packaged code at the end of the exercise.

1. Fork the [raw code repository](TODO)
2. Read the [README](TODO) of the repository and understand the main steps of converting a raw code to a packaged code. Also refer to the steps in the [example from python.org](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) as these are the steps which will be followed
3. Restructure the code into the specified file format and prepare the repository for packaging.
4. ... TODO: Some detailed steps of packaging
5. Create one [test PyPI](https://test.pypi.org/) account per group.
6. Upload package to TestPyPI.
7. Observe the remote webpage of the package and note down which information is parsed to the remote site.
8. Install the package on your local machine using `pip`.
