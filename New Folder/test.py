# from seleniumbase import SB
# import random
# from fake_useragent import UserAgent

# def get_random_user_agent():
#     """Returns a random User-Agent string."""
#     ua = UserAgent()
#     return ua.random

# with SB(uc=True) as sb:
#     # Set Chrome options to avoid detection
#     user_agent = get_random_user_agent()
#     sb.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
#     sb.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

#     url = "https://chat.openai.com"  # Change this to your target website
#     sb.open(url)
#     sb.sleep(random.uniform(2, 4))

#     print("Successfully bypassed bot detection!")
    
from seleniumbase import Driver
import random
from fake_useragent import UserAgent
import time

def get_random_user_agent():
    """Returns a random User-Agent string."""
    ua = UserAgent()
    return ua.random

# Initialize the Driver instance with undetected-chromedriver (uc) mode
driver = Driver(uc=True)

try:
    # Set Chrome options to avoid detection
    user_agent = get_random_user_agent()
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    url = "https://chat.openai.com"  # Change this to your target website
    driver.get(url)
    time.sleep(random.uniform(2, 4))

    print("Successfully bypassed bot detection!")
finally:
    # Ensure the browser is closed properly
    driver.quit()

