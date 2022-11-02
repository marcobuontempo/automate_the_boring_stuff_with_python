#! python3
# excel_to_csv.py - Converts all .xlsx files in current directory to .csv files (note: each workbook sheet is output as a separate file)


# use openpyxl module
# read all excel files and export as csv
# create 1 csv per sheet
# filename should be <excel filename>_<sheet title>.csv

import os, openpyxl

for excel_file in os.listdir("."):
    # Skip non-xlsx files, load the workbook object
    if not excel_file.endswith(".xlsx"):
        continue
    
    wb = openpyxl.load_workbook(excel_file)
    # Loop through every sheet in workbook
    for sheet_name in wb.get_sheet_names():
        
        # Create the CSV filename from the Excel filename and sheet title
        # Create the csv.writer object for this CSV file

        # Loop through every row in the sheet
        for row_num in range(1, sheet.max_row + 1):
            row_data = []   # append each call to this list
            # Loop through each cell in the row
            for col_num in range(1, sheet.max_column + 1):
                # Append each cell's data to row_data

            # Write the row_data list to the CSV file

        csv_file.close()