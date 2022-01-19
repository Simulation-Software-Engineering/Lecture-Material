---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
    font-weight: bold;
    color: orange;
  }
  .reveal p {
    text-align: left;
  }
  .reveal section h1 {
    color: orange;
  }
  .reveal section h2 {
    color: orange;
  }
  .reveal code {
    font-family: 'Ubuntu Mono';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# GitHub Actions and GitLab CI/CD

---

## Learning Goals

- Know about two common CI/CD solutions
- Know how to set up typical automation workflows
- Know about the differences similarities between GitHub Actions and GitLab CI/CD

---

## Goal in this lecture

- Set up simple CI pipeline using GitHub and GitLab
- Pipeline has three steps

    1. Check formatting
    2. Build application
    3. Test application

---

## GitHub Actions

> Automate, customize, and execute your software development workflows right in your repository with GitHub Actions.
> [From: https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

## General information (GitHub Actions)

- Usage is [limited](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#usage-limits) for GitHub's runners
- Available for public repositories or accounts with subscription
- By default Actions run on GitHub's runners
    - Linux, Windows or MacOS

---

## Components (1/2)

- [Workflow](https://docs.github.com/en/actions/using-workflows): Runs one or more jobs
- [Event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows): Triggers a workflow
- [Jobs](https://docs.github.com/en/actions/using-jobs): Set of steps of a workflow (same runner).
    - Steps executed consecutively and share data
    - Jobs by default executed in parallel
- [Action](https://docs.github.com/en/actions/creating-actions): Application performing common, complex task
- [Runner](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#runners): Server that runs jobs
- [Artifacts](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions#sharing-data-between-jobs): Files to be shared between jobs or to be kept after workflow finishes

---

## Components (2/2)

<img src="https://docs.github.com/assets/cb-25628/images/help/images/overview-actions-simple.png" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">


From [GitHub Actions tutorial](https://docs.github.com/en/actions)

---

## Setting up a workflow (GitHub Actions)

- Workflow file files stored `${REPO_ROOT}/.github/workflows`
- Configured via YAML file
- Keep an eye on changes by contributors

```yaml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

---

## Actions

```yaml
- uses: actions/checkout@v2
- uses: actions/setup-node@v2
  with:
    node-version: '14'
```

- Integrated via `uses` directive
- Additional configuration via `with` (options depend on Action)
- Find action in [marketplace](https://github.com/marketplace?type=actions)
- Write [own action](https://docs.github.com/en/actions/creating-actions)

---

## (Environment) Variables (GitHub Actions)

```yaml
jobs:
  weekday_job:
    runs-on: ubuntu-latest
    env:
      DAY_OF_WEEK: Mon
    steps:
      - name: "Hello world when it's Monday"
        if: ${{ env.DAY_OF_WEEK == 'Mon' }}
        run: echo "Hello $FIRST_NAME $middle_name $Last_Name, today is Monday!"
        env:
          FIRST_NAME: Mona
          middle_name: The
          Last_Name: Octocat
```

---

## User-specified commands (GitHub Actions)

```yaml
- name: Single line command
  run: echo "Single line command"
- name: Multi line command
  run: |
    echo "First line"
    echo "Second line. Directory ${PWD}"
  workdir: tmp/
  shell: bash
```

---

## Workflow triggers (GitHub Actions)

- Single or multiple events

  ```yaml
  on: [push, fork]
  ```

- Activities

  ```yaml
  on:
    issue:
      types:
        - opened
        - labeled
  ```

- Filters

  ```yaml
  on:
    push:
      branches:
        - main
        - 'releases/**'
  ```

---

## Expressions (GitHub Actions)

```yaml
steps:
  - uses: actions/hello-world-javascript-action@v1.1
    if: ${{ <expression> }}
    env:
      MY_ENV_VAR: ${{ <another_expression> }}
```

---

## Artifacts (GitHub Actions)

- Data sharing between jobs and data upload
- Uploading artifact

  ```yaml
  - name: 'Upload Artifact'
    uses: actions/upload-artifact@v2
    with:
      name: my-artifact
      path: my_file.txt
      retention-days: 5
  ```

- Downloading artifact

  ```yaml
  - name: Download a single artifact
    uses: actions/download-artifact@v2
    with:
      name: my-artifact
  ```

  **Note**: Drop name to download all artifacts.

---

## Test actions locally

- [act](https://github.com/nektos/act)
- Relies extensively on Docker
    - User should be in `docker` group
- Run `act` from root of the repository

  ```text
  act (runs all workflows)
  act --job WORKFLOWNAME
  ```

- Environment is not 100% identical to GitHub's
    - Workflows may fail locally, but work on GitHub

---

## Demo: GitHub Actions

---

## Advanced topics (GitHub Actions)

- [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)
- [Secrets and tokes](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Continuous deployment](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment)
- [Custom Actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions)
- [Build matrices](https://docs.github.com/en/actions/using-workflows/advanced-workflow-features#using-a-build-matrix)
- Using own Docker containers

---

## GitLab CI/CD

> GitLab CI/CD is a tool for software development using the continuous methodologies:
>
> From [homepage](https://docs.gitlab.com/ee/ci/)

---

## General information (GitLab CI/CD)

- GitLab's integration automation tool
- Powerful runners
- Checks out Git repository by default
- Slightly different meaning of "trigger"
    - GitHub: What triggers an action/workflow
    - GitLab: What should a pipeline trigger

---

## GitLab Runner

- Supports a variety of [executors](https://docs.gitlab.com/runner/executors/)
    - SSH, Shell, Docker...
- Installation is simple
    - Can also run as Docker service
- Allows reuse existing hardware
- On [GitLab.com](https://about.gitlab.com/) preconfigured runners available

---

## Demo: GitLab Runner

- Installation of GitLab Runner
- Registration of a runner to a repository

---

## Components (GitLab CI/CD, 1/2)

- [Pipelines](https://docs.gitlab.com/ee/ci/pipelines/index.html): Collection one or more jobs
- [Jobs](https://docs.gitlab.com/ee/ci/jobs/): Set of steps of a pipeline (same runner).
    - Jobs in one stage my be executed in parallel
- Stages: Group jobs and determine running order
- [Runner](https://docs.gitlab.com/runner/): Server that runs jobs
- [Artifacts](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html): Files to be shared between jobs or to be kept after workflow finishes
- No "Actions", but instead integrated features

---

## Components (GitLab CI/CD, 2/2)

<img src="https://docs.gitlab.com/ee/ci/pipelines/img/manual_pipeline_v14_2.png" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

From [GitLab CI/CD tutorial](https://docs.gitlab.com/ee/ci/pipelines/index.html)

---

## Setting up a workflow (GitLab CI/CD)

- Workflow file files stored `${REPO_ROOT}/.gitlab-ci.yml`
- Configured via YAML file
- Keep an eye on changes by contributors
- Example for a [basic pipeline](https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html#basic-pipelines):

```yaml
stages:
  - build
  - test
  - deploy

image: alpine

build job:
  stage: build
  script:
    - echo "This job builds something."

test job:
  stage: test
  script:
    - echo "This job tests something. It will only run when all jobs in the"

deploy job:
  stage: deploy
  script:
    - echo "This job deploys something. It will only run when all jobs in the"
```

---

## (Environment) Variables (GitLab CI/CD)

- Can be set in [different scopes](https://docs.gitlab.com/ee/ci/variables/)

  ```yaml
  variables:
    TEST_VAR: "All jobs can use this variable's value"

  job1:
    variables:
      TEST_VAR_JOB: "Only job1 can use this variable's value"
    script:
      - echo "$TEST_VAR" and "$TEST_VAR_JOB"
  ```

- There are lots of [predefined variable](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

---

## User-specified commands (GitLab CI/CD)

- Commands are given as a list

  ```yaml
  script:
    - COMMAND1
    - COMMAND2
  ```

- May call functions/scripts of repository
- Normally behaves as typed into a terminal
    - Sometimes wrapping in quotes needed

---

## Expressions (GitLab CI/CD)

- Expression evaluation similar to shell

  ```yaml
  job1:
    variables:
      VAR1: "variable1"
    script:
      - echo "Test variable comparison"
    rules:
      - if: $VAR1 == "variable1"
  ```

---

## Artifacts (GitLab CI/CD)

- Data sharing between jobs and data upload
- Uploading artifact

  ```yaml
  create file:
    script: echo "Content of my file" > my_file.txt
    artifacts:
      paths:
        - my_file.txt
      expire_in: 5 days
  ```

- Downloading artifact

  ```yaml
  read file:
    stage: test
    script: cat my_file.txt
    dependencies:
      - create file
  ```

  **Note**: Drop `dependencies` to download all artifacts. Pass empty list `[]` to not download artifacts.

---

## Workflow "triggers" (GitLab CI/CD)

- By default pipelines are created for every commit
- Filtering by type of events
- Example: Run job only for merge requests

  ```yaml
  job1:
    rules:
      - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
  ```

  or

  ```yaml
  job1:
    only:
      - merge_requests
  ```

- Example: Create pipeline only for merge requests

  ```yaml
  workflow:
    rules:
      - if: $CI_PIPELINE_SOURCE == 'merge_request_event'

  job1:
    script:
      - echo "This job runs in pipelines for merge requests"
  ```

---


## Advanced topics (GitLab CI/CD)

- Complex pipelines, e.g.,
    - [Directed Acyclic Graph](https://docs.gitlab.com/ee/ci/directed_acyclic_graph/)
    - [Multi-project pipelines](https://docs.gitlab.com/ee/ci/pipelines/multi_project_pipelines.html)
    - [Parent-child pipelines](https://docs.gitlab.com/ee/ci/pipelines/parent_child_pipelines.html)
- [Anchors](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)
- [ChatOps](https://docs.gitlab.com/ee/ci/chatops/)
- [Extended testing](https://docs.gitlab.com/ee/ci/unit_test_reports.html)

---

## Summary of GitHub Actions and GitLab CI/CD

- Run tasks automatically for you
- Configuration via YAML files stored in repository
    - Infrastructure as code
- Highly extendable
- Jobs executed on runners (self-hosted or forge-hosted)

---

## Further reading

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart)
- [GitLab CI/CD documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab Runner documentation](https://docs.gitlab.com/runner/)
- [GitLab `gitlab-ci.yml` reference](https://docs.gitlab.com/ee/ci/yaml/)