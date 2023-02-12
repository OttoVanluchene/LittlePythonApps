import json
import os
import re

# Bookmarks to JSON Extension for Chrome used to export bookmarks

# Open the JSON file and parse the content
with open('bookmarks.json', 'r', encoding='utf-8') as bookmarks:
    data = json.load(bookmarks)

# Create the "bookmarks" folder if it does not exist
if not os.path.exists('bookmarks'):
    os.makedirs('bookmarks')

# Clean the name of the bookmark to make it a valid file name
def clean_name(name):
    # Replace reserved characters with an space
    name = re.sub(r'[\/\\:*?"<>|]', ' ', name)

    # Remove leading and trailing whitespace
    name = name.strip()

    # Replace consecutive whitespace characters with a single space
    name = re.sub(r'\s+', ' ', name)

    # Truncate the string if it is too long
    if len(name) > 255:
        name = name[:255]

    return name

# Iterate through the list of objects
index = 0
for item in data:
    # Extract the name and url properties
    name = clean_name(item['name'])
    url = item['url']  

    print(index)

    # Create the Markdown template string
    template = f'#note/bookmark\n\nURL: {url}'

    # Write the template string to a file in the folder bookmarks
    with open(f'bookmarks/{name}.md', 'w', encoding='utf-8') as file:
        file.write(template)

    index += 1