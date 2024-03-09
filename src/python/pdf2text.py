# import fitz  # PyMuPDF
# import os

# def pdfs_to_text(folder_path, output_file):
#     with open(output_file, 'w') as out_file:
#         for filename in os.listdir(folder_path):
#             if filename.endswith('.pdf'):
#                 pdf_path = os.path.join(folder_path, filename)
#                 pdf_document = fitz.open(pdf_path)
#                 for page in pdf_document:
#                     text = page.get_text()
#                     out_file.write(text)
#                 pdf_document.close()

# # Example usage:
# pdfs_to_text('/Users/farshid/Library/CloudStorage/OneDrive-Personal/Personal/9_Reference/farshid', 'output_text_file.txt')
# brew install tesseract
# brew info tesseract

import fitz  # PyMuPDF
import os
from PIL import Image
import pytesseract
import io
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def pdf_to_text_with_ocr_recursive(base_folder_path, output_file):    
    with open(output_file, 'w') as out_file:
        for root, dirs, files in os.walk(base_folder_path):
            for filename in files:
                if filename.endswith('.pdf'):
                    pdf_path = os.path.join(root, filename)
                    pdf_document = fitz.open(pdf_path)
                    for page_number in range(len(pdf_document)):
                        page = pdf_document.load_page(page_number)
                        pix = page.get_pixmap()
                        img_bytes = pix.tobytes("ppm")
                        image = Image.open(io.BytesIO(img_bytes))
                        text = pytesseract.image_to_string(image, lang='eng')
                        out_file.write(text)
                    pdf_document.close()

pdf_to_text_with_ocr_recursive('/Users/farshid/Library/CloudStorage/OneDrive-Personal/Personal/9_Reference/farshid', 'output_text_file.txt')