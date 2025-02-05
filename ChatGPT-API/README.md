# ChatGPT API

This project provides a simple API to interact with ChatGPT using SeleniumBase for web automation. The API is built using Flask and can be used to generate responses from ChatGPT.

## Project Structure

- `api.py`: Contains the Flask API implementation.
- `app.py`: Contains the main logic to interact with ChatGPT using SeleniumBase.
- `utils.py`: Contains utility functions used in `app.py`.
- `downloaded_files/`: Directory for lock files.

## Requirements

- Python 3.x
- Flask
- SeleniumBase
- Fake UserAgent

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ChatGPT-API.git
    cd ChatGPT-API
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask API:
    ```sh
    python api.py
    ```

2. Send a GET request to the `/gpt` endpoint with a [prompt](http://_vscodecontentref_/5) parameter:
    ```sh
    curl "http://127.0.0.1:5000/gpt?prompt=Hello"
    ```

## Functions

### [utils.py](http://_vscodecontentref_/6)

- [get_random_window_size()](http://_vscodecontentref_/7): Returns a random screen resolution from a set of typical sizes.
- [check_url(url, sb)](http://_vscodecontentref_/8): Checks if the current URL matches the expected URL.
- [find_prompt_area(prompt_area, sb)](http://_vscodecontentref_/9): Finds the prompt area element on the page.
- [human_like_prompt(element, prompt, sb)](http://_vscodecontentref_/10): Types text in a human-like manner.
- [wait_for_prompt(element, sb)](http://_vscodecontentref_/11): Waits for the prompt output element to appear.
- [extract_prompt(element, sb)](http://_vscodecontentref_/12): Extracts the text from the prompt output element.

### [app.py](http://_vscodecontentref_/13)

- [generate_response(prompt)](http://_vscodecontentref_/14): Generates a response from ChatGPT for the given prompt.

### [api.py](http://_vscodecontentref_/15)

- Flask API with a single endpoint `/gpt` to generate responses from ChatGPT.

## License

This project is licensed under the MIT License.