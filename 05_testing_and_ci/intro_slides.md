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

## Learning goals of the chapter

- Learn the importance of test simulation software
- Discern the concepts of unit testing, integration testing and regression testing with the perspective of simulation software
- Getting familiar with the Python testing frameworks `pytest` and `unittest`

---

## What is testing?

- Smelling old milk before using it!
- A way to determine if a software is not producing reliable results and if so, what is the reason.
- Manual testing vs. Automated testing.

---

## Why should you test your software?

- Improve software reliability and reproducibility.
- Make sure that changes (bugfixes, new features) do not affect other parts of software.
- Generally all software is better off being tested regularly. Possible exceptions are very small codes with single users.
- Ensure that a released version of a software actually works.

---

## Nomenclature in software testing

- **Fixture**: preparatory set for testing.
- **Actual result**: what the code produces when given the fixture.
- **Expected result**: what the actual result is compared to.
- **Test coverage**: how much of the code do tests touch in one run.

---

## Some ways to test software

- Assertions
- Unit testing
- Integration testing
- Regression testing

---

## Assertions

- Principle of *defensive programming*.
- Nothing happens when an assertion is true; throws error when false.
- Types of assertion statements:
    - Precondition
    - Postcondition
    - Invariant
- A basic but powerful tool to test a software on-the-go.
- Assertion statement syntax in Python

```python
assert condition, "message"
```

---

## Unit testing

- Catching errors with assertions is good but preventing them is better!
- A *unit* is a single function in one situation.
    - A situation is one amongst many possible variations of input parameters.
- User creates the expected result manually.
- Fixture is the set of inputs used to generate an actual result.
- Actual result is compared to the expected result, for e.g. using an assertion statement.

---

## Integration testing

- Test whether several units work in conjunction.
- *Integrate* units and test them together in an *integration* test.
- Often more complicated than a unit test and has more test coverage.
- A fixture is used to generate an actual result.
- Actual result is compared to the expected result, for e.g. using an assertion statement.

---

## Regression testing

- Generating an expected result is not possible in some situations.
- Compare the current actual result with a previous actual result.
- No guarantee that the current actual result is correct.
- Risk of a bug being carried over indefinitely.
- Main purpose is to identify changes in the current state of the code with respect to a past state.

---

## Test Coverage

- Coverage is the amount of code a test touches in one run.
- Aim for high test coverage.
- There is a trade-off: high test coverage vs. effort in test development

---

## Comparing floating-point variables

- Very often quantities in simulation software are `float` / `double`.
- Such quantities cannot be compared to exact values, an approximation is necessary.
- Comparison of floating point variables needs to be done to a certain tolerance.
- In `pytest` there is `pytest.approx(value, abs=tol)`.
- In `unittest` there is `assertAlmostEqual()`.

---

## Test-driven development (TDD)

- Principle is to write a test and then write a code to fulfill the test.
- Advantages:
    - In the end user ends up with a test alongside the code.
    - Eliminates confirmation bias of the user.
    - Writing tests gives clarity on what the code is supposed to do.
- Disadvantage: known to not improve productivity.

---

## Checking-driven development (CDD)

- Developer performs spot checks; sanity checks at intermediate stages
- Simulation software often has heuristics which are easy to determine.
- Keep performing same checks at different stages of development to ensure the code works.

---

## Verifying a test

- Test written as part of a bug-fix:
    - Reproduce the bug in the test by ensuring that the test fails.
    - Fix the bug.
    - Rerun the test to ensure that it passes.
- Test written to increase code coverage:
    - Make sure that the first iteration of the test passes.
    - Try introducing a small fixable bug in the code to verify if the test fails.

---

## Further reading

- [Research Software Engineering with Python - Chapter 11: Testing Software](https://merely-useful.tech/py-rse/testing.html)
