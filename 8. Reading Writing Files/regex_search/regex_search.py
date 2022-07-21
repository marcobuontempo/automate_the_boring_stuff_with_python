#! /usr/bin/env python3
# regex_search.py - opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression
# prints results to screen

import re, os

folder = os.path.abspath(input("Enter the path of the folder:\n"))  # get user input of file path
all_files = os.listdir(folder)  # get a list of all files in the directory
file_regex = re.compile(r"(.txt)$") # regex pattern to match files ending in .txt
text_files = [] # a list to store any found text files

user_exp = input("Enter your regular expression:\n")
user_regex = re.compile(rf"{user_exp}") # store the user defined regex

# find all text files in directory
for file in all_files:
    if file_regex.search(file):
        text_files.append(file)

for file in text_files:
    text_file = open(os.path.join(folder, file))    # open each text file
    string = text_file.read()   # read each text file
    matches = user_regex.findall(string)    # find all matches with user's regex
    print("File: ",file,"\n"," ".join(matches)) # print all matches in file
    text_file.close()   # close file