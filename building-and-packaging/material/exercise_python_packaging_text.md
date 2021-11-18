# Exercise Part 1: Packaging Python Code

## Starting remarks

- Deadline for submitting this exercise is **Thursday 25th November 09:00**.
- The code in this exercise produces plots and in order to view them you need to use a GUI-based operating system or environment.

## Brief idea of the exercise

In this exercise you will convert a raw Python code into a packaged code which is uploaded to the testing index of PyPI called [TestPyPI](https://test.pypi.org/). You may find such exercises online, for example, [the tutorial on python.org](https://packaging.python.org/tutorials/packaging-projects/), but in this exercise we will attempt to package a simulation code. After preparing the code we will create distributed archives and upload them to a package index.

## Prerequisites

- An operating system / software / environment where you can install Python and some basic Python tools
- An editor or IDE to edit Python code and write text files
- The following Python tools:
    - Python (version >= 3)
    - [pip](https://pypi.org/project/pip/)
    - [NumPy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [build](https://pypa-build.readthedocs.io/en/latest/)
    - [Twine](https://twine.readthedocs.io/en/latest/)

## Step 1 - Acquiring the raw code and getting familiar with it

- Ensure that you have access to the [exercise repository](https://github.com/Simulation-Software-Engineering/test-exercise-packaging/tree/main).
- Fork this repository.
- Open the file `solver.py` and go through the file and try to understand the code components.
- Install `python >= 3.6`.
- Install pip, build, and Twine.
- Install NumPy and Matplotlib with `pip`. The installation instructions can be found on the webpages (link in the Prerequisities section of this document).
- Run the code using `python3 solver.py` and observe the output. You should see four plots combined into one figure. Save this figure on your system.
- **Information about solver.py**: This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
- Take a few minutes to play around with parameters `dx`, `dy` and `D` in the solver file and observe how the value of `dt` and the output changes. Do you notice if the code takes more or less time to finish the computation? *This tuning is only for you to understand the underlying physical phenomenon and not part of the evaluation.*
- If you are interested in the theoretical background of the code, please have a look [in Chapter 7 of the "Learning Scientific Programming with Python" book](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Step 2 - Refactoring the code

- It is usually a good idea to put different functionality in different files for better organization and code sustanability. We will do the same here.
- Create a file `output.py` on the same level as `solver.py`.
- Create two functions in the file `output.py` called `create_plot()` and `output_plots()`.
    - The function `create_plot()` creates one plot for a particular time stamp. In the earlier figure output this would be one of the four plots. You will find this functionality inside the time loop in `solver.py`
    - The function `output_plots()` outputs all the four plots as one figure. You will find this functionality outside of the time loop and at the end of `solver.py`
- Port the appropriate parts of the code pertaining to figure creation and figure output from `solver.py` into these two functions.
- Take care to pass the appropriate arguments to both these functions. Code refactoring should not affect the functionality, that is, the refactored code should work exactly as the original `solver.py`.
- Once the functionality is ported, you need to import it into the `solver.py`. This is done in the following way:

```python
from .output import create_plot, output_plots
```

- Once the output functionality has been separated from the solver, we need to bundle the solver itself into a function called `solve` in `solver.py`. We need to do this because later on we will call this function after importing the package:

```python
from package_name import solver

solver.solve()
```

- Once you have refactored the code, try calling the `solve()` function again through a Python script as shown above or a Python shell. Compare the plots with the plots in the figure you saved earlier. Both outputs should be identical.
- The function `solve()` should take in physical parameters which the user can vary. In this case change the parameters `dx`, `dy` and `D` such that they are passed to the `solve()` function by the user. Provide default values for all three of these parameters.

## Step 3 - Creating folder structure for packaging

- Now that you have a refactored code, replicate the folder structure we learnt in the lecture to prepare the code for packaging
- With the help of the [lecture notes](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/packaging_python_slides.md) create additional files `setup.py`, `__init__.py`, `README.md` and the `src/` directory.
- The `README.md` file consists of a longer description about the code and what it does. Take the information about the code from Step 1 of this exercise and add it to the README. In addition to this fill out the emtpy sections of the README with relevant information.
- In `setup.py` name your package `<your-GitLab-username>diffusion2D`. We will use semantic versioning, so the version you are developing will be `0.0.1`. The package url is the url of the GitHub repository of this exercise code.
- Try to put `classifiers` in your `setup()`.

## Step 4 - Create distribution archives

- With reference to the lecture notes, create distribution archives for this project. Use `build` to create the distribution archives.
- After creating the distribution packages, check the `dist/` folder to ensure that the archive files have been created.
- **Important**: If for some reason the package does not work and you wish to upload a changed state of the package, then you have to remove all contents of `dist/*` before creating new distribution archives

## Step 5 - Create an account and a API Token on TestPyPI

- Create an account on [TestPyPI](https://packaging.python.org/guides/using-testpypi/).
- Create an API Token on TestPyPI.
- **Note down the name and token value because this is the username and password for publishing**.
- Copy the API Token and Password and configure it on your system in the file `$HOME/.pypirc`

## Step 6 - Uploading the package

- You should already have Twine installed on your system.
- Upload the distribution archives using the commands shown in the lecture notes.
- Go to TestPyPI and view the package which has been uploaded.
- Take a screenshot of the TestPyPI webpage which displays your package.
- **Important**: Add the TestPyPI screenshot in the description of the pull request opened for submission.

## Step 7 - Testing the deployed package

- Using the commands from the lecture notes try to install the package using `pip` and also run the code by importing the `solve()` functionality in a Python script or an interactive Python shell.

## Step 8 - Submitting the exercise

- Open a pull request with the name `Packaged code for PyPI by <your-GitLab-username>` from your fork to the `main` branch of the exercise repository.
