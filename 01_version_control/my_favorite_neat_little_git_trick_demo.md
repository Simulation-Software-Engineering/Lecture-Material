# My Favorite Neat Little Git Trick

- Students present in 1-3 mins their favorite *neat little Git trick* (a tool, a command, a configuration, a GitHub thing, ...).
- Preparation should not take longer than 15 mins, should be a demo.
- Lecturers also prepare some.

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
