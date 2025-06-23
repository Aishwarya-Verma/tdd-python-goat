# 🛠️ INSTALLATION.md

## ✅ Initial Project Setup

- [x] Created public GitHub repository
- [x] Added custom LICENSE (All rights reserved, no redistribution)
- [x] Added `.github/CODEOWNERS` with self as sole code owner
- [x] Protected `main` branch with:
  - Require pull request before merging
  - Require code owner approval
  - Prevent deletion (lock enabled)
- [x] Set up GitHub Codespaces as primary dev environment

---

## 🐍 Dev Container Configuration

- [x] Used base image: `python:3.12-bullseye`
- [x] Added features:
  - `coverage-py`
- [x] Installed on container create:
  - `Django==5.2.3`
  - `Selenium==4.33`
  - `pytest`
- [x] Added VS Code extensions:
  - Spell checker (`streetsidesoftware.code-spell-checker`)
- [x] Verified `requirements.txt` installed successfully
- [x] Tested `pip`, Python version, and container rebuild

---

## Notes

- This project is being built for learning purposes only while following *TDD with Python* by Harry Percival.
- All code is original unless explicitly copied for educational exercise.


---
## Acknowledgements

- Why do you need extra system libraries for Firefox in Docker, but not on your local machine?
  - On your local machine, you already have many system libraries and GUI components installed as part of your operating system (like Windows, macOS, or a full Linux desktop). So when you run Firefox or Selenium, Firefox finds all the libraries it needs.
  - But inside a Docker container, you start from a very minimal Linux image. By default, it’s just the bare minimum OS libraries, no graphical environment, no extra GUI libraries, no audio support — just enough to run command-line tools.
- What does Firefox need to run even in headless mode?
  - Firefox is a full graphical browser. Even in headless mode (no visible window), it:
    - Still uses GUI libraries to draw the pages.
    - Loads fonts to render text.
    - Uses audio libraries for media.
    - Uses security libraries for HTTPS and certificates.
    - Uses system libraries to interact with Linux's graphics stack, even if it doesn’t display them.

---
- Explanation of key libraries you install and why:

|Library	|What it does / Why Firefox needs it	|Local machine vs Docker container
|---|---|---|
|libgtk-3-0	|GUI toolkit Firefox uses to render its windows and widgets	|Installed on desktop OS by default; not in minimal containers|
|libdbus-glib-1-2	|Communication system for Linux apps (IPC, signals, services)	|Usually present on full OS, missing in containers|
|libxt6	|X Toolkit Intrinsics — core GUI rendering components	|Needed for GUI even headless|
|libx11-xcb1	|Interface to the X Window system (Linux GUI server)|	Your laptop has X server; container doesn’t|
|libxcomposite1	|Supports compositing windows (drawing window contents offscreen)|	Needed for Firefox offscreen rendering|
|libxdamage1	|Tracks screen damage/redraw regions — helps efficient rendering	|Helps Firefox redraw only changed parts|
|libxfixes3	|Fixes/extensions to X11 for improved GUI behavior	|Necessary for stable GUI drawing|
|libxrandr2	|Supports screen resizing and rotation|	Needed for rendering, even if no real screen|
|libxss1|	Screen saver extension — manages power-saving/locking	|Prevents Firefox from “thinking” display is inactive|
|libasound2	|ALSA audio library — audio system	|Needed to avoid crashes when audio subsystems initialized|
|libnss3|	Network Security Services — SSL/TLS support	|Firefox won’t connect to HTTPS sites without this|
|libgl1	|OpenGL library — hardware-accelerated graphics rendering	|Needed for some rendering paths in Firefox|
|libegl1	|Interface between graphics APIs and windowing systems	|Supports rendering pipelines|
|libfontconfig1	|Font configuration and customization	|Ensures text renders correctly|
|xauth	|Manages X server authentication tokens	|Needed if using virtual X servers like xvfb|
|xvfb	|Virtual Frame Buffer: simulates an X11 server without a physical display	|Provides a “fake” GUI environment headless Firefox can use|

### TL;DR:
- On your local machine, all these libraries are already installed by your OS or GUI environment.
- In a minimal Docker container, you must explicitly install all these underlying GUI and system libraries because the container starts almost empty.
- Firefox needs these to work even when running in headless mode, since it still uses the graphics stack internally.
- If you want an analogy:
  - Your local machine is a fully furnished house with everything pre-installed.
  - A Docker container is an empty apartment where you have to bring all your furniture and utilities before living.
  - You’re installing the “utilities” (libgtk, libnss, etc.) so Firefox can run inside the container.
