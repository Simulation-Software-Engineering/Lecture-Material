# Exercise: Git Workflows

## Starting remarks

- [Exercise repository link](https://github.com/Simulation-Software-Engineering/git-exercise).
- Deadline for submitting this exercise is **Thursday 10th November 09:00**.
- This exercise has been originally created by Dennis Gläser @dglaeser.

## Brief idea of the exercise

The exercises should be worked on in groups of two people. Start with forking this repository (each one of you), and decide which of the two forks should act as the "main repository". Note that the exercises build upon each other, so you need, for instance, to complete Exercise 1 before you can continue with Exercise 2. Each exercise is described in the comments at the top of the respective `.py` file. Typically, each one of you will have to make one of the already existing tests pass. The tests in a file can be run with `pytest`, for instance, with `python3 -m pytest FILENAME.py`. To run only the test you are working on, use `python3 -m pytest FILE.py -k TESTNAME`.

## Exercise 1

Distribute the two tasks A and B and work on them in parallel.

- Create a branch for your task, giving it an appropriate name, for example `ex-1-task-A`.
- Commit the solution to your task in a single commit with appropriate name, for example `solution to task A`.
- Push your commit to your fork of the remote repository.
- Open a merge request from the branch you are working on to the main branch of the main repository.
- Together, integrate both tasks via merge requests, while taking care that the final git history is either semi-linear:

```sh
* merge task B
| \
|  * task B
| /
* merge task A
| \
|  * task A
| /
* commit from which you start your work
```

or linear:

```sh
* task B
|
* task A
|
* commit from which you start your work
```

## Exercise 2

Repeat the same procedure as from Exercise 1, but this time using the file `exercise2.py`. This time we want a semi-linear history, which should now continue like this:

```sh
* merge ex2 task B
| \
|  * ex2 task B
| /
* merge ex2 task A
| \
|  * ex2 task A
| /
* last commit of exercise 1
...
```

Again, proper commit messages and branch names should be used.

## Exercise 3

Repeat the procedure from the previous exercises, but this time using the file `exercise3.py`. We again want a semi-linear history, but this time the entire exercise should be done in one merge request:

```sh
* merge ex3
| \
|  * ex3 task B
|  * ex3 task A
| /
* merge ex2 task B (from last exercise)
| \
...
```

Again, proper commit messages and branch names should be used.

## Exercise 4

In this exercise, we want to achieve yet a different layout of the git history:

```sh
* merge ex4
| \
|  * merge ex4 task B
|  | \
|  |  * ex4 task B
|  | /
|  * merge ex4 task A
|  | \
|  |  * ex 4 task A
|  | /
|  * ex 4 task 0
| /
* merge ex3 (from last exercise)
| \
...
```
