# admonitio

> Admonitio is a latin noun which means "to warn" or "to remind".

..a background application that reminds you to stay productive, built
with qt technologies!

at random (or set!) intervals, an event will play to remind you to get back to work!

## tech-stacks

### tools

- **basedpyright** for LSP
- **ruff** for linting and formatting
- **uv** for development environment
- **neovim**, with **astronvim** as the code editor!

### technologies used

- **Python3** as the main programming language
  - **PySide6** as a binding to build the graphical interface
- **Qt** as the main technology used for the graphical interface

## configuring

when launching the application, a graphical interface will appear allowing
you to configure how and what events are played

### intervals

intervals have two options you can set it to:

- fixed interval: events are played at every *user-chosen* minute
- random interval: events are played random intervals (maximum time with no event
is 1 hour)

### events

events have three options you can set it to:

1. audio: plays an audio everytime an event is triggered
2. image: shows an image everytime an event is triggered
3. both: plays an audio and shows an image everytime an event is
triggered

you can replace the audio and image to something of your liking,
or just use the available preset

## running the application

### for users

just head over to the [releases](https://github.com/dumpiez/personal-site/releases) page
and download the executable file!

---

### for developers

#### prerequisites

- python: `3.14` or higher
- uv: `0.13.8` until `0.14.0`
- git: for version control!

#### steps

1. clone the repository!

```sh
git clone https://github.com/dumpiez/admonitio
cd admonitio
```

2. install the dependencies

```sh
uv sync
```

3. run the application

```sh
uv run python -m admonitio.main
```

a new window should appear, where you can configure and start the
application!
