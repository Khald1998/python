# Wikipedia Python Scraper

This Python script demonstrates a simple web scraping approach using [Requests](https://pypi.org/project/requests/) and [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). It fetches the Wikipedia article on "Python (programming language)," finds the main content, and prints out the text from each paragraph (`<p>` tag) until it reaches a heading with the text "See also."

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Requests library](https://pypi.org/project/requests/)
- [BeautifulSoup library](https://pypi.org/project/beautifulsoup4/)

You can install the required libraries via:
```bash
pip install requests beautifulsoup4
```

## How It Works
1. The script sends an HTTP GET request to the Wikipedia page for Python.
2. It then uses BeautifulSoup to parse the HTML content.
3. It locates the main content section (`div` with `id="bodyContent"`).
4. It finds all `<p>` tags and prints their text content.
5. The script stops printing when it encounters a sibling `<h2>` tag with the text "See also."

## How to Use
1. Download or clone this script.
2. Ensure you have installed the required dependencies.
3. Run the script:
   ```bash
   python script.py
   ```
4. You will see the paragraph texts from the Wikipedia article in your console until the "See also" heading is reached.
