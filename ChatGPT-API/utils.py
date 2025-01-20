import random
from seleniumbase.common.exceptions import TimeoutException

def get_random_window_size():
    """Return a random screen resolution from a set of typical sizes."""
    common_sizes = [(1920, 1080), (1600, 900), (1366, 768), (1536, 864), (1440, 900)]
    return random.choice(common_sizes)
    
def check_url(url,sb):
    try:
        sb.assert_url(url)
        print(f"Current URL is: {sb.get_current_url()}")
    except Exception as e:
        print(f"URL mismatch: Expected [{url}], but got [{sb.get_current_url()}]")
        exit()  

def find_prompt_area(prompt_area,sb):
    try:
        sb.wait_for_element(prompt_area, timeout=15)
        element = sb.find_element(prompt_area)
        return element
    except TimeoutException:
        print(f"Timeout: The element prompt area [{prompt_area}] was not found within 15 seconds.")
        exit()

def human_like_prompt(element, prompt,sb):
    """Types text in a human-like manner."""
    print(f"The prompt: {prompt}")
    for char in prompt:
        element.send_keys(char)
        sb.sleep(random.uniform(0.1, 0.3))
    sb.sleep(random.uniform(1, 2))
    sb.type('p', "\n")

def wait_for_prompt(element,sb):
    try:
        sb.wait_for_element(element, timeout=120)
    except TimeoutException:
        print(f"Timeout: The element for waiting the prompt output was not found within 120 seconds.")
        exit()
    sb.sleep(random.uniform(1, 2))

def extract_prompt(element,sb):
    input_elements = sb.find_element(element)
    if input_elements:
        result = input_elements.text
        print(result)
        return result