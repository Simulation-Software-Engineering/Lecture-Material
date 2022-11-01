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

## What do we mean with Standards?

- GitHub uses standards or conventions.
- Certain files or names trigger certain behavior automatically.
- Many are supported by most forges.
    - **This is good.**
    - Everybody should know them.

---

## Special Files

Certain files lead to special formatting (normally directly at root of repo):

- `README.md`
    - ... contains meta information / overview / first steps of software.
    - ... gets rendered on landing page (and in every folder).
- `LICENSE`
    - ... contains software license.
    - ... gets rendered on right sidebar, when clicking on license, and on repo preview.
- `CONTRIBUTING.md`
    - ... contains guidelines for contributing.
    - First-time contributors see banner.
- `CODE_OF_CONDUCT.md`
    - ... contains code of conduct.
    - ... gets rendered on right sidebar.

---

## Issues and PRs

- Templates for description in `.github` folder
- `closes #34` (or several other keywords: `fixes`, `resolves`) in commit message or PR description will close issue 34 when merged.
- `help wanted` label gets rendered on repo preview (e.g. *"3 issues need help"*).
