from urllib.parse import urlparse
import random
import string
import time
from fake_useragent import UserAgent

def generate_random_string(length=8):
    # Randomly select letters and digits
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def get_domain(url):
    """This function returns the domain without the path."""
    parsed_url = urlparse(url)
    return parsed_url.netloc

def is_auth(driver,auth_url):
    """This function returns the domain without the path."""
    url = get_domain(driver.get_current_url())
    return url==auth_url

def get_random_user_agent():
    """Returns a random User-Agent string."""
    ua = UserAgent()
    return ua.random

def human_like_typing(element, text):
    """Types text in a human-like manner."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

def do_auth(email, password, driver):
    """This function will perform the authentication steps."""
    driver.wait_for_element("tag name", "button", timeout=60)
    time.sleep(random.uniform(2, 6))
    login_button = driver.find_element("tag name", "button")
    login_button.click()  # Use uc_click for stealthy interaction

    # Wait for the login elements and enter credentials
    driver.wait_for_element("class name", "email-input", timeout=60)
    time.sleep(random.uniform(2, 6))
    email_space = driver.find_element("class name", "email-input")
    human_like_typing(email_space, email)
    # email_space.send_keys(email)
    time.sleep(random.uniform(2, 6))
    email_button = driver.find_element("tag name", "button")
    email_button.click()  # Use uc_click for stealthy interaction

    driver.wait_for_element_visible("class name", "input", timeout=60)
    time.sleep(random.uniform(2, 6))
    password_space = driver.find_element("class name", "input")
    human_like_typing(password_space,password)
    # password_space.send_keys(password)
    password_button = driver.find_element("class name", "_button-login-password")
    password_button.click()  # Use uc_click for stealthy interaction
    time.sleep(random.uniform(2, 6))



def do_prompt(driver,Keys,prompt,is_loged):
    # Find input elements by class name
    driver.wait_for_element("class name", "placeholder", timeout=60)
    time.sleep(random.uniform(1, 4))
    input_element = driver.find_element("class name", "placeholder")
    if input_element:
        human_like_typing(input_element,prompt)
        # input_element.send_keys(prompt)
        time.sleep(random.uniform(2, 6))
        input_element.send_keys(Keys.ENTER)
        time.sleep(random.uniform(2, 6))
        if is_loged:
            driver.wait_for_element('//button[@aria-label="Start voice mode"]', timeout=60)
        else:
            driver.wait_for_element('//button[@aria-label="Send prompt"]', timeout=60) 
        time.sleep(random.uniform(2, 6))

    # Find input elements by tag name "p"
    input_elements = driver.find_element("class name", "markdown.prose")

    time.sleep(random.uniform(2, 6))
    # Extract text from elements and get only the first element
    if input_elements:
        result = input_elements.text
        print(result)

def do_prompt_test(driver,prompt):
    # Find input elements by class name
    driver.wait_for_element("class name", "placeholder", timeout=15)
    time.sleep(random.uniform(1, 4))
    input_element = driver.find_element("class name", "placeholder")
    if input_element:
        human_like_typing(input_element,prompt)
        time.sleep(random.uniform(2, 6))
        input_element.send_keys("\n")
        time.sleep(random.uniform(2, 6))
        driver.wait_for_element('//button[@aria-label="Send prompt"]', timeout=15) 
        time.sleep(random.uniform(2, 6))

    # Find input elements by tag name "p"
    input_elements = driver.find_element("class name", "markdown.prose")

    time.sleep(random.uniform(2, 6))
    # Extract text from elements and get only the first element
    if input_elements:
        result = input_elements.text
        print(result)