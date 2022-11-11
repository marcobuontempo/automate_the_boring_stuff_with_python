#! python3
# selective_copy.py - Copies all files within the folder tree of a specified directory,
# that match a specified file format (e.g. ".pdf")

import os
import re
import shutil

# Get inputs from user
folder = os.path.abspath(input("Please enter folder location:\n"))
file_type = input(
    "Enter the file extension type to copy: (e.g. txt, pdf, jpg, etc.)\n")

# Regex to match file extension specified
file_regex = re.compile(rf"(.{file_type})$")

# Create new folder
folder_number = 1
while True:
    copy_folder_name = os.path.basename(
        folder) + "_" + file_type + "_" + str(folder_number)
    if not os.path.exists(copy_folder_name):
        break
    folder_number += 1
new_folder = os.path.join(os.path.dirname(folder), copy_folder_name)
os.mkdir(new_folder)

# Traverse folder structure and copy any files that have the specified extension, to the newly created folder
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if file_regex.search(filename) != None:
            path_from = os.path.join(foldername, filename)
            new_filename = os.path.basename(foldername) + "_" + filename
            path_to = os.path.join(new_folder, new_filename)
            shutil.copy(path_from, path_to)
