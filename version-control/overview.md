# Git -- the standard version control system

Learning goals:

- Refresh and organize students' existing knowledge on git (learn how to learn more).
- Students can explain difference between merge and rebase and when to use what.
- How to use git workflows to organize research software development in a team.
- Get to know a few useful GitHub/GitLab standards and a few helpful tools.

## Introduction to version control

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | slides | [`intro_slides.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/version-control/material/intro_slides.md) |

## Recap of Git basics

Duration: 15 mins
Format: poll, picture, demo

| Duration | Format |
| --- | --- |
| 15 minutes | poll, picture, demo |

- Expert level poll on git: ask students to estimate their level.
  - Beginner: I have hardly ever used Git
  - User: pull, commit, push, status, diff
  - Developer: fork, branch, merge, checkout
  - Maintainer: rebase, squash, cherry-pick, bisect
  - Owner: submodules

![git overview picture from py-rse](https://merely-useful.tech/py-rse/figures/git-cmdline/git-remote.png)

- `git --help`, `git commit --help`
- incomplete statement `git comm`

- There is a difference between Git and hosting services ([*forges*](https://en.wikipedia.org/wiki/Forge_(software)))
  - [GitHub](https://github.com/)
  - [GitLab](https://about.gitlab.com/), open-source, hosted e.g. at [IPVS](https://gitlab-sim.informatik.uni-stuttgart.de)
  - [Bitbucket](https://bitbucket.org/product/)
  - [SourceForge](https://sourceforge.net/)
  - many more
  - often, more than just hosting, also DevOps

- Give outlook on remainder of Git chapter: *How I work with Git*, quiz, advanced topics (workflows, rebase, standards), *my neat little Git trick*

## How I work with Git

| Duration | Format |
| --- | --- |
| 40 minutes | demo |

Starting remarks:

- There is not *the one solution* how to do things with Git. I simply show what I typically use.
- Don't use a client if you don't understand the command line `git`

- (1) Look at GitHub
  - [preCICE repository](https://github.com/precice/precice)
  - default branch `develop`
  - fork -> my fork

- (2) Working directory:
  - ZSH shell shows git branches
  - `git remote -v` (I have upstream, myfork, ...)
  - mention difference between ssh and https (also see GitHub)
  - get newest changes `git pull upstream develop`
  - `git log` -> I use special format, see `~/.gitconfig`,
  - check log on GitHub; explain short hash
  - `git branch`
  - `git branch add-demo-feature`
  - `git checkout add-demo-feature`

- (3) First commit
  - `git status` -> always tells you what you can do
  - `vi src/action/Action.hpp` -> add `#include "MagicHeader.hpp"`
  - `git diff`, `git diff src/com/Action.hpp`, `git diff --color-words`
  - `git status`, `git add`, `git status`
  - `git commit` -> "Include MagicHeader in Action.hpp"
  - `git status`, `git log`, `git log -p`, `git show`

- (4) Change or revert things
  - I forgot to add sth: `git reset --soft HEAD~1`, `git status`
  - `git diff`, `git diff HEAD` because already staged
  - `git log`
  - `git commit`
  - actually all that is nonsense: `git reset --hard HEAD~1`
  - modify again, all nonsense before committing: `git checkout src/action/Action.hpp`

- (5) Stash
  - while working on unfinished feature, I need to change / test this other thing quickly, too lazy for commits / branches
  - `git stash`
  - `git stash pop`

- (6) Create PR
  - create commit again
  - preview what will be in PR: `git diff develop..add-demo-feature`
  - `git push -u myfork add-demo-feature` -> copy link
  - explain PR template
  - explain target branch
  - explain "Allow edits by maintainers"
  - cancel
  - my fork -> branches -> delete

- (7) Check out someone else's work
  - have a look at an existing PR, look at all tabs, show suggestion feature
  - but sometimes we want to really build and try sth out ...
  - `git remote -v`
  - `git remote add alex git@github.com:ajaust/precice.git` if I don't have remote already (or somebody else)
  - `git fetch alex`
  - `git checkout -t alex/[branch-name]`
  - I could now also push to `ajaust`'s remote

## Clicker quiz about Git

| Duration | Format | Material |
| --- | --- | --- |
| 30 minutes | quiz | [`git_quiz.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/version-control/material/git_quiz.md) |

## My favorite neat little Git trick

| Duration | Format |
| --- | --- |
| 30-45 minutes | student presentations and discussion |

- Students present in 3-5 mins their favorite *neat little Git trick* (a tool, a command, a configuration, a GitHub thing, ...).
- Preparation should not take longer than 15 mins, should be a demo.
- Lecturers also prepare some.
- Examples Benjamin:
  - `git blame` on GitHub
  - `git reflog`
  - [gitignore templates](https://github.com/github/gitignore)
  - [GitExplorer](https://gitexplorer.com/)
- More examples:
  - GitHub CLI
  - [GitKraken](https://www.gitkraken.com/)
- Collect links via PRs

Remarks:

- Only use a GUI once you understand command-line Git.

## Merge vs. rebase

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | slides | [`workflow_slides.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/version-control/material/workflow_slides.md) |

## Working in teams / git workflows

| Duration | Format | Material |
| --- | --- | --- |
| 15 minutes | slides | TODO |

## GitHub/GitLab standards

| Duration | Format |
| --- | --- |
| 10 minutes | slides, demo |

TODO

- README.md
- license
- CONTRIBUTING.md
- issue or PR templates
- closes #34

## Exercise: SSE Git cheat sheet

Duration: 75 mins
Format: group work (~10-15 students, if more we might need to split)
Prerequisites: everybody needs a GitHub account, everybody needs to have write access to the master branch
Material: TODO

## Further reading

### Quick things

- [Video: Git in 15 minutes: basics, branching, no remote](https://www.youtube.com/watch?v=USjZcfj8yxE)
- [The GitHub Blog: Commits are snapshots, not diffs](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
- Chapters [6](https://merely-useful.tech/py-rse/git-cmdline.html) and [7](https://merely-useful.tech/py-rse/git-advanced.html) of Research Software Engineering with Python
- [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)
- [git purr](https://girliemac.com/blog/2017/12/26/git-purr/)

### References

- [Official documentation](http://git-scm.com/doc)
