import os
import re
def search_files(root_path, file_extension, search_sentence):
    if re.search(r'\W', search_sentence):
        search_sentence = re.escape(search_sentence)
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file_extension:
                if not file.endswith(file_extension):
                    continue
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()
                for line in content:
                    if re.search(search_sentence, line):
                        print(f"Found in {filepath}: {line.strip()}")
root_path = input("Enter the root path (leave empty for current path): ")
file_extension = input("Enter the file extension (leave empty for all files): ")
search_sentence = input("Enter the search sentence: ")
if not root_path:
    root_path = "."
search_files(root_path, file_extension, search_sentence)