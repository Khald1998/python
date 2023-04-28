


# Code README

This Python code retrieves the content of a Wikipedia article on the Python programming language and extracts the text of all `p` tags within the `div` element with the `id` attribute "bodyContent". 

## Prerequisites
- Python 3.x
- requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)


## Usage
1. Set the `url` variable to the URL of the Wikipedia article you want to retrieve.
2. Run the script using a Python interpreter.
3. The script will print the text content of each `p` tag within the `div` element with the `id` attribute "bodyContent".
4. The script will stop printing when it encounters an `h2` tag with the text content "See also" as its sibling.

## Notes
- This script uses the `requests` library to send a GET request to the specified URL and the `BeautifulSoup` library to parse the HTML content of the response.
- This script assumes that the Wikipedia article has a `div` element with the `id` attribute "bodyContent" containing the main body content of the article.
- This script uses the `find_all` method of the `BeautifulSoup` object to find all `p` tags within the `div` element with the `id` attribute "bodyContent".
- This script uses the `get_text` method of the `Tag` object to extract the text content of each `p` tag.
- This script checks if the sibling of each `p` tag is an `h2` tag with the text content "See also" using the `find_next_sibling` method of the `Tag` object and stops printing if it encounters such a tag.
