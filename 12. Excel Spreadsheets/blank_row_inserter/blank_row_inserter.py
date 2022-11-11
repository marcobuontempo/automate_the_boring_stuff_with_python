#! python3
# blank_row_inserter.py - inserts N number of rows starting at row index M
# Usage: python3 blank_row_inserter.py [N-index] [M-rows] [filename]

import openpyxl
import sys

# Validate usage and setup workbook to operate on
try:
    if len(sys.argv) != 4:
        raise Exception
    N = int(sys.argv[1])
    M = int(sys.argv[2])

    wb = openpyxl.load_workbook(sys.argv[3])
    sheet = wb.active
except:
    print(
        "Incorrect command-line arguments.\nUsage: python3 blank_row_inserter.py [N-index] [M-rows] [filename]\n")

# Insert Blank Rows
sheet.insert_rows(N, M)

# Save File
new_filename = sys.argv[3][0].upper() + sys.argv[3][1:]
wb.save(f"updated{new_filename}")
