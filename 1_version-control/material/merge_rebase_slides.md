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

# Merge vs. Rebase

---

## Linear History

<img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/version-control/material/figs/history_linear/fig.png" width=60%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

- Commits are snapshots + pointer to parent, not diffs
    - But for linear history, this makes no difference
- Each normal commit has one parent commit
    - `c05f017^` <-- `c05f017`
    - `A` = `B^` <-- `B`
    - (`^` is the same as `~1`)
    - Pointer to parent commit goes into hash
- `git show` gives diff of commit to parent

---

## Merge Commits


- `git checkout main && git merge feature`
    <img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/version-control/material/figs/history_merge/fig.png" width=70%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px" >
- A merge commit (normally) has two parent commits `M^1` and `M^2` (don't confuse `^2` with `~2`)
    - Can't show unique diff
    - First parent relative to the branch you are on (`M^1` = `C`, `M^2` = `E`)
- `git show`
    - `git show`: *"combined diff"*
    - GitHub: `git show --first-parent`
    - `git show -m`: separate diff to all parents

---

## Why is a Linear History Important?

We use here:

> Linear history := no merge commits

- Merge commits are hard to understand per se
- A merge takes all commits from `feature` to `main` (on `git log`) --> hard to understand
- Developers often follow projects by reading commits (reading the diffs) --> harder to read (where happened what)
- Tracing bugs easier with linear history (see `git bisect`)
    - Example: we know a bug was introduced between `v1.3` and `v1.4`

---

## How to get a Linear History?

- Real conflicts are very rare in real projects, most merge commits are false positives (not conflicts) and should be avoided
- If there are no changes on `main`, `git merge` does a *"fast-forward"* merge (no merge commit)
- If there are changes on `main`, rebase `feature` branch

---

## Rebase

- `git checkout feature && git rebase main`
    <img src="https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/version-control/material/figs/history_rebase/fig.png" width=90%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">
- New parents --> new hashes --> history is rewritten
- If `feature` is already on remote, it needs a force push `git push --force myfork feature`
- Be careful: only use rebase if **only you** work on a branch (a local branch or a branch on your fork)
- Remark: for local branches very helpful: `git pull --rebase` (fetch & rebase)

---

## GitHub PR Merge Variants

- GitHub offers three ways to merge a non-conflicting (no changes in same files) PR:
    - Create a merge commit
    - Squash and merge
    - Rebase and merge
- Look at a PR together, e.g. [this one](https://github.com/precice/precice/pull/986) (will be closed eventually)

> What do the options do?

---

## Squash and Merge

- ... squashes all commits into one
    - Often, single commits of feature branch are important while developing the feature,
    - ... but not when the feature is merged
    - Works well for small feature PRs
- ... also does a rebase (interactively, `git rebase -i`)

---

## Conflicts

> But what if there is a conflict?

- Resolve by rebasing `feature` branch (recommended)
- Or resolve by merging `main` into `feature`

---

## Summary and Final Remarks

- Try to keep a linear history with rebasing whenever reasonable
- Don't use rebase on a public/shared branch
- Squash before merging if reasonable
- Delete `feature` branch after merging
- Local view: `git log --graph`
- Remote view on GitHub, e.g. [for preCICE](https://github.com/precice/precice/network)

---

## Further Reading

- [Bitbucket docs: "Merging vs. Rebasing"](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [Hackernoon: "What's the diff?"](https://hackernoon.com/git-merge-vs-rebase-whats-the-diff-76413c117333)
- [GitHub Blog: "Commits are snapshots, not diffs"](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
- [Stack Overflow: "Git show of a merge commit"](https://stackoverflow.com/questions/40986518/git-show-of-a-merge-commit?)
