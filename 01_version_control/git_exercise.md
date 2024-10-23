# Exercise: Git Workflows

Deadline: **Wednesday, October 30, 2024, 9:00**

## Preparation

- Work on the exercises in groups of two. One of you creates a new organization on GitHub (public, free plan) and adds their partner.
- Import the [exercise repository](https://github.com/Simulation-Software-Engineering/git-exercise) and name it `git-exercise` again. Make it public to get access to all features we need. We refer to this repository as the *upstream* repository.
- Add a branch protection rule for the `main` branch of the repository:
    - Require a pull request before merging
    - Require linear history
- Finally, everybody forks the repository into their own namespace.

## Idea of the Exercise

- There are three separate exercises. Each one consists of an individual Python file `exerciseX.py`. The exercises build upon each other, work from one to three. Each exercise is described in the comments at the top of the respective Python file.
- Each exercise has two tasks: A and B. Distribute the two tasks and **work on them in parallel**.
- For each task, create a new branch with an appropriate name (e.g., `ex-1-task-A`) and use appropriate commit messages (not `Solve task A`, but `Fix missing copy in Vector construction` or similar).
- When ready, push the new branch via `git push -u <remote> <branchname>` to your own remote and open a pull request to the `main` branch upstream (i.e. use the feature branch workflow, but with feature branches on forks).
- Assign your partner as reviewer. Review, fix problems, and eventually merge. For the best learning experience, use a different order of steps in every exercise.
- **Goal of the exercises**: Create a linear history with readable commit messages.

## Pytest and Python

- In each task, you typically need to make one of already existing tests pass. We use `pytest` here (you will learn more about `pytest` after Christmas):
    - Install from [PyPI](https://pypi.org/project/pytest/): `pip install --user pytest`.
    - Run all tests of a file with `python3 -m pytest exerciseX.py`.
    - Run a specific test with `python3 -m pytest exerciseX.py -k TESTNAME`.
- Ask if you are stuck with Python issues (quick search on Google often helps as well). This exercise is about Git, not Python.

## Submission

Please open an issue (one per group) in the [exercise repository](https://github.com/Simulation-Software-Engineering/git-exercise) with the title `Submission <gitlab_username1> <gitlab_username2>` and post a link to your upstream repository.

## Credits

These exercises are taken from the [RSE 102 block course](https://github.com/RSE-102), created by [Dennis Gläser](https://github.com/dglaeser).
