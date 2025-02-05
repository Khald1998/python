# Python Projects

This repository contains several small Python projects, each demonstrating different functionalities and libraries.

## Table of Contents

- [ChatGPT API](#chatgpt-api)
- [Gif Creator](#gif-creator)
- [Web to PDF](#web-to-pdf)
- [Wikipedia Python Scraper](#wikipedia-python-scraper)

## ChatGPT API

A simple API to interact with ChatGPT using SeleniumBase for web automation. The API is built using Flask.

### Requirements

- Python 3.x
- Flask
- SeleniumBase
- Fake UserAgent

### Usage

1. Run the Flask API:
    ```sh
    python ChatGPT-API/api.py
    ```

2. Send a GET request to the `/gpt` endpoint with a [prompt](http://_vscodecontentref_/0) parameter:
    ```sh
    curl "http://127.0.0.1:5000/gpt?prompt=Hello"
    ```

## Gif Creator

A Python project that converts video files into GIFs using the [moviepy](http://_vscodecontentref_/1) library.

### Requirements

- Python 3.x
- moviepy

### Usage

1. Update [video_path](http://_vscodecontentref_/2) and [output_path](http://_vscodecontentref_/3) in [main.py](http://_vscodecontentref_/4).
2. Run the script:
    ```sh
    python Gif-Creator/main.py
    ```

## Web to PDF

A Python script to convert a webpage into a PDF using pdfkit and wkhtmltopdf.

### Requirements

- Python 3
- pdfkit
- wkhtmltopdf

### Usage

1. Update the script with the correct path to [wkhtmltopdf](http://_vscodecontentref_/5) if needed.
2. Run the script:
    ```sh
    python web-to-PDF/main.py
    ```

## Wikipedia Python Scraper

A Python script to scrape the Wikipedia article on "Python (programming language)" using Requests and BeautifulSoup.

### Requirements

- Python 3
- Requests
- BeautifulSoup

### Usage

1. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4
    ```
2. Run the script:
    ```sh
    python wikiReader/main.py
    ```

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.