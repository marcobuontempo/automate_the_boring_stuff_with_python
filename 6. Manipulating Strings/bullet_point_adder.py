#! python3
# bullet_pointer_adder.py - Adds bullet points (*) to the start of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# separate lines and add stars
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = "* " + lines[i]  # adds a start to each string in the lines list
text = "\n".join(lines)
pyperclip.copy(text)
