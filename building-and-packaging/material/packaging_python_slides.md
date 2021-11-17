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

- `setup.py` allows you to install packages by running `python setup.py install`
- `setup.py` is written using [setuptools](https://pypi.org/project/setuptools/)
- Example:

```bash
from setuptools import setup

setup(
    name="package-name",
    version="<version-number>",
    author="Your Name",
    author_email="Your Email",
    description="A small description",
    url="package-website-url",
    package_dir={"": "<directory-name>"},
    packages=setuptools.find_packages(where="<directory-name>"),
    python_requires=">=3.6",
)

```

---

## Why is setup.py not the best way?

- Before doing `python setup.py install` you have to manually search and install dependencies
- A package installed by `setup.py` needs to be manually maintained and uninstalled if required
- Requires manual downloading of files from the package website

<span>
Is there a better way?
<!-- .element: class="fragment" data-fragment-index="1" --></span>

<span>
Yes! Use pip!
<!-- .element: class="fragment" data-fragment-index="2" --></span>

---

## What is pip?

- pip is a package installer to install packages from the [Python Package Index PyPI]((https://pypi.org/))
- pip is itself a [package](https://pypi.org/project/pip/) which is available on PyPI
- pip is open-source and is developed on [GitHub](https://github.com/pypa/pip)

---

## Using pip

- When `pip install package-name` is run, pip chooses a distribution file and installs it in the environment
- Doing `python -m pip install package-name` is basically the same as `pip install package-name`
- pip tracks metadata to allow for easy uninstallation and updating of packages
- pip is bundled together with Python 3.x, making it even more easier to use
- pip can install a package from a source distribution (`.tar.gz`) or a wheel distribution (`.whl`)
- Do not use `sudo pip install`! Various security issues with doing so. Go for `pip install --user <package-name>`

---

## What is PyPI?

- [PyPI](https://pypi.org/) = **The Python Package Index** is a repository of software developed in the Python community
- PyPI itself is developed on GitHub through another software called [Warehouse](https://github.com/pypa/warehouse)
- PyPI has a informative [public dashboard](https://p.datadoghq.com/sb/7dc8b3250-85dcf667bd) to show its activity
- A major advantage is the active maintenance of PyPI and the packages indexed in it
- Not to be confused with **PyPA** which is Python Packaging Authority, a working group which maintains projects in Python packaging

---

## Example of PyPI package: fenicsprecice

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)

---

## Python Enhancement Proposals (PEPs)

- PEP is an evolving design document which provides information regarding new features of Python, new processes and new environments
- PEPs typically involve concise technical information, which also acts as standardizations
- Packaging workflows are also standardized through PEPs. Example:
    - [PEP 427](https://www.python.org/dev/peps/pep-0427/) introduces the built-package format "wheel"
- It is always a good idea to look for **PEP** conventions before trying out processes

---

## File structure for code packaging 1/2

- Most essential component of packaging is file structure. Basic file structure is as follows:

```bash
generic_folder_name/
└── src/
    └── package_name/
        ├── __init__.py
        └── solver.py
```

- The file `__init__.py` is required to import the `package_name/` as a package. This file is mostly empty
- `solver.py` will contain the code developed by the user

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
│       └── solver.py
└── tests/
```

<span>
Lets have a detailed look at individual files in this folder structure
<!-- .element: class="fragment" data-fragment-index="1" --></span>

---

## Additional options in setup.py 1/2

- [Classifiers](https://pypi.org/classifiers/): additional metadata for the version of the package
- Defined as part of [PEP 303](https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification)
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

- This file provides details on which license is the package distributed under
- Choosing the correct license is often a critical step in open-source software development
- More on licenses in a future chapter of this course

---

## README.md

- A `README.md` file typically gives a description of the package, code structure, meta information, the installation procedure and more ...
- It is common practice to parse the `README.md` to `setuptools` as a long description
- Newer versions of `setuptools` also include this file automatically
- This file can also be written using [reStructuredText](https://docutils.sourceforge.io/rst.html) which is part of [Docutils](https://docutils.sourceforge.io/index.html)

---

## Creating distribution archives

- The project needs to be converted to distribution archives so that pip can install them
- There are two ways to create these archives:
    - Using the package builder [build](https://pypa-build.readthedocs.io/en/stable/index.html) which was introduced in [PEP 517](https://www.python.org/dev/peps/pep-0517/)
    - Using the packaging standard [wheel](https://wheel.readthedocs.io/en/stable/) which was introduced in [PEP 427](https://www.python.org/dev/peps/pep-0427/)
- A source distribution archive file (`package-name-<tags>.tar.gz`) can be generated by running the command `python3 setup.py sdist` in the `package_name/` repository
- A wheel archive file (`package-name-<tags>.whl`) can be generated by running the command `python3 setup.py bdist_wheel` in the `package_name/` repository
- In both cases the files will be generated in a folder `package_name/dist/`

---

## Uploading the distribution archives 1/2

- [Twine](https://twine.readthedocs.io/en/latest/) is a common tool to upload our package to PyPI
- Why Twine?
    - Secure authentication of the user to PyPI over HTTPS using a verified connection
    - Its predecessor `python setup.py upload` required careful configuration
    - Encourages users to create distribution files to promote testing before releasing
- [TestPyPI](https://test.pypi.org/) is a testing instance of PyPI which does not affect the real index
- Uploading the distribution to TestPyPI before PyPI is a standard pre-deployment step

---

## Uploading the distribution archives 2/2

- Before using TestPyPI (or PyPI) you need an account and a PyPI API Token
- Account creation and API Token generation is straightforward through the [registration page](https://test.pypi.org/account/register/)
- Uploading to TestPyPI can be done using the command: `python3 -m twine upload --repository testpypi dist/*`
- The uploading process looks something like:

```bash
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your username]
Enter your password: [your password]
Uploading package_name-0.0.1-py3-none-any.whl
100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
Uploading package_name-0.0.1.tar.gz
100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
```

---

## Installing the uploaded package

- The last step in the packaging pipeline is a sanity check done by installing the package that has been uploaded
- The installation can be done by:

```bash
pip install --user --index-url https://test.pypi.org/simple/ <package-name>
```

---

## Conda

- [Conda](https://docs.conda.io/en/latest/) is a package and environment management system which supports multiple languages
- Conda provides a fast option to setup an isolated environment on your local system
- Conda is configured to work with [Anaconda installers and packages](https://repo.anaconda.com/)
- Conda is often the preferred way to run Python packages on Windows and MacOS. See example in [FEniCS on Anaconda section](https://fenicsproject.org/download/)

---

## Difference between Conda and pip

| Feature | Conda | pip |
| Multi-language dependency | Yes | No |
| Package installation | Anaconda installer / download binaries | build / wheels |
| Package availability | ~8000 | ~336,000 |
| Virtual environment functionality | In-built environment management | No, but support for `virtualenv` |

---

## Important takeaways

Packaging involves two central work packages:

- Creation of a standardized folder structure to convert a raw code into a project
- Creating and uploading distribution archives to a packaging index

We saw the process of packaging and uploading to PyPI
