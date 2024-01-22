root_dir = 'src/books/goal'
#root_dir = '/Users/farshid/code/__!myWork/2024/github/pirahansiah.github.io/src/books/goal'
combined_md_file = 'src/books/goal/temp_combined.md'
output_pdf = 'src/books/goal/output.pdf'







import os
import markdown2
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def collect_markdown_files(root_dir):
    markdown_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in sorted(files):
            if file.endswith('.md'):
                markdown_files.append(os.path.join(subdir, file))
    return markdown_files

def extract_and_remove_images(html_content, folder):
    updated_html = html_content
    image_paths = []
    image_paths = re.findall(r'<img src="(.*?)"', html_content)
    img_tags = re.findall(r'<img src="(.*?)"', html_content)

    for img_tag in img_tags:
        full_path = os.path.join(folder, img_tag)
        if os.path.isfile(full_path):
            image_paths.append(full_path)
            updated_html = re.sub(r'<img src="{}"'.format(re.escape(img_tag)), '', updated_html, 1)
        else:
            print(f"Image file not found: {full_path}")
        



    return updated_html, image_paths

def convert_md_to_pdf_with_images(markdown_files, output_pdf):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    for md_file in markdown_files:
        folder = os.path.dirname(md_file)
        with open(md_file, 'r') as file:
            md_content = file.read()
            html_content = markdown2.markdown(md_content)

        updated_html, image_paths = extract_and_remove_images(html_content, folder)
        for image_path in image_paths:
            story.append(Image(image_path, width=400, height=200)) 
        story.append(Paragraph(updated_html, styles['Normal']))
        story.append(Spacer(1, 12))

    try:
        doc.build(story)
    except:
        doc.build(story) 


markdown_files = collect_markdown_files(root_dir)
convert_md_to_pdf_with_images(markdown_files, output_pdf)
