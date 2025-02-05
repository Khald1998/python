This Python script demonstrates how to convert a webpage into a PDF using pdfkit and wkhtmltopdf.

## Requirements
- Python 3
- pdfkit
- wkhtmltopdf

Install **pdfkit**:
```
pip install pdfkit
```

Download and install **wkhtmltopdf** from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html).  
Make sure the **wkhtmltopdf** executable path is set correctly in your code.

## How It Works
1. It sets up PDF output options (page size, margins, encoding).
2. It points to the URL you want to save as PDF.
3. It specifies the path to the **wkhtmltopdf** executable.
4. Finally, it uses `pdfkit.from_url()` to generate a PDF of the webpage.

## Usage
1. Update the script with the correct path to `wkhtmltopdf` if needed.
2. Run the script:
   ```
   python script.py
   ```
3. The PDF (`example.pdf`) will be generated in the same directory as the script.
