from seleniumbase import Driver
import random
prompt = "test"
driver = Driver(uc=False)
url = "https://chatgpt.com"
driver.open(url)

# Retrieve and print the current User-Agent
current_user_agent = driver.get_user_agent()
print(f"Current User-Agent: {current_user_agent}")

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
