# `pip`: Python Packaging Tool (Notes)

**Note**: Maybe run everything in a fresh Docker container. I built the container `jaustar/spack-package-tutorial-base` locally for myself. It contains installed/downloaded Spack, that was not set up yet, i.e., one needs to run `spack compiler find` and `spack external find`. `clingo` needs to be downloaded first as well.

## 1. Installing packages with `pip`

Installing a package

```bash
pip install micro-manager-precice
```

Install a specific version of a package

```bash
pip install micro-manager-precice==0.0.2
```

Uninstalling a package

```bash
pip uninstall micro-manager-precice
```

- By default `pip` tries to install packages in the system directory, for example `/usr/local/lib/python<version>`. This is problematic as it has no user isolation and it requires root privileges.
- With the `--user` flag, packages are installed in the `home` directory, typically at `/home/user/.local/lib/python<version>/site-packages/`. This is important when one is not working with virtual environments.

Installing a package from a folder

```bash
pip install --user .
```

- A `build` folder is created and the package files are copied into it.
- But now `pip3 uninstall package-name` does not work as `pip` looks in the home path. Removal of package can be done by deleting the `build` folder or using manually using `setup.py`.

**NOTE**: To successfully install `micro-manager-precice`, the dependencies `libopenmpi-dev`, `pkg-config`and `precice` which can be installed in the following way

```bash
apt install libopenmpi-dev pkg-config
apt install wget
wget https://github.com/precice/precice/releases/download/v2.5.0/libprecice2_2.5.0_jammy.deb
apt install ./libprecice2_2.5.0_jammy.deb
```

## 2. Getting information of currently installed packages

```bash
pip list
```

or for a specific package

```bash
pip show micro-manager-precice
```

## 3. Installing dependencies of a package

- Using `requirements.txt` is a standard way to handle dependency installation.

```bash
pip install -r requirements.txt

```

## 4. Running `pip` as a Python module

```bash
python -m pip install package-name
```

## 5. Getting information of installed packages

Get package information on the terminal using

```bash
pip show package-name
```

## 6. How to read a PEP

- Have a look at [PEP 8](https://peps.python.org/pep-0008/)

## 7. Understanding a PyPI package webpage

- Having a look at [fenicsprecice](https://pypi.org/project/fenicsprecice/)
