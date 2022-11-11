#! python3
# strong_password_detection.py - Detects whether a password is strong (8+ characters, contains 1+ uppercase, 1+ lowercase, and 1+ digit)

import re
import sys

if len(sys.argv) < 2:
    print("\nUsage: python strong_password_detection.py <password> - determines password strength\n")
    sys.exit()

# regex to match requirements
pwd_len = re.compile(r".{8,}")      # 8+ characters
pwd_lower = re.compile(r"[a-z]+")   # 1+ lowercase
pwd_upper = re.compile(r"[A-Z]+")   # 1+ uppercase
pwd_digit = re.compile(r"[0-9]+")   # 1+ digit

# get password from command-line argument
pwd = sys.argv[1]

# validate whether all regex are matched


def password_strength(password):
    if pwd_len.search(password) == None:
        return False
    if pwd_lower.search(password) == None:
        return False
    if pwd_upper.search(password) == None:
        return False
    if pwd_digit.search(password) == None:
        return False
    return True


# output to user whether password is strong
if password_strength(pwd):
    print("\nPassword is strong!\n")
else:
    print("\nWeak password! Use at least 8 characters, including 1+ lowercase, 1+ uppercase, and 1+ digit\n")
