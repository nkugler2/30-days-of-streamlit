---
id: Day 1 - Setting up a local development environment
aliases:
  - Day 1 - Setting up a local development environment
tags: []
---

# Setting Up a Local Development Environment

## Getting `conda` on my machine

I decided to go with the guides recommendation and use `conda`. I have some familiarity with it from school and personal projects, and also had notes of how to start things up which were helpful. While I stuck with `conda`, I wanted to take a slightly different route and download `conda` to this machine using `homebrew`.

That process was simple with `brew install --cask anaconda`

## Changes to my `~/.zshrc`

I added the following code to my `~/.zshrc`:

```zsh
conda_enable() {
    __conda_setup="$('/opt/homebrew/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/opt/homebrew/anaconda3/etc/profile.d/conda.sh" ]; then
            . "/opt/homebrew/anaconda3/etc/profile.d/conda.sh"
        else
            export PATH="/opt/homebrew/anaconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
}
```

This ensures that `conda` does not activate every time I open my shell. Instead, to use `conda`, I first type `conda_enable` into my terminal. This will show (base) next to the path given in the terminal. From there I can use normal `conda` commands like `activate`, `deactivate`, and manage environments.

## Starting my environment

I decided against using the default given environment name and version. I opted to call my `conda` environment `30-days-of-streamlit` to make it easier to remember what the virtual environment was for. I also used Python 3.13.12 rather than 3.9. Like all great attempts at a tutorial, I have to make a huge change in the beginning so that I can be dumbfounded later when my code doesn't work even though I followed the same steps.

To start the environment, simply run:

```zsh
conda activate 30-days-of-streamlit
```

And run `conda deactivate` to deactivate it.

## Installing Streamlit

Make sure the environment is active before running:

```zsh
pip install streamlit
```

## Launching the Demo Project

In the terminal, run `streamlit hello`
