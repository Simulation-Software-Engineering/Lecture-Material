# Boost.Test and CTest in Action: SideMade Exercise

In this exercise, you extend and automate the unit tests of the [SideMade code](https://github.com/Simulation-Software-Engineering/testing-boost-exercise), on which we worked during the lecture.

Deadline: **Thursday, February 3rd, 2022, 09:00**

## Preparation and Submission

- Similar to last week, we again need a *copy* of the exercise repository as we cannot easily add automation on forks. Go to GitHub and click on the "+" in the right corner. Choose "import repository". As *old* repository use `https://github.com/Simulation-Software-Engineering/testing-boost-exercise`, use `testing-boost-exercise` as new name, and make the repository public.
- Create a new branch `extend-tests` from `main` and work in this branch.
- To submit, open a PR from `extend-tests` to `main` in your own repository. Then paste a link to this PR in a new issue in the original repository. Use `[GITLAB-USERNAME] Boost test exercise` as title of the issue.

## Task Descriptions

### (1) IO Testing

- Following similar style and structure as in the lecture, implement a simple unit test for the function `matrixIO::openData`.

### (2) Automation

- Similar to last week, add a GitHub Action workflow with three jobs:
    - Style: Check whether all `cpp` and `hpp` files are formatted correctly using `clang-format` (see `README.md`).
    - Build: Check whether the code builds successfully.
    - Test: Check whether all tests run successfully.
- Add a corresponding [GitHub workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) to the `README.md`.

### (3) Regression Testing

- Add a workflow for a larger regression test. To this end, generate test data for a 250x250 matrix. The function `matrixIO::saveData` might come handy.

## Optional Task

- Extend the automation with a [build matrix](https://docs.github.com/en/actions/using-jobs/using-a-build-matrix-for-your-jobs). Test whether your code builds in Debug and in Release mode, and with the gcc and the clang compiler. Make use of CMake variables to modify these parameters.
