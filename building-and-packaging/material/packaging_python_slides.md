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

## Questions?

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

## setup.cfg

- We will use [setuptools](https://pypi.org/project/setuptools/) to define the installation recipe for the package
- `setuptools` can be configured using a config script called `setup.cfg`
- `setup.cfg` consists of details like name of the package, version of package, files to include in the package and more.
- An example of `setup.cfg` is:

```bash
[metadata]
name = example-pkg-YOUR-USERNAME-HERE
version = 0.0.1
author = <name>
author_email = <email>
description = <Add your description here>
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/Simulation-Software-Engineering/test-exercise-packaging
project_urls =
    Bug Tracker = https://github.com/Simulation-Software-Engineering/test-exercise-packaging/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: <Name of license>
    Operating System :: OS Independent

[options]
package_dir =
    = solver
packages = find:
python_requires = >=3.6

[options.packages.find]
where = solver
```

## setup.py

- We will use [setuptools](https://pypi.org/project/setuptools/) to define the installation recipe for the package
- The `setuptools` build recipe can be defined in a build script called `setup.py`
- `setup.py` consists of configuration information as well as information on dependencies and details to pass on to PyPI after publishing
- An example of `setup.py` is:

```bash
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YOUR-USERNAME-SSE-package",
    version="0.0.1",
    author="Your Name",
    author_email="Your Email",
    description="A small description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simulation-Software-Engineering/test-exercise-packaging",
    project_urls={
        "Bug Tracker": "https://github.com/Simulation-Software-Engineering/test-exercise-packaging/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: <Name of License>",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
```

---

## LICENSE

- This file provides details on which License is the package distributed under
- Choosing the correct license is often a critical step in open-source software development
- More on licenses in a future chapter of this course

---

## README.md

- A `README` file typically involves detailed description about the package and also the installation procedure#
- The `setuptools` configuration loads the `README.md` file to get the `long_description`, hence it is mandatory to include this file
- Newer versions of `setuptools` also include this file automatically

---

## Creating distribution archives 1/2

- We need to convert the folder sturcture that we have into an archive file system which the end user can download and install on their system
- To do this we will use the package builder [build](https://pypa-build.readthedocs.io/en/stable/index.html) which was introduced in [PEP 517](https://www.python.org/dev/peps/pep-0517/)
- These archive files are finally uploaded to PyPI and can be installed by pip
- The disctribution archives are generated by running the command `python3 setup.py sdist` in the `package_name/` repository
- The following directory and files will be generated in the repository:

```python
dist/
  package_name_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  package_name_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

---

## Uploading the distribution archives 1/2

- Once the distribution archives are created, we want to upload it to the Python Package Index
- We will use [Twine](https://twine.readthedocs.io/en/latest/) to upload our package to PyPI
    - Twine is widely used as it securely authenticates the user to PyPI over HTTPS using a verified connection
    - Its predecessor `python setup.py upload` required careful configuration of the user system and Python version
- PyPI offers an alternative index for testing called TestPyPI on which a user can upload and experiment with their package
- It is always a good idea to verify uploading over TestPyPI before uploading to the real PyPI

---

## Uploading the distribution archives 2/2

- Before using TestPyPI one needs an account and a PyPI API Token
- Account generation is straightforward through a [registration procedure](https://test.pypi.org/account/register/)
- API Token generation is also [a similar procedure](https://test.pypi.org/account/login/?next=%2Fmanage%2Faccount%2F#api-tokens)
- The token `__token__` is the username and the token value is the password required for uploading
- Uploading to TestPyPI can be done using the command: `python3 -m twine upload --repository testpypi dist/*`
- The upload looks something like:

```python
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your username]
Enter your password:
Uploading package_name_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
Uploading package_name_YOUR_USERNAME_HERE-0.0.1.tar.gz
100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]
```

---

## Installing the uploaded package

- The last step in the packaging pipeline is a sanity check done by installing the package that has been uploaded
- The installation can be done by: `python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps package-name-YOUR-USERNAME-HERE`

---

## Summary of folder structure for packaging