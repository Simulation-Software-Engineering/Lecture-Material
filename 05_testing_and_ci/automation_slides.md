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

# Workflow automation

---

## Learning goals

- How to automate common workflows.
- How to use built-in automation of GitHub and GitLab.

---

## Introduction

- Automatize tasks
    - Run tests frequently, give feedback early etc.
    - Cannot forget automatized tasks
    - Less burden to developer
    - Running predefined workflows/pipelines is simple
- Process often integrated in development workflow
    - Example: Support by hooks or Git forges

---

## Typical tasks

- Compile code for different platforms
- Run tests periodically
- Check code in pull request
- Build documentation
- Deploy homepage after changes to source
- Generate coverage reports

---

## Common practices (1/2)

- **Continuous Integration** (CI)
    - Continuously integrate changes into "main" branch.
    - Avoids "merge hell"
    - Relies on testing and checking code continuously
        - Should be automatized

---

## Common practices (2/2)

- **Continuous Delivery** (CD)
    - Software is in a state that allows new release at any time
    - Software package is built
    - Actual release triggered manually
- **Continuous Deployment** (CD)
    - Software is in a state that allows new release at any time
    - Software package is built
    - Actual release triggered automatically (continuously)

---

## Automation services/software

- [GitHub Actions](https://github.com/features/actions)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [Circle CI](https://circleci.com/)
- [Travis CI](https://www.travis-ci.com/)
- [Jenkins](https://www.jenkins.io/)
- ...

---

## Further reading

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD documentation](https://docs.gitlab.com/ee/ci/)
- [What is Continuous Integration?](https://www.atlassian.com/continuous-delivery/continuous-integration)