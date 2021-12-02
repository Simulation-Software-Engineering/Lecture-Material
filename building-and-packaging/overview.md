# Building and Packaging

Learning goals:

- What is code packaging and which technologies are available to package code
- How is Python code packaged for uploading to PyPI and installation with pip
- What are libraries, how can they be used
- How can codes be build and dependencies handled with Make and CMake
- How are software packages provided via common packaging approaches (pip, apt, npm)
- How are software packages provided for high-performance computing (Spack, EasyBuild)

## Survey

| Duration | Format | Material |
| --- | --- | --- |
| 10 minutes | poll | [packaging_quiz.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_quiz.md) |

- Conduct an online poll with four questions to get an impression of how much the students already know about packaging
- Discuss results and quantify the minimum knowledge level of the class

## Introduction to Packaging

| Duration | Format | Material |
| --- | --- | --- |
| 20 minutes | slides | [intro_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/intro_slides.md) |

## Packaging a Python Code

| Duration | Format | Material |
| --- | --- | --- |
| 60 minutes | slides | [packaging_python_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_python_slides.md) |

### Further Reading on Packing for Python

- [Packaging tutorial on python.org](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPI help](https://pypi.org/help/)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/shipping/packaging/)
- ["How To Package Your Python Code" by Scott Torborg](https://python-packaging.readthedocs.io/en/latest/)
- [Python Packaging User Guide](https://packaging.python.org/)

## Pip / PyPI Exercise

| Duration | Format | Material |
| --- | --- | --- |
| 90 minutes | in-class exercise | [exercise_python_packaging_text.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/exercise_python_packaging_text.md)

## System Paths, Libraries, and How to Use Them

| Duration | Format | Material |
| --- | --- | --- |
| 25 minutes | slides and demo | [systempaths_and_librarytools_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/systempaths_and_librarytools_slides.md), [systempaths_and_librarytools_notes.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/systempaths_and_librarytools_notes.md) |

## Introduction to Make

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | slides and demo | [make_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/make_slides.md), [make_demo_notes.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/make_demo_notes.md)

## Introduction to CMake

| Duration | Format | Material |
| --- | --- | --- |
| 45 minutes | slides and demo | [cmake_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/cmake_slides.md), [cmake_demo_notes.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/cmake_demo_notes.md)

## Creating Debian Packages from CMake

| Duration | Format | Material |
| --- | --- | --- |
| 35 minutes | slides and demo | [packaging_debian_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_debian_slides.md), [packaging_debian_notes.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_debian_notes.md)

## Packaging for High-Performance Computing and for you

| Duration | Format | Material |
| --- | --- | --- |
| 50 minutes | slides and demo | [packaging_hpc_slides.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_hpc_slides.md), [packaging_hpc_notes.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_hpc_notes.md)