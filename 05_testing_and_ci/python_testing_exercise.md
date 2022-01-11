# Exercise: Testing Python Code

## Starting remarks

- [Exercise repository link]()
- Deadline for submitting this exercise is **Thursday 20th January 2022 09:00**.

## Prerequisites

- An operating system / software / environment where you can install Python and some basic Python tools
- An editor or IDE to edit Python code and write text files
- The following Python tools:
    - Python (version >= 3)
    - [pip](https://pypi.org/project/pip/)
    - [NumPy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [pytest]()
    - [unittest]()
    - [coverage]()

## Step 1 - Getting familiar with the code

- The code in `diffusion2d.py` is in principle the code used for the Python packaging exercise. The main difference is that now the code has a class `SolveDiffusion2D` which has several member functions.
- Each function name states what the function does, for example the function `initialize_domain()` takes in input arguments width, height, dx and dy and sets the values to member variables of the class and also calculates the number of points in X and Y directions.
- The functions `initialize_domain` and `initialize_physical_parameters` have default values for all input parameters, hence they can be called without any parameters.
- The file also has a `main()` function which shows a step-by-step procedure to solve the diffusion problem using an object of the class `SolveDiffusion2D`.
- Make sure that `NumPy` and `Matplotlib` is installed on the system that you are working on.
- Try to run this example in the following way:

```python
python3 diffusion2d.py
```

- Observe the output produced, it should be the same output as what was seen during the packaging exercise.
- Spend some time understanding what each function does. It is important to understand all the functions as you will be writing tests for these functions.

## Step 2 - Adding assertion statements

## Step 3 - Writing unit tests

- In the repository there is a folder `tests/`. In this folder there are two folders `unit/` and `integration/`. The first tests written will be unit tests.
- In the file `tests/unit/test_diffusion2d_functions.py` there is already a skeleton code for three unit tests which are to be implemented.
- The name of each test is of the format `test_<name_of_function_being_tested>`.
- As these are unit tests, in each test only the call to the respective function needs to be made. No other function from `diffusion2d.py` must be called.
- In this step you will write all the tests in a way that they can be run using `pytest` and not using the `unittest` format.
- As an example, let us look at how we can write a unit test for the function `initialize_domain`
    - When the function `initialize_domain` is being tested, you need to first identify which variables are being calculated in this function.
    - In this case they are the variables `nx` and `ny`. Now choose some values for the variables `w`, `h`, `dx`, and `dy` which are different from the default values. For these values manually calculate the `nx` and `ny`.
    - These manually calculated values are the expected values in this test.
    - Now call the function `initialize_domain` which the chosen values of `w`, `h`, `dx`, and `dy` and using check if the `nx` and `ny` in the class member variables is equal to your expected values.
    - Note that you have the object of the class `SolveDiffusion2D` and hence you can access member variables, for example `solver.nx` and `solver.ny`. This is useful to check the actual values.
    - This check is done using an assertion statement, something that you have already seen in the demo during the lecture.
- Using a similar workflow, complete the other two unit tests.
- If everything is done correctly then after running `pytest`, all the tests should pass.
- How can we make sure that we have written correct tests? By breaking them purposely!

## Step 4 - Writing unit tests using unittest

## Step 5 - Writing integration tests

## BONUS Step 6 - Checking test coverage
