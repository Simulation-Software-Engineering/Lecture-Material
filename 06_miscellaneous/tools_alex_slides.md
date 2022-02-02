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

# Tools (Alex)

---

## Introduction

- My opinion/experience

---

## Editor and IDEs

- Current choices
    - [VS Code](https://code.visualstudio.com/)
        - Plenty of addons, powerful feature
    - [VIM](https://www.vim.org/)
        - Plenty of addons, small footprint, special input
    - Sublime Text

- Earlier choices: Gedit, NEdit, Emacs, QtCreator...
- Switching editors may impact productivity.
- Knowing basics of one CLI editor useful

---

## Dotfiles

- I (try to) organize my dotfiles
    - [Git repository](https://github.com/ajaust/dotfiles)
- Easy to deploy via Git
- Should be portable
- Configuration files not applicable to a system are usually ignored
- Checkout other people's dotfiles
- **Warning**: Do not share secrets by accident

---

## Terminal

- [fzf](https://github.com/junegunn/fzf): A command line fuzzy finder
- Bash prompt (`PS1`)
    - Show directory
    - Show branch if in a Git repository
- Terminal emulator with UTF-8 support
- Tiling window manager (i3wm, swaywm)

---

## Tools

- `find`, `grep`, `man` etc.: Basic Unix/Linux commands
- [ripgrep](https://github.com/BurntSushi/ripgrep): Fast grep respecting `.gitignore` tailored to search through (typical) code/repositories
- [lmod](https://lmod.readthedocs.io/en/latest/): Module system
- [Bash](https://www.gnu.org/software/bash/)
- [spack](https://spack.io/)
- Docker
- Vagrant

---

## Working remote

- SSH
    - Note that VS Code has SSH support
- tmux
    - Open several terminals (splitting)
    - Reconnect to terminals
    - Reconfigured bindings immediately
- scp: Copy data
- rsync: Copy data, but more powerful

---

## C++

- [clang-format](https://clang.llvm.org/docs/ClangFormat.html): Code formatting
- [valgrind](https://valgrind.org/): Dynamic analysis
    - Memory leak check, memory consumption...
- CMake

---

## Python

- [black](https://pypi.org/project/black/)

---

## Data

- [git-annex]() (sometimes)

Backups/Data

- [borgbackup](https://borgbackup.readthedocs.io/en/stable/)
- [rsnapshot](https://rsnapshot.org/)

---

## Documentation

Self:

- Markdown and mkdocs

Projects:

- Markdown or reStructuredText. What fits better.
- Doxygen (C++) or docstrings (Python)

---

## Remarks

- Customization vs. portability
- Get acquainted to your tools

---

## Further reading

- [Bash/Prompt customization](https://wiki.archlinux.org/title/Bash/Prompt_customization)