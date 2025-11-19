# My Favorite Neat Little Git Trick

- Students present in 1-3 mins their favorite *neat little Git trick* (a tool, a command, a configuration, a GitHub thing, ...).
- Preparation should not take longer than 15 mins, should be a demo.
- Lecturers also prepare some.

## Tricks from Winter Team 2025/26

- Click on line number on GitHub and then `blame` to study history of file
- GitHub uses [gitignore templates](https://github.com/github/gitignore) if you create a `.gitignore` file from GitHub
- To get a nice compact `git log`, you can add the following to your `gitconfig`:

    ```
    [format]
            pretty = format:%C(auto,yellow)%h %C(auto,blue)%>(12,trunc)%ad %C(auto,green)%<(20,trunc)%aN%C(auto,reset)%s%C(auto,red)% gD% D
    ```

- If you rebased/merged and messed up your history, use `git reflog` to go back to a previous state
- If you only need one file from another commit or branch, use `git checkout <branch_or_sha> -- <path>`
- Use [Git LFS](https://git-lfs.com/) for big files >10 MB or for non-diffable binaries (e.g., images, media, archives, shared libraries).
- Prefer `git add -p` over `git add [FILE]`. This allows you to specify what you want to add to a commit in a more fine-grained manner
- A very nice alias for editing any earlier commit, without having to manually rebase:

    ```
    [alias]
        amend = "!f() { \
            COMMIT=$(git rev-parse --short \"$1\") && \
            git commit --fixup \"$COMMIT\" && \
            GIT_SEQUENCE_EDITOR=true git rebase --autosquash --autostash --interactive "$COMMIT^"; \
        }; f"
    ```

    Usage: e.g. `git add -p ...` and then `git amend HEAD~5`. This would add the staged changes to the fifth last commit.

## Tricks from Winter Term 2024/25

- Click on line number on GitHub and then `blame` to study history of file
- GitHub uses [gitignore templates](https://github.com/github/gitignore) if you create a `.gitignore` file from GitHub
- To get a nice compact `git log`, you can add the following to your `gitconfig`:

    ```
    [format]
            pretty = format:%C(auto,yellow)%h %C(auto,blue)%>(12,trunc)%ad %C(auto,green)%<(20,trunc)%aN%C(auto,reset)%s%C(auto,red)% gD% D
    ```

- Fix spelling mistakes in latest commit, which was not pushed to the remote yet
    - `git commit -m "Improved commit message" --amend`
    - Use with local changes only!

- Be faster with Git using aliases
    - For example with the `zsh` shell and the [OhMyZsh! git plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git)
        - `git commit -> gc`
        - `git log --graph -> glgg`

- To create a custom `.gitignore` file using *multiple* languages or IDEs, you can also use [gitignore.io](https://gitignore.io/).
    - *Toptal* also provides a [cli tool](https://docs.gitignore.io/install/command-line) which enables quick creation of a `.gitignore` file in the current repository.
    - You can also use `wget` or `curl` in combination with [https://www.toptal.com/developers/gitignore/api/](https://www.toptal.com/developers/gitignore/api/) followed by a comma (`,`) separated list to get the `.gitignore` file directly without the cli.

- Use Git Bisect to identify bugs in your code
    - This command uses a binary search algorithm to find which commit in your project's history introduced a bug. You use it by first telling it a "bad" commit that is known to contain the bug, and a "good" commit that is known to be before the bug was introduced. Then git bisect picks a commit between those two endpoints and asks you whether the selected commit is "good" or "bad".
    - Start bisecting with `git bisect start`, mark the bad commit using `git bisect bad <commit>` and the last known good one with `git bisect good <commit>`. After a bisect session, to clean up the bisection state use `git bisect reset`.
    - It continues narrowing down the range until it finds the exact commit that introduced the change/bug.
    - For a practical demonstration, refer to the following repository: [Git Bisect Little Trick Demo](https://github.com/Vaish-W/git-bisect-little-trick-demo).

## Tricks from Winter Term 2022/23

- An interactive learning environment: [Learn Git Branching](https://learngitbranching.js.org/)
- Click on line number on GitHub and then `blame` to study history of file
- GitHub uses [gitignore templates](https://github.com/github/gitignore) if you create a `.gitignore` file from GitHub
- To get a nice compact `git log`, you can add the following to your `gitconfig`:

    ```
    [format]
            pretty = format:%C(auto,yellow)%h %C(auto,blue)%>(12,trunc)%ad %C(auto,green)%<(20,trunc)%aN%C(auto,reset)%s%C(auto,red)% gD% D
    ```

- `git gui citool` is a nice GUI to stage parts of your changes (https://git-scm.com/docs/git-gui).

### Git Lens

- [Git Lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) extends the Git capabilities built into Visual Studio Code. It helps you visualize code authorship at a glance using Git Blame annotations and Code Lens, seamlessly navigate and explore Git repositories, gain valuable insights with powerful comparison commands, and more.
- The Git Lens extension is one of the most popular in the community and is also the most powerful. In most cases, its functionality can replace either of the previous two extensions.
- For blame information, a subtle message appears to the right of the line you are working on, letting you know the change was made when it was made and the associated commit message. Some additional information is shown when you hover over this message, like the code change itself, the timestamp, and more.
- For Git history information, this extension offers a variety of features. You can easily access various options, including viewing file history, comparing to previous versions, opening a specific revision, and more. To open these options, you can click the text in the bottom status bar that contains the author who edited the line of code and how long it has been since it was edited.
- This extension is packed with functionality and will take you a while to absorb everything it offers.

### A helpful git config

```
[push]
        default = simple
        autoSetupRemote = true
[pull]
        rebase = true
[rebase]
        autoStash = true
        autosquash = true
[init]
        defaultBranch = main
[alias]
        # git mr origin 5
        mr = !sh -c 'git fetch $1 merge-requests/$2/head:mr-$1-$2 && git checkout mr-$1-$2' -
        pushf = push --force-with-lease
        fixup = "!git log -n 50 --pretty=format:'%h %s' --no-merges | fzf | cut -c -7 | xargs -o git commit --fixup"
[url "git@github.com:"]
        insteadOf = https://github.com/
        insteadOf = http://github.com/
        insteadOf = git://github.com/
        insteadOf = gh://
[url "git@gitlab.com:"]
        insteadOf = https://gitlab.com/
        insteadOf = http://gitlab.com/
        insteadOf = git://gitlab.com/
        insteadOf = gl://
```

What does it do?

- When pushing new branches, automatically set the upstream branch to a branch with the same name on the primary remote
- Auto rebase on pull and auto stash, on rebase (configured in git config)
- Git Alias `fixup = "!git log -n 50 --pretty=format:'%h %s' --no-merges | fzf | cut -c -7 | xargs -o git commit --fixup"`
    - Allows committing current staged changes as a fixup commit for a previous commit
    - Follow by `git rebase -i --autosquash` (or enable `autosquash` for rebase on default in git config)
    - Requires [`fzf`](https://github.com/junegunn/fzf) to be installed.
- Automatically fix http(s) urls (changing it to the correct ssh url) using git config `url` section
    - Also allows copying url from browser
    - Also allows entering `gh://username/repo` by memory

## Tricks from Winter Term 2021/22

- Click on line number on GitHub and then `blame` to study history of file
- `git reflog` to resurrect accidentally deleted branches
- GitHub uses [gitignore templates](https://github.com/github/gitignore) if you create a `.gitignore` file from GitHub
- [GitExplorer](https://gitexplorer.com/): a nice way to generate important git command
- Shortcut `t` to search project files on GitHub
- Shortcut `ctrl` + `k` to never use mouse on GitHub again
- `git effort` (from `git-extras`repository): Show effort statistics on file(s) in repository
- `git commit -m "Title of commit" -d "Description of commit` to specify a commit message and description without going to vim
- Use [aheadfork](https://github.com/mbomb007/aheadfork) to find GitHub forks that are ahead
- Use [permanent links](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting/creating-a-permanent-link-to-a-code-snippet#linking-to-code) on GitHub to refer to and display code snippets in issues
- Coding in the cloud with GitHub [Codespaces](https://github.com/features/codespaces) and VS Code: type `.` in a repository to jump into the editor
- One can create empty commits, i.e. a commit without any changes, using the `--allow-empty` options. This can be useful for debugging, for example. The full command could look like this: `git commit --allow-empty -m 'This commit is empty'`
- You can generate a list of contributors sorted by the number of contributions using `git shortlog --summary --numbered --email.
- If you have some contributors with several different email addresses and/or configured names, you can merge them via aliases in a file called [`.mailmap`](https://git-scm.com/docs/gitmailmap) that should reside in the root of the repository.
