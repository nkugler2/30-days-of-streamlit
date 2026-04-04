---
id: Day 2 - Building your first Streamlit app
aliases:
  - Day 2 - Building your first Streamlit app
tags: []
---

# Building your first Streamlit app

## Fire up your IDE

For me, I am using Neovim (by the way).

We will create `streamlit_app.py` to get started.

## Entering your first line of code

Here's how we start off:

```python
import streamlit as st

st.title("Hello World!")
```

## Fire up the command line terminal

We just enter

```zsh
streamlit run streamlit_app.py
```

And for me, it worked!

# But what about everything else that I do because I do too much

## The Obsidivim Problem

I had a miserable time trying to get my obsidian version of neovim going because of a very weird bug where if my cursor was the last character of the line, it would move one column to the left. I completely gave up.

## Getting Conda perfect in my terminal workflow

I made some changes so that I can create new terminal windows in tmux and they will not only be in the same directory, but also the same conda environment.

1. Installed `direnv`: Tmux can see what directory the last terminal window was in, but it can't natively grab the environment
2. Made `~/.config/direnv/direnvrc` to house a function to load conda when direnv sees a `.envrc` in a project directory
3. Made `.envrc` for this project in the root directory, that just says which environment to use

Now, whenever I `cd` (or `z` for `zoxide`) into the 30-days-of-streamlit project or create a new terminal instance in tmux that goes into this project, it will automatically start up the conda environment.

All I need to do to enter the project fully is go `z 30` in my home directory in the terminal, and I get both the right directory and `conda` environment
