root_dir = 'src/books/goal'
#root_dir = '/Users/farshid/code/__!myWork/2024/github/pirahansiah.github.io/src/books/goal'
combined_md_file = 'src/books/goal/temp_combined.md'
output_pdf = 'src/books/goal/output.pdf'

import os
import markdown2
from weasyprint import HTML

def collect_folders_with_md_files(root_dir):
    """Collects folders that contain markdown files."""
    folders = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                folders.append(subdir)
                break
    return folders

def convert_md_to_pdf_with_images(folders, output_pdf):
    """Converts markdown files to a single PDF, including images at the start and end of each md file."""
    combined_html = ''
    for folder in folders:
        md_files = [f for f in os.listdir(folder) if f.endswith('.md')]
        image_files = [f for f in os.listdir(folder) if f.endswith(('.png'))]

        if md_files and len(image_files) >= 2:
            # Assuming the first two images are the start and end images
            start_image, end_image = image_files[:2]

            # Add start image
            combined_html += f'<img src="{os.path.join(folder, start_image)}">'

            # Add Markdown content
            with open(os.path.join(folder, md_files[0]), 'r') as file:
                md_content = file.read()
                html_content = markdown2.markdown(md_content)
                combined_html += html_content

            # Add end image
            combined_html += f'<img src="{os.path.join(folder, end_image)}">'

    # Convert the combined HTML to PDF
    HTML(string=combined_html, base_url=root_dir).write_pdf(output_pdf)

# Collect folders with Markdown files
folders = collect_folders_with_md_files(root_dir)

# Create a single PDF from all Markdown files, including start and end images for each
convert_md_to_pdf_with_images(folders, output_pdf)
