# Git -- the standard version control system

Learning goals:
* we don't teach git in the course, we only recap
* TODO


## Introduction to version control

Duration: 15 mins
Format: slides

* very brief: why needed
  * tracks changes to files and helps people share those changes with each other
  * can also be done via email or Google Docs, but not so accurate and efficient
  * originally developed for software development, but today cornerstone of reproducible research

> If you can't git diff it, the file format is broken 

* how it works
  * master copy of code in repository, can't edit directly
  * instead: check out a working copy of code, edit, commit changes back
  * repository records complete revision history (you can go back in time & it's clear who did what and when)
  
[PhD Comics: A story told in file names](https://phdcomics.com/comics/archive_print.php?comicid=1323)

* short history of version control
  * RCS, later CVS became front end of RCS
  * Microsoft Visual SourceSafe
  * SVN
  * centralized vs. distributed (memory vs. performance)
  * distributed: Mercurial, Git (started more or less at same time, others as well, frustration over commercial Bitkeeper)
  * past: highly fragmented market, today no longer: there is nearly only Git; TODO: stats over time
    * TODO: our simulation software list: how many use Git?
    * convergence to a single "standard" is also a good thing
  * [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)
    
  
* Git itself is open-source: GPL license
  * source on [GitHub](https://github.com/git/git), contributions are a bit more complicated than a simple PR
  * written mainly in C
  * started by Linus Torvalds, first release in 2005, core maintainer since later 2005: Junio Hamano
  
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

## Show my workflow

Duration: 20 mins
Format: demo

Starting remark: There is not *the one solution* how to do things with git. I'll show you what I typically use.

* (1) Look at GitHub 
  * organization, precice repository, forks, my fork
  
* (2) working directory: 
  * `git remote -v` (I have upstream, myfork, ...)
  * Mention difference between ssh and https
  * get newest changes `git pull upstream develop`
  * `git log` -> ~/.gitconfig, also check log on GitHub
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

TODO

* git workflows
* https://www.atlassian.com/git/tutorials/comparing-workflows
* GitHub flow: 
  * https://guides.github.com/introduction/flow/ 
  * https://docs.github.com/en/get-started/quickstart/github-flow
  * https://lucamezzalira.com/2014/03/10/git-flow-vs-github-flow/
* which ones does preCICE use?

* keep PRs small
  * easier to review
  * faster to merge -> less conflict resolving
  * easier to squash


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
  * "squash and merge" squashes all commits and the merge commit into one (often single commit of feature branch are important while developing the feature, but not when the feature is merged; keep feature PRs small)
  * no linear history, but still very readable (as there was no conflict it makes no real difference what the parent commit of the squashed commit is; the diff is the same)
  * if there are conflicts: resolve with rebase (recommended) or merge on `feature branch`
  * delete `feature` branch after merging
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






