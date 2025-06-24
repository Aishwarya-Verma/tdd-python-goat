import shutil
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_firefox():
    print("🦊 Running Firefox test...")
    options = FirefoxOptions()
    options.add_argument("--headless")
    service = FirefoxService(executable_path=shutil.which("geckodriver"))
    driver = webdriver.Firefox(service=service, options=options)
    try:
        driver.get("https://example.com")
        print("✅ Firefox title:", driver.title)
    finally:
        driver.quit()


def test_chrome():
    print("🎯 Running Chrome test...")
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Use system-installed chromedriver (matched to system chromium)
    service = ChromeService(executable_path=shutil.which("chromedriver"))
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://example.com")
        print("✅ Chrome title:", driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_firefox()
    test_chrome()
