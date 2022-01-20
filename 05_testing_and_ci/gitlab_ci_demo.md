# Demo: GitLab Runner and GitLab CI/CD

## 1. GitLab Runner

### 1. GitLab Runner Installation

- Installing GitLab Runner via Docker is simple. It can be done via the following command

  ```bash
  docker run -d --name gitlab-runner --restart always \
           -v /srv/gitlab-runner/config:/etc/gitlab-runner \
           -v /var/run/docker.sock:/var/run/docker.sock \
           gitlab/gitlab-runner:latest
  ```

  **Note**: The paths are correct for Linux and might be different for MacOS or Windows. Please checkout the Docker documentation ith is case.

    - `docker run -d --name gitlab-runner --restart always` runs the container in the background (`-d` means detached) names it `gitlab-runner` and makes sure that it always runs. The container is automatically restarted once it stops/crashes. If you want to stop the container, you have to stop it manually (`docker container stop`).
    - `-v /srv/gitlab-runner/config:/etc/gitlab-runner` mounts the directory `/srv/gitlab-runner/config` into the container. Check the directory `/srv/gitlab-runner/config` on the Host to find a GitLab Runner configuration file (`config.toml`).
    - `-v /var/run/docker.sock:/var/run/docker.sock` mounts important Docker files into the container such that the container can start other containers (for pipelines).
    - `gitlab/gitlab-runner:latest` is the GitLab Runner image used from Docker Hub.

- Stores configuration on you local machine

  ```bash
   /srv/gitlab-runner/config:/etc/gitlab-runner/config.toml
   ```

- See also [installation instructions](https://docs.gitlab.com/runner/install/)
- And more specific [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)

### 2. Runner registration

Information needed:

- Go to [automation lecture repository](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/automation-lecture) on our GitLab instance.
- Show that there are currently pipelines with the label "stuck". I have added the repository which contains a valid GitLab CI/CD configuration while there are/were no runners assigned. If the pipelines failed, they are not labeled as "stuck". In this case one can restart the pipeline manually (without any active runner) to get he pipeline back into the "stuck" status.
- GitLab instance URL. In our case <https://gitlab-sim.informatik.uni-stuttgart.de>
- There exist different executors
    - We use `docker` executor. This makes it obligatory to specify a default Docker to use. This image will be used for pipelines that do not specify any Docker image themselves. The image can be overwritten in the configuration file of the pipeline.
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

## 2. Setting up GitLab CI/CD

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
      - python -m unittest
  ```

- Trigger the pipeline via commit or re-trigger it in GitLab's overview.
- Show different stages and their output.
- Show file in CI/CD editor.
    - GitLab repository -> CI/CD -> Editor
- The students probably know the emails one gets for broken and fixed pipelines.

## 3. CI with explicit dependencies

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
      - python -m unittest
  ```

- Having dependencies declared allows GitLab to build a graph (DAG) which could allow for more efficient job scheduling.
    - Show this in the pipeline overview. (CI/CD -> Pipelines -> Choose most recent pipeline run)

## 4. Other Workflows/Pipelines

Show pipelines used in the lecture

- [Challenge repository](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/challenge)