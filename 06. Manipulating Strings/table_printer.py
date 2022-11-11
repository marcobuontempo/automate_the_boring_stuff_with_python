#! python3
# table_printer.py - prints a list-of-lists (with equal sized inner lists) to the terminal, with each column vertically aligned and justified-right

def print_table(table_data):
    col_widths = [0] * len(table_data)
    n_col = len(table_data[0])
    n_row = len(table_data)

    for i in range(n_row):
        for j in range(n_col):
            string = table_data[i][j]
            if len(string) > col_widths[i]:
                col_widths[i] = len(string)

    for j in range(n_col):
        row_output = ""
        for i in range(n_row):
            word = table_data[i][j]
            row_output += word.rjust(col_widths[i]) + " "
        print(row_output)


input_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]

print_table(input_data)
