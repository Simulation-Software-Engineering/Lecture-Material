---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
    font-weight: bold;
    color: orange;
  }
  .reveal p {
    text-align: left;
  }
  .reveal section h1 {
    color: orange;
  }
  .reveal section h2 {
    color: orange;
  }
</style>

# Testing a Python Code

---

## pytest

- Library to write and manage tests.
- Command-line tool also called `pytest`.
- Install using pip: `pip install -U pytest`.
- All tests need to be in files named `test_*.py`.
- Each test function needs to be named as `test_*`.
- pytest gives a detailed description of assertion checks.

---

## pytest Demo

---

## unittest

- Python framework specifically designed to run, monitor and automate unit tests.
- Many features like test automation, sharing of setup and shutdown of tests, etc.
- Use the base class `unittest.TestCase` to create a test suite.
- Command-line interface: `python -m unittest test_module1 test_module2 ...`.

---

## unittest Demo

---

## coverage

- Python library to check code coverage. Installation: `pip install coverage`.
- Testing frameworks can be run via coverage to generate code coverage data while tests run.
- Code coverage information can be viewed on the terminal using: `coverage report -m`.

---

## coverage Demo

---

## tox

- Environment orchestrator to setup and execute various tools for a project.
- Creates virtual environments for each process.
- Processes include testing, linting, building, documentation generation, and more.
- Configuration via `tox.toml` or `tox.ini` file.

---

## tox Demo

---

## Other Testing Frameworks

- [nose](https://pypi.org/project/nose2/) is an extension to `unittest` with added plugins.
- [testify](https://pypi.org/project/testify/) based on unittest and nose with additional features.
- [robotframework](https://pypi.org/project/robotframework/) is a generic automation framework.

---

## Further Reading

- [pytest documentation](https://docs.pytest.org/en/6.2.x/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [tox user guide](https://tox.wiki/en/4.23.2/user_guide.html#user-guide)
