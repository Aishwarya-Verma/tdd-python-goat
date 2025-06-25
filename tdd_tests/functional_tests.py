import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import shutil
from selenium.common.exceptions import WebDriverException
import sys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        print("🧨 SetUp: Running test in Firefox")
        self.options = FirefoxOptions()
        self.options.add_argument("--headless")
        self.service = FirefoxService(executable_path=shutil.which("geckodriver"))
        self.browser = webdriver.Firefox(service=self.service, options=self.options)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self. assertIn("To-Do", self.browser.title)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # She types "Buy peacock feathers" into a text box
        # Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        #Satisfied, she goes back to sleep

        print("✅ OK")


if __name__ == "__main__":
    unittest.main()
