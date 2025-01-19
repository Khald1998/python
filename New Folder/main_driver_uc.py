from seleniumbase import Driver
import random
from fake_useragent import UserAgent

def get_random_window_size():
    """Return a random screen resolution from a set of typical sizes."""
    common_sizes = ["1920,1080","1600,900","1366,768","1536,864","1440,900"]
    return random.choice(common_sizes)

prompt = "test"
driver = Driver(uc=True, incognito=True,agent=UserAgent().random)
driver.set_window_size(1000, 800)
# print(get_random_window_size())
url = "https://chatgpt.com"
driver.activate_cdp_mode(url)
driver.sleep(random.uniform(3, 8))
driver.wait_for_element("p.placeholder", timeout=10)
element = driver.find_element("p.placeholder")

# Type each character with a delay
for char in prompt:
    element.send_keys(char)
    driver.sleep(random.uniform(0.1, 0.3))
driver.sleep(random.uniform(1, 5))
element.send_keys("\n")
driver.sleep(random.uniform(1, 5))
driver.quit()
