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

# Workflow Automation

---

## Learning Goals

- Name and explain common workflows to automate in RSE.
- Explain the differences between the various continuous methodologies.
- Explain why automation is crucial in RSE.
- Write basic automation scripts for GitHub Actions.
- Read basic automation scripts for GitLab CI/CD.
- Name and roughly explain the necessary steps to host GitLab Runners yourself.

---

## Why Automation?

- Automatize tasks
    - Run tests frequently, give feedback early etc.
    - Ensure reproducible test environments
    - Cannot forget automatized tasks
    - Less burden to developer (and their workstation)
    - Avoid manual errors
- Process often integrated in development workflow
    - Example: Support by Git hooks or Git forges

---

## Typical Automation Tasks in RSE

- Check code formatting and quality
- Compile and test code for different platforms
- Periodically run tasks
    - Big tests, nightly builds...
- Build documentation and deploy it
- Generate coverage reports and visualization
- Build, package, and upload releases

---

## Continuous Methodologies (1/2)

- **Continuous Integration** (CI)
    - Continuously integrate changes into "main" branch
    - Avoids "merge hell"
    - Relies on testing and checking code continuously
        - Should be automatized

---

## Continuous Methodologies (2/2)

- **Continuous Delivery** (CD)
    - Software is in a state that allows new release at any time
    - Software package is built
    - Actual release triggered manually
- **Continuous Deployment** (CD)
    - Software is in a state that allows new release at any time
    - Software package is built
    - Actual release triggered automatically (continuously)

---

## Automation Services/Software

- [GitHub Actions](https://github.com/features/actions)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [Circle CI](https://circleci.com/)
- [Travis CI](https://www.travis-ci.com/)
- [Jenkins](https://www.jenkins.io/)
- ...

---

## Further Reading

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD documentation](https://docs.gitlab.com/ee/ci/)
- [What is Continuous Integration?](https://www.atlassian.com/continuous-delivery/continuous-integration)
