#! python3
# multiclipboard.py - saves and loads pieces of text to the clipboard
# Usage: py.exe multiclipboard.pyw save <keyword> - saves clipboard to keyword
#        py.exe multiclipboard.pyw <keyword> - loads keyword to clipboard
#        py.exe multiclipboard.pyw delete <keyword> - deletes keyword and contents
#        py.exe multiclipboard.pyw delete all - deletes all contents saved in multiclipboard
#        py.exe multiclipboard.pyw - loads all keywords to clipboard

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open("mcb")

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        # save clipboard content to keyword
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        if sys.argv[2].lower() in mcb_shelf:    # delete keyword
            del mcb_shelf[sys.argv[2]]
        elif sys.argv[2].lower() == "all":  # delete all keywords
            for key in mcb_shelf:
                del mcb_shelf[key]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":   # list keywords
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:  # load content
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
