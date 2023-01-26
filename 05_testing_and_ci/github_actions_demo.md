# Demo: Automation with GitHub Actions

## 1. Setting up a Test Job

- Clone [automation lecture repository](https://github.com/Simulation-Software-Engineering/automation-lecture-wt2223) and run code and tests
- Set up workflow file

  ```bash
  mkdir -p .github/workflows
  cd .github/workflows
  vi testing.yml
  ```

- In the first go, we only want to run the `unittest` tests.
- Edit `testing.yml` to have following content

  ```yaml
  name: Testing workflow

  on: [push, pull_request]

  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
          with:
            python-version: '3.8'
        - name: "Run unittest"
          run: python -m unittest
  ```

- `runs-on` does **not** refer to a Docker container, but to a runner tag.
- This specific Python version as it is the current version on my laptop (and let's say I want to reproduce this environment)
- Add, commit, push
- After the push, inspect "Action" panel on GitHub repository
    - GitHub will schedule a run (yellow dot)
    - Hooray. We have set up our first action.
- Failing test example:
    - Edit settings on GitHub that one can only merge if all tests pass:
        - Settings -> Branches -> Branch protection rule
        - Choose `main` branch
        - Enable "Require status checks to pass before merging". Optionally enable "Require branches to be up to date before merging"
        - Choose status checks that need to pass: `test`
        - Click on "Create" at bottom of page.
    - Create a new branch `break-code`.
    - Edit `operations.py`, break the code, commit it and push it to the branch. Afterwards open a new PR and inspect the failing test. We are also not able to merge the changes as the "Merge" button should be inactive.

## 2. Extend Action to Have Several Dependent Jobs

- Briefly explain what `black` is: a compact, easy-to-use formatting tool.
    - Run `black` locally on repository and explain what it does.

      ```bash
      black --check .
      ```

    - Add an empty line somewhere and run again.
    - Run without `--check` and `git status`.

- Adding additional jobs by editing on GitHub. The workflow should have the following content:

  ```yaml
  name: Testing workflow

  on: [push, pull_request]

  jobs:
    style:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
          with:
            python-version: '3.8'
        - name: "Install style checker"
          run: pip install black
        - name: "Run style check"
          run: black --check .
    build:
      needs: style
      runs-on: ubuntu-latest
      env:
        PROJECT_NAME: "Automation Lecture"
      steps:
        - name: "Run build phase"
          run: echo "Building project $PROJECT_NAME"
    test:
      needs: build
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
          with:
            python-version: '3.8'
        - name: "Run unittest"
          run: python -m unittest
  ```

- We need to run `actions/checkout@v2` in each job
    - We could share the repository between jobs via artifacts, but that is uncommon.
- We need to run `actions/setup-python@v2` since jobs do not share the environment.
- We specify dependencies by `needs` such that the steps run after each other.
- We do not have a real build step since it is Python. However, this might be interesting for compiled code.

## 3. Other Workflows

- Show workflows of [preCICE](https://github.com/precice/precice)
    - Show `Actions` tab
        - `Build and test` job, click on a run
        - Jobs created through test matrix
        - Click on a job, click on a few steps
    - Show `workflows` folder, click on `Build and Test`
    - Only one job. `build`, `test`, ... are modeled as steps

## 4. act Demo

- `act` is for quick checks while developing workflows, not for developing the code
- Check available jobs

  ```bash
  act -l
  ```

- Run jobs for `push` event (default event)

  ```bash
  act
  ```

- Run a specific job

  ```bash
  act -j test
  ```
