# 🚀 Quick Start (in Codespaces)
- Open this repo in GitHub Codespaces
- GitHub will automatically build and start the development container.

---
## Run the tests
- Inside the Codespace terminal:
    - File: basic_selenium_sanity_test.py
    - This script uses Selenium to run browser tests in both Firefox and Chrome using headless mode.

```sh
python3 basic_selenium_sanity_test.py
```

- You'll see Firefox and Chrome tests running headlessly and printing page titles from https://example.com.

``` sh
Example output:

🦊 Running Firefox test...
✅ Firefox title: Example Domain
🎯 Running Chrome test...
✅ Chrome title: Example Domain
```

---
### 🔍 Browser Support
- Firefox (via geckodriver)
- Chrome (via chromedriver and Chromium)
- Both are installed in the container and run using Xvfb (virtual framebuffer) for GUI-less environments.

---
- **Book**: Test-Driven Development with Python
- **Author**: Harry J.W. Percival
- **Publisher**: O’Reilly Media

- 🤖 Big thanks to **ChatGPT** by **OpenAI** for making the setup smoother, docs clearer, and TDD a little more fun!
---
## 📄 License and Use
This repository is for educational and demonstration purposes only.

✅ Personal learning

❌ No redistribution, modification, or reuse without permission

**All rights reserved**