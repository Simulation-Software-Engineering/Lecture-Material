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

## Special Files (1)

Certain files lead to special formatting (normally directly at root of repo):

- `README.md`
    - ... contains meta information / overview / first steps of software.
    - ... gets rendered on landing page (and in every folder).
- `LICENSE`
    - ... contains software license.
    - ... gets rendered on the sidebar and on repo preview.

---

## Special Files (2)

- `CONTRIBUTING.md`
    - ... contains guidelines for contributing.
    - First-time contributors see banner.
- `CODE_OF_CONDUCT.md`
    - ... contains code of conduct.
    - ... gets rendered on the sidebar.

---

## Special Files (3)

- `CITATION.cff`
    - ... contains preferred citation details.
    - ... gets rendered on the sidebar.
    - ... export to BibTeX.
- `AGENTS.md`
    - ... contains context and instructions for GenAI.
    - ... more and more coding agents read it.


---

## Issues and PRs

- Templates for description are placed in the `.github` folder.
- `closes #34` (or several other keywords: `fixes`, `resolves`) in commit message or PR description will close issue 34 when merged.
- `co-authored-by: name <email>` will attach multiple authors.
- `help wanted` issue label gets rendered on repository preview<br/> (e.g. *"3 issues need help"*).
