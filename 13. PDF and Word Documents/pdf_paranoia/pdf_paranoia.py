#! python3
# pdf_paranoia.py - Goes through every PDF in a folder and encrypts them using a password provided on the command line. Deletes the original unencrypted files.
# Usage: python3 pdf_paranoia.py [password_for_encrpytion]

import os
import sys
import PyPDF2

# verify correct usage
if len(sys.argv) != 2:
    print("Usage: python3 pdf_paranoia.py [password_for_encrpytion]")
    sys.exit()

# get user defined password for encryption from command-line input
password = sys.argv[1]

# initialise array to store names of files that failed to encrypt
files_failed = []

# find all .pdf files
for foldername, subfolders, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith('.pdf'):
            # open file
            path = os.path.join(foldername, filename)
            pdf_file_obj = open(filename, 'rb')
            try:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
                if pdf_reader.isEncrypted == False:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    # copy file to new pdf document
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    # encrypt new pdf document
                    pdf_writer.encrypt(password)
                    # update the new file with "_encrypted.pdf" extension
                    encrypted_path = path.replace(".pdf", "_encrypted.pdf")
                    encrypted_file = open(encrypted_path, "wb")
                    pdf_writer.write(encrypted_file)
                    encrypted_file.close()
                    # verify file was encrypted
                    pdf_reader = PyPDF2.PdfFileReader(
                        open(encrypted_path, "rb"))
                    if pdf_reader.isEncrypted == True and pdf_reader.decrypt(password):
                        os.remove(path)
                        pass
                    else:
                        os.remove(encrypted_path)
                        raise Exception
            except:
                # if encryption process failed, add to list of failed files
                files_failed.append(filename)

# notify user of fail/success
if len(files_failed) > 0:
    print("Failed encryption operation for the following files:")
    for filename in files_failed:
        print("-", filename)
    print("All other files have been successfully encrypted.")
else:
    print("Encryption and deletion process has been successfully completed.")
