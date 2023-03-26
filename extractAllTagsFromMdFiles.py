import os
import re

# Extract all tags from all markdown files from current folder and all subfolders, nested tags supported.
# Output is an new markdown file with all tags sorted from a-z.

def find_markdown_files(path):
    markdown_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))

    return markdown_files

def extract_tags_from_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
    tags = re.findall(r'(?:\s|^)#([\w/]+)', content)
    return tags

def main():
    current_directory = os.getcwd()
    markdown_files = find_markdown_files(current_directory)
    
    # Print length of markdown files
    print("Number of markdown files:" + str(len(markdown_files)))

    all_tags = set()
    for file in markdown_files:
        tags = extract_tags_from_file(file)
        # Print the tags of the file
        print(tags)
        all_tags.update(tags)

    # Print length of all tags
    print("Number of tags:" + str(len(all_tags)))

    # Remove tags that start with a number or match a HEX pattern
    hex_pattern = re.compile(r'^[0-9A-Fa-f]+(?:/[0-9A-Fa-f]+)*$')
    cleaned_tags = [tag for tag in all_tags if not (tag[0].isdigit() or hex_pattern.match(tag))]
    
    # Sort the tags
    sorted_tags = sorted(cleaned_tags)

    with open("alltags.md", "w", encoding="utf-8") as output_file:
        for tag in sorted_tags:
            output_file.write(f"#{tag}\n")

if __name__ == "__main__":
    main()
