# Demo: Automation with GitHub Actions and GitLab CI

## To remove: Contents to cover

### Automation

- General terms
    - What is CI? What is CD? Where is it used?
    - Common terms: Runner, event, workflow etc.
    - Configuration examples


## What to automatize?

- Checking of code (use `black` style checker)
- Building (Just print some statement)
- Testing (running pytest)
- Coverage report (Run coverage after the test have been run)

## Preliminary step

- Set up a Docker container that contains
    - `python`, this should include `unittest`
    - `pip` to install packages:
        - `black`
    - **Note**: We will use the `coverage` package later, but we will *not* install it here. The package will be our example to show that we can install extra software within the CI.
- Checkout `Dockerfile` in `examples/automation` directory
    - Image is build on top of [alpine Linux](https://www.alpinelinux.org). Alpine is optimized to produce tiny build to be used in containers.
    - We fix the version of the base image to make sure to not run into compatibility problems.
    - We need to install Python etc. ourselves:
        - `python3`, `pip` and Python libraries/packages (`black`, `coverage`)
        - `pip` should be installed and used from a non-root user. Therefore, we create a user called `testuser` and change to this user

- Build the image locally and tag it according to my DockerHub accountname (`ajaust`)

  ```bash
  sudo docker build -t ajaust/automation-lecture .
  ```

- Checkout the image list `sudo docker image list` to point out that the container is reasonably small. During the preparation it was about 72 MB large.
- Push image to DockerHub such that we can use it in CI pipelines

  ```bash
  sudo docker push ajaust/automation-lecture
  ```

## GitHub Actions

### Components of Actions

- Workflow:
- Event:
- Jobs:
- Action:
- Runner:

## GitLab CI

### GitLab Runner

#### Installation

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

#### Registration

Information needed:
- GitLab instance URL
- There exist different executors
    - We use `docker` executor
- Find **registration token of repository**

  ```text
  GitLab repository -> Settings -> CI/CD -> Runners ->  Specific runners
  ```

  - Registration process in detail

    ```text
    docker run --rm -it -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register
    Runtime platform                                    arch=amd64 os=linux pid=7 revision=5316d4ac version=14.6.0
    Running in system-mode.

    Enter the GitLab instance URL (for example, https://gitlab.com/):
    URL, e.g.https://gitlab-sim.informatik.uni-stuttgart.de
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
