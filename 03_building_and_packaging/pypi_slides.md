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
</style>

# Packaging a Python Code

---

## Python packaging is itself evolving

Files which are commonly seen:

`setup.py`, `setup.cfg`, `pyproject.toml`, `requirements.txt`.

All are files which packaging-related tools consume. What do these files do?

---

## Python Enhancement Proposals (PEPs)

- PEP is an evolving design document which provides information regarding new features of Python, new processes and new environments.
- PEPs typically involve concise technical information, which also acts as standardizations.
- Packaging workflows are also standardized through PEPs. Examples are
    - [PEP 427](https://www.python.org/dev/peps/pep-0427/) which introduces the built-package format "wheel".
    - [PEP 518](https://peps.python.org/pep-0518/) which introduces a configuration file for packaging.
- Tip: read the *Rationale* section of the **PEP** convention of a particular feature.

---

## Python libraries used to install packages

- `disutils`: old and deprecated, to be phased out in Python 3.12.
- `setuptools`: actively maintained packaging tool which is shipped with Python (built on top of `disutils`).

---

## setup.py - setup.cfg - pyproject.toml

- Names of all these files are standardized.
- `setup.py` is the interface to the command line. Needs to be at the root of the repository.
- `setup.cfg` has metadata of all the options that can also be specified in `setup.py`.
- `pyproject.toml` is similar to `setup.cfg` but has additionally the `build-system` table.

---

## Comparison of various approaches

- `setup.py` has been widely popular but main limitation is that it cannot be executed without knowing its dependencies. *Chicken and egg* problem regarding dependencies.
- Does `setup.cfg` solve the dependencies problem? No, because no packaging tool can directly read dependencies from it.
- Solution is to use an additional `pyproject.toml` with the `[build-system]` table specified.
- [PyPA sample project](https://github.com/pypa/sampleproject) shows an example using all three files.

---

## Using only setup.py

`setup.py`  is written using [setuptools](https://pypi.org/project/setuptools/):

```python
from setuptools import setup
import setuptools

setup(
    name="package-name",
    version="<version-number>",
    author="Your Name",
    description="A small description",
    url="package-website-url",
    package_dir={"": "<directory-name>"},
    packages=setuptools.find_packages(where="<directory-name>"),
    python_requires=">=3.6",
    install_requires=["<dependencies>"]
    entry_points={
      'console_scripts': ['package-import-name = <path-to-main-function-with-dots>']
    }
)
```

---

## Using setup.cfg and setup.py

Entries moved to `setup.cfg` would look like:

```python
[metadata]
name="package-name"
version="<version-number>"
author="Your Name"
url="package-website-url"
description="A small description"

[options]
packages = find:
install_requires =
  "<dependencies>"
  python_version>"3.6"

[options.entry_points]
console_scripts =
  executable-name = <path-to-main-function-with-dots>
```

A nominal `setup.py` is still required

```python
from setuptools import setup

if __name__ == "__main__":
  setup()
```

---

## Using pyproject.toml

- According to PEP 621, using `pyproject.toml` is the default recommended way of creating packages with `setuptools`.
- Most important table is `[build-system]` which specifies minimum requirements of the package (PEP 518).
- `pyproject.toml` is readable by packaging tools like pip.

Example `pyproject.toml` can look like

```python
[build-system]
requires = ["setuptools", "wheel"]

[project]
name = "package-name"
description = "A small description"
readme = "README.md"
requires-python = ">=3.6"
keywords = ["keyword1", "keyword2"]
license = {text = "BSD License"}
classifiers = [
    "Programming Language :: Python :: 3"
]
dependencies = [
    "requests",
    'importlib-metadata; python_version<"3.8"',
]
dynamic = ["<version-number>"]
```

A nominal `setup.py` is still required.

---

## Packaging tool `build`

```bash
python -m build
```

`build` uses `setup.py` for building the package, without any dependency management.

Drawbacks are

- Requires manual downloading of files from the package website.
- Packages cannot be easily shared between projects, so you would have to manually define a path which can be used by different projects to access the package.

<span>
Is there a better way? Yes! Use pip!
<!-- .element: class="fragment" data-fragment-index="1" --></span>

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
- pip is bundled together with Python 3.x, making it even easier to use.
- pip can install a package from a source distribution (`.tar.gz`) or a wheel distribution (`.whl`).

**Important**: Do not use

```bash
sudo pip install <package>
```

Various security issues with doing so! Go for

```bash
pip install --user <package>
```

---

## Installing a package in editable mode

```bash
pip install -e <package>
```

- Creates a direct link between local package files and installation, which is useful for development.
- Make sure to *undo* post development.

---

## Using pip

Uninstall a package

```bash
pip uninstall <package>
```

Update a package

```bash
pip install --upgrade <package>
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

## File structure for code packaging 1/2

Four places where naming is relevant:

- Name of the repository (on GitHub or GitLab).
- Name of the folder which has the source code.
- Name of the package as seen my PyPI.
- Name of the package to be used in the `import` statement.

**All three names are independent of each other.**

Example folder structure:

```bash
generic_folder_name/
└── src/
     ├── __init__.py
     └── source-code.py
```

- The file `__init__.py` is required to import the `package_name/` package as a package. This file is mostly empty
- `source-code.py` contains the code. It can be multiple files.

---

## File structure for code packaging 2/2

- Once the file structuring is complete, the repository will look like:

```bash
generic_folder_name/
├── LICENSE
├── setup.py
├── README.md
├── src/
│    ├── __init__.py
│    └── source-code.py
└── tests/
```

---

## Additional options in setup.py 1/3

- [Classifiers](https://pypi.org/classifiers/): additional metadata for the version of the package
- Defined as part of [PEP 303](https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification).
- Example:

```python
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

## Additional options in setup.py 2/3

- The file `README.md` can be passed as a long description in the following way:

```python
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

## Additional options in setup.py 3/3

The option `entry_points` provide metadata which are exposed after installation. For example: executable functions from a terminal.

```python
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    ...
    entry_points={
      'console_scripts': ['package-import-name = <path-to-main-function-with-dots>']
    }
    ...
)
```

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

Both the commands must be run in the same directory as `setup.py`.

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

Packaging of Python code is

- creation of a standardized folder structure to convert raw Python code into a project.
- creating and uploading distribution archives.
- Uploading distribution archives to a package index.

We saw the process of packaging and uploading to TestPyPI which is similar to uploading to the PyPI.
