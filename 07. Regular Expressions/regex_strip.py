#! python3
# regex_strip.py [character_to_remove] - implements the same functionality as the .strip() method, but by using regex
# Note: if specified, surround the "character_to_remove" in quotes in the command-line (i.e. "*") for proper functionality

import sys
import re

remove = " "    # character to remove. default is whitespace
if len(sys.argv) > 1:   # update character to remove if specified in command-line argument
    arg = sys.argv[1]
    if len(arg) > 1:
        print("Only specify 1 character to strip")
        sys.exit()
    if re.match(r"\W", arg):
        remove = rf"\{arg}"  # escape the character if it isn't text/digit
    else:
        remove = arg


text = input("Enter text to strip: ")   # get user input for text to strip

# regex pattern to match any preceding or trailing characters to remove
strip_regex = re.compile(rf"^({remove}+)|({remove}+)$")

stripped_text = strip_regex.sub("", text)   # strip the input text

print("\n"+stripped_text+"\n")  # output the stripped text to user
