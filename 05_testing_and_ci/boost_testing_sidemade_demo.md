# Boost.Test and CTest in Action: SideMade Demo

Repository: [testing boost exercise – demo-start branch](https://github.com/Simulation-Software-Engineering/testing-boost-exercise/tree/demo-start)

## 1. Get to Know the Code

- Go through all sections of `README.md`
- Try: build and run
    - Explain shell output
    - Try different matrices and algorithms
- Look into the code
    - `main.cpp`
    - `Configuration.hpp/cpp`
    - `matrixIO.hpp/cpp`
    - `MatrixSolver.hpp/cpp`
- Look into `CMakeLists.txt`
- Our mission:
    - The code has no unit tests yet. -> We add some of them with Boost UTF.
    - Exercise: continue with same code, add more tests, set up GitHub Actions, and more
    - We combine and consolidate knowledge on CMake, Boost UTF, and GitHub Actions.

## 2. First Dummy Test Case

- `mkdir tests`, create `tests/MatrixSolverTest.cpp`
- `#define BOOST_TEST_MODULE SideMadeTests`
    - Needs to be in (exactly) one of our test files. We will write multiple files with tests (one file for each class/feature to be tested) so we have to make sure that this only appears in one file.
- `#define BOOST_TEST_DYN_LINK`
    - needed if UTF used as a shared (aka dynamic) library
    - in header-only mode, you cannot split tests over multiple files
    - needed in *every* of our files containing tests
- `#include <boost/test/unit_test.hpp>`
    - different header/path than for header-only usage
- Add first test:

    ```cpp
    BOOST_AUTO_TEST_CASE(LU)
    {
      BOOST_TEST(true);
    }
    ```

- Adjust `CMakeLists.txt`:

    ```cmake
    include(CTest)
    find_package(Boost 1.71 REQUIRED unit_test_framework)
    file(GLOB_RECURSE TEST_FILES CONFIGURE_DEPENDS tests/*.cpp)
    add_executable(testsidemade "${TEST_FILES}")
    target_link_libraries(testsidemade PRIVATE Boost::unit_test_framework)
    add_test(NAME "MatrixSolverTests" COMMAND ${CMAKE_CURRENT_BINARY_DIR}/testsidemade)
    ```

- Reconfigure CMake, build, run via ...
    - `./testsidemade`
    - `./testsidemade --list_content`
    - `./testsidemade --report_level=detailed`
    - `make test`
    - `ctest`
- If we leave out the last line (`add_test(...)`), the test can be run via `testsidemade`, but not via `make test` or `ctest` since CMake does not know about the test.

## 3. Use Actual Implementation in Matrix Solver Test

- Give a known matrix `A` and right hand side `b` to the MatrixSolver and compare it to the expected result. Do this test for all available decompositions (LU, QR, LU2).
- Needs more includes:

    ```cpp
    #include <Eigen/Dense>
    #include "MatrixSolver.hpp"

    using namespace Eigen;
    ```

- Create data:
    - Show how to manufacture a testcase (a common scheme in numerics)
    - First choose A, then solution x. Compute right hand side b accordingly.

    ```cpp
    MatrixXd A(3, 3);
    A << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    VectorXd expectedX(3);
    expectedX << 2, 0, 0.5;

    VectorXd b(3);
    b << 3.5, 11, 18.5;
    ```

- Add testing code:

    ```cpp
    MatrixSolver solver(MatrixSolver::LU);
    VectorXd     x(3);
    solver.solve(A, b, x);
    BOOST_TEST(x == expectedX);
    ```

- Adjust `CMakeLists.txt`
    - Add `"${SRC_FILES}"` to test executable
    - Make headers visible `target_include_directories(testsidemade PRIVATE ${PROJECT_SOURCE_DIR}/src)`
    - link `Eigen3::Eigen` and also `yaml-cpp` (since used in `SRC_FILES`)

    ```cmake
    add_executable(testsidemade "${TEST_FILES}" "${SRC_FILES}")
    target_include_directories(testsidemade PRIVATE ${PROJECT_SOURCE_DIR}/src)
    target_link_libraries(testsidemade PRIVATE Boost::unit_test_framework Eigen3::Eigen yaml-cpp)
    ```

- Build ... problem that two "main" functions are defined
    - Fix by:

    ```cmake
    file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS src/*.cpp)
    list(REMOVE_ITEM SRC_FILES "${PROJECT_SOURCE_DIR}/src/main.cpp")

    add_executable("${PROJECT_NAME}" "${SRC_FILES}" src/main.cpp)
    ```

- Build and run tests

## 4. Organize Matrix Solver Tests

- Use a fixture to provide data; just copy "create data" code there

    ```cpp
    struct MatrixSolverFixture {
      MatrixSolverFixture()
      {
        A = MatrixXd(3, 3);
        A << 1, 2, 3,
            4, 5, 6,
            7, 8, 9;

        b = VectorXd(3);
        b << 3.5, 11, 18.5;

        expectedX = VectorXd(3);
        expectedX << 2, 0, 0.5;
      }

      MatrixXd A;
      VectorXd b;
      VectorXd expectedX;
    };
    ```

- Add fixture to test and use: `BOOST_FIXTURE_TEST_CASE(LU, MatrixSolverFixture)`
- Build and run

- Add suite to group test cases and add fixture there:

    ```cpp
    BOOST_FIXTURE_TEST_SUITE(MatrixSolverTests, MatrixSolverFixture)
    ...
    BOOST_AUTO_TEST_SUITE_END()
    ```

    - We can change back `BOOST_FIXTURE_TEST_CASE(LU, MatrixSolverFixture)` to `BOOST_AUTO_TEST_CASE(LU)`

- Build and run
- `./testsidemade --list_content`
- Add tests for `QR` and `LU2` by copying the one for `LU`
- `make test` -> fail, but which one?
- `./testsidemade` -> line number tells us that QR test fails, but why?
- Other ways to get more output: `ctest --output-on-failure` or `ctest --verbose`
- Replace with explicit calls to entries to further investigate problem

    ```cpp
    BOOST_TEST(x(0) == expectedX(0));
    BOOST_TEST(x(1) == expectedX(1));
    BOOST_TEST(x(2) == expectedX(2));
    ```

- Seems that for floating point values, we need a tolerance. Use decorator, directly add to suite:

    ```cpp
    BOOST_FIXTURE_TEST_SUITE(MatrixSolverTests, MatrixSolverFixture, *boost::unit_test::tolerance(1e-12))
    ```

- Better change all comparisons to explicit calls to entries. Or overwrite Eigen implementation.
- Of course, we could now add much more testcases to `MatrixSolverTests` (different sizes of matrices, failing solve, ...), but this is already good.
- We could also further reduce code duplication by defining a function.

## 5. Test Case for Configuration

- Test should load a known configuration and compare it to the expected values.
- Create `ConfigurationTest.cpp`
- Add includes (no `BOOST_TEST_MODULE` here)

    ```cpp
    #define BOOST_TEST_DYN_LINK
    #include <boost/test/unit_test.hpp>
    #include "Configuration.hpp"
    #include "MatrixSolver.hpp"
    ```

- Add suite and test case

    ```cpp
    BOOST_AUTO_TEST_SUITE(ConfigurationTests)
    BOOST_AUTO_TEST_CASE(ReadConfiguration)
    {}

    BOOST_AUTO_TEST_SUITE_END()
    ```

- `cp ../data/config.yml testconfig.yml` and explain what test should do TODO
- Add expected data:

    ```cpp
    const MatrixSolver::DecompositionType expectedDecompositionType{MatrixSolver::QR};
    const std::string                     expectedMatrixFileName{"../data/m3.csv"};
    const int                             expectedMatrixSize{3};
    ```

- Configure and test:

    ```cpp
    Configuration configuration{"testconfig.yml"};
    BOOST_TEST(configuration.matrixFileName == expectedMatrixFileName);
    BOOST_TEST(configuration.decompositionType == expectedDecompositionType);
    BOOST_TEST(configuration.matrixSize == expectedMatrixSize);
    ```

- Adjust `CMakeLists.txt`:
    - In principle OK like it is, but we could organize things a bit better.
    - Add tests and [filter](https://www.boost.org/doc/libs/1_78_0/libs/test/doc/html/boost_test/runtime_config/test_unit_filtering.html):

    ```cmake
    add_test(NAME "MatrixSolverTests" COMMAND ${CMAKE_CURRENT_BINARY_DIR}/testsidemade --run_test=MatrixSolverTests/*)
    add_test(NAME "ConfigurationTests" COMMAND ${CMAKE_CURRENT_BINARY_DIR}/testsidemade --run_test=ConfigurationTests/*)
    ```

    - We match by name here. We could also request explicit tests that are part of a suite such as `--run_test=MatrixSolverTests/LU`. We could also use labels `run_test=@LLABELNAME`. `@L` is tells the test tool to look for specific labels. We can also use the `*` wildcard to run tests with certain prefixes or suffixes.

- Build, run -> does not find config file
    - We could run it from the `tests` folder, but this cannot be the solution: `cd ../tests && ../build/testsidemade`
    - Add working directory to test:

    ```cmake
    add_test(NAME "ConfigurationTests" COMMAND ... WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/tests)
    ```
