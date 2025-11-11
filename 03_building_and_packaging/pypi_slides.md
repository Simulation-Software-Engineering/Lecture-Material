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

## Python Package Managers 1/3

The most significant package managers:

- pip
- Conda
- Poetry
- uv

---

## Python Package Managers 2/3

pip and Conda are well-established package managers with large ecosystems.

- pip is well-documented and widely used.
- Conda has cross-language support and higher use in scientific computing.

Poetry and uv are newer variants with better functionality and speed.

- Poetry provides not just packaging but also dependency handling and virtual environment management.
- uv is a faster and smarter drop-in replacement for pip.

---

## Python Package Managers 3/3

In this lecture, we work with pip, because ...

- ... of its wide use in the Python community.
- ... the package repository PyPI is large.
- ... it is still the fundamental way to package Python code.
- ... it is easy to understand and use.

---

## Python Enhancement Proposals (PEPs)

- PEP is an evolving design document which provides information regarding new features, processes and new environments.
- PEPs typically involve concise technical information, which also acts as standardizations.
- Packaging is standardized by [Packaging PEPs](https://peps.python.org/topic/packaging/).
- Example of a Packaging PEP: 

---

## Distribution Package vs. Import Package

Distribution package

- Something you can install.
- `pip install pkg`.

Import package

- An import package is a Python module which typically contains submodules.
- Writing `import pkg` in a file. Potentially also `from pkg import xyz`.
- Import package is available when its distribution package is installed.

Distribution package name and import package need not be the same, but usually is.

Read more about [distribution package vs. import package](https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/#distribution-package-vs-import-package).

---

## Steps in Packaging a Python Code

1. Get or create a source tree of the code.
2. Write a packaging configuration file, typically `pyproject.toml`.
3. Create build artifacts.
4. Upload the build artifacts to the package distribution service (PyPI).

---

## Create the source tree 1/2

Four places where naming is relevant:

- Name of the repository (on GitHub or GitLab).
- Name of the folder which has the source code.
- Name of the package as seen by PyPI.
- Name of the package to be used in the `import` statement.

**All names are independent of each other.**

Example folder structure:

```bash
generic_folder_name/
- src/
  - __init__.py
  - source-code.py
```

- The file `__init__.py` is required to import the `package_name/` as a package. This file is mostly empty
- `source-code.py` contains the code. It can be multiple files.

---

## Create the source tree 2/2

- Once the file structuring is complete, the source tree is:

```bash
generic_folder_name/
- pyproject.toml
- src/
  - __init__.py
  - source-code.py
  - tests/
```

---

## Write Configuration File 1/4

- File `pyproject.toml` written in the [TOML](https://github.com/toml-lang/toml) language.
- Minimum requirement is specifying a build tool via `[build-system]`.
- In the past, configuration files would be `setup.py` and `setup.cfg`.

Documentation about [writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml).

---

## Write Configuration File 2/4

`pyproject.toml` must contain a `[build-system]` table.

- `requires` key states which packages are required to build your package.
- `build-backend` key states which build backend tool is used. For example, `setuptools`.
- A build backend converts the source code into a distribution package.

`[project.scripts]` allows defining executable scripts.

Complete list of configuration options in [writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml).

---

## Write Configuration File 3/4

Let us look at an actual [pyproject.toml](https://github.com/precice/micro-manager/blob/develop/pyproject.toml).

---

## Write Configuration File 4/4

What happened to the files `setup.py` and `setup.cfg`?

- `setup.py` is a configuration file for the build backend `setuptools`.
- It still remains a valid configuration file.
- Using `setup.py` as a command line tool is **deprecated**, avoid `python setup.py`.
- `setup.cfg` is yet another valid configuration file for `setuptools`.
- These files are necessary if the Python package as C extensions.

Read more in [is setup.py deprecated?](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/#setup-py-deprecated).

---

## Create Build Artifacts 1/3

Source distribution (sdist) vs. built distribution (wheel)

---

## Create Build Artifacts 2/3

Source distribution (sdist)

- Contains files enough to install the package from source at end location.
- Run `python3 -m build --sdist source-tree-directory`.

---

## Create Build Artifacts 3/3

Built distribution (wheel)

- Contains files needed only to run package at end location.
- No compilation done, just a copy paste into a directory at end location.
- In most cases only one generic wheel is required. Exceptions are different Python interpreters, different OS configurations.
- Run `python3 -m build --wheel source-tree-directory`.
- If no wheel is available, pip falls back to source distribution.

---

## Uploading Build Artifacts

- The [twine](https://twine.readthedocs.io/en/latest/) is a tool to upload the build artifacts.
- Run `twine upload dist/package-name-version.tar.gz dist/package-name-version-py3-none-any.whl`.
- Why Twine?
    - Secure authentication of the user over HTTPS using a verified connection.
    - Its predecessor `python setup.py upload` required careful configuration, and is deprecated.
    - Encourages users to create distribution files to promote testing before releasing.
- The archive files are uploaded to a package index from where pip can get them.

---

## pip 1/3

- pip is a package installer to install packages from the Python package index [PyPI]((https://pypi.org/)).
- pip is itself a [package](https://pypi.org/project/pip/) which is available on PyPI.
- pip is open-source and is developed on [GitHub](https://github.com/pypa/pip).

---

## pip 2/3

Executing:

```bash
pip install package-name
```

leads to pip choosing a distribution file for the package and installing it in the environment.

```bash
python -m pip install package-name
```

is basically the same as:

```bash
pip install package-name
```

---

## pip 3/3

- pip tracks metadata to allow for easy updating and uninstalling of packages.
- pip is bundled together with Python 3.x, making it even easier to use.
- pip can install a package from a source distribution (`.tar.gz`) or a wheel distribution (`.whl`).

**Important**: Do not use

```bash
sudo pip install <package>
```

as there are security issues! Use a virtual environment or use

```bash
pip install --user <package>
```

---

## pip vs. pipx

- pip installs packages in the global namespace.
- pipx installs packages in individual virtual environments.
- pipx is meant to be used for applications run directly via the command line.
- For libraries, the recommended way is using pip in a virtual environment.

---

## pip Commands 1/2

Uninstall a package

```bash
pip uninstall <package>
```

Update a package

```bash
pip install --upgrade <package>
```

---

## pip Commands 2/2

List packages by running

```bash
pip freeze
```

or

```bash
pipx list
```

---

## PyPI

- [PyPI](https://pypi.org/) = **Python Package Index** is a repository of software developed in the Python community.
- PyPI itself is developed on GitHub through another software called [Warehouse](https://github.com/pypa/warehouse).
- PyPI has an informative [public dashboard](https://p.datadoghq.com/sb/7dc8b3250-85dcf667bd) to show its activity.
- A major advantage is the active maintenance of PyPI and the packages indexed in it.

---

## TestPyPI

- [TestPyPI](https://test.pypi.org/) is a testing instance of PyPI which does not affect the real index.
- Uploading the distribution to TestPyPI before PyPI is a standard pre-deployment step.
- Before using TestPyPI (or PyPI) you need an account and a PyPI API Token.
- Account creation and API Token generation is straightforward through the [registration page](https://test.pypi.org/account/register/).
- The API token is configured in a file `.pypirc` that is typically in the user home directory.

---

## Example of PyPI package: fenicsprecice

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)

---

## Installing the uploaded package

- The last step in the packaging pipeline is a sanity check done by installing the package that has been uploaded.
- The installation can be done by:

```bash
pip install --index-url https://test.pypi.org/simple/ <package-name>
```

---

## Important takeaways

Packaging of Python code is

- creation of a standardized folder structure to convert raw Python code into a project.
- creating and uploading distribution archives.
- Uploading distribution archives to a package index.

We saw the process of packaging and uploading to TestPyPI which is similar to uploading to the PyPI.
