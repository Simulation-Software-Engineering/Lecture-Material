# Exercise: Testing Python Code

## Starting Remarks

- [Exercise repository link](https://github.com/Simulation-Software-Engineering/testing-python-exercise-wt2223)
- Deadline for submitting this exercise is **Thursday 26th January 2023 09:00**.
- Structure all the tests in a format similar to what is shown in the [demo code](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/examples/python_testing).

## Prerequisites

- An operating system / software / environment where you can install Python and some basic Python tools
- An editor or IDE to edit Python code and write text files
- The following Python tools:
    - Python (version >= 3)
    - [pip](https://pypi.org/project/pip/)
    - [NumPy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html#install-pytest)
    - [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
    - [coverage](https://coverage.readthedocs.io/en/6.2/#quick-start)
    - [tox](https://tox.wiki/en/4.0.15/installation.html)

## Step 1 - Getting Familiar With the Code

- Fork the [repository](https://github.com/Simulation-Software-Engineering/testing-python-exercise-wt2223).
- The code in `diffusion2d.py` is in principle the same code used for the Python packaging exercise. The main difference is that now the code has a class `SolveDiffusion2D` which has several member functions.
- Each function name states what the function does, for example the function `initialize_domain()` takes in input arguments `w` (width), `h` (height), `dx` and `dy` and sets the values to member variables of the class and also calculates the number of points in x and y directions.
- The functions `initialize_domain` and `initialize_physical_parameters` have default values for all input parameters, hence they can be called without any parameters.
- The file also has a `main()` function which shows a step-by-step procedure to solve the diffusion problem using an object of the class `SolveDiffusion2D`.
- Make sure that `NumPy` and `Matplotlib` are installed on the system that you are working on.
- Run this example by running `python3 diffusion2d.py`.
- Observe the output produced, it should be the same output as what was seen during the packaging exercise.
- Spend some time understanding what each function does. It is important to understand all the functions as you will be writing tests for these functions.

## Step 2 - Adding Assertion Statements

- Add assertion statements to the functions `initialize_domain` and `initialize_physical_parameters` which check whether all input parameters have type `float`.
- Rerun the code after inserting all the assertion statements? Does the code break? Which parameters are problematic?
- The default values of some of the input parameters like `T_hot` and `T_cold` are in fact integers and need to be changed. Change these values to floats and rerun the code to make sure that all assertions are returning true.

## Step 3 - Writing Unit Tests

- Now you will write all the tests in a way that they can be run using `pytest`.
- In the repository there is a folder `tests/`. In this folder there are two folders `unit/` and `integration/`. The first tests written will be unit tests.
- In the file `tests/unit/test_diffusion2d_functions.py` there is already a skeleton code for three unit tests which are to be implemented. The name of each test is of the format `test_<name_of_function_being_tested>`.
- As these are unit tests, in each test, only the call to the respective function needs to be made. No other function from `diffusion2d.py` must be called. If another function call is required to define some member variables, it can be evaded by directly defining the member variables in the test. All the member variables can be accessed directly using the class object.
- As an example, let us look at how we can write a unit test for the function `initialize_domain`.
    - When the function `initialize_domain` is being tested, you need to first identify which variables are being calculated in this function.
    - In this case they are the variables `nx` and `ny`. Now choose some values for the variables `w`, `h`, `dx`, and `dy` which are different from the default values. For these values, manually calculate the values of `nx` and `ny`. These manually calculated values are the expected values in this test.
    - Now call the function `initialize_domain` with the chosen values of `w`, `h`, `dx`, and `dy` and using an assertion statement, check if the values of `nx` and `ny` in the class member variables are equal to your expected values.
    - Note that you have the object of the class `SolveDiffusion2D` and hence you can access member variables, for example `solver.nx` and `solver.ny`. This is useful to check the actual values.
- Using a similar workflow, complete the other two unit tests.
- Run the tests using `pytest`.
- It is observed that in some instances `pytest` is not able to find the tests. One reason is the way pytest is installed, which is typically either using `pip` or `apt`. Refer to the [corresponding section](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_demo.md#pytest) in the demo for more details. If such errors occur, then try to explicitly point pytest to the relevant test file. For example:

```bash
pytest tests/unit/test_diffusion2d_functions.py
```

- If everything is done correctly, then after running `pytest` all the tests should pass.
- How can you make sure that you have written correct tests? By breaking them purposely!
    - Introduce a bug in a function on purpose and then re-run the test to see if the test fails.
    - Lets try this in the function `initialize_domain`. In line 42 of `diffusion2d.py`, change the calculation from `self.nx = int(w / dx)` to `self.nx = int(h / dx)`. This is clearly a mistake and our test should catch it.
    - Now re-run pytest. Did the test catch the bug? If yes, then you have written the test correctly. If the test does not catch the bug, try to think why did it not? Is your choice of values for the parameters `w`, `h`, `dx` and `dy` responsible for it? If the test is run with `w = h` then this bug will not be caught. What do we learn from this? We learn that the test fixture should be as general as possible and we should ensure that we are not testing special scenarios. A domain with `w = h` is a square domain which is a special case of a rectangular domain with arbitrary values for `w` and `h`.
- **Important step**: A failing test in pytest will produce an output log in the terminal. Copy this output log in a code block in the `README.md` file under the section *pytest log*. This log output will be part of the submission and hence is important.
- Purposely break all the unit tests and copy the failing tests logs into the aforementioned section in the README file.
- Before moving on from this step, make sure that you have reverted all the intentionally introduced bugs in the original code.

## Step 4 - Writing Unit Tests Using unittest

- Now you will write all the tests in a way that they can be run using `unittest`.
- Modify the unit tests written in the previous section to be run with unittest. This is done in the same file `tests/unit/test_diffusion2d_functions.py`.
- Start by creating a class `TestDiffusion2D` which is derived from the class `unittest.TestCase`. Migrate all the tests inside the class and change them to be member functions of the class. Note that the parameter `self` needs to be used in the input parameters of all member functions and also while defining and using member variables.
- The tests themselves will not change. The same functions will be tested in the same way, just with the `unittest` framework.
- Identify the common steps necessary in all the tests and transfer the functionality to the function `setUp`. One example of this is the definition of the object of class `SolveDiffusion2D`.
- The main change is in the assertion statements. Change the assertion statements to the format as required by `unittest`. Refer to the lecture demo for an example on how to do this.
- Using the same logic as in the previous step, intentionally break the tests to make sure that the tests are constructed correctly.
- **Important step**: A failing test in unittest will produce an output log in the terminal. Copy this output log in a code block in the README file under the section *unittest log*. This log output will be part of the submission and hence is important.
- Purposely break all the unit tests and copy the failing tests logs into the aforementioned section in the README file.
- Before moving on from the unit tests, make sure that you have reverted all the intentionally introduced bugs in the original code.

## Step 5 - Writing Integration Tests

- You will now write integration tests for this code **using pytest**. The integration tests will be written in the file `tests/integration/test_diffusion2d.py`.
- Integration tests will be written for the functions `initialize_physical_parameters` and `set_initial_conditions`. As these are integration tests, each test should check how different functions from `SolveDiffusion2D` work together.
- For example, let us look at how the test for `initialize_physical_parameters` will look like.
    - First step is to select some values for the input parameters to the function `initialize_physical_parameters` and also the function `initialize_domain`.
    - Looking at the functionality in `initialize_physical_parameters` we understand that the most relevant variable being calculated is `dt`.
    - Based on the choice of all input parameters, manually compute the value of `dt` for the test. This is the expected result.
    - Call the function `initialize_domain` and then the function `initialize_physical_parameters`.
    - Compare the value of the member variable `dt` with the manually computed `dt` using an assertion statement.
- Now also write a similar integration test for `set_initial_conditions`. Note that this will be the most extensive test from the whole set. The field variable `u` is computed in `set_initial_conditions`, which is a 2D array. The test should have a computation which computes a similar `u` array for a user-defined set of initial parameters. This computed `u` is the expected result.
- Using the same logic as in the previous steps, intentionally break the tests to make sure that the tests are constructed correctly.
- **Important step**: A failing test in integration test will produce an output log in the terminal. Copy this output log in a code block in the `README.md` file under the section *Integration test log*. This log output will be part of the submission and hence is important.
- Purposely break all the integration tests and copy the failing tests logs into the aforementioned section in the README file.
- Before moving on from the integration tests, make sure that you have reverted all the intentionally introduced bugs in the original code.

## Step 6 - Checking Test Coverage

- Using the coverage tool generate a HTML report of the code coverage of all the tests.
- Open the report file in a browser and print the report to a file called `coverage-report.pdf`. Add this file to the repository.
- **Note**: coverage can be used with both `pytest` and `unittest`. In this case generating the report of the unit tests using unittest is sufficient.

## Step 7 - Automation Using tox

- Write a `tox.ini` file such that by running the command `tox`, both `pytest` and `unittest` are executed.
- Use the `requirements.txt` file to send all the dependencies information to tox.

## Step 8 - Submission

- Open a pull request titled `Adding tests by <GitLab username>` from your fork to the main repository.
