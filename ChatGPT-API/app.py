from seleniumbase import SB
import random
from fake_useragent import UserAgent
from utils import get_random_window_size, check_url, find_prompt_area, human_like_prompt, wait_for_prompt, extract_prompt

def generate_response(prompt):
    with SB(uc=True, test=False, locale_code="en", agent=UserAgent().random, headless=True) as sb:
        width, height, error = get_random_window_size()
        if error:
            return None, error
        sb.set_window_size(width, height)
        url = "https://chatgpt.com/"
        sb.activate_cdp_mode(url)
        sb.sleep(random.uniform(2, 3))

        success, error = check_url(url, sb)
        if not success:
            return None, error

        element, error = find_prompt_area("p.placeholder", sb)
        if error:
            return None, error

        success, error = human_like_prompt(element, prompt, sb)
        if not success:
            return None, error

        success, error = wait_for_prompt('//button[@aria-label="Send prompt"]', sb)
        if not success:
            return None, error

        response, error = extract_prompt("div.markdown", sb)
        if error:
            return None, error

        return response, None
