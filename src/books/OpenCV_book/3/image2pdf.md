Convert images to PDF with Python! Using the FPDF library, this code creates a PDF from a folder of images. It sorts the images, adds each image as a page, and includes the filename as a caption. Try it now! #Python #PDF #ImageProcessing
Convert images to PDF with Python! Using the FPDF library, this code creates a PDF from a folder of images. It sorts the images, adds each image as a page, and includes the filename as a caption. Try it now! #Python #PDF #ImageProcessing

## convert image to video 
```python
#pip install fpdf
import os
from fpdf import FPDF
def create_pdf_from_images(image_folder, output_pdf):
    pdf = FPDF()
    image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        pdf.add_page()
        pdf.image(image_path)
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(0, 0, 0)
        pdf.cell(190, 10, os.path.basename(image_file), ln=True, align='C', fill=True)

    pdf.output(output_pdf)
image_folder = 'images'
output_pdf = 'images.pdf'
create_pdf_from_images(image_folder, output_pdf)
```

