from seleniumbase import BaseCase
import time
import random
from fake_useragent import UserAgent
prompt = "test"

class UndetectableBot(BaseCase):
    def test_visit_website(self):
        width = random.randint(1280, 1920)
        height = random.randint(720, 1080)
        self.set_window_size(width, height)
        self.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": UserAgent().random})
        self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        time.sleep(random.uniform(2, 5))
        self.open("https://chatgpt.com/")
        time.sleep(10)
        # self.wait_for_element("class name", "placeholder", timeout=15)
        # time.sleep(random.uniform(2, 5))
        # input_field = self.find_element("class name", "placeholder")
        # for char in prompt:
        #     self.type(input_field, char)
        #     time.sleep(random.uniform(0.1, 0.3))
        # time.sleep(random.uniform(2, 5))
        # self.type(input_field, "\n")
        # time.sleep(random.uniform(2, 5))
        
        # input_element = self.find_element("class name", "placeholder")
        # if input_element:
        #     human_like_typing(input_element,prompt)
        #     time.sleep(random.uniform(2, 6))
        #     input_element.send_keys("\n")
        #     time.sleep(random.uniform(2, 6))
        #     driver.wait_for_element('//button[@aria-label="Send prompt"]', timeout=15) 
        #     time.sleep(random.uniform(2, 6))

        # # Find input elements by tag name "p"
        # input_elements = driver.find_element("class name", "markdown.prose")

        # time.sleep(random.uniform(2, 6))
        # # Extract text from elements and get only the first element
        # if input_elements:
        #     result = input_elements.text
        #     print(result)