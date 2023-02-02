# Boost.Test and CTest in Action: SideMade Exercise

In this exercise, you extend and automate the unit tests of the [SideMade code](https://github.com/Simulation-Software-Engineering/testing-boost-exercise), on which we worked during the lecture.

Deadline: **Thursday, February 9rd, 2023, 09:00**

## Preparation and Submission

- Similar to last week, we again need a *copy* of the exercise repository as we cannot easily add automation on forks. Go to GitHub and click on the "+" in the right corner. Choose "import repository". As *old* repository use `https://github.com/Simulation-Software-Engineering/testing-boost-exercise`, use `testing-boost-exercise` as new name, and make the repository public.
- Create a new branch `extend-tests` from `main` and work in this branch.
- To submit, open a PR from `extend-tests` to `main` in your own repository. Then paste a link to this PR in a new issue in the original repository. Use `[GITLAB-USERNAME] Boost test exercise` as title of the issue.

## Task Descriptions

### (1) IO Testing

- Following similar style and structure as in the lecture, implement a simple unit test for the function `matrixIO::openData`.

### (2) Automation

- Similar to last week, add a GitHub Action workflow with three jobs:
    - Style: Check whether all `cpp` and `hpp` files (in `src` and `tests` are formatted correctly using `clang-format` (see `README.md`).
    - Build: Check whether the code builds successfully.
    - Test: Check whether all tests run successfully.
- Add a corresponding [GitHub workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) to the `README.md`.

## Optional Task

- Extend the automation with a [build matrix](https://docs.github.com/en/actions/using-jobs/using-a-build-matrix-for-your-jobs). Test whether your code builds in Debug and in Release mode, and with the gcc and the clang compiler. Make use of CMake variables to modify these parameters.

## Hints and Remarks

- When importing a project on GitHub, it could be that by default actions are disabled. You can enable them via `Settings -> Actions -> General -> Allow all actions`.
- Be careful: the style job should not format the code, but rather report whether the code was formatted correctly or not. There are different ways how to do this. You could use the option `--dry-run`, but then you still need to interpret warnings as errors with `-Werror`. Or you could format inplace (`-i`) and use `git diff`.
- Try to use the build from the build job for the tests in the test job by uploading and downloading the build as an artifact. Problem is that this way file permissions are not preserved. You can work around this problem, by archiving. See [the official workaround](https://github.com/actions/upload-artifact#maintaining-file-permissions-and-case-sensitive-files). Hint: There is also an action `download-artifact`.
