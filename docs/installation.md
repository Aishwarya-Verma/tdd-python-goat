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
