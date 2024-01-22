root_dir = 'src/books/goal'
combined_md_file = 'src/books/goal/temp_combined.md'
output_pdf = 'src/books/goal/output.pdf'


import os
import markdown2
from weasyprint import HTML

def collect_markdown_files(root_dir):
    """Collects all markdown files from root_dir and its subdirectories."""
    markdown_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in sorted(files):
            if file.endswith('.md'):
                markdown_files.append(os.path.join(subdir, file))
    return markdown_files

def convert_md_to_pdf(markdown_files, output_pdf):
    """Converts a list of markdown files to a single PDF."""
    combined_html = ''
    for md_file in markdown_files:
        with open(md_file, 'r') as file:
            md_content = file.read()
            html_content = markdown2.markdown(md_content)
            combined_html += html_content

    HTML(string=combined_html).write_pdf(output_pdf)


# Collect all Markdown files
markdown_files = collect_markdown_files(root_dir)

# Create a single PDF from all Markdown files
convert_md_to_pdf(markdown_files, output_pdf)
