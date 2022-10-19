# Demo: Tools (Alex)


## VS Code

[SSH support](https://code.visualstudio.com/docs/remote/ssh)

- Start VS Code
- CTRL-P -> Connect to host -> neon
- Check terminal output
    - On first connection some software will be installed on the remote
- Open new terminal. Show that hostname is different.
    - Can also be seen at bottom left. Should say `SSH: neon`
- I can install tools on the remote now
- One could connect to a VM, container etc. if one wants to.

## Dotfiles

- Show <https://github.com/ajaust/dotfiles>
- Configuration files for a variety of software
- Config of command prompt

  ```text
  export PS1="\[\033[0;32m\]\u\[\033[0;36m\]@\h:\w\[\033[0;32m\]\$(__git_ps1)\n└─(\[\033[1;32m\]\t    , \$(ls -1 | wc -l | sed 's: ::g') files, \$(ls -sh | head -n1 | sed 's/total //')b\[\033[1;37m\]\[\    033[0;32m\])\342\224\200>\[\033[0m\] "
  ```

  In a normal directory in gives:

  ```text
  jaustar@lapsgs24:~
  └─(12:43:29, 58 files, 336Kb)─>
  ```

  In a git repository:

  ```text
  jaustar@lapsgs24:~/dotfiles (master)
  └─(13:05:11, 26 files, 104Kb)─>
  ```

## tmux

- Connect to `helium`
    - Open `tmux` window
    - Split window vertically and horizontally (`CTRL |` and `CTRL -`)
    - Leave tmux (`CTRL A` then `D`)
- Disconnect from `helium`
- Reconnect to `helium`
    - Check tmux sessions `tmux ls`
    - Reconnect to existing tmux session `tmux a -t TARGET`

