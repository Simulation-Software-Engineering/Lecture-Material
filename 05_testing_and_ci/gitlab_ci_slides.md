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

# GitLab CI/CD

---

## Outline of this Demo/Lecture

- Set up simple CI pipeline using GitLab CI/CD
- Pipeline has three steps

    1. Check formatting
    2. Build application
    3. Test application

- Reuse code of Python testing lecture

---

## What is "GitLab CI/CD"?

> GitLab CI/CD is a tool for software development using the continuous methodologies:

From: [https://docs.gitlab.com/ee/ci/](https://docs.gitlab.com/ee/ci/)

---

## General Information

- GitLab's integration automation tool
- Powerful runners
- Checks out Git repository by default
- Slightly different meaning of word "trigger"
    - GitHub: What triggers an action/workflow
    - GitLab: What should a pipeline trigger and what triggers a pipeline

---

## GitLab Runner

- Supports a variety of [executors](https://docs.gitlab.com/runner/executors/)
    - SSH, Shell, Docker...
- Installation is simple
    - Can also run as Docker service
- Allows reusing existing hardware
- Preconfigured runners available on [gitlab.com](https://about.gitlab.com/)

---

## Demo: GitLab Runner

- Installation of GitLab Runner
- Registration of a runner to a repository

---

## Components (1/2)

- [Pipelines](https://docs.gitlab.com/ee/ci/pipelines/index.html): Collection of one or more jobs
- [Jobs](https://docs.gitlab.com/ee/ci/jobs/): Set of steps of a pipeline (same runner)
    - Jobs in one stage my be executed in parallel
- Stages: Group jobs and determine running order
- [Runner](https://docs.gitlab.com/runner/): Server that runs jobs
- [Artifacts](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html): Files to be shared between jobs or to be kept after workflow finishes
- No "Actions", but instead integrated features

---

## Components (2/2)

<img src="https://docs.gitlab.com/ee/ci/pipelines/img/manual_pipeline_v14_2.png" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

From [GitLab CI/CD tutorial](https://docs.gitlab.com/ee/ci/pipelines/index.html)

---

## Setting up a Workflow/Pipeline

- Workflow file stored in `${REPO_ROOT}/.gitlab-ci.yml`
- Configured via YAML file
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
    - echo "This job tests something. It will only run when all jobs in the build stage are complete."

deploy job:
  stage: deploy
  script:
    - echo "This job deploys something. It will only run when all jobs in the test stage complete."
```

---

## (Environment) Variables

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

- There are lots of [predefined variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

---

## User-specified Commands

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

## Expressions

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

## Artifacts

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

## Workflow "Triggers"

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

## Advanced Topics

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

- [GitLab CI/CD documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab Runner documentation](https://docs.gitlab.com/runner/)
- [GitLab `gitlab-ci.yml` reference](https://docs.gitlab.com/ee/ci/yaml/)

