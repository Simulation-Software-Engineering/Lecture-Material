# Introduction to Boost.Test – Hello World Demo

Code is in `05_testing_and_ci/examples/boost_test`

- Explain code
    - Uses UTF in header-only mode (can also be used as library, more later)
    - Give name to `BOOST_TEST_MODULE`
    - UTF defines `main` function for us (could also be done manually)
    - Single test case, which is added automatically with `AUTO` (could also be done manually)
- Build: `g++ -o test helloWorldTest.cpp`
- Run: `./test`
- Inspect: `./test --help` and `./test --list_content` (`*` means that a testcase is active)
