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
  .reveal code {
    font-family: 'Ubuntu Mono';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# Introduction to Boost.Test

---

## Learning Goals of Complete Lecture

- How to use `Boost.Test` to write simple tests for C++ toy codes.
- What general concepts of test frameworks such as fixtures or decorators are.
- How tests can be called from CMake via CTest.
- How unit and integration tests look like for preCICE as an example of a real simulation software.
- How `Boost.Test`, CMake, and GitHub Actions work together for preCICE as an example of a real simulation software.

---

## Boost Unit Test Framework

- Part of Boost (we have already seen other Boost libraries: `filesystem`, `container`)
- Powerful unit test framework
- Sometimes called (the) **Unit Test Framework** (UTF) or **Boost.Test**
    - Valid on all slides: `namespace utf = boost::unit_test;`
- [List of contributors and maintainers](https://www.boost.org/doc/libs/1_81_0/libs/test/doc/html/boost_test/acknowledgements.html)

---

## Other Testing Frameworks for C++ Codes

We study **Boost.Test** as an example.
If you know one, the next one is easy to learn.

- [Catch2](https://github.com/catchorg/Catch2)
- [CppUnit](http://sourceforge.net/apps/mediawiki/cppunit/index.php?title=Main_Page)
- [Cute](http://www.cute-test.com/)
- [GoogleTest](http://code.google.com/p/googletest/)
- [More](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C.2B.2B)

---

## Hello World Demo

See demo notes

---

## Test Suites

- Organize tests as a tree
    - Master test suite is root (handled internally, name specified with `BOOST_TEST_MODULE`)
    - Test suites are internal nodes of the tree
    - Test cases are the leaves

```cpp
#define BOOST_TEST_MODULE Master Suite Name
#include <boost/test/included/unit_test.hpp>

BOOST_AUTO_TEST_SUITE(Suite1)
    BOOST_AUTO_TEST_CASE(Test1) {...}
    BOOST_AUTO_TEST_CASE(Test2) {...}
BOOST_AUTO_TEST_SUITE_END()

BOOST_AUTO_TEST_SUITE(Suite2)
    BOOST_AUTO_TEST_CASE(Test3) {...}
BOOST_AUTO_TEST_SUITE_END()
```

- Can also be spread over multiple files (same suite name -> added to same suite)

---

## Decorators (1/2)

- Label decorator for filtering

    ```cpp
    BOOST_AUTO_TEST_CASE(Test1, * utf::label("trivial")) {...}
    ```

- Example from preCICE: filter out tests for MPI ports functionality if built with specific MPI version
- List all labels with `--list_labels` option
- Decorators can also be added to suites

    ```cpp
    BOOST_AUTO_TEST_SUITE(Suite1, * utf::label("trivial")) {...}
    ```

- Multiple decorators can be combined: `* utf::dec1() * utf::dec2()`

---

## Decorators (2/2)

- Disable decorator

    ```cpp
    BOOST_AUTO_TEST_CASE(Test1, * utf::disabled()) {...}
    ```

- Why is disabling a test better than commenting it out?

<div>
    <!-- .element: class="fragment" data-fragment-index="1" -->

- Keep checking whether it builds (imagine somebody else refactors something you use in the test)
- UTF still knows the test exists (option `--list_content`)

</div>

---

## Fixtures (1/2)

- Set up and tear down test data
- Fulfill preconditions
- Do clean-up work
    - Example from preCICE: static geometry ID seed

```cpp
struct MyFixture {
  MyFixture() : i(0) {}
  ~MyFixture() {}

  int i;
};

BOOST_FIXTURE_TEST_CASE(Test1, MyFixture)
{
  BOOST_TEST(i == 0);
}
```

---

## Fixtures (2/2)

- Use `BOOST_FIXTURE_TEST_CASE` instead of `BOOST_AUTO_TEST_CASE`
- Fixture can be added to multiple tests -> always new instance
- Multiple fixture can be added as decorators
    - `* utf::fixture<MyFixture>()`
    - (behaves strange in many regards, cannot recommend)
- Fixture can be added to complete suite:

    ```cpp
    BOOST_FIXTURE_TEST_SUITE(Suite1, MyFixture);
    ```

Which behavior do you then expect and why?

<div>
    <!-- .element: class="fragment" data-fragment-index="1" -->

- Just like adding fixture to every test -> always new instance
- Tests should not depend on each other

</div>

---

## Further Reading

- [Documentation of Boost Unit Test Framework](https://www.boost.org/doc/libs/1_78_0/libs/test/doc/html/index.html)
