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

- Motivation and importance of writing tests for a software
- Understanding the different types of tests and their relevance in testing scientific software
- Becoming familiar with Python testing frameworks `pytest` and `unittest`

---

## Lets start with a survey

- survey link
- slido ID

---

## What is testing?

- Smelling old milk before using it!
- A way to determine if a software is producing reliable results
- Manual testing vs. Automated testing

---

## Why should you test your software?

- Improve software reliability and reproducibility
- Almost all software is better off being tested regularly
- Ensure that a distributed version of a software actually works

---

## Nomenclature in software testing

- **Fixture**: the thing being tested
- **Actual result**: what the code produces when given the fixture
- **Expected result**: what the actual result is compared to
- **Test coverage**: How much of the code does a test touch

---

## Ways to test software

- Assertions
- Unit testing
- Integration testing
- Regression testing

---

## Assertions

- Principle of *defensive programming*
- Python does nothing when an assertion is true; returns error when false.
- Types of assertion statements:
    - Precondition
    - Postcondition
    - Invariant
- A basic but powerful tool to test a software on-the-go.

---

## Unit testing

- Catching errors with assertions is good but preventing them is better!
- A *unit* is a single function in one situation.
- User creates the expected result manually.
- A fixture is used to generate an actual result.
- Assertion statement is used to compare expected result and actual result.

---

## Integration testing

- Test whether several units work in conjunction.
- *Integrate* units and test them together in an *integration* test.
- Often more complicated than a unit test and has more test coverage.
- A fixture is used to generate an actual result.
- Assertion statement is used to compare expected result and actual result.

---

## Regression testing

- Generating an expected result is not possible in some situations
- Compare the current actual result with a previous actual result
- No guarantee that the current actual result is correct
- Risk of a bug being carried over indefinitely
- Main purpose is to identify changes in the current state of the code

---

## Some important points

- Aim for high test coverage
- Comparison of floating point variables needs to be done to a certain tolerance
- Comparing visualizations is often very sensitive, it is better to compare the underlying data instead
- Test-driven development (TDD) vs. Checking-driven development (CDD)
- Validation vs. Verification from the perspective of testing scientific software
- Always make sure that a test breaks when it is supposed to
