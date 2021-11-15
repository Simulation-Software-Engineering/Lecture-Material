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
</style>

# How to prepare a Python code for packaging

---

## What is PyPI?

- [PyPI](https://pypi.org/) = **The Python Package Index** is a repository of software developed in the Python community
- PyPI itself is developed on GitHub through another software called [Warehouse](https://github.com/pypa/warehouse)
- PyPI has a informative [public dashboard](https://p.datadoghq.com/sb/7dc8b3250-85dcf667bd?from_ts=1636972832484&to_ts=1636976432484&live=true) to show its activity
- Who maintains PyPI and pip? A big community! For example check out [Donald Stufft](https://twitter.com/dstufft/)
- A major advantage is the active maintenance of PyPI, which is fueled by a big community. PyPI is also on [Twitter](https://twitter.com/PyPI)

---

## Example of PyPI package: fenicsprecice

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)

---

## What is pip?

- pip is sometimes referred to as a *package installer* and sometimes as a *package management system*
- For all practical purposes it is an installer for packages available at PyPI
- pip is itself a [package](https://pypi.org/project/pip/) which is available on PyPI
- pip is open-source and is developed on [GitHub](https://github.com/pypa/pip)
- pip has many more things which are worth exploring! [Look here!](https://pip.pypa.io/en/latest/development/)

---

## Python Enhancement Proposals (PEPs)

- PEP is an evolving deisgn document which provides information regarding new features of Python, new processes and new environments
- PEPs typically involve concise technical information which also acts as standardizations
- Packaging workflows are also standardized in through multiple PEPs. Examples are:
  - [PEP 427](https://www.python.org/dev/peps/pep-0427/) introduces the built-package format "wheel"
- It is always a good idea to look for **PEP** conventions before trying out processes

---

## File structure for code packaging 1/2

- Most essential component of packaging is file structure. Basic file structure is as follows:

package_name/
└── src/
    └── solver/
        ├── __init__.py
        └── solver.py

- The file `__init__.py` is required to import the `src/` as a package. This file is mostly empty
- `solver.py` will contain the code developed by the user

---

## File structure for code packaging 2/2

- Once the file structuring is complete, the repository will look like:

package_name/
├── LICENSE
├── setup.py
├── setup.cfg
├── README.md
├── src/
│   └── solver/
│       ├── __init__.py
│       └── solver.py
└── tests/

- We will now look at individual components in greater detail

---

## setup.py

- We will use [setuptools](https://pypi.org/project/setuptools/) to define the installation recipe for the package
- `setuptools` can be configured using a config script called `setup.cfg` and the build recipe can be defined in a build script called `setup.py`
  - `setup.cfg` consists of details like name of the package, version of package, files to include in the package.
  - `setup.py` consists of configuration information as well as information on dependencies and details to pass on to PyPI after publishing

## LICENSE

- This file provides details on which License is the package distributed under
- Choosing the correct license is often a critical step in open-source software development
- More on licenses in a future chapter of this course

## README.md

- A `README` file typically involves detailed description about the package and also the installation procedure#
- The `setuptools` configuration loads the `README.md` file to get the `long_description`, hence it is mandatory to include this file
- Newer versions of `setuptools` also include this file automatically

## Creating distribution archives 1/2

- We need to convert the folder sturcture that we have into an archive file system which the end user can download and install on their system
- To do this we will use the package builder [build](https://pypa-build.readthedocs.io/en/stable/index.html) which was introduced in [PEP 517](https://www.python.org/dev/peps/pep-0517/)
- These archive files are finally uploaded to PyPI and can be installed by pip
- 
