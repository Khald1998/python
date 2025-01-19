import time
import random
from fake_useragent import UserAgent
from seleniumbase import BaseCase

class UndetectableBot(BaseCase):
    def test_visit_website(self):
        # Set a random window size
        width = random.randint(1280, 1920)
        height = random.randint(720, 1080)
        self.set_window_size(width, height)

        # Override the User-Agent
        self.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": UserAgent().random})

        # Remove the 'webdriver' property from navigator
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Introduce a random delay to mimic human behavior
        time.sleep(random.uniform(2, 5))

        # Open the target website
        self.open("https://chatgpt.com/")

        # Wait for 10 seconds to observe the loaded page
        time.sleep(10)

if __name__ == "__main__":
    # Initialize the test case
    test_case = UndetectableBot("test_visit_website")

    # Configure test parameters
    test_case.browser = "chrome"  # Specify the browser to use
    test_case.headless = False    # Set to True to run in headless mode
    test_case.uc = True           # Enable undetected-chromedriver mode

    # Set up the test environment
    test_case.setUp()

    try:
        # Execute the test
        test_case.test_visit_website()
    finally:
        # Tear down the test environment
        test_case.tearDown()
