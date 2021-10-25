# Code Packaging

Learning goals:

- Understanding the necessity to package code
- Determining the type of packaging required for your code
- Modifying code and packaging it
- Uploading code to a remote package managing platform

## Quiz

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | poll | x |

- Conduct an online poll with 3-4 questions to get an impression of how much the students already know about packaging
- Discuss results and quantify the minimum knowledge level of the class
- **Most important question**: How do students perceive the term *packaging*?

## Introduction to packaging

| Duration | Format | Material |
| --- | --- | --- |
| 30 minutes | slides | x |

- Why should we think about *packaging* our code?
  - Small and simple codes written for single applications perhaps do not need packaging. For example you are the only user and you yourself know how to compile the code and how to debug it
  - Codes with many files and a variety of functionalities are difficult to maintain in the long run. Such codes are also difficult to use for users who are not developers of the code. These codes may have multiple dependencies and also multiple users. Users may find it hard to understand and debug the code when errors are observed during the compilation process
  - The aforementioned reasons apply not only to 
  - Writing extensive documentation is one solution, but it needs a lot of effort and it not sustainable
  - Converting a raw code into a standardized and user friendly format is a need that is addressed by *packaging*
  - Packaging is basically *standardization* of a raw code
  - Main reasons for packaging:
    - Increase usability
    - Increase sustainability
    - Ease of distribution
    - Avoiding extensive documentation by following a standard
    - Version control

- Getting started with packaging
  - First explore various ways of packaging codes and which package manager fits best for the code
  - Package managers and installation managers:
    - [CMake](https://cmake.org/)
    - [Spack](https://spack.io/)
    - [Conan](https://conan.io/)
- We concentrate on Python code package managers in this lecture:
  - Packaging Python codes:
    - [PyPI](https://pypi.org/) and [pip](https://pypi.org/project/pip/)
    - [Conda](https://docs.conda.io/en/latest/)

- Why do we look at Python code packaging in detail?
  - Python codes are widely used in scientific computing and simulation sciences and its packaging workflow with PyPI and pip is well established

**Remark**: It is important to understand the abstract packaging concepts from the example of packaging Python code using PyPI and pip**

## Basic steps in packaging a Python code

- Restructing the files to a specific pre-defined file format. This file format depends on which package manager we use.
- How are dependencies of the code being packaged handled?
- How is the installation routine specified?
- Go through examples: [python.org example](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) and [py-rse example](https://merely-useful.tech/py-rse/packaging.html).

## Using a package manager - PyPI and pip

| Duration | Format | Material |
| --- | --- | --- |
| 20 minutes | slides | x |

- How is a packaged code used?
  - Several package managers are available. Lets look at a package manager for Python codes: [PyPI](https://pypi.org/)
  - A packaged code can be installed using package installers, for example [pip](https://pypi.org/project/pip/) which is an installer for Python packages on PyPI and is itself a Python package! pip is itself [open source](https://github.com/pypa/pip).
  - A packaged code lives at a remote location of the package manager. It is from this location that the installer can fetch the code files and install it.

## Exercise

### Part 1: Prepare a raw code for packaging

| Duration | Format | Material |
| --- | --- | --- |
| 30 minutes | in-class exercise | x |

Starting remarks:

- Students to form groups of 3~4 students
- One student forks the repository and every student from the group clones it
- Every student is expected to contribute in the exercise session
- Figure out a way for all group members to work on the same fork, for example, by using branches

Lets convert a raw Python code into a properly packaged code which is uploaded to a package manager. There are many such examples out there but doing the whole workflow yourself once is important to get the hang of the process. Our intention is not to provide a brand new exercise but to take the concepts of packaging and package management and put them into context of simulation software engineering. Every group is expected to have an uploaded version of the packaged code at the end of the exercise.

1. One group member forks the [raw code repository](TODO)
2. Read the [README](TODO) of the repository and understand the main steps of converting a raw code to a packaged code. Also refer to the steps in the [example from python.org](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) as these are the steps which will be followed
3. Restructure the code into the specified file format and prepare the repository for packaging.
4. ... TODO: Some detailed steps of packaging

### Part 2: Upload code to TestPyPI and install it using pip

| Duration | Format | Material |
| --- | --- | --- |
| 30 minutes | in-class exercise | x |

1. Create one [test PyPI](https://test.pypi.org/) account per group.
2. Upload package to TestPyPI.
3. Observe the remote webpage of the package and note down which information is parsed to the remote site.
4. Install the package on your local machine using `pip`.

## Advanced concepts and variants of packaging code

TODO

## Further reading

- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/shipping/packaging/)
- [readthedocs guide](https://python-packaging.readthedocs.io/en/latest/)
- [Python Packaging User Guide](https://packaging.python.org/)

## Other
