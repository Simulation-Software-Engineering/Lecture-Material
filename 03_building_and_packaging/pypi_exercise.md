# Exercise: Packaging Python Code

## Starting remarks

- [Exercise repository link](https://github.com/Simulation-Software-Engineering/diffusion2D)
- Deadline for submitting this exercise is **Wednesday 19th November 09:00**.
- The code in this exercise produces plots and in order to view them you need to use a GUI-based operating system or environment.

## Brief idea of the exercise

In this exercise you will convert a raw Python code into a packaged code which is uploaded to the testing index of PyPI called [TestPyPI](https://test.pypi.org/). You may find such exercises online, for example, [the tutorial on python.org](https://packaging.python.org/tutorials/packaging-projects/), but in this exercise we will attempt to package a simulation code. After preparing the code we will create build artifacts and upload them to the package index.

## Prerequisites

- An operating system / software / environment where you can install Python and some basic Python tools.
- An editor or IDE to edit Python code and write text files.
- The following Python tools:
    - Python (version >= 3)
    - [pip](https://pypi.org/project/pip/)
    - [NumPy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [build](https://pypa-build.readthedocs.io/en/latest/)
    - [twine](https://twine.readthedocs.io/en/latest/)

## Step 1 - Acquiring the code and getting familiar with it

- Fork the [exercise repository](https://github.com/Simulation-Software-Engineering/diffusion2D).
- Open the file `diffusion2d.py` and go through the file and try to understand the code components.
- Check if your system has Python version >= 3.6 and update it if it is older than 3.6.
- Install pip, build, and twine.
- Install NumPy and Matplotlib with `pip`. The installation instructions can be found on the webpages (links in the Prerequisites section of this document).
- Run the code using `python diffusion2d.py` and observe the output. You should see four plots combined into one figure. Save this figure on your system.
- **Information about diffusion2d.py**: This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the [finite-difference method](https://en.wikipedia.org/wiki/Finite_difference_method). The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
- Take a few minutes to play around with parameters `dx`, `dy` and `D` in the solver file and observe how the value of `dt` and the output changes. Do you notice if the code takes more or less time to finish the computation?
- If you are interested in the theoretical background of the code, please have a look in [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Step 2 - Refactoring the code

- It is good practice to put code specific to a functionality in a separate file for better organization and code sustainability. We will do the same here.
- Create a file `output.py` on the same level as `diffusion2d.py`.
- Create two functions in the file `output.py` called `create_plot()` and `output_plots()`.
    - The function `create_plot()` should create one plot for one time stamp. In the earlier output, this would be one of the four plots. You will find this functionality inside the time loop in `diffusion2d.py`.
    - The function `output_plots()` should output all the four plots as one figure. You will find this functionality outside of the time loop and at the end of `diffusion2d.py`.
- Port the appropriate parts of the code pertaining to figure creation and figure output from `diffusion2d.py` into these two functions.
- Take care to pass the appropriate arguments to both these functions and also return the correct quantities. Code refactoring should not affect the functionality, that is, the refactored code should work exactly as the original `diffusion2d.py`.
- Once the functionality is ported, you need to import it into the `diffusion2d.py`. This is done in the following way

```python
from output import create_plot, output_plots
```

- Note that the `from output` command will only import functions from `output.py` if no global Python package with the name `output` exists. If another package named `output` exists, then a relative import needs to be done.
- Once the output functionality has been separated from the solver, we need to bundle the solver itself into a function called `solve` in `diffusion2d.py`. We need to do this because later on we will call this function after importing the package in the following way,

```python
from package_name import diffusion2d

diffusion2d.solve()
```

- Once you have refactored the code, try calling the `solve()` function again through a Python script or directly in a Python shell. Compare the plots with the plots in the figure you saved earlier. Both outputs should be identical.
- The function `solve()` should take in physical parameters as input arguments. In this case, change the parameters `dx`, `dy` and `D` such that they are passed to the `solve()` function by the user. Provide default values for all three of these parameters.
- In some cases an additional `__init__.py` file may be necessary on each level of the directory structure to ensure that the local import `from .output ...` works. First try to run the refactored code without adding any additional file, and if it is does not work, add the `__init__.py` file. The `__init__.py` should be empty in this case. An explanation of why this file is necessary is found in the [Python packaging documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#a-simple-project).

## Step 3 - Creating folder structure for packaging

- Now that you have a refactored code, replicate the folder structure we learned in the lecture to prepare the code for packaging.
- As discussed in the lecture, create the configuration file `pyproject.toml` file, and a `README.md`.
- It is recommended to have the `package-name/` folder which has the source code in it. Select an appropriate package name.
- **Note**: General recommendation is to have the name of the folder having the source files to be same as the name of the package as seen when imported at the time of use.
- The `README.md` file consists of a longer description about the code and what it does. Take the information about the code from Step 1 of this exercise and add it to the README. In addition to this fill out the empty sections of the README with relevant information.
- In the `pyproject.toml`, name your package `<your-GitLab-username>_diffusion2d` (the underscore `_` between your GitLab username and diffusion2d is important, because any other symbol will not work). We will use semantic versioning, so the version you are developing will be `0.0.1`. The package url is the url of the GitHub repository of this exercise code.
- As the package should be easy to install and provide maximum possible information, try to include as many configuration options as possible.
- **Hint**: Look at the guide on [configuring setuptools with pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

## Step 4 - Create distribution archives

- With reference to the lecture notes, create distribution archives for this project. Use the `build` tool to create the distribution archives.
- After creating the distribution packages, check the `dist/` folder to ensure that the archive files have been created.
- **Important**: If for some reason the package does not work and you wish to upload a changed state of the package, then you have to remove all contents of `dist/` before creating new distribution archives.

## Step 5 - Create an account and a API Token on TestPyPI

- Create an account on [TestPyPI](https://packaging.python.org/guides/using-testpypi/).
- Create an API Token on TestPyPI.
- **Note down the name and token value because this is the username and password for publishing**.
- Copy the API Token and Password and configure it on your system in the file `$HOME/.pypirc`.

## Step 6 - Uploading the package

- Upload the distribution archives to TestPyPI.
- Go to TestPyPI and view the package which has been uploaded.
- Take a screenshot of the TestPyPI webpage which displays your package.

## Step 7 - Testing the deployed package

- Using the commands from the lecture notes try to install the package using `pip` and also run the code by importing the `solve()` functionality in a Python script or an interactive Python shell.
- Even though your package is on TestPyPI, the dependencies of the package need to be installed from PyPI. To make sure that the dependencies are installed from PyPI and not TestPyPI, use the `--extra-index-url` flag in the `pip` command appropriately.

## Step 8 - Submitting the exercise

- Open a pull request with the name `Packaged code for PyPI by <your-GitLab-username>` from your fork to the `main` branch of the exercise repository.
- Only push the `pyproject.toml`, `README.md`, and `__init__.py` in addition to the refactored code.
- **Important**: Add the TestPyPI screenshot in the description of the pull request opened for submission.

## Bonus: Using Versioneer to handle versioning of code

- Use [Versioneer](https://pypi.org/project/versioneer/) to handle the versioning in your package.
