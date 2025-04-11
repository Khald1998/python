from seleniumbase import SB
from fpdf import FPDF
import os
from PIL import Image
import json

images_folder = "images"

# Load cookies from the JSON file
cookies_file = "search.labserver.cloud_cookies.json"


if not os.path.exists(images_folder):
    os.makedirs(images_folder)

with SB(browser="edge",uc=True, test=False, locale_code="en", headless=False) as sb:
    sb.set_window_size(1920, 1080)
    # Define the range of question numbers (update as needed)
    start = 1
    end = 130  # Example values; replace with your start/end values
    cert = "EX200"
    # List to store screenshot file paths (order matters)
    screenshot_files = []

    # Base URL for your Searxng instance (replace with your actual URL)
    searxng_url = "https://search.labserver.cloud"

    for q in range(start, end + 1):
        sb.sleep(2) # Wait for the screenshots to be saved
        # Print the user agent
        user_agent = sb.execute_script("return navigator.userAgent;")
        print(f"User agent for question {q}: {user_agent}")

        # Build the query
        query = f"\"Exam {cert} topic 1 question {q} discussion\" site:examtopics.com"
        query_text=f"Exam {cert} topic 1 question {q}"
        # Open the Searxng search page
        sb.open(searxng_url)
        sb.load_cookies(name="cookies.txt")
        # Wait for the search box to be present and type the query
        sb.type("input[name='q']", query)
        sb.submit("form")

        # Find all search result <h3> elements
        found = False
        h3_elements = sb.find_elements("h3")  # SeleniumBase method

        for h3 in h3_elements:
            try:
                # Try to find the <a> tag inside the <h3> element
                a_tag = h3.find_element("tag name", "a")
                link_text = a_tag.text.strip()
                # print(a_tag.get_attribute("href"))
                # Compare the text with the query string exactly
                if query_text.replace(" ", "-").lower() in a_tag.get_attribute("href").lower():
                    found = True
                    # Click the link to navigate to the result page
                    a_tag.click()
                    sb.wait(2)  # wait for the page to load
                    break  # Exit loop after finding the matching link

            except Exception as e:
                print(f"Skipping an <h3> element due to error: {e}")
                continue  # If an <h3> doesn't have an <a>, move to the next
        if not found:
            print(f"No matching search result for query '{query_text}'. Skipping.")
            continue  # Skip to the next question

        # Now on the result page, wait for the element containing the question
        try:
            sb.wait_for_element("div.discussion-header-container", timeout=10)

            # Wait for the popup overlay to load
            sb.wait_for_element("div.popup-overlay.show", timeout=10)
            sb.wait(1)  # Wait for the popup to be fully visible
            # Hide the popup overlay by setting its display style to none
            sb.execute_script('document.querySelector("div.popup-overlay.show").style.display = "none";')
            sb.wait(1)  # Wait for the popup to be hidden
            # Screenshot of the question content only
            sb.scroll_to("div.discussion-header-container")  # Scroll to the question
            question_screenshot = f"{images_folder}/screenshot_{q}_question.png"
            sb.save_screenshot(question_screenshot, selector="div.discussion-header-container")
            screenshot_files.append(question_screenshot)

            # Click the "Reveal Solution" button
            sb.click("a.btn.btn-primary.reveal-solution")
            # Wait for any potential changes (e.g. solution becomes visible)
            sb.wait_for_element("div.discussion-header-container", timeout=10)
            sb.wait(1)  # Wait for the solution to be fully visible
            # sb.execute_script("window.scrollTo(0, 0);")
            sb.scroll_to("div.question-answer")  # Scroll to the answer
            sb.wait(1)
            # Screenshot of the solution (which is now revealed)
            solution_screenshot =  f"{images_folder}/screenshot_{q}_solution.png"
            sb.save_screenshot(solution_screenshot, selector="div.question-answer")
            screenshot_files.append(solution_screenshot)
            

        except Exception as e:
            print(f"Error processing question {q}: {e}")
        

from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()

# Define padding in millimeters
padding = 5  # Adjust as needed

for image_file in screenshot_files:
    with Image.open(image_file) as img:
        width, height = img.size
        width_mm = width * 25.4 / 96
        height_mm = height * 25.4 / 96

    page_width = width_mm + 2 * padding
    page_height = height_mm + 2 * padding

    pdf.add_page(format=(page_width, page_height))
    pdf.image(image_file, x=padding, y=padding, w=width_mm, h=height_mm)

pdf_file = f"{cert} exam questions.pdf"
pdf.output(pdf_file, "F")
print(f"PDF created: {os.path.abspath(pdf_file)}")
