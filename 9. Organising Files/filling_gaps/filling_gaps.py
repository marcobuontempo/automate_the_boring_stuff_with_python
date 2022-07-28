#! /usr/bin/env python3
# filling_gaps.py - Closes the numbering gap between files, or insert a gap to add a new numbered file

# Closing Gap: 
    # python3 filling_gaps.py close
    # e.g. spam001.txt, spam003.txt and spam004.txt - renames spam003.txt->spam002.txt, spam004.txt->spam003.txt
# Adding Gap: 
    # python3 filling_gaps.py add [number_to_add_gap]
    # e.g. spam001.txt, spam002.txt, and spam003.txt - (if adding gap at number 1) renames spam002.txt->spam003.txt, spam003.txt->spam004.txt


import os, re, shutil


def get_sorted_matches(folder):
    """Finds all regex matches in folder and sorts in order of suffix number in filename"""

    # store all match objects in dictionary
    match_objs = {}

    # check through files and find matches
    for filename in os.listdir(folder):
        match = file_regex.search(filename)
        if match == None:
            continue
        match_objs[match.group(2)] = match

    # sort the matches and store into list
    matches = []
    for key in sorted(match_objs):
        matches.append(match_objs[key])

    # exit if no matches found
    if len(matches) == 0:
        return None
    # return the list of sorted matches
    return matches


def close_gaps(folder):
    """Closes the gaps in numbered files"""

    matches = get_sorted_matches(folder)    # find all matches

    # find the longest number - used to figure out leading 0's in filename
    num_len = 0
    for match in matches:
        num = len(match.group(2))
        if num > num_len:
            num_len = num

    last_num = int(matches[0].group(2)) + 1     # initialise numbering system at first number found + 1

    for i in range(1, len(matches)):    # starts at 2nd item (as first item won't be renamed)
        match = matches[i]
        old_file = os.path.join(folder, f"{match.group(1)}{match.group(2)}{match.group(3)}")    # old file path

        zeroes = "0" * (num_len - len(str(last_num)))   # get prefix 0's for the numbering (i.e. 001 instead of 1)
        new_num = zeroes + str(last_num)    # new number

        new_file = os.path.join(folder, f"{match.group(1)}{new_num}{match.group(3)}")   # new file path
        
        shutil.move(old_file, new_file) # rename file
    
        last_num += 1   # update number for next file



def add_gap(folder, skip_num):
    """Adds a gap in the numbering of files"""
    
    close_gaps(folder)  # close any gaps in numbering to ensure neat format
    
    matches = get_sorted_matches(folder)    # find all matches

    # find the longest number - used to figure out leading 0's in filename
    num_len = 0
    for match in matches:
        num = len(match.group(2))
        if num > num_len:
            num_len = num

    # shorten the list of matches, to only include filenames AFTER the specified number to skip
    spliced = False
    for match in matches:    
        if int(match.group(2)) >= skip_num:
            matches = matches[matches.index(match):]
            matches.reverse()   # reverse matches as we will rename files starting with the largest number suffix 
                                # (otherwise we may overwrite existing files e.g. spam003.txt -> spam004.txt will overwrite spam004.txt if it already exists)
            spliced = True
            break
    if spliced == False:    # end function if number to skip is out of the current numbering range
        return
            
    # calculate the last number to use for the filenames
    last_num = skip_num + len(matches)

    for i in range(0, len(matches)):    # go through all matches we need to change
        match = matches[i]
        old_file = os.path.join(folder, f"{match.group(1)}{match.group(2)}{match.group(3)}")    # old file path

        zeroes = "0" * (num_len - len(str(last_num)))   # get prefix 0's for the numbering (i.e. 001 instead of 1)
        new_num = zeroes + str(last_num)    # new number

        new_file = os.path.join(folder, f"{match.group(1)}{new_num}{match.group(3)}")   # new file path
        
        shutil.move(old_file, new_file) # rename file
    
        last_num -= 1   # update number for next file



# get folder to search
folder_inp = os.path.abspath(input("Enter the absolute path to search:\n"))
# get prefix to search
prefix = input("Enter the file prefix to match (not including the numbers themselves):\n")
file_regex = re.compile(rf"({prefix})(\d+)(\..+)")
# find function to perform
close_or_add = input("Do you want to close gaps, or add a gap? [close | add]\n")
# perform necessary function
if close_or_add.lower() == "close":
    close_gaps(folder_inp)
elif close_or_add.lower() == "add":
    skip_inp = int(input("What number do you want to skip?\n"))
    add_gap(folder_inp,skip_inp)