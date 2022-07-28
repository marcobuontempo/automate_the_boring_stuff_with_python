#! /usr/bin/env python3
# delete_unneeded_files.py - Lists all files that are over 100MB in size
# Usage: python3 delete_unneeded_files.py [path_to_folder_to_search]


import sys, os, send2trash

if len(sys.argv) < 2:
    print("Usage: python3 delete_unneeded_files.py [path_to_folder_to_search]")
    sys.exit()

# get folder to search
folder = os.path.abspath(sys.argv[1])

# store paths to large files
file_index = 1
large_files = {}

# traverse folder and store all paths to files that are above 100MB
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        path = os.path.join(foldername,filename)
        size = round(os.path.getsize(path)/1000000, 2)
        if size > 100:
            large_files[str(file_index)] = {"path": path, "size": str(size)+"MB"}
            file_index += 1

# print all files over 100MB to terminal
if len(large_files) == 0:
    print("No files >100MB found")
    sys.exit()
print("\n   FILES FOUND >100MB:")
for key in large_files:
    print(f"     [{key}] -", os.path.basename(large_files[key]["path"]), "-", large_files[key]["size"])
print("\n")

# request deletion of a file in list
delete_file = input("Type a number to delete file, or type 'Q' to quit:\n")
if delete_file.upper() == "Q":
    sys.exit()
else:
    delete_obj = large_files.get(delete_file)
    if delete_obj is not None:
        # confirm deletion and send to trash
        filename_to_delete = os.path.basename(delete_obj["path"])
        confirm_deletion = input(f"Are you sure you want to delete {filename_to_delete}? (Y/N)\n")
        if confirm_deletion.upper() == "Y":
            print(f"Sending {filename_to_delete} to trash...")
            send2trash.send2trash(delete_obj["path"])
        else:
            print("Exiting program...")
            sys.exit()
    else:
        print("Not a valid number to delete")
        sys.exit()