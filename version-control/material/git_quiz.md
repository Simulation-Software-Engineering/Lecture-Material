# Git Quiz

Questions are taken from [py-rse](https://merely-useful.tech/py-rse/index.html), [learn.co](https://learn.co/lessons/git-github-learn-quiz), [w3schools](https://www.w3schools.com/quiztest/quiztest.asp?qtest=GIT),[this gist from @aspencer8111](https://gist.github.com/aspencer8111/17a80fb0a2be7b4718237fe8caa6e09c), and [codercrunch](https://www.codercrunch.com/quiz/take/1650218502/git-branching).

## Add & Commit I

Which command(s) below would save changes to myfile.txt to a local Git repository? (multiple choice)

* `git commit -m "Add recent changes"`
* `git init myfile.txt` && `git commit -m "Add recent changes"`
* `git add myfile.txt` && `git commit -m "Add recent changes"`
* `git commit myfile.txt -m "Add recent changes"`

## Add & Commit II

Assume you made the following changes. What is the output of the last command in the sequence below?

```bash
touch motivation.txt
echo "Sharing information about myself." > motivation.txt
git add motivation.txt
echo "Documenting major milestones." > motivation.txt
git commit -m "Motivate project"
git restore motivation.txt
cat motivation.txt
```

* `Sharing information about myself.`
* `Documenting major milestones.`
* The following:

```
Sharing information about myself.
Documenting major milestones.
```

* An error message because we have changed motivation.txt without committing first.

## Create Branch I

What is the command to create a new branch named `add-feature-x`?

* `git add branch add-feature-x`
* `git branch new add-feature-x`
* `git branch add add-feature-x`
* `git branch add-feature-x`

## Create Branch II

What is the difference between `git branch add-feature-x` and `git checkout -b add-feature-x`?

* They do the same thing.
* The second command creates a copy of a remote branch while the first command branches from the current local branch.
* They both create a new branch "add-feature-x". However, the first command stays at the current branch while the second directly changes to the new branch.
* The first command creates a new branch. The second command changes to "add-feature-x" if the branch already exists.

## Merge Branches

How can you merge `add-feature-x` into `main`?

* `git merge add-feature-x main`
* `git merge main add-feature-x`
* `git checkout main` && `git merge add-feature-x`
* `git checkout add-feature-x` && `git merge main`

## Delete Branches

What is the command to delete the branch "add-feature-x"?

* `git delete add-feature-x`
* `git rm add-feature-x`
* `git delete branch add-feature-x`
* `git branch -d add-feature-x`

## Add Remote

What is the command to add the remote repository `https://abc.xyz/d/e.git` as "origin"?

* `git remote add origin https://abc.xyz/d/e.git`
* `git origin=https://abc.xyz/d/e.git`
* `git add origin https://abc.xyz/d/e.git`
* `git remote https://abc.xyz/d/e.git`

## Pull

`git pull` is a combination of:

* `git fetch` and `git merge`
* `git fetch` and `git rebase`
* `git fetch` and `git update`
* `git fetch` and `git checkout`

## Undo I

To unstage a currently staged file called `octocat.txt` without losing the changes, the git command is? (multiple choice)

* `git reset --soft octocat.txt`
* `git reset octocat.txt`
* `git checkout HEAD octocat.txt`
* `git restore --staged octocat.txt`

## Undo II

Amira made changes this morning to a shell script called `data_cruncher.sh` that she has been working on for weeks. Her changes broke the script, and she has now spent an hour trying to get it back in working order. Luckily, she has been keeping track of her project’s versions using Git. Which of the commands below can she use to recover the last committed version of her script? (multiple choice)

* `git checkout HEAD`
* `git checkout HEAD data_cruncher.sh`
* `git checkout HEAD~1 data_cruncher.sh`
* `git checkout <unique ID of last commit> data_cruncher.sh`
* `git restore data_cruncher.sh`
* `git restore HEAD`

## Undo III

How can you create a commit that undoes the changes of some other commit?

* `git undo`
* `git reset`
* `git checkout`
* `git revert`

## Clean

What does `git clean` do?

* Remove all untracked files except ignored ones
* Remove all ignored files
* Unstage everything
* Delete all commits that are not pushed yet

## Detached HEAD

What can cause you to enter a "detached HEAD" state?

* `git clean`
* Checking out a commit that doesn't have a branch pointing to it
* Cloning a bare repository
* Finishing a merge

## Delete Remote Branch

How can you delete a branch in a remote repository?

* `git push delete branchName`
* `git push origin --delete branchName`
* `git rm --push branchName`
* You can only do this through the web interface of the remote (e.g. GitHub)
