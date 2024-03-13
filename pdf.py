import PyPDF2

def pdf_extractor(file_path):
    extracted_text = ""
    with open(file_path, 'rb') as f:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(f)
        
        # Iterate through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
    
    return extracted_text

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor(file_path)
print(extracted_text)


import PyPDF2
from pdfminer.high_level import extract_text

def pdf_extractor_pdfminer(file_path):
    extracted_text = extract_text(file_path)
    return extracted_text

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor_pdfminer(file_path)
print(extracted_text)


import PyPDF2
import textract

def pdf_extractor_textract(file_path):
    extracted_text = textract.process(file_path)
    return extracted_text.decode("utf-8")

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor_textract(file_path)
print(extracted_text)


import PyPDF2
import fitz

def pdf_extractor_pymupdf(file_path):
    extracted_text = ""
    with fitz.open(file_path) as pdf_document:
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            extracted_text += page.get_text()
    return extracted_text

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor_pymupdf(file_path)
print(extracted_text)

import PyPDF2
import pdfplumber

def pdf_extractor_pdfplumber(file_path):
    extracted_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()
    return extracted_text

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor_pdfplumber(file_path)
print(extracted_text)


import PyPDF2
import camelot

def pdf_extractor_camelot(file_path):
    tables = camelot.read_pdf(file_path)
    extracted_text = ""
    for table in tables:
        extracted_text += table.df.to_string()
    return extracted_text

# Example usage:
file_path = "Amudhan Resume.pdf"  # Replace with the path to your PDF file
extracted_text = pdf_extractor_camelot(file_path)
print(extracted_text)
