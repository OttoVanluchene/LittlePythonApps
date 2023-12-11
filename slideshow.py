# Starts a fullscreen slideshow, 10 sec rotation, random shuffle, esc to close, arrow keys to navigate manually
# Place the script in directory you want see the slideshow, all pictures will be fetched also from sibfolders.
# Clicking on a picture will open it in explorer (windows only)

import os
import random
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

def open_in_explorer(event):
    global image_index, images
    try:
        if os.name == 'nt':  # for Windows
            subprocess.run(['explorer', '/select,', images[image_index]])
    except Exception as e:
        print(f"Failed to open image in explorer: {e}")

def find_images(directory):
    extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                yield os.path.join(root, file)

def update_image(step=1):
    global image_index, image_label, root, images, after_id
    image_index = (image_index + step) % len(images)
    img = Image.open(images[image_index])
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    if screen_width > 0 and screen_height > 0:
        img_width, img_height = img.size

        ratio = min(screen_width / img_width, screen_height / img_height)
        new_size = (int(img_width * ratio), int(img_height * ratio))

        img = img.resize(new_size, Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

    if after_id is not None:
        root.after_cancel(after_id)
    after_id = root.after(10000, update_image)

def previous_image(event):
    update_image(-1)

def next_image(event):
    update_image(1)

def exit_slideshow(event):  # event is not used, but required by Tkinter
    global root
    root.destroy()


# Main script
directory = '.'
images = list(find_images(directory))
random.shuffle(images)

if images:
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    root.bind('<Escape>', exit_slideshow)
    root.bind('<Left>', previous_image)
    root.bind('<Right>', next_image)

    image_label = tk.Label(root)
    image_label.pack(fill=tk.BOTH, expand=True)
    image_index = -1
    image_label.bind('<Button-1>', open_in_explorer)
    
    after_id = root.after(100, update_image)
    root.mainloop()
else:
    print("No images found in the directory.")
