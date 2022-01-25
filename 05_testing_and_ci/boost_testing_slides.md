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

# Boost.Test and CTest for Testing C++ Codes

---

## Learning Goals

- How to use `Boost.Test` to write simple tests for C++ toy codes.
- What general concepts of test frameworks such as fixtures or decorators are.
- How tests can be called from CMake via CTest.
- How unit and integration tests look like for preCICE as an example of a real simulation software.
- How `Boost.Test`, CMake, and GitHub Actions work together for preCICE as an example of a real simulation software.

---

## Boost Unit Test Framework

TODO

will use `namespace utf = boost::unit_test;`

`Unit Test Framework` = `Boost.Test`

---

## Other Testing Frameworks for C++ Codes

We study **Boost.Test** as an example. If you know one, the next one is easy to learn.

- [Catch2](https://github.com/catchorg/Catch2)
- [CppUnit](http://sourceforge.net/apps/mediawiki/cppunit/index.php?title=Main_Page)
- [Cute](http://www.cute-test.com/)
- [Google Test](http://code.google.com/p/googletest/)
- [More](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C.2B.2B)

---

## Hello World Demo

---

## Test Suites

- Organize tests as a tree
  - Master test suite is root
    - Handled internally
    - Name specified with `BOOST_TEST_MODULE`
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

- Can also be spread over multiple files
  - Same suite name -> added to same suite
  
---

## Decorators (1/2)

- Label decorator for filtering 

```cpp
BOOST_AUTO_TEST_CASE(Test1, * utf::label("trivial")) {...}
```

- Example from preCICE: to filter out tests testing MPI ports functionality if built with specific MPI version (no longer done this way)
- List all labels with `--list_labels` option
- Decorators can also be added to suites

```cpp
BOOST_AUTO_TEST_SUITE(Suite1, * utf::label("trivial")) {...}
```

---

## Decorators (2/2)

<!-- .element: class="fragment" data-fragment-index="1" -->

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

## Fixture

TODO

--- 

## SideMade Demo




## Further reading

- TODO















































