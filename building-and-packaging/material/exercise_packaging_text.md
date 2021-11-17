# Exercise Part 1: Packaging Python Code

## Starting remarks

- Create a branch of the [exercise repository](https://github.com/Simulation-Software-Engineering/test-exercise-packaging/tree/main) named `<your-GitLab-username>-package` and complete all the tasks on the branch
- Deadline for submitting this exercise is **Thursday 25th November 09:00**
- The code in this exercise produces plots and in order to view them you need to use a GUI-based operating system or environment

## Brief idea of the exercise

In this exercise you will convert a raw Python code into a packaged code which is uploaded to the testing index of PyPI called [TestPyPI](https://test.pypi.org/). You may find such exercises online, for example, [the tutorial on python.org](https://packaging.python.org/tutorials/packaging-projects/), but in this exercise we will attempt to package a simulation code. After preparing the code we will create distributed archives and upload them to a package index

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

- Ensure that you have access to the [exercise repository](https://github.com/Simulation-Software-Engineering/test-exercise-packaging/tree/main)
- Clone the repository and create a branch with the name `<your-GitLab-username>-packaging`, for example **desaiin-package**
- Open the file `solver.py` and go through the file and try to understand the code components
- Install `python >= 3.6`
- Install pip, build, and Twine
- Install NumPy and Matplotlib with `pip`. The installation instructions can be found on the webpages (link in the Prerequisities section of this document)
- Run the code using `python3 solver.py` and observe the output
- You should see four plots combined into one figure. Save this figure on your system
- Take a few minutes to play around with some of the parameters in the solver file and observe how the output changes. For example you can change the value `D = 4.` in line 15 and try to observe changes in the output plots
- If you are interested in the theoretical background of the code, please have a look [in Section 7 of the "Learning Scientific Programming with Python" book](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)

## Step 2 - Refactoring the code

- It is usually a good idea to put different functionality in different files for better organization and code sustanability. We will do the same here
- Create a file `output.py` on the same level as `solver.py`
- Create two functions in the file `output.py` called `create_figure()` and `output_figures()`
- Port the appropriate parts of the code pertaining to figure creation and figure output from `solver.py` into these two functions
- Take care to pass the appropriate arguments to both these functions. Code refactoring should not affect the functionality, that is, the refactored code should work exactly as the original `solver.py`
- Once the output functionality has been separated from the solver, we need to bundle the solver itself into a function called `solve`. We need to do this because later on we will call this function after importing the package:

```python
from package_name import solver

solver.solve()
```

- Once you have refactored the code, try calling the `solve()` function again through a Python script as shown above or a Python shell. Compare the plots with the plots in the figure you saved earlier. Both outputs should be identical

- The function `solve()` should take in physical parameters which the user can vary. It is always a good idea to pass important physical parameters as input arguments to a function of a simulation software because you do not want to rebuild a package every time you change a parameter
- Try to think which parameters would be worth changing? These are typically related to the initial condition of the system being simulated

## Step 3 - Creating folder structure for packaging

- Now that you have a refactored code, replicate the folder structure we learnt in the lecture to prepare the code for packaging
- With the help of the lecture notes create additional files and arrange the files in a folder structure which is similar to what is shown in the notes
- There is ambiguity in how `setup.cfg` and `setup.py` are written and it is up to you to determine how much information is relevant for the code in this exercise. Also think if you really need both `setup.cfg` and `setup.py` for this exercise? Could you manage to publish the package with just one of them?
- The `README.md` file consists of a longer description about the code and what it does. Please try to provide as much information as possible regarding the code

## Step 4 - Create distribution packages

- With reference to the lecture notes, create distribution packages for this project
- After creating the distribution packages, check the `dist/` folder to ensure that the archive files have been created

## Step 5 - Create an account and a API Token on TestPyPI

- Create an account on [TestPyPI](https://packaging.python.org/guides/using-testpypi/)
- Create an API Token on TestPyPI
- **Note down the name and token value because this is the username and password for publishing**

## Step 6 - Uploading the package

- You should already have Twine installed on your system
- Upload the distribution archives using the commands shown in the lecture notes
- Go to TestPyPI and view the package which has been uploaded
- Take a screenshot of the TestPyPI webpage which displays your package. This screenshot will be used for submission

## Step 7 - Testing the deployed package

- Using the commands from the lecture notes try to install the package using `pip` and also run the code by importing the `solve()` functionality in a Python script or an interactive Python shell

## Step 8 - Submitting the exercise

- Open a pull request from your branch to the `main` branch of the exercise repository
- Add the TestPyPI screenshot in the description of the pull request
