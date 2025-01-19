from seleniumbase import SB
import random
from fake_useragent import UserAgent
from seleniumbase.common.exceptions import TimeoutException, NoSuchElementException

def get_random_window_size():
    """Return a random screen resolution from a set of typical sizes."""
    common_sizes = ["1920,1080", "1600,900", "1366,768", "1536,864", "1440,900"]
    return random.choice(common_sizes)

prompt = "what is love"

with SB(uc=True, test=False, locale_code="en", agent=UserAgent().random, headless=False) as sb:
    sb.set_window_size(1000, 800)
    url = "https://chatgpt.com/"
    sb.activate_cdp_mode(url)
    
    sb.sleep(random.uniform(1, 2))
    try:
        sb.assert_url(url)
    except Exception as e:
        print(f"URL mismatch: Expected [{url}], but got [{sb.get_current_url()}]")
        exit()  


    try:
        text_area = "p.placeholder"
        sb.wait_for_element(text_area, timeout=15)
        element = sb.find_element(text_area)
    except TimeoutException:
        print(f"Timeout: The element [{text_area}] was not found within 15 seconds.")
        exit()



    # Type each character with a delay
    for char in prompt:
        element.send_keys(char)
        sb.sleep(random.uniform(0.1, 0.3))

    sb.sleep(random.uniform(1, 5))
    sb.type('p', "\n")
    sb.sleep(random.uniform(1, 5))
    sb.sleep(random.uniform(2, 6))
    sb.wait_for_element('//button[@aria-label="Send prompt"]', timeout=15)
    sb.sleep(random.uniform(2, 6))

    input_elements = sb.find_element("div.markdown")

    sb.sleep(random.uniform(2, 6))
    # Extract text from elements and get only the first element
    if input_elements:
        result = input_elements.text
        print(result)
