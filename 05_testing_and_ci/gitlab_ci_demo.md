# Demo: Automation with GitHub Actions and GitLab CI

## Automation

- Nothing to show

## Preliminary step --- Building a tiny Docker container

Goal: Configure a Docker container useful for our tests. This should show

- why we did introduce Docker before.
- a common use case of Docker.
- Show how to make even tinier containers as before. We use Alpine Linux here.

Steps:

- Skip this if more time is needed
- Plan: Set up a Docker container that contains
    - `python`, this should include `unittest`
    - `pip` to install packages:
        - [`black`](https://github.com/psf/black)
    - **Note**: The `pytest` package is needed later, but we will *not* install it here. The package will be our example to show that we can install extra software within the CI.
- Checkout `Dockerfile` in `examples/automation` directory
    - Image is build on top of [Alpine Linux](https://www.alpinelinux.org). Alpine is optimized to produce tiny build to be used in containers.
    - We fix the version of the base image to make sure to not run into compatibility problems.
    - We need to install Python etc. ourselves:
        - `python3`, `pip` and Python libraries/packages (`black`)
        - `pip` should be installed and used from a non-root user. Therefore, we create a user called `testuser` and change to this user
    - Password-less sudo is enabled for the user in case it would be needed to install other packages.

- Build the image locally and tag it according to my DockerHub account name (`ajaust`)

  ```bash
  sudo docker build -t ajaust/automation-lecture .
  ```

- Checkout the image list `sudo docker image list` to point out that the container is reasonably small. During the preparation it was about 72 MB large/small. This about the size of the size of the pure Ubuntu base container:

  ```text
  ubuntu                          20.04        ba6acccedd29   3 months ago   72.8MB
  ajaust/automation-lecture       latest       a0dec678c941   5 hours ago    71.2MB
  ```

- Push image to Docker Hub such that we can use it in CI pipelines

  ```bash
  sudo docker push ajaust/automation-lecture
  ```

- Now the image can be used as `ajaust/automation-lecture` or `ajaust/automation-lecture:latest`. I did not version the uploaded container.

## GitHub Actions

### 1. Setting up a test job

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
    - `black --check .` will check files without modifying them.
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
        - name: "Install pytest dependency"
          run: pip install --user  pytest
        - name: "Run unittest"
          run: python -m unittest
  ```

- `runs-on` does **not** refer to a Docker container, but to runner tag.
- After the push inspect "Action" panel on GitHub repository
    - GitHub will schedule a run (yellow dot)
    - Hooray. We have set up our first action.
- Edit `test_operations.py`, break a test, commit it and push it to the repository. Check the failing test.

### 2. Extend Action to have several dependent jobs

- Go to tag `github-action-added` or go to `main` branch of the repository. The workflow should have the following content:

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
        - name: "Install pytest dependency"
          run: pip install --user  pytest
        - name: "Run unittest"
          run: python -m unittest
  ```

- We need to run `actions/checkout@v2` in each job
    - We could share the repository between jobs via artifacts, but that is uncommon.
- We need to run `actions/setup-python@v2` since jobs do not share the environment
- We specify dependencies `need` such that the steps run after each other
- We do not have a real build step since it is Python. However, this might be interesting for compiled code.

### SKIP: Using own Docker container in action

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
        - name: "Install pytest dependency"
          run: pip install --user pytest
        - name: "Run unittest"
          run: python -m unittest
  ```

### SKIP: act demo

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

## GitLab CI

### 1. GitLab Runner

#### 1. GitLab Runner Installation

- "Easy" via Docker

  ```bash
  docker run -d --name gitlab-runner --restart always \
           -v /srv/gitlab-runner/config:/etc/gitlab-runner \
           -v /var/run/docker.sock:/var/run/docker.sock \
           gitlab/gitlab-runner:latest
  ```

- Stores configuration on you local machine

  ```bash
   /srv/gitlab-runner/config:/etc/gitlab-runner/config.toml
   ```

- See also [installation instructions](https://docs.gitlab.com/runner/install/)
- And more specific [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)

#### 2. Runner registration

Information needed:

- Create a new repository on GitLab and push the automation repository there. Ideally this is prepared **before** the lecture.
- GitLab instance URL. In our case <https://gitlab-sim.informatik.uni-stuttgart.de>
- There exist different executors
    - We use `docker` executor. This makes it obligatory to specify a default image which can be overwritten in the configuration file of the pipeline.
- Find **registration token of repository**

  ```text
  GitLab repository -> Settings -> CI/CD -> Runners ->  Specific runners
  ```

    - Registration process in detail (terminal output)

        ```text
        docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register
        Runtime platform                                    arch=amd64 os=linux pid=7 revision=5316d4ac version=14.6.0
        Running in system-mode.

        Enter the GitLab instance URL (for example, https://gitlab.com/):
        URL, e.g. https://gitlab-sim.informatik.uni-stuttgart.de
        Enter the registration token:
        TOKEN
        Enter a description for the runner:
        [37d9963c0f15]: Lecture test runner
        Enter tags for the runner (comma-separated):

        Registering runner... succeeded                     runner=sCr8x1WF
        Enter an executor: kubernetes, custom, docker-ssh, virtualbox, docker+machine, docker-ssh+machine, docker, parallels, shell, ssh:
        docker
        Enter the default Docker image (for example, ruby:2.6):
        alpine:latest
        Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
        ```

- Afterwards, verify under `GitLab repository -> Settings -> CI/CD -> Runners ->  Specific runners` that a runner with the specified name shows up.
- Checkout the runner configuration in `/srv/gitlab-runner/config/config.toml` on the host.

  ```bash
  sudo vim /srv/gitlab-runner/config/config.toml
  ```

  should look like

  ```toml
  concurrent = 1
  check_interval = 0

  [session_server]
    session_timeout = 1800

  [[runners]]
    name = "Lecture test runner"
    url = "https://gitlab-sim.informatik.uni-stuttgart.de"
    token = "TOKEN"
    executor = "docker"
    [runners.custom_build_dir]
    [runners.cache]
      [runners.cache.s3]
      [runners.cache.gcs]
      [runners.cache.azure]
    [runners.docker]
      tls_verify = false
      image = "alpine:latest"
      privileged = false
      disable_entrypoint_overwrite = false
      oom_kill_disable = false
      disable_cache = false
      volumes = ["/cache"]
      shm_size = 0
  ```

- Information on [executors and their abilities](https://docs.gitlab.com/runner/executors/)
- More information can be found in the GitLab documentation in section [Registering runners](https://docs.gitlab.com/runner/register/index.html#docker).


### 2. Setting up GitLab CI/CD

- Create/show templates
    - Go to "Repository" -> "+ sign" to add a new file -> New file -> "Select a template type" -> `.gitlab-ci.yml` -> Choose some template. Abort then because we do not want to use any of these templates.
- Checkout tag `gitlab-ci-added` or `main` branch of [repository](https://github.com/Simulation-Software-Engineering/automation-lecture)
- Show our `.gitlab-ci.yml`

  ```yaml
  stages:
  - check
  - build
  - test

  image: ajaust/automation-lecture

  check_code:
  stage: check
  script:
      - echo "This job builds something quickly."
      - black --check .

  build_code:
  stage: build
  variables:
      PROJECT_NAME: "Automation Lecture"
  script:
      - echo "Building project $PROJECT_NAME"

  test_code:
  stage: test
  script:
      - pip install --user  pytest
      - python -m unittest
  ```

- Trigger the pipeline via commit or re-trigger it in GitLab's overview.
- Show different stages and their output.
- Show file in CI/CD editor.
    - GitLab repository -> CI/CD -> Editor
- The students probably know the emails one gets for broken and fixed pipelines.

### 3. CI with explicit dependencies

- On can also explicitly declare dependencies between jobs using the `needs` keyword:

  ```yaml
  stages:
  - check
  - build
  - test

  image: ajaust/automation-lecture

  check_code:
  stage: check
  script:
      - echo "This job builds something quickly."
      - black --check .

  build_code:
  stage: build
  needs: [check_code]
  variables:
      PROJECT_NAME: "Automation Lecture"
  script:
      - echo "Building project $PROJECT_NAME"

  test_code:
  stage: test
  needs: [build_code]
  script:
      - pip install --user  pytest
      - python -m unittest
  ```

- Having dependencies declared allows GitLab to build a graph (DAG) which could allow for more efficient job scheduling.