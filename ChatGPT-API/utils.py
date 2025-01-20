import random
from seleniumbase.common.exceptions import TimeoutException, NoSuchElementException

def get_random_window_size():
    """Return a random screen resolution from a set of typical sizes."""
    common_sizes = [(1920, 1080), (1600, 900), (1366, 768), (1536, 864), (1440, 900)]
    return random.choice(common_sizes)

def check_url(url, sb):
    try:
        sb.assert_url(url)
        print(f"Current URL is: {sb.get_current_url()}")
        return True, None
    except Exception as e:
        error_message = f"URL mismatch: Expected [{url}], but got [{sb.get_current_url()}]"
        return False, error_message

def find_prompt_area(prompt_area, sb):
    try:
        sb.wait_for_element(prompt_area, timeout=15)
        element = sb.find_element(prompt_area)
        return element, None
    except TimeoutException:
        error_message = f"Timeout: The element prompt area [{prompt_area}] was not found within 15 seconds."
        return None, error_message

def human_like_prompt(element, prompt, sb):
    """Types text in a human-like manner."""
    try:
        print(f"The prompt: {prompt}")
        for char in prompt:
            element.send_keys(char)
            sb.sleep(random.uniform(0.1, 0.3))
        sb.sleep(random.uniform(1, 2))
        sb.type('p', "\n")
        return True, None
    except Exception as e:
        error_message = f"Error during human-like typing: {str(e)}"
        return False, error_message

def wait_for_prompt(element, sb):
    try:
        sb.wait_for_element(element, timeout=120)
        sb.sleep(random.uniform(1, 2))
        return True, None
    except TimeoutException:
        error_message = f"Timeout: The element for waiting the prompt output was not found within 120 seconds."
        return False, error_message

def extract_prompt(element, sb):
    try:
        input_elements = sb.find_element(element)
        if input_elements:
            result = input_elements.text
            print(result)
            return result, None
        else:
            error_message = f"No elements found for extraction with selector [{element}]."
            return None, error_message
    except Exception as e:
        error_message = f"Error during prompt extraction: {str(e)}"
        return None, error_message
