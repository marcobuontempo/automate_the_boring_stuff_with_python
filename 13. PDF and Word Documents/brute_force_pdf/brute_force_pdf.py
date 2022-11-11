#! python3
# brute_force_pdf.py - Uses all the words stored in 'dictionary.txt' to brute force and open an encrypted PDF file
# Usage: python3 pdf_paranoia.py [filename_to_decrypt.pdf]

import sys
import PyPDF2

# verify correct usage
if len(sys.argv) != 2:
    print("Usage: python3 pdf_paranoia.py [filename_to_decrypt.pdf]")
    sys.exit()

# initialise pdf reader
filename = sys.argv[1]
pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))

# exit program if file is not encrypted
if pdf_reader.isEncrypted == False:
    print("File is not encrypted.")
    sys.exit()

# tests the lowercase/uppercase variation of each password in dictionary. Returns True if decryption is successful
def try_decrypt(password):
    try:
        if pdf_reader.decrypt(password.upper()):
            return True
        elif pdf_reader.decrypt(password.lower()):
            return True
        else:
            raise Exception
    except:
        return False


# store passwords into list, and remove any \n characters in the process
passwords = [password.strip()
             for password in open("dictionary.txt", "r").readlines()]

# attempt each password to decrypt
print("Brute forcing...")
for password in passwords:
    if try_decrypt(password) == True:
        print("Password found:", password.lower(), "or", password.upper())
        # copy contents of PDF if decryption is successful, and output to '<filename>_decrypted.pdf'
        pdf_writer = PyPDF2.PdfFileWriter()
        decrypted_file = open(filename.replace(".pdf", "_decrypted.pdf"), "wb")
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        pdf_writer.write(decrypted_file)
        decrypted_file.close()
        print("File successfully decrypted and copied to new file. Check:",
              f"'{filename}'")
        sys.exit()

# If unsuccessful decryption...
print("File could not be decrypted - No matching passwords in 'dictionary.txt'")
