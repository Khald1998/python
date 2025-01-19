from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from utils import is_auth, do_prompt, generate_random_string, get_random_user_agent
import time
import random

class GPTUndetectableAPI(BaseCase):
    def test_chatgpt_free_api(self):
        # Load environment variables
        auth_url = "auth.openai.com"
        app_url = "chatgpt.com/"
        prompt = generate_random_string(12)

        try:
            # Set a random user agent
            user_agent = get_random_user_agent()
            self.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
            self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            # Open the specified URL
            self.open(f"https://{app_url}")
            print(self.get_current_url())

            # Wait for the page to load
            time.sleep(random.uniform(1, 5))

            # Check if authentication is needed
            need_auth = is_auth(self, auth_url)
            print(need_auth)
            do_prompt(self, Keys, prompt, need_auth)
            time.sleep(10)
        finally:
            print('done')

if __name__ == "__main__":
    from seleniumbase import BaseCase
    BaseCase.main(__name__, __file__)
