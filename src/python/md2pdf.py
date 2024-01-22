import os
import subprocess

def collect_markdown_files(root_dir):
    """Collects all markdown files from root_dir and its subdirectories."""
    markdown_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(subdir, file))
    return markdown_files

def create_pdf_from_markdown(markdown_files, output_pdf):
    """Uses Pandoc to create a single PDF from a list of markdown files."""
    pandoc_command = ['pandoc', '-s'] + markdown_files + ['-o', output_pdf]
    subprocess.run(pandoc_command, check=True)

# Path to the root directory containing your Markdown files
root_dir = 'src/books/goal'

# Path for the output PDF
output_pdf = 'src/books/goal/output.pdf'

# Collect all Markdown files
markdown_files = collect_markdown_files(root_dir)

# Create a single PDF from all Markdown files
create_pdf_from_markdown(markdown_files, output_pdf)
