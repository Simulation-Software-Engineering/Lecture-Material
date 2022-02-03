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

- Some overview over tools I use commonly
- My opinion/experience

---

## Editor and IDEs

- Current choices
    - [VS Code](https://code.visualstudio.com/)
        - Plenty of addons, powerful feature,
        - Based on Electron (bad?)
    - [VIM](https://www.vim.org/)
        - Plenty of addons, small footprint, special input method
    - [Sublime Text](https://www.sublimetext.com/)
        - Plenty of addons

- Earlier choices: Gedit, NEdit, Emacs, QtCreator...
- Switching editors may impact productivity
- Knowing basics of one CLI-capable editor useful
    - nano, ed, vi, vim, emacs...

---

## Dotfiles

- I (try to) organize my dotfiles
    - [Git repository](https://github.com/ajaust/dotfiles)
- Easy to deploy via Git
- Should be portable
- Configuration files not applicable to a system are usually ignored
- **Warning**: Do not share secrets by accident
- Check out other people's dotfiles

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

## Terminal

- [fzf](https://github.com/junegunn/fzf): A command line fuzzy finder
    - [Fuzzy completion](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh)
- Bash prompt (`PS1`)
    - Show directory
    - Show branch if in a Git repository
- Terminal emulator with UTF-8 support
- Tiling window manager (i3wm, swaywm)

---

## Working remote

- SSH
    - Note that VS Code has SSH support
- tmux
    - Open several terminals (splitting)
    - Reconnect to terminals
    - Reconfigured bindings immediately
- scp: Copy data over network
- rsync: Copy data, but more powerful

---

## SSH

Configure connections in `.ssh/config`

- Configure target with name

  ```text
  Host WorkPC
      HostName 123.123.123.123
      User USERNAME
      IdentityFile ~/.ssh/some-private-key
  ```

- Connect via login server

  ```text
  Host WorkPC
      ProxyCommand ssh -q LoginServerName nc -q0 %h 22
      User USERNAME
      IdentityFile ~/.ssh/some-private-key
      IdentityFile ~/.ssh/another-private-key
  ```

  Connection to `WorkPC` will go via `LoginServerName`

---


## C++

- [clang-format](https://clang.llvm.org/docs/ClangFormat.html): Code formatting
- [valgrind](https://valgrind.org/): Dynamic analysis
    - Memory leak check, memory consumption...
- CMake
- gdb

---

## Python

- [black](https://pypi.org/project/black/)

---

## Documentation

- Markdown or reStructuredText.
    - Whatever fits better.
- mkdocs
- pandoc
- LaTeX
- Doxygen (C++) or docstrings (Python)

---

## Remarks/Tips

- Customization vs. portability
- Get acquainted with your tools

---

## Further reading

- [Bash/Prompt customization](https://wiki.archlinux.org/title/Bash/Prompt_customization)
