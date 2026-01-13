# Notes for Demos of Python Testing Frameworks

Example code is in [05_testing_and_ci/examples/python_testing](examples/python_testing/).

## Software Code Used

The file [operations.py](examples/python_testing/operations.py) consists of a class `MathOperations` that has the following functions: `reorder_data`, `find_max`, `find_median`, and `find_mean`. The `main()` routine in the file applies the functions to a list and prints the output.

## pytest

- pytest is installed using pip: `pip install pytest`.
- All tests can be run using the command-line tool called `pytest`. Just type `pytest` in the working directory and hit ENTER.
- If pytest is installed in some other way, you might need to run it like `python -m pytest`.
- Tests are written in the file `test_operations.py`. The `test_*` prefix in the name is required so that pytest detects the file as a testing file. Suffix form `*_test.py` also works.
- There are unit tests for the functions `reorder_data`, `find_max`, and `find_mean`.
- There is an integration test for the function `find_median`, and a regression test for `reorder_data`. The regression test reads in a list from a CSV file.
- The test fixture is defined under `@pytest.fixture`. pytest runs this once at the start and stores the returned output while running all other tests.
- One test fails. Error message states that the failure occurs because floating-point variable comparison is not handled correctly.
- While comparing two floating-point variables the value needs to be correct only up to a certain tolerance limit. To do this, the expected mean value needs to be changed in the following way:

```python
# Expected result
expected_mean = pytest.approx(69.57, rel=1e-2)
```

- Even if one test fails, pytest runs the rest and gives a report on the failing test.
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
- **Note**: revert to the old directory structure before proceeding to the next section.

## unittest

- Base class `unittest.TestCase` is used to create a test suite.
- Each test is now a function of a class which is derived from the class `unittest.TestCase`.
- The same tests as for `pytest` are implemented using `unittest` in the file `test_operations_unittests.py`. The tests are functions of a class named `TestOperations` which tests our mathematical operations. The class `TestOperations` is derived from `unittest.TestCase`.
- unittest discovers tests based on identifiers. A [test discovery](https://docs.python.org/3/library/unittest.html#test-discovery) mechanism is followed.
- unittest can be run as a Python module: `python -m unittest`.
- unittest.TestCase offers functions like `assertEqual`, `assertAlmostEqual`, `assertTrue`, and more ([see unittest.TestCase documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase)) for use instead of the usual assertion statements. These statements ensure that test runner to accumulate all test results and generate a test report.
- `unittest.main()` provides an option to run the tests from a command-line interface and also from a file.
- `setUp` function is executed before all the tests. Similar a clean up function `tearDown` exists.
- The intention is to group together sets of similar tests in an instant of `unittest.TestCase` and have multiple such instances.
- A unit test for the function `find_median` is written by mocking the function `reorder_data` using [MagicMock](https://docs.python.org/3/library/unittest.mock.html#magic-mock) from unittest. The function `reorder_data` is mocked so that the function `find_median` can be tested in isolation.
- Decorators such as `@unittest.skip`, `@unittest.skipIf`, `@unittest.expectedFailure` can be used to gain flexibility over working of tests.

## coverage

- Install coverage using pip: `pip install coverage`.
- Testing frameworks can be run via coverage. Run pytest via coverage:

```bash
coverage run -m pytest
```

- The `-m` flag tells coverage to run `pytest` module and measure test coverage. This flag would not exist if a Python file was directly being run.
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

## tox

- Environment orchestrator to setup and execute various tools for a project.
- `tox` creates virtual environments to run each tools in.
- `tox.toml` file consists of two environments, one to run pytest and one to run unittest.
- Global settings defined under section at the top of the `tox.toml` file.
- Start tox by running the command `tox` in the directory where the `tox.toml` exists.
- First execution of tox is slow because it creates the necessary virtual environments. Virtual environment setups are in the `.tox` repository.
