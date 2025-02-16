# Exam Topics Extractor

This project automates the process of extracting exam questions and solutions from the ExamTopics website and compiles them into a PDF document.

## Prerequisites

- Python 3.x
- SeleniumBase
- Pillow
- fpdf

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/examtopics-extractor.git
    cd examtopics-extractor
    ```

2. Install the required Python packages:

    ```sh
    pip install seleniumbase Pillow fpdf
    ```

## Usage

1. Update the [main.py](http://_vscodecontentref_/0) file with the desired range of question numbers and certification name.

2. Run the script:

    ```sh
    python main.py
    ```

3. The script will generate screenshots of the questions and solutions, and compile them into a PDF file named `Cloud Digital Leader exam questions.pdf`.

## Project Structure

- [main.py](http://_vscodecontentref_/1): The main script that performs the extraction and PDF generation.
- [images](http://_vscodecontentref_/2): Directory where the screenshots are saved.
- `Cloud Digital Leader exam questions.pdf`: The generated PDF file containing the exam questions and solutions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.