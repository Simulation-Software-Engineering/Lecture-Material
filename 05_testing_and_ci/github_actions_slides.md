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

# GitHub Actions

---

## What is "GitHub Actions"?

> Automate, customize, and execute your software development workflows right in your repository with GitHub Actions.

From: [https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

## General Information

- Usage of GitHub's runners is [limited](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#usage-limits)
- Available for public repositories or accounts with subscription
- By default Actions run on GitHub's runners
    - Linux, Windows or MacOS
- Quickly evolving and significant improvements in recent years

---

## Components (1/2)

- [Workflow](https://docs.github.com/en/actions/using-workflows): Runs one or more jobs
- [Event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows): Triggers a workflow
- [Jobs](https://docs.github.com/en/actions/using-jobs): Set of steps (running on same runner)
    - Steps executed consecutively and share data
    - Jobs by default executed in parallel
- [Action](https://docs.github.com/en/actions/creating-actions): Application performing common, complex task (step) often used in workflows
- [Runner](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#runners): Server that runs jobs
- [Artifacts](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions#sharing-data-between-jobs): Files to be shared between jobs or to be kept after workflow finishes

---

## Components (2/2)

<img src="https://docs.github.com/assets/cb-25628/images/help/images/overview-actions-simple.png" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">


From [GitHub Actions tutorial](https://docs.github.com/en/actions)

---

## Setting up a Workflow

- Workflow file files stored `${REPO_ROOT}/.github/workflows`
- Configured via YAML file

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
- Find actions in [marketplace](https://github.com/marketplace?type=actions)
- Write [own actions](https://docs.github.com/en/actions/creating-actions)

---

## (Environment) Variables

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

## User-specified Commands

```yaml
- name: "Single line command"
  run: echo "Single line command"
- name: "Multi line command"
  run: |
    echo "First line"
    echo "Second line. Directory ${PWD}"
  workdir: tmp/
  shell: bash
```

---

## Events

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

## Expressions

```yaml
steps:
  - uses: actions/hello-world-javascript-action@v1.1
    if: ${{ <expression> }}
    env:
      MY_ENV_VAR: ${{ <another_expression> }}
```

---

## Artifacts

- Data sharing between jobs and data upload
- Uploading artifact

  ```yaml
  - name: "Upload artifact"
    uses: actions/upload-artifact@v2
    with:
      name: my-artifact
      path: my_file.txt
      retention-days: 5
  ```

- Downloading artifact

  ```yaml
  - name: "Download a single artifact"
    uses: actions/download-artifact@v2
    with:
      name: my-artifact
  ```

  **Note**: Drop name to download all artifacts

---

## Test Actions Locally

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

- Set up simple CI pipeline using GitHub Actions
- Reuse code of Python testing lecture
- Pipeline has three steps

    1. Check formatting
    2. Build application
    3. Test application

---

## Advanced Topics

- [Self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)
- [Secrets and tokens](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Continuous deployment](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment)
- [Custom actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions)
- [Build matrices](https://docs.github.com/en/actions/using-workflows/advanced-workflow-features#using-a-build-matrix)
- Using own Docker containers

---

## Further Reading

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart)
