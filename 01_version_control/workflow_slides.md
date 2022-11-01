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
</style>

# Working in Teams / Git Workflows

---

## Why Workflows?

- Git offers a lot of flexibility in managing changes.
- When working in a team, some agreements need to be made however (especially on how to work with branches).

---

## Which Workflow?

- There are standard solutions.
- It depends on the size of the team.
- Workflow should enhance effectiveness of team, not be a burden that limits productivity.

---

## Centralized Workflow

- Only one branch: the `main` branch
- Keep your changes in local commits till some feature is ready
- If ready, directly push to `main`; no PRs, no reviews
- Conflicts: fix locally (push not allowed anyway), use `git pull --rebase`
- **Good for**: small teams, small projects, projects that are anyway reviewed over and over again
- Example: LaTeX papers
    - Put each section in separate file
    - Put each sentence in separate line

---

## Feature Branch Workflow

- Each feature (or bugfix) in separate branch
- Push feature branch to remote, use descriptive name
    - e.g. issue number in name if each branch closes one issue
- `main` should never contain broken code
- Protect direct push to `main`
- PR (or MR) with review to merge from feature branch to `main`
- Rebase feature branch on `main` if necessary
- Delete remote branch once merged and no longer needed (one click on GitHub after merge)
- **Good for**: small teams, small projects, prototyping, websites (continuous deployment), documentation
- Aka. [trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development) or [GitHub flow](https://guides.github.com/introduction/flow/)

---

## Gitflow

- [Visualization by Vincent Driessen](https://nvie.com/img/git-model@2x.png), from [original blog post in 2010](https://nvie.com/posts/a-successful-git-branching-model/)
- `main` and `develop`
    - `main` contains releases as tags
    - `develop` contains latest features
- Feature branches created of `develop`, PRs back to `develop`
- Protect `main` and (possibly) `develop` from direct pushes
- Dedicated release branches (e.g., `v1.0`) created of `develop`
    - Tested, fixed, merged to `main`
    - Afterwards, tagged, merged back to `develop`
- Hotfix branches directly of and to `main`
- **Good for**: software with users, larger teams
- There is a tool `git-flow`, a wrapper around `git`, e.g. `git flow init` ... but not really necessary IMHO

---

## Forking Workflow

- Gitflow + feature branches on other forks
- More control over access rights, distinguish between maintainers and external contributors
- Should maintainers also use branches on their forks?
    - Makes overview of branches easier
    - Distinguishes between prototype branches (on fork, no PR), serious enhancements (on fork with PR), joint enhancements (on upstream)
- **Good for**: open-source projects with external contributions (used more or less in preCICE)

---

## Do Small PRs

- For all workflows, it is better to do small PRs
    - Easier to review
    - Faster to merge --> fewer conflicts
    - Easier to squash

---

## Quick reads

- [Atlassian docs on workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
- [Original gitflow blog post](https://nvie.com/posts/a-successful-git-branching-model/)
- [Trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)
- [GitHub flow](https://guides.github.com/introduction/flow/)
- [How to keep pull requests manageable](https://gist.github.com/sktse/569cb192ce1518f83db58567591e3205)
