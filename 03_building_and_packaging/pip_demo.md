# `pip`: Python Packaging Tool Demo Notes

**Note**: Maybe run everything in a fresh Ubuntu Docker container. Launch such a container using `docker run --rm -it ubuntu:jammy`. The other option is to work in a Python virtual environment. An environment can be created as follows

```bash
python -m venv env-name
source env-name/bin/activate
```

## 0. Getting `pip`

If Python has been installed using a system package manager like `apt`, it will not come with `pip`. `pip`can be installed in several ways

```bash
python -m ensurepip --upgrade
```

or

```bash
apt install pip
```

- If installed with Python, the Python version is used to determine which version of `pip` is installed. So Python 3.8 will install `pip3.8`.
- In general `pip3` works with Python v3.x.

## 1. Installing packages with `pip`

Let us install the finite element library [Nutils](https://nutils.org/)

```bash
pip install nutils
```

Install a specific version of a package

```bash
pip install nutils==6.0.0
```

Uninstalling a package

```bash
pip uninstall nutils
```

- By default `pip` tries to install packages in the system directory, for example `/usr/local/lib/python<version>`. This is problematic as it has no user isolation and it requires root privileges.
- With the `--user` flag, packages are installed in the `home` directory, typically at `/home/user/.local/lib/python<version>/site-packages/`. This is important when one is not working with virtual environments.

Installing a package from a folder

```bash
git clone https://github.com/evalf/nutils.git
cd nutils
pip install --user .
```

- A `build` folder is created and the package files are copied into it.
- But now `pip uninstall package-name` does not work as `pip` looks in the home path. Removal of package can be done by deleting the `build` folder or using manually using `setup.py`.

## 2. Getting information of currently installed packages

```bash
pip list
```

or for a specific package

```bash
pip show nutils
```

## 3. Running `pip` as a Python module

```bash
python -m pip install package-name
```

## 4. How to read a PEP

- Have a look at [PEP 8](https://peps.python.org/pep-0008/)

## 5. Understanding a PyPI package webpage

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)
