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

# Packaging a Python Code

---

## Using setup.py to package Python code

`setup.py`  is written by [setuptools](https://pypi.org/project/setuptools/) allows you to install packages by running

```bash
python setup.py install
```

Example:

```bash
from setuptools import setup
import setuptools

setup(
    name="package-name",
    version="<version-number>",
    author="Your Name",
    description="A small description",
    url="package-website-url",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["<installation dependencies>"]
)
```

---

## Why is setup.py not the best way?

- Before doing installing with `setup.py` you have to manually search and install dependencies.
- A package installed by `setup.py` needs to be manually maintained and uninstalled if required.
- Requires manual downloading of files from the package website.

<span>
Is there a better way?
<!-- .element: class="fragment" data-fragment-index="1" --></span>

<span>
Yes! Use pip!
<!-- .element: class="fragment" data-fragment-index="2" --></span>

---

## What is pip?

- pip is a package installer to install packages from the [Python Package Index PyPI]((https://pypi.org/)).
- pip is itself a [package](https://pypi.org/project/pip/) which is available on PyPI.
- pip is open-source and is developed on [GitHub](https://github.com/pypa/pip).

---

## Using pip 1/2

Executing:

```bash
pip install package-name
```

leads to pip choosing a distribution file  for the package and installing it in the environment.

```bash
python -m pip install package-name
```

is basically the same as:

```bash
pip install package-name
```

---

## Using pip 2/2

- pip tracks metadata to allow for easy uninstallation and updating of packages.
- pip is bundled together with Python 3.x, making it even more easier to use.
- pip can install a package from a source distribution (`.tar.gz`) or a wheel distribution (`.whl`).

**Important**: Do not use

```bash
sudo pip install <package-name>
```

Various security issues with doing so! Go for

```bash
pip install --user <package-name>
```

---

## What is PyPI?

- [PyPI](https://pypi.org/) = **Python Package Index** is a repository of software developed in the Python community.
- PyPI itself is developed on GitHub through another software called [Warehouse](https://github.com/pypa/warehouse).
- PyPI has a informative [public dashboard](https://p.datadoghq.com/sb/7dc8b3250-85dcf667bd) to show its activity.
- A major advantage is the active maintenance of PyPI and the packages indexed in it.
- Not to be confused with **PyPA** which is Python Packaging Authority, a working group which maintains projects in Python packaging.

---

## Example of PyPI package: fenicsprecice

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)

---

## Python Enhancement Proposals (PEPs)

- PEP is an evolving design document which provides information regarding new features of Python, new processes and new environments.
- PEPs typically involve concise technical information, which also acts as standardizations.
- Packaging workflows are also standardized through PEPs. Example:
    - [PEP 427](https://www.python.org/dev/peps/pep-0427/) introduces the built-package format "wheel".
- It is always a good idea to look for **PEP** conventions before trying out processes.

---

## File structure for code packaging 1/2

- Most essential component of packaging is file structure. Basic file structure is as follows:

```bash
generic_folder_name/
└── src/
    └── package_name/
        ├── __init__.py
        └── package-code.py
```

- The file `__init__.py` is required to import the `package_name/` as a package. This file is mostly empty
- `solver.py` will contain the code developed by the user.

---

## File structure for code packaging 2/2

- Once the file structuring is complete, the repository will look like:

```bash
generic_folder_name/
├── LICENSE
├── setup.py
├── README.md
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── package-code.py
└── tests/
```

<span>
Lets have a detailed look at individual files in this folder structure.
<!-- .element: class="fragment" data-fragment-index="1" --></span>

---

## Additional options in setup.py 1/2

- [Classifiers](https://pypi.org/classifiers/): additional metadata for the version of the package
- Defined as part of [PEP 303](https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification).
- Example:

```bash
from setuptools import setup

setup(
    ...
    classifiers=[
        "Programming Language :: Python :: <Python-version>",
        "License :: OSI Approved :: <Name of License>",
        "Operating System :: <OS's on which this package runs>",
    ],
    ...
)
```

---

## Additional options in setup.py 2/2

- The file `README.md` can be passed as a long description in the following way:

```bash
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    ...
    long_description=long_description,
    long_description_content_type="text/markdown",
    ...
)
```

---

## LICENSE

- This file provides details under which license is the package distributed.
- Choosing the correct license is often a critical step in open-source software development.
- More on licenses in a future chapter of this course.

---

## README.md

- A `README.md` file typically gives a description of the package, code structure, meta information, the installation procedure and more ...
- It is common practice to parse the `README.md` to `setuptools` as a long description.
- Newer versions of `setuptools` also include this file automatically.
- This file can also be written using [reStructuredText](https://docutils.sourceforge.io/rst.html) which is part of [Docutils](https://docutils.sourceforge.io/index.html).

---

## Creating distribution archives 1/2

There are two ways to create these archives:

- Using the package builder [build](https://pypa-build.readthedocs.io/en/stable/index.html) which was introduced in [PEP 517](https://www.python.org/dev/peps/pep-0517/).
- Using the packaging standard [wheel](https://wheel.readthedocs.io/en/stable/) which was introduced in [PEP 427](https://www.python.org/dev/peps/pep-0427/).

In both cases the files will be generated in a folder `repository/dist/`.

---

## Creating distribution archives 2/2

A source distribution archive file (`package-name-<tags>.tar.gz`) can be generated by running the command:

```bash
python setup.py sdist
```

A wheel archive file (`package-name-<tags>.whl`) can be generated by running the command:

```bash
python setup.py bdist_wheel
```

Both the commands are run at the same level as `setup.py`

---

## Uploading the distribution archives 1/3

- [Twine](https://twine.readthedocs.io/en/latest/) is a common tool to upload our package to PyPI.
- Why Twine?
    - Secure authentication of the user to PyPI over HTTPS using a verified connection.
    - Its predecessor `python setup.py upload` required careful configuration.
    - Encourages users to create distribution files to promote testing before releasing.
- The archive files are uploaded to a package index from where pip can get them

---

## Uploading the distribution archives 2/3

- [TestPyPI](https://test.pypi.org/) is a testing instance of PyPI which does not affect the real index.
- Uploading the distribution to TestPyPI before PyPI is a standard pre-deployment step.
- Before using TestPyPI (or PyPI) you need an account and a PyPI API Token.
- Account creation and API Token generation is straightforward through the [registration page](https://test.pypi.org/account/register/).
- The API token can be configured in a file `$HOME/.pypirc`

---

## Uploading the distribution archives 3/3

Uploading to TestPyPI can be done using the command:

```bash
python -m twine upload --repository testpypi dist/*
```

The uploading process looks something like:

```bash
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your username]
Enter your password: [your password]
Uploading package_name-0.0.1.tar.gz
100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
```

---

## Installing the uploaded package

- The last step in the packaging pipeline is a sanity check done by installing the package that has been uploaded.
- The installation can be done by:

```bash
pip install --user --index-url https://test.pypi.org/simple/ <package-name>
```

---

## Conda

- [Conda](https://docs.conda.io/en/latest/) is a package and environment management system which supports multiple languages.
- Conda provides a fast option to setup an isolated environment on your local system.
- Conda is configured to work with [Anaconda installers and packages](https://repo.anaconda.com/).
- Conda is often the preferred way to run Python packages on Windows and MacOS. See example in [FEniCS on Anaconda section](https://fenicsproject.org/download/).

---

## Difference between Conda and pip

<style>
td {
    font-size: 35px
}
</style>

| Feature | Conda | pip |
| ------- | ----- | --- |
| Multi-language dependency | Yes | No |
| Package installation | Anaconda installer / download binaries | build / wheels |
| Package availability | ~8000 | ~336,000 |
| Virtual environment functionality | In-built environment management | No, but support for `virtualenv` |

---

## Be careful while using Python environments

<img src="https://imgs.xkcd.com/comics/python_environment.png" width=50% style="margin-left:auto; margin-right:auto">

[xkcd Python Environments](https://imgs.xkcd.com/comics/python_environment.png)

---

## Important takeaways

Packaging of Python code involves two central work packages:

- Creation of a standardized folder structure to convert a raw Python code into a project.
- Creating and uploading distribution archives.
- Uploading distribution archives to a package index.

We saw the process of packaging and uploading to TestPyPI which is similar to uploading to the PyPI
