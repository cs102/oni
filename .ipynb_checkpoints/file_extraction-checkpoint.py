# 1. Install required libraries
# 2. Import libraties
import PyPDF2
#import pdfpumbler 
import pandas as pd

# 2. Define file path
file_path = 'one.pdf'

# 3. Read PDF by PyPDF2

with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(f"Number of pages: {len(reader.pages)}")
    page = reader.pages[0]
    text = page.extract_text()
    print("Text from PyPDF2\n", text)
