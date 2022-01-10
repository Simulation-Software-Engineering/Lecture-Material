# Notes for Demos of Python Testing Frameworks

Example code is in [05_testing_and_ci/examples](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/examples)

## pytest

- **Note**: `main()` function in `operations.py` has assertion statements to check if the correct data type is passed to specific functions.
- Assertion statements are the most basic way of testing code and are also used in unit and integration testing.
- Tests are written in the file `test_operations.py`. The `test_*` prefix in the name is required so that pytest detects the file as a testing file. Suffix form `*_test.py` also works.
- In all there are two unit tests, one integration test and one regression test.
- The unit tests test the individual functions `find_max` and `find_average`.
- All tests can be run using the command-line tool called `pytest`.
- **Comparing floating point variables** needs to be handled in functions like `find_average` and is done using `pytest.approx(value, abs)`.
- Even if one test fails, pytest runs all the tests and gives a report on the failing test. The assertion failure report generated my pytest is also more detailed than the usual Python assertion report.
- pytest can run unittest suites directly using `pytest tests`.
- pytest is able to detect tests in several forms of folder structures, and the folder structures have advantages and disadvantages. More information on this is in the [documentation](https://docs.pytest.org/en/6.2.x/goodpractices.html#choosing-a-test-layout-import-rules).
- Example:

```
setup.py
my_software/
    __init__.py
    main.py
    feature.py
    test/
        __init__.py
        test_one.py
        test_two.py
        ...
```

## unittest

- Base class `unittest.TestCase` is used to create a test suite consisting of all the tests of a software.
- Each test is now a function of a class which is derived from the class `unittest.TestCase`.
- The same tests are implemented using `unittest` in the file `test_operations_unittests.py` as functions of a class `TestOperations`.
- unittest.TestCase offers functions like `assertEqual`, `assertAlmostEqual`, `assertTrue`, etc. for use instead of the usual assertion statements. These statements help the test runner to accumulate all test results and generate a test report.
- `unittest.main()` provides an option to run the tests from a command-line interface.
- 