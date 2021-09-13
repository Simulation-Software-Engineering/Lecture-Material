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

*  Expert level poll: ask students to estimate their level.
  * Beginner: I have hardly ever used Git
  * User: pull, commit, push, status, diff
  * Developer: fork, branch, merge, checkout
  * Maintainer: rebase, squash,
  * Owner: Test me, I know it all
  
* show some overview picture: https://images.app.goo.gl/7bq21CbKk53HB7h57 and discuss
  
* `git --help`, `git commit --help`

* Git, GitHub and GitLab: TODO
  * There is also SourceForge and Bitbucket

## Show my workflow

Duration: 20 mins
Format: demo

* (1) Look at GitHub 
  * organization, precice repository, forks, my fork
  
* (2) working directory: 
  * `git remote -v`
  * get newest changes `git pull upstream develop`
  * `git log` -> ~/.gitconfig, also check log on GitHub
  * `git branch`
  * `git branch test_changes`
  * `git checkout test_changes`
  * btw, fancy ZSH shell shows git branches 

* (3) first commit
  * `vi src/com/Action.hpp` 
  * `git status` -> always tells you what you can do
  * `git diff`, `git diff src/com/Action.hpp` --color-words
  * `git add`, `git status`
  * `git commit` "Include MagicHeader in Action.hpp"
  * `git status`, `git log`
  
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
  
* (6) squash
  * do two commits, `git log`
  * `git rebase -i HEAD~2` (i=interactive)
  * change second to squash to only have first commit
  * `git log`
  * but really all changes? `git diff HEAD~1`
  
* (7) create PR
  * target branch
  * also look at existing PR
  * suggestion feature



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


## Merge vs. rebase

Duration: 15 mins
Format: slides

TODO

* why linear history is important

## GitHub standards

Duration: 15 mins
Format: slides, demo

TODO

* README.md
* license
* CONTRIBUTING.md
* issue or PR templates

## Working in teams

Duration: 15 mins
Format: slides

TODO

* branching workflows



## Exercise: SSE Git cheat sheet

Duration: 60 mins
Format: group work (~10-15 students, if more we might need to split)
Prerequisites: everybody needs a GitHub account, everybody needs to have write access to the master branch
Material: TODO: create repo, master branch protected, one md file with title and some placeholder categories. license

Let's create our own SSE Git cheat sheet written in markdown. Obviously, there are many great Git cheat sheets out there. There is also the official manual. Our goal is not make an even better cheat sheet. Instead, our goal is the process of how to get there: to learn how to work together as a team on GitHub and to maybe learn something new about Git on the way. Restrict the cheat sheet to the really important every-day Git commands. We want to have a usable cheat sheet in one hour.

1. Fork the [Git cheat sheet repository](TODO)
2. Create issues (in the upstream repository) on what you think the group should work on. Examples: "Define categories" or "add `git pull and push`". Look for and avoid duplicates. Assign yourself if you want to work on an issue. If necessary, use the issue to discuss details. Don't open too many issues right away.
3. If you think you have a good first extension of the cheat sheet, open a PR from a feature branch on your fork to the upstream master branch. Keep PRs concise, such that they are easy to review and quick to merge. Briefly describe the rationale of the PR. Assign yourself to the PR. You are responsible for the life cycle of the PR.
4. Find at least one reviewer for your PR (by asking around offline). Assign them as reviewers or let them assign themselves.
5. Review other PRs. Give constructive feedback how to improve. Avoid endless discussions, better open additional issues if something goes beyond current PRs.
6. Regularly rebase your PR on master (force push to your feature branch if necessary). Avoid merge commits. Ideally, we get a perfect linear history in the end.
7. Merge the PR if you have at least one *approving* review and no *changes requested*. Squash if necessary.
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




## Further reading

### Quick things

* [Video: Git in 15 minutes: basics, branching, no remote](https://www.youtube.com/watch?v=USjZcfj8yxE)
* [The GitHub Blog: Commit are snapshots, not diffs](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
* Chapters [6](https://merely-useful.tech/py-rse/git-cmdline.html) and [7](https://merely-useful.tech/py-rse/git-advanced.html) of Research Software Engineering with Python
* [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)

### References

* [Official documentation](http://git-scm.com/doc)






