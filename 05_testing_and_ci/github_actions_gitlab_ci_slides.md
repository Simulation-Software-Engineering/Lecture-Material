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

# Automation with GitHub Actions and GitLab CI/CD

---

## Learning Goals

- You know how to set up

---

## Introduction

- In lecture: Jobs that use Docker

---

## Common terms

- Artifact: Data that should be preserved after a step finishes
- Runner: Some instance to run code, actions...

--

## Common features

- Configuration via YAML files stored in repository
  - Infrastructure as code

---

## GitHub Actions

> Automate, customize, and execute your software development workflows right in your repository with GitHub Actions.

[From: https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

## Components (1/2)

<img src="https://docs.github.com/assets/cb-25628/images/help/images/overview-actions-simple.png" width=50%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">


From [GitHub Actions Tutorial](https://docs.github.com/en/actions)

---

## Components (2/2)



---

## Marketplace

---

## Test actions locally

- [act](https://github.com/nektos/act)

---

## Self-hosted runners

-

---

## GitLab CI

---

## Advanced topics

- [Parent-child pipelines](https://docs.gitlab.com/ee/ci/pipelines/parent_child_pipelines.html)

---

## GitLab Runner

- Installation is rather easy with Docker

---

## Comparison

- GitHub Actions run on GitHub's hardware -> Limited compute time. Pay money for additional compute time.
- GitLab CI runs on GitLab Runner. Install runner yourself or pay some service.
- Are jobs run for other users?
    - GitHub: Yes
    - GitLab: No

---

## General notes

- Make sure nobody breaks/deactivates your tests in their contributions

---

## Further reading

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart)