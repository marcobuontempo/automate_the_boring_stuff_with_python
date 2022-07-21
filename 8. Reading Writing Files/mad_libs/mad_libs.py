#! /usr/bin/env python3
# mad_libs.py - reads text files and prompts users to replace all occurrences of ADJECTIVE, NOUN, ADVERB, & VERB
# Prints results and saves output to new text file

import sys, os, re

if len(sys.argv) < 2:
    print("Usage: python mad_libs.py <./path_to_file.txt>")
    sys.exit()

text_file_path = os.path.abspath(sys.argv[1])
input_file = open(text_file_path, "r")
input_text = input_file.read()
input_file.close()

output_file = open("mad_libs.txt", "w")

madlib_regex = re.compile(r"(ADJECTIVE|NOUN|ADVERB|VERB)")
matches = madlib_regex.findall(input_text)

for match in matches:
    prompt = "Enter a"
    if match.upper()=="ADJECTIVE":
        prompt += "n"
    prompt += " " + match.lower() + ":\n"
    new_word = input(prompt)
    input_text = madlib_regex.sub(new_word, input_text, 1)

output_file.write(input_text)
output_file.close()

print(input_text)
