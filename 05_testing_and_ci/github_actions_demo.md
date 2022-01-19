# Demo: Automation with GitHub Actions

## 1. Setting up a Test Job

- Go to [repository](https://github.com/Simulation-Software-Engineering/automation-lecture) an check out tag `initial-state`.
- Create a new branch `lecture-branch`
- Set up workflow file

  ```bash
  mkdir -p .github/workflows
  cd .github/workflows
  touch testing.yml
  ```

- Run `black` shortly locally and explain what it does.

  ```bash
  black --check .
  ```

    - It is a style checker that checks whether the Python files are formatted according to a certain standard.
    - `black --check .` will chececify dependencik files without modifying them.
    - `black` uses a lot of smileys

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
            python-version: '3.8.10'
        - name: "Run unittest"
          run: python -m unittest
  ```

- `runs-on` does **not** refer to a Docker container, but to runner tag.
- After the push inspect "Action" panel on GitHub repository
    - GitHub will schedule a run (yellow dot)
    - Hooray. We have set up our first action.
- Failing test example:
    - Edit settings on GitHub that one can only merge if all tests pass:
        - Settings -> Branches -> Branch protection rule
        - Enable "Require status checks to pass before merging". Optionally enable "Require branches to be up to date before merging"
        - Choose status checks that need to pass:
            - `style`, `build`, `test`
        - Click on "Create" at bottom of page.
    - Create a new branch `break-code`.
    - Edit `operations.py`, break a code, commit it and push it to the repository. Check the failing test.

## 2. Extend Action to Have Several Dependent Jobs

- Go to tag `github-action-added` of the repository. The workflow should have the following content:

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
            python-version: '3.8.10'
        - name: "Install style checker"
          run: pip install --user black
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
            python-version: '3.8.10'
        - name: "Run unittest"
          run: python -m unittest
  ```

- We need to run `actions/checkout@v2` in each job
    - We could share the repository between jobs via artifacts, but that is uncommon.
- We need to run `actions/setup-python@v2` since jobs do not share the environment.
- We specify dependencies by `needs` such that the steps run after each other.
- We do not have a real build step since it is Python. However, this might be interesting for compiled code.

## 3. Other Workflows

Show workflows in the lecture repositories.

- [Lecture material](https://github.com/Simulation-Software-Engineering/Lecture-Material)
- [Homepage](https://github.com/Simulation-Software-Engineering/homepage)

## SKIP: Using own Docker Container in Action

Currently the own container does not work due to some privilege issues. When the GitHub Action is checking out the repository into my container it cannot access all files. This is due to the fact that my user is non-root. Even password-less sudo is not enough. The entrypoint of the container has to be root.

References:

- [Permission problems when checking out code as part of GitHub action](https://github.community/t/permission-problems-when-checking-out-code-as-part-of-github-action/202263)

- Now we want to use our own container for the action.
- Create own container from image `examples/automation`

  ```bash
  sudo docker build -t ajaust/automation-lecture .
  sudo docker push ajaust/automation-lecture
  ```

  and the container will be available on Docker Hub.

  **Note**: It is important that one is password-less root in the container

- We edit the workflow file

  ```yaml
  name: Testing workflow

  on: [push, pull_request]

  jobs:
    style:
      runs-on: ubuntu-latest
      container:
        image: ajaust/automation-lecture:latest
      steps:
        - uses: actions/checkout@v2
        - name: "Run style check"
          run: black --check .
    build:
      runs-on: ubuntu-latest
      needs: style
      container:
        image: ajaust/automation-lecture:latest
      env:
        PROJECT_NAME: "Automation Lecture"
      steps:
        - name: "Run build phase"
          run: echo "Building project $PROJECT_NAME"
    test:
      runs-on: ubuntu-latest
      needs: build
      container:
        image: ajaust/automation-lecture:latest
      steps:
        - uses: actions/checkout@v2
        - name: "Run unittest"
          run: python -m unittest
  ```

## SKIP: act Demo

- Currently fails due to different/wrong paths set
- Go into Vagrant Vm
- Checkout [repository](https://github.com/Simulation-Software-Engineering/automation-lecture) if it is not already checked out
- Got into repository root directory
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
