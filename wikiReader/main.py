import requests
from bs4 import BeautifulSoup

# The URL of the Wikipedia article
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object using the content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with class "mw-parser-output"
mw_parser_output_div = soup.find('div', {'id': 'bodyContent'})
# print(mw_parser_output_div)


# Find all p tags inside the div
p_tags = mw_parser_output_div.find_all('p')

# Print the text content of each p tag
for p in p_tags:
    print(p.get_text())

    # Check if the p tag's parent sibling is an h2 tag with "See also" as its text content
    next_sibling = p.find_next_sibling()
    if next_sibling and next_sibling.name == 'h2' and next_sibling.get_text() == 'See also':
        break