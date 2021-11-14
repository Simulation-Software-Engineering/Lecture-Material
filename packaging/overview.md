# Code Packaging

Learning goals:

- Understanding the necessity to somehow package code written in a crude way
- Being able to determine the type of packaging required for the code
- Modifying code and packaging it according to a standardization
- Uploading code to a remote package managing platform and testing the installation

## Survey

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | poll | [packaging_survey.md](https://github.com/Simulation-Software-Engineering/Lecture-Material) |

- Conduct an online poll with four questions to get an impression of how much the students already know about packaging
- Discuss results and quantify the minimum knowledge level of the class
- **Most important question**: How do students perceive the term *packaging*?

## Introduction to packaging

| Duration | Format | Material |
| --- | --- | --- |
| 30 minutes | slides | [intro_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material) |

## Basic steps of packaging a Python code

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
