from seleniumbase import SB
from fpdf import FPDF
import os
from PIL import Image

images_folder = "images"

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

with SB(uc=True, test=False, locale_code="en", headless=False) as sb:
    sb.set_window_size(1920, 1080)
    # Define the range of question numbers (update as needed)
    start = 1
    end = 268  # Example values; replace with your start/end values

    # List to store screenshot file paths (order matters)
    screenshot_files = []

    # Base URL for your Searxng instance (replace with your actual URL)
    searxng_url = "https://search.labserver.cloud"

    for q in range(start, end + 1):
        # Build the query
        query = f"\"Exam Cloud Digital Leader topic 1 question {q} discussion\" site:examtopics.com"
        query_text=f"Exam Cloud Digital Leader topic 1 question {q} discussion"
        # Open the Searxng search page
        sb.open(searxng_url)
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
                # Compare the text with the query string exactly
                if link_text == query_text:
                    found = True
                    # Click the link to navigate to the result page
                    a_tag.click()
                    sb.wait(2)  # wait for the page to load
                    break  # Exit loop after finding the matching link

            except Exception as e:
                print(f"Skipping an <h3> element due to error: {e}")
                continue  # If an <h3> doesn't have an <a>, move to the next
        if not found:
            print(f"No matching search result for query '{query}'. Skipping.")
            continue  # Skip to the next question

    # Ensure the 'images' folder exists

        # Now on the result page, wait for the element containing the question
        try:
            sb.wait_for_element("div.discussion-header-container", timeout=10)

            # Screenshot of the question content only
            question_screenshot = f"{images_folder}/screenshot_{q}_question.png"
            sb.save_screenshot(question_screenshot, selector="div.discussion-header-container")
            screenshot_files.append(question_screenshot)

            # Click the "Reveal Solution" button
            sb.click("a.btn.btn-primary.reveal-solution")
            # Wait for any potential changes (e.g. solution becomes visible)
            sb.wait_for_element("div.discussion-header-container", timeout=10)

            sb.execute_script("window.scrollTo(0, 0);")

            # Screenshot of the solution (which is now revealed)
            solution_screenshot =  f"{images_folder}/screenshot_{q}_solution.png"
            sb.save_screenshot(solution_screenshot, selector="div.discussion-header-container")
            screenshot_files.append(solution_screenshot)
        except Exception as e:
            print(f"Error processing question {q}: {e}")

    # Once all screenshots are captured, merge them into a PDF
    pdf = FPDF()
    for image_file in screenshot_files:
        # Get the dimensions of the image
        with Image.open(image_file) as img:
            width, height = img.size
            # Convert pixels to mm (assuming 96 dpi)
            width_mm = width * 25.4 / 96
            height_mm = height * 25.4 / 96
        # Add a new page with the same size as the image
        pdf.add_page(orientation='P' if width_mm < height_mm else 'L')
        pdf.image(image_file, x=0, y=0, w=width_mm, h=height_mm)
    pdf_file = "exam_questions.pdf"
    pdf.output(pdf_file, "F")
    print(f"PDF created: {os.path.abspath(pdf_file)}")
