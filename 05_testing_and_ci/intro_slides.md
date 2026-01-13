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

# Introduction to Testing

---

## Learning Goals of the Chapter

- Explain the importance of writing tests for simulation software.
- Explain the concepts of unit testing, integration testing and regression testing with the perspective of simulation software.
- Write tests using the Python libraries `pytest` and `unittest`.
- Write tests in C++ using `Boost.Test`.
- Explain the concepts of automation workflows in RSE.
- Write automation workflows using GitHub Actions and GitLab CI.

---

## What is Testing?

- Smelling old milk before using it!
- A method to ensure that a software is producing reliable results.
- Manual testing vs. automated testing.

---

## Why Should you Test your Software?

- Catch errors before software use in the real world.
- Improve software reliability.
- Make sure that changes (bugfixes, features) do not introduce bugs.
- All software is better off being tested regularly. Exceptions could be very small codes with single users.
- Packaged version works as expected.

---

## Nomenclature in Software Testing

- **Fixture**: preparatory definitions for testing.
- **Actual result**: what the software produces with the fixture.
- **Expected result**: ground truth or true result.
- **Test coverage**: how much of the software do tests run through.

---

## Some Ways to Test Software

- Assertions
- Unit tests
- Integration tests
- Regression tests

---

## Assertions

- Principle of *defensive programming*.
- Nothing happens when an assertion is true; throws error when false.
- Types of assertion statements:
    - Precondition: something that must be true at the start.
    - Postcondition: something that is true after execution.
    - Invariant: something that is always true.
- A basic but powerful tool to test a software on-the-go.
- Assertion statement syntax in Python:

```python
assert condition, "message"
```

---

## Unit Tests

- Catching errors with assertions is good but preventing them is better!
- A *unit* is a single function in one situation.
    - A situation is one amongst many possible variations of input parameters.
- Expected result is created manually.
- Actual result is compared to the expected result, for e.g. using an assertion statement.

---

## Integration Tests

- Test whether several units work in conjunction.
- *Integrate* units and test them together in an *integration* test.
- Often more complicated than a unit test and has more test coverage.
- Actual result is compared to the expected result, for e.g. using an assertion statement.

---

## Regression Tests

- Generating an expected result is not always possible.
- Compare the current actual result with a previous actual result.
- No guarantee that the current actual result is correct.
- Does not catch long-existing bugs.
- Compare changes in the current state of the software with respect to a past (reliable) state.

---

## Test Coverage

- Coverage is the amount of software that is run by running the tests.
- Aim for high test coverage.
- Trade-off: extremely high test coverage vs. effort in test development

---

## Comparing Floating-point Variables

- Very often data in simulation software is of type `float` or `double`.
- Such data cannot be compared to exact values, an approximation is necessary.
- Comparing such data up to a certain tolerance.
- In `pytest` there is `pytest.approx(value, abs=tol)`.
- In `unittest` there is `assertAlmostEqual()`.

---

## Test-driven Development (TDD)

- Idea: write a test and then write part of the software to fulfill the test.
- Advantages:
    - Leads to a robust test along with the implementation.
    - Eliminates confirmation bias of the user.
    - Facilitates continuous integration.
    - Reduces need for debugging.
- Disadvantages:
    - False security from tests.
    - Neglect of overall design.

[TDD on Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)

---

## Verifying a Test

- Reproduce the bug in the test by ensuring that the test fails.
- Fix the bug.
- Rerun the test to ensure that it passes.

---

## Further Reading

- [Research Software Engineering with Python - Chapter 11: Testing Software](https://third-bit.com/py-rse/testing.html)
