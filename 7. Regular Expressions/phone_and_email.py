#! /usr/bin/env python3
# phone_and_email.py - Finds phone numbers and email addresses in the clipboard (using regex)

import pyperclip, re

# phone number regex
phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)""", re.VERBOSE)

# email address regex
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something
)""", re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    # join area code, first 3 digits, last 4 digits, extension - in a standard format
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# copy results to clipboard (and print to terminal)
if len(matches) > 0:
    output_text = "\n".join(matches)
    pyperclip.copy(output_text)
    print("Copied to clipboard:")
    print(output_text)
else:
    print("No phone numbers or email addresses found!")