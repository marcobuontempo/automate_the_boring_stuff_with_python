#! python3
# photo_folder_finder.py - Identifies "photo" folders, by scanning every folder on the hard drive.

# Definition of a "photo" folder, in this program:
#   - Contains photos with a minimum resolution of 500px * 500px
#   - Have .png / .jpg / .jpeg file format
#   - At least half of all the files in the folder are photo images


import os
from PIL import Image

for foldername, subfolders, filenames in os.walk("/"):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            num_non_photo_files += 1
            continue    # skip to next filename

        # Open image using Pillow
        image = Image.open(os.path.join(foldername, filename))
        width, height = image.size

        # Check if width & height are larger than 500
        if width >= 500 and height >= 500:
            # Image is large enough to be considered a photo
            num_photo_files += 1
        else:
            # Image is too small to be a photo
            num_non_photo_files += 1

    # If more than half of files were photos, print the absolute path of the folder
    if num_photo_files >= num_non_photo_files:
        print(os.path.abspath(foldername))
