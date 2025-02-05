import pdfkit

# Set the options for saving PDF
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
}

# Set the URL of the website to save as PDF
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Set the filename for the PDF file
pdf_filename = 'example.pdf'

# Set the path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

# Use pdfkit to save the website as PDF
pdfkit.from_url(url, pdf_filename, options=options, configuration=config)
