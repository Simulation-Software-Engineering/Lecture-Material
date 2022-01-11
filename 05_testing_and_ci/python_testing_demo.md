# Notes for Demos of Python Testing Frameworks

Example code is in [05_testing_and_ci/examples](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/examples)

## Software code used

- The file `operations.py` consists of two functions `find_max` and `find_mean` which calculate the maximum and mean of all elements of a list. The `main()` routine in the file applies the functions to a list and prints the output.
- `main()` function in `operations.py` has assertion statements to check if the correct data type is passed to specific functions.
- Assertion statements are the most basic way of testing code and are also used in unit and integration testing as demonstrated here.
- Tests are written in the file `test_operations.py`. The `test_*` prefix in the name is required so that pytest detects the file as a testing file. Suffix form `*_test.py` also works.
- In all there are two unit tests, one integration test and one regression test.
- The unit tests test the individual functions `find_max` and `find_mean`.
- The integration test triggers both the functions `find_max` and `find_mean` and checks that the mean is less than the maximum, something that should always be true for a set of numbers.
- The regression test first reads an old data set and a mean value from a CSV file. Then the function `find_mean` is run with the old data set and the new mean value is compared to the old one.

## pytest

- pytest is installed by:

```bash
pip install -U pytest
```

- All tests can be run using the command-line tool called `pytest`. Just type `pytest` in the working directory and hit ENTER.
- One test is expected to fail. Reading the error message we understand that the failure occurs because floating-point variable comparison is not handled correctly.
- We need to tell pytest that while comparing two floating-point variables the value needs to be correct only up to a certain tolerance limit. To do this the expected mean value needs to be changed by uncommenting the line in the following part of the code:

```python
# Expected result
    expected_mean = 78.33
    # expected_result = pytest.approx(78.3, abs=0.01)
```

- **Comparing floating point variables** needs to be handled in functions like `find_average` and is done using `pytest.approx(value, abs)`. The `abs` value is the tolerance up to which the floating-point value will be checked, that is `78.33 +/- 0.01`.
- Even if one test fails, pytest runs all the tests and gives a report on the failing test. The assertion failure report generated my pytest is also more detailed than the usual Python assertion report. When the test fails, the following is observed:

```bash
============================================================================================ FAILURES ======================================================================================
__________________________________________________________________________________________ test_find_mean __________________________________________________________________________________

    def test_find_mean():
        """
        Test operations.find_mean
        """
        # Fixture
        data = [43, 32, 167, 18, 1, 209]

        # Expected result
        expected_mean = 78.33
        # expected_result = pytest.approx(78.33, abs=0.01)

        # Actual result
        actual_mean = find_mean(data)

        # Test
>       assert actual_mean == expected_mean
E       assert 78.33333333333333 == 78.33

test_operations.py:44: AssertionError
```

- pytest not only points to the assertion but also prints out the test which has failed.
- It is worth noting that pytest is also able to detect tests from other files and run them even if they are not in the conventional test formats.
- pytest is able to detect tests in several forms of folder structures, and the folder structures have advantages and disadvantages. More information on this is in the [documentation](https://docs.pytest.org/en/6.2.x/goodpractices.html#choosing-a-test-layout-import-rules). In this demo we use the simplest folder structure where the source file and the test files are at the same directory level. Very often this is not the case. A more organized folder structure can be generated:

```bash
operations.py
tests/
    test_operations.py
    test_operations_unittests.py
        ...
```

- Putting the tests in a folder `tests/` does not affect the behavior of pytest. When pytest is run from the original directory, the tests are found and run.

## unittest

- Base class `unittest.TestCase` is used to create a test suite consisting of all the tests of a software.
- Each test is now a function of a class which is derived from the class `unittest.TestCase`.
- The same tests as for `pytest` are implemented using `unittest` in the file `test_operations_unittests.py`. The tests are functions of a class named `TestOperations` which tests our mathematical operations. The class `TestOperations` is derived from `unittest.TestCase`.
- unittest can be run by:

```bash
python -m unittest
```

- unittest.TestCase offers functions like `assertEqual`, `assertAlmostEqual`, `assertTrue`, etc. for use instead of the usual assertion statements. These statements help the test runner to accumulate all test results and generate a test report.
- `unittest.main()` provides an option to run the tests from a command-line interface.
- `setUp` function is executed before all the tests. Similar a clean up function `tearDown` exists.
- The intention is to group together sets of similar tests in an instant of `unittest.TestCase` and have multiple such instances.
- Decorators such as `@unittest.skip`, `@unittest.skipIf`, `@unittest.expectedFailure` can be used to gain flexibility over working of tests.
- `unittest.TestCase.subTest` can be used to distinguish parameters inside the body of a test.

## coverage

- Installing coverage using pip:

```bash
pip install -U coverage
```

- Testing frameworks can be run via coverage. Lets take our first example and run pytest via coverage:

```bash
coverage run -m pytest
```

- coverage does not generate any output immediately as it would interfere with the test output.
- Code coverage information is stored in a file `.coverage` in the working directory. This information can be viewed using:

```bash
coverage report -m
```

- A more fancier report can be viewed by generating HTML output using

```bash
coverage html
```

- The file `htmlcov/index.html` can be opened in a browser to view the test coverage report.
