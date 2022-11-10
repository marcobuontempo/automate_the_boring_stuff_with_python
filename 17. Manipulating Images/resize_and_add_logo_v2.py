#! python3
# resize_and_add_logo.py - Resizes all images in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right corner.

# V2 Changes:
#   - Additionally accepts BMP and GIF image formats
#   - Matches case-insensitive file extensions (e.g. .png or .PNG)
#   - Only adds logo if base image is 2x logo's height and width

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

# Load Logo Image
logo_image = Image.open(LOGO_FILENAME)
logo_image = logo_image.resize((80, int((logo_image.size[0]/logo_image.size[1]) * 80))) # Resize logo to 80px width
logo_width, logo_height = logo_image.size

os.makedirs("with_logo", exist_ok=True)

# Loop over all files in the working directory
for filename in os.listdir("."):
    if not ( filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")) ) or filename == LOGO_FILENAME:
        continue    # skip non-image files and the logo file itself

    image = Image.open(filename)
    width, height = image.size

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image
        print("Resizing %s..." % filename)
        image = image.resize((width, height))

    # Add the logo
    if width >= (logo_width*2) and height >= (logo_height*2):
        print("Adding logo to %s..." % filename)
        image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

    # Save the changes
    image.save(os.path.join("with_logo", filename))