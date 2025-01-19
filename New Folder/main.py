from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from utils import do_auth,is_auth,do_prompt,generate_random_string,get_random_user_agent
import time
import random

# Load environment variables
load_dotenv()

# Initialize the Driver with UC mode enabled
driver = Driver(uc=True)

# prompt = "write long store about bigfoot"
prompt = generate_random_string(12)
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
auth_url = "auth.openai.com"
app_url = "chatgpt.com/"
need_auth = False
try:

    user_agent = get_random_user_agent()
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent},)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Open the specified URL
    driver.get(f"https://{app_url}")
    print(driver.get_current_url())

    # Wait for the page to load and check URL for next step.
    time.sleep(random.uniform(1, 5))

    need_auth = is_auth(driver,auth_url)
    print(need_auth)

    if need_auth:
        do_auth(email, password, driver)
        do_prompt(driver,Keys,prompt,need_auth)
    else:
        do_prompt(driver,Keys,prompt,need_auth)


finally:
    # Ensure the browser is closed after operations
    driver.quit()


