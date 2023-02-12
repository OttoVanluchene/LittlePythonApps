import os
import re

# Removes the prefix from the filename and renames the file.
# Many cameras use the prefix IMG- or IMG_ for photos and
# VID- or VID_ for videos. This script removes the prefix.
# So for most the date is the first part of the filename.

def rename_files(directory, prefix, new_prefix):
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            new_filename = re.sub(f"^{prefix}", new_prefix, filename)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            count += 1
    return count

img_count = rename_files(".", "IMG-", "")
img2_count = rename_files(".", "IMG_", "")
vid_count = rename_files(".", "VID-", "")
vid2_count = rename_files(".", "VID_", "")

print(f"{img_count} IMG files renamed.")
print(f"{img2_count} IMG2 files renamed.")
print(f"{vid_count} VID files renamed.")
print(f"{vid2_count} VID2 files renamed.")

input("Press Enter to exit...")