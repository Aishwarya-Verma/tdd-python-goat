from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


options = Options()
options.headless = True     # Run Firefox in headless mode(no GUI)
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    browser.get('http://localhost:8000')
    assert 'Django' in browser.title
    browser.save_screeshot('test_artifacts/trial_scrnsht.png')
    print("Screenshot saved at: test_artifacts/trial_scrnsht.png")

finally:
    browser.quit()
