# Python Projects

This repository contains several small Python projects, each demonstrating different functionalities and libraries. Below is a brief overview of each project.

## Table of Contents

- [ChatGPT API](#chatgpt-api)
- [Gif Creator](#gif-creator)
- [Web to PDF](#web-to-pdf)
- [Wikipedia Python Scraper](#wikipedia-python-scraper)

## ChatGPT API

This project provides a simple API to interact with ChatGPT using SeleniumBase for web automation. The API is built using Flask and can be used to generate responses from ChatGPT.

### Project Structure

- `api.py`: Contains the Flask API implementation.
- `app.py`: Contains the main logic to interact with ChatGPT using SeleniumBase.
- `utils.py`: Contains utility functions used in `app.py`.
- `downloaded_files/`: Directory for lock files.

### Requirements

- Python 3.x
- Flask
- SeleniumBase
- Fake UserAgent

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ChatGPT-API.git
    cd ChatGPT-API
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask API:
    ```sh
    python api.py
    ```

2. Send a GET request to the `/gpt` endpoint with a [prompt](http://_vscodecontentref_/0) parameter:
    ```sh
    curl "http://127.0.0.1:5000/gpt?prompt=Hello"
    ```

## Gif Creator

Gif-Creator is a simple Python project that converts video files into GIFs using the [moviepy](http://_vscodecontentref_/1) library.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Gif-Creator.git
    cd Gif-Creator
    ```

2. Install the required dependencies:
    ```sh
    pip install moviepy
    ```

### Usage

1. Replace the [video_path](http://_vscodecontentref_/2) variable in [main.py](http://_vscodecontentref_/3) with the path to your video file.
2. Replace the [output_path](http://_vscodecontentref_/4) variable in [main.py](http://_vscodecontentref_/5) with the desired path for the output GIF.
3. Run the script:
    ```sh
    python main.py
    ```

## Web to PDF

This Python script demonstrates how to convert a webpage into a PDF using pdfkit and wkhtmltopdf.

### Requirements

- Python 3
- pdfkit
- wkhtmltopdf

### Installation

1. Install **pdfkit**:
    ```sh
    pip install pdfkit
    ```

2. Download and install **wkhtmltopdf** from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html).  
   Make sure the **wkhtmltopdf** executable path is set correctly in your code.

### Usage

1. Update the script with the correct path to [wkhtmltopdf](http://_vscodecontentref_/6) if needed.
2. Run the script:
    ```sh
    python main.py
    ```

3. The PDF (`example.pdf`) will be generated in the same directory as the script.

## Wikipedia Python Scraper

This Python script demonstrates a simple web scraping approach using [Requests](https://pypi.org/project/requests/) and [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). It fetches the Wikipedia article on "Python (programming language)," finds the main content, and prints out the text from each paragraph (`<p>` tag) until it reaches a heading with the text "See also."

### Requirements

- [Python 3](https://www.python.org/downloads/)
- [Requests library](https://pypi.org/project/requests/)
- [BeautifulSoup library](https://pypi.org/project/beautifulsoup4/)

### Installation

Install the required libraries via:
```bash
pip install requests beautifulsoup4
```
### License
This repository is licensed under the MIT License. See the LICENSE file for more information.


