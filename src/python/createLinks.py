root_directory = '/Users/farshid/farshid/pirahansiah.github.io/site'


import os
import re

def find_md_files(root_dir, exclude='links.md'):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md') and not file == exclude:
                yield os.path.join(root, file)

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                # Extract the first Markdown header line as the title
                return re.sub(r'^#+\s*', '', line)
    return "Untitled"

def file_path_to_html_link(file_path, root_dir):
    relative_path = os.path.relpath(file_path, root_dir)
    html_path = relative_path[:-3] + '.html'  # Replace .md with .html
    return f"https://pirahansiah.com/pages/{html_path.replace(os.sep, '/')}"

def generate_sitemap(md_files, root_dir):
    sitemap = []
    for md_file in sorted(md_files):
        title = extract_title(md_file)
        link = file_path_to_html_link(md_file, root_dir)
        depth = md_file.count(os.sep) - root_dir.count(os.sep)
        sitemap.append((depth, title, link))
    return sitemap

def pretty_print_hierarchy(sitemap, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for depth, title, link in sitemap:
            indent = '    ' * depth
            file.write(f"{indent}- [{title}]({link})\n")

if __name__ == "__main__":
    print('farshid')
    
    # output_file = os.path.join(root_directory, 'links.md')

    # md_files = list(find_md_files(root_directory))
    # print(f"Found {len(md_files)} Markdown files.")

    # sitemap = generate_sitemap(md_files, root_directory)
    # pretty_print_hierarchy(sitemap, output_file)

    # print(f"Sitemap generated in {output_file}.")
