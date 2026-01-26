# Boost.Test in the Real World: preCICE Demo

Look around preCICE in the terminal + text editor.

## First Look

- `cd src && ls`: preCICE is organized in several namespaces.
- `cd math && ls`: Each namespace has a `tests` folder
- Look at `math/tests/DifferenceTest.cpp`
    - Imports `testing/Testing.hpp`, there we handle UTF imports
    - Test suite for `math` namespace and test suite per file (here `math/differences.hpp`)
    - `BOOST_CHECK` actually not recommended to use. Is used internally by `BOOST_TEST`.
    - Powerful macro `PRECICE_TEST()` to setup test context (resources, singletons, not data)

## Unit vs. Integration Tests

- Clear separation in preCICE: integration tests only directly use API of preCICE.
- They are located in `tests` folder.
- Look at `tests/serial/initialize-data/Explicit.cpp`:
    - Explain `PRECICE_TEST_SETUP` and how it is used: test is run on two MPI ranks living in separate MPI communicators.
    - Information can be accessed via `context`.
    - More information: [blog post on bssw.io on multiphysics testing](https://bssw.io/blog_posts/overcoming-complexity-in-testing-multiphysics-coupling-software)

## White-Box Testing

- Not a UTF feature, but an independent C++ trick
- Explain black-box testing:
    - A class has a public API and we only use this API for testing.
    - Makes a lot of sense
- Sometimes, we want white-box testing:
    - Why? Access and/or check private members
    - Could `friend` the test, but this quickly gets out of hand
- Example: class `src/precice/implDataContext.hpp`
    - Has public and protected or private members. We want to check the protected members in tests.
    - Does not `friend` every test, but only `DataContextFixture`
    - `src/testing/DataContextFixture.hpp` has functions to access protected members
    - This fixture is used in many tests in `src/precice/tests/DataContextTest` (but not handed over to test like normal UTF fixtures)

## Test Matrices

- Look at `tests/serial/mapping-nearest-projection/QuadMappingDiagonalNearestProjectionEdgesTallKite.cpp`:
    - Define test matrix with data sets: `boost::unit_test::data::make`

## Boost Test Context

- Look at `src/mapping/tests/NearestProjectionMappingTest.cpp`:
    - `BOOST_TEST_CONTEXT` outputs context information on failure

## CMake

- Look at `cmake/CTestConfig.cmake`: Complicated, but more things tested than only UTF (search for `add_test`)

## CTest in Parallel

- Build preCICE and run tests via `ctest -j 16`, runs tests in parallel, automatic feature of CTest

## Mocking preCICE

- Even more important than for "normal" software, since coupling library needs two software stacks to couple.
- WIP: mock shipped with preCICE, currently there is "only" a prototype in Python bindings
  - Look at [how both environments are distinguished](https://github.com/precice/python-bindings/blob/313441ca296da9bbc694bd99ba930c64b48aa11a/setup.py#L35-L39)
  - Look at files in [`test/`](https://github.com/precice/python-bindings/tree/develop/test)
