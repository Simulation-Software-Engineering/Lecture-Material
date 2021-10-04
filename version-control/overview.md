# Git -- the standard version control system

*Learning goals*

- Refresh and organize students' existing knowledge on git (learn how to learn more).
- Students can explain difference between merge and rebase and when to use what.
- How to use git workflows to organize research software development in a team.
- Get to know a few useful GitHub/GitLab standards and a few helpful tools.


## Introduction to version control

Duration: 15 mins
Format: slides
Material: `intro_slides.md`
  
## Recap of Git basics

Duration: 15 mins
Format: poll, slides, demo

* Expert level poll on git: ask students to estimate their level.
  * Beginner: I have hardly ever used Git
  * User: pull, commit, push, status, diff
  * Developer: fork, branch, merge, checkout
  * Maintainer: rebase, squash, cherry-pick, bisect
  * Owner: submodules

* show some overview picture: https://merely-useful.tech/py-rse/git-cmdline.html#fig:git-cmdline-remote and discuss
  
* `git --help`, `git commit --help`
* also show incomplete statement `git comm`

* Git, GitHub and GitLab: TODO
  * There is also SourceForge and Bitbucket

## Show how I work with Git and preCICE's workflow

Duration: 20 mins
Format: demo

Starting remark: There is not *the one solution* how to do things with git. I'll show you what I typically use.

* (1) Look at GitHub 
  * organization, precice repository, forks, my fork
  
* (2) working directory: 
  * `git remote -v` (I have upstream, myfork, ...)
  * Mention difference between ssh and https
  * get newest changes `git pull upstream develop`
  * `git log` -> ~/.gitconfig, also check log on GitHub; explain short hash
  * `git branch`
  * `git branch test_changes`
  * `git checkout test_changes`
  * btw, fancy ZSH shell shows git branches 

* (3) first commit
  * `git status` -> always tells you what you can do
  * `vi src/action/Action.hpp`  -> add `#include "MagicHeader.hpp"`
  * `git diff`, `git diff src/com/Action.hpp` --color-words
  * `git add`, `git status`
  * `git commit` "Include MagicHeader in Action.hpp"
  * `git status`, `git log`, `git log -p`, `git show`
  
* (4) Change or revert stuff
  * I forgot to add sth: `git reset --soft HEAD~1`, `git status`
  * `git diff HEAD` because already staged
  * `git log`
  * `git commit -a`
  * actually all that is nonsense: `git reset --hard HEAD~1`
  * modify again, all nonsense before committing: `git checkout`
  
* (5) stash
  * modify sth else, "some idea i have", but actually i need to change this other thing quickly
  * `git stash`
  * `git stash pop`
  
* (6) create PR
  * create commit again
  * preview what will be in PR: `git diff develop..test_changes`
  * `git push -u myfork/test_changes`
  * explain target branch and "somebody else can edit"
  
* (7) Check out someone else's work
  * have a look at an existing PR, look at all tabs, show suggestion feature
  * but sometimes we want to really build and try sth out ... 
  * `git remote -v` (ideally remote not yet known, maybe delete in preparation)
  * `git remote add alex git@github.com:ajaust/precice.git` (or somebody else)
  * `git fetch alex`
  * `git checkout -t alex/[branch-name]`


## Clicker quiz about Git

Duration: 30 mins
Format: clicker quiz

* https://learn.co/lessons/git-github-learn-quiz ... maybe a bit too simple
* https://www.w3schools.com/quiztest/quiztest.asp?qtest=GIT ... also a bit simple, but a few ones are useful
* https://gist.github.com/aspencer8111/17a80fb0a2be7b4718237fe8caa6e09c ... some useful ones
* https://www.codequizzes.com/git ... more complex, but no clicker style
* https://www.codercrunch.com/quiz/take/1650218502/git-branching ... complex and clicker style, some are too hard
* book
  * https://merely-useful.tech/py-rse/git-cmdline.html#git-cmdline-ex-commit a single good question from the book
  * https://merely-useful.tech/py-rse/git-cmdline.html#git-cmdline-ex-history another good one
  * "Recovering older versions of a file"
* question with gitignore, ! example in there, templates from GitHub: https://github.com/github/gitignore


## My favorite neat little Git trick

Duration: 30 mins
Format: student presentations and discussion

