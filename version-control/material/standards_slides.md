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

# GitHub / GitLab Standards

---

## Why Standards?

- GitHub uses standards / conventions
- Many are supported by most forges
- **This is good**

---

## Special Files

Certain files lead to special formatting (normally directly at root of repo):

- `README.md`
  - Contains meta information / overview / first steps of software
  - Gets rendered on landing page (and in every folder)
- `LICENSE`
  - Contains software license
  - Gets rendered on right sidebar, when clicking on license, and on repo preview
- `CONTRIBUTING.md`
  - Contains guidelines for contributing
  - First-time contributors see banner
- `CODE_OF_CONDUCT.md`
  - Contains code of conduct
  - Creates link on community profile

---

## Issues and PRs

- Templates for description in `.github` folder
- `closes #34` (or several other keywords: `fixes`, `resolves`) in commit message or PR description will close issue 34 when merged
- `help wanted` label gets rendered on repo preview (e.g. *"3 issues need help"*)
