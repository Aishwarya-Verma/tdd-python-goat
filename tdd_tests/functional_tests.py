from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import shutil
from selenium.common.exceptions import WebDriverException
import sys


print("🧨 Running test in Firefox")

options = FirefoxOptions()
options.add_argument("--headless")

service = FirefoxService(executable_path=shutil.which("geckodriver"))

browser = webdriver.Firefox(service=service, options=options)

try:
    browser.get("http://localhost:8000")
    assert "Congratulations!" in browser.title
    print("✅ OK")
except WebDriverException as e:
    print("\n💥 Could not connect to the webdriver. Is it running on http://localhost:8000?")
    print(f"Error: {e.msg}")
    sys.exit(1)
except AssertionError:
    print("\n❌ Test failed: 'Congratulations!' not found in page title.")
    print(f"Page title was: {browser.title}")
    sys.exit(1)
finally:
    browser.quit()
