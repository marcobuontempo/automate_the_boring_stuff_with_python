#! /usr/bin/env python3
# password_locker.py - An insecure password locker program

PASSWORDS = {"email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
             "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
             "luggage": "12345"}

import sys, pyperclip
if len(sys.argv) < 2:   # ensure an argument is passed when running the program (1st arg = python file, 2nd arg = account name)
    print("Usage: python password_locker.py <account> - copy account password")
    sys.exit()

account = sys.argv[1]   # first command-line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for",account,"copied to clipboard")
else:
    print("There is not account named",account)
