# ------------- sourcing -:::----------

source <(fzf --zsh)

# ------------ env vars ------------
set -o vi
zle_highlight=('paste:none')

export EDITOR=nvim
export VISUAL=nvim

export BROWSER="brave"

export XDG_CONFIG_HOME=~/.config
export ZDOTDIR=~/.config/zsh/

# ------------ history -------------

HISTFILE=$ZDOTDIR/.zsh_history
HISTSIZE=100000
SAVEHIST=100000

setopt HIST_IGNORE_SPACE # don't save starting with space
setopt HIST_IGNORE_DUPS  # don't save duplicate lines
setopt SHARE_HISTORY     # share between sessions

# ------------ prompt --------------

fpath+=($ZDOTDIR/pure)

autoload -U promptinit; promptinit

PURE_PROMPT_SYMBOL='::'
PURE_PROMPT_VICMD_SYMBOL=':N:'

zstyle :prompt:pure:path color green
zstyle :prompt:pure:git:stash show yes
zstyle ':prompt:pure:prompt:*' color red

prompt pure

# ----------- completion -----------

fpath+=($HOME/.zsh/.zfunc)

autoload -Uz compinit
compinit -u

zstyle ':completion:*' menu select


#------------ aliases --------------
alias vim='nvim'
alias la='ls -lah --color=auto'
alias ls='ls --color=auto'
alias ff='fastfetch'
alias clock='tty-clock'
alias c='clear'
alias hc='nvim $HOME/.config/hypr/hyprland.conf'

# Created by `pipx` on 2025-06-24 07:59:02
export PATH="$PATH:/home/bear/.local/bin"
