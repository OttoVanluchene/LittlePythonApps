import os
import random
import subprocess

# Select a random file from a directory and its subdirectories
# and reveal it in the explorer.exe
# You can change the directory on line 26.

def get_all_files(dir_path):
    # Get all the files in the directory and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

def open_file_and_explorer(file_path):

    # Open the explorer.exe with the file selected
    subprocess.run(["explorer.exe", "/select,", file_path], check=True)

# Get all the files in the directory and its subdirectories
all_files = get_all_files(r"E:\OneDrive")
print(len(all_files))

# Select a random file
random_file = random.choice(all_files)
print(random_file)

# Open the file and explorer.exe
try:
    open_file_and_explorer(random_file)
except FileNotFoundError as e:
    print("File not found:", e)

