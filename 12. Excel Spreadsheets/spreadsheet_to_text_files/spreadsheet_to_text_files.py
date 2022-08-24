#! python3
# spreadsheet_to_text_files.py - Converts a spreadsheet file to text files. Each column will output 
#                                as a seperate text file, and each row of that column will represent
#                                one line of the text file.
# Usage: spreadsheet_to_text_files.py [spreadsheet_name]

import sys, os, openpyxl

# Validate command-line usage
try:
    if len(sys.argv) != 2:
        raise Exception

    # Read file lines into dictionary
    file_contents = {}
    
    # Create workbook
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb.active

    # Option to use first row as file names
    while True:
        has_headers = input("Does the first row of the spreadsheet contain headers or the text file name? (Y/N)\n").upper()
        if has_headers=="Y" or has_headers=="N": break
    has_headers = True if has_headers=="Y" else False   

    # Create 'text_files' directory if it doesn't already exist
    if os.path.isdir("text_files")==False:
        os.makedirs("text_files")        

except Exception as e:
    print(f"\n{e}\nUsage: Usage: spreadsheet_to_text_files.py [spreadsheet_name]\n")



file_count = 0
for col_num in range(1, sheet.max_column+1):
    file_count += 1
    # Default filename if spreadsheet does not have headers, otherwise use first row as header
    file_name = f"text_file_{file_count}.txt" if has_headers==False else sheet.cell(row=1,column=col_num).value
    file = open(os.path.join("text_files",file_name), "w")
    for row_num in range(1, sheet.max_row+1):
        if has_headers==True and row_num==1: continue   # skip writing the first line if it is a header
        line = sheet.cell(row=row_num,column=col_num).value # get text from cell
        if line != None:
            file.write(line)    # write line to file
    file.close()