* students present in 3-5mins their favorite neat little Git trick (a tool, a command, a configuration, a GitHub thing, ...)
* tell them to prepare after first lecture; but preparation should not take longer than 15 mins; should be a demo
* we also prepare some:
  * GitHub CLI
  * [GitKraken](https://www.gitkraken.com/)
  * `git blame` on GitHub

Remarks:

* only use a GUI once you understand command-line Git


## Working in teams / git workflows

Duration: 15 mins
Format: slides


* why workflows?
  * git offers a lot of flexibility in managing changes. there is no standardized process on how to interact with git (cf. discussion "show my workflow"
  * when working in a team, some agreements need to be made however (especially on how to work with branches)
* which workflow?
  * there are standard solutions
  * it depends a lot on the size of the team (should enhance the effectiveness of the team and not be a burden that limits productivity)
* Centralized Workflow
  * only one branch: the `main` branch
  * keep your changes in local commits till some feature is ready; if ready, directly push to `main`
  * no PRs, now reviews, ...
  * conflicts: fix locally (push not allowed anyway), use `git pull --rebase`
  * good for: small teams, small projectsm, projects which are anyway reviewed over and over again
  * example: (LaTeX) papers (put each section in separate file, each sentence in new line)
* Feature Branch Workflow 
  * each feature (or bugfix) in separate branch, push feature branch to remote; descriptive name, e.g. each feature branch closes one issue (issue number could be in name) 
  * `main` should never contain broken code
  * PR with review to merge from feature branch to `main`, protect direct push to master, CI run in PR
  * PRs can also be opened as draft to only discuss things, let people know that you are working on a feature 
  * rebase feature branch on `main` if necessary
  * delete remote branch once merged and no longer needed (one click on GitHub after merge)
  * good for: 2-3 person code projects, prototyping, websites, documentation 
  * aka [trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development) or [GitHub flow](https://guides.github.com/introduction/flow/)
* Gitflow
  * there is a tool `git-flow`, a wrapper around git, e.g. `git flow init` ... but not really necessary IMHO
  * `main` and `develop`; `main` contains releases as tags, `develop` latest features
  * feature branches created of `develop`, PRs back to `develop`
  * protect `main` and (if wanted) `develop` from direct pushes
  * dedicated release branches (e.g., `v0.2`) created of `develop`, tested, fixed, merged to `main`, tagged, merged back to `develop`
  * hotfix branches directly from and to `main`
  * visualization: https://nvie.com/img/git-model@2x.png, by Vincent Driessen
  * good for: software with users, larger teams; used more or less in preCICE
* Forking workflow
  * gitflow + feature branches on other forks
  * more control over access rights, distinguish between maintainers and external contributors
  * also use feature branches on forks for maintainers? makes overview of branches easier, distinguish between prototype branches (on fork, no PR), serious enhancements (on fork with PR), joint enhancements (on upstream)
  * good for: open-source projects with external contributions
* For all workflows, it is better to do small PRs
  * easier to review
  * faster to merge -> less conflict resolving
  * easier to squash


### Quick reads

* [Atlassian docs on workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
* [Original gitflow blog post](https://nvie.com/posts/a-successful-git-branching-model/)
* [Trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)
* [GitHub flow](https://guides.github.com/introduction/flow/)
* [How to Keep Pull Requests Manageable](https://gist.github.com/sktse/569cb192ce1518f83db58567591e3205)


## Merge vs. rebase

Duration: 15 mins
Format: slides

TODO: look for suitable pictures and create slides

* what is a merge commit
  * show picture with a linear history
  * commits are snapshots, not diffs (but for linear history, this makes no difference)
  * each normal commit has a parent commit, `c05f017` <- `c05f017^` (`^` is the same as `~1`)
  * `git show` gives diff of commit to parent
  * show picture with two branches and a merge commit and `git checkout main`, `git merge feature`
  * a merge commit has two (also multiple, but that's not important) parent commits `c05f017^1` and `c05f017^2`, not one -> can't show unique diff (don't confuse `^2` with `~2`)
  * first parent is to the current commit on the branch you are on
  * `git show` of merge commit shows *combined diff*, GitHub shows `git show --first-parent` ... IMHO all not very helpful
  * `git show -m` shows separate diff to all parents
* why linear history is important
  * merge commits are hard to understand per-se
  * a merge takes all commits from `feature` to `main` -> no longer a linear history
  * developers often follow project by reading commits -> becomes harder to read (where happened what)
  * a bug was introduced between v1.3 and v1.4, a linear history allows to bisect
  * real conflicts are very rare in real projects, most conflicts / merge commits are false positives -> they should be avoided
* how to get a linear history?
  * if there are not changes on `main`, just `git merge --fast-forward feature`
  * if there are changes on `main` -> rebase
* what is rebase?
  * show same graph again, but now with a rebase, `git checkout feature`, `git rebase main`, `git checkout main`, `git merge feature --fast-forward` -> we can keep a linear history
  * downside: history is rewritten, the commits are not the same, they have now different parent commits (similar to a force push)
  * only use rebase if only you work on a branch (a local branch, a branch on your fork)
  * if local changes, very helpful: `git pull --rebase` (fetch & rebase)
* squash and merge
  * GitHub offers three ways how to merge a non-conflicting (no changes in same files) PR: create a merge commit, squash and merge, rebase and merge
  * let students explain options "create a merge commit", "rebase and merge". good or bad?
  * "squash and merge" squashes all commits into one (often single commit of feature branch are important while developing the feature, but not when the feature is merged; keep feature PRs small)
  * also does a rebase, basically does a `git rebase -i`
  * if there are conflicts: resolve with rebase (recommended) or merge on `feature branch`
  * delete `feature` branch after merging (altered history)
* summary
  * try to keep a linear history with rebasing whereever reasonable
  * don't use rebase on a public/shared branch
  * squash before merging if reasonable
    


* `git log --graph` is local view, https://github.com/precice/precice/network is global view


* [Bitbucket docs](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
* [Hackernoon](https://hackernoon.com/git-merge-vs-rebase-whats-the-diff-76413c117333)
* refer to [The GitHub Blog: Commits are snapshots, not diffs](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
* [good stack overflow post](https://stackoverflow.com/questions/40986518/git-show-of-a-merge-commit?answertab=votes#tab-top)

## GitHub standards

Duration: 15 mins
Format: slides, demo

TODO

* README.md
* license
* CONTRIBUTING.md
* issue or PR templates
* closes #34



## Gitlab

* Show DuMuX GitLab as a role model for archiving research results?



## Exercise: SSE Git cheat sheet

Duration: 60 mins
Format: group work (~10-15 students, if more we might need to split)
Prerequisites: everybody needs a GitHub account, everybody needs to have write access to the master branch
Material: TODO: create repo, master branch protected, one md file with title and some placeholder categories. license

Let's create our own SSE Git cheat sheet written in markdown. Obviously, there are many great Git cheat sheets out there. There is also the official manual. Our goal is not make an even better cheat sheet. Instead, our goal is the process of how to get there: to learn how to work together as a team on GitHub and to maybe learn something new about Git on the way. Restrict the cheat sheet to the really important every-day Git commands. We want to have a usable cheat sheet in one hour.

TODO: which git workflow should be used?

1. Fork the [Git cheat sheet repository](TODO)
2. Create issues (in the upstream repository) on what you think the group should work on. Examples: "Define categories" or "add `git pull and push`". Look for and avoid duplicates. Assign yourself if you want to work on an issue. If necessary, use the issue to discuss details. Don't open too many issues right away.
3. If you think you have a good first extension of the cheat sheet, open a PR from a feature branch on your fork to the upstream master branch. Keep PRs concise, such that they are easy to review and quick to merge. Briefly describe the rationale of the PR. Assign yourself to the PR. You are responsible for the life cycle of the PR.
4. Find at least one reviewer for your PR (by asking around offline). Assign them as reviewers or let them assign themselves.
5. Review other PRs. Give constructive feedback how to improve. Avoid endless discussions, better open additional issues if something goes beyond current PRs.
6. Regularly rebase your PR on master (force push to your feature branch if necessary). Avoid merge commits. Ideally, we get perfectly readable history in the end.
7. Merge the PR if you have at least one *approving* review and no *changes requested*. Squash if necessary to get meaningful commits.
8. Start at step 2 or step 5 again.

Bonus:

* Create a project to manage and oversee the overall progress.
* Add a markdownlint GitHub action to check whether our cheat sheet follows markdown standards.
* Discuss and add categories to issues and PRs.
* Extent the readme file and add a contributors list there.
* Push your fork also to a (private) GitLab repository.


Minimal requirement to pass. Everybody should at least ...

* Open and merge one PR
* Give one review

Discussion (at least 10 mins):

* How did it work?
* Where were problems?
* What did you learn? Any other trick you want to share?

Final remarks:

* If you want continue with the cheat sheet or do more of them in other chapters of the lecture (docker, cmake, ...)




## Further reading

### Quick things

* [Video: Git in 15 minutes: basics, branching, no remote](https://www.youtube.com/watch?v=USjZcfj8yxE)
* [The GitHub Blog: Commits are snapshots, not diffs](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
* Chapters [6](https://merely-useful.tech/py-rse/git-cmdline.html) and [7](https://merely-useful.tech/py-rse/git-advanced.html) of Research Software Engineering with Python
* [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)
* [git purr](https://girliemac.com/blog/2017/12/26/git-purr/)

### References

* [Official documentation](http://git-scm.com/doc)






