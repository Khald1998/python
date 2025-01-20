from seleniumbase import SB
import random
from fake_useragent import UserAgent
from utils import get_random_window_size,check_url,find_prompt_area,human_like_prompt,wait_for_prompt,extract_prompt

prompt = "say something random"

with SB(uc=True, test=False, locale_code="en", agent=UserAgent().random, headless=True) as sb:
    width, height = get_random_window_size()
    sb.set_window_size(width, height)
    url = "https://chatgpt.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(random.uniform(2, 3))

    check_url(url,sb)
    element=find_prompt_area("p.placeholder",sb)
    human_like_prompt(element,prompt,sb)
    wait_for_prompt('//button[@aria-label="Send prompt"]',sb)
    respons = extract_prompt("div.markdown",sb)


