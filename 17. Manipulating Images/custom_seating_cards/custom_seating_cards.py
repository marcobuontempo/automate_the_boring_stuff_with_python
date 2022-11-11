#! python3
# custom_seating_cards.py - Generates image files of custom seating cards, for each guest in "guests.txt" file


import sys
import os
from PIL import Image, ImageDraw, ImageFont

# 4inch * 5inch cards  =  288px * 360px (as PIL uses 72ppi)
CARD_WIDTH = 288
CARD_HEIGHT = 360

# populate list of guest names
guest_names = []
try:
    guest_file = open("guests.txt")
    guest_names = guest_file.readlines()
except:
    # exit if error loading names
    print("Error: 'guests.txt' does not exist in current directory or was unable to load")
    sys.exit()

# Create directory to store generated card images
os.makedirs("custom_cards", exist_ok=True)

# Import the decoration image and resize
decoration_image = Image.open("catlogo.png")
decoration_width, decoration_height = decoration_image.size
decoration_image = decoration_image.resize(
    (int(decoration_width/decoration_height) * CARD_WIDTH, CARD_HEIGHT))

# Create card for each guest
for guest_name in guest_names:
    guest_name = guest_name.strip()  # remove \n from name
    image = Image.new("RGBA", (CARD_WIDTH, CARD_HEIGHT),
                      "white")    # Create new blank image
    # Paste decoration image as background
    image.paste(decoration_image, mask=decoration_image)
    # Create ImageDraw object to allow for custom text drawings
    draw = ImageDraw.Draw(image)

    # Draw guest name
    ttf_font = ImageFont.truetype("/Microsoft/Arial.ttf", 32)
    name_width, name_height = draw.textbbox((0, 0), guest_name, ttf_font)[2:]
    draw.text(((CARD_WIDTH - name_width) / 2, (CARD_HEIGHT - name_height) / 2),
              guest_name, fill="purple", font=ttf_font, stroke_width=2, stroke_fill="white")

    # Draw welcome text
    welcome_text = "Welcome to dinner!"
    ttf_font = ImageFont.truetype("/Microsoft/Arial.ttf", 24)
    welcome_width, welcome_height = draw.textbbox(
        (0, 0), welcome_text, ttf_font)[2:]
    draw.text(((CARD_WIDTH - welcome_width) / 2, ((CARD_HEIGHT - name_height) / 2) - welcome_height - 10),
              welcome_text, fill="cornflowerblue", font=ttf_font, stroke_width=1, stroke_fill="white")

    # Draw end text
    end_text = "Enjoy :)"
    end_width, end_height = draw.textbbox((0, 0), end_text, ttf_font)[2:]
    draw.text(((CARD_WIDTH - end_width) / 2, CARD_HEIGHT - end_height - 20), end_text,
              fill="cadetblue", font=ttf_font, stroke_width=1, stroke_fill="white")

    # Add border
    draw.rectangle((0, 0, CARD_WIDTH-1, CARD_HEIGHT-1),
                   outline="green", width=5)
    draw.rectangle((0, 0, CARD_WIDTH-1, CARD_HEIGHT-1),
                   outline="black", width=2)

    # TODO fix filename format (no . " " or __)
    image.save(os.path.join("custom_cards", guest_name.lower().replace(
        ".", "_").replace(" ", "_").replace("__", "_") + "_card.png"))
