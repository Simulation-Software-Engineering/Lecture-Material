# `pip`: Python Packaging Tool Demo Notes

**Note**: It is recommended run everything in a Ubuntu Docker container or a virtual environment. Launch a container using `docker run --rm -it ubuntu:jammy`. A virtual environment can be created as follows

```bash
python -m venv env-name
source env-name/bin/activate
```

## 0. Getting `pip`

A clean Docker container may not have Python installed. Install Python using `apt`: `apt install python3`. If Python has been installed using a package manager like `apt`, it will not come with `pip`. `pip`can be installed in several ways

```bash
python -m ensurepip --upgrade
```

or

```bash
apt install python3-pip
```

- If installed with Python, the Python version is used to determine which `pip` is installed. So Python 3.8 will install a `pip` by the name of `pip3.8` which will be compatible with Python 3.8.
- In general `pip3` works with Python v3.x.
- **Note**: Different `pip` names (`pip3`) are not to be confused with the version of the `pip` package, which can be seen with `pip --version`.

## 1. Installing packages with `pip`

Let us install the finite element library [Nutils](https://nutils.org/).

```bash
pip install nutils
```

Install a specific version of a package

```bash
pip install nutils==7.0.0
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
