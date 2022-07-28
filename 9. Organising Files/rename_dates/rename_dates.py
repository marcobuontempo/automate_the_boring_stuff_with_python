#! /usr/bin/env python3
# rename_dates.py - renames all files in the current directory 
# from American dates (MM-DD-YYYY) to European dates (DD-MM-YYYY)

import os, shutil, re

# regex to match American date format
date_regex = re.compile(r"""^(.*?)          # all text before the date
                        ((0|1)?\d)-         # one or two digits for the month
                        ((0|1|2|3)?\d)-     # one or two digits for the day
                        ((19|20)\d\d)       # four digits for the year
                        (.*?)$              # all text after the date
                        """, re.VERBOSE)


# loop over files in the working directory
for filename in os.listdir("."):
    match = date_regex.search(filename)

    # skip files without date
    if match == None:
        continue

    # get different parts of the filename
    before_part = match.group(1)
    month_part = match.group(2)
    day_part = match.group(4)
    year_part = match.group(6)
    after_part = match.group(8)

    # create European-formatted date
    new_filename = before_part + day_part + "-" + month_part + "-" + year_part + after_part

    # get the full, absolute file paths
    abs_working_dir = os.path.abspath(".")
    filename = os.path.join(abs_working_dir, filename)
    new_filename = os.path.join(abs_working_dir, new_filename)

    # rename the files
    # print("\nRenaming '%s' to '%s'..." % (filename, new_filename))
    shutil.move(filename, new_filename)